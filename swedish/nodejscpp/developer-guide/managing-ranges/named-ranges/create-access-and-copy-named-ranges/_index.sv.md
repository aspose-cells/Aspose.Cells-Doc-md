---  
title: Skapa åtkomst och kopiera namngivna områden med Node.js via C++  
linktitle: Skapa åtkomst och kopiera namngivna intervall  
type: docs  
weight: 200  
url: /sv/nodejs-cpp/create-access-and-copy-named-ranges/  
description: Lär dig hur du skapar, får åtkomst till och kopierar namngivna områden i Excel med Aspose.Cells for Node.js via C++.  
---  

## **Introduktion**  

Vanligtvis används kolumn- och radetiketter för att referera till enskilda celler. Det är möjligt att skapa beskrivande namn för att representera celler, områden av celler, formler eller konstanter. Ordet **namn** kan referera till en sträng av tecken som representerar en cell, ett område av celler, en formel eller ett konstant värde. Att tilldela ett namn till ett område betyder att detta område kan refereras till med dess namn. Använd lättförståeliga namn, som Produkter, för att referera till svårförståeliga områden, som Försäljning!C20:C30. Etiketterna kan användas i formler som hänvisar till data på samma kalkylblad; vill du representera ett område på ett annat kalkylblad kan du använda ett namn. *Namngivna områden är en av de mäktigaste funktionerna i Microsoft Excel, särskilt när de används som datakälla för listkontroller, pivottabeller, diagram och liknande.*  

## **Arbeta med namngivet intervall med Microsoft Excel**  

### **Skapa namngivna intervall**  

Följande steg beskriver hur du namnger en cell eller ett cellområde med **MS Excel**. Denna metod gäller för **Microsoft Office Excel 2003**, **Microsoft Excel 97**, **2000** och **2002**.  

1. Välj den cell eller det cellområde som du vill namnge.  
2. Klicka på **Namnrutan** till vänster om formelfältet.  
3. Skriv in namnet för cellerna.  
4. Tryck på ENTER.  

{{% alert color="primary" %}}  
Du kan inte namnge en cell medan du ändrar innehållet i cellen.  
{{% /alert %}}  

## **Arbeta med namngivna områden med hjälp av Aspose.Cells**  

Här använder vi Aspose.Cells API för att utföra uppgiften.  
Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-klassen innehåller en [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-samling som möjliggör åtkomst till varje kalkylblad i en Excel-fil. Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen tillhandahåller en [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samling.  

### **Skapa namngivet område**  

Det är möjligt att skapa ett namngivet område genom att anropa den överlagrade metoden [**createRange(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) i samlingen [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). En vanlig version av [**createRange(string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-)-metoden tar följande parametrar:  

- Namn på övre vänstra cell, namnet på den översta vänstra cellen i området.  
- Namnet på den nedre högra cellen, namnet på den längst ner till höger i området.  

När metoden [**createRange(string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-) kallas returneras det nysskapade området som en instans av klassen [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range). Använd detta [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range)-objekt för att konfigurera det namngivna området. Till exempel, ställ in namnet på området med hjälp av egenskapen [**getName()**](https://reference.aspose.com/cells/nodejs-cpp/range/#getName--). Följande exempel visar hur man skapar ett namngivet område av celler som sträcker sig över B4:G14.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Creating a named range
const range = worksheet.getCells().createRange("B4", "G14");

// Setting the name of the named range
range.setName("TestRange");

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

### **Ange data i cellerna i det namngivna området**  

Du kan sätta in data i de individuella cellerna i ett område enligt mönstret  

- **JavaScript**: Range[row,column]  

Säg att du har ett namngivet område av celler som sträcker sig över A1:C4. Matrisen skapar 4 * 3 = 12 celler. De individuella områdets celler är arrangerade sekventiellt: Range[0,0], Range[0,1], Range[0,2], Range[1,0], Range[1,1], Range[1,2], Range[2,0], Range[2,1], Range[2,2], Range[3,0], Range[3,1], Range[3,2].  

Använd följande egenskaper för att identifiera cellerna i området:  

- firstRow returnerar indexen för den första raden i det namngivna området.  
- firstColumn returnerar indexen för den första kolumnen i det namngivna området.  
- rowCount returnerar det totala antalet rader i det namngivna området.  
- columnCount returnerar det totala antalet kolumner i det namngivna området.  

Följande exempel visar hur man anger några värden i cellerna i ett specificerat område.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet in the workbook.
const worksheet1 = workbook.getWorksheets().get(0);

// Create a range of cells based on H1:J4.
const range = worksheet1.getCells().createRange("H1", "J4");

// Name the range.
range.setName("MyRange");

// Input some data into cells in the range.
range.get(0, 0).setValue("USA");
range.get(0, 1).setValue("SA");
range.get(0, 2).setValue("Israel");
range.get(1, 0).setValue("UK");
range.get(1, 1).setValue("AUS");
range.get(1, 2).setValue("Canada");
range.get(2, 0).setValue("France");
range.get(2, 1).setValue("India");
range.get(2, 2).setValue("Egypt");
range.get(3, 0).setValue("China");
range.get(3, 1).setValue("Philipine");
range.get(3, 2).setValue("Brazil");

// Save the excel file.
workbook.save(path.join(dataDir, "rangecells.out.xls"));
```  

### **Identifiera celler i det namngivna området**  

Du kan sätta in data i de individuella cellerna i ett område enligt mönstret:  

- **JavaScript**: Range[row,column]  

Om du har ett namngivet område som sträcker sig över A1:C4. Matrisen skapar 4 * 3 = 12 celler. De individuella områdets celler är arrangerade sekventiellt: Range[0,0], Range[0,1], Range[0,2], Range[1,0] ,Range[1,1], Range[1,2], Range[2,0], Range[2,1], Range[2,2], Range[3,0], Range[3,1], Range[3,2].  

Använd följande egenskaper för att identifiera cellerna i området:  

- firstRow returnerar indexen för den första raden i det namngivna området.  
- firstColumn returnerar indexen för den första kolumnen i det namngivna området.  
- rowCount returnerar det totala antalet rader i det namngivna området.  
- columnCount returnerar det totala antalet kolumner i det namngivna området.  

Följande exempel visar hur man anger några värden i cellerna i ett specificerat område.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1_testrange.xls"));

// Getting the specified named range
const range = workbook.getWorksheets().getRangeByName("TestRange");

// Identify range cells.
console.log("First Row : " + range.getFirstRow());
console.log("First Column : " + range.getFirstColumn());
console.log("Row Count : " + range.getRowCount());
console.log("Column Count : " + range.getColumnCount());
```  

### **Åtkomst till namngivna områden**  

#### **Åtkomst till ett specifikt namngivet område**  

Anropa [**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection)-kollektionens [**getRangeByName(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getRangeByName-string-)-metod för att få ett område med det angivna namnet. En typisk [**getRangeByName(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getRangeByName-string-)-metod tar namnet på det namngivna området och returnerar det angivna namngivna området som en instans av klassen [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range). Följande exempel visar hur man åtkommer ett angivet område med dess namn.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1_testrange.xls"));

// Getting the specified named range
const range = workbook.getWorksheets().getRangeByName("TestRange");

if (range !== null) 
{
console.log("Named Range : " + range.getRefersTo());
}
```  

#### **Åtkomst till alla namngivna områden i ett kalkylblad**  

Anropa [**worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) samlingens [**getNamedRanges()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getNamedRanges--) metod för att få alla namngivna områden i ett kalkylblad. [**getNamedRanges()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getNamedRanges--) metoden returnerar en array av alla namngivna områden i [**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) samlingen.  

Följande exempel visar hur man åtkommer alla namngivna områden i en arbetsbok.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Getting all named ranges
const ranges = workbook.getWorksheets().getNamedRanges();

if (ranges != null) {
console.log("Total Number of Named Ranges: " + ranges.length);
}
```  

### **Kopiera namngivna områden**  

Aspose.Cells tillhandahåller [**range.copy(Range, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/range/#copy-range-pasteoptions-)-metoden för att kopiera ett cellområde med formatering till ett annat område.  

Följande exempel visar hur man kopierar en källräcka med celler till ett annat namngivet område.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Get the first worksheet in the worksheets collection.
const worksheet = workbook.getWorksheets().get(0);

// Create a range of cells.
const range1 = worksheet.getCells().createRange("E12", "I12");

// Name the range.
range1.setName("MyRange");

// Set the outline border to the range.
range1.setOutlineBorder(AsposeCells.BorderType.TopBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.BottomBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.LeftBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.RightBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));

// Input some data with some formattings into
// A few cells in the range.
range1.get(0, 0).putValue("Test");
range1.get(0, 4).putValue("123");

// Create another range of cells.
const range2 = worksheet.getCells().createRange("B3", "F3");

// Name the range.
range2.setName("testrange");

// Copy the first range into second range.
range2.copy(range1);

// Save the excel file.
workbook.save(path.join(dataDir, "copyranges.out.xls"));
```  

