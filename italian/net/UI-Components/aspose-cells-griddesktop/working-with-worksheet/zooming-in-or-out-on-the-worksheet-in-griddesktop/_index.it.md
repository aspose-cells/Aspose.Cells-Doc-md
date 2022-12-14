---
title: Zoom avanti o indietro sul foglio di lavoro in GridDesktop
type: docs
weight: 160
url: /it/net/zooming-in-or-out-on-the-worksheet-in-griddesktop/
---
{{% alert color="primary" %}} 

A volte, quando lavori con i tuoi dati, potresti voler ingrandire i contenuti sullo schermo senza modificare effettivamente la dimensione del carattere. Ad esempio, potresti aver formattato il tuo testo in modo che utilizzi un carattere piccolo. (Questo è spesso necessario per ottenere tutte le informazioni su una stampa.) Quando si lavora nel foglio di lavoro, tuttavia, il carattere è difficile da leggere perché è così piccolo.

In Microsoft Excel, è disponibile un dispositivo di scorrimento dello zoom per ingrandire e ridurre i documenti in modo rapido e semplice. Il dispositivo di scorrimento dello zoom si trova solitamente nell'angolo in basso a destra della finestra del software.

Aspose.Cells consente inoltre agli sviluppatori di impostare il fattore di zoom del foglio di lavoro, quindi i contenuti dovrebbero apparire secondo il valore percentuale desiderato.

{{% /alert %}} 
## **Zoom avanti o indietro utilizzando Aspose.Cells.GridDesktop**
Aspose.Cells fornisce la classe Aspose.Cells.GridDesktop.Worksheet che dispone di un'ampia gamma di proprietà e metodi per la gestione dei fogli di lavoro. Per impostare il fattore di zoom di un foglio di lavoro, utilizzare la proprietà Zoom della classe Worksheet. Il fattore di zoom viene impostato assegnando un valore numerico (intero) alla proprietà Zoom.

Costruiamo un dispositivo di scorrimento dello zoom simile a MS Excel utilizzando il controllo TrackBar (.NET). In un progetto WinForm, inseriamo il controllo Aspose.Cells.GridDesktop da Toolbox nel form e specifichiamo alcune proprietà per impostarne il nome, la dimensione o altri aspetti di conseguenza. Ora posizioniamo il controllo TrackBar nell'angolo in basso a destra sotto il controllo GridDesktop, inseriamo anche un controllo Label che mostra il valore percentuale specificato tramite l'handle del controllo TrackBar. Aggiungiamo righe di codice relative nell'evento Scroll di TrackBar, quindi quando scorri il controllo Trackbar, GridDesktop dovrebbe ingrandire o ridurre per mostrare i dati/contenuti al suo interno.

Di seguito viene fornito un esempio completo che mostra come utilizzare la proprietà Zoom per impostare il fattore di zoom del foglio di lavoro attivo di GridDesktop. Per prima cosa importiamo un file Excel modello in GridDesktop.

Scrivere sotto il codice nell'evento Load del modulo per impostare il file Excel del modello in GridDesktop e il valore della trackbar.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-LoadEvent.cs" >}}


Ora copia sotto il codice all'interno dell'evento di scorrimento della traccia ed esegui l'applicazione. Noterai che lo spostamento della barra della traccia cambierà la proprietà dello zoom del foglio di lavoro.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-ZoomInOut.cs" >}}
