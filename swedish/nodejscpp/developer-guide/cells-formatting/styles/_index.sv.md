---
title: Hämta och ställ in stil för celler
description: Upptäck hur du utför datumbertering och styling i Aspose.Cells for Node.js via C++, inklusive textformatering, nummerformat, datumformat och andra stylingalternativ. Vår guide hjälper dig att skapa professionella kalkylblad med attraktiv formatering.
keywords: Aspose.Cells for Node.js via C++, datumbertering, styling, textformatering, nummerformat, datumformat, stylingalternativ, kalkylblad, attraktiv formatering, professionellt utseende.
linktitle: Stilar
type: docs
weight: 50
url: /sv/nodejs-cpp/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells for Node.js via C++ introducerade två nya metoder för att formatera celler: Cell.getStyle och Cell.setStyle. Denna artikel undersöker Cell.getStyle/setStyle-ansatsen för att hjälpa dig att bedöma vilken teknik som passar dig bäst.

{{% /alert %}} 
## **Formatering av celler**
Det finns två sätt att formatera en cell, som illustreras nedan.
### **Användning av getStyle()**
Med följande kod initieras ett Style-objekt för varje cell vid formatering. Om många celler formateras används mycket minne eftersom Style-objektet är stort. Dessa Style-objekt kommer inte att frigöras förrän Workbook.save-metoden anropas.

**JavaScript**

{{< highlight javascript >}}
cell.getStyle().getFont().setIsBold(true);
{{< /highlight >}}
### **Användning av setStyle()**
Det första tillvägagångssättet är enkelt och rak så varför lade vi till det andra tillvägagångssättet?

Vi lade till ett andra tillvägagångssätt för att optimera minnesanvändningen. Efter att ha hämtat ett Style-objekt med Cell.getStyle-metoden, ändra det och använd Cell.setStyle-metoden för att tilldela det till denna cell. Detta Style-objekt kommer inte att bevaras och JavaScripts garbage collector kommer att samla in det när det inte längre används.

När Cell.setStyle-metoden anropas sparas inte Style-objektet för varje cell. Istället jämförs detta Style-objekt med en intern Style-objektpool för att se om det kan återanvändas. Endast Style-objekt som skiljer sig från de befintliga behålls för varje Workbook-objekt. Detta innebär att det finns bara några hundra Style-objekt för varje Excel-fil istället för tusentals. För varje cell bevaras endast ett index till Style-objektpoolen.

**JavaScript**

{{< highlight javascript >}}
let style = cell.getStyle();

style.getFont().setIsBold(true);

cell.setStyle(style);
{{< /highlight >}}

## **Fortsatta ämnen**
- [Skapa Style-objekt med hjälp av CellsFactory-klassen](/cells/sv/nodejs-cpp/create-style-object-using-cellsfactory-class/)
- [Modifiera en befintlig stil](/cells/sv/nodejs-cpp/modify-an-existing-style/)
- [Återanvändning av Stilobjekt](/cells/sv/nodejs-cpp/reusing-style-objects/)
- [Användning av inbyggda stilar](/cells/sv/nodejs-cpp/using-built-in-styles/)

