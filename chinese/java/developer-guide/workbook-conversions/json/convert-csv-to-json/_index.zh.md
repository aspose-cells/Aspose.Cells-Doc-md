---
title: 将CSV转换为JSON
type: docs
weight: 170
url: /zh/java/convert-csv-to-json/
---

## **将CSV转换为JSON**

Aspose.Cells支持将CSV转换为JSON。为此，API提供了[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)和[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)类。[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)类提供了导出范围到JSON的选项。[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)类具有以下属性。

- [**ExportAsString**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#ExportAsString)：导出单元格的字符串值给JSON。
- [**HasHeaderRow**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#HasHeaderRow)：指示范围是否包含标题行。
- [**Indent**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#Indent)：表示缩进。

[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)类使用与[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)类设置的导出选项导出JSON。

以下代码示例演示了使用[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)和[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)类加载源CSV文件并在控制台上打印JSON输出。

### **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.java" >}}

### **控制台输出**

[
{
"id": 1,
"language": "Java",
"edition": "third",
"author": "Herbert Schildt",
"街道地址": 126,
"城市": "圣何塞",
"州": "CA",
"邮政编码": 394221
},
{
"id": 2,
"language": "C++",
"版本": "第二版",
"author": "EAAAA",
"街道地址": 126,
"城市": "圣何塞",
"州": "CA",
"邮政编码": 394221
},
{
"id": 3,
"语言": ".Net",
"版本": "第二版",
"作者": "E.Balagurusamy",
"街道地址": 126,
"城市": "圣何塞",
"州": "CA",
"邮政编码": 394221
}
]
