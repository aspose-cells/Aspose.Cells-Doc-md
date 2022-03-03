---
title: Manage Worksheets
type: docs
weight: 20
url: /java/manage-worksheets/
---

{{% alert color="primary" %}}

Developers can easily create and manage worksheets in their Excel files programmatically using the flexible API of Aspose.Cells. In this topic, we will discuss some approaches to add and remove worksheets in Excel files.

{{% /alert %}}

Managing worksheets using Aspose.Cells is as easy as ABC. In this section, we will describe how can we:

1. Create a new Excel file from scratch and add a worksheet to it
1. Add worksheets to designer spreadsheets
1. Accessing Worksheets using Sheet Name
1. Remove a worksheet from an Excel file using its sheet name
1. Remove a worksheet from an Excel file using its sheet index

Aspose.Cells provides a class, [**Workbook**](https://apireference.aspose.com/cells/java/com.aspose.cells/workbook) that represents an Excel file. [**Workbook**](https://apireference.aspose.com/cells/java/com.aspose.cells/workbook) class contains a [**WorksheetCollection**](https://apireference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) that allows access to each worksheet in the Excel file.

A worksheet is represented by the [**Worksheet**](https://apireference.aspose.com/cells/java/com.aspose.cells/worksheet) class. [**Worksheet**](https://apireference.aspose.com/cells/java/com.aspose.cells/worksheet) class provides a wide range of properties and methods to manage a worksheet. Let's see how can we make use of these basic set of APIs.

## **Adding Worksheets to a New Excel File**

To create a new Excel file programmatically, developers would need to create an object of [**Workbook**](https://apireference.aspose.com/cells/java/com.aspose.cells/workbook) class that represents an Excel file. Then developers can call [**add**](https://apireference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add()) method of the [**WorksheetCollection**](https://apireference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection). When we call [**add**](https://apireference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add()) method, an empty worksheet is added to the Excel file automatically, which can be referenced by passing the sheet index of the newly added worksheet to the [**WorksheetCollection**](https://apireference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection). After the worksheet reference is obtained, developers can work on their worksheets according to their requirements. After the work is done on the worksheets, developers can save their newly created Excel file with new worksheets by calling the [**save**](https://apireference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) method of the [**Workbook**](https://apireference.aspose.com/cells/java/com.aspose.cells/workbook) class.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoNewExcelFile-AddingWorksheetstoNewExcelFile.java" >}}

## **Adding Worksheets to a Designer Spreadsheet**

The process of adding worksheets to a designer spreadsheet is entirely same as that of the above approach except that the Excel file is already created and we need to open that Excel file first before adding a worksheet to it. A designer spreadsheet can be opened by passing the file path or stream while initializing the [**Workbook**](https://apireference.aspose.com/cells/java/com.aspose.cells/workbook) class.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoDesignerSpreadsheet-AddingWorksheetstoDesignerSpreadsheet.java" >}}

## **Accessing Worksheets using Sheet Name**

Developers may access or get any worksheet by specifying its name or index.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AccessingWorksheetsusingSheetName-AccessingWorksheetsusingSheetName.java" >}}

## **Removing Worksheets using Sheet Name**

Sometimes, developers may need to remove worksheets from existing Excel files and that task can be performed by calling the [**removeAt**](https://apireference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String)) method of the [**WorksheetCollection**](https://apireference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) collection. We can pass the sheet name to the [**removeAt**](https://apireference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String)) method to remove a specific worksheet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetName-RemovingWorksheetsusingSheetName.java" >}}

## **Removing Worksheets using Sheet Index**

The above approach of removing worksheets works well if developers already know the sheet names of the worksheets to be deleted. But, what if you don't know the sheet name of the worksheet that you want to remove from your Excel file?

Well, in such circumstances, developers can use an overloaded version of [**removeAt**](https://apireference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(int)) method that takes the sheet index of the worksheet instead of its sheet name.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetIndex-RemovingWorksheetsusingSheetIndex.java" >}}
