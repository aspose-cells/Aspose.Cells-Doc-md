---
title: Hyperlinks im Arbeitsblatt verwalten
type: docs
weight: 100
url: /de/net/manage-hyperlinks-in-worksheet/
---
{{% alert color="primary" %}} 

In diesem Thema wird erläutert, welche Arten von Hyperlinks in Aspose.Cells.GridWeb unterstützt werden und wie sie programmgesteuert verwaltet werden. Hyperlinks können entweder zum Erstellen von Links zu Web-URLs oder zum Durchführen von Postbacks zu einem Server verwendet werden.

{{% /alert %}} 
## **Arbeiten mit Hyperlinks**
### **Arten von Hyperlinks**
Im Allgemeinen werden die folgenden Hyperlinks von Aspose.Cells.GridWeb unterstützt:

- [URL-Hyperlinks](/cells/de/net/manage-hyperlinks-in-worksheet/), Hyperlinks, die mit Web-URLs verknüpft werden können.
- [Text-Hyperlinks](/cells/de/net/manage-hyperlinks-in-worksheet/), auf Text angewendete URL-Hyperlinks.
- [Bild-Hyperlinks](/cells/de/net/manage-hyperlinks-in-worksheet/), auf Bilder angewendete URL-Hyperlinks.
- [Cell Befehls-Hyperlinks](/cells/de/net/manage-hyperlinks-in-worksheet/), Hyperlinks, die Daten an einen Server senden. Solche Hyperlinks verhalten sich eher wie eine Schaltfläche, die beim Klicken ein serverseitiges Ereignis auslöst.

In den folgenden Abschnitten wird die Verwendung aller Arten von Hyperlinks im Detail beschrieben. Außerdem wird erläutert, wie auf Links zugegriffen oder diese entfernt werden.
### **Hinzufügen von Hyperlinks**

#### **URL-Hyperlinks**
URL-Hyperlinks sehen eher wie einfache Hyperlinks aus, die Sie normalerweise auf Websites sehen. Ein URL-Hyperlink funktioniert wie ein Anker in einer Zelle. Immer wenn es angeklickt wird, navigiert es zu einer Webseite oder öffnet ein neues Browserfenster.

Es gibt verschiedene Arten von URL-Hyperlinks:

- Text-Hyperlinks.
- Bild-Hyperlinks.

Entwickler können ein Bild für den Hyperlink angeben. Wenn kein Bild angegeben ist, wird ein Text-Hyperlink erstellt; andernfalls wird ein Bild-Hyperlink erstellt.


##### **Text-Hyperlinks**
So fügen Sie einem Arbeitsblatt einen Text-Hyperlink hinzu:

1. Fügen Sie Ihrem Webformular das Steuerelement Aspose.Cells.GridWeb hinzu.
1. Greifen Sie auf ein Arbeitsblatt zu.
1. Fügen Sie einer Zelle im Arbeitsblatt einen Hyperlink hinzu.
1. Legen Sie den Text fest, der in der Zelle angezeigt wird.
1. Legen Sie die URL des Hyperlinks fest.
1. Legen Sie bei Bedarf das Ziel des Hyperlinks fest.
1. Legen Sie bei Bedarf eine QuickInfo fest.

{{% alert color="primary" %}} 

 HINWEIS: Das Hyperlink-Ziel kann auf eingestellt werden_ selbst,_top oder _parent zum Öffnen von Web-URLs in einem neuen, aktuellen oder obersten Fenster.

{{% /alert %}} 

Im folgenden Beispiel werden einem Arbeitsblatt zwei Hyperlinks hinzugefügt. Einer hat kein Ziel, während der andere auf _parent gesetzt ist.

**Ausgabe: Text-Hyperlinks, die dem Arbeitsblatt hinzugefügt wurden** 

![todo: Bild_alt_Text](manage-hyperlinks-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddTextHyperlinks.cs" >}}


##### **Bild-Hyperlinks**
So fügen Sie einen Bild-Hyperlink hinzu:

1. Fügen Sie Ihrem Webformular das Steuerelement Aspose.Cells.GridWeb hinzu.
1. Greifen Sie auf ein Arbeitsblatt zu.
1. Fügen Sie einer Zelle einen Hyperlink hinzu.
1. Legen Sie die URL des Bildes fest, das als Hyperlink angezeigt wird.
1. Legen Sie die Hyperlink-URL fest.
1. Legen Sie bei Bedarf eine QuickInfo fest.
1. Legen Sie bei Bedarf den Hyperlink-Text fest.

**Ausgabe: Bild-Hyperlinks zum Arbeitsblatt hinzugefügt** 

![todo: Bild_alt_Text](manage-hyperlinks-in-worksheet_2.png)

{{% alert color="primary" %}} 

 Das Festlegen des AltText des Bild-Hyperlinks erfüllt eine ähnliche Funktion wie das Festlegen von an<ALT> -Tag im HTML-Format. Der Text wird nur angezeigt, wenn das verlinkte Bild nicht angezeigt wird. (Beispielsweise, wenn sich das Bild nicht an der angegebenen Position befindet.) Wenn das Bild des zweiten Hyperlinks nicht gefunden wird, würde die Ausgabe des folgenden Codeausschnitts wie folgt aussehen.

**Das Bild für die Bild-URL konnte nicht gefunden werden** 

![todo: Bild_alt_Text](manage-hyperlinks-in-worksheet_3.png)

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddImageHyperlinks.cs" >}}


#### **Cell Befehls-Hyperlinks**
Ein Zellenbefehls-Hyperlink ist eine spezielle Art von Hyperlink, der ein serverseitiges Ereignis auslöst, anstatt eine Webseite zu öffnen. Entwickler können dem serverseitigen Ereignis Code hinzufügen und jede Aufgabe ausführen, wenn auf den Hyperlink geklickt wird. Diese Funktion ermöglicht es Entwicklern, interaktivere Anwendungen zu erstellen.

So fügen Sie einen Zellbefehl-Hyperlink hinzu:

1. Fügen Sie Ihrem Webformular das Steuerelement Aspose.Cells.GridWeb hinzu.
1. Greifen Sie auf ein Arbeitsblatt zu.
1. Fügen Sie einer Zelle einen Hyperlink hinzu.
1. Setzen Sie den Befehl des Hyperlinks auf einen beliebigen gewünschten Wert.
 Der Wert wird vom Ereignishandler des Hyperlinks verwendet, um ihn zu erkennen.
1. Legen Sie bei Bedarf eine QuickInfo fest.
1. Legen Sie die URL für das Bild fest, das als Hyperlink angezeigt wird.

**Dem Arbeitsblatt wurde ein Zellenbefehls-Hyperlink hinzugefügt** 

![todo: Bild_alt_Text](manage-hyperlinks-in-worksheet_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddCellCommandHyperlinks.cs" >}}
##### **Ereignisbehandlung von Cell-Befehls-Hyperlinks**
Entwickler müssen einen Ereignishandler für das CellCommand-Ereignis des GridWeb-Steuerelements erstellen, um bestimmte Aufgaben auszuführen, wenn auf einen bestimmten Zellenbefehls-Hyperlink geklickt wird. Die Ereignisbehandlungsroutine des CellCommand-Ereignisses stellt ein Objekt vom Typ CellEventArgs bereit, das die Argument-Eigenschaft bereitstellt. Verwenden Sie die Argument-Eigenschaft, um einen bestimmten Hyperlink zu identifizieren, indem Sie seinen CellCommand-Wert vergleichen.

Das folgende Beispiel erstellt einen Ereignishandler für den im obigen Code erstellten Zellenbefehls-Hyperlink. Der CellCommand des Hyperlinks wurde auf Click festgelegt. Überprüfen Sie es also im Ereignishandler zuerst und fügen Sie dann Code hinzu, der eine Nachricht in der A6-Zelle anzeigt.

Der Ereignishandler wird aufgerufen, wenn auf den Hyperlink geklickt wird.

**Ausgabe: Text, der der A6-Zelle hinzugefügt wird, wenn auf den Hyperlink geklickt wird** 

![todo: Bild_alt_Text](manage-hyperlinks-in-worksheet_5.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-HandleCellCommandHyperlinkEvent.cs" >}}
### **Zugriff auf Hyperlinks**
So greifen Sie auf einen vorhandenen Hyperlink zu:

1. Greifen Sie auf die Zelle zu, die es enthält.
1. Holen Sie sich den Zellbezug.
1. Übergeben Sie den Verweis an die GetHyperlink-Methode der Hyperlinks-Auflistung, um auf den Hyperlink zuzugreifen.
1. Ändern Sie die Eigenschaften des Hyperlinks.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-AccessHyperlinks.cs" >}}
### **Entfernen von Hyperlinks**
So entfernen Sie einen Hyperlink:

1. Greifen Sie auf das aktive Arbeitsblatt zu.
1. Entfernen Sie einen Hyperlink mit der Remove-Methode der Hyperlinks-Auflistung.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-RemoveHyperlink.cs" >}}
