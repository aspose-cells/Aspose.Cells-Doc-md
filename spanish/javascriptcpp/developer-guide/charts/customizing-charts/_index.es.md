---
title: Personalización de gráficos con JavaScript vía C++
linktitle: Personalización de gráficos
description: Aprende cómo personalizar gráficos en Aspose.Cells for JavaScript vía C++. Nuestra guía te mostrará cómo modificar diseños del gráfico, agregar y dar formato a las series de datos, ajustar los ejes y aplicar varias opciones de formato para mejorar la apariencia y usabilidad de tus gráficos.
keywords: Aspose.Cells for JavaScript vía C++, gráficos, personalización, diseños, series de datos, ejes, formato, apariencia, usabilidad.
type: docs
weight: 40
url: /es/javascript-cpp/customizing-charts/
---

## **Creación de gráficos personalizados**  

Hasta ahora, cuando hemos discutido sobre gráficos, hemos visto gráficos estándar que tienen su configuración de formato estándar. Solo definimos la fuente de datos, configuramos algunas propiedades y el gráfico se crea con su configuración predeterminada. Pero las API de Aspose.Cells también soportan la creación de gráficos personalizados que permiten a los desarrolladores crear gráficos con sus propios ajustes de formato.  

Los desarrolladores pueden crear gráficos personalizados en tiempo de ejecución utilizando Aspose.Cells.  

Un gráfico se compone de una serie de datos. Cada serie de datos en Aspose.Cells está representada por un objeto [**Series**](https://reference.aspose.com/cells/javascript-cpp/series) mientras que el objeto [**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection) sirve como colección de objetos [**Series**](https://reference.aspose.com/cells/javascript-cpp/series). Al crear un gráfico personalizado, los desarrolladores tienen la libertad de usar diferentes tipos de gráficos para diferentes series de datos (recogidas en el objeto [**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection)).  

El código de ejemplo a continuación demuestra cómo crear gráficos personalizados. En este ejemplo, vamos a usar un gráfico de columnas para la primera serie de datos y un gráfico de líneas para la segunda serie. El resultado es que agregamos un gráfico de columnas, combinado con un gráfico de líneas, a la hoja de cálculo.  

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
            // Ensure Aspose.Cells is initialized
            await readyPromise;

            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("A4").value = 110;
            worksheet.cells.get("B1").value = 260;
            worksheet.cells.get("B2").value = 12;
            worksheet.cells.get("B3").value = 50;
            worksheet.cells.get("B4").value = 100;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding NSeries (chart data source) to the chart ranging from "A1" cell to "B4"
            chart.nSeries.add("A1:B4", true);

            // Setting the chart type of 2nd NSeries to display as line chart
            chart.nSeries.get(1).type = ChartType.Line;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  

Actualmente, Aspose.Cells solo soporta gráficos personalizados que combinan gráficos de pastel, línea, columna y apilados, pero en futuras versiones se soportarán más gráficos.  

{{% /alert %}}
