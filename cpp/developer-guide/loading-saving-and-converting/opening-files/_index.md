---
title: Opening Files
type: docs
weight: 10
url: /cpp/opening-files/
---

{{% alert color="primary" %}} 

With Aspose.Cells it is possible to open files, for example to retrieve data, or to use a designer template to speed up the development process. Aspose.Cells can open a range of different files, such as Microsoft Excel spreadsheets (XLS, XLSX, XLSM, XLSB), CSV or TabDelimited files.

{{% /alert %}} 
## **Opening a File via a Path**
Developers can open a Microsoft Excel file using its file path on the local computer by specifying it in the [IWorkbook](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_workbook/) class constructor. Simply pass the path in the constructor as String. Aspose.Cells will automatically detect the file format type.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingPath.cpp" >}}
## **Opening a File using a Stream**
It is also possible to open an Excel file as a stream. To do so, use an overloaded version of the constructor that takes the *Stream* object that contains the file.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingStream.cpp" >}}
