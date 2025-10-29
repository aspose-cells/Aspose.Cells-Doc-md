---
title: 使用 Golang 通过 C++ 将 CSV 转换为 JSON
linktitle: 将CSV转换为JSON
type: docs
weight: 220
url: /zh/go-cpp/convert-csv-to-json/
description: 使用简单易用的Aspose.Cells for C++ API将CSV文件转换为JSON。
keywords: 转换，转换CSV为JSON，CSV转JSON，CSV，JSON，使用C++将CSV转换为JSON的代码
---

## **将CSV转换为JSON**

Aspose.Cells支持将CSV转换为JSON。为此，API提供了[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/)和[**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/)类。[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/)类提供导出范围至JSON的选项。[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/)类具有以下属性：

- [**GetExportAsString()**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/getexportasstring/)：导出单元格的字符串值给JSON。
- [**GetHasHeaderRow()**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/gethasheaderrow/)：指示范围是否包含标题行。
- [**GetIndent()**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/getindent/)：指示缩进。

[**JsonUtility**](https://reference.aspose.com/cells/go-cpp/jsonutility/)类使用[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/)类设置的导出选项导出JSON。

以下代码示例演示了如何使用 [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) 和 [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) 类加载 [源 CSV 文件](104398879.csv) 并在控制台中打印 JSON 输出。

### **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertCsvToJson.go" >}}
### **控制台输出**
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
