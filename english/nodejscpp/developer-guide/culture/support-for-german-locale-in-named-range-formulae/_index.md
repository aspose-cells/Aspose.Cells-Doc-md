---  
title: Support for German Locale in Named Range Formulae with Node.js via C++  
linktitle: Support for German Locale in Named Range Formulae  
type: docs  
weight: 60  
url: /nodejs-cpp/support-for-german-locale-in-named-range-formulae/  
description: Learn how to support German locale in named range formulae using Aspose.Cells for Node.js via C++.  
---  

English formulae are written into named region. This Excel file can be opened in an environment where the system is configured to German Locale, however, the English formula shall be translated to German language. The following example demonstrates this feature; however, it requires Excel to be installed in German language and the system locale shall be set to German as well.  

Sample file for testing this feature can be downloaded from the following link:  

[sampleNamedRangeTest.xlsm](73990165.xlsm)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleNamedRangeTest.xlsm");
const outputFilePath = path.join(dataDir, "sampleOutputNamedRangeTest.xlsm");

// Initialize the name and formula
const name = "HasFormula";
const value = "=GET.CELL(48, INDIRECT(\"ZS\",FALSE))";

// Load the workbook
const wbSource = new AsposeCells.Workbook(sourceFilePath);
const wsCol = wbSource.getWorksheets();

const nameIndex = wsCol.getNames().add(name);
const namedRange = wsCol.getNames().get(nameIndex);
namedRange.setRefersTo(value);

// Save the workbook
wbSource.save(outputFilePath);
```  
  
