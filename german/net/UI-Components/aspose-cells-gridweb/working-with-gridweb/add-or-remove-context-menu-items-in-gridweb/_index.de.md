---
title: Hinzufügen oder Entfernen von Kontextmenüelementen in GridWeb
type: docs
weight: 130
url: /de/net/add-or-remove-context-menu-items-in-gridweb/
---
{{% alert color="primary" %}} 

Sie können Kontextmenüelemente mit dem Markup ASP.NET oder mit dem Code .NET hinzufügen. Sie können Kontextmenüelemente auch mit dem Code .NET entfernen. Bitte verwenden Sie für diesen Zweck die Methoden GridWeb.CustomCommandButtons.Add() und GridWeb.CustomCommandButtons.Remove() oder RemoveAt().

{{% /alert %}} 
## **Kontextmenüelement mit ASP.NET-Markup hinzufügen**
Das folgende ASP.NET-Markup fügt ein Kontextmenüelement in GridWeb hinzu.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem-InitContextMenuItem.aspx" >}}



Hier ist das vollständige ASP.NET-Markup, das ein GridWeb mit dem obigen Kontextmenüelement erstellt. Bitte beachten Sie das Attribut OnCustomCommand="GridWeb1_CustomCommand". Es ist der Name des Ereignishandlers, der aufgerufen wird, wenn auf Ihr Kontextmenüelement geklickt wird.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem-InitContextMenuItem.aspx" >}}



So sieht das Kontextmenüelement aus, nachdem es mit dem obigen ASP.NET-Markup hinzugefügt wurde.

![todo: Bild_alt_Text](add-or-remove-context-menu-items-in-gridweb_1.png)

Dies ist der Event-Handler-Code, der ausgeführt wird, wenn auf das Kontextmenüelement geklickt wird. Der Code überprüft zuerst den Befehlsnamen, wenn er mit unserem Befehl übereinstimmt, fügt er einen Text in Zelle A1 des aktiven GridWeb-Arbeitsblatts hinzu und setzt die erste Spaltenbreite auf 40 Einheiten, um Text sichtbar zu machen.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem.aspx-HandleContextMenuItemCommand.cs" >}}


So sieht das GridWeb aus, wenn Sie auf den Kontextmenüpunkt klicken.

![todo: Bild_alt_Text](add-or-remove-context-menu-items-in-gridweb_2.png)
## **Fügen Sie mithilfe von Code Kontextmenüelemente in Aspose.Cells.GridWeb hinzu**
Dieser Code zeigt, wie Sie mithilfe von Code ein Kontextmenüelement in einem GridWeb hinzufügen.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-AddContextMenuItem.cs" >}}
## **Entfernen Sie Kontextmenüelemente in Aspose.Cells.GridWeb mit Code**
Dieser Code zeigt, wie ein Kontextmenüelement mithilfe der Methoden CustomCommandButtons.Remove() und CustomCommandButtons.RemoveAt() entfernt wird.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-RemoveContextMenuItem.cs" >}}
