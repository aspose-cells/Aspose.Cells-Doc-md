---
title: CSV den JSON a Dönüştürme
type: docs
weight: 170
url: /tr/java/convert-csv-to-json/
---

## **CSV'yi JSON'a dönüştür**

Aspose.Cells, CSV'yi JSON'a dönüştürmeyi destekler. Bu amaçla API, [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) ve [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) sınıflarını sağlar. [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) sınıfı, aralığı JSON şeklinde dışa aktarma seçeneklerini sağlar. [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) sınıfının aşağıdaki özellikleri bulunmaktadır.

- [**ExportAsString**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#ExportAsString): Bu, hücrelerin dize değerlerini JSON'a dışa aktarır.
- [**HasHeaderRow**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#HasHeaderRow): Bu, aralığın başlık satırı içerip içermediğini belirtir.
- [**Indent**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#Indent): Sekme boşluğunu belirtir.

[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) sınıfı, [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) sınıfı ile belirlenen dışa aktarma seçeneklerini kullanarak JSON'u dışa aktarır.

Aşağıdaki örnek kod, [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) ve [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) sınıflarını kullanarak [kaynak CSV dosyasını](SampleCsv.csv) yüklüyor ve çıktı [JSON'ı](SampleJson_out.csv) konsolda yazdırıyor.

### **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.java" >}}

### **Konsol Çıktısı**

{{< highlight java >}}

[
{
"id": 1,
"language": "Java",
"edition": "third",
"author": "Herbert Schildt",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 2,
"language": "C++",
"edition": "second",
"author": "EAAAA",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 3,
"language": ".Net",
"edition": "second",
"author": "E.Balagurusamy",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
}
]

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
