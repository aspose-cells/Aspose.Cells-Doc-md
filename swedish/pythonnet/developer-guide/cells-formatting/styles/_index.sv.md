---
title: Hämta och ställ in stil för celler
description: Upptäck hur du utför dataformatering och styling i Aspose.Cells för Python via .NET, inklusive textformatering, nummerformat, datumformat och andra stylingsalternativ. Vår guide hjälper dig att skapa professionella kalkylblad med attraktiv formatering.
keywords: Aspose.Cells för Python via .NET, dataformatering, styling, textformatering, nummerformat, datumformat, stylingsalternativ, kalkylblad, attraktiv formatering, professionellt utseende.
linktitle: Stilar
type: docs
weight: 50
url: /sv/python-net/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells för Python via .NET introducerade två nya metoder för cellformatering: Cell.GetStyle och Cell.SetStyle. Denna artikel granskar Cell.GetStyle/SetStyle-metoden för att hjälpa dig bedöma vilken teknik som passar dig bäst.

{{% /alert %}} 

## **Formatering av celler**
Det finns två sätt att formatera en cell, som illustreras nedan.

### **Användning av GetStyle()**
Med följande kod styrs en Style-objekt för varje cell när den formateras. Om många celler formateras förbrukas en stor mängd minne eftersom Style-objektet är ett stort objekt. Dessa Style-objekt frigörs inte förrän Workbook.Save-metoden anropas.


**Python**

{{< highlight python >}}

cell.get_style().font.is_bold = True

{{< /highlight >}}

### **Användning av SetStyle()**
Det första tillvägagångssättet är enkelt och rak så varför lade vi till det andra tillvägagångssättet?

Vi lade till det andra tillvägagångssättet för att optimera minnesanvändningen. Efter att ha använt metoden Cell.GetStyle för att hämta en Style-objekt, ändra den och använd metoden Cell.SetStyle för att ställa in den tillbaka till den här cellen. Detta Style-objekt kommer inte att bevaras och .NET GC samlar in det när det inte refereras till.

När metoden Cell.SetStyle anropas sparas inte Style-objektet för varje cell. Istället jämför vi detta Style-objekt med en intern Style-objektpool för att se om det kan återanvändas. Endast Style-objekt som skiljer sig från de befintliga behålls för varje Workbook-objekt. Det innebär att det bara finns flera hundra Style-objekt för varje Excel-fil istället för tusentals. För varje cell bevaras endast en index till Style-objektpoolen.



**Python**

{{< highlight python >}}

style = cell.get_style()
style.font.is_bold = True
cell.set_style(style)

{{< /highlight >}}

## **Fortsatta ämnen**
- [Skapa Style-objekt med hjälp av CellsFactory-klassen](/cells/sv/python-net/create-style-object-using-cellsfactory-class/)
- [Modifiera en befintlig stil](/cells/sv/python-net/modify-an-existing-style/)
- [Återanvändning av Stilobjekt](/cells/sv/python-net/reusing-style-objects/)
- [Användning av inbyggda stilar](/cells/sv/python-net/using-built-in-styles/)


{{< app/cells/assistant language="python-net" >}}
