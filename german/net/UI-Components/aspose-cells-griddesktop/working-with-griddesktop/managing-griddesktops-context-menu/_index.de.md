---
title: Verwaltung des Kontextmenüs von GridDesktop
type: docs
weight: 40
url: /de/net/aspose-cells-griddesktop/manage-griddesktops-context-menu/
keywords: GridDesktop, Kontext, Kontextmenü
description: Dieser Artikel zeigt, wie das Kontextmenü im GridDesktop angepasst werden kann.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop verfügt über ein Kontextmenü mit allen gängigen Befehlen. Die Steuerung ermöglicht es, Menüpunkte auszublenden/einzublenden. Darüber hinaus ist es möglich, neue Menüpunkte mit Ereignishandlern zum Menü hinzuzufügen.

{{% /alert %}} 
## **Einführung**
Die Klasse ContextMenuManager wird verwendet, um die Kontextmenüpunkte zu verwalten. Das Attribut GridDesktop.ContextMenuManager erhält die Instanz des Objekts ContextMenuManager. Zum Beispiel wird das Attribut ContextMenuManager.MenuItemAvailable_Copy verwendet, um den Wert zu erhalten oder festzulegen, ob der Kontextmenüpunkt **Kopieren** verfügbar ist oder nicht. Ebenso haben wir entsprechende Attribute für verschiedene Kontextmenüpunkte.

**WICHTIG:** Standardmäßig sind alle Kontextmenüpunkte in der Liste sichtbar.
## **Verwaltung des Kontextmenüs**
### **Ausblenden von Kontextmenüpunkten**
Um diese Aufgabe auszuführen, werfen wir zuerst einen Blick auf das Standardkontextmenü des GridDesktop.

**Standardmenü des GridDeskop** 

![todo:image_alt_text](managing-griddesktops-context-menu_1.png)

Jetzt einige Menüpunkte mithilfe des folgenden Codes ausblenden:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-HideContextMenuItem.cs" >}}



Nach Ausführung des obigen Codes werden einige Menüpunkte für die Benutzer nicht sichtbar sein:

**Einige Menüpunkte sind ausgeblendet** 

![todo:image_alt_text](managing-griddesktops-context-menu_2.png)
### **Hinzufügen neuer Menüpunkte**
Fügen Sie mithilfe des folgenden Code-Snippets einen neuen Kontextmenüpunkt zur Liste hinzu.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-AddContextMenuItem.cs" >}}


Wir geben auch einen Ereignishandler für den neuen Befehl/Option an.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-EventHandler.cs" >}}



Nach Ausführung des obigen Codes wird ein neuer Menüpunkt im Kontextmenü zu sehen sein. Es wird auch eine Nachricht erscheinen, wenn eine Zelle geklickt wird.

**Ein neuer Menüpunkt wurde der Liste hinzugefügt** 

![todo:image_alt_text](managing-griddesktops-context-menu_3.png)
