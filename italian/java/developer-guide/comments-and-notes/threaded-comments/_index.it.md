---
title: Commenti filettati
type: docs
weight: 140
url: /it/java/threaded-comments/
---

# **Commenti in discussione**
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
  - Fare clic sul pulsante **Nuovo commento**
  - Si aprirà un dialogo per inserire commenti nella cella attiva.
  - ![todo:image_alt_text](threaded-comments_4.jpg)
- Metodo 2
  - Fare clic con il pulsante destro del mouse sulla cella in cui si desidera inserire il commento.
  - Fare clic sull'opzione **Nuovo commento**.
  - Si aprirà un dialogo per inserire commenti nella cella attiva.
  - ![todo:image_alt_text](threaded-comments_5)
### **Aggiungi Commento in Thread utilizzando Aspose.Cells**
Aspose.Cells fornisce il metodo [Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment-java.lang.String-java.lang.String-com.aspose.cells.ThreadedCommentAuthor-) per aggiungere commenti a thread. Il metodo [Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment-java.lang.String-java.lang.String-com.aspose.cells.ThreadedCommentAuthor-) accetta i seguenti tre parametri.

- Nome della cella: Il nome della cella in cui verrà inserito il commento.
- Testo del commento: Il testo del commento.
- [ThreadedCommentAuthor](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentAuthor): L'autore del commento

Il campione di codice seguente dimostra l'utilizzo del metodo [Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment-java.lang.String-java.lang.String-com.aspose.cells.ThreadedCommentAuthor-) per aggiungere un commento con thread alla cella A1. Si prega di consultare il file Excel di output ([AddThreadedComments_out.xlsx](AddThreadedComments_out.xlsx)) generato dal codice come riferimento.
#### **Codice di Esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddThreadedComments-1.java" >}}
## **Leggi Commenti in Thread**
### **Leggi commenti in thread con Excel**
Per leggere i commenti in Excel, passa semplicemente il mouse sopra la cella contenente i commenti per visualizzarli. La visualizzazione dei commenti assomiglierà alla vista dell'immagine seguente.

![todo:image_alt_text](threaded-comments_1.jpg)
### **Leggi i commenti con thread utilizzando Aspose.Cells**
Aspose.Cells offre il metodo [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) per recuperare i commenti con thread per la colonna specificata. Il metodo [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) accetta come parametro il nome della colonna e restituisce l'oggetto [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). È possibile iterare su di esso per visualizzare i commenti.

L'esempio seguente illustra la lettura dei commenti dalla colonna A1 caricando il [file Excel di esempio](ThreadedCommentsSample.xlsx). Si prega di consultare l'output della console generato dal codice per riferimento.
#### **Codice di Esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedComments-1.java" >}}
#### **Output della console**

{{< highlight java >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **Leggi l'ora della creazione dei commenti con thread**
Aspose.Cells offre il metodo [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) per recuperare i commenti con thread per la colonna specificata. Il metodo accetta come parametro il nome della colonna e restituisce l'oggetto [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). È possibile iterare su di esso e utilizzare la proprietà [ThreadedComment.CreatedTime](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcomment#CreatedTime).

L'esempio seguente illustra la lettura dell'orario di creazione dei commenti in filo caricando il [file Excel di esempio](ThreadedCommentsSample.xlsx). Si prega di consultare l'output della console generato dal codice per riferimento.
#### **Codice di Esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedCommentCreatedTime-1.java" >}}
#### **Output della console**

{{< highlight java >}}

Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 2019-05-15T12:46:23

{{< /highlight >}}

## **Modifica i commenti con thread**
### **Modifica il commento con thread con Excel**
Per modificare un commento a thread in Excel, fare clic sul collegamento **Modifica** sul commento come mostrato nell'immagine seguente.

![todo:image_alt_text](threaded-comments_7.jpg)
### **Modifica il commento con thread utilizzando Aspose.Cells**
Aspose.Cells offre il metodo [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) per recuperare i commenti con thread per la colonna specificata. Il metodo accetta come parametro il nome della colonna e restituisce l'oggetto [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). Puoi aggiornare il commento necessario in questa collezione e salvare il workbook.

L'esempio seguente illustra la modifica del primo commento in thread nella colonna A1 caricando il [file Excel di esempio](ThreadedCommentsSample.xlsx). Si prega di consultare il [file Excel di output](EditThreadedComments.xlsx) generato dal codice che mostra il commento aggiornato per riferimento.
#### **Codice di Esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "EditThreadedComments-1.java" >}}
## **Rimuovi i commenti con thread**
### **Rimuovi i commenti con thread con Excel**
Per rimuovere commenti in thread in Excel, fare clic con il pulsante destro del mouse sulla cella che contiene i commenti e fare clic sull'opzione **Elimina commento** come mostrato nell'immagine seguente.

![todo:image_alt_text](threaded-comments_8.jpg)
### **Rimuovi i commenti con thread utilizzando Aspose.Cells**
Aspose.Cells offre il metodo [Comments.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt-int-) per rimuovere i commenti dalla colonna specificata. Il metodo [Comments.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt-int-) accetta come parametro il nome della colonna e rimuove i commenti in essa presenti. 

L'esempio seguente illustra la rimozione dei commenti nella colonna A1 caricando il [file Excel di esempio](ThreadedCommentsSample.xlsx). Si prega di consultare il [file Excel di output](ThreadedCommentsSample_Out.xlsx) generato dal codice per riferimento.
#### **Codice di Esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "RemoveThreadedComments-1.java" >}}

{{% alert color="primary" %}} 

Si noti che rimuovendo un commento con Aspose.Cells, l'autore non viene rimosso automaticamente. Se si desidera rimuovere anche l'autore, utilizzare il metodo [ThreadedCommentAuthorCollection.removeAt](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcommentauthorcollection#removeAt-int-) come mostrato nell'esempio sopra.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
