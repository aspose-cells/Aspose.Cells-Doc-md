---
title: Threaded Comments
type: docs
weight: 140
url: /de/java/threaded-comments/
---

# **Antwortkommentare**
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
  - Klicken Sie auf die Registerkarte **Überprüfen**
  - Klicken Sie auf die Schaltfläche **Neuer Kommentar**
  - Dadurch wird ein Dialogfeld geöffnet, um Kommentare in der aktiven Zelle einzugeben.
  - ![todo:image_alt_text](threaded-comments_4.jpg)
- Methode 2
  - Klicken Sie mit der rechten Maustaste auf die Zelle, in die Sie den Kommentar einfügen möchten.
  - Wählen Sie die Option **Neuer Kommentar** aus.
  - Dadurch wird ein Dialogfeld geöffnet, um Kommentare in der aktiven Zelle einzugeben.
  - ![todo:image_alt_text](threaded-comments_5)
### **Fügen Sie einen Kommentarfaden mit Aspose.Cells hinzu**
Aspose.Cells bietet die Methode [Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment-java.lang.String-java.lang.String-com.aspose.cells.ThreadedCommentAuthor-) zum Hinzufügen von Threaded-Kommentaren. Die Methode [Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment-java.lang.String-java.lang.String-com.aspose.cells.ThreadedCommentAuthor-) akzeptiert die folgenden drei Parameter.

- Zellenname: Der Name der Zelle, in die der Kommentar eingefügt wird.
- Kommentartext: Der Text des Kommentars.
- [ThreadedCommentAuthor](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentAuthor): Der Verfasser des Kommentars.

Das folgende Codebeispiel zeigt die Verwendung der Methode [Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment-java.lang.String-java.lang.String-com.aspose.cells.ThreadedCommentAuthor-) zum Hinzufügen eines Threaded-Kommentars in die Zelle A1. Bitte sehen Sie sich die [Ausgabedatei](AddThreadedComments_out.xlsx) an, die durch den Code erzeugt wurde.
#### **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddThreadedComments-1.java" >}}
## **Lese kommentierte Fäden**
### **Lese kommentierte Fäden mit Excel**
Um kommentierte Fäden in Excel zu lesen, fahren Sie einfach mit der Maus über die Zelle, die Kommentare enthält, um die Kommentare anzuzeigen. Die Ansicht der Kommentare wird der Darstellung im folgenden Bild ähneln.

![todo:image_alt_text](threaded-comments_1.jpg)
### **Lese kommentierte Fäden mit Aspose.Cells**
Aspose.Cells bietet die Methode [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) zum Abrufen von Threaded-Kommentaren für die angegebene Spalte. Die Methode [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) nimmt den Spaltennamen als Parameter und gibt die [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection) zurück. Sie können über die [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection) iterieren, um die Kommentare zu sehen.

Das folgende Beispiel demonstriert das Lesen von Kommentaren aus Spalte A1 durch Laden der [Beispieldatei](ThreadedCommentsSample.xlsx). Bitte sehen Sie die durch den Code generierte Konsolenausgabe als Referenz an.
#### **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedComments-1.java" >}}
#### **Konsolenausgabe**

{{< highlight java >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **Lese Erstellungszeitpunkt von kommentierten Fäden**
Aspose.Cells bietet die Methode [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) zum Abrufen von Threaded-Kommentaren für die angegebene Spalte. Die Methode [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) nimmt den Spaltennamen als Parameter und gibt die [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection) zurück. Sie können die Kommentare innerhalb der [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection) mit der Eigenschaft [ThreadedComment.CreatedTime](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcomment#CreatedTime) aktualisieren.

Das folgende Beispiel demonstriert das Lesen des Erstellungszeitpunkts themenbezogener Kommentare durch Laden der [Beispieldatei](ThreadedCommentsSample.xlsx). Bitte sehen Sie die durch den Code generierte Konsolenausgabe als Referenz an.
#### **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedCommentCreatedTime-1.java" >}}
#### **Konsolenausgabe**

{{< highlight java >}}

Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 2019-05-15T12:46:23

{{< /highlight >}}

## **Kommentare bearbeiten**
### **Bearbeiten Sie kommentierte Kommentare mit Excel**
Um einen gestuften Kommentar in Excel zu bearbeiten, klicken Sie auf den **Bearbeiten**-Link des Kommentars, wie im folgenden Bild gezeigt.

![todo:image_alt_text](threaded-comments_7.jpg)
### **Threaded-Kommentar bearbeiten mit Aspose.Cells**
Aspose.Cells bietet die Methode [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) zum Abrufen von Threaded-Kommentaren für die angegebene Spalte. Die Methode [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) akzeptiert den Spaltennamen als Parameter und gibt die [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection) zurück. Sie können den erforderlichen Kommentar in der [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection) aktualisieren und die Arbeitsmappe speichern.

Das folgende Beispiel zeigt, wie der erste gestufte Kommentar in Spalte A1 bearbeitet wird, indem die [Beispiel-Excel-Datei](ThreadedCommentsSample.xlsx) geladen wird. Sehen Sie sich die durch den Code generierte [Ausgabedatei](EditThreadedComments.xlsx) an, um den aktualisierten Kommentar zu sehen.
#### **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "EditThreadedComments-1.java" >}}
## **Threaded-Kommentare entfernen**
### **Threaded-Kommentare mit Excel entfernen**
Um gestufte Kommentare in Excel zu entfernen, klicken Sie mit der rechten Maustaste auf die Zelle mit den Kommentaren und wählen Sie die Option **Kommentar löschen**, wie im folgenden Bild gezeigt.

![todo:image_alt_text](threaded-comments_8.jpg)
### **Threaded-Kommentare mit Aspose.Cells entfernen**
Aspose.Cells bietet die Methode [Comments.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt-int-) zum Entfernen von Kommentaren in der angegebenen Spalte. Die Methode [Comments.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt-int-) nimmt den Spaltennamen als Parameter und entfernt die Kommentare in dieser Spalte. 

Das folgende Beispiel zeigt, wie Kommentare in Spalte A1 entfernt werden, indem die [Beispiel-Excel-Datei](ThreadedCommentsSample.xlsx) geladen wird. Sehen Sie sich die durch den Code generierte [Ausgabedatei](ThreadedCommentsSample_Out.xlsx) für Referenzzwecke an.
#### **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "RemoveThreadedComments-1.java" >}}

{{% alert color="primary" %}} 

Bitte beachten Sie, dass beim Entfernen eines Kommentars mit Aspose.Cells der Autor nicht automatisch entfernt wird. Wenn Sie den Autor ebenfalls entfernen möchten, verwenden Sie bitte die Methode [ThreadedCommentAuthorCollection.removeAt](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcommentauthorcollection#removeAt-int-) wie im Beispiel oben gezeigt.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
