---
title: 打开文件的不同方式
linktitle: 打开文件的不同方式
type: docs
weight: 10
url: /zh/cpp/different-ways-to-open-files/
---

{{% alert color="primary" %}} 

使用Aspose.Cells可以打开文件，例如检索数据，或者使用设计模板加速开发过程。Aspose.Cells可以打开多种不同类型的文件，如Microsoft Excel电子表格（XLS、XLSX、XLSM、XLSB）、CSV或Tab分隔文件。

{{% /alert %}} 
## **通过路径打开文件**
开发人员可以通过在 [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)  类构造函数中对其指定的本地计算机上的文件路径来打开 Microsoft Excel 文件。 只需在构造函数中传递路径即可。Aspose.Cells 将自动检测文件格式类型。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingPath-new.cpp" >}}

## **使用流打开文件**
也可以将 Excel 文件作为流打开。 为此，请使用接受包含文件的 *流*  对象的构造函数的重载版本。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingStream-new.cpp" >}}

{{< app/cells/assistant language="cpp" >}}
