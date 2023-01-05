---
title: Skydda rader och kolumner
type: docs
weight: 60
url: /sv/net/protect-rows-and-columns/
---
{{% alert color="primary" %}} 

Det här ämnet diskuterar några tekniker för att skydda celler i rader och kolumner från alla typer av åtgärder som utförs av slutanvändare. Utvecklare kan implementera detta skydd med två tekniker: genom att göra celler i rader och kolumner läsbara eller genom att begränsa Aspose.Cells.GridWebs snabbmenyalternativ. Båda dessa tekniker diskuteras nedan med hjälp av exempel.

{{% /alert %}} 
## **Skyddar Cells i rader och kolumner**
### **Gör rader och kolumner skrivskyddade**
Ett sätt att skydda rader och kolumner i ett kalkylblad är att göra cellerna läsbara. Då kan de inte raderas av slutanvändare.

Så här gör du rader och kolumner läsbara:

1. Lägg till Aspose.Cells.GridWeb-kontrollen till ett webbformulär.
1. Öppna GridWorksheet i samlingen.
1. Ställ in önskade celler i rader eller kolumner för att endast läsas.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-MakeRowsColumnsReadOnly.aspx-MakeCellReadOnly.cs" >}}
### **Begränsa kontextmenyalternativ**
Aspose.Cells.GridWeb tillhandahåller en snabbmeny som slutanvändare kan använda för att utföra operationer på kontrollen. Menyn innehåller många alternativ för att manipulera celler, rader och kolumner.

**Komplettera kontextuella alternativ** 

![todo:image_alt_text](protect-rows-and-columns_1.png)

Det är möjligt att begränsa alla typer av operationer på klientsidan på rader och kolumner genom att begränsa de tillgängliga alternativen i snabbmenyn. Det kan göras genom att ställa in egenskaperna EnableClientColumnOperations och EnableClientRowOperations för GridWeb-kontrollen till false. Det är också möjligt att begränsa användare från att frysa rader och kolumner genom att ställa in GridWeb-kontrollens EnableClientFreeze-egenskap till false.

**Snabbmeny efter begränsning av rad- och kolumnalternativ** 

![todo:image_alt_text](protect-rows-and-columns_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-RestrictContextMenu.aspx-RestrictContextMenu.cs" >}}
