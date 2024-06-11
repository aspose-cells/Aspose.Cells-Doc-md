---
title: 加载或导入具有公式的CSV文件
type: docs
weight: 500
url: /zh/java/load-or-import-csv-file-with-formulas/
---

{{% alert color="primary" %}} 

CSV文件通常包含文本数据，不包含任何公式。但有时CSV文件也包含公式。应将此类CSV文件通过将[TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#HasFormula)设置为**true**来加载。一旦将此属性设置为**true**，Aspose.Cells将不会将公式视为简单文本。它们将被视为公式，并且Aspose.Cells公式计算引擎将像往常一样处理它们。

{{% /alert %}} 
## **加载或导入带公式的CSV文件**
以下代码说明了您如何加载和导入带有公式的CSV文件。您可以使用任何CSV文件。为了说明的目的，我们使用了包含此数据的[简单csv文件](5472505.csv)。如您所见它包含一个公式。

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

代码首先加载CSV文件，然后再次导入到单元格D4中。最后，将工作簿对象以XSLX格式保存。[输出XLSX文件](5472503.xlsx)的外观如下。如您所见，单元格C3和F4包含公式及其结果800。

![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadOrImportCSVFile-LoadOrImportCSVFile.java" >}}
