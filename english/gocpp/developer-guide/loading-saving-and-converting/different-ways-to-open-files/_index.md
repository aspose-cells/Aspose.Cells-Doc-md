---
title: Different Ways to Open Files
linktitle: Different Ways to Open Files
type: docs
weight: 10
url: /go-cpp/different-ways-to-open-files/
---

{{% alert color="primary" %}}

With Aspose.Cells, you can open files, for example, to retrieve data or to use a designer template to speed up the development process. Aspose.Cells can open a range of different files, such as Microsoft Excel spreadsheets (XLS, XLSX, XLSM, XLSB), CSV, or TabDelimited files.

{{% /alert %}}

## **Opening a File via a Path**

Developers can open a Microsoft Excel file using its file path on the local computer by specifying it in the [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) class constructor. Pass the path in the constructor as a string. Aspose.Cells will automatically detect the file format type.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadWorkbookUsingPath.go" >}}

## **Opening a File Using a Stream**

It is also possible to open an Excel file as a stream. To do so, use an overloaded version of the constructor that takes the *Stream* object that contains the file.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadWorkbookUsingStream.go" >}}
