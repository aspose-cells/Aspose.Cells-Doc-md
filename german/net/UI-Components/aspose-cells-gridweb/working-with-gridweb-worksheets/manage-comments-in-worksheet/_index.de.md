---
title: Kommentare in Arbeitsblatt verwalten
type: docs
weight: 110
url: /de/net/aspose-cells-gridweb/manage-comment-in-worksheet/
keywords: GridWeb,comment
description: In diesem Artikel wird erläutert, wie Sie mit Kommentaren in GridWeb arbeiten.
---

{{% alert color="primary" %}} 

Dieses Thema behandelt das Hinzufügen, Zugreifen und Entfernen von Kommentaren aus Arbeitsblättern. Kommentare sind nützlich, um Notizen oder nützliche Informationen für Benutzer hinzuzufügen, die mit dem Blatt arbeiten werden. Entwickler haben die Flexibilität, Kommentare zu jeder Zelle des Arbeitsblatts hinzuzufügen.

{{% /alert %}} 
## **Arbeiten mit Kommentaren**
### **Kommentare hinzufügen**
Um einem Arbeitsblatt einen Kommentar hinzuzufügen, befolgen Sie bitte die folgenden Schritte:

1. Fügen Sie das Aspose.Cells.GridWeb-Control dem Webformular hinzu.
1. Greifen Sie auf das Arbeitsblatt zu, zu dem Sie Kommentare hinzufügen.
1. Fügen Sie einem Zelle einen Kommentar hinzu.
1. Setzen Sie eine Notiz für den neuen Kommentar.

**Ein Kommentar wurde dem Arbeitsblatt hinzugefügt** 

![todo:image_alt_text](manage-comments-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AddComments.cs" >}}
### **Zugriff auf Kommentare**
Um auf einen Kommentar zuzugreifen:

1. Greifen Sie auf die Zelle zu, die den Kommentar enthält.
1. Ermitteln Sie die Referenz der Zelle.
1. Geben Sie die Referenz an die Kommentar-Sammlung weiter, um auf den Kommentar zuzugreifen.
1. Es ist jetzt möglich, die Eigenschaften des Kommentars zu ändern.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AccessComments.cs" >}}
### **Kommentare entfernen**
Um einen Kommentar zu entfernen:

1. Greifen Sie wie oben erläutert auf die Zelle zu.
1. Verwenden Sie die RemoveAt-Methode der Kommentar-Sammlung, um den Kommentar zu entfernen.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-RemoveComments.cs" >}}
