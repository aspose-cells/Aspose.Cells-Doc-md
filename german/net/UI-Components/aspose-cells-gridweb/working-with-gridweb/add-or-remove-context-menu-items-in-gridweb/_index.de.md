---
title: Kontextmenü Elemente in GridWeb hinzufügen oder entfernen
type: docs
weight: 130
url: /de/net/aspose-cells-gridweb/add-or-remove-context-menu-items-in-gridweb/
keywords: GridWeb, kontextmenü, menü
description: Dieser Artikel zeigt, wie Kontextmenü Elemente in GridWeb hinzugefügt oder entfernt werden können.
---

{{% alert color="primary" %}} 

Sie können Kontextmenü-Elemente mit ASP.NET-Markup oder mit dem .NET-Code hinzufügen. Sie können auch Kontextmenü-Elemente mit dem .NET-Code entfernen. Verwenden Sie für diesen Zweck die Methoden GridWeb.CustomCommandButtons.Add() und GridWeb.CustomCommandButtons.Remove() oder RemoveAt().

{{% /alert %}} 
## **Kontextmenü-Element mit ASP.NET-Markup hinzufügen**
Der folgende ASP.NET-Markup fügt ein Kontextmenü-Element in GridWeb hinzu.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem-InitContextMenuItem.aspx" >}}



Hier ist der vollständige ASP.NET-Markup, der einen GridWeb mit dem oben genannten Kontextmenü-Element erstellt. Bitte beachten Sie das Attribut OnCustomCommand="GridWeb1_CustomCommand". Es ist der Ereignishandlername, der aufgerufen wird, wenn Ihr Kontextmenü-Element angeklickt wird.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem-InitContextMenuItem.aspx" >}}



So sieht das Kontextmenü-Element aus, nachdem es mit dem obigen ASP.NET-Markup hinzugefügt wurde.

![todo:image_alt_text](add-or-remove-context-menu-items-in-gridweb_1.png)

Dies ist der Ereignishandlercode, der ausgeführt wird, wenn das Kontextmenü-Element angeklickt wird. Der Code überprüft zuerst den Befehlsnamen, und wenn er unserem Befehl entspricht, fügt er einen Text in Zelle A1 des aktiven GridWeb-Arbeitsblatts hinzu und setzt die Breite der ersten Spalte auf 40 Einheiten, um den Text sichtbar zu machen.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem.aspx-HandleContextMenuItemCommand.cs" >}}


So sieht der GridWeb aus, wenn Sie auf das Kontextmenü-Element klicken.

![todo:image_alt_text](add-or-remove-context-menu-items-in-gridweb_2.png)
## **Kontextmenü-Elemente in Aspose.Cells.GridWeb mit Code hinzufügen**
Dieser Code zeigt, wie ein Kontextmenü-Element innerhalb eines GridWeb mit Code hinzugefügt wird.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-AddContextMenuItem.cs" >}}
## **Kontextmenü-Elemente in Aspose.Cells.GridWeb mit Code entfernen**
Dieser Code zeigt, wie ein Kontextmenü-Element mithilfe der Methoden CustomCommandButtons.Remove() und CustomCommandButtons.RemoveAt() entfernt wird.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-RemoveContextMenuItem.cs" >}}
