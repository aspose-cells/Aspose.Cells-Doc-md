---  
title: Public API Changes in Aspose.Cells 8.0.0  
type: docs  
weight: 10  
url: /net/public-api-changes-in-aspose-cells-8-0-0/  
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  

This page lists public API changes that were introduced in Aspose.Cells 8.0.0. It includes not only new and obsolete public methods, but also a description of any changes in the behavior behind the scenes in Aspose.Cells that may affect the existing code.  

{{% /alert %}}  

## **Added MemorySetting to LoadOptions & WorkbookSettings**  
Starting from v8.0.0 of Aspose.Cells for .NET, we provide memory‑usage options for performance considerations. The `MemorySetting` property is now available in the `LoadOptions` and `WorkbookSettings` classes.  

##### **Example**  
Demonstrates how to read an Excel file (having large size) in optimized mode.  

**C#**  

{{< highlight csharp >}}  

 //Initialize LoadOptions  

LoadOptions options = new LoadOptions();  

//Set memory preferences  

options.MemorySetting = MemorySetting.MEMORY_PREFERENCE;  

//Instantiate the Workbook with an object of LoadOptions  

Workbook book = new Workbook(myDir + "large.xlsx", options);  

{{< /highlight >}}  

Demonstrates how to write a large dataset to a worksheet in optimized mode.  

**C#**  

{{< highlight csharp >}}  

 //Instantiate a new Workbook  

Workbook book = new Workbook();  

//Set the memory preferences for WorkbookSettings  

book.Settings.MemorySetting = MemorySetting.MEMORY_PREFERENCE;  

//Input large data into the cells  

//.........  

{{< /highlight >}}  

{{% alert color="primary" %}}  

Please check the detailed article on [Optimizing Memory while Working with Large Files](/cells/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).  

{{% /alert %}}  

## **Implementations of Row & Cell have changed**  
In previous versions, Row and Cell objects were kept in memory to represent the corresponding row and cell in a worksheet. The same instance was returned whenever `RowCollection[int index]` or `Cells[int row, int column]` were retrieved. For memory‑performance considerations, only the properties and data of Row and Cell are kept in memory from now on. Hence, the Row and Cell objects have become wrappers of the aforementioned properties.  

### **Example**  
Demonstrates how to compare the Cell and Row objects from now on.  

**C#**  

{{< highlight csharp >}}  

 //..  

row1.Equals(row2);  

  

cell1.Equals(cell2);  

 //..  

{{< /highlight >}}  

Because the Row and Cell objects are instantiated according to the invocation, they are not kept and managed in memory by the Cells component. Therefore, after some insertion and deletion operations, the Row and Column indexes may not be updated, or, even worse, these objects become invalid.  

### **Example**  
For instance, the following code snippet will return invalid results in 8.0.0 and above,  

**C#**  

{{< highlight csharp >}}  

 Cell cell = cells["A2"];  

Console.WriteLine(cell.Name + ":" + cell.Value);  

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);  

Console.WriteLine(cell.Name + ":" + cell.Value);  

{{< /highlight >}}  

With the new version, the `Cell` object may become invalid or refer to A2 with an unwanted value. To avoid such a situation, retrieve the Row or Cell objects again from the cells collection to obtain the correct result.  

**C#**  

{{< highlight csharp >}}  

 Cell cell = cells["A2"];  

Console.WriteLine(cell.Name + ":" + cell.Value);  

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);  

//Fetch the cell reference again  

Cell cell = cells["A3"];  

Console.WriteLine(cell.Name + ":" + cell.Value);  

{{< /highlight >}}  

{{% alert color="primary" %}}  

`RowCollection` does not inherit `CollectionBase` anymore because there is no Row object in its inner list.  

{{% /alert %}}  

## **Cell.StringValue behavior changed**  
In previous versions, the special pattern `_` was ignored while formatting cell values, whereas the special character `*` always produced one character in the formatted result. From this version, we have changed the logic to handle the special characters `_` and `*` so that the formatted result matches that of the Excel application. For instance, the custom cell format `"_(\$* #,##0.00_)`" used to represent the value `123` produced the result `"$ 123.00"`. With the new version, `Cell.StringValue` will contain the result `"$123.00"`, which is the same behavior as Excel exhibits when copying the cell to text or exporting to CSV.  

## **Added CreatedTime to PdfSaveOptions**  
Now users can get or set the PDF creation time when saving the spreadsheet to PDF using the `PdfSaveOptions` class.  

## **Added ShowFormulas to Worksheet**  
From now on, users may use the Boolean property `ShowFormulas` offered by `Worksheet` to toggle the view between formulas and values in a worksheet.  

## **Added Ooxml to FileFormatType**  
A new constant `Ooxml` has been added to the `FileFormatType` class to represent encrypted Office Open XML files such as XLSX, DOCX, PPTX, and more.  

## **Obsoleted FilterColumnCollection of AutoFilter**  
With Aspose.Cells for Java, the `FilterColumnCollection` property has been marked obsolete. It is suggested to use `AutoFilter.FilterColumns` instead.  

## **Replaced SeriesCollection.SecondCatergoryData with SeriesCollection.SecondCategoryData**  
We have corrected the typographical error in the property name for `SeriesCollection.SecondCatergoryData`. You may use `SeriesCollection.SecondCategoryData` from now on, whereas the original property `SeriesCollection.SecondCatergoryData` has been marked obsolete.  

{{< app/cells/assistant language="csharp" >}}
