---
title: Imposta DataSource personalizzato per WorkbookDesigner
type: docs
weight: 60
url: /it/net/set-custom-datasource-for-workbookdesigner/
---

Aspose.Cells fornisce l'opzione di impostare un DataSource personalizzato per WorkbookDesigner. L'API fornisce un metodo sovraccaricato [WorkbookDesigner.SetDataSource](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/setdatasource/methods/5) che prende il nome della sorgente come primo parametro e l'istanza della classe che implementa [ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable) come secondo parametro. 

Il seguente frammento di codice dimostra l'uso del metodo [WorkbookDesigner.SetDataSource](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/setdatasource/methods/5) per impostare il DataSource personalizzato.
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-1.cs" >}}

Di seguito è riportata l'implementazione delle classi *CustomerDataSource*, *Customer* e *CustomerList*

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}

I file excel sorgente e di output sono allegati a scopo informativo.

[File di origine](95584319.xlsx)

[File di output](95584320.xlsx)
