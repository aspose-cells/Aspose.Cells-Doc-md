---
title: Especificar cómo cruzar cadenas en HTML de salida usando HtmlCrossType con Node.js mediante C++
linktitle: Especifique cómo cruzar cadenas en HTML de salida utilizando HtmlCrossType
type: docs
weight: 140
url: /es/nodejs-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: Aprende cómo controlar el desbordamiento de cadenas en la salida HTML especificando HtmlCrossType en Aspose.Cells for Node.js via C++. 
---

## **Escenarios de uso posibles**

Cuando una celda contiene texto o cadena pero es mayor que el ancho de la celda, la cadena desborda si la siguiente celda en la siguiente columna es null o está vacía. Cuando guardas tu archivo de Excel en HTML, puedes controlar este desbordamiento especificando el tipo de cruce usando la enumeración [**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype). Tiene los siguientes valores:

- **HtmlCrossType.Default**: Muestra como MS Excel; depende de la siguiente celda. Si la siguiente celda es null, la cadena cruzará o será truncada.

- **HtmlCrossType.MSExport**: Muestra la cadena como exportación HTML de MS Excel.

- **HtmlCrossType.Cross**: Muestra la cadena cruzada en HTML; el rendimiento para crear archivos HTML grandes será más de diez veces más rápido que establecer el valor en Default o FitToCell.

- **HtmlCrossType.FitToCell**: Solo mostrar la cadena dentro del ancho de la celda.

## **Especifica cómo cruzar la cadena en HTML de salida utilizando HtmlCrossType**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](51740732.xlsx) y lo guarda en formato HTML especificando diferentes [**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype). Descargue los [HTMLs de salida](51740734.zip) generados con este código. El archivo de Excel de muestra contiene la imagen con borde de color rojo como se muestra en esta captura de pantalla que demuestra el efecto de los valores [**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype) en el HTML de salida.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Código de muestra**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleHtmlCrossStringType.xlsx");

// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Specify HTML Cross Type
const opts = new AsposeCells.HtmlSaveOptions();
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.Default);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.MSExport);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.Cross);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.FitToCell);

// Output Html
workbook.save("out" + opts.getHtmlCrossStringType() + ".htm", opts);
```
