---
title: Encuentra el tipo de valores de X e Y de los puntos en la serie del gráfico con JavaScript vía C++
linktitle: Encontrar el tipo de valores X e Y de los puntos en la serie del gráfico
description: Aprende cómo determinar el tipo de valores de X e Y en los puntos de la serie del gráfico usando Aspose.Cells for JavaScript vía C++. Esta guía explica los tipos de valores de datos y cómo acceder y trabajar con ellos en tus gráficos.
keywords: Aspose.Cells for JavaScript vía C++, gráficos, valores de X, valores de Y, tipos de datos, acceder, trabajar con, serie del gráfico.
type: docs
weight: 150
url: /es/javascript-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Escenarios de uso posibles**  
A veces, quieres conocer el tipo de valores de X e Y de los puntos en un gráfico. Aspose.Cells for JavaScript vía C++ proporciona las propiedades `ChartPoint.XValueType` y `ChartPoint.YValueType` que pueden usarse para este propósito. Ten en cuenta que debes llamar al método `Chart.calculate()` antes de poder usar estas propiedades eficazmente.  

## **Encontrar el tipo de valores X e Y de los puntos en la serie del gráfico**  
El siguiente código de ejemplo carga el [archivo de ejemplo en Excel](64716905.xlsx) y accede al primer gráfico dentro de la primera hoja. Luego llama al método `Chart.calculate()` y encuentra el tipo de valores X e Y del primer punto del gráfico, imprimiéndolos en la consola. Consulta la salida de la consola a continuación como referencia.  

## **Código de muestra**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Find Type Of X and Y Values Of Points In Chart Series</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access first chart.
            const chart = worksheet.charts.get(0);

            // Calculate chart data.
            chart.calculate();

            // Access first chart point in the first series.
            const point = chart.nSeries.get(0).points.get(0);

            // Get the types of X and Y values of chart point.
            const xValueType = point.xValueType;
            const yValueType = point.yValueType;

            // Display results
            document.getElementById('result').innerHTML = `
                <p style="color: green;">Operation completed successfully!</p>
                <p>X Value Type: ${xValueType}</p>
                <p>Y Value Type: ${yValueType}</p>
            `;
        });
    </script>
</html>
```  

## **Salida de la consola**  

{{< highlight java >}}  
 X Value Type: IsString  

Y Value Type: IsNumeric  
{{< /highlight >}}
