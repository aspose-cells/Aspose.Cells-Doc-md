---
title: CSV'i JSON'e dönüştür
type: docs
weight: 220
url: /tr/python-net/convert-csv-to-json/
description: Aspose.Cells for Python via .NET API'i kullanarak CSV'i JSON'e dönüştürün.
keywords: Convert CVS to JSON, Convert CSV to JSON in Python via NET, Python convert CSV to JSON, Save CSV to JSON
---
##  **CSV'i JSON'e dönüştür**

Aspose.Cells for Python via .NET, CSV'in JSON'e dönüştürülmesini destekler. Bunun için API şunları sağlar:**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**Ve**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)** sınıflar.**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**sınıfı, aralığı JSON'e aktarma seçenekleri sunar.**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**sınıf aşağıdaki özelliklere sahiptir.

- *[ihracat_as_string](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/export_as_string/)**: Bu, hücrelerin dize değerini JSON'e aktarır.
- *[has_header_row](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/has_header_row/)**: Bu, aralığın bir başlık satırı içerip içermediğini gösterir.
- *[girinti](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/indent/)**: Girintiyi belirtir.

**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)**sınıf, ile ayarlanan dışa aktarma seçeneklerini kullanarak JSON'i dışa aktarır.**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**sınıf.

Aşağıdaki kod örneği kullanımını gösterir:**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**Ve**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)** yüklenecek sınıflar[kaynak CSV dosyası](104398879.csv)ve konsolda JSON çıktısını yazdırır.

###  **Basit kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.py" >}}

###  **Konsol Çıkışı**
```json
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
```