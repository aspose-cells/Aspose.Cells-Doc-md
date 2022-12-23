---
title: 将 JSON 转换为 CSV
type: docs
weight: 160
url: /zh/java/convert-json-to-csv/
---
Aspose.Cells 支持将简单和嵌套的 JSON 转换为 CSV。为此，API 提供[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)和[**Json工具**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)类。这[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)类提供 JSON 布局的选项，例如[**忽略数组标题**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle)（如果数组是对象的属性，则忽略标题）或[**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable)（将数组作为表格处理）。这[**Json工具**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)类使用设置的布局选项处理 JSON[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)班级。

下面的代码示例演示了使用[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)和[**Json工具**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)加载的类[源文件 JSON](SampleJson.json)并生成[输出 CSV 文件](SampleJson_out.csv).

## 示例代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.java" >}}
