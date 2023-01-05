---
title: Aggiunta di controlli Cell nelle colonne
type: docs
weight: 90
url: /it/net/adding-cell-controls-in-columns/
---
{{% alert color="primary" %}} 

Nelle nostre discussioni successive, abbiamo discusso dell'aggiunta e della gestione dei controlli delle celle nel foglio di lavoro. Ma, usando questi approcci, possiamo aggiungere controlli di cella a singole celle uno per uno. Cosa succede se qualcuno desidera aggiungere controlli di cella a tutte le celle di una o più colonne? In tali casi, per ridurre gli sforzi degli sviluppatori, Aspose.Cells.GridDesktop fornisce la funzione di aggiungere controlli di cella per base di colonna. Significa che gli sviluppatori possono selezionare solo una colonna desiderata e specificare qualsiasi controllo cella. Il controllo cella specificato verrà aggiunto a tutte le celle della colonna specificata. Vediamo come possiamo utilizzare questa funzione.

{{% /alert %}} 
## **introduzione**
Attualmente, Aspose.Cells.GridDesktop supporta l'aggiunta di tre tipi di controlli cella, che includono quanto segue:

- **Pulsante**
- **Casella di controllo**
- **Casella combinata**

 Tutti questi controlli derivano da una classe astratta,**CellControl**.

**IMPORTANTE:** Se desideri aggiungere controlli di cella a una singola cella anziché all'intera colonna, puoi fare riferimento a[Aggiunta di controlli Cell nei fogli di lavoro.](/cells/it/net/adding-cell-controls-in-worksheets/)
### **Aggiunta di pulsante**
Per aggiungere pulsanti in una colonna utilizzando Aspose.Cells.GridDesktop, procedi nel seguente modo:

-  Aggiungi il controllo Aspose.Cells.GridDesktop al tuo**Modulo**
-  Accedi a qualsiasi desiderato**Foglio di lavoro**
-  Aggiungere**Pulsante** a qualsiasi specificato**Colonna** del**Foglio di lavoro**

**NOTA:** Durante l'aggiunta**Pulsante**, possiamo specificare la larghezza, l'altezza e la didascalia del pulsante.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingButton.cs" >}}


 Il frammento di codice sopra aggiunge pulsanti a tutte le celle della colonna specificata. Ogni volta che viene selezionata una cella di quella specifica colonna, diventa visibile un pulsante. Per ulteriori informazioni sulla gestione degli eventi dei pulsanti, fare riferimento a[Gestione degli eventi di un controllo Button.](/cells/it/net/adding-cell-controls-in-worksheets/#event-handling-of-button)
### **Aggiunta di CheckBox**
Per aggiungere caselle di controllo in una colonna utilizzando Aspose.Cells.GridDesktop, procedi nel seguente modo:

-  Aggiungi il controllo Aspose.Cells.GridDesktop al tuo**Modulo**
-  Accedi a qualsiasi desiderato**Foglio di lavoro**
-  Aggiungere**Casella di controllo** a qualsiasi specificato**Colonna** del**Foglio di lavoro**

**NOTA:** Durante l'aggiunta**Casella di controllo**, possiamo anche specificare lo stato della casella di controllo.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCheckbox.cs" >}}


 Lo snippet di codice sopra aggiunge caselle di controllo a tutte le celle della colonna specificata. Per ulteriori informazioni sulla gestione degli eventi delle caselle di controllo, fare riferimento a[Gestione degli eventi di un controllo CheckBox.](/cells/it/net/adding-cell-controls-in-worksheets/#event-handling-of-checkbox)
### **Aggiunta di ComboBox**
Per aggiungere caselle combinate in una colonna utilizzando Aspose.Cells.GridDesktop, procedi nel seguente modo:

-  Aggiungi il controllo Aspose.Cells.GridDesktop al tuo**Modulo**
-  Accedi a qualsiasi desiderato**Foglio di lavoro**
-  Crea un array di elementi (o valori) a cui verranno aggiunti**Casella combinata**
-  Aggiungere**Casella combinata** (contenente elementi o valori) a qualsiasi specificato**Colonna** del**Foglio di lavoro**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCombobox.cs" >}}


 Il frammento di codice sopra aggiunge caselle combinate a tutte le celle della colonna specificata. Ogni volta che viene selezionata una cella di quella specifica colonna, diventa visibile una casella combinata. Per ulteriori informazioni sulla gestione degli eventi delle caselle combinate, fare riferimento a[Gestione degli eventi di un controllo ComboBox.](/cells/it/net/adding-cell-controls-in-worksheets/#event-handling-of-combobox)
