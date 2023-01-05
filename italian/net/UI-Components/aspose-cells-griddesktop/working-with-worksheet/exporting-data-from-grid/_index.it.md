---
title: Esportazione di dati dalla griglia
type: docs
weight: 60
url: /it/net/exporting-data-from-grid/
---
{{% alert color="primary" %}} 

Nel nostro argomento precedente, abbiamo parlato dell'importazione del contenuto di un DataTable nel controllo Aspose.Cells.GridDesktop ma non abbiamo volutamente menzionato che Aspose.Cells.GridDesktop supporta anche il processo inverso. Quindi, in questo argomento, discuteremo dell'esportazione dei dati all'interno del controllo Aspose.Cells.GridDesktop in un DataTable.

{{% /alert %}} 
## **Esportazione del contenuto della griglia**
### **Esportazione in un DataTable specifico**
 Per esportare il contenuto della griglia in un oggetto DataTable specifico, procedi nel seguente modo: Aggiungi il controllo Aspose.Cells.GridDesktop al tuo**Modulo**.

- Crea un oggetto DataTable specifico in base alle tue esigenze.
-  Esporta i dati di un selezionato**Foglio di lavoro** all'oggetto DataTable specificato.

Nell'esempio riportato di seguito, abbiamo creato un oggetto DataTable specifico con quattro colonne all'interno. Infine, abbiamo esportato i dati del foglio di lavoro (a partire dalla prima cella con 69 righe e 4 colonne) in un oggetto DataTable già creato da noi.

**Esempio:**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToSpecificDataTable.cs" >}}
### **Esportazione in un nuovo DataTable**
volte, gli sviluppatori potrebbero non essere interessati a creare il proprio oggetto DataTable e potrebbero avere la semplice necessità di esportare semplicemente i dati del foglio di lavoro in un nuovo oggetto DataTable. Sarebbe il modo più rapido per gli sviluppatori di esportare semplicemente i dati del foglio di lavoro.

Nell'esempio fornito di seguito, abbiamo provato un modo diverso per spiegare l'utilizzo del metodo ExportDataTable. Abbiamo preso il riferimento del foglio di lavoro attualmente attivo e quindi abbiamo esportato i dati completi di quel foglio di lavoro attivo in un nuovo oggetto DataTable. Ora, questo oggetto DataTable può essere utilizzato in qualsiasi modo uno sviluppatore desideri. Solo per esempio, uno sviluppatore può associare questo oggetto DataTable a un DataGrid per visualizzare i dati.

**Esempio:**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToNewDataTable.cs" >}}

{{% alert color="primary" %}} 

Nel caso precedente, utilizzeremo una versione sovraccaricata del metodo ExportDataTable che restituirà semplicemente un nuovo oggetto DataTable contenente i dati esportati dal foglio di lavoro.

{{% /alert %}}
