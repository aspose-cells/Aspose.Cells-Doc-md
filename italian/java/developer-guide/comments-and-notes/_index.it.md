---
title: Gestisci commenti e note
linktitle: Commenti e Note
type: docs
weight: 128
url: /it/java/comments-and-notes/
description: Inserisci e gestisci commenti o note con Aspose.Cells per java.
keywords: insert comments, insert notes
---
## **introduzione**

commenti vengono utilizzati per aggiungere ulteriori informazioni alle celle. Aspose.Cells fornisce due metodi per aggiungere commenti alle celle. Il primo consiste nel creare manualmente i commenti in un file di progettazione. Questi commenti vengono quindi importati utilizzando Aspose.Cells. Il secondo consiste nell'aggiungere commenti utilizzando l'API Aspose.Cells in fase di esecuzione. Questo argomento illustra l'aggiunta di commenti alle celle utilizzando l'API Aspose.Cells. Verranno spiegati anche i commenti di formattazione.

## **Aggiunta di un commento**

 Aggiungi un commento a una cella chiamando il metodo[**Commenti**](https://reference.aspose.com/cells/java/com.aspose.cells/CommentCollection) della collezione**Aggiungere** metodo (incapsulato nel file[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) oggetto). Il nuovo[**Commento**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) è possibile accedere all'oggetto da[**Commenti**](https://reference.aspose.com/cells/java/com.aspose.cells/CommentCollection) raccolta passando l'indice dei commenti. Dopo aver effettuato l'accesso al[**Commento**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) oggetto, personalizzare la nota di commento utilizzando il[**Commento**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) dell'oggetto[**Nota**](https://reference.aspose.com/cells/java/com.aspose.cells/comment#Note)proprietà.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddingComment-1.java" >}}

## **Formattazione dei commenti**

È anche possibile formattare l'aspetto dei commenti configurandone l'altezza, la larghezza e le impostazioni del carattere.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "CommentFormatting-1.java" >}}

## **Aggiungi un'immagine al commento**

Con Microsoft Excel 2007, è anche possibile avere un'immagine come sfondo di un commento di cella. In Excel 2007 ciò si ottiene eseguendo i seguenti passaggi. (Suppongono che tu abbia già aggiunto un commento di cella.)

1. Fare clic con il pulsante destro del mouse sulla cella che contiene il commento.
1.  Selezionare**Mostra/Nascondi commenti**e cancella qualsiasi testo dal commento.
1. Fare clic sul bordo del commento per selezionarlo.
1.  Selezionare**Formato** , poi**Commento**.
1.  Sul**Colori e Linee** scheda, espandere il file**Colore** elenco.
1.  Clic**Effetti di riempimento**.
1.  Sul**Immagine** scheda, fare clic**Seleziona Immagine**.
1. Individua e seleziona l'immagine.
1.  Clic**OK** fino alla chiusura di tutte le finestre di dialogo.

Aspose.Cells fornisce anche questa funzione. Di seguito è riportato un esempio di codice che crea un file XLSX da zero, aggiungendo un commento alla cella "A1" con un'immagine impostata come sfondo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddImageToComment-1.java" >}}

## **Argomenti avanzati**
- [Cambia la direzione del testo del commento](/cells/it/java/change-text-direction-of-the-comment/)
- [Come modificare il colore del carattere del commento](/cells/it/java/how-to-change-the-comment-font-color/)
- [Come impostare lo sfondo dei commenti](/cells/it/java/how-to-set-comment-background/)
- [Commenti in discussione](/cells/it/java/threaded-comments/)

