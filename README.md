# Deepika_Dattatraya_NaikGoogle_girl_hackathon_2025
Solution for AI algorithm to predict combinational complexity/depth of signals to quickly identify timing violations. 
# RTL Combinational Logic Depth Predictor

## Description

This project implements a machine learning-based tool to predict the combinational logic depth (CLD) of signals in Register Transfer Level (RTL) designs. By analyzing RTL code and extracting relevant features, the tool estimates signal CLD, significantly reducing the need for lengthy synthesis runs. This enables faster design space exploration and early identification of timing bottlenecks.

## Environment Setup

1.  **Create a virtual environment:**
    ```bash
    conda create -n rtl-cld python=3.8  # Or python=3.x
    conda activate rtl-cld
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Synthesis Tool (if generating dataset):**
    * If you need to generate the dataset from RTL files and synthesis reports, ensure you have a logic synthesis tool (e.g., Synopsys Design Compiler, Cadence Genus) installed and configured.
    * Specific instructions for installing and configuring the synthesis tool are outside the scope of this README. Please refer to the tool's documentation.

## Running the Code

1.  **Data Preparation:**
    * Ensure your RTL files and corresponding synthesis reports are placed in the `data/rtl_designs/` and `data/synthesis_reports/` directories, respectively.
    * Run the data loader and feature extraction scripts to generate or update the `data/dataset.csv` file.
    * If you have a pre-generated dataset, simply place it in the `data/` folder.

2.  **Training and Evaluation:**
    * Execute the training script:
        ```bash
        python src/trainer.py
        ```
    * The `trainer.py` script will load the dataset, train the chosen machine learning model, and evaluate its performance.
    * The evaluation results (e.g., MSE, MAE, R-squared, run-time) will be printed to the console.

3.  **Generating the Dataset (if needed):**
    * If you need to create the dataset from scratch, you will need to adapt the data_loader.py and feature_extractor.py scripts to work with your synthesis tool, and report file formats.
    * Modify the scripts to parse your synthesis reports and extract the correct CLD values.
    * You will also need to modify the feature extractor to extract the needed features from your RTL files.

## Dataset Details

* **RTL Designs:** The dataset consists of [number] RTL designs written in [Verilog/VHDL/both]. The designs vary in complexity and functionality, representing a range of typical hardware designs.
* **Timing-Critical Signals:** Timing-critical signals were identified by [methodology, e.g., manual inspection of critical paths, signal naming conventions, or automated analysis of synthesis reports].
* **Synthesis Tool:** The CLD reports were generated using [synthesis tool name] with the following settings: [list key synthesis settings].

## Model Details

* **ML Agent:** The chosen machine learning agent for CLD prediction is [model name, e.g., Random Forest Regression, Graph Neural Network].
* **Feature Engineering:** The following features were extracted from the RTL designs:
    * Fan-in count
    * Fan-out count
    * Operator count (e.g. AND, OR, XOR)
    * Signal type (register, wire, input, output)
    * Lines of code
    * Graph based features (if applicable)
    * One hot encoded features.
* **Hyperparameter Tuning:** Hyperparameters were tuned using [method, e.g., cross-validation, grid search, random search]. The optimal hyperparameters were [list key hyperparameters and their values].

## Evaluation Metrics

* **Mean Squared Error (MSE):** Measures the average squared difference between predicted and actual CLD values.
* **Mean Absolute Error (MAE):** Measures the average absolute difference between predicted and actual CLD values.
* **R-squared:** Measures the proportion of variance in the CLD values that is predictable from the features.
* **Run-time Measurement:** The prediction run-time was measured using the `time` module in Python. The synthesis run-time was obtained from the synthesis reports.

## Dependencies

* Python 3.8 (or later)
* pandas
* scikit-learn
* TensorFlow or PyTorch (if using neural networks)
* networkx (if using graph features)
* any other dependencies listed in requirements.txt

Key Code Implementation Considerations:

Data Loading and Preprocessing (data_loader.py):
Use libraries like pandas to load and manipulate CSV/JSON datasets.
Implement functions to parse synthesis reports and extract CLD values.
Handle missing or inconsistent data.
Feature Extraction (feature_extractor.py):
Implement functions to calculate fan-in, fan-out, and other relevant features.
Use libraries like networkx for graph-based feature extraction (if using GNNs).
Implement one hot encoding.
Model Implementation (model.py):
Use libraries like scikit-learn for Random Forest or Gradient Boosting.
Use TensorFlow or PyTorch for neural network models (GNNs, MLPs).
Implement the chosen model architecture.
Training and Evaluation (trainer.py):
Implement training loops using scikit-learn or TensorFlow/PyTorch.
Use scikit-learn metrics for evaluation.
Implement run-time measurement using time module.
Graph Creation:
Use Antlr4, or other parsing tools, to create the graph from the RTL.
Error Handling:
Implement robust error handling throughout the code.
V. Evaluation Criteria Alignment:

Accuracy of Logic-Depth Prediction:
Use MSE, MAE, or R-squared to quantify the difference between predicted and actual CLD values.
Present results in tables and graphs.
Prediction Run-Time:
Measure the time taken for feature extraction and model prediction.
Compare the run-time with the synthesis run-time.
Present run-time results in tables and graphs.
Feature Engineering:
Provide a detailed explanation of the chosen features and their impact on prediction quality.
Perform ablation studies to assess the importance of individual features.
