---  
title: Supporto per la localizzazione tedesca in formule denominate con Node.js via C++  
linktitle: Supporto per la localizzazione in tedesco nelle formule dei nomi  
type: docs  
weight: 60  
url: /it/nodejs-cpp/support-for-german-locale-in-named-range-formulae/  
description: Impara come supportare la localizzazione tedesca nelle formule di nomi usando Aspose.Cells for Node.js via C++.  
---  

Le formule in inglese sono scritte nelle regioni denominate. Questo file Excel può essere aperto in un ambiente dove il sistema è configurato per la localizzazione tedesca, ma le formule inglesi saranno tradotte in tedesco. Il seguente esempio dimostra questa funzione; richiede tuttavia che Excel sia installato in lingua tedesca e che la localizzazione di sistema sia impostata su tedesco.  

Il file di esempio per testare questa funzionalità può essere scaricato dal seguente link:  

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

