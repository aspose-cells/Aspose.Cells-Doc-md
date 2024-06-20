---
title: Creare Pulsanti di Comando Personalizzati
type: docs
weight: 100
url: /it/net/aspose-cells-gridweb/create-custom-command-buttons/
keywords: GridWeb, comando, pulsanti di comando, personalizzato
description: Questo articolo introduce come personalizzare i pulsanti di comando in GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb contiene pulsanti speciali come **Invia**, **Salva** e **Annulla**. Tutti questi pulsanti svolgono compiti specifici per Aspose.Cells.GridWeb.
E' inoltre possibile aggiungere pulsanti personalizzati che svolgono compiti personalizzati. Questo argomento spiega come utilizzare questa funzionalità.

{{% /alert %}} 
## **Creazione di pulsanti di comando personalizzati**
Per creare un pulsante di comando personalizzato in Aspose.Cells.GridWeb:

1. Aggiungi il controllo Aspose.Cells.GridWeb al modulo web.
1. Accedi a un foglio di lavoro.
1. Crea un'istanza della classe CustomCommandButton.
1. Imposta il comando del pulsante su un certo valore. Questo valore viene utilizzato nell'handler dell'evento del pulsante.
1. Imposta il testo del pulsante.
1. Imposta l'URL dell'immagine del pulsante.
1. Infine, aggiungi l'oggetto CustomCommandButton alla collezione CustomCommandButtons del controllo GridWeb.

{{% alert color="primary" %}} 

I pulsanti di comando personalizzati possono anche essere aggiunti in modalità WYSIWYG utilizzando il dialog delle Proprietà di Visual Studio.

{{% /alert %}} 

Di seguito viene mostrato l'output del frammento di codice:

**Un pulsante di comando personalizzato aggiunto al controllo GridWeb** 

![todo:image_alt_text](create-custom-command-buttons_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitCustomCommandButton.aspx-InitCustomCommandButton.cs" >}}
### **Gestione degli eventi del pulsante di comando personalizzato**
L'aspetto più importante dei pulsanti di comando personalizzati è l'azione che compiono quando vengono cliccati. Per impostare l'azione, crea un handler dell'evento per l'evento CustomCommand del controllo GridWeb.

L'evento CustomCommand viene sempre attivato quando viene cliccato un pulsante di comando personalizzato. Quindi l'handler dell'evento deve identificare il pulsante di comando personalizzato specifico a cui si applica tramite il Command impostato durante l'aggiunta del pulsante al controllo GridWeb. Infine, aggiungi del codice personalizzato che viene eseguito quando il pulsante viene cliccato.

Nell'esempio di codice sottostante, viene aggiunto un messaggio di testo alla cella A1 quando il pulsante viene cliccato.

**Testo aggiunto alla cella A1 quando viene cliccato il pulsante di comando personalizzato** 

![todo:image_alt_text](create-custom-command-buttons_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleCustomCommandEvent.aspx-HandleCustomCommandEvent.cs" >}}
