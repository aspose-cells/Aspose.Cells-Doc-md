---
title: 使用公式加载或导入 CSV 文件
type: docs
weight: 500
url: /zh/java/load-or-import-csv-file-with-formulas/
---
{{% alert color="primary" %}} 

CSV 文件主要包含文本数据，不包含任何公式。但是有时会发生 CSV 文件也包含公式。此类 CSV 文件应通过设置加载[TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#HasFormula)到**真的** .一旦这个属性将被设置为**真的**Aspose.Cells 不会将公式视为简单文本。它们将被视为公式，Aspose.Cells 公式计算引擎将照常处理它们。

{{% /alert %}} 
## **使用公式加载或导入 CSV 文件**
以下代码说明了如何加载和导入带有公式的 CSV 文件。您可以使用任何 CSV 文件。为了说明的目的，我们使用[简单的csv文件](5472505.csv)其中包含此数据。如您所见，它包含一个公式。

{{< highlight "java" >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

代码首先加载 CSV 文件，然后在单元格 D4 中再次导入它。最后，它以 XSLX 格式保存工作簿对象。这[输出 XLSX 文件](5472503.xlsx)看起来像这样。如您所见，单元格 C3 和 F4 包含公式及其结果 800。

![待办事项：图片_替代_文本](load-or-import-csv-file-with-formulas_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadOrImportCSVFile-LoadOrImportCSVFile.java" >}}
