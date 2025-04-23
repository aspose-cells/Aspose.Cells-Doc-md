---  
title: Använder LightCells API med Node.js via C++  
linktitle: Användning av LightCells API  
type: docs  
weight: 160  
url: /sv/nodejs-cpp/using-lightcells-api/  
description: Lär dig hur du läser och skriver stora Excel filer med LightCells API i Node.js via C++. Förbättra prestanda och effektivitet med mindre minnesförbrukning.  
---  

{{% alert color="primary" %}}  

Ibland behöver du läsa och skriva stora Microsoft Excel-filer med en stor lista över data eller innehåll i kalkylarket. LightCells API är användbart för att skapa stora Exceldokument: med det behöver du mindre minne och får bättre prestanda och effektivitet.  

{{% /alert %}}  
# Event Driven Architecture  
Aspose.Cells tillhandahåller LightCells API, främst utformat för att manipulera celldata en i taget utan att bygga en komplett datamodellblock (med hjälp av Cell-samlingen etc.) i minnet. Det fungerar i ett händelsestyrt läge.  

För att spara arbetsböcker, ange cellinnehållet cell för cell vid sparande, och komponenten sparar det till utdatafilen direkt.  

När du läser mallfiler parsa komponenten varje cell och tillhandahåller deras värde en i taget.  

I båda rutinerna bearbetas ett Cell-objekt och sedan kastas det; Workbook-objektet håller inte samlingen. I detta läge sparas minne när du importerar och exporterar Microsoft Excel-filer som har en stor datamängd, vilket annars skulle använda mycket minne.  

Även om LightCells API bearbetar cellerna på samma sätt för XLSX- och XLS-filer (det läser inte faktiskt in alla celler i minnet utan bearbetar en cell och kastar sedan bort den), sparar det minnet effektivare för XLSX-filer än XLS-filer på grund av de olika datamodellerna och strukturerna för de två formaten.  

Men, **för XLS-filer**, för att spara mer minne kan utvecklare ange en tillfällig plats för att spara tillfällig data som genereras under Spara-processen. Vanligtvis kan **användning av LightCells API för att spara XLSX-filer spara 50% eller mer minne** jämfört med det vanliga sättet; **att spara XLS kan spara cirka 20-40% minne**.  

## Skriver en stor Excel-fil  
Aspose.Cells erbjuder ett gränssnitt, `LightCellsDataProvider`, som måste implementeras i ditt program. Gränssnittet representerar dataleverantören för att spara stora kalkylbladsfiler i lättviktläge.  

När du sparar en arbetsbok i detta läge kontrolleras `StartSheet(int)` när varje kalkblad sparas. För ett blad, om `StartSheet(int)` är sant, tillhandahålls all data och egenskaper för rader och celler i detta blad av denna implementation. I första hand kallas `NextRow()` för att få nästa radindex att spara. Om ett giltigt radindex returneras (radindex måste vara i stigande ordning för raderna som ska sparas), tillhandahålls ett Rad-objekt för detta blad för att ställa in dess egenskaper med `StartRow(Row)`.  

För en rad kontrolleras först `NextCell()`. Om ett giltigt kolumnindex returneras (kolumnindex måste vara i stigande ordning för alla celler i en rad för att sparas), tillhandahålls ett Cell-objekt för denna cell för implementering att ställa in dess data och egenskaper med `StartCell(Cell)`. Efter att cellens data är satt sparas cellen direkt till den genererade kalkylbladsfilen och nästa cell kontrolleras och bearbetas.  
### Skriv ut en stor Excel-fil: Exempel  
Se följande exempelkod för att se arbete med LightCells API. Lägg till och ta bort eller uppdatera kodsegmenten enligt dina behov.  

Programmet skapar en enorm fil med **10 000 (10000x30 matris) poster** i ett kalkylblad och fyller dem med dummy-data. Du kan specificera din egen matris genom att ändra variablerna `rowsCount` och `colsCount` i `Main()`-metoden.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

class TestDataProvider {
constructor(workbook, maxRows, maxColumns) {
this._workbook = workbook;
this.maxRows = maxRows;
this.maxColumns = maxColumns;
this._row = -1;
this._column = -1;
}

isGatherString() {
return false;
}

nextCell() {
this._column++;
if (this._column < this.maxColumns) {
return this._column;
} else {
this._column = -1;
return -1;
}
}

nextRow() {
this._row++;
if (this._row < this.maxRows) {
this._column = -1;
return this._row;
} else {
return -1;
}
}

startCell(cell) {
cell.putValue(this._row + this._column);
if (this._row !== 1) {
cell.setFormula("=Rand() + A2");
}
}

startRow(row) {
}

startSheet(sheetIndex) {
return sheetIndex === 0;
}
}

const run = async () => {
const dataDir = path.join(__dirname, "data");

const rowsCount = 10000;
const colsCount = 30;

const workbook = new AsposeCells.Workbook();
const ooxmlSaveOptions = new AsposeCells.OoxmlSaveOptions();

ooxmlSaveOptions.setLightCellsDataProvider(new TestDataProvider(workbook, rowsCount, colsCount));

await workbook.saveAsync(path.join(dataDir, "output.out.xlsx"), ooxmlSaveOptions);
};

run();
```  

## Läs stora Excel-filer  
Aspose.Cells erbjuder ett gränssnitt, `LightCellsDataHandler`, som måste implementeras i ditt program. Gränssnittet representerar dataleverantören för att läsa stora kalkylblad i lätta lägen.  

När du läser ett arbetsblad i detta läge kontrolleras `StartSheet` när varje kalkblad läses. Om `StartSheet` returnerar sant, kontrolleras och bearbetas all data och egenskaper för cellerna i rader och kolumner på bladet av denna implementation. För varje rad kallas `StartRow` för att kontrollera om den ska bearbetas. Om en rad behöver bearbetas, läses dess egenskaper först, och utvecklaren kan komma åt dess egenskaper med `ProcessRow`. Om radernas celler också behöver bearbetas ska `ProcessRow` returnera sant, och därefter kallas `StartCell` för varje befintlig cell i raden för att kontrollera om en cell ska bearbetas. Om en cell behöver bearbetas, kallas `ProcessCell` för att bearbeta cellen av denna gränssnittsimplementation.  
### Läsa stora Excel-filer: Exempel  
Se följande exempelkod för att se arbete med LightCells API. Lägg till och ta bort eller uppdatera kodsegmenten enligt dina behov.  

Programmet läser en enorm fil med miljontals poster i ett kalkylblad. Det tar lite tid att läsa varje blad i arbetsboken. Exempel-koden läser filen och hämtar totalt antal celler, antalet strängar och formelantalet i varje kalkylblad.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

class LightCellsDataHandlerVisitCells {
constructor() {
this.cellCount = 0;
this.formulaCount = 0;
this.stringCount = 0;
}

get CellCount() {
return this.cellCount;
}

get FormulaCount() {
return this.formulaCount;
}

get StringCount() {
return this.stringCount;
}

StartSheet(sheet) {
console.log("Processing sheet[" + sheet.getName() + "]");
return true;
}

StartRow(rowIndex) {
return true;
}

ProcessRow(row) {
return true;
}

StartCell(column) {
return true;
}

ProcessCell(cell) {
this.cellCount++;
if (cell.isFormula()) {
this.formulaCount++;
} else if (cell.getType() === AsposeCells.CellValueType.IsString) {
this.stringCount++;
}
return false;
}
}

async function run() {
const dataDir = path.join(__dirname, "data");
const opts = new AsposeCells.LoadOptions();
const v = new LightCellsDataHandlerVisitCells();
opts.setLightCellsDataHandler(v);
const wb = new AsposeCells.Workbook(path.join(dataDir, "LargeBook1.xlsx"), opts);
const sheetCount = wb.getWorksheets().getCount();
console.log("Total sheets: " + sheetCount + ", cells: " + v.CellCount
+ ", strings: " + v.StringCount + ", formulas: " + v.FormulaCount);
}

run();
```  

