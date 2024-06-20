---
title: Scrivere script lato client di GridWeb
type: docs
weight: 10
url: /it/net/aspose-cells-gridweb/write-gridweb-client-side-script/
keywords: GridWeb,client,js,javascript
description: Questo articolo illustra come lavorare con le api js client in GridWeb.
---

{{% alert color="primary" %}} 

Gli sviluppatori possono scrivere script lato client per il controllo Aspose.Cells.GridWeb. Ciò significa che è possibile invocare una funzione JavaScript lato client per eseguire un compito specifico relativo al controllo GridWeb. Ad esempio, gli sviluppatori possono scrivere funzioni JavaScript per inviare i dati GridWeb a un server o mostrare un messaggio di allerta quando si verifica un errore di convalida ecc.

Questo argomento spiega questa funzionalità con l'aiuto di esempi.

{{% /alert %}} 
## **Scrittura di script lato client per Aspose.Cells.GridWeb**
### **Informazioni di base**
Aspose.Cells.GridWeb fornisce due proprietà create appositamente per supportare gli script lato client:

- OnSubmitClientFunction
- OnValidationErrorClientFunction

Creare funzioni JavaScript in una pagina ASPX e assegnare i nomi di queste funzioni alle proprietà OnSubmitClientFunction e OnValidationErrorClientFunction.

{{% alert color="primary" %}} 

La funzione JavaScript che verrà assegnata alla proprietà OnSubmitClientFunction deve essere definita correttamente come mostrato di seguito:

**JavaScript**

{{< highlight csharp >}}

 function function_name(arg, cancelEdit)

 {

   //Add javascript code here

 }



{{< /highlight >}}

dove il parametro [arg] rappresenta il comando generato dal controllo. Il comando può essere "Salva", "Invia", "Annulla" ecc. e il parametro [cancelEdit] è un valore booleano, che indica se l'input dell'utente è stato annullato o meno.

Qualsiasi funzione JavaScript assegnata alla proprietà OnSubmitClientFunction è chiamata ogni volta dal controllo GridWeb prima di inviare i dati di GridWeb a un server. Allo stesso modo, se una funzione è assegnata alla proprietà OnValidationErrorClientFunction, quella funzione verrà chiamata ogni volta che si verifica un errore di convalida.

{{% /alert %}} 
### **Funzioni per lo scripting lato client**
Aspose.Cells.GridWeb espone anche funzioni specialmente per lo scripting lato client. Queste funzioni possono essere utilizzate all'interno delle funzioni JavaScript per ottenere un maggiore controllo di Aspose.Cells.GridWeb. Queste funzioni lato client includono le seguenti:

|**Funzioni**|**Descrizione**|
| :- | :- |
|updateData(bool cancelEdit)|Aggiorna tutti i dati client di Aspose.Cells.GridWeb prima di inviarli al server. Se il parametro cancelEdit è true, allora GridWeb scarta tutti gli input dell'utente.|
|validateAll()|Usato per verificare se ci sono errori di convalida nell'input dell'utente. Se c'è un errore, la funzione restituisce false, altrimenti true.|
|submit(string arg, bool cancelEdit)|Chiama questa funzione per inviare dati al server. Questa funzione esegue entrambi i compiti, ovvero aggiornare i dati e convalidare l'input dell'utente. Questa funzione può anche generare un evento di comando lato server. Utilizzare il parametro arg per passare il comando. Ad esempio: il comando SAVE viene utilizzato per fare clic sul pulsante **Salva** nella barra dei comandi del controllo GridWeb e il comando CCMD:MYCOMMAND attiva un evento di comando personalizzato.|
|setActiveCell(int row, int column)|Usato per attivare una cella specifica.|
|setCellValue(int row, int column, string value)|Usato per inserire un valore in qualsiasi cella specificata utilizzando i suoi numeri di riga e colonna.|
|getCellValue(int row, int column)|Restituisce il valore di una cella specificata.|
|getActiveRow()|Utilizzato in combinazione con la funzione getActiveColumn() per determinare la posizione di una cella attiva.|
|getActiveColumn()|Usato in combinazione con la funzione getActiveRow() per determinare la posizione di una cella attiva.|
|getSelectRange()|Restituisce l'ultimo intervallo selezionato.|
|setSelectRange()|Seleziona l'intervallo dato.|
|clearSelections()|Pulisce tutta la selezione escludendo la cella attiva corrente.|
|getCellsArray()|Viene utilizzata con altre funzioni correlate come getCellName(), getCellValueByCell(), getCellRow() e getCellColumn(). Si prega di leggere questo articolo per ulteriori informazioni riguardanti l'utilizzo di questa funzione: [Leggere i valori delle celle di GridWeb sul lato client](/cells/it/net/aspose-cells-gridweb/read-the-values-of-the-gridweb-cells-on-client-side/)|
Per creare un'applicazione di test contenente script lato client che funzionano con Aspose.Cells.GridWeb, seguire i passaggi seguenti:

1. Creare le funzioni JavaScript da invocare da GridWeb.
   These functions will be added to the ASP.NET page's <script></script> tag.
1. Assegnare i nomi delle funzioni alle proprietà OnSubmitClientFunction e OnValidationErrorClientFunction.

L'output dell'esempio di codice è mostrato di seguito:

**Una convalida aggiunta alla cella C1** 

![todo:image_alt_text](write-gridweb-client-side-script_1.png)

Aggiungi un valore non valido e clicca su **Salva**. Si verifica un errore di convalida e viene eseguita la funzione ValidationErrorFunction.

**Funzione di convalida invocata in caso di errore di convalida** 

![todo:image_alt_text](write-gridweb-client-side-script_2.png)

Fino a quando non inserisci un valore valido, nessun dato viene inviato al server. Inserisci un valore valido e clicca su **Salva**. Viene eseguita la funzione ConfirmFunction.

**Funzione di conferma invocata prima dell'invio dei dati di GridWeb al server** 

![todo:image_alt_text](write-gridweb-client-side-script_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript-WriteClientSideScript.aspx" >}}

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript.aspx-WriteClientSideScript.cs" >}}
