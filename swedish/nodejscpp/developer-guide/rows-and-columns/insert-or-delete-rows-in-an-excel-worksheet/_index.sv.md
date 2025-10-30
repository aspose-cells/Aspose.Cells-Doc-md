---  
title: Infoga eller ta bort rader i ett Excel ark med Node.js via C++  
linktitle: Infoga eller ta bort rader i ett Excel ark  
type: docs  
weight: 20  
url: /sv/nodejs-cpp/insert-or-delete-rows-in-an-excel-worksheet/  
description: Denna artikel tillhandahåller Node.js kod med C++ för att infoga och ta bort rader i ett Excel ark.  
keywords: node.js infoga eller ta bort rader i excel ark, node.js infoga eller ta bort rader i excel, node.js infoga rader i excel, node.js ta bort rader i excel, infoga eller ta bort rader i excel ark med node.js, infoga eller ta bort rader i excel med node.js, infoga rader i excel med node.js, ta bort rader i excel med node.js  
---  

{{% alert color="primary" %}}  

När du skapar ett nytt ark eller använder ett befintligt ark kan du behöva lägga till extra rader eller kolumner för att rymma data. Ibland kan du behöva ta bort rader eller kolumner från angivna positioner i arket.  

{{% /alert %}}  

Aspose.Cells for Node.js via C++ erbjuder två metoder för att infoga och ta bort rader: [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) och [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-). Dessa metoder är optimerade för prestanda och gör jobbet mycket snabbt.  

För att infoga eller ta bort ett antal rader rekommenderar vi att du alltid använder [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) och [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-) metoderna istället för att använda [**Cells.insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-) eller [**Cells.deleteRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRow-number-) metoder i en loop.  

Aspose.Cells fungerar på samma sätt som Microsoft Excel gör. När rader eller kolumner läggs till skiftas innehållet i arbetsbladet nedåt och till höger. När rader eller kolumner tas bort skiftas innehållet i arbetsbladet uppåt eller till vänster. Alla referenser i andra arbetsblad och celler uppdateras när rader läggs till eller tas bort.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a Workbook object.
// Load a template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xlsx"));

// Get the first worksheet in the book.
const sheet = workbook.getWorksheets().get(0);

// Insert 10 rows at row index 2 (insertion starts at 3rd row)
sheet.getCells().insertRows(2, 10);

// Delete 5 rows now. (8th row - 12th row)
sheet.getCells().deleteRows(7, 5);

// Save the excel file.
workbook.save(path.join(dataDir, "out_book1.out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
