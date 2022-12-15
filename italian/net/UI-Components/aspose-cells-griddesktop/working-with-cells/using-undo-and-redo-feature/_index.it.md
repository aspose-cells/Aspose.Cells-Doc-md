---
title: Utilizzo della funzione Annulla e Ripristina
type: docs
weight: 120
url: /it/net/using-undo-and-redo-feature/
---
{{% alert color="primary" %}} 

La funzione Annulla/Ripristina di GridDesktop è molto utile. Il nome spiega la sua stessa funzionalità, ti consente di annullare/ripristinare le azioni recenti in un foglio di lavoro. Ad esempio, se una formula viene eliminata accidentalmente o si modificano i dati in una cella che non si desidera effettivamente, queste azioni possono essere corrette utilizzando le operazioni Annulla e Ripristina fornite dal controllo.

{{% /alert %}} 
## **Esecuzione di operazioni di annullamento e ripristino**
Le seguenti API sono disponibili per l'attività. La descrizione è fornita con ciascuna API, controllale.

- **GridDesktop.EnableAnnulla** - attributo: indica se la funzione Undo è abilitata, il valore di default è "false".
- **Annulla Manager** – classe: viene utilizzata per gestire l'operazione di annullamento/ripristino.
- **GridDesktop.UndoManager** – attributo: ottiene l'istanza di the**Annulla Manager** oggetto.
- **AnnullaManager.Annulla** – metodo: esegue un'operazione di annullamento.
- **UndoManager.Redo -**metodo: esegue l'operazione di ripristino.
- **UndoManager.ClearStack** – metodo: cancella lo stack annulla/ripristina.
- **UndoManager.UndoStepsCount** – attributo: ottiene il conteggio degli attuali passaggi di annullamento disponibili.
- **UndoManager.RedoStepsCount** – attributo: ottiene il conteggio degli attuali passaggi di ripetizione disponibili.
- **UndoManager.UndoStackSize** – attributo: ottiene/imposta la dimensione dello stack di annullamento.
### **Annullare**
Il codice di esempio seguente mostra come implementare l'operazione Undo usando l'API GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Undo.cs" >}}
### **Rifare**
Il codice di esempio seguente mostra come implementare l'operazione Redo usando l'API GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Redo.cs" >}}

{{% alert color="primary" %}} 

Attualmente, l'operazione di annullamento/ripristino si riferisce alla modifica del valore di una cella.

{{% /alert %}}
