import json
from pathlib import Path

def analyze_openapi_coverage(config):
    # Try to find OpenAPI specification file
    """Analyze coverage of OpenAPI documentation.
    Parameters:
        - config (dict): A configuration dictionary containing paths and file names, with keys:
            - "openapi_path" (str, optional): Path to OpenAPI specification file. If not provided, the function will attempt to find it in the project root.
            - "project_root" (str): Path to the project root directory to search for OpenAPI specification files if not directly provided.
            - "report_dir" (str): Directory path to save the coverage report.
            - "api_doc_output" (str): Filename for saving the API documentation report.
    Returns:
        - dict: A dictionary containing analysis results, with keys as follows:
            - "total_endpoints" (int): Total number of endpoints discovered from the OpenAPI specification.
            - "documented" (int): Number of endpoints documented with a summary or description.
            - "undocumented" (int): Number of endpoints lacking sufficient documentation.
            - "coverage_percent" (float): Percentage of documented endpoints.
            - "undocumented_endpoints" (list of dict): List containing details of undocumented endpoints, each with:
                - "path" (str): Endpoint path.
                - "method" (str): HTTP method.
                - "operationId" (str, optional): Operation ID, if available.
    Processing Logic:
        - Attempts to locate the OpenAPI specification file using a predefined list of filenames in the project root directory.
        - Reads and parses the OpenAPI specification file using either YAML or JSON format, depending on the file extension.
        - Analyzes each endpoint for the presence of summary or description to evaluate documentation coverage.
        - Generates a JSON report of the documentation coverage results, and saves it to a specified directory and file.
        - Outputs results and coverage percentage to the console."""
    openapi_path = config.get("openapi_path")
    if not openapi_path:
        # Look for common OpenAPI file names in project root
        project_root = Path(config["project_root"])
        possible_files = [
            "openapi.json", "openapi.yaml", "openapi.yml",
            "swagger.json", "swagger.yaml", "swagger.yml",
            "api-docs.json", "api-spec.json"
        ]
        
        for filename in possible_files:
            potential_path = project_root / filename
            if potential_path.exists():
                openapi_path = str(potential_path)
                break
        
        if not openapi_path:
            print("❌ No OpenAPI specification file found. Looked for:")
            for filename in possible_files:
                print(f"   - {project_root / filename}")
            return {"error": "No OpenAPI specification file found"}
    
    report_file = Path(config["report_dir"]) / config["api_doc_output"]

    try:
        with open(openapi_path) as f:
            if openapi_path.endswith(('.yaml', '.yml')):
                import yaml
                spec = yaml.safe_load(f)
            else:
                spec = json.load(f)
    except FileNotFoundError:
        print(f"❌ OpenAPI file not found at {openapi_path}")
        return {"error": "OpenAPI file not found"}
    except Exception as e:
        print(f"❌ Error reading OpenAPI file: {str(e)}")
        return {"error": f"Error reading OpenAPI file: {str(e)}"}

    paths = spec.get("paths", {})
    undocumented = []
    total = 0

    for path, methods in paths.items():
        for method, details in methods.items():
            if method.lower() not in {"get", "post", "put", "delete", "patch", "options", "head"}:
                continue
            total += 1
            if not details.get("summary") and not details.get("description"):
                undocumented.append({
                    "path": path,
                    "method": method.upper(),
                    "operationId": details.get("operationId", "")
                })

    documented = total - len(undocumented)
    percent = round((documented / total) * 100, 2) if total else 100.0

    result = {
        "total_endpoints": total,
        "documented": documented,
        "undocumented": len(undocumented),
        "coverage_percent": percent,
        "undocumented_endpoints": undocumented
    }

    report_file.parent.mkdir(parents=True, exist_ok=True)
    with open(report_file, "w") as f:
        json.dump(result, f, indent=2)

    print(f"✅ API doc coverage complete: {percent}%")
    return result

