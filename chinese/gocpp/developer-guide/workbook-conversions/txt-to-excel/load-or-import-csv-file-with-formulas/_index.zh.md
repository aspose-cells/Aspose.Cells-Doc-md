---
title: 使用C++加载或导入带有公式的CSV文件。
linktitle: 加载或导入具有公式的CSV文件
type: docs
weight: 350
url: /zh/go-cpp/load-or-import-csv-file-with-formulas/
description: 使用Golang通过C++加载或导入包含公式的CSV文件
---

{{% alert color="primary" %}} 

CSV文件主要包含文本数据，通常不包含任何公式。但是，也存在CSV文件可能包含公式的情况。此类CSV文件应通过将[TxtLoadOptions.GetHasFormula()](https://reference.aspose.com/cells/go-cpp/txtloadoptions/gethasformula/)设为**true**来加载。将此属性设为**true**后，Aspose.Cells不会将公式当作普通文本，而会将其作为公式，Aspose.Cells的公式计算引擎会正常处理它们。

{{% /alert %}} 

以下代码演示如何加载和导入带有公式的CSV文件。你可以使用任何CSV文件。为了示例，我们使用包含此数据的 [简单CSV文件](5115034.csv)，如你所见，它包含一个公式。

{{< highlight cpp >}}
 300,500,=Sum(A1:B1)
{{< /highlight >}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadOrImportCsvFileWithFormulas.go" >}}
代码首先加载CSV文件，然后在单元格D4处重新导入，并最终将工作簿保存为XLSX格式。输出的 XLSX 文件（[链接](5115052.xlsx)）如下所示。你可以看到，单元格C3和F4包含公式，其结果为800。

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |
