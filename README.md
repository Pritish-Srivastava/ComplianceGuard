# Compliance Monitoring and Enforcement using Large Language Models

## Introduction
This project demonstrates an automated compliance monitoring and enforcement system that utilizes large language models (LLMs) to analyze log data. It identifies non-compliant activities based on predefined compliance rules and generates actionable insights for remediation.

## Features
- Utilizes spaCy's 'en_core_web_lg' LLM for rule inference and text analysis.
- Implements rule matching using CountVectorizer and cosine similarity.
- Generates actionable insights for non-compliant logs.
- Provides a simple command-line interface for demonstration purposes.

## Usage
1. Install the required Python packages:

   pip install pandas spacy scikit-learn

2. Set up the 'en_core_web_lg' LLM using spaCy:

   python -m spacy download en_core_web_lg

3. Modify the 'compliance_rules' dictionary and 'log_data' list in the script according to your use case.

4. Run the script:

   python compliance_monitoring.py

## Installation
1. Clone this repository:
        git clone https://github.com/Pritish-Srivastava/compliance-monitoring.git
   
        cd compliance-monitoring

3. Follow the usage instructions to set up and run the script.

