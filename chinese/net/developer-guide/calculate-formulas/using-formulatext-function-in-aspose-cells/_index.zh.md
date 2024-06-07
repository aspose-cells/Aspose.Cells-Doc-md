---
title: 在Aspose.Cells中使用FormulaText函数
description: 该文章介绍了如何在Aspose.Cells库中使用FormulaText函数处理Microsoft Excel中的公式。通过加载现有的Excel文件或创建新的Excel文件，我们可以使用Aspose.Cells提供的方法获取和设置单元格的公式文本并获取结果。最后，我们将修改后的Excel文件保存到磁盘。
keywords: Aspose.Cells, Excel, FormulaText函数
type: docs
weight: 60
url: /zh/net/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText是Excel 2013及以后版本的功能。它不受以前版本如Excel 2010或2007等的支持。顾名思义，它打印给定单元格中存在的公式的文本。本文将向您展示如何使用Aspose.Cells使用此功能。

{{% /alert %}} 

以下示例代码显示了在Aspose.Cells中使用FormulaText的用法。该代码首先在单元格A1中编写一个公式，然后在单元格A2中使用FormulaText打印公式的文本。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingFormulaTextFunction-UsingFormulaTextFunction.cs" >}}
## **控制台输出**
这是上述示例代码的控制台输出。

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
