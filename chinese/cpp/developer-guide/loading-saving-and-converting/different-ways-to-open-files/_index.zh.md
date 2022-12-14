---
title: 打开文件的不同方法
linktitle: 打开文件的不同方法
type: docs
weight: 10
url: /zh/cpp/different-ways-to-open-files/
---
{{% alert color="primary" %}} 

使用 Aspose.Cells 可以打开文件，例如检索数据，或使用设计器模板来加快开发过程。 Aspose.Cells 可以打开一系列不同的文件，例如 Microsoft Excel 电子表格（XLS、XLSX、XLSM、XLSB）、CSV 或 TabDelimited 文件。

{{% /alert %}} 
## **通过路径打开文件**
开发人员可以通过在本地计算机上指定它的文件路径来打开 Microsoft Excel 文件[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)类构造函数。只需将构造函数中的路径作为字符串传递即可。 Aspose.Cells 会自动检测文件格式类型。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingPath.cpp" >}}

## **使用流打开文件**
也可以将 Excel 文件作为流打开。为此，请使用构造函数的重载版本，该版本采用*溪流*包含文件的对象。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingStream.cpp" >}}

