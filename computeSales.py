import sys
import json
import time


def load_json_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found: {filename}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file: {filename}")
        return None
    except Exception as e:  # pylint: disable=broad-except
        print(f"Error: An unexpected error occurred reading {filename}: {e}")
        return None





def main():

    start_time = time.time()

    if len(sys.argv) != 3:
        print(
            "Usage: python computeSales.py "
            "priceCatalogue.json salesRecord.json"
        )
        sys.exit(1)

    catalogue_file = sys.argv[1]
    sales_file = sys.argv[2]

    catalogue_data = load_json_file(catalogue_file)
    sales_data = load_json_file(sales_file)

    
if __name__ == "__main__":
    main()
