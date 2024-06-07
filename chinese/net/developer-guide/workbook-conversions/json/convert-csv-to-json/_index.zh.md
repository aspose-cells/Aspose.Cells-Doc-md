---
title: 将CSV转换为JSON
type: docs
weight: 220
url: /zh/net/convert-csv-to-json/
description: 通过易于使用的Aspose.Cells for .NET API将CSF文件转换为JSON。
keywords: 转换，将CVS转换为JSON，CSV转JSON，CSV，JSON，将CSV转换为JSON CSharp，转换CSV为JSON的C#代码
---

## **将CSV转换为JSON**

Aspose.Cells支持将CSV转换为JSON。为此，API提供了ExportRangeToJsonOptions和JsonUtility类。ExportRangeToJsonOptions类提供了将范围导出到JSON的选项。ExportRangeToJsonOptions类具有以下属性。

- [ExportAsString](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetooptions/properties/exportasstring)：将单元格的字符串值导出到JSON。
- [HasHeaderRow](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetooptions/properties/hasheaderrow)：指示范围是否包含标题行。
- [Indent](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetooptions/properties/indent)：指示缩进。

JsonUtility类使用与ExportRangeToJsonOptions类设置的导出选项导出JSON。

以下代码示例演示了使用ExportRangeToJsonOptions和JsonUtility类加载源CSV文件，并在控制台中打印JSON输出。

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
