---
title: Scrivere lo script lato client GridWeb
type: docs
weight: 10
url: /it/net/write-gridweb-client-side-script/
---
{{% alert color="primary" %}} 

Gli sviluppatori possono scrivere script sul lato client per il controllo Aspose.Cells.GridWeb. Ciò significa che è possibile richiamare una funzione JavaScript lato client per eseguire un'attività specifica correlata al controllo GridWeb. Ad esempio, gli sviluppatori possono scrivere funzioni JavaScript per inviare dati GridWeb a un server o mostrare un messaggio di avviso quando si verifica un errore di convalida, ecc.

Questo argomento spiega questa funzione con l'aiuto di esempi.

{{% /alert %}} 
## **Scrittura di script lato client per Aspose.Cells.GridWeb**
### **Informazioni di base**
Aspose.Cells.GridWeb fornisce due proprietà create appositamente per supportare gli script lato client:

- OnSubmitClientFunction
- OnValidationErrorClientFunction

Creare funzioni JavaScript in una pagina ASPX e assegnare i nomi di queste funzioni alle proprietà OnSubmitClientFunction e OnValidationErrorClientFunction.

{{% alert color="primary" %}} 

La funzione JavaScript che verrà assegnata alla proprietà OnSubmitClientFunction deve essere definita correttamente come mostrato di seguito:

**javascript**

{{< highlight "csharp" >}}

 function function_name(arg, cancelEdit)

 {

   //Add javascript code here

 }



{{< /highlight >}}

dove il parametro [arg] rappresenta il comando generato dal controllo. Il comando può essere "Salva", "Invia", "Annulla" ecc. e il parametro [cancelEdit] è un valore booleano, che indica se l'input dell'utente è stato annullato o meno.

Qualsiasi funzione JavaScript assegnata alla proprietà OnSubmitClientFunction viene chiamata ogni volta dal controllo GridWeb prima di inviare i dati GridWeb a un server. Analogamente, se una funzione viene assegnata alla proprietà OnValidationErrorClientFunction, tale funzione verrà richiamata ogni volta che si verifica un errore di convalida.

{{% /alert %}} 
### **Funzioni per lo scripting lato client**
Aspose.Cells.GridWeb espone anche funzioni specialmente per lo scripting lato client. Queste funzioni possono essere utilizzate all'interno delle funzioni JavaScript per ottenere un maggiore controllo di Aspose.Cells.GridWeb. Queste funzioni lato client includono quanto segue:

|**Funzioni**|**Descrizione**|
|:- |:- |
|updateData(bool cancelModifica)|Aggiorna tutti i dati client di Aspose.Cells.GridWeb prima di inviarli al server. Se il parametro cancelEdit è vero, GridWeb elimina tutti gli input dell'utente.|
|convalidaTutto()|Utilizzato per verificare se sono presenti errori di convalida nell'input dell'utente. Se c'è un errore, la funzione restituisce false, altrimenti true .|
|submit(string arg, bool cancelModifica)|Chiamare questa funzione per eseguire il postback o inviare i dati al server. Questa funzione esegue entrambe le attività, ovvero l'aggiornamento dei dati e la convalida dell'input dell'utente. Questa funzione può anche attivare un evento di comando sul lato server. Usa il parametro arg per passare il tuo comando. Ad esempio: il comando SALVA viene utilizzato per fare clic su**Salva** pulsante sulla barra dei comandi del controllo GridWeb e il comando CCMD:MYCOMMAND genera un evento CustomCommand.|
|setCellaAttiva(int riga, int colonna)|Utilizzato per attivare una cella specifica.|
|setCellValue(int riga, int colonna, valore stringa)|Utilizzato per inserire un valore in qualsiasi cella specificata utilizzando i relativi numeri di riga e colonna.|
|getCellValue(int riga, int colonna)|Restituisce il valore di qualsiasi cella specificata.|
|getActiveRow()|Utilizzato insieme alla funzione getActiveColumn() per determinare la posizione di una cella attiva.|
|getActiveColumn()|Utilizzato insieme alla funzione getActiveRow() per determinare la posizione di una cella attiva.|
|getSelectRange()|Restituisce l'ultimo intervallo selezionato.|
|setSelectRange()|Seleziona l'intervallo specificato.|
|cancellaSelezioni()|Cancella tutta la selezione esclusa la cella attiva corrente.|
|getCellsArray()| Viene utilizzato con altre funzioni correlate come getCellName(), getCellValueByCell(), getCellRow() e getCellColumn(). Si prega di leggere questo articolo per ulteriori informazioni sull'utilizzo di questa funzione:[Leggere i valori delle celle GridWeb sul lato client](/cells/it/net/read-the-values-of-the-gridweb-cells-on-client-side/)|
Per creare un'applicazione di test contenente script lato client che funzionano con Aspose.Cells.GridWeb, attenersi alla seguente procedura:

1. Crea funzioni JavaScript che devono essere richiamate da GridWeb.
 Queste funzioni verranno aggiunte alle pagine ASP.NET<script></script>etichetta.
1. Assegnare i nomi delle funzioni alle proprietà OnSubmitClientFunction e OnValidationErrorClientFunction.

L'output dell'esempio di codice è mostrato di seguito:

**Una convalida aggiunta alla cella C1** 

![cose da fare:immagine_alt_testo](write-gridweb-client-side-script_1.png)

 Aggiungi un valore non valido e fai clic**Salva**. Si verifica un errore di convalida e viene eseguita la ValidationErrorFunction.

**ValidationErrorFunction richiamato in caso di errore di convalida** 

![cose da fare:immagine_alt_testo](write-gridweb-client-side-script_2.png)

 Finché non si immette un valore valido, nessun dato viene inviato al server. Immettere un valore valido e fare clic**Salva**. Viene eseguita la funzione Confirm.

**ConfirmFunction richiamato prima di inviare i dati GridWeb al server** 

![cose da fare:immagine_alt_testo](write-gridweb-client-side-script_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript-WriteClientSideScript.aspx" >}}

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript.aspx-WriteClientSideScript.cs" >}}
