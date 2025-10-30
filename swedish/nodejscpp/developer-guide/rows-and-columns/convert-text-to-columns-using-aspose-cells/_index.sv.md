---  
title: Konvertera Text till Kolumner med Aspose.Cells for Node.js via C++  
linktitle: Konvertera Text till Kolumner  
type: docs  
weight: 30  
url: /sv/nodejs-cpp/convert-text-to-columns-using-aspose-cells/  
description: Lär dig hur du konverterar text till kolumner i Excel med Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**  

Du kan konvertera din Text till Kolumner med Microsoft Excel. Denna funktion finns under *Data Tools* i fliken *Data*. För att dela upp innehållet i en kolumn till flera kolumner ska data innehålla en specifik avgränsare, såsom ett kommatecken (eller någon annan tecken), baserat på vilken Microsoft Excel delar upp cellens innehåll till flera celler. Aspose.Cells for Node.js via C++ erbjuder också denna funktion via [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-number-number-number-txtloadoptions-).  

## **Konvertera Text till Kolumner med Aspose.Cells for Node.js via C++**  

Följande exempelprogram förklarar användningen av [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-number-number-number-txtloadoptions-)-metoden. Koden lägger först till några personnamn i kolumn A i det första arbetsbladet. Förnamn och efternamn är separerade med ett mellanslag. Sedan tillämpar den [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-number-number-number-txtloadoptions-)-metoden på kolumn A och sparar det som en utdata-Excel-fil. Om du öppnar [utdata-Excel-filen](25395213.xlsx) kommer du att se att förnamnen är i kolumn A medan efternamnen är i kolumn B, som visas i skärmbilden.  

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)  

## **Exempelkod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create a workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Add people name in column A. First name and last name are separated by space.
ws.getCells().get("A1").putValue("John Teal");
ws.getCells().get("A2").putValue("Peter Graham");
ws.getCells().get("A3").putValue("Brady Cortez");
ws.getCells().get("A4").putValue("Mack Nick");
ws.getCells().get("A5").putValue("Hsu Lee");

// Create text load options with space as separator.
const opts = new AsposeCells.TxtLoadOptions();
opts.setSeparator(' ');

// Split the column A into two columns using TextToColumns() method.
// Now column A will have first name and column B will have second name.
ws.getCells().textToColumns(0, 0, 5, opts);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "outputTextToColumns.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
