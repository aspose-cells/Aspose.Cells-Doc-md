---
title: Exportera Excel-data till DataTable utan någon formatering
type: docs
weight: 280
url: /sv/net/export-excel-data-to-datatable-without-any-formatting/
---
{{% alert color="primary" %}}

Ibland vill användare exportera Excel-data till en datatabell utan någon formatering. Till exempel, om en cell har värdet 0,012345 och den är formaterad så att den visar två decimaler, när användaren exporterar Excel-data till en datatabell, kommer den att exporteras som 0,01 och inte som 0,012345. För att hantera detta problem har Aspose.Cells tillhandahållit[**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy) egendom som kan ta ett av dessa tre värden

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

 Om du vill ställa in det på[**CellValueFormatStrategy.None**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy), sedan exporterar den data utan någon formatering.

{{% /alert %}}

## Exempelkod

 Följande exempel förklarar användningen av[**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy)egenskap för att exportera Excel-data med och utan formatering.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ExportExcelDataToDataTableWithoutFormatting-ExportExcelDataToDataTableWithoutFormatting.cs" >}}

## **Konsolutgång**

Nedan är konsolens felsökningsutgång för ovanstående exempelkod

{{< highlight "java" >}}

Cell String Value: 0.01

Cell String Value without Format: 0.012345

Export Data Table with Format Strategy as Cell Style: 0.01

Export Data Table with Format Strategy as None: 0.012345

{{< /highlight >}}
