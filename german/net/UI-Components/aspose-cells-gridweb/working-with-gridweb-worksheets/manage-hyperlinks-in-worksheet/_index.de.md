---
title: Hyperlinks in Arbeitsblatt verwalten
type: docs
weight: 100
url: /de/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/
keywords: GridWeb, Hyperlink
description: Dieser Artikel stellt vor, wie man mit Hyperlinks in GridWeb arbeitet.
---

{{% alert color="primary" %}} 

Dieses Thema behandelt, welche Arten von Hyperlinks von Aspose.Cells.GridWeb unterstützt werden und wie man sie programmgesteuert verwaltet. Hyperlinks können entweder zum Erstellen von Links zu Web-URLs oder zum Ausführen von Postbacks an einen Server verwendet werden.

{{% /alert %}} 
## **Arbeiten mit Hyperlinks**
### **Arten von Hyperlinks**
Im Allgemeinen werden folgende Hyperlinks von Aspose.Cells.GridWeb unterstützt:

- URL-Hyperlinks, Hyperlinks, die mit Web-URLs verknüpft werden können.
- Text-Hyperlinks, URL-Hyperlinks, die auf Text angewendet werden.
- Bild-Hyperlinks, URL-Hyperlinks, die auf Bilder angewendet werden.
- Zellbefehls-Hyperlinks, Hyperlinks, die Daten an einen Server senden. Solche Hyperlinks verhalten sich eher wie eine Schaltfläche, die bei einem Klick ein serverseitiges Ereignis auslöst.

Die folgenden Abschnitte beschreiben die Verwendung aller Arten von Hyperlinks im Detail. Es wird auch erläutert, wie man Links zugreift oder entfernt.
### **Hinzufügen von Hyperlinks**

#### **URL-Hyperlinks**
URL-Hyperlinks sehen eher wie einfache Hyperlinks aus, wie man sie normalerweise auf Websites sieht. Ein URL-Hyperlink funktioniert wie ein Anker in einer Zelle. Wenn darauf geklickt wird, navigiert er zu einer Webseite oder öffnet ein neues Browserfenster.

Es gibt verschiedene Arten von URL-Hyperlinks:

- Text-Hyperlinks.
- Bild-Hyperlinks.

Entwickler können ein Bild für den Hyperlink festlegen. Wenn kein Bild festgelegt ist, wird ein Text-Hyperlink erstellt, andernfalls ein Bild-Hyperlink.


##### **Text-Hyperlinks**
Um einen Text-Hyperlink zu einem Arbeitsblatt hinzuzufügen:

1. Fügen Sie die Aspose.Cells.GridWeb-Steuerung Ihrem Webformular hinzu.
1. Greifen Sie auf ein Arbeitsblatt zu.
1. Fügen Sie einen Hyperlink zu einer Zelle im Arbeitsblatt hinzu.
1. Legen Sie den Text fest, der in der Zelle angezeigt wird.
1. Legen Sie die URL des Hyperlinks fest.
1. Legen Sie bei Bedarf das Ziel des Hyperlinks fest.
1. Legen Sie bei Bedarf einen Tool-Tipp fest.

{{% alert color="primary" %}} 

HINWEIS: Das Hyperlink-Ziel kann auf _self, _top oder _parent gesetzt werden, um Web-URLs in einem neuen, dem aktuellen oder dem obersten Fenster zu öffnen.

{{% /alert %}} 

Im folgenden Beispiel werden zwei Hyperlinks zu einem Arbeitsblatt hinzugefügt. Einer hat kein Ziel, während der andere auf _parent gesetzt ist.

**Output: Text-Hyperlinks zum Arbeitsblatt hinzugefügt** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddTextHyperlinks.cs" >}}


##### **Bild-Hyperlinks**
Um einen Bild-Hyperlink hinzuzufügen:

1. Fügen Sie die Aspose.Cells.GridWeb-Steuerung Ihrem Webformular hinzu.
1. Greifen Sie auf ein Arbeitsblatt zu.
1. Fügen Sie einen Hyperlink zu einer Zelle hinzu.
1. Legen Sie die URL des Bildes fest, das als Hyperlink angezeigt werden soll.
1. Legen Sie die Hyperlink-URL fest.
1. Legen Sie bei Bedarf einen Tool-Tipp fest.
1. Legen Sie bei Bedarf den Hyperlink-Text fest.

**Ausgabe: Bild-Hyperlinks zum Arbeitsblatt hinzugefügt** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_2.png)

{{% alert color="primary" %}} 

Setting the image hyperlink's AltText fills a similar function as setting an <ALT> tag in HTML. The text is displayed only if the hyperlinked image is not displayed. (For example, if the image isn't at the specified location.) If the image of the second hyperlink is not found, the output of the code snippet below would look as follows.

**Das Bild für die Bild-URL konnte nicht gefunden werden** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_3.png)

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddImageHyperlinks.cs" >}}


#### **Zellenbefehl-Hyperlinks**
Ein Zellenbefehl-Hyperlink ist eine spezielle Art von Hyperlink, die anstelle einer Webseite ein serverseitiges Ereignis auslöst. Entwickler können Code zum serverseitigen Ereignis hinzufügen und jede Aufgabe ausführen, wenn auf den Hyperlink geklickt wird. Mit diesem Feature können Entwickler interaktivere Anwendungen erstellen.

Um einen Zellenbefehl-Hyperlink hinzuzufügen:

1. Fügen Sie die Aspose.Cells.GridWeb-Steuerung Ihrem Webformular hinzu.
1. Greifen Sie auf ein Arbeitsblatt zu.
1. Fügen Sie einen Hyperlink zu einer Zelle hinzu.
1. Legen Sie den Befehl des Hyperlinks auf einen beliebigen Wert fest.
   Der Wert wird vom Ereignisverarbeiter des Hyperlinks verwendet, um ihn zu erkennen.
1. Legen Sie bei Bedarf einen Tool-Tipp fest.
1. Legen Sie die URL für das Bild fest, das als Hyperlink angezeigt wird.

**Ein Zellenbefehls-Hyperlink wurde zum Arbeitsblatt hinzugefügt** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddCellCommandHyperlinks.cs" >}}
##### **Ereignisbehandlung von Zellenbefehls-Hyperlinks**
Entwickler müssen einen Ereignishandler für das CellCommand-Ereignis des GridWeb-Steuerelements erstellen, um bestimmte Aufgaben auszuführen, wenn auf einen bestimmten Zellenbefehls-Hyperlink geklickt wird. Der Ereignishandler des CellCommand-Ereignisses stellt ein Objekt vom Typ CellEventArgs bereit, das die Argument-Eigenschaft bietet. Verwenden Sie die Argument-Eigenschaft, um einen bestimmten Hyperlink anhand seines CellCommand-Werts zu identifizieren.

Das folgende Beispiel erstellt einen Ereignishandler für den Zellenbefehls-Hyperlink, der im obigen Code erstellt wurde. Der CellCommand des Hyperlinks wurde auf Klick setzen. Überprüfen Sie daher im Ereignishandler zuerst den Hyperlink und fügen Sie dann den Code hinzu, der eine Nachricht in der Zelle A6 anzeigt.

Der Ereignishandler wird aufgerufen, wenn auf den Hyperlink geklickt wird.

**Ausgabe: Text wird zur Zelle A6 hinzugefügt, wenn auf den Hyperlink geklickt wird** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_5.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-HandleCellCommandHyperlinkEvent.cs" >}}
### **Zugriff auf Hyperlinks**
Um auf einen vorhandenen Hyperlink zuzugreifen:

1. Greifen Sie auf die Zelle zu, die ihn enthält.
2. Erhalten Sie die Zellreferenz.
3. Übergeben Sie die Referenz an die GetHyperlink-Methode der Hyperlinks-Sammlung, um auf den Hyperlink zuzugreifen.
4. Ändern Sie die Eigenschaften des Hyperlinks.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-AccessHyperlinks.cs" >}}
### **Hyperlinks entfernen**
Um einen Hyperlink zu entfernen:

1. Greifen Sie auf das aktive Arbeitsblatt zu.
2. Entfernen Sie einen Hyperlink mithilfe der Remove-Methode der Hyperlinks-Sammlung.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-RemoveHyperlink.cs" >}}
