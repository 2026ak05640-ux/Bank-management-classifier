
import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(
    page_title="ML Classification Project",
    page_icon="📊",
    layout="wide"
)

st.title("Machine Learning Classification Project")

st.subheader("Bank Marketing Dataset")
st.write(
    "Comparison of five machine learning classification "
    "algorithms using six evaluation metrics."
)

# Load results
if os.path.exists("model_comparison_results.csv"):
    results = pd.read_csv("model_comparison_results.csv")

    st.subheader("Model Performance Comparison")
    st.dataframe(results, use_container_width=True)

    # Performance chart
    metrics = [
        "Accuracy", "AUC", "Precision",
        "Recall", "F1", "MCC"
    ]

    st.subheader("Performance Visualization")

    chart_data = results.set_index("ML Model Name")[metrics]
    st.bar_chart(chart_data)

else:
    st.error("Model results file not found.")

# Model selection
st.subheader("Explore Trained Models")

models = {
    "Logistic Regression": "logistic_regression.joblib",
    "Decision Tree": "decision_tree.joblib",
    "KNN": "knn.joblib",
    "Naive Bayes": "naive_bayes.joblib",
    "Support Vector Machine": "svm.joblib"
}

selected_model = st.selectbox(
    "Select Classification Model",
    list(models.keys())
)

model_path = os.path.join(
    "model", models[selected_model]
)

if os.path.exists(model_path):
    model = joblib.load(model_path)

    st.success(f"{selected_model} loaded successfully!")

    st.write("Trained model:", selected_model)

# Test dataset
st.subheader("Test Dataset")

if os.path.exists("test_data.csv"):
    test_data = pd.read_csv("test_data.csv")

    st.write("Test dataset shape:", test_data.shape)
    st.dataframe(test_data.head(10))

    if st.button("Run Predictions"):
        X_new = test_data.drop(columns=["y"])
        predictions = model.predict(X_new)

        output = pd.DataFrame({
            "Actual": test_data["y"],
            "Predicted": predictions
        })

        st.subheader("Prediction Results")
        st.dataframe(output)

        st.download_button(
            "Download Predictions",
            output.to_csv(index=False),
            file_name="predictions.csv",
            mime="text/csv"
        )
else:
    st.warning("Test dataset not found.")
