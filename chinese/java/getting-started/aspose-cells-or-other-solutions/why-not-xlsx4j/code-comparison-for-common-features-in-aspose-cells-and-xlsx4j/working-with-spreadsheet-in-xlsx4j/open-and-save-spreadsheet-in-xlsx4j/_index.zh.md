---
title: 在xlsx4j中打开和保存电子表格
type: docs
weight: 40
url: /zh/java/open-and-save-spreadsheet-in-xlsx4j/
---

## **Aspose.Cells - 打开和保存电子表格**
开发人员使用Aspose.Cells打开文件以供不同目的使用。例如，打开一个文件以从中检索数据，或者使用预定义的设计者电子表格文件加快开发进程。Aspose.Cells允许开发者打开不同类型的源文件。这些源文件可以是Microsoft Excel报表、SpreadsheetML、CSV或制表符分隔的文件。 

**Aspose.Cells**允许开发者使用其灵活的API从头开始创建Excel文件。一旦创建了Excel文件，您还需要保存工作簿（文件）。Aspose.Cells提供多种保存这些文件的方式。

**Java**

{{< highlight java >}}

 //Creating an Workbook object with an Excel file path

Workbook workbook = new Workbook(dataDir + "pivot.xlsm");

//Saving the Excel file

workbook.save(dataDir + "pivot-rtt-Aspose.xlsm");

{{< /highlight >}}
## **xlsx4j - 打开和保存电子表格**
下面的示例展示了如何在使用xlsx4j时打开和保存电子表格。

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
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/opensavespreadsheet)
