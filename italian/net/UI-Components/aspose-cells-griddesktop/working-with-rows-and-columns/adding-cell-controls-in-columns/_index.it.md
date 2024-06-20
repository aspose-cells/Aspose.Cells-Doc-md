---
title: Aggiunta di Controlli della Cella nelle Colonne
type: docs
weight: 90
url: /it/net/aspose-cells-griddesktop/add-cell-controls-in-columns/
keywords: GridDesktop,add,control,controls
description: Questo articolo illustra come aggiungere un controllo nella colonna in GridDesktop.
---

{{% alert color="primary" %}} 

Nelle nostre discussioni successive, abbiamo parlato di come aggiungere e gestire controlli delle celle nel foglio di calcolo. Ma, usando quegli approcci, possiamo aggiungere controlli delle celle una per volta a celle singole. Cosa succede se qualcuno volesse aggiungere controlli delle celle a tutte le celle di una o più colonne? In tali casi, per ridurre gli sforzi degli sviluppatori, Aspose.Cells.GridDesktop fornisce la funzionalità di aggiungere controlli delle celle per colonna. Significa che gli sviluppatori possono solo selezionare una colonna desiderata e specificare qualsiasi controllo della cella. Il controllo della cella specificato verrà aggiunto a tutte le celle della colonna specificata. Vediamo come possiamo utilizzare questa funzionalità.

{{% /alert %}} 
## **Introduzione**
Attualmente, Aspose.Cells.GridDesktop supporta l'aggiunta di tre tipi di controlli delle celle, che includono i seguenti:

- **Pulsante**
- **Casella di controllo**
- **ComboBox**

Tutti questi controlli derivano da una classe astratta, **CellControl**.

**IMPORTANTE:** Se si desidera aggiungere controlli delle celle a una singola cella invece che a tutta la colonna, è possibile fare riferimento a [Aggiungere Controlli delle Celle nei Fogli di Calcolo.](/cells/it/net/adding-cell-controls-in-worksheets/)
### **Aggiunta di un pulsante**
Per aggiungere pulsanti in una colonna utilizzando Aspose.Cells.GridDesktop, seguire i seguenti passaggi:

- Aggiungi il controllo Aspose.Cells.GridDesktop al tuo **Form**
- Accedere a qualsiasi **Foglio di lavoro** desiderato
- Aggiungi **Pulsante** in una colonna specifica del **Foglio di lavoro**

**NOTA:** Aggiungendo un **Pulsante**, possiamo specificare larghezza, altezza e didascalia del pulsante.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingButton.cs" >}}


Il frammento di codice precedente aggiunge pulsanti a tutte le celle della colonna specificata. Ogni volta che viene selezionata una cella di quella colonna specifica, un pulsante diventa visibile. Per ulteriori informazioni sull'handling degli eventi dei pulsanti, fare riferimento a [Handling degli Eventi di un Controllo Pulsante.](/cells/it/net/adding-cell-controls-in-worksheets/#event-handling-of-button)
### **Aggiunta di CheckBox**
Per aggiungere checkbox in una colonna utilizzando Aspose.Cells.GridDesktop, seguire i seguenti passaggi:

- Aggiungi il controllo Aspose.Cells.GridDesktop al tuo **Form**
- Accedere a qualsiasi **Foglio di lavoro** desiderato
- Aggiungi **CheckBox** in una colonna specifica del **Foglio di lavoro**

**NOTA:** Aggiungendo **CheckBox**, è possibile specificare anche lo stato della casella di controllo.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCheckbox.cs" >}}


Il frammento di codice precedente aggiunge checkbox a tutte le celle della colonna specificata. Per ulteriori informazioni sull'handling degli eventi delle checkbox, fare riferimento a [Handling degli Eventi di un Controllo Checkbox.](/cells/it/net/adding-cell-controls-in-worksheets/#event-handling-of-checkbox)
### **Aggiunta di ComboBox**
Per aggiungere combobox in una colonna utilizzando Aspose.Cells.GridDesktop, seguire i seguenti passaggi:

- Aggiungi il controllo Aspose.Cells.GridDesktop al tuo **Form**
- Accedere a qualsiasi **Foglio di lavoro** desiderato
- Crea un array di elementi (o valori) che saranno aggiunti alla **ComboBox**
- Aggiungi **ComboBox** (contenente elementi o valori) in una colonna specifica del **Foglio di lavoro**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCombobox.cs" >}}


Il frammento di codice precedente aggiunge combobox a tutte le celle della colonna specificata. Ogni volta che viene selezionata una cella di quella colonna specifica, un combobox diventa visibile. Per ulteriori informazioni sull'handling degli eventi dei combobox, fare riferimento a [Handling degli Eventi di un Controllo ComboBox.](/cells/it/net/adding-cell-controls-in-worksheets/#event-handling-of-combobox)
