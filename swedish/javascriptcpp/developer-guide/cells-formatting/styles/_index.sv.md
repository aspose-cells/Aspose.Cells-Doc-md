---
title: Hämta och ställ in stil för celler
description: Upptäck hur man utför datanformatering och styling i Aspose.Cells for JavaScript via C++, inklusive textformatering, nummerformat, datumformat och andra stylingalternativ. Vår guide hjälper dig att skapa professionella kalkylblad med attraktiva format.
keywords: Aspose.Cells for JavaScript via C++, datanformatering, styling, textformatering, nummerformat, datumformat, stylingalternativ, kalkylblad, attraktiv formatering, professionellt utseende.
linktitle: Stilar
type: docs
weight: 50
url: /sv/javascript-cpp/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells for JavaScript via C++ introducerade två nya metoder för formatering av celler: Cell.style och Cell.style. Den här artikeln undersöker Cell.style/stil-metoden för att hjälpa dig att bedöma vilken teknik som passar dig bäst.

{{% /alert %}} 
## **Formatering av celler**
Det finns två sätt att formatera en cell, som illustreras nedan.
### **Använda stil**
Med följande kod initieras ett Style-objekt för varje cell vid formatering. Om många celler formateras används mycket minne eftersom Style-objektet är stort. Dessa Style-objekt kommer inte att frigöras förrän Workbook.save-metoden anropas.

**JavaScript**

{{< highlight javascript >}}
cell.style.font.isBold = true;
{{< /highlight >}}
### **Använda stil**
Det första tillvägagångssättet är enkelt och rak så varför lade vi till det andra tillvägagångssättet?

Vi lade till det andra tillvägagångssättet för att optimera minnesanvändningen. Efter att ha använt egenskapen Cell.style för att hämta ett Style-objekt, modifiera det och tilldela det tillbaka med egenskapen Cell.style till denna cell. Detta Style-objekt kommer inte att bevaras och JavaScript:s garbage collector kommer att samla in det när det inte längre refereras.

När du tilldelar egenskapen Cell.style sparas inte Style-objektet för varje cell. Istället jämförs detta Style-objekt med en intern Style-objektpool för att se om det kan återanvändas. Endast Style-objekt som skiljer sig från de befintliga behålls för varje arbetsboksobjekt. Detta innebär att det finns bara några hundra Style-objekt för varje Excel-fil i stället för tusentals. För varje cell bevaras endast en index till Style-objektpoolen.

**JavaScript**

{{< highlight javascript >}}
let style = cell.style;

style.font.isBold = true;

cell.style = style;
{{< /highlight >}}

## **Fortsatta ämnen**
- [Skapa Style-objekt med hjälp av CellsFactory-klassen](/cells/sv/javascript-cpp/create-style-object-using-cellsfactory-class/)
- [Modifiera en befintlig stil](/cells/sv/javascript-cpp/modify-an-existing-style/)
- [Återanvändning av Stilobjekt](/cells/sv/javascript-cpp/reusing-style-objects/)
- [Användning av inbyggda stilar](/cells/sv/javascript-cpp/using-built-in-styles/)
