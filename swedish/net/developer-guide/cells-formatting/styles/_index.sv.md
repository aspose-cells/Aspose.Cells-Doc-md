---
title: Hämta och ställ in stil för celler
description: Upptäck hur du utför dataformatering och formatering i Aspose.Cells for .NET, inklusive textformatering, nummerformatering, datumformatering och andra stilalternativ. Vår guide hjälper dig att skapa professionella kalkylblad med attraktiv formatering.
keywords: Aspose.Cells for .NET, data formatting, styling, text formatting, number formatting, date formatting, styling options, spreadsheets, attractive formatting, professional-looking.
linktitle: Stilar
type: docs
weight: 50
url: /sv/net/styling-and-data-formatting/
---
{{% alert color="primary" %}} 

Aspose.Cells for .NET 4.4.2 introducerade två nya metoder för att formatera celler: Cell.GetStyle och Cell.SetStyle. Den här artikeln undersöker metoden Cell.GetStyle/SetStyle för att hjälpa dig att bedöma vilken teknik som passar dig bäst.

{{% /alert %}} 
##  **Formatering Cells**
Det finns två sätt att formatera en cell, illustreras nedan.
###  **Använda GetStyle()**
Med följande kodbit initieras ett Style-objekt för varje cell när den formateras. Om många celler formateras förbrukas en stor mängd minne eftersom Style-objektet är ett stort objekt. Dessa stilobjekt kommer inte att frigöras förrän metoden Workbook.Save anropas.



**C#**

{{< highlight "csharp" >}}

cell.GetStyle().Font.IsBold = true;



{{< /highlight >}}
###  **Använder SetStyle()**
Det första tillvägagångssättet är enkelt och okomplicerat, så varför lade vi till det andra tillvägagångssättet?

Vi lade till den andra metoden för att optimera minnesanvändningen. Efter att ha använt metoden Cell.GetStyle för att hämta ett Style-objekt, ändra det och använd metoden Cell.SetStyle för att ställa tillbaka det till den här cellen. Detta Style-objekt kommer inte att bevaras och .NET GC samlar in det när det inte refereras till det.

När du anropar metoden Cell.SetStyle sparas inte Style-objektet för varje cell. Istället jämför vi detta Style-objekt med en intern Style-objektpool för att se om det kan återanvändas. Endast stilobjekt som skiljer sig från de befintliga behålls för varje arbetsboksobjekt. Det betyder att det bara finns flera hundra Style-objekt för varje Excel-fil istället för tusentals. För varje cell bevaras endast ett index till Style-objektpoolen.



**C#**

{{< highlight "csharp" >}}

Style style = cell.GetStyle();

style.Font.IsBold = true;

cell.SetStyle(style);
{{< /highlight >}}

##  **Förhandsämnen**
- [Skapa Style-objekt med klassen CellsFactory](/cells/sv/net/create-style-object-using-cellsfactory-class/)
- [Ändra en befintlig stil](/cells/sv/net/modify-an-existing-style/)
- [Återanvända stilobjekt](/cells/sv/net/reusing-style-objects/)
- [Använda inbyggda stilar](/cells/sv/net/using-built-in-styles/)


