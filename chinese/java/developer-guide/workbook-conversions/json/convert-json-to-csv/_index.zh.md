---
title: 将JSON转换为CSV
type: docs
weight: 160
url: /zh/java/convert-json-to-csv/
---

Aspose.Cells支持将简单和嵌套的JSON转换为CSV。为此，API提供了[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)和[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)类。[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)类提供了JSON布局的选项，比如[**IgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle)(如果数组是对象的属性，则忽略标题)或者[**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable)(将数组处理为表)。[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)类使用与[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)类设置的布局选项处理JSON。

以下代码示例演示了如何使用[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)和[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)类加载[source JSON file](SampleJson.json)并生成[output CSV file](SampleJson_out.csv)。

## 示例代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.java" >}}
