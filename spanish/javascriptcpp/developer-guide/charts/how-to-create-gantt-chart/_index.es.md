---
title: Cómo crear un diagrama de Gantt con JavaScript a través de C++
linktitle: Cómo crear un gráfico de Gantt
type: docs
weight: 72
url: /es/javascript-cpp/how-to-create-gantt-chart/
description: Aprende cómo crear un diagrama de Gantt con Script Aspose.Cells for Java a través de la API C++.
keywords: Crear un diagrama de Gantt en JavaScript, agregar un diagrama de Gantt, insertar un diagrama de Gantt
---

## **Qué es un gráfico de Gantt**

Un gráfico de Gantt es un tipo de gráfico de barras que ilustra un cronograma de proyecto. Muestra las fechas de inicio y fin de los diferentes elementos de un proyecto. Cada tarea o actividad está representada por una barra, cuya duración corresponde a su período. Los gráficos de Gantt también indican dependencias entre tareas, permitiendo a los gerentes de proyecto visualizar la secuencia en la que las tareas deben completarse. Son ampliamente utilizados en la gestión de proyectos para planificar, programar y rastrear proyectos de manera efectiva.

## **Cómo crear un gráfico de Gantt en Excel**

Puedes crear un gráfico de Gantt en Excel siguiendo estos pasos:
1. Agrega algunos datos para el gráfico de Gantt. 
<br>
<img src="00.png" width=50% />
1. Selecciona los datos y ve a Insertar --> Gráficos --> Insertar gráfico de columnas o barras --> Barra apilada. En nuestro ejemplo, eso es B1:B7, y luego Inserta un gráfico de **barra apilada**.
<br>
<img src="1.png" width=50% />

1. Selecciona el gráfico, **Seleccionar datos** -> **Agregar**, configura el **Nombre de la serie** y los **Valores de la serie** como sigue.
<br>
<img src="2.png" width=50% />

1. Selecciona el gráfico, edita las **Etiquetas del eje horizontal (categoría)**.
<br>
<img src="3.png" width=50% />

1. **Formatear eje** la Eje Y, selecciona **Categorías en orden inverso**.
1. Selecciona la **Serie Azul** y establece **Relleno -> Sin relleno**.
1. **Formatear eje** en el eje X, establece los **Mínimo y Máximo** (1/5/2019:43470, 1/30/2019:43494).
<br>
<img src="4.png" width=50% />

1. **Agregar etiquetas de datos** para el gráfico, ahora obtendrás un gráfico de Gantt.
<br>
<img src="0.png" width=50% />


## **Cómo agregar un gráfico de Gantt en Aspose.Cells**
Por favor, vea el siguiente código de ejemplo. Carga el [archivo de Excel de ejemplo](sample.xlsx) que contiene algunos datos de muestra. Luego crea el gráfico de barras apiladas basado en los datos iniciales y establece las propiedades relevantes. Finalmente, guarda el libro de trabajo en [formato XLSX de salida](result.xlsx). La siguiente captura de pantalla muestra el gráfico de Gantt creado por Aspose.Cells en el archivo de Excel de salida.
<br>
<img src="5.png" width=60% />

### **Código de muestra**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Chart Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Create BarStacked Chart
            const i = worksheet.charts.add(AsposeCells.ChartType.BarStacked, 5, 6, 20, 15);

            // Retrieve the Chart object
            const chart = worksheet.charts.get(i);

            // Set the chart title name 
            chart.title.text = "Gantt Chart";

            // Set the chart title is Visible
            chart.title.isVisible = true;

            // Set data range
            chart.chartDataRange = "B1:B6";

            // Add series data range
            chart.nSeries.add("C2:C6", true);

            // No fill for one serie
            chart.nSeries.get(0).area.fillFormat.fillType = AsposeCells.FillType.None;

            // Set the Horizontal(Category) Axis
            chart.nSeries.setCategoryData("A2:A6");

            // Reverse the Horizontal(Category) Axis
            chart.categoryAxis.isPlotOrderReversed = true;

            // Set the value axis's MinValue and MaxValue
            const minValue = parseFloat(worksheet.cells.get("B2").value);
            const maxValue = parseFloat(worksheet.cells.get("D6").value);
            chart.valueAxis.minValue = isNaN(minValue) ? 0 : minValue;
            chart.valueAxis.maxValue = isNaN(maxValue) ? 0 : maxValue;

            chart.plotArea.area.fillFormat.fillType = AsposeCells.FillType.None;

            // Show the DataLabels
            chart.nSeries.get(1).dataLabels.showValue = true;

            // Disable the Legend
            chart.showLegend = false;

            // Save the result
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
