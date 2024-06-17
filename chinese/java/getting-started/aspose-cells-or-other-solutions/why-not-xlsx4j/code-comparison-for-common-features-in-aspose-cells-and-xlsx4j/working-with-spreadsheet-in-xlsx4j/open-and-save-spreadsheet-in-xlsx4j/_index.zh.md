---
title: 在 xlsx4j 中打开和保存电子表格
type: docs
weight: 40
url: /zh/java/open-and-save-spreadsheet-in-xlsx4j/
---

## **Aspose.Cells - 打开和保存电子表格**
开发人员可以使用 Aspose.Cells 以不同的目的打开文件。例如，打开文件以从中检索数据，或使用预定义的设计电子表格文件加速开发过程。Aspose.Cells 允许开发人员打开不同类型的源文件。这些源文件可以是 Microsoft Excel 报告、SpreadsheetML、CSV 或制表符分隔文件。 

**Aspose.Cells** 允许开发人员使用其灵活的 API 从头开始创建 Excel 文件。一旦创建了 Excel 文件，您还需要保存工作簿（文件）。Aspose.Cells 提供了多种保存这些文件的方法。

**Java**

{{< highlight java >}}

 //Creating an Workbook object with an Excel file path

Workbook workbook = new Workbook(dataDir + "pivot.xlsm");

//Saving the Excel file

workbook.save(dataDir + "pivot-rtt-Aspose.xlsm");

{{< /highlight >}}
## **xlsx4j - 打开和保存电子表格**
以下示例显示了在使用 xlsx4j 时如何打开和保存电子表格。

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
