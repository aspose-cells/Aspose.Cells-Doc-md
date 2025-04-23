---  
title: Reemplazar texto en un libro usando expresión regular con Node.js via C++  
linktitle: Reemplazar texto en un libro usando expresiones regulares  
type: docs  
weight: 90  
url: /es/nodejs-cpp/replace-text-in-a-workbook-using-regular-expression/  
description: Reemplazar texto en un libro usando expresión regular en Node.js via C++.  
---  

Aspose.Cells ofrece la función de reemplazar texto en un libro usando una expresión regular. Para esto, la API proporciona la propiedad [**ReplaceOptions.getRegexKey()**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions/#getRegexKey--) de la clase [**ReplaceOptions**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions). Establecer [**ReplaceOptions.getRegexKey()**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions/#getRegexKey--) en **true** indica que la clave buscada será una expresión regular.

El siguiente fragmento de código demuestra el uso de la propiedad [**ReplaceOptions.getRegexKey()**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions/#getRegexKey--) mediante el uso del [archivo de Excel de muestra](101089318.xlsx). El [archivo de salida](101089319.xlsx) generado por el siguiente fragmento de código está adjunto para referencia.

## **Código de muestra**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "SampleRegexReplace.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const replace = new AsposeCells.ReplaceOptions();
replace.setCaseSensitive(false);
replace.setMatchEntireCellContents(false);
// Set to true to indicate that the searched key is regex
replace.setRegexKey(true);

workbook.replace("\\bKIM\\b", "^^^TIM^^^", replace);
workbook.save(path.join(outputDir, "RegexReplace_out.xlsx"));
```  

