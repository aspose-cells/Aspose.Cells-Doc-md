---
title: 打开文件的不同方式
linktitle: 打开文件的不同方式
type: docs
weight: 10
url: /zh/go-cpp/different-ways-to-open-files/
---

{{% alert color="primary" %}}

使用Aspose.Cells，可以打开文件以检索数据或使用设计模板加快开发。Aspose.Cells支持打开多种文件格式，如Microsoft Excel（XLS、XLSX、XLSM、XLSB）、CSV或TabDelimited文件。

{{% /alert %}}

## **通过路径打开文件**

开发者可以通过在【Workbook】类构造函数中指定本地计算机上的文件路径，打开Microsoft Excel文件。将路径作为字符串传入，Aspose.Cells会自动检测文件格式。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadWorkbookUsingPath.go" >}}

## **通过流打开文件**

也可以将 Excel 文件作为流打开。 为此，请使用接受包含文件的 *流*  对象的构造函数的重载版本。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadWorkbookUsingStream.go" >}}
