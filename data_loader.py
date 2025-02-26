# rtl-cld-predictor/src/data_loader.py
import pandas as pd
import os

def load_data(data_path="data/dataset.csv"):
    """Loads the dataset from a CSV file."""
    try:
        data = pd.read_csv(data_path)
        return data
    except FileNotFoundError:
        print(f"Error: Dataset not found at {data_path}")
        return None

def preprocess_data(data, features, label):
    """Preprocesses the data, separating features and labels."""
    if data is None:
        return None, None
    features_data = data[features]
    labels_data = data[label]
    return features_data, labels_data

# Example of loading from RTL and report files, and generating a dataset.csv
def generate_dataset(rtl_dir="data/rtl_designs", report_dir="data/synthesis_reports", output_path="data/dataset.csv"):
    """Generates a dataset CSV from RTL and synthesis report files."""
    data = []
    for filename in os.listdir(rtl_dir):
        if filename.endswith(".v"): # or other RTL extensions
            rtl_path = os.path.join(rtl_dir, filename)
            report_path = os.path.join(report_dir, filename.replace(".v", ".rpt")) # Adjust report extension
            try:
                # Example: Extract CLD from report (adapt to your report format)
                with open(report_path, 'r') as report_file:
                    report_content = report_file.read()
                    cld = extract_cld_from_report(report_content) # Implement this function
                # Example: Extract features from RTL (adapt to your feature extraction)
                features = extract_features_from_rtl(rtl_path) # Implement this function
                data.append({**features, "cld": cld}) #merge dicts

            except FileNotFoundError:
                print(f"Warning: Report not found for {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")
    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)
    return df

def extract_cld_from_report(report_content):
    """Implement this function to extract CLD from your synthesis reports."""
    # Example (adapt to your report format):
    if "max_combinational_path" in report_content:
        lines = report_content.split('\n')
        for line in lines:
            if "max_combinational_path" in line:
                cld = int(line.split(":")[1].strip())
                return cld
    return 0 # Or a default value

def extract_features_from_rtl(rtl_path):
    """Implement this function to extract features from your RTL files."""
    # Example (adapt to your feature extraction logic):
    features = {"fan_in": 0, "fan_out": 0, "lines_of_code": 0}
    with open(rtl_path, 'r') as rtl_file:
        rtl_content = rtl_file.read()
        features["lines_of_code"] = len(rtl_content.split('\n'))
        # Add logic to extract fan_in, fan_out, etc.
    return features
