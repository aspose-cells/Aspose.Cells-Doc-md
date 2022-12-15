---
title: Gestione dei controlli Cell nei fogli di lavoro
type: docs
weight: 130
url: /it/net/managing-cell-controls-in-worksheets/
---
{{% alert color="primary" %}} 

In questo argomento vengono illustrati alcuni concetti importanti sulla gestione dei controlli cella tramite l'API di Aspose.Cells.GridDesktop. Spiegheremo come gli sviluppatori possono accedere, modificare e rimuovere i controlli delle celle dai loro fogli di lavoro. Diamo un'occhiata.

{{% /alert %}} 
## **Accesso ai controlli Cell**
 Per accedere e modificare un controllo cella esistente nel foglio di lavoro, gli sviluppatori possono accedere a un controllo cella specifico dal file**Controlli** raccolta del**Foglio di lavoro** specificando la cella (usando il nome della cella o la sua posizione in termini di numeri di riga e colonna) in cui viene visualizzato il controllo della cella. Una volta effettuato l'accesso a un controllo cella, gli sviluppatori possono modificarne le proprietà in fase di esecuzione. Ad esempio, nell'esempio fornito di seguito, abbiamo avuto accesso a un file esistente**Casella di controllo** controllo cellulare da**Foglio di lavoro** e ne ha modificato la proprietà Checked.

**IMPORTANTE:** **Controlli** la raccolta contiene tutti i tipi di controlli cellulari sotto forma di**CellControl** oggetti. Quindi, se hai bisogno di accedere a un tipo specifico di controllo cellulare, ad esempio**Casella di controllo** quindi dovrai digitare il file**CellControl** opporsi a**Casella di controllo** classe.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-AccessCheckbox.cs" >}}
## **Rimozione dei comandi Cell**
 Per rimuovere un controllo cella esistente, gli sviluppatori possono semplicemente accedere a un foglio di lavoro desiderato e quindi**Rimuovere** il controllo cellulare dal**Controlli** raccolta del**Foglio di lavoro** specificando la cella (usando il suo nome o il numero di riga e colonna) contenente il controllo cella.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-RemoveCheckbox.cs" >}}
