---
title: GridDesktops-Kontextmenü verwalten
type: docs
weight: 40
url: /de/net/managing-griddesktops-context-menu/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop verfügt über ein Kontextmenü mit allen häufig verwendeten Befehlen. Mit dem Steuerelement können Sie Menüelemente ein-/ausblenden. Außerdem ist es möglich, dem Menü neue Menüpunkte mit Eventhandlern hinzuzufügen.

{{% /alert %}} 
## **Einführung**
Die ContextMenuManager-Klasse wird verwendet, um die Kontextmenüelemente zu verwalten. Das GridDesktop.ContextMenuManager-Attribut ruft die Instanz des ContextMenuManager-Objekts ab. Beispielsweise erhält oder legt das Attribut ContextMenuManager.MenuItemAvailable_Copy einen Wert fest, der angibt, ob das Kontextmenüelement **Kopieren** verfügbar ist oder nicht. Ebenso haben wir alle entsprechenden Attribute für verschiedene Kontextmenüelemente.

**WICHTIG:** Standardmäßig sind alle Kontextmenüpunkte in der Liste sichtbar.
## **Verwalten des Kontextmenüs**
### **Ausblenden von Kontextmenüelementen**
Um diese Aufgabe auszuführen, werfen wir zunächst einen Blick auf das standardmäßige Kontextmenü des GridDesktop.

**Das Standardmenü von GridDeskop** 

![todo: Bild_alt_Text](managing-griddesktops-context-menu_1.png)

Blenden Sie nun einige Menüpunkte mit dem folgenden Code aus:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-HideContextMenuItem.cs" >}}



Nach dem Ausführen des obigen Codes sind einige Menüpunkte für die Benutzer nicht sichtbar:

**Einige Menüpunkte sind ausgeblendet** 

![todo: Bild_alt_Text](managing-griddesktops-context-menu_2.png)
### **Neue Menüpunkte hinzufügen**
Fügen Sie der Liste mithilfe des folgenden Codeausschnitts ein neues Kontextmenüelement hinzu.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-AddContextMenuItem.cs" >}}


Wir spezifizieren auch einen Event-Handler für den neuen Befehl/die neue Option.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-EventHandler.cs" >}}



Nach Ausführung des obigen Codes ist im Kontextmenü ein neuer Menüpunkt zu sehen. Eine Meldung wird auch angezeigt, wenn auf die Zelle geklickt wird.

**Der Liste wird ein neuer Menüpunkt hinzugefügt** 

![todo: Bild_alt_Text](managing-griddesktops-context-menu_3.png)
