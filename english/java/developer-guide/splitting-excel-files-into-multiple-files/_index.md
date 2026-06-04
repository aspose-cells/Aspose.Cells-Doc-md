---
title: Splitting Excel Files into Multiple Files
description: Aspose.Cells is a Java library for working with spreadsheet files, which supports splitting a single Excel file into multiple files. This article will introduce how to split Excel files by copying each worksheet to a separate workbook and by copying specific cell ranges to other workbooks.
keywords: Aspose.Cells, Java library, spreadsheet, split Excel file, copy worksheet, copy range, multiple workbooks, save as separate files
type: docs
weight: 195
url: /java/splitting-excel-files-into-multiple-files/
---

{{% alert color="primary" %}}

Aspose.Cells supports splitting a single Excel file into multiple files. There are two primary ways to do this: (1) by copying each worksheet of the source workbook to a new workbook and saving each as a separate file, and (2) by copying a specific cell range from a worksheet to a new workbook. Both approaches are useful when you need to distribute subsets of data, create smaller reports for different recipients, or isolate data for individual processing.

{{% /alert %}}

## **Introduction**

There are many real-world scenarios in which a developer needs to break a single Excel file into several smaller files. For example, a workbook may contain one worksheet per department, and each department head needs to receive only their own sheet. In other cases, you may want to extract a particular table or data block from a worksheet and send it as a stand-alone file via email, without exposing the rest of the workbook. Large consolidated workbooks may also need to be split into smaller pieces for easier handling, faster loading, or downstream processing by other systems.

Aspose.Cells provides two flexible approaches for this task. The first approach iterates through every worksheet in the source workbook and copies its content into a brand-new `Workbook` instance, saving each one as a separate file. The second approach focuses on a specific cell range within a worksheet and copies only that range into a new workbook. In both cases, the general flow is the same: load the source workbook using the `Workbook` class, access the relevant data through the `Worksheet` and `Cells` objects, transfer the content to a destination `Workbook`, and then save the destination to disk.

## **Splitting an Excel File by Copying Each Worksheet to a New Workbook**

### **Approach Overview**

In this approach, the source workbook is opened once, and then for every `Worksheet` in its `Worksheets` collection, a new destination `Workbook` is created. The content of the source worksheet is then copied into the first worksheet of the destination workbook, and the destination workbook is saved as a file whose name is derived from the source worksheet's name. The result is one output file per worksheet, with each output file containing the data of a single source sheet.

This method is the right choice when each worksheet in your source workbook represents a logically independent unit of information (such as a department, region, month, or product line) and you want to deliver or process each unit on its own.

### **Steps**

The following steps describe how to split an Excel file by copying each worksheet to a new workbook:

1. Open the source Excel file by instantiating a `Workbook` object and passing the file path to its constructor.
2. Iterate through the `Workbook.Worksheets` collection using a `for` or `foreach` loop so that every `Worksheet` in the source file is processed.
3. Inside the loop, create a new destination `Workbook` instance (an empty workbook) for the current worksheet.
4. Add a new `Worksheet` to the destination workbook (or use the default first worksheet) and assign it a meaningful name, ideally the same as the source worksheet's `Name` property.
5. Copy the content of the source worksheet into the destination worksheet. This can be done by iterating the cells of the source worksheet's `Cells` collection and writing their values into the corresponding cells of the destination worksheet, or by using the `Cells.copy` method to transfer an entire range at once.
6. Construct an output file path that incorporates the source worksheet's name (for example, `dataDir + worksheet.getName() + ".xls"`) so that each generated file has a unique name.
7. Call the destination `Workbook.save` method to write the file to disk.
8. Repeat steps 3 through 7 for the next worksheet until all worksheets have been processed.

### **Code Example**

```java
import com.aspose.cells.*;

String dataDir = "data/";
Workbook workbook = new Workbook(dataDir + "book1.xls");

for (int i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    Worksheet sourceSheet = workbook.getWorksheets().get(i);
    String sheetName = sourceSheet.getName();
    
    Workbook destWorkbook = new Workbook();
    int destIndex = destWorkbook.getWorksheets().add();
    Worksheet destSheet = destWorkbook.getWorksheets().get(destIndex);
    destSheet.setName(sheetName);
    
    destSheet.copy(sourceSheet);
    
    String destFile = dataDir + sheetName + ".xls";
    destWorkbook.save(destFile, SaveFormat.EXCEL_97_TO_2003);
}
```

The expected output is a set of new files in the data directory, one file per worksheet from the source workbook. Each file is named after its corresponding source sheet, and the file contains the data (and optionally the formatting) of that single sheet.

## **Splitting an Excel File by Copying a Range to a New Workbook**

### **Approach Overview**

Sometimes the data you need to split does not correspond to an entire worksheet but rather to a specific rectangular region of a worksheet, such as `A1:D10` or a named range that represents a particular table. In these cases, copying whole worksheets is wasteful, and a more precise approach is required: identify the source range, copy only that range into a new workbook, and save the new file.

This approach is ideal when you want to extract a single table, report block, or data area from a larger worksheet while discarding all unrelated content. It is also useful for exporting user-selected regions of a sheet as standalone files.

### **Steps**

The following steps describe how to split an Excel file by copying a specific range to a new workbook:

1. Open the source Excel file by instantiating a `Workbook` object with the file path.
2. Retrieve the target `Worksheet` that contains the range you want to copy, either by index (for example, the first sheet) or by name from the `Worksheets` collection.
3. Identify the range to be copied. This can be a hard-coded cell range such as `A1:C10`, or a named range obtained through the `Worksheet.Cells` collection, or a range created via `Worksheet.Cells.createRange`.
4. Create a new destination `Workbook` instance.
5. Access the first `Worksheet` of the destination workbook (the default sheet).
6. Copy the source range into the destination worksheet, typically starting from cell `A1`. The `Cells.copy` method on the destination `Cells` collection can be used to copy an entire range, or you can iterate through the source range's cells and write their values into the destination cells with `putValue`. Optional `CopyOptions` may be supplied to control what is transferred (values only, values and styles, formulas, and so on).
7. Save the destination workbook to a new file path on disk using the `Workbook.save` method.

### **Code Example**

```java
import com.aspose.cells.*;

// Define the data directory and file paths
String dataDir = "data/";
String sourcePath = dataDir + "book1.xls";
String outputPath = dataDir + "outputrange.xls";

// Open the source Excel file
Workbook sourceWorkbook = new Workbook(sourcePath);

// Get the first worksheet from the source workbook
Worksheet sourceWorksheet = sourceWorkbook.getWorksheets().get(0);

// Define the source cell range A1:C10 (10 rows, 3 columns starting at row 0, col 0)
Range sourceRange = sourceWorksheet.getCells().createRange(0, 0, 10, 3);

// Create a new destination workbook
Workbook destWorkbook = new Workbook();

// Access the first worksheet in the destination workbook
Worksheet destWorksheet = destWorkbook.getWorksheets().get(0);

// Create the destination range at A1 with the same dimensions as the source range
Range destRange = destWorksheet.getCells().createRange(0, 0, 10, 3);

// Copy the source range to the destination range
destRange.copy(sourceRange);

// Save the destination workbook to a new .xls file
destWorkbook.save(outputPath, SaveFormat.EXCEL_97_TO_2003);
```

The expected output is a single new file in the data directory that contains only the values (and optionally the formatting) of the specified range extracted from the source workbook. The destination file has no relationship to any other data in the source file; it contains just the extracted range, beginning at cell `A1` of its first worksheet.

## **Related Articles**

- [Copying Rows and Columns](/cells/java/copying-rows-and-columns/)
- [Merging and Unmerging Cells](/cells/java/merging-and-unmerging-cells/)

{{< app/cells/assistant language="java" >}}