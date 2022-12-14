---
title: Crea pulsanti di comando personalizzati
type: docs
weight: 100
url: /it/net/create-custom-command-buttons/
---
{{% alert color="primary" %}} 

 Aspose.Cells.GridWeb contiene pulsanti speciali come**Invia**, **Salva** e**Annullare**. Tutti questi pulsanti eseguono attività specifiche per Aspose.Cells.GridWeb.
È anche possibile aggiungere pulsanti personalizzati che eseguono attività personalizzate. Questo argomento spiega come utilizzare questa funzione.

{{% /alert %}} 
## **Creazione di pulsanti di comando personalizzati**
Per creare un pulsante di comando personalizzato in Aspose.Cells.GridWeb:

1. Aggiungere il controllo Aspose.Cells.GridWeb al modulo Web.
1. Accedi a un foglio di lavoro.
1. Creare un'istanza della classe CustomCommandButton.
1. Imposta il comando del pulsante su un valore. Questo valore viene utilizzato nel gestore eventi del pulsante.
1. Imposta il testo del pulsante.
1. Imposta l'URL dell'immagine del pulsante.
1. Infine, aggiungi l'oggetto CustomCommandButton alla raccolta CustomCommandButtons del controllo GridWeb.

{{% alert color="primary" %}} 

I pulsanti di comando personalizzati possono anche essere aggiunti in modalità WYSIWYG utilizzando la finestra di dialogo Proprietà di Visual Studio.

{{% /alert %}} 

L'output del frammento di codice è mostrato di seguito:

**Un pulsante di comando personalizzato aggiunto al controllo GridWeb** 

![cose da fare:immagine_alt_testo](create-custom-command-buttons_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitCustomCommandButton.aspx-InitCustomCommandButton.cs" >}}
### **Gestione degli eventi del pulsante di comando personalizzato**
L'aspetto più importante dei pulsanti di comando personalizzati è l'azione che eseguono quando vengono cliccati. Per impostare l'azione, creare un gestore eventi per l'evento CustomCommand del controllo GridWeb.

L'evento CustomCommand viene sempre attivato quando si fa clic su un pulsante di comando personalizzato. Pertanto, il gestore dell'evento deve identificare il pulsante di comando personalizzato specifico a cui si applica dal set di comandi quando aggiunge il pulsante al controllo GridWeb. Infine, aggiungi il codice personalizzato che viene eseguito quando si fa clic sul pulsante.

Nell'esempio di codice seguente, un messaggio di testo viene aggiunto alla cella A1 quando si fa clic sul pulsante.

**Testo aggiunto alla cella A1 quando si fa clic sul pulsante di comando personalizzato** 

![cose da fare:immagine_alt_testo](create-custom-command-buttons_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleCustomCommandEvent.aspx-HandleCustomCommandEvent.cs" >}}
