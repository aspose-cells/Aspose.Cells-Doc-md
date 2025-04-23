---
title: Hämta och ställ in stil för celler
description: Upptäck hur du utför dataformatering och formatering i Aspose.Cells for .NET, inklusive textformatering, nummerformatering, datumformatering och andra formateringsalternativ. Vår guide hjälper dig att skapa professionellt utseende kalkylblad med attraktiv formatering.
keywords: Aspose.Cells for .NET, dataformatering, formatering, textformatering, nummerformatering, datumformatering, formateringsalternativ, kalkylblad, attraktiv formatering, professionellt utseende.
linktitle: Stilar
type: docs
weight: 50
url: /sv/net/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells for .NET 4.4.2 införde två nya metoder för att formatera celler: Cell.GetStyle och Cell.SetStyle. Den här artikeln undersöker Cell.GetStyle/SetStyle-metoden för att hjälpa dig att bedöma vilken teknik som passar dig bäst.

{{% /alert %}} 
## **Formatering av celler**
Det finns två sätt att formatera en cell, som illustreras nedan.
### **Användning av GetStyle()**
Med följande kod styrs en Style-objekt för varje cell när den formateras. Om många celler formateras förbrukas en stor mängd minne eftersom Style-objektet är ett stort objekt. Dessa Style-objekt frigörs inte förrän Workbook.Save-metoden anropas.



**C#**

{{< highlight csharp >}}

cell.GetStyle().Font.IsBold = true;



{{< /highlight >}}
### **Användning av SetStyle()**
Det första tillvägagångssättet är enkelt och rak så varför lade vi till det andra tillvägagångssättet?

Vi lade till det andra tillvägagångssättet för att optimera minnesanvändningen. Efter att ha använt metoden Cell.GetStyle för att hämta en Style-objekt, ändra den och använd metoden Cell.SetStyle för att ställa in den tillbaka till den här cellen. Detta Style-objekt kommer inte att bevaras och .NET GC samlar in det när det inte refereras till.

När metoden Cell.SetStyle anropas sparas inte Style-objektet för varje cell. Istället jämför vi detta Style-objekt med en intern Style-objektpool för att se om det kan återanvändas. Endast Style-objekt som skiljer sig från de befintliga behålls för varje Workbook-objekt. Det innebär att det bara finns flera hundra Style-objekt för varje Excel-fil istället för tusentals. För varje cell bevaras endast en index till Style-objektpoolen.



**C#**

{{< highlight csharp >}}

Style style = cell.GetStyle();

style.Font.IsBold = true;

cell.SetStyle(style);
{{< /highlight >}}

## **Fortsatta ämnen**
- [Skapa Style-objekt med hjälp av CellsFactory-klassen](/cells/sv/net/create-style-object-using-cellsfactory-class/)
- [Modifiera en befintlig stil](/cells/sv/net/modify-an-existing-style/)
- [Återanvändning av Stilobjekt](/cells/sv/net/reusing-style-objects/)
- [Användning av inbyggda stilar](/cells/sv/net/using-built-in-styles/)


{{< app/cells/assistant language="csharp" >}}
