---
title: Föregångare och beroenden med Node.js via C++
linktitle: Precedenser och beroende
type: docs
weight: 230
url: /sv/nodejs-cpp/precedents-and-dependents/
description: Lär dig spåra föregångare och beroende celler i kalkylblad med Aspose.Cells for Node.js via C++. Förstå hur man identifierar länkade celler i komplexa finansiella kalkylblad.
---

{{% alert color="primary" %}} 

Komplexa finansiella arbetsblad, särskilt de som utvecklats i samarbete, kan dölja de mest pinsamma felen. Att kontrollera formler för noggrannhet och hitta felets källa kan vara svårt när formeln använder precedens- och beroendeceller.

{{% /alert %}} 
## **Introduktion**
- **Precedensceller** är celler som hänvisas till av en formel i en annan cell. Till exempel, om cell D10 innehåller formeln =B5, är cell B5 en precedens till cell D10.
- **Beroende celler** innehåller formler som hänvisar till andra celler. Till exempel, om cell D10 innehåller formeln =B5, är D10 beroende av cell B5.

För att göra kalkylarket lättläst vill du kanske tydligt visa vilka celler på ett kalkylblad som används i en formel. På liknande sätt kan du vilja extrahera de beroende cellerna för andra celler.

Aspose.Cells låter dig spåra celler och ta reda på vilka som är länkade.
## **Spåra precedens- och beroendeceller: Microsoft Excel**
Formler kan ändras baserat på ändringar som görs av en klient. Till exempel, om cell C1 är beroende av C3 och C4 som innehåller en formel, och C1 ändras (så formeln åsidosätts), måste C3 och C4, eller andra celler, ändras för att balansera kalkylarket baserat på affärsregler.

På liknande sätt, anta att C1 innehåller formeln "=(B1*22)/(M2*N32)". Jag vill hitta de celler som C1 är beroende av, dvs. precedenscellerna B1, M2 och N32.

Du kan behöva spåra beroendet för en specifik cell till andra celler. Om affärsregler är inbäddade i formler vill vi ta reda på beroendet och utföra några regler baserat på det. På liknande sätt, om värdet på en specifik cell ändras, vilka celler i arbetsbladet påverkas av den ändringen?

Microsoft Excel tillåter användare att spåra precedenser och beroenden.

1. På **Visa verktygsfältet**, välj **Formelgranskning**. Dialogrutan för formelgranskning visas.
1. Spåra Precedenser:
   1. Välj den cell som innehåller formeln för vilken du vill hitta precedensceller.
   1. För att visa en spårpil till varje cell som direkt tillhandahåller data till den aktiva cellen, klicka på **Spåra Precedenser** på verktygsfältet för formelgranskning.
1. Spåra formler som refererar till en specifik cell (beroenden)
   1. Välj den cell för vilken du vill identifiera de beroende cellerna.
   1. För att visa en spårarepil till varje cell som är beroende av den aktiva cellen, klicka på **Trace Dependents** på Formulaspårningsverktygsfältet.
## **Spårar föregående och beroende celler: Aspose.Cells**
### **Spårar föregående**
Aspose.Cells gör det enkelt att få föregående celler. Den kan inte bara hämta celler som ger data till enkla formelföregångare utan också hitta celler som ger data till komplexa formelföregångare med namngivna områden.

I exemplet nedan används en template excelfil, Book1.xls. Kalkylarket har data och formler på den första arbetsbladet.

Aspose.Cells tillhandahåller klassen [Cell](https://reference.aspose.com/cells/nodejs-cpp/cell)s metod [Cell.getPrecedents()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getPrecedents--) som används för att spåra en cell's föregångare. Det returnerar en samling av refererade områden. Som du kan se ovan, i Book1.xls, innehåller cell B7 formeln "=SUM(A1:A3)". Så cellerna A1:A3 är föregångare till cell B7. Följande exempel demonstrerar funktionaliteten för att spåra föregångare med mallfilen Book1.xls.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const cells = workbook.getWorksheets().get(0).getCells();
const cell = cells.get("B4");
// Check if the cell object is not null before proceeding
if (cell) 
{
const ret = cell.getPrecedents();
if (!ret.isNull() && ret.getCount() > 0)
{
const area = ret.get(0);
console.log(area.getSheetName());
console.log(AsposeCells.CellsHelper.cellIndexToName(area.getStartRow(), area.getStartColumn()));
console.log(AsposeCells.CellsHelper.cellIndexToName(area.getEndRow(), area.getEndColumn()));
}
else
{
console.error("No precedents found for the cell.");
}
} 
else 
{
console.error("Cell B4 is null.");
}
```
### **Spårar beroende**
Aspose.Cells låter dig få beroende celler i kalkylblad. Aspose.Cells kan inte bara hämta celler som tillhandahåller data för en enkel formel utan också hitta celler som tillhandahåller data till komplexa formelberoenden med namngivna områden.

Aspose.Cells tillhandahåller klassen [Cell](https://reference.aspose.com/cells/nodejs-cpp/cell)s metod [Cell.getDependents(boolean)](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDependents-boolean-) som används för att spåra en cell's beroende. Till exempel, i Book1.xlsx finns formler: "=A1+20" och "=A1+30" i cellerna B2 och C2 respektive. Följande exempel visar hur man spårar beroenden för cellen A1 med hjälp av mallfilen Book1.xlsx.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const cells = workbook.getWorksheets().get(0).getCells();
const cell = cells.get("B2");
// Ensure dependents is an array
const dependents = cell.getDependents(true);

if (Array.isArray(dependents)) 
{
for (const c of dependents) 
{
console.log(c.getName());
}
} 
else 
{
console.error("Dependents is not an array");
}
```
### **Spårning av föregående och beroende celler enligt beräkningskedjan**
De ovan nämnda API:erna för att spåra föregångare och beroenden är baserade på formeluttrycket i sig. De ger en enkel metod för att spåra interdependenser för några få formler. Om det finns ett stort antal formler i arbetsboken och användaren behöver spåra föregångare och beroenden för varje cell, kommer prestandan att bli dålig. För en sådan situation bör användaren överväga att använda [Cell.getPrecedentsInCalculation()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getPrecedentsInCalculation--) och [Cell.getDependentsInCalculation(boolean)](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDependentsInCalculation-boolean-) metoder. Dessa två metoder spårar beroenden enligt beräkningskedjan. För att använda dem, måste du först aktivera beräkningskedjan med [FormulaSettings.getEnableCalculationChain()](https://reference.aspose.com/cells/nodejs-cpp/formulasettings/#getEnableCalculationChain--) och sedan utföra fullständig beräkning av arbetsboken med [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--). Därefter kan du spåra föregångare eller beroenden för alla dessa celler du behöver.

För vissa formler kan de resulterande föregångarna vara olika för getPrecedents och getPrecedentsInCalculation, och de resulterande beroendena kan vara olika för getDependents och getDependentsInCalculation. Till exempel, om cell A1:s formel är "=IF(TRUE,B2,C3)", kommer getPrecedents att ge B2 och C3 som A1:s föregångare. Dessutom, B2 och C3 har båda beroendet A1 när man kontrollerar med getDependents. Men för beräkningen av denna formel är det tydligt att endast B2 kan påverka det beräknade resultatet. Så getPrecedentsInCalculation kommer inte att ge C3 för A1, och getDependentsInCalculation kommer inte att ge A1 för C3. Ibland kan användare bara ha behov av att spåra de interdependenser som faktiskt påverkar det beräknade resultatet av formler baserat på den aktuella data i arbetsboken, då måste de också använda getDependentsInCalculation/getPrecedentsInCalculation istället för getDependents/getPrecedents.

Följande exempel visar hur man spårar föregångare och beroenden enligt beräkningskedjan för celler:


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const cells = workbook.getWorksheets().get(0).getCells();
cells.get("A1").setFormula("=B1+SUM(B1:B10)+[Book1.xls]Sheet1!B2");
cells.get("A2").setFormula("=IF(TRUE,B2,B1)");
workbook.getSettings().getFormulaSettings().setEnableCalculationChain(true);
workbook.calculateFormula();

let en = cells.get("B1").getDependentsInCalculation(false);
console.log("B1's calculation dependents:");
for (var cell of en) {
console.log(cell.getName());
}


en = cells.get("B2").getDependentsInCalculation(false);
console.log("B2's calculation dependents:");
for (var cell of en) {
console.log(cell.getName());
}

en = cells.get("A1").getPrecedentsInCalculation();
console.log("A1's calculation precedents:");
for (var area of en) {
console.log(area.toString());
}


en = cells.get("A2").getPrecedentsInCalculation();
console.log("A2's calculation precedents:");
for (var area of en) {
console.log(area.toString());
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
