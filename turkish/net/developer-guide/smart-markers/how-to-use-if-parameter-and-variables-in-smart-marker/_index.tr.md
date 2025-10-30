---
title: Akıllı İşaretçilerde if Parametresi ve Değişkenler Nasıl Kullanılır
type: docs
weight: 10
url: /tr/net/how-to-use-if-parameter-and-Variables-in-smart-markers/
---

## **Akıllı İşaretçilerde if Parametresi ve Değişkenler Kullanmanın Nedenleri**
Akıllı İşaretçiler çeşitli bağlamlarda güçlü araçlardır. Akıllı İşaretçilerde parametrelerin ve değişkenlerin kullanımı, esnekliklerini, verimliliklerini ve işlevselliği önemli ölçüde artırır.

1. Dinamik Veri İşleme ve Esneklik: Parametreler ve değişkenler, Akıllı İşaretçilerin verileri dinamik olarak işlemesine olanak tanır, şablon veya kodda manuel ayar yapmaya gerek kalmadan değişen girdilere uyum sağlar.
2. Davranış ve İşlemler Üzerinde Kontrol: Parametreler, Akıllı İşaretçilerin davranışını ince ayar yapar, gruplayarak, sıralayarak, toplamlayarak ve koşullu biçimlendirme gibi işlemleri mümkün kılar.
3. Karmaşık Veri Yapılarını Destekleme: Değişkenler, Akıllı İşaretçilerin karmaşık veri kaynaklarıyla, diziler, nesneler ve çok boyutlu veriler dahil çalışmasına olanak tanır.
4. Verimlilik ve Otomasyon: Parametreler ve değişkenler, tekrarlayan görevleri otomatikleştirir, manuel çabayı ve olası hataları azaltır.
5. Koşullu Mantık ve Filtreleme: Bazı bağlamlarda sınırlı olsa da, parametreler ve değişkenler koşullu mantık uygulayabilir.
6. Özelleştirme ve Kullanıcı Etkileşimi: Değişkenler, kullanıcı girişlerinin, Akıllı İşaretçilerinin davranışını dinamik olarak özelleştirmesine olanak tanır.
7. Performans Optimizasyonu: Parametreler, verilerin işlenme şeklini kontrol ederek performansı optimize eder.


## **Akıllı İşaretçilerde if Parametresi ve Değişkenler Nasıl Kullanılır**
Bazen, Akıllı İşaretçilerde değişken parametrelerine if koşulu yargısı eklemeniz gerekir. Aspose.Cells, Akıllı İşaretçilerde if parametresi ve değişkenleri kullanmayı mümkün kılar. Lütfen [şablon dosyasını](template.xlsx), [json dosyasını](data.json) ve aşağıdaki kodla oluşturulan çıktı excel dosyasının ekran görüntüsünü kontrol edin.

|**variables gösteren template.xlsx dosyasının ilk çalışma sayfası.**|
| :- |
|![todo:image_alt_text](variables.png)|

|**Smart Markers gösteren template.xlsx dosyasının ikinci çalışma sayfası.**|
| :- |
|![todo:image_alt_text](template.png)|

|**Çıktı excel dosyasının ekran görüntüsü.**|
| :- |
|![todo:image_alt_text](result.png)|

Json verileri şu şekildedir:
```json data
{
    "Directors": [
        {
            "FirstName": "director first 1",
            "id": "director id 1",
            "LastName": "director last 1",
            "MiddleName": "director middle 1",
            "Reportees": [
                {
                    "City": "aaa city",
                    "Department": "aaa department",
                    "FirstName": "first aaa",
                    "GST": "Yes",
                    "id": "aaa",
                    "ITR": "No",
                    "LastName": "last aaa",
                    "MiddleName": "middle aaa"
                },
                {
                    "City": "bbb city",
                    "Department": "bbb department",
                    "FirstName": "first bbb",
                    "GST": "Yes",
                    "id": "bbb",
                    "ITR": "Yes",
                    "LastName": "last bbb",
                    "MiddleName": "middle bbb"
                },
                {
                    "City": "ccc city",
                    "Department": "ccc department",
                    "FirstName": "first ccc",
                    "GST": "No",
                    "id": "ccc",
                    "ITR": "No",
                    "LastName": "last ccc",
                    "MiddleName": "middle ccc"
                }
            ]
        },
        {
            "FirstName": "director first 2",
            "id": "director id 2",
            "LastName": "director last 2",
            "MiddleName": "director middle 2",
            "Reportees": [
                {
                    "City": "eee city",
                    "Department": "eee department",
                    "FirstName": "first eee",
                    "GST": "Yes",
                    "id": "eee",
                    "ITR": "No",
                    "LastName": "last eee",
                    "MiddleName": "middle eee"
                },
                {
                    "City": "fff city",
                    "Department": "fff department",
                    "FirstName": "first fff",
                    "GST": "No",
                    "id": "fff",
                    "ITR": "No",
                    "LastName": "last fff",
                    "MiddleName": "middle fff"
                }
            ]
        }
    ],
    "DOB": "2025-02-08",
    "EntityCin": "EntityCin Test",
    "EntityName": "EntityName Test",
    "FirstName": "FirstName Test",
    "LastName": "LastName Test",
    "MiddleName": "MiddleName Test",
    "SSN": "11111111"
}
```
Aşağıdaki örnek, bu işlemin nasıl çalıştığını gösterir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-If-Parameter-And-Variables.cs" >}}

{{< app/cells/assistant language="csharp" >}}
