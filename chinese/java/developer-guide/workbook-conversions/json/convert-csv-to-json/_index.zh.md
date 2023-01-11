﻿---
title: 将 CSV 转换为 JSON
type: docs
weight: 170
url: /zh/java/convert-csv-to-json/
---
## **将 CSV 转换为 JSON**

Aspose.Cells 支持将 CSV 转换为 JSON。为此，API 提供[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)和[**Json工具**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)类。这[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)类提供了将范围导出到 JSON 的选项。[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)类具有以下属性。

- [**导出为字符串**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#ExportAsString)：这会将单元格的字符串值导出为 JSON。
- [**有标题行**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#HasHeaderRow)：这表示范围是否包含标题行。
- [**缩进**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#Indent)表示缩进。

这[**Json工具**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)类使用设置的导出选项导出 JSON[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)班级。

下面的代码示例演示了使用[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)和[**Json工具**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)加载的类[源文件 CSV](SampleCsv.csv)并打印[JSON](SampleJson_out.csv)在控制台输出。

### **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.java" >}}

### **控制台输出**

[