---
title: Lägg till eller ta bort kontextmenyobjekt i GridWeb
type: docs
weight: 130
url: /sv/net/add-or-remove-context-menu-items-in-gridweb/
---
{{% alert color="primary" %}} 

Du kan lägga till snabbmenyalternativ med ASP.NET-markering eller med .NET-koden. Du kan också ta bort snabbmenyalternativ med .NET-koden. Använd metoderna GridWeb.CustomCommandButtons.Add() och GridWeb.CustomCommandButtons.Remove() eller RemoveAt() för dessa ändamål.

{{% /alert %}} 
## **Lägg till kontextmenyobjekt med ASP.NET Markup**
Följande ASP.NET-markering lägger till ett snabbmenyalternativ i GridWeb.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem-InitContextMenuItem.aspx" >}}



Här är den fullständiga ASP.NET-markeringen som skapar en GridWeb med ovanstående snabbmeny. Observera attributet OnCustomCommand="GridWeb1_CustomCommand". Det är händelsehanterarens namn som kommer att anropas när ditt snabbmenyalternativ klickas.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem-InitContextMenuItem.aspx" >}}



Så här ser snabbmenyalternativet ut efter att ha lagts till med ovanstående ASP.NET-markering.

![todo:image_alt_text](add-or-remove-context-menu-items-in-gridweb_1.png)

Detta är händelsehanterarens kod som exekveras när du klickar på snabbmenyalternativet. Koden kontrollerar först kommandonamnet, om det matchar vårt kommando lägger den till en text i cell A1 i det aktiva GridWeb-kalkylbladet och ställer in den första kolumnbredden till 40 enheter för att göra texten synlig.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem.aspx-HandleContextMenuItemCommand.cs" >}}


Så här ser GridWeb ut när du klickar på snabbmenyn.

![todo:image_alt_text](add-or-remove-context-menu-items-in-gridweb_2.png)
## **Lägg till kontextmenyobjekt i Aspose.Cells.GridWeb med hjälp av kod**
Den här koden visar hur man lägger till ett snabbmenyobjekt i en GridWeb med hjälp av kod.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-AddContextMenuItem.cs" >}}
## **Ta bort kontextmenyobjekt i Aspose.Cells.GridWeb med hjälp av kod**
Den här koden visar hur man tar bort ett snabbmenyobjekt med metoderna CustomCommandButtons.Remove() och CustomCommandButtons.RemoveAt().



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-RemoveContextMenuItem.cs" >}}
