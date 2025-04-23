---
title: Infoga och ta bort rader och kolumner i Excelfil
linktitle: Infoga och ta bort rader och kolumner
type: docs
weight: 70
url: /sv/nodejs-cpp/inserting-and-deleting-rows-and-columns/
description: Denna artikel visar hur man infogar och tar bort rader och kolumner med API n Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells Node.js via C++ hanterar rader och kolumner, infogar rader och kolumner, tar bort rader och kolumner
---

## **Introduktion**

Oavsett om du skapar en ny arbetsbok från grunden eller arbetar med en befintlig arbetsbok kan vi behöva lägga till extra rader eller kolumner för att rymma mer data. Å andra sidan kan det också hända att vi behöver ta bort rader eller kolumner från angivna positioner i arbetsboken. 
För att uppfylla dessa krav tillhandahåller Aspose.Cells for Node.js via C++ ett mycket enkelt set av klasser och metoder, diskuteras nedan.

### **Hantera rader och kolumner**

Aspose.Cells for Node.js via C++ tillhandahåller en klass [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), som representerar en Microsoft Excel-fil. Klasserna [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) innehåller en [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) samling som ger tillgång till varje ark i en Excel-fil. Ett ark representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) tillhandahåller en [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) samling som representerar alla celler i arket.

Samlingen [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) ger flera metoder för att hantera rader och kolumner i ett arbetsblad. Några av dessa diskuteras nedan.

{{% alert color="primary" %}}

När rader eller kolumner läggs till skiftas innehållet i arbetsbladet nedåt eller åt höger, och om rader eller kolumner tas bort skiftas innehållet uppåt eller åt vänster.

{{% /alert %}}


## **Infoga rader och kolumner**

### **Hur man infogar en rad**

Infoga en rad i arbetsbladet på valfri plats genom att anropa [**insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-)-metoden i [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-samlingen. Metoden [**insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-) tar indexet för raden där den nya raden ska infogas.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Inserting a row into the worksheet at 3rd position
worksheet.getCells().insertRow(2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```

### **Hur man infogar flera rader**

För att infoga flera rader i ett arbetsblad, ring [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-)-metoden i [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-samlingen. Metoden [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) tar två parametrar:

- Radindex, index för raden från vilken de nya raderna ska infogas.
- Antal rader, det totala antalet rader som ska infogas.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

const fileData = fs.readFileSync(filePath);
const workbook = new AsposeCells.Workbook(fileData);

const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().insertRows(2, 10);

workbook.save(path.join(dataDir, "output.out.xls"));
```

### **Hur man infogar en rad med formatering**

För att infoga en rad med formateringsalternativ, använd [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-)-överbelastningen som tar [**InsertOptions**](https://reference.aspose.com/cells/nodejs-cpp/insertoptions) som parameter. Ange [**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/)-egenskapen i [**InsertOptions**](https://reference.aspose.com/cells/nodejs-cpp/insertoptions)-klassen med [**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/)-uppräkningen. [**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/)-uppräkningen har tre medlemmar som listas nedan.

- SammaSomOvan: Formaterar raden på samma sätt som raden ovan.
- SammaSomNedan: Formaterar raden på samma sätt som raden nedan.
- Rensa: Rensar formateringen.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Creating a file stream containing the Excel file to be opened
const filePath = path.join(dataDir, "book1.xls");
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting Formatting options
const insertOptions = new AsposeCells.InsertOptions();
insertOptions.setCopyFormatType(AsposeCells.CopyFormatType.SameAsAbove);

// Inserting a row into the worksheet at 3rd position
worksheet.getCells().insertRows(2, 1, insertOptions);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "InsertingARowWithFormatting.out.xls"));
```

### **Hur man infogar en kolumn**

Utvecklare kan också infoga en kolumn i arbetsbladet på valfri plats genom att anropa [**insertColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertColumn-number-boolean-)-metoden i [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-samlingen. Metoden [**insertColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertColumn-number-boolean-) tar indexet för kolumnen där den nya kolumnen ska infogas.

```javascript
const fs = require('fs');
const path = require('path');
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fileStream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fileStream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Inserting a column into the worksheet at 2nd position
worksheet.getCells().insertColumn(1);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```

## **Ta bort rader och kolumner**

### **Hur man tar bort flera rader**

För att ta bort flera rader från ett arbetsblad, ring [**deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-)-metoden i [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-samlingen. Metoden [**deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-) tar två parametrar:

- Radindex, index för raden från vilken raderna ska tas bort.
- Antal rader, det totala antalet rader som ska tas bort.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Read file contents as Uint8Array
const fileContent = fs.readFileSync(filePath);
const fileBuffer = new Uint8Array(fileContent);

// Instantiating a Workbook object with file buffer
const workbook = new AsposeCells.Workbook(fileBuffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Deleting 10 rows from the worksheet starting from 3rd row
worksheet.getCells().deleteRows(2, 10);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```


### **Hur man tar bort en kolumn**

För att ta bort en kolumn från arbetsbladet på valfri plats, ring [**deleteColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteColumn-number-boolean-)-metoden i [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-samlingen. Metoden [**deleteColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteColumn-number-boolean-) tar indexet för kolumnen som ska tas bort.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Creating a file stream containing the Excel file to be opened
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fs.readFileSync(filePath));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Deleting a column from the worksheet at 5th position
worksheet.getCells().deleteColumn(4);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));

// Closing resources is handled automatically by Node.js, no specific close needed.
```
