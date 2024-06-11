---
title: 在智能标记字段中使用Formula参数
type: docs
weight: 30
url: /zh/java/using-formula-parameter-in-smart-marker-field/
---

## **可能的使用场景**
有时，您想在智能标记字段中嵌入公式。本文介绍了如何使用Formula参数在智能标记字段中嵌入公式。
## **在智能标记变量名为Test及其数据源名称也为Test中嵌入公式的下面样本代码是这样子的 **&=$Test(formula)**，在执行代码后，[最终的输出Excel文件](47153156.xlsx)将在A1到A5单元格中具有公式。**
下面的示例代码将在名为Test的智能标记变量中嵌入公式，其数据源名称也为Test，因此带有公式参数的完整字段看起来像**&=$Test(formula)**，执行代码后，[最终输出的Excel文件](47153156.xlsx)中将在A1到A5单元格中包含公式。
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-SmartMarkers-UsingFormulaParameterInSmartMarkerField.java" >}}
