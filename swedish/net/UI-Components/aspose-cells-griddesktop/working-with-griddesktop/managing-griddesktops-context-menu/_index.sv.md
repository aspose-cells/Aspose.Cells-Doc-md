---
title: Hantera GridDesktops kontextmeny
type: docs
weight: 40
url: /sv/net/aspose-cells-griddesktop/manage-griddesktops-context-menu/
keywords: GridDesktop,kontext,kontextmeny
description: Den här artikeln introducerar hur man anpassar kontextmenyn i GridDesktop.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop har en kontextmeny som innehåller alla de vanligt använda kommandona. Kontrollen låter dig dölja/visa menyobjekt. Dessutom är det möjligt att lägga till nya menyobjekt med händelsehanterare till menyn.

{{% /alert %}} 
## **Introduktion**
Klassen ContextMenuManager används för att hantera kontextmenyobjekten. Attributet GridDesktop.ContextMenuManager hämtar instansen av objektet ContextMenuManager. Till exempel hämtar eller sätter attributet ContextMenuManager.MenuItemAvailable_Copy ett värde som indikerar om kontextmenyobjektet Kopiera är tillgängligt eller inte. På samma sätt har vi alla motsvarande attribut för olika kontextmenyobjekt.

**VIKTIGT:** Som standard är alla kontextmenyobjekten synliga i listan.
## **Hantera kontextmenyn**
### **Dölja kontextmenyobjekt**
För att utföra denna uppgift tittar vi först på den standards kontextmeny som GridDesktop har.

**GridDesktops standardmeny** 

![todo:image_alt_text](managing-griddesktops-context-menu_1.png)

Nu, dölj några menyobjekt med hjälp av koden nedan:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-HideContextMenuItem.cs" >}}



Efter att ovanstående kod har exekverats kommer vissa menyobjekt inte att vara synliga för användarna:

**Några menyobjekt är dolda** 

![todo:image_alt_text](managing-griddesktops-context-menu_2.png)
### **Lägga till nya menyobjekt**
Lägg till ett nytt kontextmenyobjekt i listan med hjälp av följande kodsnutt.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-AddContextMenuItem.cs" >}}


Vi specificerar också en händelsehanterare för den nya kommandot/alternativet.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-EventHandler.cs" >}}



Efter att ovanstående kod har exekverats kan ett nytt menyobjekt ses i kontextmenyn. Ett meddelande kommer också att visas när cellen klickas.

**En ny menyföremål läggs till i listan** 

![todo:image_alt_text](managing-griddesktops-context-menu_3.png)
