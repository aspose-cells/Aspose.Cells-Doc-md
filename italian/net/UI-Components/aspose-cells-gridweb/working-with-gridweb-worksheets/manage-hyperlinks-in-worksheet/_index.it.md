---
title: Gestisci i collegamenti ipertestuali nel foglio di lavoro
type: docs
weight: 100
url: /it/net/manage-hyperlinks-in-worksheet/
---
{{% alert color="primary" %}} 

Questo argomento illustra quali tipi di collegamenti ipertestuali sono supportati in Aspose.Cells.GridWeb e come gestirli a livello di codice. I collegamenti ipertestuali possono essere utilizzati per creare collegamenti a URL Web o per eseguire il postback su un server.

{{% /alert %}} 
## **Lavorare con i collegamenti ipertestuali**
### **Tipi di collegamenti ipertestuali**
Generalmente, i seguenti collegamenti ipertestuali sono supportati da Aspose.Cells.GridWeb:

- [Collegamenti ipertestuali dell'URL](/cells/it/net/manage-hyperlinks-in-worksheet/), collegamenti ipertestuali che possono essere collegati a URL Web.
- [Collegamenti ipertestuali di testo](/cells/it/net/manage-hyperlinks-in-worksheet/), collegamenti ipertestuali URL applicati al testo.
- [Collegamenti ipertestuali delle immagini](/cells/it/net/manage-hyperlinks-in-worksheet/), collegamenti ipertestuali URL applicati alle immagini.
- [Cell collegamenti ipertestuali di comando](/cells/it/net/manage-hyperlinks-in-worksheet/), collegamenti ipertestuali che inviano dati a un server. Tali collegamenti ipertestuali agiscono più come un pulsante che attiva un evento lato server quando viene cliccato.

Le sezioni seguenti descrivono in dettaglio l'uso di tutti i tipi di collegamenti ipertestuali. Discute anche su come accedere o rimuovere i link.
### **Aggiunta di collegamenti ipertestuali**

#### **Collegamenti ipertestuali dell'URL**
I collegamenti ipertestuali URL assomigliano più a semplici collegamenti ipertestuali che si vedono normalmente sui siti web. Un collegamento ipertestuale URL funziona come un'ancora in una cella. Ogni volta che viene cliccato, naviga verso una pagina web o apre una nuova finestra del browser.

Esistono diversi tipi di collegamenti ipertestuali URL:

- Collegamenti ipertestuali di testo.
- Collegamenti ipertestuali delle immagini.

Gli sviluppatori possono specificare un'immagine per il collegamento ipertestuale. Se non viene specificata un'immagine, viene creato un collegamento ipertestuale di testo; altrimenti viene creato un collegamento ipertestuale immagine.


##### **Collegamenti ipertestuali di testo**
Per aggiungere un collegamento ipertestuale di testo a un foglio di lavoro:

1. Aggiungere il controllo Aspose.Cells.GridWeb al Web Form.
1. Accedi a un foglio di lavoro.
1. Aggiungere un collegamento ipertestuale a una cella nel foglio di lavoro.
1. Imposta il testo che verrà mostrato nella cella.
1. Imposta l'URL del collegamento ipertestuale.
1. Impostare la destinazione del collegamento ipertestuale, se lo si desidera.
1. Impostare una descrizione comandi, se lo si desidera.

{{% alert color="primary" %}} 

 NOTA: la destinazione del collegamento ipertestuale può essere impostata su_ se stesso,_top o _parent per aprire rispettivamente gli URL web in una finestra nuova, corrente o in alto.

{{% /alert %}} 

L'esempio seguente aggiunge due collegamenti ipertestuali a un foglio di lavoro. Uno non ha target mentre l'altro è impostato su _parent.

**Output: collegamenti ipertestuali di testo aggiunti al foglio di lavoro** 

![cose da fare:immagine_alt_testo](manage-hyperlinks-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddTextHyperlinks.cs" >}}


##### **Collegamenti ipertestuali delle immagini**
Per aggiungere un collegamento ipertestuale all'immagine:

1. Aggiungere il controllo Aspose.Cells.GridWeb al Web Form.
1. Accedi a un foglio di lavoro.
1. Aggiungere un collegamento ipertestuale a una cella.
1. Imposta l'URL dell'immagine che verrà visualizzata come collegamento ipertestuale.
1. Imposta l'URL del collegamento ipertestuale.
1. Impostare una descrizione comandi, se lo si desidera.
1. Impostare il testo del collegamento ipertestuale, se lo si desidera.

**Output: collegamenti ipertestuali immagine aggiunti al foglio di lavoro** 

![cose da fare:immagine_alt_testo](manage-hyperlinks-in-worksheet_2.png)

{{% alert color="primary" %}} 

 L'impostazione dell'AltText del collegamento ipertestuale dell'immagine svolge una funzione simile all'impostazione di an<ALT> tag in HTML. Il testo viene visualizzato solo se l'immagine con collegamento ipertestuale non viene visualizzata. (Ad esempio, se l'immagine non si trova nella posizione specificata.) Se l'immagine del secondo collegamento ipertestuale non viene trovata, l'output del frammento di codice seguente avrà il seguente aspetto.

**Impossibile trovare l'immagine per l'URL dell'immagine** 

![cose da fare:immagine_alt_testo](manage-hyperlinks-in-worksheet_3.png)

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddImageHyperlinks.cs" >}}


#### **Cell Comando Collegamenti ipertestuali**
Un collegamento ipertestuale di comando cella è un tipo speciale di collegamento ipertestuale che attiva un evento sul lato server invece di aprire una pagina Web. Gli sviluppatori possono aggiungere codice all'evento lato server ed eseguire qualsiasi attività quando si fa clic sul collegamento ipertestuale. Questa funzione consente agli sviluppatori di creare più applicazioni interattive.

Per aggiungere un collegamento ipertestuale al comando di cella:

1. Aggiungere il controllo Aspose.Cells.GridWeb al Web Form.
1. Accedi a un foglio di lavoro.
1. Aggiungere un collegamento ipertestuale a una cella.
1. Impostare il comando del collegamento ipertestuale su qualsiasi valore desiderato.
 Il valore viene utilizzato dal gestore dell'evento del collegamento ipertestuale per riconoscerlo.
1. Impostare una descrizione comandi, se lo si desidera.
1. Imposta l'URL per l'immagine che verrà visualizzata come collegamento ipertestuale.

**Un collegamento ipertestuale di comando cella è stato aggiunto al foglio di lavoro** 

![cose da fare:immagine_alt_testo](manage-hyperlinks-in-worksheet_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddCellCommandHyperlinks.cs" >}}
##### **Gestione degli eventi dei collegamenti ipertestuali di comando Cell**
Gli sviluppatori devono creare un gestore eventi per l'evento CellCommand del controllo GridWeb per eseguire attività specifiche quando si fa clic su un collegamento ipertestuale di comando cella specifico. Il gestore dell'evento dell'evento CellCommand fornisce un oggetto del tipo CellEventArgs che offre la proprietà Argument. Utilizzare la proprietà Argument per identificare un collegamento ipertestuale specifico confrontandone il valore CellCommand.

L'esempio seguente crea un gestore eventi per il collegamento ipertestuale del comando cella creato nel codice precedente. Il CellCommand del collegamento ipertestuale è stato impostato su Click. Quindi, nel gestore dell'evento, prima controllalo e poi aggiungi il codice che visualizza un messaggio nella cella A6.

Il gestore dell'evento viene richiamato quando si fa clic sul collegamento ipertestuale.

**Output: testo aggiunto alla cella A6 quando si fa clic sul collegamento ipertestuale** 

![cose da fare:immagine_alt_testo](manage-hyperlinks-in-worksheet_5.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-HandleCellCommandHyperlinkEvent.cs" >}}
### **Accesso ai collegamenti ipertestuali**
Per accedere a un collegamento ipertestuale esistente:

1. Accedi alla cella che lo contiene.
1. Ottieni il riferimento di cella.
1. Passare il riferimento al metodo GetHyperlink della raccolta Hyperlinks per accedere al collegamento ipertestuale.
1. Modifica le proprietà del collegamento ipertestuale.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-AccessHyperlinks.cs" >}}
### **Rimozione di collegamenti ipertestuali**
Per rimuovere un collegamento ipertestuale:

1. Accedi al foglio di lavoro attivo.
1. Rimuovere un collegamento ipertestuale utilizzando il metodo Remove della raccolta Hyperlinks.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-RemoveHyperlink.cs" >}}
