---
title: Saving Files
type: docs
weight: 20
url: /go-cpp/saving-files/
---

{{% alert color="primary" %}}

Aspose.Cells make it possible to create and save files and to manipulate existing files. This article explains the various ways in which files can be saved.

{{% /alert %}}

## **Different Ways to Save Files**

Aspose.Cells provides the [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/), which represents a Microsoft Excel file and provides methods necessary to work with Excel files. The [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) class provides the [Save](https://reference.aspose.com/cells/go-cpp/workbook/save/) method used to save Excel files. The [Save](https://reference.aspose.com/cells/go-cpp/workbook/save/) method has many overloads that are used to save files in different ways. The file format that the file is saved to is decided by the [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/) enumeration.

## **Saving File to Some Location**

To save files to a storage location, specify the file name (complete with storage path) and the desired file format (from the [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/) enumeration) when calling the [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) object's [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string/) method.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToSomeLocation.go" >}}

## **Saving File to Stream**

To save files to a stream, create a MemoryStream or FileStream object and save the file to that stream object by calling the [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) object's [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string/) method. Specify the desired file format using the [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/) enumeration when calling the [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_saveFormat/) method.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToStream.go" >}}

## **Saving File to PDF**

To save the desired content to a PDF file using the Aspose.Cells for Go via C++ library, create a new [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) object or construct a [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) object by reading an existing Excel file, and then [save](https://reference.aspose.com/cells/go-cpp/workbook/save_string_saveOptions/) the file to PDF by calling the Save method of the [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) object.    When calling the Save method, use the [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/) enumeration to specify the desired file format.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToPdf.go" >}}
