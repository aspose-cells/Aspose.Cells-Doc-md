---
title: Copiar Formas entre Hojas de Cálculo con Node.js a través de C++
linktitle: Copiar formas
type: docs
weight: 200
url: /es/nodejs-cpp/copy-shapes-between-worksheets/
description: Aprende cómo copiar formas como imágenes y gráficos entre hojas de cálculo usando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

A veces, necesitas copiar elementos en una hoja de cálculo, por ejemplo, imágenes, gráficos y otros objetos de dibujo, entre hojas de cálculo. Aspose.Cells for Node.js via C++ admite esta función. Los gráficos, imágenes y otros objetos pueden copiarse con el mayor grado de precisión.

Este artículo te brinda una comprensión detallada de cómo copiar formas entre hojas de cálculo.

{{% /alert %}}

## **Copiar una Imagen de una Hoja de Cálculo a Otra**

Para copiar una imagen de una hoja de cálculo a otra, utiliza el método [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-number-number-uint8array-) como se muestra en el código de ejemplo a continuación.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample_picture.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get the Picture from the "Picture" worksheet.
const picturesource = workbook.getWorksheets().get("Picture").getPictures().get(0);

// Save Picture to Memory Stream
const ms = picturesource.getData();

// Copy the picture to the Result Worksheet
workbook.getWorksheets().get("Result").getPictures().add(picturesource.getUpperLeftRow(), picturesource.getUpperLeftColumn(), ms, picturesource.getWidthScale(), picturesource.getHeightScale());

// Save the Worksheet
workbook.save(path.join(dataDir, "PictureCopied_out.xlsx"));
```

## **Copiar un gráfico de una hoja de cálculo a otra**

El siguiente código demuestra el uso del método [**ShapeCollection.addCopy(Shape, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addCopy-shape-number-number-number-number-) para copiar un gráfico de una hoja de cálculo a otra.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample_chart.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get the Chart from the "Chart" worksheet.
const chartsource = workbook.getWorksheets().get("Chart").getCharts().get(0);
const cshape = chartsource.getChartObject();

// Copy the Chart to the Result Worksheet
workbook.getWorksheets().get("Result").getShapes().addCopy(cshape, 20, 0, 2, 0);

// Save the Worksheet
workbook.save(path.join(dataDir, "ChartCopied_out.xlsx"));
```

## **Copiar controles y otros objetos de dibujo de una hoja de cálculo a otra**

Para copiar controles y otros objetos de dibujo, usa el método [**ShapeCollection.addCopy(Shape, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addCopy-shape-number-number-number-number-) como se muestra en el ejemplo a continuación.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample_control.xlsx");
// Open the template file
const workbook = new AsposeCells.Workbook(filePath);

// Get the Shapes from the "Control" worksheet.
const shape = workbook.getWorksheets().get("Control").getShapes();

// Copy the Textbox to the Result Worksheet
workbook.getWorksheets().get("Result").getShapes().addCopy(shape.get(0), 5, 0, 2, 0);

// Copy the Oval Shape to the Result Worksheet
workbook.getWorksheets().get("Result").getShapes().addCopy(shape.get(1), 10, 0, 2, 0);

// Save the Worksheet
workbook.save(path.join(dataDir, "ControlsCopied_out.xlsx"));
```
