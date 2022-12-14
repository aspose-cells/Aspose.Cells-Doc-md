---
title: Gestione dei controlli Cell nelle colonne
type: docs
weight: 100
url: /it/net/managing-cell-controls-in-columns/
---
{{% alert color="primary" %}} 

Questo argomento discute alcuni concetti importanti sulla gestione dei controlli cella nelle colonne usando Aspose.Cells.GridDesktop API. Spiegheremo come gli sviluppatori possono accedere, modificare e rimuovere i controlli cella dalle colonne dei loro fogli di lavoro. Diamo un'occhiata.

{{% /alert %}} 
## **Accesso ai controlli Cell**
 Per accedere e modificare un controllo cella esistente nella colonna, gli sviluppatori possono utilizzare la proprietà CellControl di a**Aspose.Cells.GridDesktop.Data.GridColumn** . Una volta effettuato l'accesso a un controllo cella, gli sviluppatori possono modificarne le proprietà in fase di esecuzione. Ad esempio, nell'esempio fornito di seguito, abbiamo avuto accesso a un file esistente**Casella di controllo** controllo cellulare da uno specifico**Aspose.Cells.GridDesktop.Data.GridColumn** e ne ha modificato la proprietà Checked.

**IMPORTANTE:** La proprietà CellControl fornisce un controllo cella sotto forma di**CellControl**oggetto. Quindi, se hai bisogno di accedere a un tipo specifico di controllo cellulare, ad esempio**Casella di controllo** quindi dovrai digitare il file**CellControl** opporsi a**Casella di controllo** classe.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-AccessCheckbox.cs" >}}
## **Rimozione dei comandi Cell**
 Per rimuovere un controllo cella esistente, gli sviluppatori possono semplicemente accedere a un foglio di lavoro desiderato e quindi**Rimuovere** il controllo della cella dalla colonna specifica utilizzando il**RemoveCellControl** metodo di**Aspose.Cells.GridDesktop.Data.GridColumn**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-RemoveCheckbox.cs" >}}

{{% alert color="primary" %}} 

 Ogni colonna del**Colonne** raccolta del**Foglio di lavoro** è rappresentato da un'istanza di**Aspose.Cells.GridDesktop.Data.GridColumn** classe.

{{% /alert %}}
