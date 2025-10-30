---
title: Determina si los puntos de datos están en la segunda sección de pastel o barra en un gráfico de pastel de pastel o barra de pastel con JavaScript vía C++  
linktitle: Encuentre si los Puntos de Datos están en el Segundo Círculo o Barra en un Gráfico de Círculo de Círculos o Barra de Círculos  
description: Aprende a usar Aspose.Cells for JavaScript vía C++ para determinar si los puntos de datos están en la segunda sección de pastel o barra en un gráfico de pastel de pastel o barra de pastel. Esta guía demostrará cómo identificar y acceder a la sección o barra secundaria en un gráfico compuesto, permitiendo analizar y manipular los datos eficazmente.  
keywords: Aspose.Cells for JavaScript vía C++, Gráfico de pastel de pastel, Gráfico de barra de pastel, Segundo pastel, Segundo barra, Análisis de datos, Manipulación de datos.  
type: docs  
weight: 180  
url: /es/javascript-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/  
---  

## **Escenarios de uso posibles**  
Puedes saber si los puntos de datos de una serie están en el segundo pastel en un gráfico *Pastel de pastel* o en la barra de *Barra de pastel* usando Aspose.Cells for JavaScript vía C++. Utiliza la propiedad [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/javascript-cpp/chartpoint/#isInSecondaryPlot--) para determinarlo.  

Por favor, descarga el [archivo Excel de ejemplo](5115193.xlsx) utilizado en el siguiente código de ejemplo y revisa su salida en la consola. Si abres el [archivo Excel de ejemplo](5115193.xlsx), encontrarás que todos los puntos de datos menores a 10 están dentro de la barra del gráfico *Bar of Pie* como también especifica la salida en consola.  
## **Encontrar si los Puntos de Datos están en el Segundo Pastel o Barra en un Gráfico de Pastel de Pastel o de Barra de Pastel**  
El siguiente código de ejemplo muestra cómo determinar si los puntos de datos están en la segunda tarta o barra en un gráfico *Pie of Pie* o *Bar of Pie*.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Bar of Pie Chart Data Points Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            resultDiv.innerHTML = '';
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (e.g., PieBars.xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first chart which is Bar of Pie chart and calculate it
            const chart = worksheet.charts.get(0);
            chart.calculate();

            // Access the chart series
            const series = chart.nSeries.get(0);

            // Iterate and collect output
            let outputLines = [];
            for (let i = 0; i < series.points.count; i++) {
                // Access chart point
                const chartPoint = series.points.get(i);

                // Skip null values
                if (chartPoint.yValue === null) continue;

                // Print the chart point value and see if it is inside bar or pie.
                // If the IsInSecondaryPlot is true, then the data point is inside bar 
                // otherwise it is inside the pie. 
                const valueLine = "Value: " + chartPoint.yValue;
                const inSecondaryLine = "IsInSecondaryPlot: " + chartPoint.isInSecondaryPlot();
                console.log(valueLine);
                console.log(inSecondaryLine);
                console.log();

                outputLines.push(valueLine);
                outputLines.push(inSecondaryLine);
                outputLines.push("");
            }

            if (outputLines.length === 0) {
                resultDiv.innerHTML = '<p style="color: orange;">No data points found or all values are null.</p>';
            } else {
                resultDiv.innerHTML = '<pre>' + outputLines.join('\n') + '</pre>';
            }
        });
    </script>
</html>
```  
## **Salida de la consola**  
Por favor, consulta la salida de consola generada tras la ejecución del código de ejemplo anterior con el [archivo de Excel de muestra](5115193.xlsx). Si [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/javascript-cpp/chartpoint/#isInSecondaryPlot--) es **falso**, el punto de datos está en el Pastel o si es **verdadero**, entonces el punto de datos está en la Barra.  

{{< highlight javascript >}}  
 Value: 15  
IsInSecondaryPlot: false  

Value: 9  
IsInSecondaryPlot: true  

Value: 2  
IsInSecondaryPlot: true  

Value: 40  
IsInSecondaryPlot: false  

Value: 5  
IsInSecondaryPlot: true  

Value: 4  
IsInSecondaryPlot: true  

Value: 25  
IsInSecondaryPlot: false  
{{< /highlight >}}
