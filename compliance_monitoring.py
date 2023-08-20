import pandas as pd
import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Loading the large language model (LLM) using spaCy
nlp = spacy.load('en_core_web_lg')

# Loading compliance rules and standards
compliance_rules = {
    'access_control': 'Employees should have limited access to sensitive data.',
    'data_encryption': 'Sensitive data must be encrypted at rest and during transit.',
    # ...
}

# Loading sample log data
log_data = [
    'User alice accessed sensitive data at 10:30 AM.',
    'Failed login attempt for user bob at 11:45 AM.',
    # ...
]

# Preprocess log data
def preprocess_text(text):
    return ' '.join([token.lemma_ for token in nlp(text) if not token.is_punct])

preprocessed_logs = [preprocess_text(log) for log in log_data]

# Extracting features from logs using CountVectorizer
vectorizer = CountVectorizer()
feature_matrix = vectorizer.fit_transform(preprocessed_logs)

# Calculating cosine similarity between compliance rules and log features
compliance_scores = {}
for rule_name, rule_text in compliance_rules.items():
    rule_vector = vectorizer.transform([preprocess_text(rule_text)])
    similarity_scores = cosine_similarity(feature_matrix, rule_vector)
    compliance_scores[rule_name] = similarity_scores.flatten()

# Identifying non-compliant logs
threshold = 0.5
non_compliant_logs = []
for rule_name, scores in compliance_scores.items():
    non_compliant_indices = [i for i, score in enumerate(scores) if score < threshold]
    non_compliant_logs.extend([(log_data[i], rule_name) for i in non_compliant_indices])

# Generating actionable insights for non-compliant logs
actionable_insights = {}
for log, rule_name in non_compliant_logs:
    actionable_insights[log] = f"Action needed: {compliance_rules[rule_name]}"

# Displaying results
for log, insight in actionable_insights.items():
    print(f"Log: {log}")
    print(f"Actionable Insight: {insight}")
    print("=" * 50)
