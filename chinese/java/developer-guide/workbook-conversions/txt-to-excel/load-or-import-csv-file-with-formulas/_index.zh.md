---
title: 加载或导入具有公式的CSV文件
type: docs
weight: 500
url: /zh/java/load-or-import-csv-file-with-formulas/
---

{{% alert color="primary" %}} 

CSV文件主要包含文本数据，不包含任何公式。但有时CSV文件也可能包含公式。这样的CSV文件应通过将[TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#HasFormula)设置为**true**来加载。设置此属性后，Aspose.Cells将不会将公式视为简单文本。它们将被视为公式，Aspose.Cells公式计算引擎将像往常一样处理它们。

{{% /alert %}} 
## **加载或导入带有公式的 CSV 文件**
下面的代码示例了如何加载和导入带有公式的CSV文件。您可以使用任何CSV文件。为了说明，我们使用了包含此数据的[simple csv file](5472505.csv)。如您所见，它包含一个公式。

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

代码先加载CSV文件，然后在单元格D4再次导入它。最后，以XSLX格式保存工作簿对象。[output XLSX文件](5472503.xlsx)如下所示。如您所见，单元格C3和F4包含公式及其结果800。

![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadOrImportCSVFile-LoadOrImportCSVFile.java" >}}
