---
title: 将 CSV 转换为 JSON
type: docs
weight: 220
url: /zh/python-net/convert-csv-to-json/
description: 使用 Aspose.Cells for Python via .NET API 将 CSV 转换为 JSON。
keywords: Convert CVS to JSON, Convert CSV to JSON in Python via NET, Python convert CSV to JSON, Save CSV to JSON
---
##  **将 CSV 转换为 JSON**

Aspose.Cells for Python via .NET 支持将 CSV 转换为 JSON。为此，API 提供**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**和**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)**类。这**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**类提供了将范围导出到 JSON 的选项。**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**类具有以下属性。

- *[导出为字符串](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/export_as_string/)**：这会将单元格的字符串值导出到 JSON。
- *[有_标题_行](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/has_header_row/)**：这指示该范围是否包含标题行。
- *[缩进](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/indent/)**：表示缩进。

这**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)**类使用设置的导出选项导出 JSON**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**班级。

下面的代码示例演示了使用**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**和**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)**类来加载[源CSV文件](104398879.csv)并在控制台中打印 JSON 输出。

###  **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.py" >}}

###  **控制台输出**
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