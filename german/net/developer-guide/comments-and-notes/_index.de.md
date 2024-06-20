---
title: Kommentare und Notizen verwalten
linktitle: Kommentare und Notizen
type: docs
weight: 128
url: /de/net/comments-and-notes/
description: Kommentare oder Notizen mit Aspose.Cells für .Net einfügen und verwalten
keywords: Kommentare einfügen, Notizen einfügen
---

## **Einführung**

Kommentare werden verwendet, um zusätzliche Informationen zu Zellen hinzuzufügen. Aspose.Cells bietet zwei Methoden zum Hinzufügen von Kommentaren zu Zellen. Die erste Methode besteht darin, Kommentare manuell in einer Designerdatei zu erstellen. Diese Kommentare werden dann mithilfe von Aspose.Cells importiert. Die zweite Methode besteht darin, Kommentare mithilfe der Aspose.Cells-API zur Laufzeit hinzuzufügen. In diesem Thema wird das Hinzufügen von Kommentaren zu Zellen mithilfe der Aspose.Cells-API erläutert. Auch die Formatierung von Kommentaren wird erklärt.

## **Einen Kommentar hinzufügen**

Fügen Sie mithilfe der [**Comments**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection)-Sammlung und der [**Add**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/add/index)-Methode der [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-Objektsammlung einen Kommentar zu einer Zelle hinzu. Das neue [**Comment**](https://reference.aspose.com/cells/net/aspose.cells/comment)-Objekt kann aus der [**Comments**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection)-Sammlung durch Weitergabe des Kommentarindex abgerufen werden. Nach dem Abrufen des [**Comment**](https://reference.aspose.com/cells/net/aspose.cells/comment)-Objekts passen Sie die Kommentarnotiz mithilfe der [**Comment**](https://reference.aspose.com/cells/net/aspose.cells/comment)-Eigenschaft des [**Note**](https://reference.aspose.com/cells/net/aspose.cells/comment/properties/note)-Objekts an.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-AddingComment-1.cs" >}}

## **Kommentarformatierung**

Es ist auch möglich, das Erscheinungsbild von Kommentaren zu formatieren, indem ihre Höhe, Breite und Schriftarteneinstellungen konfiguriert werden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-CommentFormatting-1.cs" >}}

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-AddImageToComment-1.cs" >}}

## **Erweiterte Themen**
- [Ändern der Textrichtung des Kommentars](/cells/de/net/change-text-direction-of-the-comment/)
- [Ändern der Kommentarschriftfarbe](/cells/de/net/how-to-change-the-comment-font-color/)
- [Wie man den Kommentarhintergrund einstellt](/cells/de/net/how-to-set-comment-background/)
- [Antwortkommentare](/cells/de/net/threaded-comments/)

