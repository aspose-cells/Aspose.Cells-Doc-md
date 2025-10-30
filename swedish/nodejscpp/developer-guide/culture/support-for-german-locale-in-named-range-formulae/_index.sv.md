---  
title: Stöd för tysk lokal i namngivna intervallformler med Node.js via C++  
linktitle: Stöd för tysk lokal i namnformler  
type: docs  
weight: 60  
url: /sv/nodejs-cpp/support-for-german-locale-in-named-range-formulae/  
description: Lär dig hur du stöder tysk lokal i namngivna intervallformler med Aspose.Cells for Node.js via C++.  
---  

Engelska formler skrivs in i det namngivna området. Denna Excel-fil kan öppnas i en miljö där systemet är inställt på tysk lokal, men den engelska formeln översätts till tyska. Följande exempel demonstrerar denna funktion; dock krävs Excel installerat på tyska och systemets lokal ska också vara satt till tyska.  

Provfil för att testa den här funktionen kan laddas ner från följande länk:  

[sampleNamedRangeTest.xlsm](73990165.xlsm)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
const fs = require("fs");

const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleNamedRangeTest.xlsm");
const outputFilePath = path.join(dataDir, "sampleOutputNamedRangeTest.xlsm");

const wb = new AsposeCells.Workbook();
wb.save(sourceFilePath);

const name = "HasFormula";
const value = "=GET.CELL(48, INDIRECT(\"ZS\",FALSE))";

const wbSource = new AsposeCells.Workbook(sourceFilePath);
const wsCol = wbSource.getWorksheets();

const nameIndex = wsCol.getNames().add(name);
const namedRange = wsCol.getNames().get(nameIndex);
namedRange.setRefersTo(value);

wbSource.save(outputFilePath);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
