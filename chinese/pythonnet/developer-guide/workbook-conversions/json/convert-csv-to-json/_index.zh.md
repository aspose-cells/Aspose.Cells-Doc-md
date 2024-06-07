---
title: 将CSV转换为JSON
type: docs
weight: 220
url: /zh/python-net/convert-csv-to-json/
description: 通过使用Aspose.Cells for Python通过.NET API将CSV转换为JSON。
keywords: 将CVS转换为JSON，在Python via NET中将CSV转换为JSON，Python将CSV转换为JSON，保存CSV为JSON
---

## **将CSV转换为JSON**

Aspose.Cells for Python通过.NET支持将CSV转换为JSON。为此，API提供了**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**和**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)**类。**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**类提供了导出范围到JSON的选项。**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**类包含以下属性。

- **[export_as_string](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/export_as_string/)**: 这将将单元格的字符串值导出为JSON。
- **[has_header_row](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/has_header_row/)**: 这指示范围是否包含标题行。
- **[indent](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/indent/)**: 指示缩进。

**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)**类使用与**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**类设置的导出选项导出JSON。

以下代码示例演示了如何使用**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**和**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)**类加载[源CSV文件](104398879.csv)并在控制台上打印JSON输出。

### **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.py" >}}

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
