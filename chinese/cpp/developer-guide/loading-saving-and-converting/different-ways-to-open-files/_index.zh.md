---
title: 打开文件的不同方式
linktitle: 打开文件的不同方式
type: docs
weight: 10
url: /zh/cpp/different-ways-to-open-files/
---
{{% alert color="primary" %}} 

使用 Aspose.Cells 可以打开文件，例如检索数据，或使用设计器模板来加快开发过程。 Aspose.Cells可以打开一系列不同的文件，例如Microsoft Excel电子表格（XLS、XLSX、XLSM、XLSB）、CSV或TabDelimited文件。

{{% /alert %}} 
##  **通过路径打开文件**
开发者可以通过在本地计算机上指定Microsoft Excel文件的文件路径来打开该文件。[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类构造函数。只需将构造函数中的路径作为字符串传递即可。 Aspose.Cells会自动检测文件格式类型。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingPath-new.cpp" >}}

##  **使用流打开文件**
还可以将 Excel 文件作为流打开。为此，请使用构造函数的重载版本，该构造函数采用*溪流*包含该文件的对象。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingStream-new.cpp" >}}

