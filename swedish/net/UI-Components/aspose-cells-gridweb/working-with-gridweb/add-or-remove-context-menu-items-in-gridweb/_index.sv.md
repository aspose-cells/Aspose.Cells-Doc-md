---
title: Lägg till eller ta bort element i kontextmenyn i GridWeb
type: docs
weight: 130
url: /sv/net/aspose-cells-gridweb/add-or-remove-context-menu-items-in-gridweb/
keywords: GridWeb, kontextmeny, meny
description: I den här artikeln beskrivs hur man lägger till eller tar bort element i kontextmenyn i GridWeb.
---

{{% alert color="primary" %}} 

Du kan lägga till element i kontextmenyn med ASP.NET-markering eller med .NET-kod. Du kan också ta bort element från kontextmenyn med .NET-kod. Använd GridWeb.CustomCommandButtons.Add() och GridWeb.CustomCommandButtons.Remove() eller RemoveAt() metoder för detta ändamål.

{{% /alert %}} 
## **Lägg till element i kontextmenyn med hjälp av ASP.NET-markeringen**
Följande ASP.NET-markering lägger till element i kontextmenyn i GridWeb.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem-InitContextMenuItem.aspx" >}}



Här är den kompletta ASP.NET-markeringen som skapar en GridWeb med ovanstående kontextmeny. Observera attributet OnCustomCommand="GridWeb1_CustomCommand". Det är händelsehanterarnamnet som kommer att kallas när ditt kontextmenyobjekt klickas.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem-InitContextMenuItem.aspx" >}}



Så här ser kontextmenyn ut efter att den har lagts till med ovanstående ASP.NET-markering.

![todo:image_alt_text](add-or-remove-context-menu-items-in-gridweb_1.png)

Detta är händelsehanterarkoden som körs när kontextmenyn klickas. Koden kontrollerar först kommandonamnet, om det matchar vårt kommando lägger den till en text i cell A1 på aktiv GridWeb-arbetsblad och ställer in den första kolumnens bredd till 40 enheter så att texten blir synlig.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem.aspx-HandleContextMenuItemCommand.cs" >}}


Så här ser GridWeb ut när du klickar på kontextmenyn.

![todo:image_alt_text](add-or-remove-context-menu-items-in-gridweb_2.png)
## **Lägg till element i kontextmenyn i Aspose.Cells.GridWeb med hjälp av kod**
Den här koden visar hur du lägger till element i kontextmenyn inne i en GridWeb med hjälp av kod.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-AddContextMenuItem.cs" >}}
## **Ta bort element från kontextmenyn i Aspose.Cells.GridWeb med hjälp av kod**
Den här koden visar hur du tar bort element från kontextmenyn med hjälp av CustomCommandButtons.Remove() och CustomCommandButtons.RemoveAt() metoder.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-RemoveContextMenuItem.cs" >}}
