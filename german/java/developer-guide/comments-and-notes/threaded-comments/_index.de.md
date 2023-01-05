---
title: Verkettete Kommentare
type: docs
weight: 140
url: /de/java/threaded-comments/
---
# **Verkettete Kommentare**
MS Excel 365 bietet eine Funktion zum Hinzufügen von Thread-Kommentaren. Diese Kommentare funktionieren als Konversationen und können für Diskussionen verwendet werden. Die Kommentare verfügen jetzt über ein Antwortfeld, das Thread-Gespräche ermöglicht. Die alten Kommentare heißen in Excel 365 Notizen. Der folgende Screenshot zeigt, wie Thread-Kommentare angezeigt werden, wenn sie in Excel geöffnet werden.

![todo: Bild_alt_Text](threaded-comments_1.jpg)

Thread-Kommentare werden in älteren Versionen von Excel so angezeigt. Die folgenden Bilder wurden durch Öffnen der Beispieldatei in Excel 2016 aufgenommen.

![todo: Bild_alt_Text](threaded-comments_2.jpg)



![todo: Bild_alt_Text](threaded-comments_3.jpg)



Aspose.Cells bietet auch die Funktion zum Verwalten von Thread-Kommentaren.
## **Verkettete Kommentare hinzufügen**
### **Verketteten Kommentar mit Excel hinzufügen**
Führen Sie die folgenden Schritte aus, um Thread-Kommentare in Excel 365 hinzuzufügen.

- Methode 1
 - Drücke den**Überprüfung**Tab
 - Drücke den**Neuer Kommentar**Knopf
 - Dies öffnet einen Dialog zur Eingabe von Kommentaren in die aktive Zelle.
  - ![todo: Bild_alt_Text](threaded-comments_4.jpg)
- Methode 2
 - Klicken Sie mit der rechten Maustaste auf die Zelle, in die Sie den Kommentar einfügen möchten.
 - Drücke den**Neuer Kommentar**Möglichkeit.
 - Dies öffnet einen Dialog zur Eingabe von Kommentaren in die aktive Zelle.
  - ![todo: Bild_alt_Text](threaded-comments_5)
### **Fügen Sie einen Thread-Kommentar mit Aspose.Cells hinzu**
Aspose.Cells bietet[Kommentare.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\))-Methode zum Hinzufügen von Thread-Kommentaren[Kommentare.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\)) akzeptiert die folgenden drei Parameter.

- Cell Name: Der Name der Zelle, in die der Kommentar eingefügt wird.
- Kommentartext: Der Text des Kommentars.
- [ThreadedCommentAutor](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentAuthor): Der Autor des Kommentars

Das folgende Codebeispiel veranschaulicht die Verwendung von[Kommentare.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\)) Methode, um der Zelle A1 einen Thread-Kommentar hinzuzufügen. Bitte sehen Sie sich ... an[Excel-Datei ausgeben](AddThreadedComments_out.xlsx)generiert durch den Code als Referenz.
#### **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddThreadedComments-1.java" >}}
## **Lesen Sie Thread-Kommentare**
### **Lesen Sie Thread-Kommentare mit Excel**
Um Thread-Kommentare in Excel zu lesen, bewegen Sie einfach die Maus über die Zelle, die Kommentare enthält, um die Kommentare anzuzeigen. Die Kommentaransicht sieht wie in der folgenden Abbildung aus.

![todo: Bild_alt_Text](threaded-comments_1.jpg)
### **Lesen Sie Thread-Kommentare mit Aspose.Cells**
Aspose.Cells bietet[Kommentare.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\))-Methode, um Thread-Kommentare für die angegebene Spalte abzurufen.[Kommentare.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\))-Methode akzeptiert den Spaltennamen als Parameter und gibt die zurück[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). Sie können über die iterieren[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)um die Kommentare anzuzeigen.

Das folgende Beispiel demonstriert das Lesen von Kommentaren aus Spalte A1 durch Laden der[Beispiel-Excel-Datei](ThreadedCommentsSample.xlsx). Bitte sehen Sie sich die vom Code generierte Konsolenausgabe als Referenz an.
#### **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedComments-1.java" >}}
#### **Konsolenausgabe**
Kommentar: Thread-Kommentar testen

Autor: Aspose Test
### **Lesen Sie die Erstellungszeit von Thread-Kommentaren**
Aspose.Cells bietet[Kommentare.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\))-Methode, um Thread-Kommentare für die angegebene Spalte abzurufen.[Kommentare.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\))-Methode akzeptiert den Spaltennamen als Parameter und gibt die zurück[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). Sie können über die iterieren[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)und benutze die[ThreadedComment.CreatedTime](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcomment#CreatedTime)Eigentum.

Das folgende Beispiel demonstriert das Lesen der Erstellungszeit von Thread-Kommentaren durch Laden der[Beispiel-Excel-Datei](ThreadedCommentsSample.xlsx). Bitte sehen Sie sich die vom Code generierte Konsolenausgabe als Referenz an.
#### **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedCommentCreatedTime-1.java" >}}
#### **Konsolenausgabe**
Kommentar: Thread-Kommentar testen

Autor: Aspose Test

Erstellungszeit: 2019-05-15T12:46:23
## **Verkettete Kommentare bearbeiten**
### **Bearbeiten Sie Thread-Kommentare mit Excel**
Um einen Thread-Kommentar in Excel zu bearbeiten, klicken Sie auf**Bearbeiten**Link auf den Kommentar, wie im folgenden Bild gezeigt.

![todo: Bild_alt_Text](threaded-comments_7.jpg)
### **Bearbeiten Sie den Thread-Kommentar mit Aspose.Cells**
Aspose.Cells bietet[Kommentare.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\))-Methode, um Thread-Kommentare für die angegebene Spalte abzurufen.[Kommentare.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\))-Methode akzeptiert den Spaltennamen als Parameter und gibt die zurück[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). Sie können den erforderlichen Kommentar in der aktualisieren[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)und speichern Sie die Arbeitsmappe.

Das folgende Beispiel zeigt das Bearbeiten des ersten Kommentarthreads in Spalte A1 durch Laden der[Beispiel-Excel-Datei](ThreadedCommentsSample.xlsx). Bitte sehen Sie sich ... an[Excel-Datei ausgeben](EditThreadedComments.xlsx)generiert durch den Code, der den aktualisierten Kommentar als Referenz anzeigt.
#### **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "EditThreadedComments-1.java" >}}
## **Verkettete Kommentare entfernen**
### **Entfernen Sie Thread-Kommentare mit Excel**
Um Thread-Kommentare in Excel zu entfernen, klicken Sie mit der rechten Maustaste auf die Zelle, die die Kommentare enthält, und klicken Sie auf die**Kommentar löschen**Option wie im folgenden Bild gezeigt.

![todo: Bild_alt_Text](threaded-comments_8.jpg)
### **Entfernen Sie Thread-Kommentare mit Aspose.Cells**
Aspose.Cells bietet[Kommentare.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt\(int\))-Methode zum Entfernen von Kommentaren für die angegebene Spalte.[Kommentare.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt\(int\)) akzeptiert den Spaltennamen als Parameter und entfernt die Kommentare in dieser Spalte.

Das folgende Beispiel zeigt das Entfernen von Kommentaren in Spalte A1 durch Laden der[Beispiel-Excel-Datei](ThreadedCommentsSample.xlsx). Bitte sehen Sie sich ... an[Excel-Datei ausgeben](ThreadedCommentsSample_Out.xlsx)generiert durch den Code als Referenz.
#### **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "RemoveThreadedComments-1.java" >}}

{{% alert color="primary" %}} 

 Bitte beachten Sie, dass durch das Entfernen eines Kommentars mit Aspose.Cells der Autor nicht automatisch entfernt wird. Wenn Sie auch den Autor entfernen müssen, verwenden Sie bitte die[ThreadedCommentAuthorCollection.removeAt](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcommentauthorcollection#removeAt\(int\)Methode wie im obigen Beispiel gezeigt.

{{% /alert %}}
