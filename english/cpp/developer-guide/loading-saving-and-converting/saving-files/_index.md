---
title: Saving Files
type: docs
weight: 20
url: /cpp/saving-files/
---

{{% alert color="primary" %}} 

Aspose.Cells makes it possible to create and save files, and to manipulate existing files. This article explains the various ways in which files can be saved.

{{% /alert %}} 
## **Different Ways to Save Files**
Aspose.Cells provides the [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) which represents a Microsoft Excel file and provides methods necessary to work with Excel files. The [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class provides the [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) method used to save Excel files. The [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) method has many overloads that are used to save files in different ways. The file format that the file is saved to is decided by the [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) enumeration.
## **Saving File to Some Location**
To save files to a storage location, specify the file name (complete with storage path) and the desired file format (from the [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) enumeration) when calling the [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) object's [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) method.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToSomeLocation-new.cpp" >}}


## **Saving File to Stream**
To save files to a stream, create a MemoryStream or FileStream object and save the file to that stream object by calling the [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) object's [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) method. Specify the desired file format using the [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) enumeration when calling the [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) method.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToStream-new.cpp" >}}

## **Saving File to PDF**
To save the desired content to a PDF file using the Aspose.Cells for C++ library, create a new [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) object or construct a [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) object by reading an existing Excel file, and then [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) the file to PDF by calling the Save method of the [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) object.    When calling the Save method, use the [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) enumeration to specify the desired file format.


{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToPdf-new.cpp" >}}
