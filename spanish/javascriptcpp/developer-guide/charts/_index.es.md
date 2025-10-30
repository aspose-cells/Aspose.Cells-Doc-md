---
title: Crear y gestionar gráficos con JavaScript vía C++
linktitle: Gráficos
description: Aprende cómo usar Aspose.Cells for JavaScript vía C++ para crear gráficos en Microsoft Excel. Nuestra guía demostrará varios tipos de gráficos y cómo personalizar su apariencia y formato.
keywords: Aspose.Cells for JavaScript vía C++, creación de gráficos, Microsoft Excel, tipos de gráficos, personalización, apariencia, formato.
type: docs
weight: 130
url: /es/javascript-cpp/creating-charts/
---

{{% alert color="primary" %}}

Es posible agregar una variedad de gráficos a hojas de cálculo con Aspose.Cells. Aspose.Cells proporciona muchos objetos de gráficos flexibles. Este tema discute los objetos de gráficos de Aspose.Cells.

{{% /alert %}}

## **Creando gráficos**

### **Simplemente creando un gráfico**
Es simple crear un gráfico con Aspose.Cells con los siguientes ejemplos de código:
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object with the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding sample values to cells
            worksheet.cells.get("A2").value = "Category1";
            worksheet.cells.get("A3").value = "Category2";
            worksheet.cells.get("A4").value = "Category3";

            worksheet.cells.get("B1").value = "Column1";
            worksheet.cells.get("B2").value = 4;
            worksheet.cells.get("B3").value = 20;
            worksheet.cells.get("B4").value = 50;

            worksheet.cells.get("C1").value = "Column2";
            worksheet.cells.get("C2").value = 50;
            worksheet.cells.get("C3").value = 100;
            worksheet.cells.get("C4").value = 150;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Setting chart data source as the range "A1:C4"
            chart.chartDataRange = { range: "A1:C4", isSeriesInRows: true };

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
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

 Agregue cualquier tipo de gráfico a una hoja usando la colección [**charts**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#charts--). Cada elemento en la colección [**charts**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#charts--) representa un objeto [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/). Un objeto [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/) encapsula todos los demás objetos de gráficos necesarios para personalizar la apariencia del gráfico. La siguiente sección muestra cómo usar algunos objetos básicos de gráficos para crear un gráfico simple.

### **Crear gráfico usando Aspose.Cells**



 1. Agregue algunos datos a las celdas de la hoja con el método [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell/) del objeto [**putValue(string)**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-string-).
   Esto se utilizará como fuente de datos para el gráfico.
2. Añade un gráfico a la hoja de cálculo llamando al método [**add**](https://reference.aspose.com/cells/javascript-cpp/chartcollection/#add-charttype-number-number-number-number-) de la colección [**ChartCollection**](https://reference.aspose.com/cells/javascript-cpp/chartcollection), encapsulado en el objeto [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet/).
3. Especifica el tipo de gráfico con la enumeración [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/).
    Por ejemplo, el ejemplo a continuación usa el valor [**ChartType.Pyramid**](https://reference.aspose.com/cells/javascript-cpp/charttype) como tipo de gráfico.
4. Accede al nuevo objeto [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/) desde la colección [**Charts**](https://reference.aspose.com/cells/javascript-cpp/chartcollection) pasando su índice.
5. Usa cualquiera de los objetos de gráficos encapsulados en el objeto [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/) para gestionar el gráfico.
    El ejemplo a continuación usa el objeto de gráficos [**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection/) para especificar la fuente de datos del gráfico.

 Cuando agregue datos fuente al gráfico, la fuente puede ser un rango de celdas (como "A1:C3"), o una secuencia de celdas no contiguas (como "A1, A3, A5"), o una secuencia de valores (como "1,2,3").

Estos pasos generales le permiten crear cualquier tipo de gráfico. Utilice diferentes objetos de gráficos para crear distintos gráficos.

Es posible crear muchos tipos diferentes de gráficos con Aspose.Cells. Todos los gráficos estándar admitidos por Aspose.Cells están predefinidos en una enumeración llamada [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/).

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

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Chart and Download</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');

            // If a file is provided, load it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 20;
            worksheet.cells.get("B3").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Pyramid, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and chart added. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

#### **Gráfico de líneas**

 En el ejemplo anterior, simplemente cambiar el [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/) por *Línea* crea un gráfico de línea. La fuente completa se proporciona a continuación. Cuando se ejecuta el código, se añade un gráfico de línea a la hoja de cálculo.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Chart</title>
    </head>
    <body>
        <h1>Add Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 20;
            worksheet.cells.get("B3").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(AsposeCells.ChartType.Line, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

#### **Gráfico de burbujas**

 Para crear un gráfico de burbujas, el [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/) debe establecerse en [**ChartType.Bubble**](https://reference.aspose.com/cells/javascript-cpp/charttype) y algunas propiedades adicionales como BubbleSizes, Values y XValues deben configurarse en consecuencia. Al ejecutar el siguiente código, se añade un gráfico de burbajas a la hoja.

#### **Gráfico de líneas con marcadores de datos**

 Para crear un gráfico de línea con marcador de datos, el [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/) debe establecerse en *ChartType.LineWithDataMarkers* y algunas propiedades adicionales como área de fondo, marcadores de serie, valores y XValues deben configurarse en consecuencia. Al ejecutar el siguiente código, se añade un gráfico de línea con marcador de datos a la hoja.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Line With Data Marker Chart</title>
    </head>
    <body>
        <h1>Line With Data Marker Chart Example</h1>
        <p>You may optionally select an existing Excel file to modify, or leave empty to create a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (fileInput.files.length === 0) {
                // Proceed with a new workbook if no file selected
            }

            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');

            // Instantiate or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Set columns title 
            worksheet.cells.get(0, 0).putValue("X");
            worksheet.cells.get(0, 1).putValue("Y");

            // Random data shall be used for generating the chart
            // Create random data and save in the cells
            for (let i = 1; i < 21; i++) {
                worksheet.cells.get(i, 0).putValue(i);
                worksheet.cells.get(i, 1).putValue(0.8);
            }

            for (let i = 21; i < 41; i++) {
                worksheet.cells.get(i, 0).putValue(i - 20);
                worksheet.cells.get(i, 1).putValue(0.9);
            }

            // Add a chart to the worksheet
            const idx = worksheet.charts.add(AsposeCells.ChartType.LineWithDataMarkers, 1, 3, 20, 20);

            // Access the newly created chart
            const chart = worksheet.charts.get(idx);

            // Set chart style
            chart.style = 3;

            // Set autoscaling value to true
            chart.autoScaling = true;

            // Set foreground color white
            chart.plotArea.area.foregroundColor = AsposeCells.Color.White;

            // Set Properties of chart title
            chart.title.text = "Sample Chart";

            // Set chart type
            chart.type = AsposeCells.ChartType.LineWithDataMarkers;

            // Set Properties of categoryaxis title
            chart.categoryAxis.title.text = "Units";

            //Set Properties of nseries
            const s2_idx = chart.nSeries.add("A2:A2", true);
            const s3_idx = chart.nSeries.add("A22:A22", true);

            // Set IsColorVaried to true for varied points color
            chart.nSeries.isColorVaried = true;

            // Set properties of background area and series markers
            const series2 = chart.nSeries.get(s2_idx);
            series2.area.formatting = AsposeCells.FormattingType.Custom;
            series2.marker.area.foregroundColor = AsposeCells.Color.Yellow;
            series2.marker.border.isVisible = false;

            // Set X and Y values of series chart
            series2.xValues = "A2:A21";
            series2.values = "B2:B21";

            // Set properties of background area and series markers for series3
            const series3 = chart.nSeries.get(s3_idx);
            series3.area.formatting = AsposeCells.FormattingType.Custom;
            series3.marker.area.foregroundColor = AsposeCells.Color.Green;
            series3.marker.border.isVisible = false;

            // Set X and Y values of series chart
            series3.xValues = "A22:A41";
            series3.values = "B22:B41";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'LineWithDataMarkerChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            result.innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Temas avanzados**
- [Leer y manipular los gráficos de Excel 2016](/cells/es/javascript-cpp/read-and-manipulate-excel-2016-charts/)
- [Gestionar los ejes de los gráficos de Excel](/cells/es/javascript-cpp/chart-axes/)
- [Configurar la apariencia del gráfico](/cells/es/javascript-cpp/setting-chart-appearance/)
- [Tipos de gráficos](/cells/es/javascript-cpp/chart-types/)
- [Personalizar gráficos](/cells/es/javascript-cpp/customizing-charts/)
- [Establecer la fuente de datos para el gráfico](/cells/es/javascript-cpp/data-formatting-in-charts/)
- [Gestionar las etiquetas de datos de los gráficos de Excel](/cells/es/javascript-cpp/insert-datalabels-to-chart/)
- [Obtener hoja de cálculo del gráfico](/cells/es/javascript-cpp/get-worksheet-of-the-chart/)
- [Gestionar leyenda de gráficos de Excel](/cells/es/javascript-cpp/chart-legend/)
- [Manipular tamaño de posición y diseñar gráfico](/cells/es/javascript-cpp/manipulate-position-size-and-designer-chart/)
- [Crear gráficos circulares con líneas de líder](/cells/es/javascript-cpp/creating-pie-chart-with-leader-lines/)
- [Formas en gráficos](/cells/es/javascript-cpp/controls-in-charts/)
- [Gestionar títulos de gráficos de Excel](/cells/es/javascript-cpp/chart-and-axis-titles/)
- [Representación de gráficos](/cells/es/javascript-cpp/chart-rendering/)
- [Obtener texto de la ecuación de la línea de tendencia del gráfico](/cells/es/javascript-cpp/get-equation-text-of-chart-trendline/)
