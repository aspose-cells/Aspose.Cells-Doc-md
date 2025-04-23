---
title: 在智能标记字段中使用Formula参数
type: docs
weight: 40
url: /zh/net/using-formula-parameter-in-smart-marker-field/
---


## **可能的使用场景**
有时，您想要在智能标记字段中嵌入公式。本文介绍了如何使用*公式*参数在智能标记字段中嵌入公式。
## **在智能标记变量名为Test及其数据源名称也为Test中嵌入公式的下面样本代码是这样子的 **&=$Test(formula)**，在执行代码后，[最终的输出Excel文件](47153156.xlsx)将在A1到A5单元格中具有公式。**
以下示例代码将公式嵌入名为TestFormula的智能标记字段，其数据源名称为MyDataSource，因此带公式参数的完整字段如 &=MyDataSource.TestFormula(公式)，执行代码后，[最终输出的Excel文件](46465047.xlsx)将在单元格A1到A5中具有公式。
## **示例代码**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingFormulaParameterInSmartMarkerField.cs" >}}
{{< app/cells/assistant language="csharp" >}}
