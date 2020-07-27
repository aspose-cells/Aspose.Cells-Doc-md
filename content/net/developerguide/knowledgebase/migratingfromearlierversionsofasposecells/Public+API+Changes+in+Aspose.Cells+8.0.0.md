+++
title = "Public API Changes in Aspose.Cells 8.0.0" 
description = "" 
weight = 16748 
+++

Aspose.Cells for .NET : Public API Changes in Aspose.Cells 8.0.0  

# Aspose.Cells for .NET : Public API Changes in Aspose.Cells 8.0.0


This page lists public API changes that were introduced in Aspose.Cells 8.0.0. It includes not only new and obsoleted public methods, but also a description of any changes in the behavior behind the scenes in Aspose.Cells which may affect the existing code.

### Added MemorySetting to LoadOptions & WorkbookSettings

Starting from v8.0.0 of Aspose.Cells for .NET we have provided the memory usage options for performance considerations. `MemorySetting` property is now available in `LoadOptions` & `WorkbookSettings` classes.

##### Example

Demonstrates how to read an Excel file (having large size) in optimized mode.

**C#**

{{< code lang="c#" >}}
//Initialize LoadOptions
LoadOptions options = new LoadOptions();
//Set memory preferences
options.MemorySetting = MemorySetting.MEMORY_PREFERENCE;
//Instantiate the Workbook with an object of LoadOptions
Workbook book = new Workbook(myDir + "large.xlsx", options);
{{< /code >}}

Demonstrates how to write large Dataset to a worksheet in optimized mode.

**C#**

{{< code lang="c#" >}}
//Instantiate a new Workbook
Workbook book = new Workbook();
//Set the memory preferences for WorkbookSettings
book.Settings.MemorySetting = MemorySetting.MEMORY_PREFERENCE;

//Input large data into the cells
//.........
{{< /code >}}

Please check the detailed article on [Optimizing Memory while Working with Large File](https://docs2.aspose.com/cells/net/developerguide/technicalarticles/asposecellsgeneral/managingworkbooksandworksheets/optimizing+memory+usage+while+working+with+big+files+having+large+datasets).

### Implementations of Row & Cell has changed

In previous versions, `Row` and `Cell` objects were kept in memory to represent corresponding row and cell in a `Worksheet`. The same instance was returned whenever **RowCollection\[int index\]** or **Cells\[int row, int column\]** were retrieved. For memory performance consideration, only properties and data of `Row` and `Cell` will be kept in the memory now onward. Hence, the `Row` & `Cell` object have become the wrapper of aforesaid properties.

##### Example

Demonstrates how to compare the `Cell` and `Row` objects from now onward.

**C#**

{{< code lang="c#" >}}
//..
row1.Equals(row2);


cell1.Equals(cell2);
//..
{{< /code >}}

Because the `Row` and `Cell` objects are instantiated according to the invocation, they will not be kept and managed in memory by the Cells component. Therefore after some insertion and deletion operations, the Row & Column indexes may not be updated or even worse, these objects become invalid.

##### Example

For instance the following code snippet will return invalid results using 8.0.0 and above,

**C#**

{{< code lang="c#" >}}
Cell cell = cells["A2"];
Console.WriteLine(cell.Name + ":" + cell.Value);
cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);
Console.WriteLine(cell.Name + ":" + cell.Value);
{{< /code >}}

With new version the `Cell` object will become invalid or refer to A2 with some unwanted value. In order to avoid such situation, get the `Row` or `Cell` objects again from the cells collection to retrieve the correct result.

**C#**

{{< code lang="c#" >}}
Cell cell = cells["A2"];
Console.WriteLine(cell.Name + ":" + cell.Value);
cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);
//Fetch the cell reference again
Cell cell = cells["A3"];
Console.WriteLine(cell.Name + ":" + cell.Value);
{{< /code >}}

`RowCollection` does not inherit `CollectionBase` anymore because there is no Row object in its inner list.

### Cell.StringValue Behavior Changed

In previous versions, special pattern \_ was ignored while formatting cell values, wheres the special character \* always produced one character into the formatted result. From this version, we have changed the logic to handle special characters \_ and \* in order to make the formatted result same as of Excel application. For instance, the custom cell format "\_(\\$\* #,##0.00\_)" used to represent value 123 produced the result as "$ 123.00". With new versions, `Cell.StringValue` will contain the result as "$123.00" which is the same behavior as Excel application exhibits while copying the cell to text or export to CSV.

### Added CreatedTime to PdfSaveOptions

Now users can get or set PDF creation time while saving the spreadsheet to PDF while using `PdfSaveOptions` class.

### Added ShowFormulas to Worksheet

From now onward, users may use Boolean property `ShowFormulas` offered by `Worksheet` to change view from formula to value of a given worksheet.

### Added Ooxml to FileFormatType

A new constant `Ooxml` has been added to the `FileFormatType` class to represent the encrypted Office open XML file such as XLSX, DOCX, PPTX and more.

### Obsoleted FilterColumnCollection of AutoFilter

With Aspose.Cells for Java, the `FilterColumnCollection` property has been marked obsoleted. It is suggested to use `AuotFilter.FilterColumns` property instead.

### Replaced SeriesCollection.SecondCatergoryData with SeriesCollection.SecondCategoryData

We have basically corrected the typo error in property name for `SeriesCollection.SecondCatergoryData`. You may use `SeriesCollection.SecondCategoryData` property now onward, whereas the original property `SeriesCollection.SecondCatergoryData` has been marked obsoleted.

