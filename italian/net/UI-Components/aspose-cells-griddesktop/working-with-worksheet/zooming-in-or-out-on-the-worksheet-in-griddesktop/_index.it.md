---
title: Ingrandire o ridurre la visualizzazione del foglio di lavoro in GridDesktop
type: docs
weight: 160
url: /it/net/aspose-cells-griddesktop/zoom-in-or-out-on-the-worksheet-in-griddesktop/
keywords: GridDesktop, zoom, ingrandire, ridurre
description: Questo articolo illustra come ingrandire o ridurre la visualizzazione in GridDesktop.
---

{{% alert color="primary" %}} 

A volte, quando si lavora con i tuoi dati, potresti voler ingrandire i contenuti sullo schermo senza cambiare effettivamente la dimensione del carattere. Ad esempio, potresti aver formattato il testo in modo che utilizzi un carattere piccolo. (Questo è spesso necessario per ottenere tutte le informazioni su una stampa.) Tuttavia, quando si lavora nel foglio di lavoro, il carattere è difficile da leggere perché è troppo piccolo.

In Microsoft Excel, è disponibile un cursore zoom per ingrandire e ridurre rapidamente e facilmente i documenti. Il cursore zoom è di solito nell'angolo in basso a destra della finestra del software.

Aspose.Cells consente anche agli sviluppatori di impostare il fattore di zoom del foglio di lavoro, affinché i contenuti appaiano come desiderato.

{{% /alert %}} 
## **Ingrandire o ridurre utilizzando Aspose.Cells.GridDesktop**
Aspose.Cells fornisce la classe Aspose.Cells.GridDesktop.Worksheet che ha una vasta gamma di proprietà e metodi per la gestione dei fogli di lavoro. Per impostare il fattore di zoom di un foglio di lavoro, utilizzare la proprietà Zoom della classe Worksheet. Il fattore di zoom viene impostato assegnando un valore numerico (int) alla proprietà Zoom.

Costruiamo un cursore di zoom simile a quello di MS Excel utilizzando il controllo TrackBar (.NET). In un progetto WinForm, posizioniamo il controllo Aspose.Cells.GridDesktop dalla Toolbox al modulo e specificare alcune proprietà per impostarne il nome, dimensioni o altri aspetti di conseguenza. Ora, posizioniamo il controllo TrackBar nell'angolo in basso a destra sotto il controllo GridDesktop, mettiamo anche un controllo Label che mostrerà il valore in percentuale specificato tramite l'impugnatura del controllo TrackBar. Aggiungiamo righe relative di codice nel evento Scroll del TrackBar, quindi quando si scorre il controllo TrackBar, GridDesktop dovrebbe ingrandire o ridurre per mostrare i dati/ contenuti in esso.

Viene fornito un esempio completo qui sotto che dimostra come utilizzare la proprietà Zoom per impostare il fattore di zoom del foglio di lavoro attivo di GridDesktop. Prima importiamo un file Excel di modello in GridDesktop.

Scrivi il codice sottostante nell'evento Load del modulo per impostare il file Excel di modello in GridDesktop e il valore del cursore.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-LoadEvent.cs" >}}


Ora copia il codice sottostante nell'evento di scorrimento del cursore e avvia l'applicazione. Noterai che spostando il cursore del track bar cambierà la proprietà di zoom del foglio di lavoro.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-ZoomInOut.cs" >}}
