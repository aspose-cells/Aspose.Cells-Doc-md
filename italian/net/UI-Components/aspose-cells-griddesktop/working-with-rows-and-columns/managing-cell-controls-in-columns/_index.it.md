---
title: Gestione dei controlli delle celle nelle colonne
type: docs
weight: 100
url: /it/net/aspose-cells-griddesktop/manage-cell-controls-in-columns/
keywords: GridDesktop,controlli,controllo
description: Questo articolo introduce come impostare il controllo nella colonna GridDesktop.
---

{{% alert color="primary" %}} 

Questo argomento discute alcuni concetti importanti sulla gestione dei controlli delle celle nelle colonne utilizzando l'API Aspose.Cells.GridDesktop. Spiegheremo come gli sviluppatori possono accedere, modificare e rimuovere i controlli delle celle dalle colonne dei loro fogli di lavoro. Diamo un'occhiata a questo.

{{% /alert %}} 
## **Accesso ai controlli delle celle**
Per accedere e modificare un controllo di cella esistente nella colonna, gli sviluppatori possono utilizzare la proprietà CellControl di un **Aspose.Cells.GridDesktop.Data.GridColumn**. Una volta che si accede a un controllo di cella, gli sviluppatori possono modificarne le proprietà in tempo reale. Ad esempio, nell'esempio riportato di seguito, abbiamo accesso a un controllo di cella **CheckBox** esistente da una specifica **Aspose.Cells.GridDesktop.Data.GridColumn** e ne abbiamo modificato la proprietà Checked.

**IMPORTANTE:** La proprietà CellControl fornisce un controllo di cella sotto forma di oggetto **CellControl**. Quindi, se è necessario accedere a un tipo specifico di controllo di cella, ad esempio **CheckBox**, sarà necessario eseguire il cast dell'oggetto **CellControl** alla classe **CheckBox**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-AccessCheckbox.cs" >}}
## **Rimozione dei controlli delle celle**
Per rimuovere un controllo di cella esistente, gli sviluppatori possono semplicemente accedere a un foglio di lavoro desiderato e quindi rimuovere il controllo di cella dalla colonna specifica utilizzando il metodo **RemoveCellControl** di **Aspose.Cells.GridDesktop.Data.GridColumn**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-RemoveCheckbox.cs" >}}

{{% alert color="primary" %}} 

Ogni colonna nella raccolta **Columns** del **Worksheet** è rappresentata da un'istanza della classe **Aspose.Cells.GridDesktop.Data.GridColumn**.

{{% /alert %}}
