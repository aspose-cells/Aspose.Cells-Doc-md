---
title: Commenti filettati
type: docs
weight: 140
url: /it/python-net/threaded-comments/
---

## **Commenti in discussione**

MS Excel 365 fornisce una funzionalità per aggiungere commenti filettati. Questi commenti funzionano come conversazioni e possono essere utilizzati per le discussioni. I commenti ora sono dotati di una casella Rispondi che consente conversazioni filettate. I vecchi commenti sono chiamati Note in Excel 365. La schermata qui sotto mostra come vengono visualizzati i commenti filettati quando aperti in Excel.

![todo:image_alt_text](threaded-comments_1.jpg)

I commenti filettati vengono mostrati in questo modo nelle versioni più vecchie di Excel. Le seguenti immagini sono state scattate aprendo il file di esempio in Excel 2016.

![todo:image_alt_text](threaded-comments_2.jpg)

![todo:image_alt_text](threaded-comments_3.jpg)

Aspose.Cells per Python via .NET offre anche la possibilità di gestire commenti a thread.

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

### **Aggiungi commento a thread usando Aspose.Cells per Python via .NET**

Aspose.Cells per Python via .NET fornisce il metodo [**Comments.add_threaded_comment**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add_threaded_comment/) per aggiungere commenti a thread. Il metodo [**Comments.add_threaded_comment**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add_threaded_comment) accetta i seguenti tre parametri.

- Nome della cella: Il nome della cella in cui verrà inserito il commento.
- Testo del commento: Il testo del commento.
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentauthor): L'autore del commento

Il seguente esempio di codice dimostra l'uso del metodo [**Comments.add_threaded_comment**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add_threaded_comment) per aggiungere un Commento in Thread alla cella A1. Si prega di vedere il [file Excel di output](89849859.xlsx) generato dal codice per riferimento.

#### **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-AddThreadedComments-1.py" >}}

## **Leggi Commenti in Thread**

### **Leggi commenti in thread con Excel**

Per leggere i commenti in Excel, passa semplicemente il mouse sopra la cella contenente i commenti per visualizzarli. La visualizzazione dei commenti assomiglierà alla vista dell'immagine seguente.

![todo:image_alt_text](threaded-comments_1.jpg)

### **Leggi commenti a thread usando Aspose.Cells per Python via .NET**

Aspose.Cells per Python via .NET fornisce il metodo [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) per recuperare commenti a thread per la colonna specificata. Il metodo [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) accetta il nome della colonna come parametro e restituisce il [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection). È possibile iterare su [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection) per visualizzare i commenti.

L'esempio seguente dimostra la lettura dei commenti dalla colonna A1 caricando il [file Excel di esempio](89849861.xlsx). Si prega di consultare l'output della console generato dal codice per riferimento.

#### **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-ReadThreadedComments-1.py" >}}

#### **Output della console**

{{< highlight csharp >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **Leggi l'ora della creazione dei commenti con thread**

Aspose.Cells per Python via .NET fornisce il metodo [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) per recuperare commenti a thread per la colonna specificata. Il metodo [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) accetta il nome della colonna come parametro e restituisce il [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection). È possibile iterare su [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection) e usare la proprietà [**ThreadedComment.created_time**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcomment/created_time).

L'esempio seguente dimostra la lettura dell'orario di creazione dei commenti con thread caricando il [file Excel di esempio](89849861.xlsx). Si prega di consultare l'output della console generato dal codice per riferimento.

#### **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-ReadThreadedCommentCreatedTime-1.py" >}}

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

### **Modifica commento a thread usando Aspose.Cells per Python via .NET**

Aspose.Cells per Python via .NET fornisce il metodo [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) per recuperare commenti a thread per la colonna specificata. Il metodo [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) accetta il nome della colonna come parametro e restituisce il [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection). È possibile aggiornare il commento richiesto in [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection) e salvare il workbook.

L'esempio seguente dimostra la modifica del primo commento con thread nella colonna A1 caricando il [file Excel di esempio](89849861.xlsx). Si prega di consultare il [file Excel di output](89849862.xlsx) generato dal codice che mostra il commento aggiornato per riferimento.

#### **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-EditThreadedComments-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
