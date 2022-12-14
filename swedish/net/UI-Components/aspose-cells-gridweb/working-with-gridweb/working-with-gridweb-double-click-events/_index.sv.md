---
title: Arbeta med GridWeb Double Click Events
type: docs
weight: 80
url: /sv/net/working-with-gridweb-double-click-events/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb innehåller tre typer av dubbelklickshändelser:

- CellDoubleClick, aktiveras när en cell dubbelklickas.
- ColumnDoubleClick, aktiveras när en kolumnrubrik dubbelklickas.
- RowDoubleClick, aktiveras när en radrubrik dubbelklickas.

Det här ämnet diskuterar hur du aktiverar dubbelklickshändelser i Aspose.Cells.GridWeb. Den diskuterar också att skapa händelsehanterare för dessa händelser.

{{% /alert %}} 
## **Aktiverar dubbelklickshändelser**
Alla typer av dubbelklickshändelser kan aktiveras på klientsidan genom att ställa in GridWeb-kontrollens EnableDoubleClickEvent-egenskap till true.

{{% alert color="primary" %}} 

Som standard är egenskapen EnableDoubleClickEvent inställd på false. Detta betyder att dubbelklickshändelser inte är aktiverade som standard. För att implementera sådana händelser, aktivera först funktionen.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-EnableDoubleClickEvents.cs" >}}



När dubbelklickshändelser är aktiverade är det möjligt att skapa händelsehanterare för alla dubbelklickshändelser. Dessa händelsehanterare utför specifika uppgifter när en given dubbelklickshändelse utlöses.
## **Hantera dubbelklickshändelser**
Så här skapar du en händelsehanterare i Visual Studio:

1.  Dubbelklicka på en händelse i**evenemang** lista i rutan Egenskaper.

För det här exemplet implementerade vi händelsehanterare för olika dubbelklickshändelser.
### **Dubbelklicka Cell**
Händelsehanteraren för händelsen CellDoubleClick tillhandahåller ett argument av typen CellEventArgs, som tillhandahåller fullständig information om cellen som dubbelklickas.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-CellDoubleClickEvent.cs" >}}
### **Dubbelklicka på kolumnrubrik**
Händelsehanteraren för ColumnDoubleClick-händelsen tillhandahåller ett argument av typen RowColumnEventArgs som ger indexnumret för kolumnen för rubriken som dubbelklickades och annan information.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-ColumnDoubleClickEvent.cs" >}}
### **Dubbelklicka på radrubrik**
Händelsehanteraren för händelsen RowDoubleClick tillhandahåller ett argument av typen RowColumnEventArgs som ger indexnumret för raden för rubriken som dubbelklickades och annan relaterad information.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-RowDoubleClickEvent.cs" >}}
