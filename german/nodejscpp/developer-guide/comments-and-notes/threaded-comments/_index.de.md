---  
title: Threaded Comments mit Node.js über C++  
linktitle: Threaded Comments  
type: docs  
weight: 140  
url: /de/nodejs-cpp/threaded-comments/  
description: Verwalten Sie threadspezifische Kommentare in Excel Dokumenten mit Aspose.Cells for Node.js via C++. Lernen Sie, thread spezifische Kommentare hinzuzufügen, zu lesen, zu bearbeiten und zu entfernen.  
---  

## **Antwortkommentare**  

MS Excel 365 bietet eine Funktion zum Hinzufügen von Threaded-Kommentaren. Diese Kommentare fungieren als Unterhaltungen und können für Diskussionen verwendet werden. Die Kommentare enthalten nun eine Antwortbox, die Threaded-Konversationen ermöglicht. Die alten Kommentare werden in Excel 365 als Notizen bezeichnet. Der Screenshot unten zeigt, wie threaded Kommentare angezeigt werden, wenn sie in Excel geöffnet werden.  

![todo:image_alt_text](threaded-comments_1.jpg)  

Threaded comments werden in älteren Versionen von Excel so angezeigt. Die folgenden Bilder wurden erstellt, indem die Beispieldatei in Excel 2016 geöffnet wurde.  

![todo:image_alt_text](threaded-comments_2.jpg)  

![todo:image_alt_text](threaded-comments_3.jpg)  

Aspose.Cells bietet auch die Funktion zur Verwaltung von Threaded-Kommentaren.  

## **Threaded-Kommentare hinzufügen**  

### **Threaded-Kommentar mit Excel hinzufügen**  

Um Threaded-Kommentare in Excel 365 hinzuzufügen, befolgen Sie die folgenden Schritte.  

- Methode 1  
  - Klicken Sie auf die Registerkarte **Überprüfen**  
  - Klicken Sie auf die Schaltfläche **Neuer Kommentar**  
  - Dadurch wird ein Dialogfeld geöffnet, um Kommentare in der aktiven Zelle einzugeben.  
  - ![todo:image_alt_text](threaded-comments_4.jpg)  
- Methode 2  
  - Klicken Sie mit der rechten Maustaste auf die Zelle, in die Sie den Kommentar einfügen möchten.  
  - Klicken Sie auf die Option **Neuer Kommentar**.  
  - Dadurch wird ein Dialogfeld geöffnet, um Kommentare in der aktiven Zelle einzugeben.  
  - ![todo:image_alt_text](threaded-comments_5)  

### **Fügen Sie einen Kommentarfaden mit Aspose.Cells hinzu**  

Aspose.Cells bietet die Methode [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-), um threaded comments hinzuzufügen. Die Methode [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) akzeptiert die folgenden drei Parameter.  

- Zellenname: Der Name der Zelle, in die der Kommentar eingefügt wird.  
- Kommentartext: Der Text des Kommentars.  
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentauthor): Der Verfasser des Kommentars  

Das folgende Codebeispiel zeigt die Verwendung der Methode [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-), um einen thread-spezifischen Kommentar in Zelle A1 hinzuzufügen. Bitte beachten Sie die [Ausgabedatei](89849859.xlsx), die durch den Code erstellt wird, zur Referenz.  

#### **Beispielcode**  

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

## **Lese kommentierte Fäden**  

### **Lese kommentierte Fäden mit Excel**  

Um kommentierte Fäden in Excel zu lesen, fahren Sie einfach mit der Maus über die Zelle, die Kommentare enthält, um die Kommentare anzuzeigen. Die Ansicht der Kommentare wird der Darstellung im folgenden Bild ähneln.  

![todo:image_alt_text](threaded-comments_1.jpg)  

### **Lese kommentierte Fäden mit Aspose.Cells**  

Aspose.Cells bietet die Methode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) zum Abrufen von kommentierten Fäden für die angegebene Spalte. Die Methode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) akzeptiert den Spaltennamen als Parameter und gibt die [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection) zurück. Sie können über die [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection) iterieren, um die Kommentare anzuzeigen.  

Das folgende Beispiel zeigt das Lesen von Kommentaren aus Spalte A1 durch Laden der [Beispiel-Excel-Datei](89849861.xlsx). Bitte sehen Sie die durch den Code generierte Konsolenausgabe zur Referenz an.  

#### **Beispielcode**  

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

#### **Konsolenausgabe**  

{{< highlight javascript >}}  

Comment: Test Threaded Comment  

Author: Aspose Test  

{{< /highlight >}}  

### **Lese Erstellungszeitpunkt von kommentierten Fäden**  

Aspose.Cells bietet die Methode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-), um thread-spezifische Kommentare für die angegebene Spalte abzurufen. Die Methode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) akzeptiert den Spaltennamen als Parameter und gibt die [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection) zurück. Sie können die [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection) durchlaufen und die [**ThreadedComment.getCreatedTime()**](https://reference.aspose.com/cells/nodejs-cpp/threadedcomment/#getCreatedTime--)-Eigenschaft verwenden.  

Das folgende Beispiel zeigt das Lesen des Erstellungszeitpunkts von kommentierten Fäden durch Laden der [Beispiel-Excel-Datei](89849861.xlsx). Bitte sehen Sie die durch den Code generierte Konsolenausgabe zur Referenz an.  

#### **Beispielcode**  

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

#### **Konsolenausgabe**  

{{< highlight javascript >}}  

Comment: Test Threaded Comment  

Author: Aspose Test  

Created Time: 5/15/2019 12:46:23 PM  

{{< /highlight >}}  

## **Kommentare bearbeiten**  

### **Bearbeiten Sie kommentierte Kommentare mit Excel**  

Um einen kommentierten Kommentar in Excel zu bearbeiten, klicken Sie auf den **Bearbeiten**-Link im Kommentar wie im folgenden Bild gezeigt.  

![todo:image_alt_text](threaded-comments_7.jpg)  

### **Threaded-Kommentar bearbeiten mit Aspose.Cells**  

Aspose.Cells bietet die Methode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-), um thread-spezifische Kommentare für die angegebene Spalte abzurufen. Die Methode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) akzeptiert den Spaltennamen als Parameter und gibt die [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection) zurück. Sie können den gewünschten Kommentar in der [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection) aktualisieren und die Arbeitsmappe speichern.  

Das folgende Beispiel demonstriert die Bearbeitung des ersten Threaded-Kommentars in Spalte A1 durch Laden der [Beispiel Excel Datei](89849861.xlsx). Bitte beachten Sie die [Ausgabe Excel-Datei](89849862.xlsx), die vom Code generiert wird und die aktualisierten Kommentare zur Referenz zeigt.  

#### **Beispielcode**  

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

## **Threaded-Kommentare entfernen**  

### **Threaded-Kommentare mit Excel entfernen**  

Um Threaded-Kommentare in Excel zu entfernen, klicken Sie mit der rechten Maustaste auf die Zelle mit den Kommentaren und wählen Sie die Option **Kommentar löschen**, wie im folgenden Bild gezeigt.  

![todo:image_alt_text](threaded-comments_8.jpg)   


{{< app/cells/assistant language="nodejs-cpp" >}}
