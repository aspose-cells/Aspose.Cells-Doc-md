---
title: Gestione dei controlli di cella nei fogli di lavoro
type: docs
weight: 130
url: /it/net/aspose-cells-griddesktop/manage-cell-controls-in-worksheets/
keywords: GridDesktop,controllo di cella,controllo,controlli
description: Questo articolo introduce come lavorare con i controlli delle celle in GridDesktop.
---

{{% alert color="primary" %}} 

Questo argomento discute alcuni concetti importanti sulla gestione dei controlli delle celle utilizzando l'API di Aspose.Cells.GridDesktop. Spiegheremo come gli sviluppatori possono accedere, modificare e rimuovere i controlli delle celle dai loro fogli di lavoro. Diamo un'occhiata.

{{% /alert %}} 
## **Accesso ai controlli delle celle**
Per accedere e modificare un controllo di cella esistente nel foglio di lavoro, gli sviluppatori possono accedere a un controllo di cella specifico dalla collezione **Controls** della classe **Worksheet** specificando la cella (utilizzando il nome della cella o la sua posizione in termini di numeri di riga e colonna) in cui viene visualizzato il controllo di cella. Una volta che un controllo di cella viene accesso, gli sviluppatori possono modificare le sue proprietà durante l'esecuzione. Ad esempio, nell'esempio riportato di seguito, abbiamo accesso a un controllo di cella **CheckBox** esistente dal **Worksheet** e modificato la sua proprietà Checked.

**IMPORTANTE:** La collezione **Controls** contiene tutti i tipi di controlli di cella sotto forma di oggetti **CellControl**. Pertanto, se è necessario accedere a un tipo specifico di controllo cella, ad esempio **CheckBox**, sarà necessario eseguire il cast dell'oggetto **CellControl** alla classe **CheckBox**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-AccessCheckbox.cs" >}}
## **Rimozione dei controlli delle celle**
Per rimuovere un controllo di cella esistente, gli sviluppatori possono semplicemente accedere a un foglio di lavoro desiderato e quindi **rimuovere** il controllo di cella dalla collezione **Controls** della classe **Worksheet** specificando la cella (utilizzando il suo nome o il numero di riga e colonna) contenente il controllo di cella.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-RemoveCheckbox.cs" >}}
