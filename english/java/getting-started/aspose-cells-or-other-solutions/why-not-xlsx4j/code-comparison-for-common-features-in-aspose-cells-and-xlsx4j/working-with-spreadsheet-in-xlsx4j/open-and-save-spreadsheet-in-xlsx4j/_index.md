---
title: Open and Save Spreadsheet in xlsx4j
type: docs
weight: 40
url: /java/open-and-save-spreadsheet-in-xlsx4j/
---

## **Aspose.Cells - Open and Save Spreadsheet**
Developers use of Aspose.Cells to open files for different purposes. For example, open a file to retrieve data from it, or use a pre-defined designer spreadsheet file to speed up your development process. Aspose.Cells allows developers to open different kinds of source files. These source files can be Microsoft Excel reports, SpreadsheetML, CSV or Tab Delimited files. 

**Aspose.Cells** allows developers to create Excel files from scratch using its flexible API. Once you create Excel files, you would also need to save your workbook (file). Aspose.Cells provides a variety of ways to save these files.

**Java**

{{< highlight java >}}

 //Creating an Workbook object with an Excel file path

Workbook workbook = new Workbook(dataDir + "pivot.xlsm");

//Saving the Excel file

workbook.save(dataDir + "pivot-rtt-Aspose.xlsm");

{{< /highlight >}}
## **xlsx4j - Open and Save Spreadsheet**
Below example shows how to open and save spreadsheets while using xlsx4j.

**Java**

{{< highlight java >}}

 String inputfilepath  = dataDir + "pivot.xlsm";

boolean save = true;

String outputfilepath = dataDir + "pivot-rtt-xlsx4j.xlsm";

// Open a document from the file system

// 1. Load the Package

OpcPackage pkg = OpcPackage.load(new java.io.File(inputfilepath));

// Save it

if (save) {

    SaveToZipFile saver = new SaveToZipFile(pkg);

    saver.save(outputfilepath);

}

{{< /highlight >}}
## **Download Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Download Sample Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/opensavespreadsheet)
