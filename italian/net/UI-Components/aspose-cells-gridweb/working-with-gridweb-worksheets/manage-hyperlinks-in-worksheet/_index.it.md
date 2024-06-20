---
title: Gestione degli Hyperlink nel foglio di lavoro
type: docs
weight: 100
url: /it/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/
keywords: GridWeb, hyperlink
description: Questo articolo introduce come lavorare con il collegamento ipertestuale in GridWeb.
---

{{% alert color="primary" %}} 

Questo argomento discute quali tipi di collegamenti ipertestuali sono supportati in Aspose.Cells.GridWeb e come gestirli programmaticamente. I collegamenti ipertestuali possono essere utilizzati sia per creare collegamenti a URL web sia per eseguire un postback a un server.

{{% /alert %}} 
## **Lavorare con Collegamenti Ipotestuali**
### **Tipi di Collegamenti Ipotestuali**
Generalmente, i seguenti collegamenti ipertestuali sono supportati da Aspose.Cells.GridWeb:

- [Collegamenti ipertestuali URL](/cells/it/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/), collegamenti ipertestuali che possono essere collegati a URL web.
- [Collegamenti ipertestuali di testo](/cells/it/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/), collegamenti ipertestuali URL applicati al testo.
- [Collegamenti ipertestuali di immagini](/cells/it/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/), collegamenti ipertestuali URL applicati alle immagini.
- [Collegamenti ipertestuali di comando celle](/cells/it/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/), collegamenti ipertestuali che inviano dati a un server. Tali collegamenti ipertestuali agiscono più come un pulsante che attiva un evento lato server quando viene cliccato.

Le sezioni seguenti descrivono l'uso di tutti i tipi di collegamenti ipertestuali in dettaglio. Si discute anche come accedere o rimuovere i collegamenti.
### **Aggiunta di Collegamenti Ipotestuali**

#### **Collegamenti Ipotestuali URL**
I collegamenti ipertestuali URL assomigliano più a semplici collegamenti ipertestuali che normalmente si vedono sui siti web. Un collegamento ipertestuale URL funziona come un'ancla in una cella. Ogni volta che viene cliccato, naviga su una pagina web o apre una nuova finestra del browser.

Ci sono diversi tipi di collegamenti ipertestuali URL:

- Collegamenti ipertestuali di testo.
- Collegamenti ipertestuali di immagini.

Gli sviluppatori possono specificare un'immagine per il collegamento ipertestuale. Se un'immagine non è specificata, viene creato un collegamento ipertestuale di testo; altrimenti, viene creato un collegamento ipertestuale di immagine.


##### **Collegamenti Ipotestuali di Testo**
Per aggiungere un collegamento ipertestuale di testo a un foglio di lavoro:

1. Aggiungi il controllo Aspose.Cells.GridWeb al tuo modulo web.
1. Accedi a un foglio di lavoro.
1. Aggiungi un collegamento ipertestuale a una cella nel foglio di lavoro.
1. Imposta il testo che verrà mostrato nella cella.
1. Imposta l'URL del collegamento ipertestuale.
1. Imposta il target del collegamento ipertestuale, se desiderato.
1. Imposta un suggerimento per lo strumento, se desiderato.

{{% alert color="primary" %}} 

NOTA: Il target del collegamento ipertestuale può essere impostato su _self, _top o _parent per aprire gli URL web in una nuova finestra, la finestra corrente o la finestra superiore rispettivamente.

{{% /alert %}} 

Nell'esempio sottostante vengono aggiunti due collegamenti ipertestuali a un foglio di lavoro. Uno non ha alcun target, mentre l'altro è impostato su _parent.

**Output: collegamenti ipertestuali di testo aggiunti al foglio di lavoro** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddTextHyperlinks.cs" >}}


##### **Collegamenti ipertestuali delle immagini**
Per aggiungere un collegamento ipertestuale all'immagine:

1. Aggiungi il controllo Aspose.Cells.GridWeb al tuo modulo web.
1. Accedi a un foglio di lavoro.
1. Aggiungi un collegamento ipertestuale a una cella.
1. Imposta l'URL dell'immagine che verrà visualizzata come collegamento ipertestuale.
1. Imposta l'URL del collegamento ipertestuale.
1. Imposta un suggerimento per lo strumento, se desiderato.
1. Imposta il testo del collegamento ipertestuale, se desiderato.

**Output: collegamenti ipertestuali delle immagini aggiunti al foglio di lavoro** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_2.png)

{{% alert color="primary" %}} 

Setting the image hyperlink's AltText fills a similar function as setting an <ALT> tag in HTML. The text is displayed only if the hyperlinked image is not displayed. (For example, if the image isn't at the specified location.) If the image of the second hyperlink is not found, the output of the code snippet below would look as follows.

**Non è stato possibile trovare l'immagine per l'URL dell'immagine** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_3.png)

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddImageHyperlinks.cs" >}}


#### **Collegamenti ipertestuali delle celle di comando**
Un collegamento ipertestuale di comando della cella è un tipo speciale di collegamento ipertestuale che attiva un evento lato server invece di aprire una pagina web. Gli sviluppatori possono aggiungere codice all'evento lato server e eseguire qualsiasi attività quando il collegamento ipertestuale viene cliccato. Questa funzionalità consente agli sviluppatori di creare applicazioni più interattive.

Per aggiungere un collegamento ipertestuale di comando della cella:

1. Aggiungi il controllo Aspose.Cells.GridWeb al tuo modulo web.
1. Accedi a un foglio di lavoro.
1. Aggiungi un collegamento ipertestuale a una cella.
1. Imposta il comando del collegamento ipertestuale su un valore desiderato.
   Il valore è utilizzato dall'handler dell'evento del collegamento ipertestuale per riconoscerlo.
1. Imposta un suggerimento per lo strumento, se desiderato.
1. Imposta l'URL per l'immagine che verrà visualizzata come collegamento ipertestuale.

**Un collegamento ipertestuale di comando della cella è stato aggiunto al foglio di lavoro** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddCellCommandHyperlinks.cs" >}}
##### **Gestione degli eventi dei collegamenti ipertestuali di comando cella**
Gli sviluppatori devono creare un gestore eventi per l'evento CellCommand del controllo GridWeb per eseguire compiti specifici quando viene cliccato un collegamento ipertestuale di comando della cella specifica. Il gestore eventi di CellCommand fornisce un oggetto del tipo CellEventArgs che offre la proprietà Argument. Utilizza la proprietà Argument per identificare un collegamento ipertestuale specifico confrontando il suo valore di CellCommand.

L'esempio sottostante crea un gestore eventi per il collegamento ipertestuale di comando della cella creato nel codice sopra. Il CellCommand del collegamento ipertestuale è stato impostato su Click. Quindi, nell'handler dell'evento, controlla prima di aggiungere il codice che visualizza un messaggio nella cella A6.

Il gestore eventi viene invocato quando il collegamento ipertestuale viene cliccato.

**Output: testo aggiunto alla cella A6 quando viene cliccato il collegamento ipertestuale** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_5.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-HandleCellCommandHyperlinkEvent.cs" >}}
### **Accesso ai collegamenti ipertestuali**
Per accedere a un collegamento ipertestuale esistente:

1. Accedi alla cella che lo contiene.
1. Ottieni il riferimento della cella.
1. Passa il riferimento al metodo GetHyperlink della collezione Hyperlinks per accedere al collegamento ipertestuale.
1. Modifica le proprietà del collegamento ipertestuale.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-AccessHyperlinks.cs" >}}
### **Rimozione dei collegamenti ipertestuali**
Per rimuovere un collegamento ipertestuale:

1. Accedi alla scheda attiva.
1. Rimuovi un collegamento ipertestuale utilizzando il metodo Rimuovi della raccolta Collegamenti ipertestuali.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-RemoveHyperlink.cs" >}}
