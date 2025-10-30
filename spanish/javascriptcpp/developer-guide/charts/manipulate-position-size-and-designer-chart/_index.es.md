---
title: Manipular posición, tamaño y diseñador del gráfico con JavaScript vía C++
linktitle: Manipular la Posición, Tamaño y Diseño del Gráfico
description: Aprende cómo usar Aspose.Cells for JavaScript vía C++ para manipular eficazmente la posición, tamaño y diseño del gráfico en Microsoft Excel. Nuestra guía demostrará cómo ajustar estas propiedades para mejorar el diseño y la visualización.
keywords: Aspose.Cells for JavaScript vía C++, Posición, Tamaño, Gráfico de diseño, Microsoft Excel, Diseño, Visualización.
type: docs
weight: 45
url: /es/javascript-cpp/manipulate-position-size-and-designer-chart/
---

## **Posición y Tamaño del Gráfico**
A veces, quieres cambiar la posición o tamaño del gráfico nuevo o existente dentro de la hoja de cálculo. Aspose.Cells proporciona la propiedad [Chart.chartObject](https://reference.aspose.com/cells/javascript-cpp/chart/#chartObject--) para lograr esto. Puedes usar sus subpropiedades para redimensionar el gráfico con una nueva altura y anchura o reposicionarlo con nuevas coordenadas X e Y.

### **Controlar la Posición y Tamaño del Gráfico**
Para cambiar la posición (coordenadas X, Y) o el tamaño (altura, ancho) del gráfico, use estas propiedades:

1. [Shape.x](https://reference.aspose.com/cells/javascript-cpp/shape/#x--)
1. [Shape.y](https://reference.aspose.com/cells/javascript-cpp/shape/#y--)
1. [Shape.height](https://reference.aspose.com/cells/javascript-cpp/shape/#height--)
1. [Shape.width](https://reference.aspose.com/cells/javascript-cpp/shape/#width--)

El siguiente ejemplo explica el uso de las APIs anteriores; carga el libro de trabajo existente que contiene un gráfico en su primera hoja. Luego redimensiona y vuelve a ubicar el gráfico usando Aspose.Cells.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Resize and Reposition Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the second worksheet in the Excel file (index 1)
            const worksheet = workbook.worksheets.get(1);

            // Load the chart from source worksheet (first chart)
            const chart = worksheet.charts.get(0);

            // Resize the chart
            chart.chartObject.width = 400;
            chart.chartObject.height = 300;

            // Reposition the chart
            chart.chartObject.x = 250;
            chart.chartObject.y = 150;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Chart resized and repositioned successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Manipulación de gráficos de diseñador**
Hay ocasiones en las que necesitas manipular o modificar gráficos en archivos de plantilla de diseño. Aspose.Cells soporta totalmente la manipulación de contenidos y elementos de gráficos de diseño. Los datos, contenidos del gráfico, imagen de fondo y formato pueden ser conservados con precisión.

### **Manipulación de gráficos de diseñador en archivos de plantillas**
Para manipular gráficos de diseñadores en archivos de plantilla, utiliza la API relacionada con gráficos. Por ejemplo, puedes usar la propiedad Worksheet.charts para obtener la colección de gráficos existentes en el archivo de plantilla.

#### **Creación de un gráfico**
El siguiente ejemplo muestra cómo crear un gráfico de pirámide. Más adelante manipularemos este gráfico.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Create Workbook with Pyramid Chart</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
            await readyPromise;

            // Instantiating a Workbook object
            const workbook = new Workbook();

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
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and chart added. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

#### **Manipulación del gráfico**
El siguiente ejemplo muestra cómo manipular el gráfico existente. En este ejemplo, modificamos el gráfico creado anteriormente. En la salida generada, se observa que la etiqueta de fecha de un punto de datos se ha establecido en 'Reino Unido, 30K'.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Pie Chart Data Label Update</title>
    </head>
    <body>
        <h1>Update Pie Chart Data Label Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart in the second sheet.
            const sheet = workbook.worksheets.get(1);
            const chart = sheet.charts.get(0);

            // Get the data labels in the data series of the third data point.
            const dataLabels = chart.nSeries.get(0).points.get(2).dataLabels;

            // Change the text of the label.
            dataLabels.text = "Unided Kingdom, 400K ";

            // Save the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Data label updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

#### **Manipulación de un gráfico de líneas en la plantilla de diseñador**
En este ejemplo, manipularemos un gráfico de líneas. Agregaremos algunas series de datos al gráfico existente y cambiaremos sus colores de línea.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Series Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart in the first worksheet.
            const worksheet = workbook.worksheets.get(0);
            const chart = worksheet.charts.get(0);

            // Add the third data series to it.
            chart.nSeries.add("{60, 80, 10}", true);

            // Add another data series (fourth) to it.
            chart.nSeries.add("{0.3, 0.7, 1.2}", true);

            // Plot the fourth data series on the second axis.
            chart.nSeries.get(3).plotOnSecondAxis = true;

            // Change the Border color of the second data series.
            chart.nSeries.get(1).border.color = AsposeCells.Color.Green;

            // Change the Border color of the third data series.
            chart.nSeries.get(2).border.color = AsposeCells.Color.Red;

            // Make the second value axis visible.
            chart.secondValueAxis.isVisible = true;

            // Save the excel file and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
