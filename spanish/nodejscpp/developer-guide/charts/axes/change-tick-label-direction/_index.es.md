---
title: Cambiar la dirección de la etiqueta de marcas de graduación con Node.js vía C++
linktitle: Cambiar la dirección de la etiqueta del eje
description: Aprende cómo cambiar la dirección de las etiquetas de marcas de graduación en Aspose.Cells para Node.js. Nuestra guía te ayudará a entender cómo ajustar la orientación de las etiquetas de marcas en los ejes, incluyendo orientaciones horizontal, vertical y en ángulo.
keywords: Aspose.Cells para Node.js, etiquetas de marcas, dirección, orientación, ejes, horizontal, vertical, en ángulo.
type: docs
weight: 170
url: /es/nodejs-cpp/change-tick-label-direction/
---

## **Cambiar la dirección de la etiqueta del eje**

Aspose.Cells te permite cambiar la dirección de las etiquetas de marcas en el gráfico usando la propiedad [**TickLabels.getDirectionType()**](https://reference.aspose.com/cells/nodejs-cpp/ticklabels/#getDirectionType--). La propiedad [**TickLabels.getDirectionType()**](https://reference.aspose.com/cells/nodejs-cpp/ticklabels/#getDirectionType--) acepta el valor de enumeración [**ChartTextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/charttextdirectiontype). La enumeración [**ChartTextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/charttextdirectiontype) proporciona los siguientes miembros:

- Horizontal
- Vertical
- Rotar 90
- Rotar 270
- Apilado

La siguiente imagen compara los archivos de origen y de salida

### **Imagen del archivo de origen**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **Imagen del archivo de salida**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

El siguiente fragmento de código cambia la dirección de las etiquetas de las marcas de verificación de Rotar90 a Horizontal.

## **Código de muestra**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");
const filePath = path.join(sourceDir, "SampleChangeTickLabelDirection.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const worksheet = workbook.getWorksheets().get(0);

// Load the chart from source worksheet
const chart = worksheet.getCharts().get(0);

chart.getCategoryAxis().getTickLabels().setDirectionType(AsposeCells.ChartTextDirectionType.Horizontal);

// Output the file
workbook.save(path.join(outputDir, "outputChangeChartDataLableDirection.xlsx"));
```

Los archivos de origen y de salida se pueden descargar desde los siguientes enlaces.

[Archivo de origen](105480221.xlsx)

[Archivo de salida](105480223.xlsx)
