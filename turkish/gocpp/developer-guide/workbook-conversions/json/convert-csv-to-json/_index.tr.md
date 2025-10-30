---
title: CSV yi JSON a Dönüştür, Golang ve C++ ile
linktitle: CSV den JSON a Dönüştürme
type: docs
weight: 220
url: /tr/go-cpp/convert-csv-to-json/
description: Basit kullanımlı Aspose.Cells for C++ API sini kullanarak CSV dosyasını JSON a dönüştürün.
keywords: Dönüştür, CSV yi JSON a Dönüştür, CSV to JSON, CSV, JSON, CSV yi JSON a Dönüştür C++, C++ kodu CSV yi JSON a dönüştürmek için
---

## **CSV'yi JSON'a dönüştür**

Aspose.Cells, CSV'yi JSON'a dönüştürmeyi destekler. Bunun için API [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) ve [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) sınıflarını sağlar. [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) sınıfı, JSON'e dışa aktarım için aralık seçenekleri sunar. [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) sınıfının aşağıdaki özellikleri vardır.

- [**GetExportAsString()**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/getexportasstring/): Bu, hücrelerin dize değerlerini JSON'a dışa aktarır.
- [**GetHasHeaderRow()**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/gethasheaderrow/): Bu, aralığın başlık satırı içerip içermediğini belirtir.
- [**GetIndent()**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/getindent/): Girintiyi gösterir.

[**JsonUtility**](https://reference.aspose.com/cells/go-cpp/jsonutility/) sınıfı, JSON'u [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/) sınıfıyla belirlenen dışa aktarma seçeneklerini kullanarak dışa aktarır.

Aşağıdaki kod örneği, [kaynak CSV dosyasını](104398879.csv) yüklemek için [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) ve [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) sınıflarını kullanmayı ve JSON çıkışını konsolda yazdırmayı göstermektedir.

### **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertCsvToJson.go" >}}
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
