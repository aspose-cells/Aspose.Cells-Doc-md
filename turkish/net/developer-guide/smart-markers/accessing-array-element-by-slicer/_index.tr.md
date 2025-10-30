---
title: Akıllı Markörlerle dilimleyici kullanarak Excel e Dizi Öğesini Akıllıca İçe Aktarma
type: docs
weight: 30
url: /tr/net/how-to-import-array-element-by-slicer-with-smart-markers/
---

## **Neden Dilimleyici ile Dizi Öğesine Erişim**
FastReport'un Akıllı Markörlerinde, dilimleyici kullanarak (ör. [array[1..3]]) dizideki öğelere erişim, veri alt kümeleriyle çalışma konusunda özlü ve verimli bir yol sağlar.

1. Basitleştirilmiş Veri Çekme: Büyük diziler üzerinde manuel yineleme, döngüler ve karmaşık sözdizimi gerektirir. Dilimleyiciler, aralıklar (alt diziler) tek satırda alınmasına olanak tanır. Örnek: [Products[1..5].Name] ilk 5 ürünün isimlerini getirir.
2. Dinamik Raporlama: Değişken veri dilimlerine göre raporlar oluşturma (ör. "En İyi N öğe", sayfalı görünümler). Örnek: [Sales[0..{PageNo*10}]] çok sayfalı raporlar için veri parçalarını dinamik olarak yükler.
3. Performans Optimizasyonu: Tüm diziyi belleğe yüklemeden sadece gereken öğeleri getir. Örnek: [Logs[^10..^1]] son 10 girdiyi verimli şekilde alır.
4. Bildirisel Sözdizimi: Niyetinizi doğrudan şablon belirteçlerinde ifade edin. Örnek: [Employees[3..7].Department] 3 ile 7 arasındaki girdilerden departmanları açıkça seçer.
5. Veri Kaynaklarıyla Entegrasyon: Veritabanlarından, JSON'dan veya koddan dizilerle çalışır. Örnek: Invoice.Items[0..2] ilk 3 satır öğesini göstermek için bağlama.
Akıllı İşaretçilere Slicer tarafından dilimleme, kod karmaşıklığını azaltır, okunabilirliği artırır ve dizi alt kümeleri için veri işleme optimizasyonu sağlar. Hızlı, aralık tabanlı erişim gerektiğinde kullanın—sayfalama, en iyi-N listeleri veya pencere tabanlı veri görünümleri için idealdir. 

## **Excel'e Slicer ile Dizi Öğesi İçe Aktarmanın Yolu ve Akıllı İşaretçiler ile kullanımı**
Aspose.Cells, akıllı işaretçilerde dilimleyici ile dizi öğesine erişimi destekler. Lütfen [şablon dosyasını](ElementBySlicer.xlsx), [json dosyasını](ElementBySlicer.json) ve aşağıdaki kodla oluşturulan çıktı excel dosyasının ekran görüntüsünü kontrol edin.

|**smartmarker.xlsx dosyasının ilk sayfası ve akıllı işaretçiler gösteriliyor.**|
| :- |
|![todo:image_alt_text](ElementBySlicer1.png)|

|**Çıktı excel dosyasının ekran görüntüsü.**|
| :- |
|![todo:image_alt_text](ElementBySlicer2.png)|

Json verileri şu şekildedir:
```json data
{
  "EntityCin": "EntityCin Test",
  "EntityName": "EntityName Test",
  "FirstName": "FirstName Test",
  "MiddleName": "MiddleName Test",
  "LastName": "LastName Test",
  "DOB": "2025-02-08",
  "SSN": "11111111",
  "Directors": [
    {
      "id": "director id 1",
      "FirstName": "director first 1",
      "MiddleName": "director middle 1",
      "LastName": "director last 1",
      "Reportees": [
        {
          "id": "aaa",
          "FirstName": "first aaa",
          "MiddleName": "middle aaa",
          "LastName": "last aaa",
          "Department": "aaa department",
          "City": "aaa city",
          "GST": "Yes",
          "ITR": "No"
        },
        {
          "id": "bbb",
          "FirstName": "first bbb",
          "MiddleName": "middle bbb",
          "LastName": "last bbb",
          "Department": "bbb department",
          "City": "bbb city",
          "GST": "Yes",
          "ITR": "Yes"
        },
        {
          "id": "ccc",
          "FirstName": "first ccc",
          "MiddleName": "middle ccc",
          "LastName": "last ccc",
          "Department": "ccc department",
          "City": "ccc city",
          "GST": "No",
          "ITR": "No"
        }
      ]
    },
    {
      "id": "director id 2",
      "FirstName": "director first 2",
      "MiddleName": "director middle 2",
      "LastName": "director last 2",
      "Reportees": [
        {
          "id": "eee",
          "FirstName": "first eee",
          "MiddleName": "middle eee",
          "LastName": "last eee",
          "Department": "eee department",
          "City": "eee city",
          "GST": "Yes",
          "ITR": "No"
        },
        {
          "id": "fff",
          "FirstName": "first fff",
          "MiddleName": "middle fff",
          "LastName": "last fff",
          "Department": "fff department",
          "City": "fff city",
          "GST": "No",
          "ITR": "No"
        }
      ]
    },
    {
      "id": "director id 3",
      "FirstName": "director first 2",
      "MiddleName": "director middle 2",
      "LastName": "director last 2",
      "Reportees": [
        {
          "id": "eee3",
          "FirstName": "first eee3",
          "MiddleName": "middle eee3",
          "LastName": "last eee3",
          "Department": "eee department3",
          "City": "eee city3",
          "GST": "Yes",
          "ITR": "No"
        },
        {
          "id": "fff3",
          "FirstName": "first fff3",
          "MiddleName": "middle fff3",
          "LastName": "last fff3",
          "Department": "fff department3",
          "City": "fff city",
          "GST": "No",
          "ITR": "No"
        }
      ]
    },
    {
      "id": "director id 4",
      "FirstName": "director first 4",
      "MiddleName": "director middle 4",
      "LastName": "director last 4",
      "Reportees": [
        {
          "id": "eee4",
          "FirstName": "first eee4",
          "MiddleName": "middle eee4",
          "LastName": "last eee4",
          "Department": "eee department4",
          "City": "eee city4",
          "GST": "Yes",
          "ITR": "No"
        },
        {
          "id": "fff4",
          "FirstName": "first fff4",
          "MiddleName": "middle fff4",
          "LastName": "last fff4",
          "Department": "fff department4",
          "City": "fff city4",
          "GST": "No",
          "ITR": "No"
        }
      ]
    }
  ]
}
```
Aşağıdaki örnek, bu işlemin nasıl çalıştığını gösterir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-AccessElementBySlicer.cs" >}}

{{< app/cells/assistant language="csharp" >}}
