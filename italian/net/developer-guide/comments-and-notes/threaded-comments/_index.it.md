---
title: Commenti in discussione
type: docs
weight: 140
url: /it/net/threaded-comments/
---
## **Commenti in discussione**

MS Excel 365 offre una funzionalità per aggiungere commenti in thread. Questi commenti funzionano come conversazioni e possono essere utilizzati per le discussioni. I commenti ora vengono forniti con una casella di risposta che consente conversazioni in thread. I vecchi commenti sono chiamati Note in Excel 365. Lo screenshot seguente mostra come vengono visualizzati i commenti in thread quando vengono aperti in Excel.

![cose da fare:immagine_alt_testo](threaded-comments_1.jpg)

I commenti in thread vengono visualizzati in questo modo nelle versioni precedenti di Excel. Le seguenti immagini sono state scattate aprendo il file di esempio in Excel 2016.

![cose da fare:immagine_alt_testo](threaded-comments_2.jpg)

![cose da fare:immagine_alt_testo](threaded-comments_3.jpg)

Aspose.Cells fornisce anche la funzione per gestire i commenti in thread.

## **Aggiungi commenti in thread**

### **Aggiungi commento Threaded con Excel**

Per aggiungere commenti in thread in Excel 365, attenersi alla seguente procedura.

- Metodo 1
 - Clicca il**Revisione** Scheda
 - Clicca il**Nuovo commento** pulsante
 - Si aprirà una finestra di dialogo per inserire commenti nella cella attiva.
  - ![cose da fare:immagine_alt_testo](threaded-comments_4.jpg)
- Metodo 2
 - Fare clic con il tasto destro sulla cella in cui si desidera inserire il commento.
 - Clicca il**Nuovo commento** opzione.
 - Si aprirà una finestra di dialogo per inserire commenti nella cella attiva.
  - ![cose da fare:immagine_alt_testo](threaded-comments_5)

### **Aggiungi commento in thread usando Aspose.Cells**

Aspose.Cells fornisce[**Commenti.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1) metodo per aggiungere commenti in thread.The[**Commenti.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1)Il metodo accetta i seguenti tre parametri.

- Cell Nome: il nome della cella in cui verrà inserito il commento.
- Testo commento: il testo del commento.
- [**ThreadedCommentAutore**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentauthor): L'autore del commento

L'esempio di codice seguente illustra l'utilizzo di[**Commenti.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1)metodo per aggiungere un commento in thread alla cella A1. Si prega di consultare il[file Excel di output](89849859.xlsx) generato dal codice per riferimento.

#### **Codice d'esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-AddThreadedComments-1.cs" >}}

## **Leggi i commenti in thread**

### **Leggi i commenti in thread con Excel**

Per leggere i commenti in thread in Excel, passa semplicemente il mouse sopra la cella contenente i commenti per visualizzare i commenti. La vista dei commenti sarà simile alla vista nell'immagine seguente.

![cose da fare:immagine_alt_testo](threaded-comments_1.jpg)

### **Leggi i commenti in discussione usando Aspose.Cells**

Aspose.Cells fornisce[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)metodo per recuperare i commenti in thread per la colonna specificata.[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)Il metodo accetta il nome della colonna come parametro e restituisce il[**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). Puoi iterare sul[**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection)per visualizzare i commenti.

L'esempio seguente illustra la lettura dei commenti dalla colonna A1 caricando il file[file Excel di esempio](89849861.xlsx). Si prega di consultare l'output della console generato dal codice per riferimento.

#### **Codice d'esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadThreadedComments-1.cs" >}}

#### **Uscita console**

Commento: prova il commento in thread

Autore: Aspose Prova

### **Leggi l'ora di creazione dei commenti in thread**

Aspose.Cells fornisce[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)metodo per recuperare i commenti in thread per la colonna specificata.[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)Il metodo accetta il nome della colonna come parametro e restituisce il[**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). Puoi iterare sul[**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) e usa il[**ThreadedComment.CreatedTime**](https://reference.aspose.com/cells/net/aspose.cells/threadedcomment/properties/createdtime) proprietà.

L'esempio seguente mostra la lettura dell'ora di creazione dei commenti in thread caricando il file[file Excel di esempio](89849861.xlsx). Si prega di consultare l'output della console generato dal codice per riferimento.

#### **Codice d'esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadThreadedCommentCreatedTime-1.cs" >}}

#### **Uscita console**

Commento: prova il commento in thread

Autore: Aspose Prova

Ora di creazione: 15/05/2019 12:46:23

## **Modifica commenti in thread**

### **Modifica commento filettato con Excel**

 Per modificare un commento con thread in Excel, fare clic su**Modificare** link sul commento come mostrato nell'immagine seguente.

![cose da fare:immagine_alt_testo](threaded-comments_7.jpg)

### **Modifica il commento in discussione utilizzando Aspose.Cells**

Aspose.Cells fornisce[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) metodo per recuperare i commenti in thread per la colonna specificata.[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)Il metodo accetta il nome della colonna come parametro e restituisce il[**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). È possibile aggiornare il commento richiesto nel file[**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection)e salva la cartella di lavoro.

L'esempio seguente mostra la modifica del primo commento con thread nella colonna A1 caricando il file[file Excel di esempio](89849861.xlsx). Si prega di consultare il[file Excel di output](89849862.xlsx)generato dal codice che mostra il commento aggiornato per riferimento.

#### **Codice d'esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-EditThreadedComments-1.cs" >}}

## **Rimuovi commenti in thread**

### **Rimuovi i commenti in thread con Excel**

 Per rimuovere i commenti in thread in Excel, fare clic con il pulsante destro del mouse sulla cella contenente i commenti e fare clic su**Elimina commento** opzione come mostrato nell'immagine seguente.

![cose da fare:immagine_alt_testo](threaded-comments_8.jpg)

### **Rimuovi i commenti in discussione usando Aspose.Cells**

Aspose.Cells fornisce[**Commenti.RimuoviAt**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/removeat/index)metodo per rimuovere i commenti per la colonna specificata.[**Commenti.RimuoviAt**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/removeat/index)Il metodo accetta il nome della colonna come parametro rimuove i commenti in quella colonna.

L'esempio seguente mostra la rimozione dei commenti nella colonna A1 caricando il file[file Excel di esempio](89849861.xlsx). Si prega di consultare il[file Excel di output](89849864.xlsx)generato dal codice per riferimento.

#### **Codice d'esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-RemoveThreadedComments-1.cs" >}}

{{% alert color="primary" %}}

 Si prega di notare che rimuovendo il commento con Aspose.Cells, l'autore non viene rimosso automaticamente. Se è necessario rimuovere anche l'autore, utilizzare il metodo RemoveAt di[**ThreadedCommentAuthorCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentauthorcollection) classe come mostrato nell'esempio precedente.

{{% /alert %}}
