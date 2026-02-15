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


def create_price_map(catalogue):

    price_map = {}
    if not isinstance(catalogue, list):
        print("Error: Invalid catalogue format. Expected a list.")
        return price_map

    for item in catalogue:
        if isinstance(item, dict) and 'title' in item and 'price' in item:
            price_map[item['title']] = item['price']
        else:
            print(f"Warning: Invalid item format in catalogue: {item}")
    return price_map


def compute_total_sales(price_map, sales_record):

    total_cost = 0.0

    if not isinstance(sales_record, list):
        print("Error: Invalid sales record format. Expected a list.")
        return total_cost

    for sale in sales_record:
        if not isinstance(sale, dict):
            print(f"Warning: Invalid sale record format: {sale}")
            continue

        product = sale.get('Product')
        quantity = sale.get('Quantity')

        if product is None or quantity is None:
            print(f"Warning: Missing product or quantity around: {sale}")
            continue

        if product not in price_map:
            print(f"Warning: Product '{product}' not found in catalogue.")
            continue

        try:
            quantity_val = float(quantity)
            price_val = float(price_map[product])
            total_cost += quantity_val * price_val
        except ValueError:
            print(f"Warning: Invalid value in sale or price: {sale}")

    return total_cost


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

    if catalogue_data is None or sales_data is None:
        sys.exit(1)

    price_map = create_price_map(catalogue_data)
    total_sales = compute_total_sales(price_map, sales_data)

    elapsed_time = time.time() - start_time

    # Format output
    output_lines = []
    output_lines.append("Sales Computation Results")
    output_lines.append("-------------------------")
    output_lines.append(f"Total Sales Cost: ${total_sales:,.2f}")
    output_lines.append(f"Time Elapsed: {elapsed_time:.6f} seconds")

    output_text = "\n".join(output_lines)

    # Print to console
    print(output_text)

    # Write to file
    try:
        with open("SalesResults.txt", "w", encoding='utf-8') as f:
            f.write(output_text)
    except Exception as e:  # pylint: disable=broad-except
        print(f"Error: Could not write to SalesResults.txt: {e}")


if __name__ == "__main__":
    main()
