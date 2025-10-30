---
title: Obtener la hoja de cálculo del gráfico con JavaScript vía C++
linktitle: Obtener hoja de cálculo del gráfico
description: Aprende cómo recuperar la hoja de cálculo asociada a un gráfico de Excel usando Aspose.Cells for JavaScript vía C++. Accede y manipula de forma eficiente los datos subyacentes del gráfico.
keywords: Aspose.Cells for JavaScript, gráficos de Excel, hojas de cálculo, manipulación de datos, datos subyacentes, operaciones, JavaScript vía C++
type: docs
weight: 1000
url: /es/javascript-cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

A veces, quieres acceder a una hoja de cálculo desde una referencia de un gráfico. Aspose.Cells proporciona la propiedad [**Chart.worksheet**](https://reference.aspose.com/cells/javascript-cpp/chart/#worksheet--) que devuelve la referencia de la hoja de cálculo que contiene el gráfico.

{{% /alert %}}

El siguiente ejemplo muestra cómo usar la propiedad [**Chart.worksheet**](https://reference.aspose.com/cells/javascript-cpp/chart/#worksheet--). El código primero imprime el nombre de la hoja, luego accede al primer gráfico en la hoja. Después, imprime nuevamente el nombre de la hoja, usando la propiedad [**Chart.worksheet**](https://reference.aspose.com/cells/javascript-cpp/chart/#worksheet--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Print worksheet name
            const sheetName = worksheet.name;
            let outputHtml = `<p>Sheet Name: ${sheetName}</p>`;

            // Access the first chart inside this worksheet
            const charts = worksheet.charts;
            if (charts.count > 0) {
                const chart = charts.get(0);

                // Access the chart's sheet and display its name again
                const chartSheetName = chart.worksheet.name;
                outputHtml += `<p>Chart's Sheet Name: ${chartSheetName}</p>`;
            } else {
                outputHtml += `<p>No charts available in the worksheet.</p>`;
            }

            document.getElementById('result').innerHTML = outputHtml;
        });
    </script>
</html>
```

A continuación se muestra la salida de la consola que produce el código de ejemplo. Como puedes ver, imprime el mismo nombre de hoja de cálculo ambas veces.

{{< highlight javascript >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
