---
title: Threaded Comments
type: docs
weight: 140
url: /de/net/threaded-comments/
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

Aspose.Cells bietet die Methode [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1) zum Hinzufügen von Kommentarfäden an. Die Methode [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1) akzeptiert die folgenden drei Parameter.

- Zellenname: Der Name der Zelle, in die der Kommentar eingefügt wird.
- Kommentartext: Der Text des Kommentars.
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentauthor): Der Verfasser des Kommentars

Das folgende Codebeispiel zeigt die Verwendung der Methode [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1) zum Hinzufügen eines kommentierten Fadens zur Zelle A1. Bitte sehen Sie die durch den Code generierte [Ausgabe-Excel-Datei](89849859.xlsx) zur Referenz an.

#### **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-AddThreadedComments-1.cs" >}}

## **Lese kommentierte Fäden**

### **Lese kommentierte Fäden mit Excel**

Um kommentierte Fäden in Excel zu lesen, fahren Sie einfach mit der Maus über die Zelle, die Kommentare enthält, um die Kommentare anzuzeigen. Die Ansicht der Kommentare wird der Darstellung im folgenden Bild ähneln.

![todo:image_alt_text](threaded-comments_1.jpg)

### **Lese kommentierte Fäden mit Aspose.Cells**

Aspose.Cells bietet die Methode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) zum Abrufen von kommentierten Fäden für die angegebene Spalte. Die Methode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) akzeptiert den Spaltennamen als Parameter und gibt die [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) zurück. Sie können über die [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) iterieren, um die Kommentare anzuzeigen.

Das folgende Beispiel zeigt das Lesen von Kommentaren aus Spalte A1 durch Laden der [Beispiel-Excel-Datei](89849861.xlsx). Bitte sehen Sie die durch den Code generierte Konsolenausgabe zur Referenz an.

#### **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadThreadedComments-1.cs" >}}

#### **Konsolenausgabe**

{{< highlight csharp >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **Lese Erstellungszeitpunkt von kommentierten Fäden**

Aspose.Cells bietet die Methode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) zum Abrufen von kommentierten Fäden für die angegebene Spalte. Die Methode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) akzeptiert den Spaltennamen als Parameter und gibt die [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) zurück. Sie können über die [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) iterieren und die [**ThreadedComment.CreatedTime**](https://reference.aspose.com/cells/net/aspose.cells/threadedcomment/properties/createdtime)-Eigenschaft verwenden.

Das folgende Beispiel zeigt das Lesen des Erstellungszeitpunkts von kommentierten Fäden durch Laden der [Beispiel-Excel-Datei](89849861.xlsx). Bitte sehen Sie die durch den Code generierte Konsolenausgabe zur Referenz an.

#### **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadThreadedCommentCreatedTime-1.cs" >}}

#### **Konsolenausgabe**

{{< highlight csharp >}}

Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 5/15/2019 12:46:23 PM

{{< /highlight >}}

## **Kommentare bearbeiten**

### **Bearbeiten Sie kommentierte Kommentare mit Excel**

Um einen kommentierten Kommentar in Excel zu bearbeiten, klicken Sie auf den **Bearbeiten**-Link im Kommentar wie im folgenden Bild gezeigt.

![todo:image_alt_text](threaded-comments_7.jpg)

### **Threaded-Kommentar bearbeiten mit Aspose.Cells**

Aspose.Cells bietet die Methode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) zum Abrufen von Threaded-Kommentaren für die angegebene Spalte. Die Methode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) akzeptiert den Spaltennamen als Parameter und gibt das [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) zurück. Sie können den erforderlichen Kommentar in den [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) aktualisieren und die Arbeitsmappe speichern.

Das folgende Beispiel demonstriert die Bearbeitung des ersten Threaded-Kommentars in Spalte A1 durch Laden der [Beispiel Excel Datei](89849861.xlsx). Bitte beachten Sie die [Ausgabe Excel-Datei](89849862.xlsx), die vom Code generiert wird und die aktualisierten Kommentare zur Referenz zeigt.

#### **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-EditThreadedComments-1.cs" >}}

## **Threaded-Kommentare entfernen**

### **Threaded-Kommentare mit Excel entfernen**

Um Threaded-Kommentare in Excel zu entfernen, klicken Sie mit der rechten Maustaste auf die Zelle mit den Kommentaren und wählen Sie die Option **Kommentar löschen**, wie im folgenden Bild gezeigt.

![todo:image_alt_text](threaded-comments_8.jpg)

### **Threaded-Kommentare mit Aspose.Cells entfernen**

Aspose.Cells bietet die Methode [**Comments.RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/removeat/index) zum Entfernen von Kommentaren für die angegebene Spalte. Die Methode [**Comments.RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/removeat/index) akzeptiert den Spaltennamen als Parameter und entfernt die Kommentare in dieser Spalte.

Das folgende Beispiel demonstriert das Entfernen von Kommentaren in Spalte A1 durch Laden der [Beispiel Excel Datei](89849861.xlsx). Bitte sehen Sie die [Ausgabe Excel-Datei](89849864.xlsx), die vom Code generiert wurde, zur Referenz.

#### **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-RemoveThreadedComments-1.cs" >}}

{{% alert color="primary" %}}

Bitte beachten Sie, dass durch Entfernen von Kommentaren mit Aspose.Cells der Autor nicht automatisch entfernt wird. Wenn Sie den Autor ebenfalls entfernen müssen, verwenden Sie bitte die RemoveAt-Methode der [**ThreadedCommentAuthorCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentauthorcollection)-Klasse, wie im obigen Beispiel gezeigt.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
