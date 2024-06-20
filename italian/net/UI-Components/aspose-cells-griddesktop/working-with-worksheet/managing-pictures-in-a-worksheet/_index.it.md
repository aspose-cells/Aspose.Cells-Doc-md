---
title: Gestione delle Immagini in un Foglio di Lavoro
type: docs
weight: 100
url: /it/net/aspose-cells-griddesktop/manage-pictures-in-a-worksheet/
keywords: GridDesktop,immagine,immagini
description: Questo articolo introduce come lavorare con le immagini nel foglio di lavoro in GridDesktop.
---

{{% alert color="primary" %}} 

La maggior parte delle persone crede che un'immagine possa spiegare le cose meglio delle parole. Ecco perché Aspose.Cells.GridDesktop supporta l'aggiunta di immagini ai fogli di lavoro per mettere in pratica questa convinzione delle persone. In questo argomento, parleremo dell'aggiunta e della manipolazione di immagini nei fogli di lavoro.

{{% /alert %}} 
## **Aggiunta di immagini**
Per aggiungere un collegamento ipertestuale a una cella utilizzando Aspose.Cells.GridDesktop, seguire i passaggi seguenti:

- Aggiungi il controllo Aspose.Cells.GridDesktop al tuo **Form**
- Accedere a qualsiasi **Foglio di lavoro** desiderato
- Aggiungere **Immagine** al foglio di lavoro specificando il percorso del file dell'immagine e il nome della cella in cui sarà inserita l'immagine

La raccolta **Pictures** nell'oggetto **Worksheet** fornisce un metodo **Add** sovraccaricato. Gli sviluppatori possono utilizzare qualsiasi versione sovraccaricata del metodo **Add** in base alle loro esigenze specifiche. Utilizzando queste versioni sovraccaricate del metodo **Add**, è possibile aggiungere un'immagine da file, flusso o oggetto **Image**.

Di seguito è riportato il codice di esempio per aggiungere immagini nei fogli di lavoro.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AddingPictures.cs" >}}
## **Accesso alle immagini**
Per accedere e modificare un'immagine esistente nel foglio di lavoro, gli sviluppatori possono accedere all'immagine dalla raccolta **Pictures** del **Worksheet** specificando la cella (usando il nome della cella o la sua posizione in termini di numero di riga e colonna) in cui viene inserita l'immagine. Una volta accessata l'immagine, gli sviluppatori possono modificarne l'immagine durante l'esecuzione.

Di seguito è riportato il codice di esempio per accedere e modificare le immagini in un foglio di lavoro.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AccessAndModifyPicture.cs" >}}
## **Rimozione delle immagini**
Per rimuovere un'immagine esistente, gli sviluppatori possono semplicemente accedere a un foglio di lavoro desiderato e quindi rimuovere l'immagine dalla raccolta **Pictures** del **Worksheet** specificando la cella (usando il nome o il numero di riga e colonna) che contiene l'immagine.

Nel codice sottostante viene mostrato come rimuovere le immagini dal foglio di lavoro.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-RemovePicture.cs" >}}
