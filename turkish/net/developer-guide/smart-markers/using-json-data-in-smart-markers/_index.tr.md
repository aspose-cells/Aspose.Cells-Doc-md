---
title: Excel’e Smart Markers ile JSON Nasıl Akıllıca İçe Aktarılır
type: docs
weight: 30
url: /tr/net/how-to-import-json-into-excel-with-smart-markers/
alias: [/net/using-json-data-in-smart-markers/]
---

## **Smart Markers için Json Verisinin Kullanımının Nedenleri**
Smart Markers için Orijinal Veri Olarak JSON Verisi Neden Kullanılır?
JSON (JavaScript Nesne Gösterimi) hafif, insan tarafından okunabilir bir veri alışveriş formatıdır ve hiyerarşik verilerin yapılandırılması için idealdir. İşte neden smart marker'lar (otomatik doldurma alanları olan dinamik yer tutucular) için uygun olduğunu gösterir:

1. Yapısal ve Hiyerarşik Veri Desteği
JSON yerel olarak gömülü nesneleri ve dizileri destekler (örn., { "kullanici": { "ad": "Alice", "siparisler": [ ... ] } }). Smart marker'lar bu hiyerarşiyi gezebilir (örn., {{kullanici.siparisler[0].fiyat}}), böylece karmaşık verilerin şablonlara eşlenmesi kolaylaşır.

2. Dil ve Platform Bağımsız
JSON parserleri hemen hemen tüm programlama dillerinde mevcuttur (Python, JavaScript, Java, vb.). Excel Power Query, Google Apps Script veya kod yazmadan platformlar (ör., Airtable) JSON’u sorunsuzca işler.

3. API Uyumlu
En modern API’ler (ör., REST, GraphQL) JSON formatında veri döndürür. Smart marker’lar canlı JSON verisini doğrudan web servislerinden alabilir, bu da gerçek zamanlı veri güncellemelerine olanak sağlar (örn., hisse senedi fiyatları, hava durumu).

4. İnsan Tarafından Okunabilir ve Hata Ayıklanabilir
JSON’ın düz metin yapısı, doğrulama (örn., JSONLint kullanılarak), manuel veya script ile düzenleme ve haritalama sırasında hata ayıklama işlemlerini kolaylaştırır.

5. Ölçeklenebilirlik ve Esneklik
JSON’daki alanları ekleme veya kaldırma, mevcut smart marker’ları bozmaz (seçmeli alanlar uygun şekilde yönetilirse). Dize, sayı, boolean, diziler ve nesneler gibi çeşitli veri türlerini destekler.

6. Ekosistem Uyumluluğu
Modern veri araçlarıyla çalışır: Veritabanları: MongoDB, PostgreSQL (JSONB), vb. Otomasyon araçları: Zapier, Integromat. Veri boru hatları: Apache NiFi, Talend.

## **Excel Nested Şablon ile JSON Verisi Kullanımı**
Aspose.Cells for .NET akıllı göstericilerde json verisini destekler, json verisi hiyerarşik olarak iç içe olabilir. Lütfen [şablon dosyasını](smartmarker.xlsx), [json dosyasını](smartmarker.json) ve aşağıdaki kodla oluşturulan çıktı excel dosyasının ekran görüntüsünü kontrol edin.

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

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-JSON-Data.cs" >}}


## **Excel Alt Toplam Şablonu ile JSON Verisi Kullanımı**
Aspose.Cells for .NET akıllı göstericilerde json verisini destekler, json verisi hiyerarşik olarak iç içe olabilir. Alt toplam, excel şablonunda veri istatistikleri için kullanıldı. Lütfen [şablon dosyasını](jsonExcelTemplate.xlsx), [json dosyasını](jsonData.json) ve aşağıdaki kodla oluşturulan çıktı excel dosyasının ekran görüntüsünü kontrol edin.

|**jsonExcelTemplate.xlsx dosyasının ilk sayfasında akıllı göstergeler gösteriliyor.**|
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

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-JSON-Data-Subtotal.cs" >}}

{{< app/cells/assistant language="csharp" >}}
