---  
title: Commenti annidati con Node.js tramite C++  
linktitle: Commenti filettati  
type: docs  
weight: 140  
url: /it/nodejs-cpp/threaded-comments/  
description: Gestisci commenti annidati nei documenti Excel usando Aspose.Cells for Node.js via C++. Impara ad aggiungere, leggere, modificare e rimuovere commenti annidati.  
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

Aspose.Cells fornisce il metodo [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) per aggiungere commenti annidati. Il metodo [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) accetta i seguenti tre parametri.  

- Nome della cella: Il nome della cella in cui verrà inserito il commento.  
- Testo del commento: Il testo del commento.  
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentauthor): L'autore del commento  

Il seguente esempio di codice dimostra l’uso del metodo [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) per aggiungere un commento annidato alla cella A1. Consulta il [file Excel di output](89849859.xlsx) generato dal codice come riferimento.  

#### **Codice di Esempio**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const outDir = path.join(__dirname, "output");

const workbook = new AsposeCells.Workbook();

// Add Author
const authorIndex = workbook.getWorksheets().getThreadedCommentAuthors().add("Aspose Test", "", "");
const author = workbook.getWorksheets().getThreadedCommentAuthors().get(authorIndex);

// Add Threaded Comment
workbook.getWorksheets().get(0).getComments().addThreadedComment("A1", "Test Threaded Comment", author);

workbook.save(outDir + "AddThreadedComments_out.xlsx");
```  

## **Leggi Commenti in Thread**  

### **Leggi commenti in thread con Excel**  

Per leggere i commenti in Excel, passa semplicemente il mouse sopra la cella contenente i commenti per visualizzarli. La visualizzazione dei commenti assomiglierà alla vista dell'immagine seguente.  

![todo:image_alt_text](threaded-comments_1.jpg)  

### **Leggi i commenti con thread utilizzando Aspose.Cells**  

Aspose.Cells fornisce il metodo [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) per recuperare i commenti con thread per la colonna specificata. Il metodo [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) accetta il nome della colonna come parametro e restituisce il [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection). Puoi iterare sul [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection) per visualizzare i commenti.  

L'esempio seguente dimostra la lettura dei commenti dalla colonna A1 caricando il [file Excel di esempio](89849861.xlsx). Si prega di consultare l'output della console generato dal codice per riferimento.  

#### **Codice di Esempio**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data"); // Adjust as necessary

const filePath = path.join(sourceDir, "ThreadedCommentsSample.xlsx");

// Loads the workbook which contains threaded comments
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get Threaded Comments
const threadedComments = worksheet.getComments().getThreadedComments("A1");

const count = threadedComments.getCount();
for (let i = 0; i < count; i++) {
const comment = threadedComments.get(i);
console.log("Comment: " + comment.getNotes());
console.log("Author: " + comment.getAuthor().getName());
}
```  

#### **Output della console**  

{{< highlight javascript >}}  

Comment: Test Threaded Comment  

Author: Aspose Test  

{{< /highlight >}}  

### **Leggi l'ora della creazione dei commenti con thread**  

Aspose.Cells fornisce il metodo [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) per recuperare i commenti annidati della colonna specificata. Il metodo [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) accetta il nome della colonna come parametro e restituisce il [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection). Puoi iterare sul [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection) e usare la proprietà [**ThreadedComment.getCreatedTime()**](https://reference.aspose.com/cells/nodejs-cpp/threadedcomment/#getCreatedTime--).  

L'esempio seguente dimostra la lettura dell'orario di creazione dei commenti con thread caricando il [file Excel di esempio](89849861.xlsx). Si prega di consultare l'output della console generato dal codice per riferimento.  

#### **Codice di Esempio**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const filePath = path.join(sourceDir, "ThreadedCommentsSample.xlsx");

// Loads the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get Threaded Comments
const threadedComments = worksheet.getComments().getThreadedComments("A1");

const count = threadedComments.getCount();

for (let i = 0; i < count; i++) {
const comment = threadedComments.get(i);
console.log("Comment: " + comment.getNotes());
console.log("Author: " + comment.getAuthor().getName());
console.log("Created Time: " + comment.getCreatedTime());
}
```  

#### **Output della console**  

{{< highlight javascript >}}  

Comment: Test Threaded Comment  

Author: Aspose Test  

Created Time: 5/15/2019 12:46:23 PM  

{{< /highlight >}}  

## **Modifica i commenti con thread**  

### **Modifica il commento con thread con Excel**  

Per modificare un commento con thread in Excel, fare clic sul collegamento **Modifica** nel commento come mostrato nell'immagine seguente.  

![todo:image_alt_text](threaded-comments_7.jpg)  

### **Modifica il commento con thread utilizzando Aspose.Cells**  

Aspose.Cells fornisce il metodo [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) per recuperare i commenti annidati della colonna specificata. Il metodo [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) accetta il nome della colonna come parametro e restituisce il [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection). Puoi aggiornare il commento necessario nel [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection) e salvare il workbook.  

L'esempio seguente dimostra la modifica del primo commento con thread nella colonna A1 caricando il [file Excel di esempio](89849861.xlsx). Si prega di consultare il [file Excel di output](89849862.xlsx) generato dal codice che mostra il commento aggiornato per riferimento.  

#### **Codice di Esempio**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source and output directories
const sourceDir = path.join(__dirname, "data");
const outDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "ThreadedCommentsSample.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get Threaded Comment
const comment = worksheet.getComments().getThreadedComments("A1").get(0);
comment.setNotes("Updated Comment");

workbook.save(outDir + "EditThreadedComments.xlsx");
```  

## **Rimuovi i commenti con thread**  

### **Rimuovi i commenti con thread con Excel**  

Per rimuovere i commenti con thread in Excel, fai clic con il pulsante destro del mouse sulla cella contenente i commenti e seleziona l'opzione **Elimina commento** come mostrato nell'immagine seguente.  

![todo:image_alt_text](threaded-comments_8.jpg)   


{{< app/cells/assistant language="nodejs-cpp" >}}
