---
title: 加载或导入具有公式的CSV文件
type: docs
weight: 350
url: /zh/net/load-or-import-csv-file-with-formulas/
---

{{% alert color="primary" %}} 

CSV文件通常包含文本数据，不包含任何公式。然而，有时会发生CSV文件也包含公式。应该将这样的CSV文件设置[TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/hasformula)为true来加载。一旦此属性设置为true，Aspose.Cells将不将公式视为简单文本。它们将被视为公式，Aspose.Cells的公式计算引擎将像往常一样处理它们。

{{% /alert %}} 

以下代码演示了如何加载和导入带有公式的CSV文件。您可以使用任何CSV文件。为了举例说明，我们使用包含此数据的[简单csv文件](5115034.csv)。正如您所看到的，它包含一个公式。

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ImportCSVWithFormulas-ImportCSVWithFormulas.cs" >}}



该代码首先加载CSV文件，然后将其再次导入到单元格D4。最后，将工作簿对象保存为XSLX格式。[输出XLSX文件](5115052.xlsx)如下所示。您可以看到单元格C3和F4包含公式及其结果800。

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |

