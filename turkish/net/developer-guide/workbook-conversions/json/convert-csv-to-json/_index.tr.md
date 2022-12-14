---
title: CSV'yi JSON'a dönüştür
type: docs
weight: 220
url: /tr/net/convert-csv-to-json/
description: Kullanımı kolay Aspose.Cells for .NET API'i kullanarak CSF dosyasını JSON'a dönüştürün.
keywords: Convert, Convert CVS to JSON, CSV to JSON, CSV, JSON, Convert CSV to JSON CSharp, c# code to convert CSV to JSON
---
## **CSV'yi JSON'a dönüştür**

Aspose.Cells, CSV'nin JSON'a dönüştürülmesini destekler. Bunun için API şunları sağlar:**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**ve**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)** sınıflar. bu**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**class, aralığı JSON'a dışa aktarma seçeneklerini sağlar. bu**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**sınıf aşağıdaki özelliklere sahiptir.

- **[ExportAsString](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/exortasstring)**Bu, hücrelerin dize değerini JSON'a aktarır.
- **[HasHeaderRow](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/hasheaderrow)**: Bu, aralığın bir başlık satırı içerip içermediğini gösterir.
- **[Girinti](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/indent)**: Girintiyi gösterir.

bu**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**class ile ayarlanan dışa aktarma seçeneklerini kullanarak JSON'u dışa aktarır.**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**sınıf.

Aşağıdaki kod örneği, kullanımını gösterir**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**ve**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**yüklemek için sınıflar[kaynak CSV dosyası](104398879.csv)ve JSON çıktısını konsolda yazdırır.

### **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.cs" >}}

### **Konsol Çıkışı**
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