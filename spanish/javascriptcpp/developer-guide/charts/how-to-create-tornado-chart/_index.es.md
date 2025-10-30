---
title: Cómo crear un gráfico de tornado con JavaScript a través de C++
linktitle: Cómo crear un gráfico de tornado
type: docs
weight: 73
url: /es/javascript-cpp/create-tornado-chart/
description: Aprende cómo crear un gráfico de tornado con Script Aspose.Cells for Java a través de la API C++.
keywords: Crear un gráfico de tornado en JavaScript, agregar un gráfico de tornado, insertar un gráfico de tornado
---

## **Introducción**
Un gráfico tornado, también conocido como diagrama tornado o gráfico tornado, es un tipo de visualización de datos que se utiliza a menudo para análisis de sensibilidad en Excel. Te ayuda a comprender el impacto de cambiar variables en un resultado particular.

## **Cómo crear un gráfico tornado en Excel**
Puedes crear un gráfico tornado en Excel siguiendo estos pasos:
1. Selecciona los datos y ve a Insertar --> Gráficos --> Insertar gráfico de columnas o barras --> Gráfico de barras apiladas. Haz clic en él.
<br>
<img src="1.png" width=70% />
2. Cambia el eje Y: Haz clic derecho en el eje Y. Haz clic en formato de eje. En etiquetas, haz clic en posición de la etiqueta desplegable y selecciona elemento inferior.
<br>
<img src="2.png" width=70% />
3. Selecciona cualquier barra y ve a formato. Establece un ancho de espacio adecuado.
<br>
<img src="3.png" width=70% />
4. Vamos a quitar el signo menos (-) del gráfico tornado. Selecciona el eje X. Ve a formato. En las opciones del eje, haz clic en el número. En categoría, selecciona personalizado. En código de formato escribe ###0,###0. Haz clic en añadir.
<br>
<img src="4.png" width=70% />
5. haz clic en el eje Y y ve a las opciones del eje. En las opciones del eje, marca Categorías en orden inverso.
<br>
<img src="5.png" width=70% />

## **Cómo agregar un gráfico de tornado en Script Aspose.Cells for Java a través de C++**
Por favor, consulta el siguiente código de muestra. Carga el [archivo de Excel de muestra](sample.xlsx) que contiene algunos datos de ejemplo. Luego, crea el gráfico de barras apiladas basado en los datos iniciales y establece propiedades relevantes. Finalmente, guarda el libro de trabajo en [formato XLSX de salida](out.xlsx). La siguiente captura de pantalla muestra el gráfico tornado creado por Aspose.Cells en el archivo de Excel de salida.
<br>
<img src="6.png" width=70% />

### **Código de muestra**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);
            const charts = sheet.charts;

            // Add bar chart
            const index = charts.add(AsposeCells.ChartType.BarStacked, 8, 1, 24, 8);
            const chart = charts.get(index);

            // Set data for bar chart
            chart.chartDataRange = "A1:C7";

            // Set properties for bar chart
            chart.title.text = "Tornado chart";
            chart.style = 2;
            chart.plotArea.area.foregroundColor = AsposeCells.Color.White;
            chart.plotArea.border.color = AsposeCells.Color.White;
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;

            chart.categoryAxis.tickLabelPosition = AsposeCells.TickLabelPositionType.Low;
            chart.category```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);
            const charts = sheet.charts;

            // Add bar chart
            const index = charts.add(AsposeCells.ChartType.BarStacked, 8, 1, 24, 8);
            const chart = charts.get(index);

            // Set data for bar chart
            chart.chartDataRange = "A1:C7";

            // Set properties for bar chart
            chart.title.text = "Tornado chart";
            chart.style = 2;
            chart.plotArea.area.foregroundColor = AsposeCells.Color.White;
            chart.plotArea.border.color = AsposeCells.Color.White;
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;

            chart.categoryAxis.tickLabelPosition = AsposeCells.TickLabelPositionType.Low;
            chart.categoryAxis.isPlotOrderReversed = true;

            chart.gapWidth = 10;

            const valueAxis = chart.valueAxis;
            valueAxis.tickLabels.numberFormat = "#,##0;#,##0";

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
