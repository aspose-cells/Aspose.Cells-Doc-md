---
title: 将 CSV 转换为 JSON
type: docs
weight: 220
url: /zh/net/convert-csv-to-json/
description: 使用简单易用的 Aspose.Cells for .NET API 将 CSF 文件转换为 JSON。
keywords: Convert, Convert CVS to JSON, CSV to JSON, CSV, JSON, Convert CSV to JSON CSharp, c# code to convert CSV to JSON
---
## **将 CSV 转换为 JSON**

Aspose.Cells 支持将 CSV 转换为 JSON。为此，API 提供**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**和**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**类。这**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**类提供将范围导出到 JSON 的选项。这**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**类具有以下属性。

- **[ExportAsString](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/exportasstring)**：这会将单元格的字符串值导出到 JSON。
- **[HasHeaderRow](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/hasheaderrow)**：这表示范围是否包含标题行。
- **[缩进](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/indent)**表示缩进。

这**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**类使用设置的导出选项导出 JSON**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**班级。

下面的代码示例演示了使用**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**和**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**加载的类[源 CSV 文件](104398879.csv)并在控制台中打印 JSON 输出。

### **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.cs" >}}

### **控制台输出**
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