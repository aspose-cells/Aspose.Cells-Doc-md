---
title: CSV den JSON a Dönüştürme
type: docs
weight: 220
url: /tr/python-net/convert-csv-to-json/
description: Aspose.Cells for Python via .NET API sını kullanarak CSV yi JSON a dönüştürme.
keywords: CSV yi JSON a, Python da CSV yi JSON a dönüştür, CSV yi JSON a dönüştürme via NET, Python da CSV yi JSON a dönüştürme, CSV yi JSON olarak kaydetme
---

## **CSV'yi JSON'a dönüştür**

Aspose.Cells for Python via .NET, CSV'yi JSON'a dönüştürmeyi destekler. Bunun için API, [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) ve [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) sınıflarını sağlar. [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) sınıfı, aralığı JSON'a aktarma seçeneklerini sağlar. [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) sınıfı ise aşağıdaki özelliklere sahiptir.

- [**export_as_string**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/export_as_string/): Bu, hücrelerin dize değerlerini JSON'a dışa aktarır.
- [**has_header_row**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/has_header_row/): Bu, aralığın başlık satırı içerip içermediğini belirtir.
- [**indent**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/indent/): Sekme boşluğunu belirtir.

[**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) sınıfı, [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) sınıfı ile belirlenen dışa aktarma seçeneklerini kullanarak JSON'u dışa aktarır.

Aşağıdaki kod örneği, [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) ve [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) sınıflarını kullanarak [kaynak CSV dosyasını](104398879.csv) yükler ve konsolda JSON çıktısını yazdırır.

### **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.py" >}}

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
{{< app/cells/assistant language="python-net" >}}
