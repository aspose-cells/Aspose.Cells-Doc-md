---
title: Kommentare und Notizen verwalten
linktitle: Kommentare und Notizen
type: docs
weight: 128
url: /de/java/comments-and-notes/
description: Fügen Sie Kommentare oder Notizen ein und verwalten Sie sie mit Aspose.Cells für Java.
keywords: insert comments, insert notes
---
## **Einführung**

Kommentare werden verwendet, um zusätzliche Informationen zu Zellen hinzuzufügen. Aspose.Cells bietet zwei Methoden zum Hinzufügen von Kommentaren zu Zellen. Die erste besteht darin, Kommentare manuell in einer Designerdatei zu erstellen. Diese Kommentare werden dann mit Aspose.Cells importiert. Die zweite besteht darin, Kommentare mit Aspose.Cells API zur Laufzeit hinzuzufügen. In diesem Thema wird das Hinzufügen von Kommentaren zu Zellen mit Aspose.Cells API behandelt. Das Formatieren von Kommentaren wird ebenfalls erläutert.

## **Hinzufügen eines Kommentars**

 Fügen Sie einer Zelle einen Kommentar hinzu, indem Sie die aufrufen[**Bemerkungen**](https://reference.aspose.com/cells/java/com.aspose.cells/CommentCollection) Sammlung**Addieren** Methode (eingekapselt in der[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Objekt). Das neue[**Kommentar**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) Auf das Objekt kann über die zugegriffen werden[**Bemerkungen**](https://reference.aspose.com/cells/java/com.aspose.cells/CommentCollection) Sammlung durch Übergabe des Kommentarindex. Nach dem Zugriff auf die[**Kommentar**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) Objekt, passen Sie die Kommentarnotiz an, indem Sie das verwenden[**Kommentar**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) Objekt[**Notiz**](https://reference.aspose.com/cells/java/com.aspose.cells/comment#Note)Eigentum.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddingComment-1.java" >}}

## **Kommentarformatierung**

Es ist auch möglich, das Erscheinungsbild von Kommentaren zu formatieren, indem Sie ihre Höhe, Breite und Schriftarteinstellungen konfigurieren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "CommentFormatting-1.java" >}}

## **Fügen Sie ein Bild zum Kommentar hinzu**

Mit Microsoft Excel 2007 ist es auch möglich, ein Bild als Hintergrund für einen Zellkommentar zu haben. In Excel 2007 wird dies durch Ausführen der folgenden Schritte erreicht. (Sie gehen davon aus, dass Sie bereits einen Zellenkommentar hinzugefügt haben.)

1. Klicken Sie mit der rechten Maustaste auf die Zelle, die den Kommentar enthält.
1.  Wählen**Kommentare ein-/ausblenden**, und löschen Sie jeglichen Text aus dem Kommentar.
1. Klicken Sie auf den Rand des Kommentars, um ihn auszuwählen.
1.  Wählen**Format** , dann**Kommentar**.
1.  Auf der**Farben und Linien** Erweitern Sie die Registerkarte**Farbe** aufführen.
1.  Klicken**Fülleffekte**.
1.  Auf der**Bild** Registerkarte, klicken Sie auf**Wählen Sie Bild**.
1. Suchen Sie das Bild und wählen Sie es aus.
1.  Klicken**OK** bis alle Dialoge geschlossen sind.

Aspose.Cells bietet diese Funktion ebenfalls. Unten ist ein Codebeispiel, das eine XLSX-Datei von Grund auf neu erstellt, indem ein Kommentar zur Zelle "A1" mit einem als Hintergrund festgelegten Bild hinzugefügt wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddImageToComment-1.java" >}}

## **Themen vorantreiben**
- [Textrichtung des Kommentars ändern](/cells/de/java/change-text-direction-of-the-comment/)
- [So ändern Sie die Schriftfarbe für Kommentare](/cells/de/java/how-to-change-the-comment-font-color/)
- [So legen Sie den Kommentarhintergrund fest](/cells/de/java/how-to-set-comment-background/)
- [Verkettete Kommentare](/cells/de/java/threaded-comments/)

