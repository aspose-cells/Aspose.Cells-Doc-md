---
title: Verwalten von Kommentaren in einem Arbeitsblatt
type: docs
weight: 110
url: /de/net/aspose-cells-griddesktop/manage-comments-in-a-worksheet/
keywords: GridDesktop, Kommentar, Kommentare
description: Dieser Artikel stellt vor, wie mit Kommentaren in GridDesktop gearbeitet wird.
---

{{% alert color="primary" %}} 

In MS Excel müssen Sie mit der Kommentarfunktion vertraut sein, die es Benutzern ermöglicht, Kommentare zu Zellen hinzuzufügen. Diese Funktion ist hilfreich, wenn Benutzern beim Eingeben von Werten in die Zellen bestimmte Informationen bereitgestellt werden müssen. Wenn ein Benutzer seinen Mauszeiger auf eine kommentierte Zelle setzt, wird eine kleine Popup-Nachricht angezeigt, um dem Benutzer einige Informationen bereitzustellen. Mit Aspose.Cells.GridDesktop können Entwickler Kommentare zu Zellen erstellen. In diesem Thema werden wir die Verwendung dieser Funktion im Detail erläutern.

{{% /alert %}} 
## **Kommentare hinzufügen**
Um einen Kommentar zu einer Zelle mit Aspose.Cells.GridDesktop hinzuzufügen, befolgen Sie bitte die folgenden Schritte:

- Fügen Sie das Steuerelement Aspose.Cells.GridDesktop zu Ihrem **Formular** hinzu
- Greifen Sie auf jedes gewünschte **Arbeitsblatt** zu
- Fügen Sie einen **Kommentar** zum Arbeitsblatt hinzu, indem Sie die Zelle (unter Verwendung ihres Namens oder ihrer Zeilen- und Spaltennummer) angeben, in der der Kommentar hinzugefügt werden soll.

Der folgende Code fügt Kommentare zu den Zellen **b2** und **b4** des Arbeitsblatts hinzu.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AddingComments.cs" >}}


Die **Comments**-Sammlung im **Worksheet**-Objekt bietet eine überladene **Add**-Methode. Entwickler können eine beliebige überladene Version der **Add**-Methode entsprechend ihren spezifischen Anforderungen verwenden.
## **Zugriff auf Kommentare**
Um auf einen vorhandenen Kommentar im Arbeitsblatt zuzugreifen und diesen zu ändern, können Entwickler den Kommentar aus der **Comments**-Sammlung des **Worksheets** abrufen, indem sie die Zelle angeben (unter Verwendung des Zellnamens oder ihrer Position in Bezug auf Zeile und Spaltennummer), in der der Kommentar eingefügt ist. Sobald der Kommentar abgerufen ist, können Entwickler seinen Text zur Laufzeit ändern.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AccessingComments.cs" >}}
## **Kommentare entfernen**
Um einen vorhandenen Kommentar zu entfernen, können Entwickler einfach auf ein gewünschtes Arbeitsblatt zugreifen und dann den Kommentar aus der **Comments**-Sammlung des **Worksheet** entfernen, indem sie die Zelle (unter Verwendung ihres Namens oder ihrer Zeilen- und Spaltennummer) angeben, die den Kommentar enthält.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-RemovingComments.cs" >}}
