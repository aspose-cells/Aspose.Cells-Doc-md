---
title: Aggiunta di controlli Cell nei fogli di lavoro
type: docs
weight: 120
url: /it/net/adding-cell-controls-in-worksheets/
---
{{% alert color="primary" %}} 

 I controlli Cell sono infatti quei controlli che possono essere aggiunti ai fogli di lavoro. Li chiamiamo**Cell Comandi** perché questi controlli vengono visualizzati nelle celle. In questo argomento, parleremo dell'aggiunta e della gestione degli eventi di questi controlli cella.

{{% /alert %}} 
## **introduzione**
Attualmente, Aspose.Cells.GridDesktop supporta l'aggiunta di tre tipi di controlli cella, che includono quanto segue:

- **Pulsante**
- **Casella di controllo**
- **Combo box**

Tutti questi controlli derivano da una classe astratta,**CellControl**. Ogni foglio di lavoro contiene una raccolta di**Controlli**È possibile aggiungere nuovi controlli cella e accedere a quelli esistenti utilizzando questo**Controlli**raccolta facilmente.

**IMPORTANTE:**Se desideri aggiungere controlli di cella a tutte le celle di una colonna invece di aggiungerne uno per uno, puoi fare riferimento a[Gestione dei controlli Cell nelle colonne.](/cells/it/net/adding-cell-controls-in-worksheets/)
### **Aggiunta di pulsante**
Per aggiungere un pulsante nel foglio di lavoro utilizzando Aspose.Cells.GridDesktop, procedi nel seguente modo:

- Aggiungi il controllo Aspose.Cells.GridDesktop al tuo**Modulo**
- Accedi a qualsiasi desiderato**Foglio di lavoro**
- Aggiungere**Pulsante**al**Controlli**raccolta del**Foglio di lavoro**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingButton.cs" >}}


Durante l'aggiunta**Pulsante**, possiamo specificare la posizione della cella (dove visualizzarla), la larghezza e l'altezza e la didascalia del pulsante.
#### **Gestione degli eventi del pulsante**
Abbiamo discusso sull'aggiunta**Pulsante**controllo al**Foglio di lavoro**ma qual è il vantaggio di avere solo un pulsante nel foglio di lavoro se non possiamo usarlo. Quindi, ecco che nasce la necessità della gestione degli eventi del pulsante.

Per gestire il**Clic**evento del**Pulsante**controllo, Aspose.Cells.GridDesktop fornisce**CellButtonClic**evento che dovrebbe essere implementato dagli sviluppatori in base alle loro esigenze. Ad esempio, abbiamo appena visualizzato un messaggio quando si fa clic sul pulsante, come mostrato di seguito:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingButton.cs" >}}
#### **Specifica di un'immagine di sfondo per il controllo pulsante**
Possiamo impostare l'immagine/immagine di sfondo per il controllo del pulsante con la sua etichetta/testo come mostrato nel codice seguente:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-SetBackground.cs" >}}


**IMPORTANTE:**Tutti gli eventi dei controlli cella contengono a**CellControlEventArgs**argomento che fornisce i numeri di riga e colonna della cella che contiene il controllo cella (il cui evento viene attivato).
### **Aggiunta di CheckBox**
Per aggiungere una casella di controllo nel foglio di lavoro utilizzando Aspose.Cells.GridDesktop, procedi nel seguente modo:

- Aggiungi il controllo Aspose.Cells.GridDesktop al tuo**Modulo**
- Accedi a qualsiasi desiderato**Foglio di lavoro**
- Aggiungere**Casella di controllo**al**Controlli**raccolta del**Foglio di lavoro**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCheckbox.cs" >}}


Durante l'aggiunta**Casella di controllo**, possiamo specificare la posizione della cella (dove visualizzarla) e lo stato della casella di controllo.
#### **Gestione degli eventi di CheckBox**
Aspose.Cells.GridDesktop fornisce**CellCheckedChanged**evento che viene attivato quando il**Controllato**lo stato della casella di controllo è cambiato. Gli sviluppatori possono gestire questo evento in base alle proprie esigenze. Ad esempio, abbiamo appena visualizzato un messaggio per mostrare il file**Controllato**stato della casella di controllo nel codice seguente:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCheckbox.cs" >}}
### **Aggiunta di ComboBox**
Per aggiungere una casella combinata nel foglio di lavoro utilizzando Aspose.Cells.GridDesktop , procedi nel seguente modo:

- Aggiungi il controllo Aspose.Cells.GridDesktop al tuo**Modulo**
- Accedi a qualsiasi desiderato**Foglio di lavoro**
- Crea un array di elementi (o valori) a cui verranno aggiunti**Combo box**
- Aggiungere**Combo box**al**Controlli**raccolta del**Foglio di lavoro**specificando la posizione della cella (dove verrà visualizzata la casella combinata) e gli elementi/valori che verranno visualizzati quando si fa clic sulla casella combinata



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCombobox.cs" >}}
#### **Gestione degli eventi di ComboBox**
Aspose.Cells.GridDesktop fornisce**CellSelectedIndexChanged**evento che viene attivato quando il**Indice selezionato**della casella combinata è cambiato. Gli sviluppatori possono gestire questo evento secondo i loro desideri. Ad esempio, abbiamo appena visualizzato un messaggio per mostrare il file**Articolo selezionato**della casella combinata:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCombobox.cs" >}}
