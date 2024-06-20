---
title: Arbetar med GridWeb dubbelklickshändelser
type: docs
weight: 80
url: /sv/net/aspose-cells-gridweb/gridweb-double-click-event/
keywords: GridWeb, dubbelklick, klickhändelse, händelse
description: Den här artikeln introducerar hur man använder dubbelklickshändelsen i GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb innehåller tre typer av dubbelklickshändelser:

- CellDoubleClick, aktiveras när en cell dubbelklickas.
- ColumnDoubleClick, aktiveras när en kolumnrubrik dubbelklickas.
- RowDoubleClick, aktiveras när en radrubrik dubbelklickas.

Detta ämne diskuterar hur man aktiverar dubbelklickshändelser i Aspose.Cells.GridWeb. Det diskuterar också skapandet av händelsehanterare för dessa händelser.

{{% /alert %}} 
## **Aktivera dubbelklickshändelser**
Alla typer av dubbelklickshändelser kan aktiveras på klientens sida genom att ställa in Egenskapen EnableDoubleClickEvent för GridWeb-kontrollen till true.

{{% alert color="primary" %}} 

Som standard är Egenskapen EnableDoubleClickEvent inställd på false. Detta innebär att dubbelklickshändelser inte är aktiverade som standard. För att implementera sådana händelser, aktivera funktionen först.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-EnableDoubleClickEvents.cs" >}}



När dubbelklickshändelser är aktiverade, är det möjligt att skapa händelsehanterare för vilka dubbelklickshändelser som helst. Dessa händelsehanterare utför specifika uppgifter när en given dubbelklickshändelse inträffar.
## **Hantering av dubbelklickshändelser**
För att skapa en händelsehanterare i Visual Studio:

1. Dubbelklicka på en händelse i **Händelser** listan i Egenskapsrutan.

För detta exempel implementerade vi händelsehanterare för olika dubbelklickshändelser.
### **Dubbelklick på cell**
Händelsehanteraren för CellDoubleClick-händelsen tillhandahåller en argument av typen CellEventArgs, som ger all information om cellen som dubbelklickades på.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-CellDoubleClickEvent.cs" >}}
### **Dubbelklick på kolumnrubrik**
Händelsehanteraren för ColumnDoubleClick-händelsen tillhandahåller ett argument av typen RowColumnEventArgs som ger indexnumret för kolumnen för rubriken som dubbelklickades på och annan information.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-ColumnDoubleClickEvent.cs" >}}
### **Dubbelklick på radrubrik**
Händelsehanteraren för RowDoubleClick-händelsen tillhandahåller ett argument av typen RowColumnEventArgs som ger indexnumret för raden för rubriken som dubbelklickades på och annan relaterad information.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-RowDoubleClickEvent.cs" >}}
