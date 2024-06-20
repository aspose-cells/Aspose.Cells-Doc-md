---
title: Aggiunta di controlli di celle nei fogli di lavoro
type: docs
weight: 120
url: /it/net/aspose-cells-griddesktop/add-cell-controls-in-worksheets/
keywords: GridDesktop,add,control,button,checkbox,combobox
description: Questo articolo introduce come aggiungere un controllo nel foglio di lavoro in GridDesktop.
---

{{% alert color="primary" %}} 

I controlli delle celle sono in realtà quei controlli che possono essere aggiunti ai fogli di lavoro. Li chiamiamo **Controlli delle celle** perché questi controlli vengono visualizzati nelle celle. In questo argomento, parleremo di come aggiungere e gestire gli eventi di questi controlli delle celle.

{{% /alert %}} 
## **Introduzione**
Attualmente, Aspose.Cells.GridDesktop supporta l'aggiunta di tre tipi di controlli delle celle, che includono i seguenti:

- **Pulsante**
- **Casella di controllo**
- **ComboBox**

Tutti questi controlli derivano da una classe astratta, **CellControl**. Ogni foglio di lavoro contiene una raccolta di **Controlli**. I nuovi controlli delle celle possono essere aggiunti e quelli esistenti possono essere accessibili utilizzando facilmente questa collezione di **Controlli**.

**IMPORTANTE:** Se si desidera aggiungere controlli alle celle di una colonna anziché aggiungerli uno per uno, è possibile fare riferimento a [Gestione dei controlli delle celle nelle colonne.](/cells/it/net/aspose-cells-griddesktop/adding-cell-controls-in-worksheets/)
### **Aggiunta di un pulsante**
Per aggiungere un pulsante nel foglio di lavoro utilizzando Aspose.Cells.GridDesktop, seguire i passaggi seguenti:

- Aggiungi il controllo Aspose.Cells.GridDesktop al tuo **Form**
- Accedi a qualsiasi **Foglio di lavoro** desiderato
- Aggiungere un **Pulsante** alla raccolta **Controlli** del **Foglio di lavoro**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingButton.cs" >}}


Durante l'aggiunta del **Pulsante**, è possibile specificare la posizione della cella (dove visualizzarla), larghezza e altezza e la didascalia del pulsante.
#### **Gestione degli eventi del pulsante**
Abbiamo parlato di aggiungere un controllo di **Pulsante** al **Foglio di lavoro** ma qual è il vantaggio di avere un semplice pulsante nel foglio di lavoro se non possiamo usarlo. Quindi, qui entra in gioco la necessità di gestire gli eventi del pulsante.

Per gestire l'evento **Clic** del controllo **Pulsante**, Aspose.Cells.GridDesktop fornisce l'evento **CellButtonClick** che dovrebbe essere implementato dagli sviluppatori secondo le loro esigenze. Ad esempio, abbiamo appena visualizzato un messaggio quando il pulsante viene cliccato come mostrato di seguito:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingButton.cs" >}}
#### **Specifica di un'immagine di sfondo per il controllo del pulsante**
È possibile impostare un'immagine di sfondo/fotografia per il controllo del pulsante con la sua etichetta/testo come mostrato nel codice seguente:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-SetBackground.cs" >}}


**IMPORTANTE:** Tutti gli eventi dei controlli di cella contengono un argomento **CellControlEventArgs** che fornisce i numeri della riga e della colonna della cella che contiene il controllo di cella (il cui evento viene attivato).
### **Aggiunta di CheckBox**
Per aggiungere una casella di controllo nel foglio di lavoro utilizzando Aspose.Cells.GridDesktop, seguire i passaggi seguenti:

- Aggiungi il controllo Aspose.Cells.GridDesktop al tuo **Form**
- Accedi a qualsiasi **Foglio di lavoro** desiderato
- Aggiungi **CheckBox** alla collezione **Controls** del **Foglio di lavoro**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCheckbox.cs" >}}


Durante l'aggiunta di **CheckBox**, è possibile specificare la posizione della cella (dove visualizzarla) e lo stato della casella di controllo
#### **Gestione eventi di CheckBox**
Aspose.Cells.GridDesktop fornisce l'evento **CellCheckedChanged** che viene attivato quando lo stato **Checked** della casella di controllo viene modificato. Gli sviluppatori possono gestire questo evento secondo le proprie esigenze. Ad esempio, abbiamo appena mostrato un messaggio per mostrare lo stato **Checked** della casella di controllo nel codice sotto:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCheckbox.cs" >}}
### **Aggiunta di ComboBox**
Per aggiungere una casella combinata nel foglio di lavoro utilizzando Aspose.Cells.GridDesktop, seguire i passaggi seguenti:

- Aggiungi il controllo Aspose.Cells.GridDesktop al tuo **Form**
- Accedi a qualsiasi **Foglio di lavoro** desiderato
- Crea un array di elementi (o valori) che verranno aggiunti a **ComboBox**
- Aggiungi **ComboBox** alla collezione **Controls** del **Foglio di lavoro** specificando la posizione della cella (dove verrà visualizzata la casella combinata) e gli elementi/valori che verranno visualizzati quando la casella combinata verrà cliccata



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCombobox.cs" >}}
#### **Gestione eventi di ComboBox**
Aspose.Cells.GridDesktop fornisce l'evento **CellSelectedIndexChanged** che viene attivato quando l'**Indice Selezionato** della casella combinata viene modificato. Gli sviluppatori possono gestire questo evento secondo i loro desideri. Ad esempio, abbiamo appena mostrato un messaggio per mostrare l'**Elemento Selezionato** della casella combinata:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCombobox.cs" >}}
