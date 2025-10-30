---
title: Threaded Comments
type: docs
weight: 140
url: /de/python-net/threaded-comments/
---

## **Antwortkommentare**

MS Excel 365 bietet eine Funktion zum Hinzufügen von Threaded-Kommentaren. Diese Kommentare fungieren als Unterhaltungen und können für Diskussionen verwendet werden. Die Kommentare enthalten nun eine Antwortbox, die Threaded-Konversationen ermöglicht. Die alten Kommentare werden in Excel 365 als Notizen bezeichnet. Der Screenshot unten zeigt, wie threaded Kommentare angezeigt werden, wenn sie in Excel geöffnet werden.

![todo:image_alt_text](threaded-comments_1.jpg)

Threaded comments werden in älteren Versionen von Excel so angezeigt. Die folgenden Bilder wurden erstellt, indem die Beispieldatei in Excel 2016 geöffnet wurde.

![todo:image_alt_text](threaded-comments_2.jpg)

![todo:image_alt_text](threaded-comments_3.jpg)

Aspose.Cells für Python via .NET bietet auch die Funktion, Threaded Comments zu verwalten.

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

### **Threaded-Kommentar mit Aspose.Cells für Python via .NET hinzufügen**

Aspose.Cells für Python via .NET stellt die [**Comments.add_threaded_comment**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add_threaded_comment/)-Methode bereit, um threaded Kommentare hinzuzufügen. Die [**Comments.add_threaded_comment**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add_threaded_comment) Methode akzeptiert die folgenden drei Parameter.

- Zellenname: Der Name der Zelle, in die der Kommentar eingefügt wird.
- Kommentartext: Der Text des Kommentars.
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentauthor): Der Verfasser des Kommentars

Das folgende Codebeispiel zeigt die Verwendung der Methode [**Comments.add_threaded_comment**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add_threaded_comment) zum Hinzufügen eines kommentierten Fadens zur Zelle A1. Bitte sehen Sie die durch den Code generierte [Ausgabe-Excel-Datei](89849859.xlsx) zur Referenz an.

#### **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-AddThreadedComments-1.py" >}}

## **Lese kommentierte Fäden**

### **Lese kommentierte Fäden mit Excel**

Um kommentierte Fäden in Excel zu lesen, fahren Sie einfach mit der Maus über die Zelle, die Kommentare enthält, um die Kommentare anzuzeigen. Die Ansicht der Kommentare wird der Darstellung im folgenden Bild ähneln.

![todo:image_alt_text](threaded-comments_1.jpg)

### **Threaded-Kommentare mit Aspose.Cells für Python via .NET lesen**

Aspose.Cells für Python via .NET bietet die [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments)-Methode zum Abrufen von Threaded-Kommentaren für die angegebene Spalte. Die [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments)-Methode akzeptiert den Spaltennamen als Parameter und gibt die [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection) zurück. Sie können über die [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection) iterieren, um die Kommentare anzuzeigen.

Das folgende Beispiel zeigt das Lesen von Kommentaren aus Spalte A1 durch Laden der [Beispiel-Excel-Datei](89849861.xlsx). Bitte sehen Sie die durch den Code generierte Konsolenausgabe zur Referenz an.

#### **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-ReadThreadedComments-1.py" >}}

#### **Konsolenausgabe**

{{< highlight csharp >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **Lese Erstellungszeitpunkt von kommentierten Fäden**

Aspose.Cells für Python via .NET bietet die [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments)-Methode zum Abrufen von Threaded-Kommentaren für die angegebene Spalte. Die [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments)-Methode akzeptiert den Spaltennamen als Parameter und gibt die [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection) zurück. Sie können über die [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection) iterieren und die [**ThreadedComment.created_time**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcomment/created_time)-Eigenschaft verwenden.

Das folgende Beispiel zeigt das Lesen des Erstellungszeitpunkts von kommentierten Fäden durch Laden der [Beispiel-Excel-Datei](89849861.xlsx). Bitte sehen Sie die durch den Code generierte Konsolenausgabe zur Referenz an.

#### **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-ReadThreadedCommentCreatedTime-1.py" >}}

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

### **Threaded-Kommentare mit Aspose.Cells für Python via .NET bearbeiten**

Aspose.Cells für Python via .NET bietet die [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments)-Methode zum Abrufen von Threaded-Kommentaren für die angegebene Spalte. Die [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments)-Methode akzeptiert den Spaltennamen als Parameter und gibt die [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection) zurück. Sie können den gewünschten Kommentar in den [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection) aktualisieren und die Arbeitsmappe speichern.

Das folgende Beispiel demonstriert die Bearbeitung des ersten Threaded-Kommentars in Spalte A1 durch Laden der [Beispiel Excel Datei](89849861.xlsx). Bitte beachten Sie die [Ausgabe Excel-Datei](89849862.xlsx), die vom Code generiert wird und die aktualisierten Kommentare zur Referenz zeigt.

#### **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-EditThreadedComments-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
