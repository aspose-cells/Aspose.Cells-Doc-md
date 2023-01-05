---
title: Kommentare im Arbeitsblatt verwalten
type: docs
weight: 110
url: /de/net/manage-comments-in-worksheet/
---
{{% alert color="primary" %}} 

In diesem Thema wird das Hinzufügen von, Zugreifen auf und Entfernen von Kommentaren aus Arbeitsblättern erläutert. Kommentare sind nützlich, um Notizen oder nützliche Informationen für Benutzer hinzuzufügen, die mit dem Blatt arbeiten werden. Entwickler haben die Flexibilität, jeder Zelle des Arbeitsblatts Kommentare hinzuzufügen.

{{% /alert %}} 
## **Arbeiten mit Kommentaren**
### **Kommentare hinzufügen**
Um einen Kommentar zum Arbeitsblatt hinzuzufügen, führen Sie bitte die folgenden Schritte aus:

1. Fügen Sie dem Webformular das Steuerelement Aspose.Cells.GridWeb hinzu.
1. Greifen Sie auf das Arbeitsblatt zu, dem Sie Kommentare hinzufügen.
1. Fügen Sie einer Zelle einen Kommentar hinzu.
1. Legen Sie eine Notiz für den neuen Kommentar fest.

**Dem Arbeitsblatt wurde ein Kommentar hinzugefügt** 

![todo: Bild_alt_Text](manage-comments-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AddComments.cs" >}}
### **Zugriff auf Kommentare**
So greifen Sie auf einen Kommentar zu:

1. Greifen Sie auf die Zelle zu, die den Kommentar enthält.
1. Holen Sie sich die Referenz der Zelle.
1. Übergeben Sie den Verweis auf die Kommentarsammlung, um auf den Kommentar zuzugreifen.
1. Es ist jetzt möglich, die Eigenschaften des Kommentars zu ändern.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AccessComments.cs" >}}
### **Kommentare entfernen**
So entfernen Sie einen Kommentar:

1. Greifen Sie wie oben beschrieben auf die Zelle zu.
1. Verwenden Sie die RemoveAt-Methode der Comment-Auflistung, um den Kommentar zu entfernen.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-RemoveComments.cs" >}}
