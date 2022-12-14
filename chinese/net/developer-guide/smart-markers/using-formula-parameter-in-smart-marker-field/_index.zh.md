---
title: 在智能标记字段中使用公式参数
type: docs
weight: 40
url: /zh/net/using-formula-parameter-in-smart-marker-field/
---
## **可能的使用场景**
有时，您想在智能标记字段中嵌入公式。本文介绍了如何使用*公式*在智能标记字段中嵌入公式的参数。
## **在智能标记字段中使用公式参数**
以下示例代码将公式嵌入名为TestFormula的智能标记字段中，其数据源名称为MyDataSource，因此带有公式参数的完整字段类似于&=MyDataSource.TestFormula(formula)，代码执行后，[最终输出Excel文件](46465047.xlsx)将在 A1 到 A5 的单元格中包含公式。
## **示例代码**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingFormulaParameterInSmartMarkerField.cs" >}}
