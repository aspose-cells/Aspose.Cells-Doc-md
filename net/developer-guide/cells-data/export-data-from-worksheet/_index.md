---
title: Export Data from Worksheet
type: docs
weight: 180
url: /net/export-data-from-worksheet/
---

{{% alert color="primary" %}}

This article discusses some data export techniques that developers have access to through Aspose.Cells.

{{% /alert %}}

## **Export Data from Worksheet**

Aspose.Cells not only facilitates its users to import data to worksheets from external data sources but also allow them to export their worksheet data to a [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8). As we know that [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) is the part of ADO.NET and is used to hold data. Once the data is stored in a [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8), it can be used in any way according to the requirements of users. Developers can also store this data (stored in [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)) directly to a database if they wish. So, we can see that it becomes easier for the developers to manipulate worksheet data if it is exported to a [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8).

## **Exporting Data to DataTable Using Aspose.Cells**

Developers can easily export their worksheet data to a [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) object by calling either [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) or [**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) method of the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) class. Both methods are used in different scenarios, which are discussed below in more detail.

## **Columns Containing Strongly Typed Data**

We know that a spreadsheet stores data as a sequence of rows and columns. If all values in the columns of a worksheet are strongly typed (that means all values in a column must have the same data type) then we can export the worksheet content by calling the [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) method of the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) class. [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) method takes the following parameters to export worksheet data as [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) object:

- **Row number**, the row number of the first cell data will be exported from.
- **Column number**, the column number of the first cell the data will be exported from.
- **Number of rows**, the number of rows to export.
- **Number of columns**, the number of columns to export.
- **Export column names**, a Boolean property that indicates whether the data in the first row of the worksheet should be exported as column names of the [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) or not.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingStronglyTypedData-1.cs" >}}

## **Columns Containing Non-Strongly Typed Data**

If all values in the columns of a worksheet are not strongly typed (that means the values in a column may have the different data types) then we can export the worksheet content by calling the [**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) method of the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) class. [**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) method takes the same set of parameters as that of the [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) method to export worksheet data as a [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) object.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingNonStronglyTypedData-1.cs" >}}

## **Export Range with flag to skip column name**

Data from a range can be exported to [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) where a flag is available to skip header row in the exported data. Following code exports a range of data to [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) with an argument [**ExportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions) which contains [**ExportColumnName**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/exportcolumnname) flag. It is set to **true** if header information is there, hence it will not be included in data and set to **false** if no header is there and all rows are to be considered as data.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportRangeWithFlagToSkipColumnHeader-1.cs" >}}

## **Advance topics**
- [Export Excel Data to DataTable without any Formatting](/cells/net/export-excel-data-to-datatable-without-any-formatting/)
- [Export HTML String Value of the Cells to the DataTable](/cells/net/export-html-string-value-of-the-cells-to-the-datatable/)
- [Export Visible Rows Data from Worksheet](/cells/net/export-visible-rows-data-from-worksheet/)
- [Ignore Hidden Columns while Exporting Worksheet Data to Data Table](/cells/net/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/)
- [Rename duplicate columns automatically while exporting worksheet data](/cells/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/)