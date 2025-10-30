---
title: Crear y administrar gráficos con Node.js a través de C++
linktitle: Gráficos
description: Aprenda cómo usar Aspose.Cells para Node.js para crear gráficos en Microsoft Excel. Nuestra guía demostrará varios tipos de gráficos y cómo personalizar su apariencia y formato.
keywords: Aspose.Cells para Node.js, Creación de gráficos, Microsoft Excel, Tipos de gráficos, Personalización, Apariencia, Formato.
type: docs
weight: 130
url: /es/nodejs-cpp/creating-charts/
---

{{% alert color="primary" %}}

Es posible agregar una variedad de gráficos a hojas de cálculo con Aspose.Cells. Aspose.Cells proporciona muchos objetos de gráficos flexibles. Este tema discute los objetos de gráficos de Aspose.Cells.

{{% /alert %}}

## **Creando gráficos**

### **Simplemente creando un gráfico**
Es simple crear un gráfico con Aspose.Cells con los siguientes ejemplos de código:
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Obtaining the reference of the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Adding sample values to cells
worksheet.getCells().get("A2").putValue("Category1");
worksheet.getCells().get("A3").putValue("Category2");
worksheet.getCells().get("A4").putValue("Category3");

worksheet.getCells().get("B1").putValue("Column1");
worksheet.getCells().get("B2").putValue(4);
worksheet.getCells().get("B3").putValue(20);
worksheet.getCells().get("B4").putValue(50);
worksheet.getCells().get("C1").putValue("Column2");
worksheet.getCells().get("C2").putValue(50);
worksheet.getCells().get("C3").putValue(100);
worksheet.getCells().get("C4").putValue(150);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Setting chart data source as the range "A1:C4"
chart.setChartDataRange("A1:C4", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **Cosas a saber para crear un gráfico**

 Antes de crear gráficos, es importante comprender algunos conceptos básicos que son útiles al crear gráficos usando Aspose.Cells.

#### **Objetos de gráficos**

 Los objetos de gráficos se enumeran a continuación:

- Series, una sola serie de datos en un gráfico.
- Eje, el eje de un gráfico.
- Gráfico, un solo gráfico de Excel.
- Área de gráfico, el área de gráfico en la hoja de cálculo.
- Tabla de datos del gráfico, una tabla de datos de gráfico.
- ChartFrame, el objeto de marco en un gráfico.
- ChartPoint, un solo punto en una serie en un gráfico.
- ChartPointCollection, una colección que contiene todos los puntos en una serie.
- Charts, una colección de objetos Chart.
- DataLabels, una colección de todos los objetos DataLabel para la serie especificada.
- FillFormat, formato de relleno para una forma.
- Floor, el suelo de un gráfico en 3D.
- Legend, la leyenda del gráfico.
- Line, la línea del gráfico.
- SeriesCollection, una colección de objetos Series.
- TickLabels, las etiquetas de marca de graduación asociadas con las marcas en un eje de un gráfico.
- Title, el título de un gráfico o eje.
- Trendline, una línea de tendencia en un gráfico.
- TrendlineCollection, una colección de todos los objetos Trendline para la serie de datos especificada.
- Walls, las paredes de un gráfico en 3D.

#### **Usar objetos de gráficos**

Como se mencionó anteriormente, todos los objetos de gráficos son instancias de sus clases respectivas y proporcionan propiedades y métodos específicos para realizar tareas específicas. Use objetos de gráficos para crear gráficos.

 Agregue cualquier tipo de gráfico a una hoja usando la colección [**getCharts()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCharts--). Cada elemento en la colección [**getCharts()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCharts--) representa un objeto [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/). Un objeto [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/) encapsula todos los demás objetos de gráficos necesarios para personalizar la apariencia del gráfico. La siguiente sección muestra cómo usar algunos objetos básicos de gráficos para crear un gráfico simple.

### **Crear gráfico usando Aspose.Cells**

**Pasos:**

 1. Agregue algunos datos a las celdas de la hoja con el método [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell/) del objeto [**putValue(string)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-string-).
   Esto se utilizará como fuente de datos para el gráfico.
 1. Agregue un gráfico a la hoja llamando al método [**add**](https://reference.aspose.com/cells/nodejs-cpp/chartcollection/#add-charttype-number-number-number-number-) de la colección [**ChartCollection**](https://reference.aspose.com/cells/nodejs-cpp/chartcollection), encapsulado en el objeto [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/).
 1. Especifique el tipo de gráfico con la enumeración [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/).
    Por ejemplo, el ejemplo a continuación usa el valor [**ChartType.Pyramid**](https://reference.aspose.com/cells/nodejs-cpp/charttype) como tipo de gráfico.
 1. Acceda al nuevo objeto [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/) desde la colección [**Charts**](https://reference.aspose.com/cells/nodejs-cpp/chartcollection) pasando su índice.
 1. Use cualquiera de los objetos de gráficos encapsulados en el objeto [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/) para gestionar el gráfico.
    El ejemplo a continuación usa el objeto de gráficos [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/) para especificar la fuente de datos del gráfico.

 Cuando agregue datos fuente al gráfico, la fuente puede ser un rango de celdas (como "A1:C3"), o una secuencia de celdas no contiguas (como "A1, A3, A5"), o una secuencia de valores (como "1,2,3").

Estos pasos generales le permiten crear cualquier tipo de gráfico. Utilice diferentes objetos de gráficos para crear distintos gráficos.

Es posible crear muchos tipos diferentes de gráficos con Aspose.Cells. Todos los gráficos estándar admitidos por Aspose.Cells están predefinidos en una enumeración llamada [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/).

Los tipos de gráficos predefinidos son:

|**Tipos de Gráficos**|**Descripción**|
| :- | :- |
|Column|Representa Gráfico de Columnas Agrupadas|
|ColumnStacked|Representa Gráfico de Columnas Apiladas|
|Column100PercentStacked|Representa Gráfico de Columnas Apiladas al 100%|
|Column3DClustered|Representa Gráfico de Columnas Agrupadas en 3D|
|Column3DStacked|Representa Gráfico de Columnas Apiladas en 3D|
|Column3D100PercentStacked|Representa Gráfico de Columnas Apiladas al 100% en 3D|
|Column3D|Representa Gráfico de Columnas en 3D|
|Bar|Representa Gráfico de Barras Agrupadas|
|BarStacked|Representa Gráfico de Barras Apiladas|
|Bar100PercentStacked|Representa Gráfico de Barras Apiladas al 100%|
|Bar3DClustered|Representa Gráfico de Barras Agrupadas en 3D|
|Bar3DStacked|Representa Gráfico de Barras Apiladas en 3D|
|Bar3D100PercentStacked|Representa Gráfico de Barras Apiladas al 100% en 3D|
|Line|Representa Gráfico de Líneas|
|LineStacked|Representa Gráfico de Líneas Apiladas|
|Line100PercentStacked|Representa Gráfico de Líneas Apiladas al 100%|
|LineWithDataMarkers|Representa Gráfico de Líneas con marcadores de datos|
|LineStackedWithDataMarkers|Representa Gráfico de Líneas Apiladas con marcadores de datos|
|Line100PercentStackedWithDataMarkers|Representa Gráfico de Líneas Apiladas al 100% con marcadores de datos|
|Line3D|Representa Gráfico de Líneas en 3D|
|Pie|Representa Gráfico Circular|
|Pie3D|Representa Gráfico Circular en 3D|
|PiePie|Representa Gráfico de Pastel de Pastel|
|PieExploded|Representa Gráfico de Pastel Explodido|
|Pie3DExploded|Representa Gráfico de Pastel Explodido en 3D|
|PieBar|Representa Gráfico de Barras de Pastel|
|Scatter|Representa Gráfico de Dispersión|
|ScatterConnectedByCurvesWithDataMarker|Representa un gráfico de dispersión conectado por curvas, con marcadores de datos|
|ScatterConnectedByCurvesWithoutDataMarker|Representa un gráfico de dispersión conectado por curvas, sin marcadores de datos|
|ScatterConnectedByLinesWithDataMarker|Representa un gráfico de dispersión conectado por líneas, con marcadores de datos|
|ScatterConnectedByLinesWithoutDataMarker|Representa un gráfico de dispersión conectado por líneas, sin marcadores de datos|
|Area|Representa un gráfico de área|
|AreaStacked|Representa un gráfico de área apilada|
|Area100PercentStacked|Representa un gráfico de área apilada al 100%|
|Area3D|Representa un gráfico de área 3D|
|Area3DStacked|Representa un gráfico de área 3D apilada|
|Area3D100PercentStacked|Representa un gráfico de área 3D apilada al 100%|
|Doughnut|Representa un gráfico de rosquilla|
|DoughnutExploded|Representa un gráfico de rosquilla explosionada|
|Radar|Representa un gráfico radar|
|RadarWithDataMarkers|Representa un gráfico radar con marcadores de datos|
|RadarFilled|Representa un gráfico radar relleno|
|Surface3D|Representa un gráfico de superficie 3D|
|SurfaceWireframe3D|Representa un gráfico de superficie 3D con estructura de alambre|
|SurfaceContour|Representa un gráfico de contorno|
|SurfaceContourWireframe|Representa un gráfico de contorno con estructura de alambre|
|Bubble|Representa un gráfico de burbujas|
|Bubble3D|Representa Gráfico de Burbujas 3D|
|Cylinder|Representa Gráfico de Cilindro|
|CylinderStacked|Representa Gráfico de Cilindro Apilado|
|Cylinder100PercentStacked|Representa Gráfico de Cilindro Apilado al 100%|
|CylindericalBar|Representa Gráfico de Barras Cilíndricas|
|CylindericalBarStacked|Representa Gráfico de Barras Cilíndricas Apiladas|
|CylindericalBar100PercentStacked|Representa Gráfico de Barras Cilíndricas Apiladas al 100%|
|CylindericalColumn3D|Representa Gráfico de Columnas Cilíndricas 3D|
|Cone|Representa Gráfico de Cono|
|ConeStacked|Representa Gráfico de Cono Apilado|
|Cone100PercentStacked|Representa Gráfico de Cono Apilado al 100%|
|ConicalBar|Representa Gráfico de Barras Cónicas|
|ConicalBarStacked|Representa Gráfico de Barras Cónicas Apiladas|
|ConicalBar100PercentStacked|Representa Gráfico de Barras Cónicas Apiladas al 100%|
|ConicalColumn3D|Representa Gráfico de Columnas Cónicas 3D|
|Pyramid|Representa Gráfico de Pirámide|
|PyramidStacked|Representa Gráfico de Pirámide Apilada|
|Pyramid100PercentStacked|Representa Gráfico de Pirámide Apilada al 100%|
|PyramidBar|Representa Gráfico de Barras de Pirámide|
|PyramidBarStacked|Representa Gráfico de Barras de Pirámide Apiladas|
|PyramidBar100PercentStacked|Representa un gráfico de barras de pirámide apilada al 100%|
|PyramidColumn3D|Representa un gráfico de columnas de pirámide 3D|
{{% alert color="primary" %}}

Cuando asignas un rango de celdas como fuente de datos, solo puedes establecer el rango de arriba a la izquierda hacia abajo a la derecha. Por ejemplo, "A1:C3" es válido mientras que "C3:A1" es inválido.

{{% /alert %}}

#### **Gráfico de pirámide**

Cuando se ejecuta el código de ejemplo, se agrega un gráfico de pirámide a la hoja de cálculo.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Pyramid, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

#### **Gráfico de líneas**

 En el ejemplo anterior, simplemente cambiar el [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) por *Línea* crea un gráfico de línea. La fuente completa se proporciona a continuación. Cuando se ejecuta el código, se añade un gráfico de línea a la hoja de cálculo.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Line, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

#### **Gráfico de burbujas**

 Para crear un gráfico de burbujas, el [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) debe establecerse en [**ChartType.Bubble**](https://reference.aspose.com/cells/nodejs-cpp/charttype) y algunas propiedades adicionales como BubbleSizes, Values y XValues deben configurarse en consecuencia. Al ejecutar el siguiente código, se añade un gráfico de burbajas a la hoja.

#### **Gráfico de líneas con marcadores de datos**

 Para crear un gráfico de línea con marcador de datos, el [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) debe establecerse en *ChartType.LineWithDataMarkers* y algunas propiedades adicionales como área de fondo, marcadores de serie, valores y XValues deben configurarse en consecuencia. Al ejecutar el siguiente código, se añade un gráfico de línea con marcador de datos a la hoja.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Instantiate a workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set columns title 
worksheet.getCells().get(0, 0).putValue("X");
worksheet.getCells().get(0, 1).putValue("Y");

// Random data shall be used for generating the chart
// Create random data and save in the cells
for (let i = 1; i < 21; i++) {
worksheet.getCells().get(i, 0).putValue(i);
worksheet.getCells().get(i, 1).putValue(0.8);
}

for (let i = 21; i < 41; i++) {
worksheet.getCells().get(i, 0).putValue(i - 20);
worksheet.getCells().get(i, 1).putValue(0.9);
}
// Add a chart to the worksheet
const idx = worksheet.getCharts().add(AsposeCells.ChartType.LineWithDataMarkers, 1, 3, 20, 20);

// Access the newly created chart
const chart = worksheet.getCharts().get(idx);

// Set chart style
chart.setStyle(3);

// Set autoscaling value to true
chart.setAutoScaling(true);

// Set foreground color white
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.White);

// Set Properties of chart title
chart.getTitle().setText("Sample Chart");

// Set chart type
chart.setType(AsposeCells.ChartType.LineWithDataMarkers);

// Set Properties of categoryaxis title
chart.getCategoryAxis().getTitle().setText("Units");

//Set Properties of nseries
const s2_idx = chart.getNSeries().add("A2:A2", true);
const s3_idx = chart.getNSeries().add("A22:A22", true);

// Set IsColorVaried to true for varied points color
chart.getNSeries().setIsColorVaried(true);

// Set properties of background area and series markers
chart.getNSeries().get(s2_idx).getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(s2_idx).getMarker().getArea().setForegroundColor(AsposeCells.Color.Yellow);
chart.getNSeries().get(s2_idx).getMarker().getBorder().setIsVisible(false);

// Set X and Y values of series chart
chart.getNSeries().get(s2_idx).setXValues("A2:A21");
chart.getNSeries().get(s2_idx).setValues("B2:B21");

// Set properties of background area and series markers
chart.getNSeries().get(s3_idx).getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(s3_idx).getMarker().getArea().setForegroundColor(AsposeCells.Color.Green);
chart.getNSeries().get(s3_idx).getMarker().getBorder().setIsVisible(false);

// Set X and Y values of series chart
chart.getNSeries().get(s3_idx).setXValues("A22:A41");
chart.getNSeries().get(s3_idx).setValues("B22:B41");

// Save the workbook
workbook.save(path.join(dataDir, "LineWithDataMarkerChart.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## **Temas avanzados**
- [Leer y manipular los gráficos de Excel 2016](/cells/es/nodejs-cpp/read-and-manipulate-excel-2016-charts/)
- [Gestionar los ejes de los gráficos de Excel](/cells/es/nodejs-cpp/chart-axes/)
- [Configurar la apariencia del gráfico](/cells/es/nodejs-cpp/setting-chart-appearance/)
- [Tipos de gráficos](/cells/es/nodejs-cpp/chart-types/)
- [Personalizar gráficos](/cells/es/nodejs-cpp/customizing-charts/)
- [Establecer la fuente de datos para el gráfico](/cells/es/nodejs-cpp/data-formatting-in-charts/)
- [Gestionar las etiquetas de datos de los gráficos de Excel](/cells/es/nodejs-cpp/insert-datalabels-to-chart/)
- [Obtener hoja de cálculo del gráfico](/cells/es/nodejs-cpp/get-worksheet-of-the-chart/)
- [Gestionar leyenda de gráficos de Excel](/cells/es/nodejs-cpp/chart-legend/)
- [Manipular tamaño de posición y diseñar gráfico](/cells/es/nodejs-cpp/manipulate-position-size-and-designer-chart/)
- [Crear gráficos circulares con líneas de líder](/cells/es/nodejs-cpp/creating-pie-chart-with-leader-lines/)
- [Formas en gráficos](/cells/es/nodejs-cpp/controls-in-charts/)
- [Gestionar títulos de gráficos de Excel](/cells/es/nodejs-cpp/chart-and-axis-titles/)
- [Representación de gráficos](/cells/es/nodejs-cpp/chart-rendering/)
- [Obtener texto de la ecuación de la línea de tendencia del gráfico](/cells/es/nodejs-cpp/get-equation-text-of-chart-trendline/)
{{< app/cells/assistant language="nodejs-cpp" >}}
