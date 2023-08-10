import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def generate_classification_report(file_path):
    data = pd.read_csv(file_path, sep='\t')
    true_labels = data['annotation']
    predicted_labels = data['prediction label']
    tp = 0
    fp = 0
    fn = 0
    tn = 0


    for true, pred in zip(true_labels, predicted_labels):
        if true == 'DELETE' and pred == 'DELETE':
            tp += 1
        elif true == 'KEEP' and pred == 'KEEP':
            tn += 1
        elif true == 'KEEP' and pred == 'DELETE':
            fp += 1
        elif true == 'DELETE' and pred == 'KEEP':
            fn += 1


    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1score = (2 * precision * recall) / (precision + recall)


    print("Confusion Matrix:")
    print(f"True Positive (TP): {tp}")
    print(f"True Negative (TN): {tn}")
    print(f"False Positive (FP): {fp}")
    print(f"False Negative (FN): {fn}")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"F1-score: {f1score}")


    labels = ['KEEP', 'DELETE']
    confusion_matrix_data = [[tn, fp], [fn, tp]]
    df_cm = pd.DataFrame(confusion_matrix_data, index=labels, columns=labels)

    sns.heatmap(df_cm, annot=True, cmap='Blues', fmt='g')
    plt.xlabel('Predicted Labels')
    plt.ylabel('True Labels')
#     plt.title('Confusion Matrix')
    plt.show()
