---
title: 加载或导入具有公式的CSV文件
type: docs
weight: 350
url: /zh/python-net/load-or-import-csv-file-with-formulas/
description: 通过Aspose.Cells for Python通过.NET API加载或导入带有公式的CSV文件。
keywords: 使用带有公式的CSV文件，将带有公式的CSV转换为Excel在Python via NET中，将带有公式的CSV转换为xlsx，将带有公式的CSV加载到Excel文件。
---

{{% alert color="primary" %}} 

CSV文件主要包含文本数据，不包含任何公式。然而，有时候CSV文件也可能包含公式。应该通过将[TxtLoadOptions.has_formula](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/has_formula/)设置为**true**来加载这种CSV文件。一旦将此属性设置为**true**，Aspose.Cells将不会将公式视为简单文本。它们将被视为公式，Aspose.Cells的公式计算引擎将像往常一样处理它们。

{{% /alert %}} 

以下代码演示了如何加载和导入带有公式的CSV文件。您可以使用任何CSV文件。为了举例说明，我们使用包含此数据的[简单csv文件](5115034.csv)。正如您所看到的，它包含一个公式。

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ImportCSVWithFormulas-ImportCSVWithFormulas.py" >}}



该代码首先加载CSV文件，然后将其再次导入到单元格D4。最后，将工作簿对象保存为XSLX格式。[输出XLSX文件](5115052.xlsx)如下所示。您可以看到单元格C3和F4包含公式及其结果800。

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |

