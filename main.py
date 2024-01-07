import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import matplotlib.pyplot as plt

# dosyayı bir veri çerçevesi olarak oku
df = pd.read_csv("tablo.txt")

# ID 3 algoritması için gerekli olan entropi ve kazanç fonksiyonlarını tanımla


#Entropi hesaplama
def entropy(col):
    values, counts = np.unique(col, return_counts=True)
    ent = 0
    for i in range(len(values)):
        p = counts[i] / np.sum(counts)
        ent = ent - p * np.log2(p)
    return ent

#Kazanç hesaplama
def gain(df, attr, target):
    total_entropy = entropy(df[target])
    values, counts = np.unique(df[attr], return_counts=True)
    attr_entropy = 0
    for i in range(len(values)):
        sub_df = df[df[attr] == values[i]]
        sub_entropy = entropy(sub_df[target])
        attr_entropy = attr_entropy + (counts[i] / np.sum(counts)) * sub_entropy
    return total_entropy - attr_entropy

#Karar agaci olusturma
def build_tree(df, target, features):
    classes = np.unique(df[target])
    if len(classes) == 1:
        return classes[0]
    elif len(features) == 0:
        return df[target].value_counts().idxmax()
    else:
        best_feature = features[0]
        best_gain = gain(df, best_feature, target)
        for feature in features[1:]:
            current_gain = gain(df, feature, target)
            if current_gain > best_gain:
                best_feature = feature
                best_gain = current_gain
        tree = {best_feature: {}}
        values = np.unique(df[best_feature])
        features.remove(best_feature)
        for value in values:
            sub_df = df[df[best_feature] == value]
            subtree = build_tree(sub_df, target, features.copy())
            tree[best_feature][value] = subtree
        return tree

target = "sınıf"
features = ["alan", "durum", "kullanım"]
tree = build_tree(df, target, features)


#Karar ağacına göre tahmin olusturma
def predict(tree, email):
    domain = email.split("@")[1]
    node = list(tree.keys())[0]
    if domain in tree[node]:
        subtree = tree[node][domain]
        if isinstance(subtree, dict):
            return predict(subtree, email)
        else:
            return subtree
    else:
        return "Geçersiz mail adresi"


#Karar ağacını görsel bir şekilde ekranda gosterme
def show_tree():
    features = ["alan", "durum", "kullanım"]
    target = "sınıf"

    label_encoders = {}
    for feature in features:
        le = LabelEncoder()
        df[feature] = le.fit_transform(df[feature])
        label_encoders[feature] = le

    # Karar ağacı modelini oluştur ve eğit
    model = DecisionTreeClassifier(criterion="entropy")
    model.fit(df[features], df[target])

    # Karar ağacını görselleştir
    plt.figure(figsize=(25, 25))
    plot_tree(model, feature_names=features, class_names=model.classes_, filled=True)
    plt.show()


show_tree()


#Giris/Cıkış işlemleri
def get_input_and_output():

    warning_text = "Lütfen geçerli bir mail adresi girdiğinizden emin olunuz!"
    while True:
        email = input("Lütfen bir e-posta adresi giriniz: ")
        if "@" in email:
            prediction = predict(tree, email)

            if prediction == "Geçersiz mail adresi":
                print(warning_text)
                continue

            print(f"{email} adresinizin sınıfı: {prediction}")
            break
        else:
            print(warning_text)


get_input_and_output()