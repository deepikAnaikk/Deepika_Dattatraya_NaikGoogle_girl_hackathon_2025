# rtl-cld-predictor/src/feature_extractor.py
import pandas as pd
import networkx as nx
import ast #for very simplified rtl.
import os

def extract_graph_features(graph):
    """Extracts graph-based features from a networkx graph."""
    features = {}
    features["node_count"] = graph.number_of_nodes()
    features["edge_count"] = graph.number_of_edges()
    # Add more graph features as needed
    return features

def extract_operator_counts(rtl_code):
    """Extracts counts of operators from RTL code."""
    operator_counts = {"and": 0, "or": 0, "xor": 0, "add": 0, "sub": 0} #example
    # Implement your logic to count operators
    for op in operator_counts:
        operator_counts[op] = rtl_code.lower().count(op)
    return operator_counts

def extract_signal_types(rtl_code):
    """Extracts signal type counts from RTL code."""
    signal_types = {"wire": 0, "reg": 0, "input": 0, "output": 0}
    for signal in signal_types:
        signal_types[signal] = rtl_code.lower().count(signal)
    return signal_types

def extract_features_from_rtl_file(rtl_file_path):
    """Extracts all features from an RTL file."""
    with open(rtl_file_path, 'r') as file:
        rtl_code = file.read()
    features = {}
    features.update(extract_operator_counts(rtl_code))
    features.update(extract_signal_types(rtl_code))
    # Add other feature extraction functions here
    return features

def process_rtl_directory(rtl_dir):
    """Processes a directory of RTL files and returns a DataFrame."""
    all_features = []
    for filename in os.listdir(rtl_dir):
        if filename.endswith(".v"): #or other extensions
            rtl_file_path = os.path.join(rtl_dir, filename)
            features = extract_features_from_rtl_file(rtl_file_path)
            all_features.append(features)
    return pd.DataFrame(all_features)
