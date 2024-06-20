---
title: Esportazione dei dati da Grid
type: docs
weight: 60
url: /it/net/aspose-cells-griddesktop/export-data-from-grid/
keywords: GridDesktop, esportazione, dati, esportazione dati
description: Questo articolo introduce come esportare dati in GridDesktop.
---

{{% alert color="primary" %}} 

Nel nostro argomento precedente, abbiamo parlato dell'importazione dei contenuti di un DataTable nel controllo Aspose.Cells.GridDesktop ma non abbiamo intenzionalmente menzionato che Aspose.Cells.GridDesktop supporta anche il processo inverso. Quindi, in questo argomento, discuteremo dell'esportazione dei dati all'interno del controllo Aspose.Cells.GridDesktop in un DataTable.

{{% /alert %}} 
## **Esportazione dei contenuti del Grid**
### **Esportazione in un DataTable specifico**
Per esportare i contenuti del Grid in un oggetto DataTable specifico, seguire i passaggi seguenti: Aggiungere il controllo Aspose.Cells.GridDesktop al proprio **Form**.

- Creare un oggetto DataTable specifico in base alle proprie esigenze.
- Esportare i dati di un **Worksheet** selezionato nel proprio oggetto DataTable specificato.

Nell'esempio qui riportato, abbiamo creato un oggetto specifico DataTable con quattro colonne all'interno. Infine, abbiamo esportato i dati del foglio di lavoro (a partire dalla prima cella con 69 righe e 4 colonne) in un oggetto DataTable già creato da noi.

**Esempio:**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToSpecificDataTable.cs" >}}
### **Esportazione in un nuovo DataTable**
A volte, gli sviluppatori potrebbero non essere interessati a creare il proprio oggetto DataTable e potrebbero avere solo la necessità di esportare i dati del foglio di lavoro in un nuovo oggetto DataTable. Sarebbe il modo più veloce per gli sviluppatori di esportare semplicemente i dati del foglio di lavoro.

Nell'esempio qui riportato, abbiamo provato un modo diverso per spiegare l'uso del metodo ExportDataTable. Abbiamo preso il riferimento del foglio di lavoro attualmente attivo e successivamente abbiamo esportato i dati completi di quel foglio di lavoro attivo in un nuovo oggetto DataTable. Questo oggetto DataTable può essere utilizzato in qualsiasi modo lo desideri uno sviluppatore. A titolo esemplificativo, uno sviluppatore potrebbe associare questo oggetto DataTable a un DataGrid per visualizzare i dati.

**Esempio:**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToNewDataTable.cs" >}}

{{% alert color="primary" %}} 

In questo caso, useremo una versione sovraccaricata del metodo ExportDataTable che restituirà semplicemente un nuovo oggetto DataTable contenente i dati esportati dal foglio di lavoro.

{{% /alert %}}
