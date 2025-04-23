---
title: CSV den JSON a Dönüştürme
type: docs
weight: 220
url: /tr/net/convert-csv-to-json/
description: Aspose.Cells, Aspose.Cells for .NET API sini kullanarak CSF dosyasını JSON a dönüştürmeyi sağlar.
keywords: CSV den JSON a Dönüştürme
---

## **CSV'yi JSON'a dönüştür**

Aspose.Cells, CSV'nin JSON'a dönüştürülmesini destekler. Bunun için API, [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions) ve [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) sınıflarını sağlar. [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions) sınıfı, JSON'a dönüştürmek için aralık ihracatı için seçenekler sağlar. [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions) sınıfında aşağıdaki özellikler bulunmaktadır.

- [**ExportAsString**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/exportasstring): Bu, hücrelerin dize değerlerini JSON'a dışa aktarır.
- [**HasHeaderRow**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/hasheaderrow): Bu, aralığın başlık satırı içerip içermediğini belirtir.
- [**Indent**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/indent): Sekme boşluğunu belirtir.

[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) sınıfı, [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions) sınıfı ile belirlenen dışa aktarma seçeneklerini kullanarak JSON'u dışa aktarır.

Aşağıdaki kod örneği, [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions) ve [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) sınıflarını kullanarak [kaynak CSV dosyasını](104398879.csv) yükler ve konsolda JSON çıktısını yazdırır.

### **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.cs" >}}

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
{{< app/cells/assistant language="csharp" >}}
