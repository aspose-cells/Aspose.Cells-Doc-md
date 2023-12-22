---
title: Esporta dati Excel in DataTable senza alcuna formattazione
type: docs
weight: 280
url: /it/net/export-excel-data-to-datatable-without-any-formatting/
description: Scopri come esportare dati Excel in DataTable senza alcuna formattazione tramite Aspose.Cells for .NET API.
keywords: Export Excel Data to DataTable without any Formatting, Specify Cell Value Format Strategy, Add Format Strategy When Exporting Data to DataTable. 
---
{{% alert color="primary" %}}

 volte gli utenti desiderano esportare dati Excel in una tabella dati senza alcuna formattazione. Ad esempio, se una cella ha un valore 0,012345 ed è formattata in modo da visualizzare due cifre decimali, quando l'utente esporterà i dati Excel in una tabella dati, verrà esportata come 0,01 e non come 0,012345. Per far fronte a questo problema ha provveduto lo Aspose.Cells[**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy) proprietà che può assumere uno di questi tre valori

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

 Se lo imposterai su[**CellValueFormatStrategy.None**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy), quindi esporterà i dati senza alcuna formattazione.

{{% /alert %}}

##  Codice d'esempio

 L'esempio seguente spiega l'uso di[**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy)proprietà per esportare dati Excel con e senza alcuna formattazione.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ExportExcelDataToDataTableWithoutFormatting-ExportExcelDataToDataTableWithoutFormatting.cs" >}}

##  **Uscita della console**

Di seguito è riportato l'output di debug della console del codice di esempio riportato sopra

{{< highlight "java" >}}

Cell String Value: 0.01

Cell String Value without Format: 0.012345

Export Data Table with Format Strategy as Cell Style: 0.01

Export Data Table with Format Strategy as None: 0.012345

{{< /highlight >}}
