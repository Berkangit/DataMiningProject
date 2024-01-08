

# Decision Tree Projesi Markdown Dosyası

## Proje Grubu Bilgileri
- *Mustafa Kamber*
  - Okul Numarası: 02205076062
- *Emir Furkan Umutlu*
  - Okul Numarası: 02205076056
- *Erhan Şen*
  - Okul Numarası: 02210201521
- *Berkan Taştekin*
  - Okul Numarası: 02210201519
- *Muhammet Mikail Afşin*
  - Okul Numarası: 02200201073

## Proje Açıklaması

Bu proje, bir e-posta adresinin sınıfını belirlemek için Decision Tree algoritmasını kullanmaktadır. Proje, Python programlama dili ve çeşitli kütüphaneler kullanılarak geliştirilmiştir.

## Kullanılan Algoritmalar

Proje, scikit-learn kütüphanesinde bulunan Decision Tree sınıflandırıcı algoritması kullanılarak e-posta adreslerinin sınıflandırılmasını gerçekleştirir. Ayrıca, proje içerisinde ID3 algoritması için özel olarak geliştirilmiş fonksiyonlar da bulunmaktadır.

## Kullanılan Teknolojiler

- Python
- pandas
- numpy
- scikit-learn
- matplotlib

## Proje İçeriği ve İşleyişi

Proje, aşağıdaki temel bileşenlere sahiptir:

1. *Veri Okuma ve İşleme:* pandas kütüphanesi kullanılarak "tablo.txt" adlı dosya bir veri çerçevesine okunur.
2. *ID3 Algoritması:* Veri seti üzerinde ID3 algoritması ile bir karar ağacı oluşturulur.
3. *Karar Ağacı Görselleştirme:* scikit-learn kütüphanesinde bulunan Decision Tree sınıflandırıcı kullanılarak oluşturulan karar ağacı görsel bir şekilde ekrana çizilir.
4. *Tahmin İşlemi:* Oluşturulan karar ağacı kullanılarak bir e-posta adresinin sınıfı tahmin edilir.
5. *Giriş/Çıkış İşlemleri:* Kullanıcıdan bir e-posta adresi alınarak, bu adresin sınıfı karar ağacı kullanılarak belirlenir.

## Kullanım

Proje, bir e-posta adresinin sınıfını belirlemek için kullanıcının girişiyle çalışır. Kullanıcıya geçerli bir e-posta adresi girmesi istenir ve ardından karar ağacı kullanılarak bu adresin sınıfı tahmin edilir.

python
# Giriş ve Çıkış İşlemleri
get_input_and_output()


## Karar Ağacı Görseli

Projenin bir parçası olarak, karar ağacı görsel bir şekilde ekrana çizilmektedir. Bu görselleştirmeyi yapmak için matplotlib ve scikit-learn kütüphaneleri kullanılmaktadır.

python
# Karar Ağacı Görselleştirme
show_tree()


## Ekran Görüntüsü

Aşağıda, karar ağacının görsel bir temsilini içeren bir örnek ekran görüntüsü bulunmaktadır:

<img src="https://i.ibb.co/Gtp4vWY/foto.png" width="520" height="520"/>

---

Bu proje, e-posta adreslerinin sınıflandırılması için Decision Tree algoritmasını kullanarak basit bir örnek sunmaktadır. Proje ekibi, algoritmanın geliştirilmesi, veri işleme ve görselleştirme süreçlerinde işbirliği yaparak projeyi tamamlamıştır.
