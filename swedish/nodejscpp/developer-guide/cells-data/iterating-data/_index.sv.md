---  
title: Hur och Var man använder Enumerator med Node.js via C++  
linktitle: Iterera data  
type: docs  
weight: 55  
url: /sv/nodejs-cpp/how-and-where-to-use-enumerators/  
description: Lär dig hur man använder Enumerator genom Aspose.Cells for Node.js via C++ API.  
keywords: Hur man använder Enumerator Node.js via C++, Cells Enumerator Node.js via C++, Rows Enumerator Node.js via C++, Columns Enumerator Node.js via C++  
---  

{{% alert color="primary" %}}  

En enumerator är ett objekt som ger möjlighet att traversera en behållare eller en samling. Enumerators kan användas för att läsa data i samlingen, men kan inte användas för att ändra den underliggande samlingen, medan Array är ett gränssnitt som definierar en metod `getEnumerator` som returnerar ett `IEnumerator`-gränssnitt, vilket i sin tur möjliggör endast läsaccess till en samling.  

Aspose.Cells API:er tillhandahåller ett gäng enumeratörer, denna artikel diskuterar huvudsakligen de tre typerna som listas nedan.  

1. Cells Enumerator  
1. Rows Enumerator  
1. Kolumnenummer  

{{% /alert %}}  

## **Hur man använder Enumerators**  

### **Cellers Enumerator**  

Det finns olika sätt att komma åt Celler Enumerator, och man kan använda någon av dessa metoder baserat på programkraven. Här är metoderna som returnerar cellerna Enumerator.  

1. [**Cells.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getEnumerator--)  
1. [**Row.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getEnumerator--)  
1. [**Range.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/range/#getEnumerator--)  

Alla ovan nämnda metoder returnerar enumeratorn som tillåter att traversera samlingen av celler som har initierats.  

{{% alert color="primary" %}}  

När man traverserar cellerna ska samlingen inte modifieras (operationer som kommer att orsaka en ny cell att instansieras eller befintlig cell att ta bort). Annars kanske inte Enumeratorn kan traversera alla celler korrekt (vissa element kan traverseras upprepade gånger eller hoppas över).  

{{% /alert %}}  

Följande kodexempel visar implementeringen av `IEnumerator`-gränssnittet för en Cells-samling.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const cells = workbook.getWorksheets().get(0).getCells().getEnumerator();
for (const cell of cells) {
console.log(`${cell.getName()} ${cell.getValue()}`);
}

const rowCells = workbook.getWorksheets().get(0).getCells().getRows().get(0).getEnumerator();
for (const cell of rowCells) {
console.log(`${cell.getName()} ${cell.getValue()}`);
}

const rangeCells = workbook.getWorksheets().get(0).getCells().createRange("A1:B10").getEnumerator();
for (const cell of rangeCells) {
console.log(`${cell.getName()} ${cell.getValue()}`);
}
```  

### **Radenummerator**  

Rows-Enumerator kan nås medan du använder [**RowCollection.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection/#getEnumerator--)-metoden. Följande kodexempel visar implementeringen av `IEnumerator`-gränssnittet för [**RowCollection**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get RowCollection and iterate using index
const rows = workbook.getWorksheets().get(0).getCells().getRows();
const rowCount = rows.getCount();

// Traverse rows in the collection
for (let i = 0; i < rowCount; i++) {
const row = rows.get(i);
console.log(row.getIndex());
}
```  

### **Kolumnenummerator**  

Columns-Enumerator kan nås medan du använder [**ColumnCollection.getEnumerator**](https://reference.aspose.com/cells/nodejs-cpp/columncollection)-metoden. Följande kodexempel visar implementeringen av `IEnumerator`-gränssnittet för [**ColumnCollection**](https://reference.aspose.com/cells/nodejs-cpp/columncollection).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get columns collection
const columns = workbook.getWorksheets().get(0).getCells().getColumns();
// Traverse columns using index
const count = columns.getCount();
for (let i = 0; i < count; i++) {
const col = columns.get(i);
console.log(col.getIndex());
}
```  

## **Var man ska använda Enumerators**  

För att diskutera fördelarna med att använda uppräknare, låt oss ta ett exempel i realtid.  

**Scenario**  

En applikationskrav är att traversera alla celler i en given [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) för att läsa deras värden. Det kan finnas flera sätt att implementera detta mål. Några demonstreras nedan.  

### **Användning av Display Range**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get Cells collection of first worksheet
const cells = workbook.getWorksheets().get(0).getCells();

// Get the MaxDisplayRange
const displayRange = cells.getMaxDisplayRange();

// Loop over all cells in the MaxDisplayRange
for (let row = displayRange.getFirstRow(); row < displayRange.getRowCount(); row++) {
for (let col = displayRange.getFirstColumn(); col < displayRange.getColumnCount(); col++) {
// Read the Cell value
console.log(displayRange.get(row, col).getStringValue());
}
}
```  

### **Användning av MaxDataRow & MaxDataColumn**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get Cells collection of first worksheet
const cells2 = workbook.getWorksheets().get(0).getCells();
const maxDataRow = cells2.getMaxDataRow();
const maxDataColumn = cells2.getMaxDataColumn();

// Loop over all cells
for (let row = 0; row <= maxDataRow; row++) {
for (let col = 0; col <= maxDataColumn; col++) {
// Read the Cell value
const currentCell = cells2.checkCell(row, col);
if (currentCell) {
console.log(currentCell.getStringValue());
}
}
}
```  

Som du kan observera använder båda ovan nämnda tillvägagångssätten mer eller mindre liknande logik, det vill säga; loopa över alla celler i samlingen för att läsa cellvärdena. Detta kan vara problematiskt av flera skäl som diskuteras nedan.  

1. API:er som [**getMaxRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxRow--), [**getMaxDataRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataRow--), [**getMaxColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxColumn--), [**getMaxDataColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataColumn--) & [**getMaxDisplayRange()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDisplayRange--) kräver extra tid för att samla in motsvarande statistik. Om datamatrisen (rader x kolumner) är stor, kan användning av dessa API:er innebära en prestandaböter.  
1. I de flesta fall är inte alla celler i en given omfattning instansierade. I sådana situationer är det inte så effektivt att kontrollera varje cell i matrisen jämfört med att bara kontrollera de initierade cellerna.  
1. Åtkomst av en cell i en loop som Celler rad, kolumn kommer att orsaka att alla cellobjekt i ett område instansieras, vilket så småningom kan orsaka OutOfMemoryException.  

## **Slutsats**  

Baserat på ovan nämnda fakta är följande möjliga scenarier där enumerators bör användas.  

1. Endast läsåtkomst av cellsamlingen krävs, dvs. kravet är att endast inspektera cellerna.  
1. Ett stort antal celler ska traverseras.  
1. Endast initialiserade celler/rader/kolumner ska traverseras.  

