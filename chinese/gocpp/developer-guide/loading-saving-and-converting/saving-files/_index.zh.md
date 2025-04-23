---
title: 保存文件
type: docs
weight: 20
url: /zh/go-cpp/saving-files/
---

{{% alert color="primary" %}}

Aspose.Cells允许创建、保存文件，并操作现有文件。本文介绍了多种保存文件的方法。

{{% /alert %}}

## **不同的文件保存方式**

Aspose.Cells提供[Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)类，它代表微软Excel文件并提供操作Excel文件所需的方法。 [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)类提供用于保存Excel文件的[Save](https://reference.aspose.com/cells/go-cpp/workbook/save/)方法。这个[Save](https://reference.aspose.com/cells/go-cpp/workbook/save/)方法有多个重载，用于不同方式保存文件。文件保存的格式由[SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/)枚举决定。

## **将文件保存到某个位置**

要将文件保存到存储位置，调用[Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)对象的[Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string/)方法时，指定文件名（包含存储路径）和所需的文件格式（取自[SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/)枚举）。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToSomeLocation.go" >}}

## **将文件保存到流**

要将文件保存到流中，创建MemoryStream或FileStream对象，并通过调用[Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)对象的[Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string/)方法，将文件保存到该流对象中。在调用[Save](https://reference.aspose.com/cells/go-cpp/workbook/save/)方法时，指定所需的文件格式(使用[SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/)枚举)。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToStream.go" >}}

## **将文件保存为 PDF**

使用Aspose.Cells for Go via C++库，将所需内容保存为PDF文件，方法是新建一个[Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)对象或从读取现有Excel文件构造一个[Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)，然后调用其[Save](https://reference.aspose.com/cells/go-cpp/workbook/save/)方法将文件保存为PDF。当调用Save方法时，用[SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/)枚举指定所需文件格式。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToPdf.go" >}}
