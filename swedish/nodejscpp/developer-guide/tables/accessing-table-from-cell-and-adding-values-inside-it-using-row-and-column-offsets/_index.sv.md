---  
title: Åtkomst till tabell från cell och tillägg av värden inuti med hjälp av rad och kolumnförskjutningar med Node.js via C++  
linktitle: Få åtkomst till tabell från cell och lägg till värden inuti den med hjälp av rad och kolumnförflyttningar  
type: docs  
weight: 230  
url: /sv/nodejs-cpp/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/  
---  

{{% alert color="primary" %}}  

Normalt sett lägger du till värden inuti tabellen eller listobjektet med hjälp av [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-)-metoden. Men ibland kan du behöva lägga till värden inuti tabellen eller listobjektet med rad- och kolumnförflyttningar.  

För att komma åt tabell eller lista objekt från en cell, använd [**Cell.getTable()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getTable--)-metoden. För att lägga till värden inuti den med hjälp av rad- och kolumnförskjutningar, använd [**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#putCellValue-number-number-object-)-metoden.  

{{% /alert %}}  

Följande skärmbild visar käll-Excel-filen som används i koden. Den innehåller den tomma tabellen och markerar cell D5 som ligger inuti tabellen. Vi kommer att komma åt denna tabell från cell D5 med hjälp av [**Cell.getTable()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getTable--)-metoden och sedan lägga till värden inuti den med hjälp av både [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) och [**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#putCellValue-number-number-object-)-metoder.  

## Exempel  

### Skärmbilder som jämför käll- och utdatafiler  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|  
| :- |  

Följande skärmbild visar den genererade utdata-Excel-filen av koden. Som du kan se har cellen D5 ett värde och cellen F6, som ligger vid förflyttning 2,2 inuti tabellen, har ett värde.  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|  
| :- |  

### Node.js-kod för att komma åt tabell från cell och lägga till värden inuti med hjälp av rad- och kolumnförskjutningar  

Följande provkod laddar den angivna källan Excel-filen som visas i skärmdumpen ovan och lägger till värden inne i tabellen och genererar den resulterande Excel-filen som visas ovan.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Accessing_Table.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cell D5 which lies inside the table
const cell = worksheet.getCells().get("D5");

// Put value inside the cell D5
cell.putValue("D5 Data");

// Access the Table from this cell
const table = cell.getTable();

// Add some value using Row and Column Offset
table.putCellValue(2, 2, "Offset [2,2]");

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
