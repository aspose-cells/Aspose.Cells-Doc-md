---
title: Export Excel Data to DataTable without any Formatting
type: docs
weight: 280
url: /net/export-excel-data-to-datatable-without-any-formatting/
description: Learn how to Export Excel Data to DataTable without any Formatting through the Aspose.Cells for .NET API.
keywords: Export Excel Data to DataTable without any Formatting, Specify Cell Value Format Strategy, Add Format Strategy When Exporting Data to DataTable. 
---

{{% alert color="primary" %}}

Sometimes users want to export excel data into a data table without any formatting. For example, if some cell has a value 0.012345 and it is formatted as to display two decimal places, then when the user will export excel data to a data table, it will be exported as 0.01 and not as 0.012345. To deal with this problem, Aspose.Cells has provided [**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy) property which can take one of these three values

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

If you will set it to [**CellValueFormatStrategy.None**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy), then it will export the data without any formatting.

{{% /alert %}}

## Sample Code

The following sample explains the use of [**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy) property to export excel data with and without any formatting.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ExportExcelDataToDataTableWithoutFormatting-ExportExcelDataToDataTableWithoutFormatting.cs" >}}

## **Console Output**

Below is the console debug output of the above sample code

{{< highlight java >}}

Cell String Value: 0.01

Cell String Value without Format: 0.012345

Export Data Table with Format Strategy as Cell Style: 0.01

Export Data Table with Format Strategy as None: 0.012345

{{< /highlight >}}
