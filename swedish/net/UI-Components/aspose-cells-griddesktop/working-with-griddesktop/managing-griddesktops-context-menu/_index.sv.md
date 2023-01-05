---
title: Hantera GridDesktops kontextmeny
type: docs
weight: 40
url: /sv/net/managing-griddesktops-context-menu/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop har en snabbmeny som har alla vanliga kommandon. Kontrollen låter dig dölja/visa menyalternativ. Dessutom är det möjligt att lägga till nya menyalternativ med händelsehanterare till menyn.

{{% /alert %}} 
## **Introduktion**
Klassen ContextMenuManager används för att hantera snabbmenyalternativen. GridDesktop.ContextMenuManager-attributet hämtar instansen av ContextMenuManager-objektet. Till exempel får eller ställer attributet ContextMenuManager.MenuItemAvailable_Copy ett värde som anger om snabbmenyalternativet **Copy** är tillgängligt eller inte. På samma sätt har vi alla motsvarande attribut för olika kontextmenyalternativ.

**VIKTIG:** Som standard är alla snabbmenyalternativ synliga i listan.
## **Hantera snabbmenyn**
### **Döljer kontextmenyobjekt**
För att utföra denna uppgift tar vi först en titt på standardkontextmenyn som GridDesktop har.

**GridDeskops standardmeny** 

![todo:image_alt_text](managing-griddesktops-context-menu_1.png)

Göm nu några menyalternativ med koden nedan:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-HideContextMenuItem.cs" >}}



Efter att ha kört ovanstående kod kommer vissa menyalternativ inte att vara synliga för användarna:

**Vissa menyalternativ är dolda** 

![todo:image_alt_text](managing-griddesktops-context-menu_2.png)
### **Lägga till nya menyalternativ**
Lägg till ett nytt snabbmenyobjekt till listan med hjälp av följande kodavsnitt.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-AddContextMenuItem.cs" >}}


Vi anger också en händelsehanterare för det nya kommandot/alternativet.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-EventHandler.cs" >}}



Efter exekvering av ovanstående kod kan ett nytt menyalternativ ses i snabbmenyn. Ett meddelande visas också när cellen klickas.

**Ett nytt menyalternativ läggs till i listan** 

![todo:image_alt_text](managing-griddesktops-context-menu_3.png)
