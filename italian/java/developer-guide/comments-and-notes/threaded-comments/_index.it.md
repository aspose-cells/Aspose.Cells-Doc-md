---
title: Commenti in discussione
type: docs
weight: 140
url: /it/java/threaded-comments/
---
# **Commenti in discussione**
MS Excel 365 offre una funzionalità per aggiungere commenti in thread. Questi commenti funzionano come conversazioni e possono essere utilizzati per le discussioni. I commenti ora vengono forniti con una casella di risposta che consente conversazioni in thread. I vecchi commenti sono chiamati Note in Excel 365. Lo screenshot seguente mostra come vengono visualizzati i commenti in thread quando vengono aperti in Excel.

![cose da fare:immagine_alt_testo](threaded-comments_1.jpg)

commenti in thread vengono visualizzati in questo modo nelle versioni precedenti di Excel. Le seguenti immagini sono state scattate aprendo il file di esempio in Excel 2016.

![cose da fare:immagine_alt_testo](threaded-comments_2.jpg)



![cose da fare:immagine_alt_testo](threaded-comments_3.jpg)



Aspose.Cells fornisce anche la funzione per gestire i commenti in thread.
## **Aggiungi commenti in thread**
### **Aggiungi commento Threaded con Excel**
Per aggiungere commenti in thread in Excel 365, attenersi alla seguente procedura.

- Metodo 1
 - Clicca il**Revisione**Scheda
 - Clicca il**Nuovo commento**pulsante
 - Si aprirà una finestra di dialogo per inserire commenti nella cella attiva.
  - ![cose da fare:immagine_alt_testo](threaded-comments_4.jpg)
- Metodo 2
 - Fare clic con il tasto destro sulla cella in cui si desidera inserire il commento.
 - Clicca il**Nuovo commento**opzione.
 - Si aprirà una finestra di dialogo per inserire commenti nella cella attiva.
  - ![cose da fare:immagine_alt_testo](threaded-comments_5)
### **Aggiungi commento in thread usando Aspose.Cells**
Aspose.Cells fornisce[Commenti.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\)) metodo per aggiungere commenti in thread.The[Commenti.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\)) accetta i seguenti tre parametri.

- Cell Nome: il nome della cella in cui verrà inserito il commento.
- Testo commento: il testo del commento.
- [ThreadedCommentAutore](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentAuthor): L'autore del commento

L'esempio di codice seguente illustra l'utilizzo di[Commenti.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\)) metodo per aggiungere un commento in thread alla cella A1. Si prega di consultare il[file Excel di output](AddThreadedComments_out.xlsx)generato dal codice per riferimento.
#### **Codice di esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddThreadedComments-1.java" >}}
## **Leggi i commenti in thread**
### **Leggi i commenti in thread con Excel**
Per leggere i commenti in thread in Excel, passa semplicemente il mouse sopra la cella contenente i commenti per visualizzare i commenti. La vista dei commenti sarà simile alla vista nell'immagine seguente.

![cose da fare:immagine_alt_testo](threaded-comments_1.jpg)
### **Leggi i commenti in discussione usando Aspose.Cells**
Aspose.Cells fornisce[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) per recuperare i commenti in thread per la colonna specificata.[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) accetta il nome della colonna come parametro e restituisce il[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). Puoi iterare sul[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)per visualizzare i commenti.

L'esempio seguente illustra la lettura dei commenti dalla colonna A1 caricando il file[file Excel di esempio](ThreadedCommentsSample.xlsx). Si prega di consultare l'output della console generato dal codice per riferimento.
#### **Codice di esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedComments-1.java" >}}
#### **Uscita console**
Commento: prova il commento in thread

Autore: Aspose Prova
### **Leggi l'ora di creazione dei commenti in thread**
Aspose.Cells fornisce[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) per recuperare i commenti in thread per la colonna specificata.[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) accetta il nome della colonna come parametro e restituisce il[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). Puoi iterare sul[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)e usa il[ThreadedComment.CreatedTime](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcomment#CreatedTime)proprietà.

L'esempio seguente mostra la lettura dell'ora di creazione dei commenti in thread caricando il file[file Excel di esempio](ThreadedCommentsSample.xlsx). Si prega di consultare l'output della console generato dal codice per riferimento.
#### **Codice di esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedCommentCreatedTime-1.java" >}}
#### **Uscita console**
Commento: prova il commento in thread

Autore: Aspose Prova

Ora di creazione: 2019-05-15T12:46:23
## **Modifica commenti in thread**
### **Modifica commento filettato con Excel**
Per modificare un commento con thread in Excel, fare clic su**Modificare**link sul commento come mostrato nell'immagine seguente.

![cose da fare:immagine_alt_testo](threaded-comments_7.jpg)
### **Modifica il commento in discussione utilizzando Aspose.Cells**
Aspose.Cells fornisce[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) per recuperare i commenti in thread per la colonna specificata.[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) accetta il nome della colonna come parametro e restituisce il[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). È possibile aggiornare il commento richiesto nel file[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)e salva la cartella di lavoro.

L'esempio seguente mostra la modifica del primo commento con thread nella colonna A1 caricando il file[file Excel di esempio](ThreadedCommentsSample.xlsx). Si prega di consultare il[file Excel di output](EditThreadedComments.xlsx)generato dal codice che mostra il commento aggiornato per riferimento.
#### **Codice di esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "EditThreadedComments-1.java" >}}
## **Rimuovi commenti in thread**
### **Rimuovi i commenti in thread con Excel**
Per rimuovere i commenti in thread in Excel, fare clic con il pulsante destro del mouse sulla cella contenente i commenti e fare clic su**Elimina commento**opzione come mostrato nell'immagine seguente.

![cose da fare:immagine_alt_testo](threaded-comments_8.jpg)
### **Rimuovi i commenti in discussione usando Aspose.Cells**
Aspose.Cells fornisce[Commenti.RimuoviAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt\(int\)) per rimuovere i commenti per la colonna specificata.[Commenti.RimuoviAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt\(int\)) accetta il nome della colonna come parametro rimuove i commenti in quella colonna.

L'esempio seguente mostra la rimozione dei commenti nella colonna A1 caricando il file[file Excel di esempio](ThreadedCommentsSample.xlsx). Si prega di consultare il[file Excel di output](ThreadedCommentsSample_Out.xlsx)generato dal codice per riferimento.
#### **Codice di esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "RemoveThreadedComments-1.java" >}}

{{% alert color="primary" %}} 

 Si prega di notare che rimuovendo il commento con Aspose.Cells, l'autore non viene rimosso automaticamente. Se è necessario rimuovere anche l'autore, utilizzare il file[ThreadedCommentAuthorCollection.removeAt](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcommentauthorcollection#removeAt\(int\)) come mostrato nell'esempio precedente.

{{% /alert %}}
