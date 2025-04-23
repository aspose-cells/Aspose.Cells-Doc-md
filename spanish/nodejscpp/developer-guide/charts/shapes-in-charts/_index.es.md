---
title: Formas en gráficos con Node.js vía C++
linktitle: Formas en gráficos
description: Aprende cómo usar Aspose.Cells for Node.js via C++ para agregar controles y personalizar gráficos en Microsoft Excel. Esta guía demuestra cómo manipular elementos del gráfico, ajustar el formato y mejorar la apariencia y usabilidad general de tus gráficos.
keywords: Aspose.Cells for Node.js via C++, Controles de gráficos, Personalización de gráficos, Microsoft Excel, Elementos del gráfico, Formato.
type: docs
weight: 70
url: /es/nodejs-cpp/controls-in-charts/
---

{{% alert color="primary" %}}
A veces es necesario insertar objetos de dibujo como etiquetas, cuadros de texto, imágenes, etc., en un gráfico. Aspose.Cells puede agregar los controles a un gráfico en tiempo de ejecución.
{{% /alert %}}

## **Agregar control de etiqueta al gráfico**

Las etiquetas proporcionan un medio para dar información a los usuarios sobre el contenido de la hoja de cálculo. Aspose.Cells le permite agregar y manipular etiquetas incluso en gráficos.

La clase [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/) proporciona un método llamado [**addLabelInChart(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLabelInChart-number-number-number-number-), utilizado para agregar un control de etiqueta a un gráfico. A continuación, se muestra una lista de los parámetros utilizados para el método:

- **arriba** – el desplazamiento vertical de la etiqueta desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **izquierda** – el desplazamiento horizontal de la etiqueta desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **altura** – la altura de la etiqueta, en unidades de 1/4000 del área del gráfico.
- **ancho** – el ancho de la etiqueta, en unidades de 1/4000 del área del gráfico.

El método devuelve un objeto [**Label**](https://reference.aspose.com/cells/nodejs-cpp/label/). La clase [**Label**](https://reference.aspose.com/cells/nodejs-cpp/label/) representa una etiqueta en el gráfico. Tiene algunos miembros importantes:

- [**getText()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getText--) (propiedad) - especifica la cadena de título de una etiqueta.
- [**getFill()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getFill--) (propiedad) - especifica los atributos del color de relleno.

Con el siguiente ejemplo se muestra cómo añadir una etiqueta al gráfico. El ejemplo utiliza un archivo del diseñador (**exp_piechart.xls**) que contiene un gráfico. Usamos este archivo para insertar una etiqueta en el gráfico. A continuación se muestra el código original para añadir una etiqueta al gráfico. La siguiente salida se genera al ejecutar el código.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "chart.xls"));

// Get the designer chart in the second sheet.
const sheet = workbook.getWorksheets().get(1);
const chart = sheet.getCharts().get(0);

// Add a new label to the chart.
const label = chart.getShapes().addLabelInChart(100, 100, 350, 900);

// Set the caption of the label.
label.setText("A Label In Chart");

// Set the Placement Type, the way the Label is attached to the cells.
label.setPlacement(AsposeCells.PlacementType.FreeFloating);

// Save the excel file.
workbook.save(path.join(dataDir, "chart.out.xls"));
```

## **Añadiendo un Control de Cuadro de Texto al Gráfico**

Una forma de resaltar información importante en un informe es mediante el uso de un cuadro de texto. Por ejemplo, introducir texto para resaltar el nombre de la empresa o indicar la región geográfica con mayores ventas. La clase [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/) proporciona un método llamado [**addTextBoxInChart(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addTextBoxInChart-number-number-number-number-), que se utiliza para añadir un control de cuadro de texto a un gráfico. A continuación se muestra la lista de parámetros utilizados para el método:

- **arriba** - el desplazamiento vertical del cuadro de texto desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **izquierda** - el desplazamiento vertical del cuadro de texto desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **altura** - la altura del cuadro de texto, en unidades de 1/4000 del área del gráfico.
- **ancho** - el ancho del cuadro de texto, en unidades de 1/4000 del área del gráfico.

El método devuelve un objeto [**TextBox**](https://reference.aspose.com/cells/nodejs-cpp/textbox/). La clase [**TextBox**](https://reference.aspose.com/cells/nodejs-cpp/textbox/) representa un cuadro de texto en el gráfico.

El siguiente ejemplo muestra cómo añadir un cuadro de texto a un gráfico. El ejemplo utiliza el archivo del diseñador anterior (**exp_piechart.xls**) que contiene un gráfico. Usamos este archivo para insertar un cuadro de texto en el gráfico para mostrar el título del gráfico. A continuación se muestra el código original para añadir un cuadro de texto al gráfico.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "chart.xls"));

// Get the designer chart in the second sheet.
const sheet = workbook.getWorksheets().get(1);
const chart = sheet.getCharts().get(0);

// Add a new textbox to the chart.
const textbox0 = chart.getShapes().addTextBoxInChart(100, 1100, 350, 2550);

// Fill the text.
textbox0.setText("Sales By Region");

// Get the textbox text frame.
// const textframe0 = textbox0.getTextFrame();

// Set the textbox to adjust it according to its contents.
// textframe0.setAutoSize(true);

// Set the font color.
textbox0.getFont().setColor(AsposeCells.Color.Maroon);

// Set the font to bold.
textbox0.getFont().setIsBold(true);

// Set the font size.
textbox0.getFont().setSize(14);

// Set font attribute to italic.
textbox0.getFont().setIsItalic(true);

// Get the fill format of the textbox.
const fillformat = textbox0.getFill();

// Get the line format type of the textbox.
const lineformat = textbox0.getLine();

// Set the line weight.
lineformat.setWeight(2);

// Set the dash style to solid.
lineformat.setDashStyle(AsposeCells.MsoLineDashStyle.Solid);

// Save the excel file.
workbook.save(path.join(dataDir, "chart.out.xls"));
```

## **Añadiendo una Imagen al Gráfico**

Aspose.Cells te permite insertar imágenes en un gráfico. Por ejemplo, agregar una imagen para resaltar o dar más significado a un gráfico o sus contenidos, o insertar un archivo de imagen de marca.

La clase [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/) proporciona un método llamado [**addPictureInChart(number, number, Uint8Array, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPictureInChart-number-number-uint8array-number-number-), que se utiliza para añadir un objeto de imagen al gráfico. A continuación se muestra la lista de parámetros utilizados para el método:

- **arriba** - el desplazamiento vertical de la imagen desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **izquierda** - el desplazamiento vertical de la imagen desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **flujo** - un objeto de flujo que contiene los datos de la imagen.
- **escalaAncho** - la escala del ancho de la imagen, un valor porcentual.
- **escalaAlto** - la escala de la altura de la imagen, un valor porcentual.

El método devuelve un objeto [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/). La clase [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/) representa un objeto de imagen en el gráfico.

El siguiente ejemplo muestra cómo agregar una imagen al gráfico. El ejemplo utiliza el archivo de diseñador anterior (**exp_piechart.xls**) que tiene un gráfico en él. Utilizamos este archivo para insertar una imagen en el gráfico. A continuación se muestra el código original para agregar una imagen al gráfico.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "chart_shapes.xls"));

// Get an image file to the stream.
const stream = fs.readFileSync(path.join(dataDir, "logo.jpg"));

// Get the designer chart in the second sheet.
const sheet = workbook.getWorksheets().get(0);
const chart = sheet.getCharts().get(0);

// Add a new picture to the chart.
const pic0 = chart.getShapes().addPictureInChart(50, 50, stream, 40, 40);

// Get the lineformat type of the picture.
const lineformat = pic0.getLine();          

// Set the dash style.
lineformat.setDashStyle(AsposeCells.MsoLineDashStyle.Solid);

// Set the line weight.
lineformat.setWeight(4);    

// Save the excel file.
workbook.save(path.join(dataDir, "chart.out.xls"));
```

## **Agregar casilla de verificación en el gráfico**

Aspose.Cells le permite insertar casillas de verificación en una hoja de gráfico utilizando la enumeración [**MsoDrawingType**](https://reference.aspose.com/cells/nodejs-cpp/msodrawingtype/). El siguiente ejemplo demuestra cómo agregar una casilla de verificación a una hoja de gráfico.

La siguiente imagen muestra la hoja de gráfico con la casilla de verificación en el archivo de salida.

![todo:image_alt_text](controls-in-charts_1.jpg)

El [archivo de salida](101089316.xlsx) generado por el siguiente fragmento de código se adjunta para su referencia.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a chart to the worksheet
const index = workbook.getWorksheets().add(AsposeCells.SheetType.Chart);

const sheet = workbook.getWorksheets().get(index);
sheet.getCharts().addFloatingChart(AsposeCells.ChartType.Column, 0, 0, 1024, 960);
sheet.getCharts().get(0).getNSeries().add("{1,2,3}", false);

// Add checkbox to the chart.
sheet.getCharts().get(0).getShapes().addShapeInChart(AsposeCells.MsoDrawingType.CheckBox, AsposeCells.PlacementType.Move, 400, 400, 1000, 600);
sheet.getCharts().get(0).getShapes().get(0).setText("CheckBox 1");

// Save the excel file.
workbook.save(outputDir +"InsertCheckboxInChartSheet_out.xlsx");
```

## **Temas avanzados**
- [Agregar marca de agua de WordArt al gráfico](/cells/es/nodejs-cpp/add-wordart-watermark-to-chart/)

