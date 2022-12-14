---
title: CSV'yi JSON'a dönüştür
type: docs
weight: 170
url: /tr/java/convert-csv-to-json/
---
## **CSV'yi JSON'a dönüştür**

Aspose.Cells, CSV'nin JSON'a dönüştürülmesini destekler. Bunun için API şunları sağlar:[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)ve[**Json Yardımcı Programı**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)sınıflar. bu[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)class, aralığı JSON'a dışa aktarma seçeneklerini sağlar. bu[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)sınıf aşağıdaki özelliklere sahiptir.

- [**ExportAsString**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#ExportAsString)Bu, hücrelerin dize değerini JSON'a aktarır.
- [**HasHeaderRow**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#HasHeaderRow): Bu, aralığın bir başlık satırı içerip içermediğini gösterir.
- [**Girinti**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#Indent): Girintiyi gösterir.

bu[**Json Yardımcı Programı**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)class ile ayarlanan dışa aktarma seçeneklerini kullanarak JSON'u dışa aktarır.[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)sınıf.

Aşağıdaki kod örneği, kullanımını gösterir[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)ve[**Json Yardımcı Programı**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)yüklemek için sınıflar[kaynak CSV dosyası](SampleCsv.csv)ve yazdırır[JSON](SampleJson_out.csv) konsolda çıktı.

### **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.java" >}}

### **Konsol Çıkışı**

[ { "id": 1, "language": "Java", "baskı": "üçüncü", "yazar": "Herbert Schildt", "streetAddress": 126, "şehir": "San Jone", "durum": "CA", "posta Kodu": 394221 }, { "id": 2, "dil": "C++", "edisyon": "ikinci", "yazar": "EAAAA", "streetAddress": 126, "şehir": "San Jone", "durum": "CA", "posta Kodu": 394221 }, { "id": 3 , "language": ".Net", "edition": "ikinci", "yazar": "E.Balagurusamy", "streetAddress": 126, "şehir": "San Jone", " durum": "CA", "postaKodu": 394221 } ]