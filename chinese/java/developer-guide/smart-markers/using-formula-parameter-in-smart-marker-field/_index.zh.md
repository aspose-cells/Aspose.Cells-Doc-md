---
title: 在智能标记字段中使用公式参数
type: docs
weight: 30
url: /zh/java/using-formula-parameter-in-smart-marker-field/
---
## **可能的使用场景**
有时，您想在智能标记字段中嵌入公式。本文介绍如何使用公式参数在智能标记字段中嵌入公式。
## **在智能标记字段中使用公式参数**
以下示例代码将公式嵌入名为Test的智能标记变量中，其数据源名称也为Test，因此带有公式参数的完整字段如下所示**&=$测试（公式）**在执行代码之后，[最终输出Excel文件](47153156.xlsx)将在 A1 到 A5 的单元格中包含公式。
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-SmartMarkers-UsingFormulaParameterInSmartMarkerField.java" >}}
