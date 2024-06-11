---
title: 加载或导入具有公式的CSV文件
type: docs
weight: 350
url: /zh/python-net/load-or-import-csv-file-with-formulas/
description: 通过使用Aspose.Cells for Python via .NET API，加载或导入带有公式的CSV文件。
keywords: Python加载或导入带有公式的CSV文件，Python将带有公式的CSV文件转换为Excel via NET，Python将带有公式的CSV转换为xlsx，加载带有公式的CSV文件到Excel文件。
---

{{% alert color="primary" %}} 

CSV文件通常包含文本数据，它们不包含任何公式。但有时会出现CSV文件也包含公式的情况。应该将这样的CSV文件加载时设置TxtLoadOptions.has_formula属性为true。一旦将此属性设置为true，Aspose.Cells将不会将公式视为简单文本。它们将被视为公式，Aspose.Cells的公式计算引擎将像往常一样处理它们。

{{% /alert %}} 

以下代码说明了如何加载和导入带有公式的CSV文件。您可以使用任何CSV文件。为了演示目的，我们使用包含此数据的**[简单csv文件](5115034.csv)**。如您所见，它包含一个公式。

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ImportCSVWithFormulas-ImportCSVWithFormulas.py" >}}



代码首先加载CSV文件，然后将其再次导入到单元格D4。最后，它将工作簿对象另存为XSLX格式。**[输出的XLSX文件](5115052.xlsx)**看起来是这样的。如您所见，单元格C3和F4包含公式及其结果800。

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |

