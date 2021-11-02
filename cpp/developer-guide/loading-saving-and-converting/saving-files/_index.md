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
Aspose.Cells provides the [IWorkbook](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) which represents a Microsoft Excel file and provides methods necessary to work with Excel files. The [IWorkbook](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) class provides the [Save](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349) method used to save Excel files. The [Save](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349) method has many overloads that are used to save files in different ways. The file format that the file is saved to is decided by the [SaveFormat](https://apireference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a) enumeration.
## **Saving File to Some Location**
To save files to a storage location, specify the file name (complete with storage path) and the desired file format (from the [SaveFormat](https://apireference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a) enumeration) when calling the [IWorkbook](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) object's [Save](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349) method.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToSomeLocation.cpp" >}}


## **Saving File to Stream**
To save files to a stream, create a MemoryStream or FileStream object and save the file to that stream object by calling the [IWorkbook](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) object's [Save](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349) method. Specify the desired file format using the [SaveFormat](https://apireference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a) enumeration when calling the [Save](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349) method.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToStream.cpp" >}}
