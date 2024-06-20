---
title: Skydda rader och kolumner
type: docs
weight: 60
url: /sv/net/aspose-cells-gridweb/protect-rows-and-columns/
keywords: GridWeb, skydda
description: I den här artikeln introduceras hur man skyddar rader och kolumner i GridWeb.
---

{{% alert color="primary" %}} 

I detta avsnitt diskuteras olika tekniker för att skydda celler i rader och kolumner från användaråtgärder. Utvecklare kan genomföra detta skydd med hjälp av två tekniker: genom att göra celler i rader och kolumner skrivskyddade eller genom att begränsa Aspose.Cells.GridWeb's kontextmenyalternativ. Båda dessa tekniker diskuteras nedan med hjälp av exempel.

{{% /alert %}} 
## **Skydda celler i rader och kolumner**
### **Gör rader och kolumner skrivskyddade**
Ett sätt att skydda rader och kolumner i ett kalkylblad är att göra cellerna skrivskyddade. Då kan de inte tas bort av användarna.

För att göra rader och kolumner skrivskyddade:

1. Lägg till Aspose.Cells.GridWeb-kontrollen i en webbformulär.
1. Få åtkomst till GridWorksheet i samlingen.
1. Ange de önskade cellerna i rader eller kolumner som skrivskyddade.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-MakeRowsColumnsReadOnly.aspx-MakeCellReadOnly.cs" >}}
### **Begränsa alternativen i kontextmenyn**
Aspose.Cells.GridWeb tillhandahåller en kontextmeny som slutanvändare kan använda för att utföra operationer på kontrollen. Menyn erbjuder många alternativ för att manipulera celler, rader och kolumner.

**Fullständiga kontextuella alternativ** 

![todo:image_alt_text](protect-rows-and-columns_1.png)

Det är möjligt att begränsa alla typer av klientoperations på rader och kolumner genom att begränsa alternativen som finns tillgängliga i kontextmenyn. Det kan göras genom att ställa in EnableClientColumnOperations och EnableClientRowOperations egenskaperna för GridWeb-kontrollen till false. Det är också möjligt att begränsa användare från att frysa rader och kolumner genom att ställa in EnableClientFreeze egenskapen hos GridWeb-kontrollen till false.

**Kontextmeny efter begränsning av alternativ för rad och kolumn** 

![todo:image_alt_text](protect-rows-and-columns_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-RestrictContextMenu.aspx-RestrictContextMenu.cs" >}}
