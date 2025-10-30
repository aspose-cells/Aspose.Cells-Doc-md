---
title: Akıllı İşaretçilerde Json Veri Kullanımı
type: docs
weight: 30
url: /tr/java/using-json-data-in-smart-markers/
---

## **Akıllı İşaretçilerde Json Veri Kullanımının Nedenleri**
Akıllı İşaretçiler için orijinal veri olarak JSON Verisini neden kullanmalıyız?
JSON (JavaScript Nesne Gösterimi) hiyerarşik verileri yapılandırmak için ideal hafif, insan tarafından okunabilir bir veri değişim formatıdır. İşte akıllı işaretçiler (otomatik olarak hesaplanan yer tutucular) için neden uygun olduğu:

1. Yapılandırılmış ve Hiyerarşik Veri Desteği
JSON doğal olarak gömülü nesne ve dizileri destekler (örneğin, { "kullanıcı": { "ad": "Alice", "siparişler": [ ... ] } }). Akıllı işaretçiler bu hiyerarşı gezebilir (örneğin, {{kullanıcı.siparişler[0].fiyat}}), bu da karmaşık verileri şablonlara kolayca eşleştirmeyi sağlar.

2. Dil ve Platform Bağımsız
JSON ayrıştırıcıları hemen hemen tüm programlama dillerinde (Python, JavaScript, Java vb.) mevcuttur. Excel Power Query, Google Apps Script veya kodsuz platformlar (ör. Airtable) JSON verisini sorunsuzca işler.

3. API Uyumlu
Çoğu modern API (örn. REST, GraphQL) veriyi JSON formatında döner. Akıllı işaretçiler web hizmetlerinden canlı JSON verisi doğrudan tüketebilir, bu da gerçek zamanlı veri güncellemelerini sağlar (örn. hisse senedi fiyatları, hava durumu).

4. İnsan tarafından okunabilir ve Hata Ayıklanabilir
JSON’un düz metin yapısı doğrulaması (örneğin, JSONLint kullanılarak), manuel veya betiklerle düzenlenmesi ve işaretçilere veri eşlemede hata ayıklaması kolaydır.

5. Ölçeklenebilirlik ve Esneklik
JSON’de alanlar ekleyip kaldırmak, var olan akıllı işaretçileri bozmadan yapılabilir (isteğe bağlı alanlar dikkatli yönetildiğinde). Farklı veri türlerini destekler: dizgeler, sayılar, mantıksal, diziler ve nesneler.

6. Ekosistem Uyumluluğu
Modern veri araçlarıyla uyumludur: Veri tabanları: MongoDB, PostgreSQL (JSONB), vb. Otomasyon araçları: Zapier, Integromat. Veri hatları: Apache NiFi, Talend.

## **Excel Gömülü Şablon ile JSON Verisi Kullanımı**
Aspose.Cells for Java JSON verisini akıllı işaretçilerde destekler, JSON verisi hiyerarşik olarak iç içe olabilir. Lütfen [şablon dosyasını](smartmarker.xlsx), [json dosyasını](smartmarker.json) ve aşağıdaki kodla oluşturulan çıktı Excel dosyasının ekran görüntüsünü kontrol edin.

|**smartmarker.xlsx dosyasının ilk sayfası ve akıllı işaretçiler gösteriliyor.**|
| :- |
|![todo:image_alt_text](jsontemplate.png)|

|**Çıktı excel dosyasının ekran görüntüsü.**|
| :- |
|![todo:image_alt_text](jsonresult.png)|

Json verileri şu şekildedir:
```json data
{
    "EntityCin" : "EntityCin Test",
    "EntityName" : "EntityName Test",
    "FirstName" : "FirstName Test",
    "MiddleName" : "MiddleName Test",
    "LastName" : "LastName Test",
    "DOB" : "2025-02-08",
    "SSN" : "11111111",
    "Directors" : [
        {
            "id" : "director id 1",
            "FirstName" : "director first 1",
            "MiddleName" : "director middle 1",
            "LastName" : "director last 1",
            "Reportees" : [
                {
                    "id" : "aaa",
                    "FirstName" : "first aaa",
                    "MiddleName" : "middle aaa",
                    "LastName" : "last aaa",
                    "Department" : "aaa department",
                    "City" : "aaa city",
                    "GST" : "Yes",
                    "ITR" : "No"
                },
                {
                    "id" : "bbb",
                    "FirstName" : "first bbb",
                    "MiddleName" : "middle bbb",
                    "LastName" : "last bbb",
                    "Department" : "bbb department",
                    "City" : "bbb city",
                    "GST" : "Yes",
                    "ITR" : "Yes"
                },
                {
                    "id" : "ccc",
                    "FirstName" : "first ccc",
                    "MiddleName" : "middle ccc",
                    "LastName" : "last ccc",
                    "Department" : "ccc department",
                    "City" : "ccc city",
                    "GST" : "No",
                    "ITR" : "No"
                }
            ]
        },
        {
            "id" : "director id 2",
            "FirstName" : "director first 2",
            "MiddleName" : "director middle 2",
            "LastName" : "director last 2",
            "Reportees" : [
                {
                    "id" : "eee",
                    "FirstName" : "first eee",
                    "MiddleName" : "middle eee",
                    "LastName" : "last eee",
                    "Department" : "eee department",
                    "City" : "eee city",
                    "GST" : "Yes",
                    "ITR" : "No"
                },
                {
                    "id" : "fff",
                    "FirstName" : "first fff",
                    "MiddleName" : "middle fff",
                    "LastName" : "last fff",
                    "Department" : "fff department",
                    "City" : "fff city",
                    "GST" : "No",
                    "ITR" : "No"
                }
            ]
        }
    ]
}
```
Aşağıdaki örnek, bu işlemin nasıl çalıştığını gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-Using-JSON-Data.java" >}}


## **Excel Alt Toplam Şablonu ile JSON Verisi Kullanımı**
Aspose.Cells for Java JSON verisini akıllı işaretçilerde destekler, JSON verisi hiyerarşik olarak iç içe olabilir. Alt toplam, excel şablonunda veri istatistiği için kullanıldı. Lütfen [şablon dosyasını](jsonExcelTemplate.xlsx), [json dosyasını](jsonData.json) ve aşağıdaki kodla oluşturulan çıktı Excel dosyasının ekran görüntüsünü kontrol edin.

|**jsonExcelTemplate.xlsx dosyasının ilk çalışma sayfası akıllı belirteçleri gösteriyor.**|
| :- |
|![todo:image_alt_text](jsontemplate2.png)|

|**Çıktı excel dosyasının ekran görüntüsü.**|
| :- |
|![todo:image_alt_text](jsonresult2.png)|

Json verileri şu şekildedir:
```json data
{
    "number": 10,
    "test": "test abc",
    "date": "2011-10-05T14:48:00.000Z",
    "arrayNumber": [1,2,3,4,5],
    "arrayWords": ["x1","xy2","yz3","z4"],
    "arrayOfObjects": [
      {"valNumber":12,"valString": "aa"},
      {"valNumber":15,"valString": "bb"},
      {"valNumber":1,"valString": "cc"},
      {"valNumber":20,"valString": "dd"}

    ],
    "nestedArray": [
      {"valNumber":12,"valString": "xy","nestArr": [{"val": 1,"some": "aa"}]},
      {"valNumber":15,"valString": "y","nestArr": [{"val": 2,"some": "bb"}]},
      {"valNumber":1,"valString": "yz","nestArr": [{"some": "cc"}]},
      {"valNumber":20,"valString": "z","nestArr": [{"some": "dd"}]}
    ],
  "Products": [
    { "ProductID": "A101", "ProductName": "Apples", "Units": 5 },
    { "ProductID": "A101", "ProductName": "Apples", "Units": 10 },
    { "ProductID": "B202", "ProductName": "Bananas", "Units": 7 },
    { "ProductID": "B202", "ProductName": "Bananas", "Units": 3 },
    { "ProductID": "C303", "ProductName": "Cherries", "Units": 8 }
  ]
}
```
Aşağıdaki örnek, bu işlemin nasıl çalıştığını gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-Using-JSON-Data-Subtotal.java" >}}

{{< app/cells/assistant language="java" >}}
