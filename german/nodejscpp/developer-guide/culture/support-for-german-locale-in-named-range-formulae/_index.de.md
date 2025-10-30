---  
title: Unterstützung für die deutsche Region in benannten Bereiche Formeln mit Node.js über C++  
linktitle: Unterstützung für das deutsche Gebietsschema in benannten Bereichsformeln  
type: docs  
weight: 60  
url: /de/nodejs-cpp/support-for-german-locale-in-named-range-formulae/  
description: Erfahren Sie, wie man deutsche Region in benannten Bereich Formeln mit Aspose.Cells for Node.js via C++ unterstützt.  
---  

Englische Formeln werden in benannten Bereichen geschrieben. Diese Excel-Datei kann in einer Umgebung geöffnet werden, in der das System auf Deutsch eingestellt ist. Die englische Formel wird jedoch ins Deutsche übersetzt. Das folgende Beispiel demonstriert diese Funktion; es erfordert jedoch, dass Excel in deutscher Sprache installiert ist und die Systemeinstellung auf Deutsch gesetzt ist.  

Die Beispieldatei für die Überprüfung dieser Funktion kann über den folgenden Link heruntergeladen werden:  

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
