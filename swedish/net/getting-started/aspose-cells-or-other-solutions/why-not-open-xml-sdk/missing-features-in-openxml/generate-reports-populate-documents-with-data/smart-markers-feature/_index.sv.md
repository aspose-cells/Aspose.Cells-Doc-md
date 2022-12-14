---
title: Smarta markörer finns i Aspose.Cells
type: docs
weight: 30
url: /sv/net/smart-markers-feature-in-aspose-cells/
---
**Smarta markörer** används för att låta Aspose.Cells veta vilken information som ska placeras i ett Microsoft Excel-designark. Smarta markörer låter dig skapa mallar som bara innehåller specifik information och formatering.
## **Designerkalkylblad och smarta markörer**
Designer-kalkylblad är vanliga Excel-filer som innehåller visuell formatering, formler och smarta markörer. De kan innehålla smarta markörer som refererar till en eller flera datakällor, till exempel information från ett projekt och information för relaterade kontakter. Smarta markörer skrivs in i cellerna där du vill ha informationen.

Alla smarta markörer börjar med &=. Ett exempel på en datamarkör är &=Party.FullName. Om datamarkören resulterar i mer än ett objekt, till exempel en hel rad, flyttas följande rader ned automatiskt för att göra plats för all ny information. Således kan delsummor och summor placeras på raden omedelbart efter datamarkören för att göra beräkningar baserat på infogade data. Använd dynamiska formler för att göra beräkningar på de infogade raderna.

 Smarta markörer består av**datakälla** och**fält namn**delar för mest information. Särskild information kan också skickas med variabler och variabla arrayer. Variabler fyller alltid bara en cell medan variabla arrayer kan fylla flera. Använd endast en datamarkör per cell. Oanvända smarta markörer tas bort.

Smart markör kan också innehålla parametrar. Parametrar låter dig ändra hur informationen kommer att läggas ut. De läggs till i slutet av smart markör inom parentes som en kommaseparerad lista.
### **Alternativ för smarta markörer**
- &=Datakälla.Fältnamn
- &=Datakälla.Fältnamn
- &=$Variabelnamn
- &=$VariableArray
- &==DynamicFormula
- &=&=RepeatDynamicFormula
### **Parametrar**
Följande parametrar är tillåtna:

- noadd - Lägg inte till extra rader för att passa data.
- skip:n - Hoppa över n antal rader för varje rad med data.
- stigande:n eller fallande:n - Sortera data i smarta markörer. Om n är 1, är kolumnen den första nyckeln i sorteraren. Data sorteras efter bearbetning av datakällan. T.ex. &=Tabell1.Fält3(stigande:1).
- horisontell - Skriv data från vänster till höger, istället för uppifrån och ner.
- numerisk - Konvertera text till nummer om möjligt. Stöds endast i .NET-version.
- shift - Skift ner eller höger, skapa extra rader eller kolumner för att passa data. Skiftparametern fungerar på samma sätt som i Microsoft Excel. Till exempel i MS Excel, när du markerar ett cellintervall, högerklickar du och väljer Infoga och anger flytta celler nedåt, flytta celler åt höger och andra alternativ. Kort sagt, skiftparametern fyller samma funktion för vertikala/normala (uppifrån och ned) eller horisontella (vänster till höger) smarta markörer.
- copystyle - Kopiera bascellens stil till alla celler i den kolumnen.

 Parametrarna**noadd** och hoppa över kan kombineras för att infoga data på alternerande rader. Eftersom mallen bearbetas från botten till toppen bör du lägga till noadd på första raden för att undvika att extra rader infogas före den alternativa raden.

Det här avsnittet innehåller följande ämnen

- [Gruppera data i Aspose.Cells](/cells/sv/net/grouping-data-in-aspose-cells/)
- [Bildmarkörer i Aspose.Cells](/cells/sv/net/image-markers-in-aspose-cells/)
- [Använda anonyma typer eller anpassade objekt i Aspose.Cells](/cells/sv/net/using-anonymous-types-or-custom-objects-in-aspose-cells/)
- [Använda kapslade objekt i Aspose.Cells](/cells/sv/net/using-nested-objects-in-aspose-cells/)
