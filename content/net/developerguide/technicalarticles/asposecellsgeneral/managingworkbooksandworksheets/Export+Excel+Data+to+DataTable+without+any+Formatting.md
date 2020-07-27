+++
title = "Export Excel Data to DataTable without any Formatting" 
description = "" 
weight = 20449 
+++

Aspose.Cells for .NET : Export Excel Data to DataTable without any Formatting  

# Aspose.Cells for .NET : Export Excel Data to DataTable without any Formatting


Sometimes users want to export excel data into a data table without any formatting. For example, if some cell has a value 0.012345 and it is formatted as to display two decimal places, then when the user will export excel data to a data table, it will be exported as 0.01 and not as 0.012345. To deal with this problem, Aspose.Cells has provided [ExportTableOptions.FormatStrategy](https://apireference.aspose.com/net/cells/aspose.cells/exporttableoptions/properties/formatstrategy) property which can take one of these three values

*   CellValueFormatStrategy.CellStyle
*   CellValueFormatStrategy.DisplayStyle
*   CellValueFormatStrategy.None

If you will set it to CellValueFormatStrategy.None, then it will export the data without any formatting.

The following sample explains the use of [ExportTableOptions.FormatStrategy](https://apireference.aspose.com/net/cells/aspose.cells/exporttableoptions/properties/formatstrategy) property to export excel data with and without any formatting.

## Console Output

Below is the console debug output of the above sample code

{{< code lang="cs" >}}
Cell String Value: 0.01
Cell String Value without Format: 0.012345
Export Data Table with Format Strategy as Cell Style: 0.01
Export Data Table with Format Strategy as None: 0.012345
{{< /code >}}

