---
title: 在Aspose.Cells中使用FormulaText函数
description: 本文介绍了如何使用Aspose.Cells库中的FormulaText函数处理Microsoft Excel中的公式。通过加载现有的Excel文件或创建新的Excel文件，我们可以使用Aspose.Cells提供的方法获取和设置单元格的公式文本并获取结果。最后，我们将修改后的Excel文件保存到磁盘。
keywords: Aspose.Cells, Excel, FormulaText函数
type: docs
weight: 60
url: /zh/net/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText是Excel 2013及以后的函数。不支持以前的版本，如Excel 2010或2007等。正如其名称所示，它打印给定单元格中存在的公式的文本。本文将向您展示如何使用Aspose.Cells利用此函数。

{{% /alert %}} 

以下示例代码显示了如何使用Aspose.Cells中的FormulaText。代码首先在单元格A1中编写一个公式，然后使用FormulaText在单元格A2中打印出公式的文本。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingFormulaTextFunction-UsingFormulaTextFunction.cs" >}}
## **控制台输出**
这是上面示例代码的控制台输出。

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
