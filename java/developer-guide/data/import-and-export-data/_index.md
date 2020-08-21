---
title: Import and Export Data
type: docs
weight: 130
url: /java/import-and-export-data/
---

{{% alert color="primary" %}} 

This article discusses some data import and export techniques that developers have access to through Aspose.Cells.

{{% /alert %}} 
## **Import Data into Worksheet**
Data represents the world as it is. To make sense of data, we analyze it and gain an understanding of the world. Data turns into information.

There are many ways of performing analysis: putting data into spreadsheets and manipulating it in different ways is one common method. With Aspose.Cells, it is easy to create spreadsheets that take data from a range of external sources and prepare them for analysis.

This article discusses some data import techniques that developers have access to through Aspose.Cells.
### **Importing Data Using Aspose.Cells**
When you open an Excel file with Aspose.Cells, all data in the file is automatically imported. Aspose.Cells can also import data from other data sources:

- [Array](/cells/java/import-and-export-data/).
- [Array list](/cells/java/import-and-export-data/).
- [Result set](/cells/java/import-and-export-data/).
- [JSON](/cells/java/import-and-export-data/)

Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook), that represents a Microsoft Excel file. The [Workbook](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook) class contains the collection [WorksheetCollection](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook#Worksheets) which allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://apireference.aspose.com/java/cells/com.aspose.cells/Worksheet) class. The [Worksheet](https://apireference.aspose.com/java/cells/com.aspose.cells/Worksheet) class provides a [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#Cells) collection. [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#Cells) collection provides very useful methods for importing data from other data sources. This article explains how these methods can be used.
#### **Importing from Array**
To import data to a spreadsheet from an array, call the importArray method of the [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#Cells) collection. There are many overloaded versions of the importArray method but a typical overload takes the following parameters:

- **Array**, the array object that you're importing content from.
- **Row number**, the row number of the first cell that the data will be imported to.
- **Column number**, the column number of the first cell that the data will be imported to.
- **Is vertical**, a Boolean value that specifies whether to import data vertically or horizontally.



{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArray-ImportingFromArray.java" >}}
#### **Importing from Multi-dimensional Arrays**
To import data to a spreadsheet from multi-dimensional arrays, call the relevant importArray overload of the [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#Cells) collection:



{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromMultiDimensionalArray-ImportingFromMultiDimensionalArray.java" >}}
#### **Importing from an ArrayList**
To import data from an *ArrayList* to worksheets, call the [ImportArrayList](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#importArrayList\(java.util.ArrayList,%20int,%20int,%20boolean\)) method of the [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#Cells) collection. The [ImportArrayList](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#importArrayList\(java.util.ArrayList,%20int,%20int,%20boolean\)) method takes the following parameters:

- **ArrayList**, the *ArrayList* object whose contents will be imported.
- **Row Number**, the row number of the first cell of the cell range from which contents will be imported.
- **Column Number**, the column number of the first cell from which data will be imported.
- **Is Vertical**, is a Boolean value that specifies whether to import data vertically or horizontally.



{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}
#### **Importing from Custom Objects to merged area**
To import data from a collection of objects to a worksheet containing merged cells, use [ImportTableOptions.CheckMergedCells](https://apireference.aspose.com/java/cells/com.aspose.cells/importtableoptions#CheckMergedCells) property. If the Excel template has merged cells, set the value of [ImportTableOptions.CheckMergedCells](https://apireference.aspose.com/java/cells/com.aspose.cells/importtableoptions#CheckMergedCells) property to true. Pass the [ImportTableOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/ImportTableOptions) object along with the list of columns/properties to the method to display your desired list of objects. The following code sample demonstrates the use of [ImportTableOptions.CheckMergedCells](https://apireference.aspose.com/java/cells/com.aspose.cells/importtableoptions#CheckMergedCells) property to import data from Custom Objects to merged cells. Please see the attached [source Excel](90112035.xlsx) file and the [output Excel](90112036.xlsx) file for reference.


