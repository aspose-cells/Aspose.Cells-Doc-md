---
title: Reading and Writing Query Table of Worksheet
type: docs
weight: 40
url: /net/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells provides Worksheet.QueryTables collection which returns the object of type QueryTable by index. It has the following two properties

- QueryTable.AdjustColumnWidth
- QueryTable.PreserveFormatting

These are both Boolean values. You can view them in Microsoft Excel via Data > Connections > Properties.

{{% /alert %}}

## Reading and Writing Query Table of Worksheet

The following sample code reads the first QueryTable of the first worksheet and then prints both of the QueryTable properties. Then it sets the QueryTable.PreserveFormatting to true.

You can download the source Excel file used in this code and the output Excel file generated by the code from the following links.

- [Source Excel File](5115533.xlsx)
- [Output Excel File](5115537.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.cs" >}}

### Console Output

Here is the console output of the above sample code

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Retrieve query table result range

Aspose.Cells provides option to read the address i.e. result range of cells for a query table. Following code demonstrates this feature by reading the address of result range for a query table. Sample file can be downloaded [here](72417290.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAddressOfResultRange.cs" >}}
{{< app/cells/assistant language="csharp" >}}