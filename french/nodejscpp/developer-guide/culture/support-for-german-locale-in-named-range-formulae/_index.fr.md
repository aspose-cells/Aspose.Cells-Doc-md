---  
title: Prise en charge de la locale allemande dans les formules de plage nommée avec Node.js via C++  
linktitle: Prise en charge de l allemand dans les formules de plage nommée  
type: docs  
weight: 60  
url: /fr/nodejs-cpp/support-for-german-locale-in-named-range-formulae/  
description: Apprenez comment prendre en charge la locale allemande dans les formules de plage nommée à l’aide de Aspose.Cells for Node.js via C++.  
---  

Les formules en anglais sont écrites dans la région nommée. Ce fichier Excel peut être ouvert dans un environnement où le système est configuré en locale allemande, mais la formule anglaise sera traduite en langue allemande. L'exemple suivant démontre cette fonctionnalité ; cependant, il nécessite que Excel soit installé en allemand et que la région système soit également réglée sur allemand.  

Un fichier d'exemple pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant :  

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
