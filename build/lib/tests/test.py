import sys
import os

# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory (root directory of the project)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

# Add the parent directory to sys.path
sys.path.append(parent_dir)

from emotion_analysis.data_preprocessing import *
from emotion_analysis.tweets_embedding import *
from emotion_analysis.frnn import *
from emotion_analysis.bert_pcc_score_emotions import *
from emotion_analysis.roberta_pcc_score_emotions import *

anger_train, anger_dev, anger_data, anger_test = upload_datasets(
    "/home/ahsan-pmylsp/Desktop/frnn_emotion_detection-main/update/Frnn_Emotion/emotion_analysis/dataset/2018-EI-oc-En-anger-dev.txt",
    "/home/ahsan-pmylsp/Desktop/frnn_emotion_detection-main/update/Frnn_Emotion/emotion_analysis/dataset/EI-oc-En-anger-train.txt",
    "/home/ahsan-pmylsp/Desktop/frnn_emotion_detection-main/update/Frnn_Emotion/emotion_analysis/dataset/2018-EI-oc-En-anger-test.txt",
)

fear_train, fear_dev, fear_data, fear_test = upload_datasets(
    "/home/ahsan-pmylsp/Desktop/frnn_emotion_detection-main/update/Frnn_Emotion/emotion_analysis/dataset/EI-oc-En-fear-train.txt",
    "/home/ahsan-pmylsp/Desktop/frnn_emotion_detection-main/update/Frnn_Emotion/emotion_analysis/dataset/2018-EI-oc-En-fear-dev.txt",
    "/home/ahsan-pmylsp/Desktop/frnn_emotion_detection-main/update/Frnn_Emotion/emotion_analysis/dataset/2018-EI-oc-En-fear-test.txt",
)

joy_train, joy_dev, joy_data, joy_test = upload_datasets(
    "/home/ahsan-pmylsp/Desktop/frnn_emotion_detection-main/update/Frnn_Emotion/emotion_analysis/dataset/EI-oc-En-joy-train.txt",
    "/home/ahsan-pmylsp/Desktop/frnn_emotion_detection-main/update/Frnn_Emotion/emotion_analysis/dataset/2018-EI-oc-En-joy-dev.txt",
    "/home/ahsan-pmylsp/Desktop/frnn_emotion_detection-main/update/Frnn_Emotion/emotion_analysis/dataset/2018-EI-oc-En-joy-test.txt",
)

sad_train, sad_dev, sad_data, sad_test = upload_datasets(
    "/home/ahsan-pmylsp/Desktop/frnn_emotion_detection-main/update/Frnn_Emotion/emotion_analysis/dataset/EI-oc-En-sadness-train.txt",
    "/home/ahsan-pmylsp/Desktop/frnn_emotion_detection-main/update/Frnn_Emotion/emotion_analysis/dataset/2018-EI-oc-En-sadness-dev.txt",
    "/home/ahsan-pmylsp/Desktop/frnn_emotion_detection-main/update/Frnn_Emotion/emotion_analysis/dataset/2018-EI-oc-En-sadness-test.txt",
)


anger_train, anger_dev, anger_data, anger_test = (
    anger_train[:5],
    anger_dev[:5],
    anger_data[:5],
    anger_test[:5],
)
fear_train, fear_dev, fear_data, fear_test = (
    fear_train[:5],
    fear_dev[:5],
    fear_data[:5],
    fear_test[:5],
)
joy_train, joy_dev, joy_data, joy_test = (
    joy_train[:5],
    joy_dev[:5],
    joy_data[:5],
    joy_test[:5],
)
sad_train, sad_dev, sad_data, sad_test = (
    sad_train[:5],
    sad_dev[:5],
    sad_data[:5],
    sad_test[:5],
)

generate_wordclouds(anger_train, anger_dev, anger_data, anger_test, "Anger")
plot_statistics(anger_train, anger_dev, anger_data, anger_test, "Anger")
plot_additional_statistics(anger_train, anger_dev, anger_test, "Anger")
plot_top_n_words(anger_train, n=20, title="Top 20 Frequent Words in Anger Train Data")
plot_ngrams_frequency(
    anger_train, n=2, top_n=10, title="Bigram Frequency in Anger Train Data"
)
plot_ngrams_frequency(
    anger_train, n=3, top_n=10, title="Trigram Frequency in Anger Train Data"
)

generate_wordclouds(joy_train, joy_dev, joy_data, joy_test, "Joy")
plot_statistics(joy_train, joy_dev, joy_data, joy_test, "Joy")
plot_additional_statistics(joy_train, joy_dev, joy_test, "Joy")
plot_top_n_words(joy_train, n=20, title="Top 20 Frequent Words in Joy Train Data")
plot_ngrams_frequency(
    joy_train, n=2, top_n=10, title="Bigram Frequency in Joy Train Data"
)
plot_ngrams_frequency(
    joy_train, n=3, top_n=10, title="Trigram Frequency in Joy Train Data"
)

generate_wordclouds(sad_train, sad_dev, sad_data, sad_test, "Sadness")
plot_statistics(sad_train, sad_dev, sad_data, sad_test, "Sadness")
plot_additional_statistics(sad_train, sad_dev, sad_test, "Sadness")
plot_top_n_words(sad_train, n=20, title="Top 20 Frequent Words in Sadness Train Data")
plot_ngrams_frequency(
    sad_train, n=2, top_n=10, title="Bigram Frequency in Sadness Train Data"
)
plot_ngrams_frequency(
    sad_train, n=3, top_n=10, title="Trigram Frequency in Sadness Train Data"
)

generate_wordclouds(fear_train, fear_dev, fear_data, fear_test, "Fear")
plot_statistics(fear_train, fear_dev, fear_data, fear_test, "Fear")
plot_additional_statistics(fear_train, fear_dev, fear_test, "Fear")
plot_top_n_words(fear_train, n=20, title="Top 20 Frequent Words in Fear Train Data")
plot_ngrams_frequency(
    fear_train, n=2, top_n=10, title="Bigram Frequency in Fear Train Data"
)
plot_ngrams_frequency(
    fear_train, n=3, top_n=10, title="Trigram Frequency in Fear Train Data"
)


plot_dataset_statistics([anger_data, joy_data, sad_data, fear_data])

print("vector Bert")

anger_data["Vector_bert"] = anger_data["Tweet"].apply(get_vector_bert)
anger_test["Vector_bert"] = anger_test["Tweet"].apply(get_vector_bert)

joy_data["Vector_bert"] = joy_data["Tweet"].apply(get_vector_bert)
joy_test["Vector_bert"] = joy_test["Tweet"].apply(get_vector_bert)

sad_data["Vector_bert"] = sad_data["Tweet"].apply(get_vector_bert)
sad_test["Vector_bert"] = sad_test["Tweet"].apply(get_vector_bert)

fear_data["Vector_bert"] = fear_data["Tweet"].apply(get_vector_bert)
fear_test["Vector_bert"] = fear_test["Tweet"].apply(get_vector_bert)

print("1st done")

anger_data["Vector_bert_cl"] = anger_data["Cleaned_tweet"].apply(get_vector_bert)
anger_test["Vector_bert_cl"] = anger_test["Cleaned_tweet"].apply(get_vector_bert)

joy_data["Vector_bert_cl"] = joy_data["Cleaned_tweet"].apply(get_vector_bert)
joy_test["Vector_bert_cl"] = joy_test["Cleaned_tweet"].apply(get_vector_bert)

sad_data["Vector_bert_cl"] = sad_data["Cleaned_tweet"].apply(get_vector_bert)
sad_test["Vector_bert_cl"] = sad_test["Cleaned_tweet"].apply(get_vector_bert)

fear_data["Vector_bert_cl"] = fear_data["Cleaned_tweet"].apply(get_vector_bert)
fear_test["Vector_bert_cl"] = fear_test["Cleaned_tweet"].apply(get_vector_bert)

print("2nd done")

# BERT
# With raw tweets

anger_data["Vector_bert_cl_ws"] = anger_data["Cleaned_tweet_wt_stopwords"].apply(
    get_vector_bert
)
anger_test["Vector_bert_cl_ws"] = anger_test["Cleaned_tweet_wt_stopwords"].apply(
    get_vector_bert
)

joy_data["Vector_bert_cl_ws"] = joy_data["Cleaned_tweet_wt_stopwords"].apply(
    get_vector_bert
)
joy_test["Vector_bert_cl_ws"] = joy_test["Cleaned_tweet_wt_stopwords"].apply(
    get_vector_bert
)

sad_data["Vector_bert_cl_ws"] = sad_data["Cleaned_tweet_wt_stopwords"].apply(
    get_vector_bert
)
sad_test["Vector_bert_cl_ws"] = sad_test["Cleaned_tweet_wt_stopwords"].apply(
    get_vector_bert
)

fear_data["Vector_bert_cl_ws"] = fear_data["Cleaned_tweet_wt_stopwords"].apply(
    get_vector_bert
)
fear_test["Vector_bert_cl_ws"] = fear_test["Cleaned_tweet_wt_stopwords"].apply(
    get_vector_bert
)


anger_data["Vector_roberta"] = anger_data["Tweet"].apply(get_vector_roberta)
anger_test["Vector_roberta"] = anger_test["Tweet"].apply(get_vector_roberta)

joy_data["Vector_roberta"] = joy_data["Tweet"].apply(get_vector_roberta)
joy_test["Vector_roberta"] = joy_test["Tweet"].apply(get_vector_roberta)

sad_data["Vector_roberta"] = sad_data["Tweet"].apply(get_vector_roberta)
sad_test["Vector_roberta"] = sad_test["Tweet"].apply(get_vector_roberta)

fear_data["Vector_roberta"] = fear_data["Tweet"].apply(get_vector_roberta)
fear_test["Vector_roberta"] = fear_test["Tweet"].apply(get_vector_roberta)

print("1st done")

anger_data["Vector_roberta_cl"] = anger_data["Cleaned_tweet"].apply(get_vector_roberta)
anger_test["Vector_roberta_cl"] = anger_test["Cleaned_tweet"].apply(get_vector_roberta)

joy_data["Vector_roberta_cl"] = joy_data["Cleaned_tweet"].apply(get_vector_roberta)
joy_test["Vector_roberta_cl"] = joy_test["Cleaned_tweet"].apply(get_vector_roberta)

sad_data["Vector_roberta_cl"] = sad_data["Cleaned_tweet"].apply(get_vector_roberta)
sad_test["Vector_roberta_cl"] = sad_test["Cleaned_tweet"].apply(get_vector_roberta)

fear_data["Vector_roberta_cl"] = fear_data["Cleaned_tweet"].apply(get_vector_roberta)
fear_test["Vector_roberta_cl"] = fear_test["Cleaned_tweet"].apply(get_vector_roberta)

print("2nd done")

# roberta
# With raw tweets

anger_data["Vector_roberta_cl_ws"] = anger_data["Cleaned_tweet_wt_stopwords"].apply(
    get_vector_roberta
)
anger_test["Vector_roberta_cl_ws"] = anger_test["Cleaned_tweet_wt_stopwords"].apply(
    get_vector_roberta
)

joy_data["Vector_roberta_cl_ws"] = joy_data["Cleaned_tweet_wt_stopwords"].apply(
    get_vector_roberta
)
joy_test["Vector_roberta_cl_ws"] = joy_test["Cleaned_tweet_wt_stopwords"].apply(
    get_vector_roberta
)

sad_data["Vector_roberta_cl_ws"] = sad_data["Cleaned_tweet_wt_stopwords"].apply(
    get_vector_roberta
)
sad_test["Vector_roberta_cl_ws"] = sad_test["Cleaned_tweet_wt_stopwords"].apply(
    get_vector_roberta
)

fear_data["Vector_roberta_cl_ws"] = fear_data["Cleaned_tweet_wt_stopwords"].apply(
    get_vector_roberta
)
fear_test["Vector_roberta_cl_ws"] = fear_test["Cleaned_tweet_wt_stopwords"].apply(
    get_vector_roberta
)


anger_pcc_scores = cross_validation_ensemble_owa(
    anger_data.head(10),
    vector_names=["Vector_roberta_cl", "Vector_roberta", "Vector_roberta_cl_ws"],
    NNeighbours=[5, 5],
    lower=[1, 1],
    upper=[1, 1],
    alpha=0.5,
    cv=5,
)
print("anger_PCC Scores:", np.mean(anger_pcc_scores))

joy_pcc_scores = cross_validation_ensemble_owa(
    joy_data.head(10),
    vector_names=["Vector_roberta_cl", "Vector_roberta", "Vector_roberta_cl_ws"],
    NNeighbours=[5, 5],
    lower=[1, 1],
    upper=[1, 1],
    alpha=0.5,
    cv=5,
)
print("joy_PCC Scores:", np.mean(joy_pcc_scores))

fear_pcc_scores = cross_validation_ensemble_owa(
    fear_data.head(10),
    vector_names=["Vector_roberta_cl", "Vector_roberta", "Vector_roberta_cl_ws"],
    NNeighbours=[5, 5],
    lower=[1, 1],
    upper=[1, 1],
    alpha=0.5,
    cv=5,
)
print("fear_PCC Scores:", np.mean(fear_pcc_scores))

sad_pcc_scores = cross_validation_ensemble_owa(
    sad_data.head(10),
    vector_names=["Vector_roberta_cl", "Vector_roberta", "Vector_roberta_cl_ws"],
    NNeighbours=[5, 5],
    lower=[1, 1],
    upper=[1, 1],
    alpha=0.5,
    cv=5,
)
print("sad_PCC Scores:", np.mean(sad_pcc_scores))


anger_pcc_scores = np.mean(anger_pcc_scores)
joy_pcc_scores = np.mean(joy_pcc_scores)
fear_pcc_scores = np.mean(fear_pcc_scores)
sad_pcc_scores = np.mean(sad_pcc_scores)
avg_roberta_emotions_pcc = (
    anger_pcc_scores + joy_pcc_scores + fear_pcc_scores + sad_pcc_scores
) / 4
print("Final PCC Score roberta :", avg_roberta_emotions_pcc)


import os
import matplotlib.pyplot as plt

# Emotion labels
emotion_labels = ["Anger", "Joy", "Fear", "Sadness"]

# Vector types
vector_types = ["Vector_roberta_cl", "Vector_roberta", "Vector_roberta_cl_ws", "bb"]

# Mean PCC scores for each vector type
mean_pcc_scores = [
    np.mean(anger_pcc_scores),
    np.mean(joy_pcc_scores),
    np.mean(fear_pcc_scores),
    np.mean(sad_pcc_scores),
]

plt.figure(figsize=(10, 6))

bars = plt.bar(vector_types, mean_pcc_scores, color="skyblue")

plt.xlabel("Vector Type")
plt.ylabel("Mean PCC Score")
plt.title("Mean PCC Scores for Different Vector Types")
plt.xticks(rotation=45)
plt.grid(axis="y")

# Set the emotion labels as tick labels on the x-axis
plt.xticks(ticks=vector_types, labels=emotion_labels)

# Add value labels on top of each bar
for bar, score in zip(bars, mean_pcc_scores):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.01,
        round(score, 4),
        ha="center",
        va="bottom",
        fontweight="bold",
    )

# Create the directory if it doesn't exist
plots_dir = "plots/roberta_pcc_score"
os.makedirs(plots_dir, exist_ok=True)

# Save the figure
plt.savefig(os.path.join(plots_dir, "roberta_pcc_scores.png"))

print("roberta Base Vector Done!")


anger_pcc_scores = cross_validation_ensemble_owa(
    anger_data.head(10),
    vector_names=["Vector_bert_cl", "Vector_bert", "Vector_bert_cl_ws"],
    NNeighbours=[5, 5],
    lower=[1, 1],
    upper=[1, 1],
    alpha=0.5,
    cv=5,
)
print("anger_PCC Scores:", np.mean(anger_pcc_scores))

joy_pcc_scores = cross_validation_ensemble_owa(
    joy_data.head(10),
    vector_names=["Vector_bert_cl", "Vector_bert", "Vector_bert_cl_ws"],
    NNeighbours=[5, 5],
    lower=[1, 1],
    upper=[1, 1],
    alpha=0.5,
    cv=5,
)
print("joy_PCC Scores:", np.mean(joy_pcc_scores))

fear_pcc_scores = cross_validation_ensemble_owa(
    fear_data.head(10),
    vector_names=["Vector_bert_cl", "Vector_bert", "Vector_bert_cl_ws"],
    NNeighbours=[5, 5],
    lower=[1, 1],
    upper=[1, 1],
    alpha=0.5,
    cv=5,
)
print("fear_PCC Scores:", np.mean(fear_pcc_scores))

sad_pcc_scores = cross_validation_ensemble_owa(
    sad_data.head(10),
    vector_names=["Vector_bert_cl", "Vector_bert", "Vector_bert_cl_ws"],
    NNeighbours=[5, 5],
    lower=[1, 1],
    upper=[1, 1],
    alpha=0.5,
    cv=5,
)
print("sad_PCC Scores:", np.mean(sad_pcc_scores))


anger_pcc_scores = np.mean(anger_pcc_scores)
joy_pcc_scores = np.mean(joy_pcc_scores)
fear_pcc_scores = np.mean(fear_pcc_scores)
sad_pcc_scores = np.mean(sad_pcc_scores)
avg_bert_emotions_pcc = (
    anger_pcc_scores + joy_pcc_scores + fear_pcc_scores + sad_pcc_scores
) / 4
print("Final PCC Score Bert :", avg_bert_emotions_pcc)


import os
import matplotlib.pyplot as plt

# Emotion labels
emotion_labels = ["Anger", "Joy", "Fear", "Sadness"]

# Vector types
vector_types = ["Vector_bert_cl", "Vector_bert", "Vector_bert_cl_ws", "bb"]

# Mean PCC scores for each vector type
mean_pcc_scores = [
    np.mean(anger_pcc_scores),
    np.mean(joy_pcc_scores),
    np.mean(fear_pcc_scores),
    np.mean(sad_pcc_scores),
]

plt.figure(figsize=(10, 6))

bars = plt.bar(vector_types, mean_pcc_scores, color="skyblue")

plt.xlabel("Vector Type")
plt.ylabel("Mean PCC Score")
plt.title("Mean PCC Scores for Different Vector Types")
plt.xticks(rotation=45)
plt.grid(axis="y")

# Set the emotion labels as tick labels on the x-axis
plt.xticks(ticks=vector_types, labels=emotion_labels)

# Add value labels on top of each bar
for bar, score in zip(bars, mean_pcc_scores):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.01,
        round(score, 4),
        ha="center",
        va="bottom",
        fontweight="bold",
    )

# Create the directory if it doesn't exist
plots_dir = "plots/bert_pcc_score"
os.makedirs(plots_dir, exist_ok=True)

# Save the figure
plt.savefig(os.path.join(plots_dir, "bert_pcc_scores.png"))

print("Bert Base Vector Done!")


print(
    "Thanks For Your Patence. Code Run Succesfull Checkout Plot Folder to see Results!"
)
