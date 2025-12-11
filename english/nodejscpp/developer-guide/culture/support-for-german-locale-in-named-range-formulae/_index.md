---  
title: Support for German Locale in Named Range Formulae with Node.js via C++  
linktitle: Support for German Locale in Named Range Formulae  
type: docs  
weight: 60  
url: /nodejs-cpp/support-for-german-locale-in-named-range-formulae/  
description: Learn how to support German locale in named range formulae using Aspose.Cells for Node.js via C++.  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

English formulas are written into a named region. This Excel file can be opened in an environment where the system is configured for the German locale; however, the English formulas will be translated to German. The following example demonstrates this feature; however, it requires Excel to be installed in German and the system locale to be set to German as well.  

Sample file for testing this feature can be downloaded from the following link:  

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
