---
title: 将CSV转换为JSON
type: docs
weight: 170
url: /zh/java/convert-csv-to-json/
---

## **将CSV转换为JSON**

Aspose.Cells 支持将 CSV 转换为 JSON。为此，API 提供了 [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) 和 [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) 类。 [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) 类为导出范围到 JSON 提供选项。 [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) 类具有以下属性。

- [**ExportAsString**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#ExportAsString): 将单元格的字符串值导出为 JSON。
- [**HasHeaderRow**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#HasHeaderRow): 指示范围是否包含标题行。
- [**Indent**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#Indent): 指示缩进。

  [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) 类使用 [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) 类设置的导出选项导出 JSON。

以下代码示例演示了使用 [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) 和 [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) 类加载 [源 CSV 文件](SampleCsv.csv) 并在控制台中打印 [JSON](SampleJson_out.csv) 输出。

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
"作者": "EAAAA",
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
