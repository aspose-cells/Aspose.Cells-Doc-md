---
title: Esportare i dati di Excel in DataTable senza alcun formato
type: docs
weight: 280
url: /it/net/export-excel-data-to-datatable-without-any-formatting/
description: Scopri come esportare i dati di Excel in DataTable senza alcun formato tramite l API Aspose.Cells for .NET.
keywords: Esportare i dati di Excel in DataTable senza alcun formato, Specificare la strategia del formato del valore della cella, Aggiungere una strategia del formato durante l esportazione dei dati in DataTable. 
---

{{% alert color="primary" %}}

A volte gli utenti desiderano esportare i dati di Excel in una tabella senza alcun formato. Ad esempio, se alcune celle hanno un valore di 0.012345 e sono formattate per mostrare due posizioni decimali, allora quando l'utente esporterà i dati di Excel in una tabella, verranno esportati come 0.01 e non come 0.012345. Per affrontare questo problema, Aspose.Cells ha fornito la proprietà [**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy) che può assumere uno di questi tre valori

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

Se lo imposti su [**CellValueFormatStrategy.None**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy), allora esporterà i dati senza alcuna formattazione.

{{% /alert %}}

## Codice di esempio

Il seguente esempio spiega l'uso della proprietà [**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy) per esportare i dati di Excel con e senza formattazione.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ExportExcelDataToDataTableWithoutFormatting-ExportExcelDataToDataTableWithoutFormatting.cs" >}}

## **Output della console**

Di seguito è riportato l'output di debug della console del codice di esempio precedente

{{< highlight java >}}

Cell String Value: 0.01

Cell String Value without Format: 0.012345

Export Data Table with Format Strategy as Cell Style: 0.01

Export Data Table with Format Strategy as None: 0.012345

{{< /highlight >}}
