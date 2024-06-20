---
title: Commenti filettati
type: docs
weight: 140
url: /it/net/threaded-comments/
---

## **Commenti in discussione**

MS Excel 365 fornisce una funzionalità per aggiungere commenti filettati. Questi commenti funzionano come conversazioni e possono essere utilizzati per le discussioni. I commenti ora sono dotati di una casella Rispondi che consente conversazioni filettate. I vecchi commenti sono chiamati Note in Excel 365. La schermata qui sotto mostra come vengono visualizzati i commenti filettati quando aperti in Excel.

![todo:image_alt_text](threaded-comments_1.jpg)

I commenti filettati vengono mostrati in questo modo nelle versioni più vecchie di Excel. Le seguenti immagini sono state scattate aprendo il file di esempio in Excel 2016.

![todo:image_alt_text](threaded-comments_2.jpg)

![todo:image_alt_text](threaded-comments_3.jpg)

Aspose.Cells fornisce anche la funzionalità di gestire commenti in thread.

## **Aggiungi Commenti in Thread**

### **Aggiungi commento in thread con Excel**

Per aggiungere commenti in thread in Excel 365, seguire i seguenti passaggi.

- Metodo 1
  - Fare clic sulla scheda **Revisione**
  - Fare clic sul pulsante **Nuovo commento**
  - Si aprirà un dialogo per inserire commenti nella cella attiva.
  - ![todo:image_alt_text](threaded-comments_4.jpg)
- Metodo 2
  - Fare clic con il pulsante destro del mouse sulla cella in cui si desidera inserire il commento.
  - Fare clic sull'opzione **Nuovo commento**
  - Si aprirà un dialogo per inserire commenti nella cella attiva.
  - ![todo:image_alt_text](threaded-comments_5)

### **Aggiungi Commento in Thread utilizzando Aspose.Cells**

Aspose.Cells fornisce il metodo [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1) per aggiungere commenti in thread. Il metodo [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1) accetta i seguenti tre parametri.

- Nome della cella: Il nome della cella in cui verrà inserito il commento.
- Testo del commento: Il testo del commento.
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentauthor): L'autore del commento

Il seguente esempio di codice dimostra l'uso del metodo [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1) per aggiungere un Commento in Thread alla cella A1. Si prega di vedere il [file Excel di output](89849859.xlsx) generato dal codice per riferimento.

#### **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-AddThreadedComments-1.cs" >}}

## **Leggi Commenti in Thread**

### **Leggi commenti in thread con Excel**

Per leggere i commenti in Excel, passa semplicemente il mouse sopra la cella contenente i commenti per visualizzarli. La visualizzazione dei commenti assomiglierà alla vista dell'immagine seguente.

![todo:image_alt_text](threaded-comments_1.jpg)

### **Leggi i commenti con thread utilizzando Aspose.Cells**

Aspose.Cells fornisce il metodo [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) per recuperare i commenti con thread per la colonna specificata. Il metodo [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) accetta il nome della colonna come parametro e restituisce il [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). Puoi iterare sul [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) per visualizzare i commenti.

L'esempio seguente dimostra la lettura dei commenti dalla colonna A1 caricando il [file Excel di esempio](89849861.xlsx). Si prega di consultare l'output della console generato dal codice per riferimento.

#### **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadThreadedComments-1.cs" >}}

#### **Output della console**

{{< highlight csharp >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **Leggi l'ora della creazione dei commenti con thread**

Aspose.Cells fornisce il metodo [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) per recuperare i commenti con thread per la colonna specificata. Il metodo [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) accetta il nome della colonna come parametro e restituisce il [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). Puoi iterare su [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) e utilizzare la proprietà [**ThreadedComment.CreatedTime**](https://reference.aspose.com/cells/net/aspose.cells/threadedcomment/properties/createdtime).

L'esempio seguente dimostra la lettura dell'orario di creazione dei commenti con thread caricando il [file Excel di esempio](89849861.xlsx). Si prega di consultare l'output della console generato dal codice per riferimento.

#### **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadThreadedCommentCreatedTime-1.cs" >}}

#### **Output della console**

{{< highlight csharp >}}

Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 5/15/2019 12:46:23 PM

{{< /highlight >}}

## **Modifica i commenti con thread**

### **Modifica il commento con thread con Excel**

Per modificare un commento con thread in Excel, fare clic sul collegamento **Modifica** nel commento come mostrato nell'immagine seguente.

![todo:image_alt_text](threaded-comments_7.jpg)

### **Modifica il commento con thread utilizzando Aspose.Cells**

Aspose.Cells fornisce il metodo [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) per recuperare i commenti con thread per la colonna specificata. Il metodo [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) accetta il nome della colonna come parametro e restituisce il [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). Puoi aggiornare il commento richiesto su [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) e salvare il workbook.

L'esempio seguente dimostra la modifica del primo commento con thread nella colonna A1 caricando il [file Excel di esempio](89849861.xlsx). Si prega di consultare il [file Excel di output](89849862.xlsx) generato dal codice che mostra il commento aggiornato per riferimento.

#### **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-EditThreadedComments-1.cs" >}}

## **Rimuovi i commenti con thread**

### **Rimuovi i commenti con thread con Excel**

Per rimuovere i commenti con thread in Excel, fai clic con il pulsante destro del mouse sulla cella contenente i commenti e seleziona l'opzione **Elimina commento** come mostrato nell'immagine seguente.

![todo:image_alt_text](threaded-comments_8.jpg)

### **Rimuovi i commenti con thread utilizzando Aspose.Cells**

Aspose.Cells fornisce il metodo [**Comments.RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/removeat/index) per rimuovere i commenti per la colonna specificata. Il metodo [**Comments.RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/removeat/index) accetta il nome della colonna come parametro e rimuove i commenti in quella colonna.

L'esempio seguente dimostra la rimozione dei commenti nella colonna A1 caricando il [file Excel di esempio](89849861.xlsx). Si prega di consultare il [file Excel di output](89849864.xlsx) generato dal codice per riferimento.

#### **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-RemoveThreadedComments-1.cs" >}}

{{% alert color="primary" %}}

Si noti che rimuovendo un commento con Aspose.Cells, l'autore non viene automaticamente rimosso. Se è necessario rimuovere anche l'autore, utilizzare il metodo RemoveAt della classe [**ThreadedCommentAuthorCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentauthorcollection) come mostrato nell'esempio sopra.

{{% /alert %}}
