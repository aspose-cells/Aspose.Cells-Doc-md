---
title: Kommentare und Notizen verwalten
linktitle: Kommentare und Notizen
type: docs
weight: 128
url: /de/java/comments-and-notes/
description: Kommentare oder Notizen mit Aspose.Cells for Java einfügen und verwalten.
keywords: Kommentare einfügen, Notizen einfügen
---

## **Einführung**

Kommentare werden verwendet, um zusätzliche Informationen zu Zellen hinzuzufügen. Aspose.Cells bietet zwei Methoden zum Hinzufügen von Kommentaren zu Zellen. Die erste Methode besteht darin, Kommentare manuell in einer Designerdatei zu erstellen. Diese Kommentare werden dann mithilfe von Aspose.Cells importiert. Die zweite Methode besteht darin, Kommentare mithilfe der Aspose.Cells-API zur Laufzeit hinzuzufügen. In diesem Thema wird das Hinzufügen von Kommentaren zu Zellen mithilfe der Aspose.Cells-API erläutert. Auch die Formatierung von Kommentaren wird erklärt.

## **Einen Kommentar hinzufügen**

Fügen Sie einen Kommentar zu einer Zelle hinzu, indem Sie die **Hinzufügen**-Methode der [**Comments**](https://reference.aspose.com/cells/java/com.aspose.cells/CommentCollection)-Sammlung (die in dem Objekt [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) verkapselt ist) aufrufen. Das neue [**Comment**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment)-Objekt kann von der [**Comments**](https://reference.aspose.com/cells/java/com.aspose.cells/CommentCollection)-Sammlung abgerufen werden, indem der Kommentarindex übergeben wird. Nach dem Zugriff auf das [**Comment**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment)-Objekt können Sie den Kommentarhinweis anpassen, indem Sie die [**Comment**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment)-Eigenschaft des Objekts [**Note**](https://reference.aspose.com/cells/java/com.aspose.cells/comment#Note) verwenden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddingComment-1.java" >}}

## **Kommentarformatierung**

Es ist auch möglich, das Erscheinungsbild von Kommentaren zu formatieren, indem ihre Höhe, Breite und Schriftarteneinstellungen konfiguriert werden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "CommentFormatting-1.java" >}}

## **Ein Bild zum Kommentar hinzufügen**

Mit Microsoft Excel 2007 ist es auch möglich, ein Bild als Hintergrund für einen Zellenkommentar zu haben. In Excel 2007 wird dies durch die folgenden Schritte erreicht. (Es wird davon ausgegangen, dass bereits ein Zellenkommentar hinzugefügt wurde.)

1. Klicken Sie mit der rechten Maustaste auf die Zelle, die den Kommentar enthält.
1. Wählen Sie **Kommentare einblenden/ausblenden** und löschen Sie jeglichen Text aus dem Kommentar.
1. Klicken Sie auf den Rand des Kommentars, um ihn auszuwählen.
1. Wählen Sie **Format** und dann **Kommentar** aus.
1. Auf der Registerkarte **Farben und Linien** die **Farbe**-Liste erweitern.
1. Klicken Sie auf **Fülleffekte**.
1. Klicken Sie auf der Registerkarte **Bild** auf **Bild auswählen**.
1. Suchen Sie das Bild und wählen Sie es aus.
1. Klicken Sie auf **OK**, bis alle Dialogfelder geschlossen sind.

Auch Aspose.Cells bietet diese Funktion. Im Folgenden finden Sie einen Beispielcode, der eine XLSX-Datei von Grund auf erstellt und einem Zelle "A1" einen Kommentar mit einem Bild als Hintergrund hinzufügt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddImageToComment-1.java" >}}

## **Erweiterte Themen**
- [Ändern der Textrichtung des Kommentars](/cells/de/java/change-text-direction-of-the-comment/)
- [Ändern der Kommentarschriftfarbe](/cells/de/java/how-to-change-the-comment-font-color/)
- [Wie man den Kommentarhintergrund einstellt](/cells/de/java/how-to-set-comment-background/)
- [Antwortkommentare](/cells/de/java/threaded-comments/)

