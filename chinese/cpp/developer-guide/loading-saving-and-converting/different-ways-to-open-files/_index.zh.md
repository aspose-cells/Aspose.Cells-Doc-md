---
title: 打开文件的不同方式
linktitle: 打开文件的不同方式
type: docs
weight: 10
url: /zh/cpp/different-ways-to-open-files/
---

{{% alert color="primary" %}} 

使用Aspose.Cells可以打开文件，例如检索数据，或使用设计模板加快开发过程。Aspose.Cells可以打开一系列不同的文件，例如Microsoft Excel电子表格(XLS，XLSX，XLSM，XLSB)，CSV或TabDelimited文件。

{{% /alert %}} 
## **通过路径打开文件**
开发人员可以通过在构造函数中指定本地计算机上的文件路径来打开Microsoft Excel文件，只需将路径作为字符串传递给构造函数即可。Aspose.Cells将自动检测文件格式类型。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingPath-new.cpp" >}}

## **使用流打开文件**
还可以将Excel文件作为流打开。为此，使用接受包含文件的*Stream*对象的构造函数的重载版本。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingStream-new.cpp" >}}

