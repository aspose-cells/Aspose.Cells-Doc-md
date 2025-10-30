---  
title: Soporte para configuración regional alemana en fórmulas de rango con Node.js a través de C++  
linktitle: Soporte para Configuración Regional Alemana en Fórmulas de Rango Nombrado  
type: docs  
weight: 60  
url: /es/nodejs-cpp/support-for-german-locale-in-named-range-formulae/  
description: Aprende cómo soportar la configuración regional alemana en fórmulas de rangos usando Aspose.Cells for Node.js via C++.  
---  

Las fórmulas en inglés se escriben en la región nombrada. Este archivo Excel puede abrirse en un entorno donde la configuración del sistema esté configurada en idioma alemán, sin embargo, la fórmula en inglés se traducirá al idioma alemán. El siguiente ejemplo demuestra esta característica; sin embargo, requiere que Excel esté instalado en idioma alemán y que la configuración regional del sistema también esté en alemán.  

Se puede descargar el archivo de muestra para probar esta función desde el siguiente enlace:  

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
