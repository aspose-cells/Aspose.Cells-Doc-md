---
title: Usa la funzione Annulla e Ripeti
type: docs
weight: 120
url: /it/net/aspose-cells-griddesktop/use-undo-and-redo-feature/
keywords: GridDesktop, annulla, ripeti
description: Questo articolo introduce la funzione annulla e ripeti in GridDesktop.
---

{{% alert color="primary" %}} 

La funzione Annulla/Ripeti di GridDesktop è molto utile. Il nome spiega già la sua funzionalità, consente di annullare/ripetere azioni recenti in un foglio di lavoro. Ad esempio, se una formula viene eliminata accidentalmente o si modifica dati in una cella che in realtà non si desidera, queste azioni possono essere corrette utilizzando le operazioni Annulla e Ripeti fornite dal controllo.

{{% /alert %}} 
## **Eseguire l'Operazione di Annulla e Ripeti**
Le seguenti API sono disponibili per il compito. La descrizione è fornita con ciascuna API, per favore controlla.

- **GridDesktop.EnableUndo** - attributo: Indica se la funzione Annulla è abilitata, il valore predefinito è "false".
- **UndoManager** - classe: Viene utilizzata per gestire l'operazione annulla/ripeti.
- **GridDesktop.UndoManager** - attributo: Ottiene l'istanza dell'oggetto **UndoManager**.
- **UndoManager.Undo** - metodo: Esegue un'operazione Annulla.
- **UndoManager.Redo** - metodo: Esegue l'operazione ripeti.
- **UndoManager.ClearStack** - metodo: Cancella la pila annulla/ripeti.
- **UndoManager.UndoStepsCount** - attributo: Ottiene il conteggio delle attuali operazioni di annulla disponibili.
- **UndoManager.RedoStepsCount** - attributo: Ottiene il conteggio delle attuali operazioni di ripeti disponibili.
- **UndoManager.UndoStackSize** - attributo: Ottiene/imposta la dimensione della pila annulla.
### **Annulla**
Il codice di esempio seguente mostra come implementare l'operazione Annulla utilizzando l'API GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Undo.cs" >}}
### **Ripeti**
Il codice di esempio seguente mostra come implementare l'operazione Ripeti utilizzando l'API GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Redo.cs" >}}

{{% alert color="primary" %}} 

Attualmente, l'operazione annulla/ripeti si riferisce al cambiamento nel valore di una cella.

{{% /alert %}}
