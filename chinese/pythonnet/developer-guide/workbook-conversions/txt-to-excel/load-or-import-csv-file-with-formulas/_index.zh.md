---
title: 使用公式加载或导入 CSV 文件
type: docs
weight: 350
url: /zh/python-net/load-or-import-csv-file-with-formulas/
description: 使用 Aspose.Cells for Python via .NET API 加载或导入包含公式的 CSV 文件。
keywords: Python Load or Import CSV file with Formulas, Convert CSV with Formulas to Excel in Python via NET, Python convert CSV with Formulas to xlsx, Load CSV with Formulas to Excel file.
---
{{% alert color="primary" %}} 

 CSV 文件主要包含文本数据，不包含任何公式。但是，有时 CSV 文件也包含公式。这样的 CSV 文件应该通过设置来加载[TxtLoadOptions.has_formula](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/has_formula/)作为*真实**。一旦设置此属性为“true”，Aspose.Cells 将不会将公式视为简单文本。它们将被视为公式，Aspose.Cells 公式计算引擎将照常处理它们。

{{% /alert %}} 

以下代码说明了如何加载和导入带有公式的 CSV 文件。您可以使用任何 CSV 文件。为了说明目的，我们使用[简单的 csv 文件](5115034.csv)其中包含此数据。如您所见，它包含一个公式。

{{< highlight "java" >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ImportCSVWithFormulas-ImportCSVWithFormulas.py" >}}



该代码首先加载 CSV 文件，然后在单元格 D4 中再次导入它。最后，它以 XSLX 格式保存工作簿对象。这[输出XLSX文件](5115052.xlsx)看起来像这样。如您所见，单元格 C3 和 F4 包含公式及其结果 800。

|![待办事项：图像_替代_文本](load-or-import-csv-file-with-formulas_1.png)|
| :- |

