---
title: Esporta DataTable da GridWeb
type: docs
weight: 70
url: /it/net/export-datatable-from-gridweb/
---
{{% alert color="primary" %}} 

[Importa DataView in GridWeb](/cells/it/net/import-dataview-to-gridweb/)ha parlato dell'importazione del contenuto di un DataView nel controllo Aspose.Cells.GridWeb. Questo argomento illustra l'esportazione dei dati dal controllo Aspose.Cells.GridWeb a un DataTable.

{{% /alert %}} 
## **Esportazione dei dati del foglio di lavoro**
### **A un DataTable specifico**
Per esportare i dati del foglio di lavoro in un oggetto DataTable specifico:

1. Aggiungere il controllo Aspose.Cells.GridWeb al Web Form.
1. Creare un oggetto DataTable specifico.
1. Esporta i dati delle celle selezionate nell'oggetto DataTable specificato.

L'esempio seguente crea un oggetto DataTable specifico con quattro colonne. I dati del foglio di lavoro vengono esportati a partire dalla prima cella con tutte le righe e le colonne visibili nel foglio di lavoro, in un oggetto DataTable già creato.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportDataTable.cs" >}}
### **A un nuovo DataTable**
A volte, non si desidera creare un oggetto DataTable ma è sufficiente esportare i dati del foglio di lavoro in un nuovo oggetto DataTable.

L'esempio seguente prova un modo diverso per mostrare l'uso del metodo Export. Prende il riferimento del foglio di lavoro attivo ed esporta i dati completi di quel foglio di lavoro in un nuovo oggetto DataTable. L'oggetto DataTable può ora essere utilizzato nel modo desiderato. Ad esempio, è possibile associare l'oggetto DataTable a un GridView per visualizzare i dati.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportNewDataTable.cs" >}}
