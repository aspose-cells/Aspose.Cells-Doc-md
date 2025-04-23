---
title: Gestione dei commenti e delle note
linktitle: Commenti e note
type: docs
weight: 128
url: /it/java/comments-and-notes/
description: Inserisci e gestisci commenti o note con Aspose.Cells for java
keywords: Inserire commenti, inserire note
---

## **Introduzione**

I commenti vengono utilizzati per aggiungere informazioni aggiuntive alle celle. Aspose.Cells fornisce due metodi per aggiungere commenti alle celle. Il primo è creare commenti manualmente in un file di progettazione. Successivamente, questi commenti vengono importati utilizzando Aspose.Cells. Il secondo è aggiungere commenti utilizzando l'API di Aspose.Cells in fase di esecuzione. Questo argomento tratta l'aggiunta di commenti alle celle utilizzando l'API di Aspose.Cells. Verrà inoltre spiegato come formattare i commenti.

## **Aggiungere un commento**

Aggiungi un commento a una cella chiamando il metodo **Aggiungi** della collezione [**Comments**](https://reference.aspose.com/cells/java/com.aspose.cells/CommentCollection) (incapsulato nell'oggetto [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)). Il nuovo oggetto [**Comment**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) può essere acceduto dalla collezione [**Comments**](https://reference.aspose.com/cells/java/com.aspose.cells/CommentCollection) passando l'indice del commento. Dopo aver acceduto all'oggetto [**Comment**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment), personalizza la nota del commento utilizzando la proprietà [**Note**](https://reference.aspose.com/cells/java/com.aspose.cells/comment#Note) dell'oggetto [**Comment**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddingComment-1.java" >}}

## **Formattazione del commento**

È anche possibile formattare l'aspetto dei commenti configurando la loro altezza, larghezza e impostazioni del carattere.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "CommentFormatting-1.java" >}}

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

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddImageToComment-1.java" >}}

## **Argomenti avanzati**
- [Cambia la Direzione del Testo del Commento](/cells/it/java/change-text-direction-of-the-comment/)
- [Come cambiare il Colore del Testo del Commento](/cells/it/java/how-to-change-the-comment-font-color/)
- [Come impostare lo sfondo del commento](/cells/it/java/how-to-set-comment-background/)
- [Commenti in discussione](/cells/it/java/threaded-comments/)

{{< app/cells/assistant language="java" >}}
