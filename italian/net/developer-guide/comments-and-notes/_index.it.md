---
title: Gestione dei commenti e delle note
linktitle: Commenti e note
type: docs
weight: 128
url: /it/net/comments-and-notes/
description: Inserire e gestire commenti o note con Aspose.Cells per .Net.
keywords: Inserire commenti, inserire note
---

## **Introduzione**

I commenti vengono utilizzati per aggiungere informazioni aggiuntive alle celle. Aspose.Cells fornisce due metodi per aggiungere commenti alle celle. Il primo è creare commenti manualmente in un file di progettazione. Successivamente, questi commenti vengono importati utilizzando Aspose.Cells. Il secondo è aggiungere commenti utilizzando l'API di Aspose.Cells in fase di esecuzione. Questo argomento tratta l'aggiunta di commenti alle celle utilizzando l'API di Aspose.Cells. Verrà inoltre spiegato come formattare i commenti.

## **Aggiungere un commento**

Aggiungi un commento a una cella chiamando il metodo [**Add**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/add/index) della raccolta [**Comments**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection) (incapsulato nell'oggetto [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)). Il nuovo oggetto [**Comment**](https://reference.aspose.com/cells/net/aspose.cells/comment) può essere accessibile dalla raccolta [**Comments**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection) passando l'indice del commento. Dopo aver accesso all'oggetto [**Comment**](https://reference.aspose.com/cells/net/aspose.cells/comment), personalizza la nota del commento utilizzando la proprietà [**Note**](https://reference.aspose.com/cells/net/aspose.cells/comment/properties/note) dell'oggetto [**Comment**](https://reference.aspose.com/cells/net/aspose.cells/comment).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-AddingComment-1.cs" >}}

## **Formattazione del commento**

È anche possibile formattare l'aspetto dei commenti configurando la loro altezza, larghezza e impostazioni del carattere.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-CommentFormatting-1.cs" >}}

## **Aggiungi un'immagine al commento**

Con Microsoft Excel 2007, è anche possibile avere un'immagine come sfondo di un commento di cella. In Excel 2007 questo si realizza seguendo i seguenti passaggi. (Si suppone che tu abbia già aggiunto un commento alla cella.)

1. Fare clic con il pulsante destro del mouse sulla cella che contiene il commento.
1. Selezionare **Mostra/Nascondi commenti**, e cancellare eventuali testi dal commento.
1. Fare clic sul bordo del commento per selezionarlo.
1. Selezionare **Formato**, quindi **Commento**.
1. Nella scheda **Colori e linee**, espandere l'elenco **Colore**.
1. Fare clic su **Effetti di riempimento**.
1. Nella scheda **Immagine**, fare clic su **Seleziona immagine**.
1. Trovare e selezionare l'immagine.
1. Fare clic su **OK** finché tutte le finestre di dialogo non si sono chiuse.

Aspose.Cells fornisce anche questa funzionalità. Di seguito è riportato un esempio di codice che crea un file XLSX da zero, aggiungendo un commento alla cella "A1" con un'immagine impostata come sfondo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-AddImageToComment-1.cs" >}}

## **Argomenti avanzati**
- [Cambia la Direzione del Testo del Commento](/cells/it/net/change-text-direction-of-the-comment/)
- [Come cambiare il Colore del Testo del Commento](/cells/it/net/how-to-change-the-comment-font-color/)
- [Come impostare lo sfondo del commento](/cells/it/net/how-to-set-comment-background/)
- [Commenti in discussione](/cells/it/net/threaded-comments/)

