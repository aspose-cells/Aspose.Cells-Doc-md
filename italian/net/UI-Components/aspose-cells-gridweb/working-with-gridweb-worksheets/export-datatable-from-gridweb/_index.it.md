---
title: Esporta DataTable da GridWeb
type: docs
weight: 70
url: /it/net/aspose-cells-gridweb/export-datatable-from-gridweb/
keywords: GridWeb, esportare
description: Questo articolo introduce come esportare una datatable in GridWeb.
---

{{% alert color="primary" %}} 

[Importare DataView in GridWeb](/cells/it/net/aspose-cells-gridweb/import-dataview-to-gridweb/) trattava dell'importazione dei contenuti di una DataView nel controllo Aspose.Cells.GridWeb. Questo argomento discute dell'esportazione dei dati dal controllo Aspose.Cells.GridWeb in una DataTable.

{{% /alert %}} 
## **Esportazione dei dati del foglio di calcolo**
### **Verso una specifica DataTable**
Per esportare i dati del foglio di lavoro in un oggetto DataTable specifico:

1. Aggiungi il controllo Aspose.Cells.GridWeb al tuo modulo web.
1. Crea un oggetto DataTable specifico.
1. Esporta i dati delle celle selezionate nell'oggetto DataTable specificato.

L'esempio qui sotto crea un oggetto DataTable specifico con quattro colonne. I dati del foglio di lavoro vengono esportati a partire dalla prima cella con tutte le righe e colonne visibili nel foglio di lavoro, verso un oggetto DataTable già creato.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportDataTable.cs" >}}
### **Verso un nuovo oggetto DataTable**
A volte, non si desidera creare un oggetto DataTable ma è sufficiente esportare i dati del foglio di lavoro in un nuovo oggetto DataTable.

L'esempio qui sotto cerca un modo diverso per mostrare l'uso del metodo di esportazione. Prende il riferimento del foglio di lavoro attivo e esporta i dati completi di quel foglio di lavoro in un nuovo oggetto DataTable. L'oggetto DataTable può ora essere utilizzato in qualsiasi modo desiderato. Ad esempio, è possibile associare l'oggetto DataTable a una GridView per visualizzare i dati.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportNewDataTable.cs" >}}
