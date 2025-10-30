---
title: Cómo establecer un punto como total con JavaScript a través de C++
linktitle: Cómo establecer un punto como total
description: Aprende a establecer puntos como total en gráficos WaterFall usando Script Aspose.Cells for Java a través de C++.
keywords: Gráfico WaterFall, Punto, Establecer como total, JavaScript a través de C++
type: docs
weight: 72
url: /es/javascript-cpp/how-to-set-point-as-total/
---

## ¿Qué es "Establecer punto como total" en el gráfico de Excel?

En algunos gráficos de Excel, por ejemplo, un gráfico de cascada, algunos datos de puntos son la suma de los puntos anteriores, y puede que necesites "establecer punto como total". Mostraremos el código de ejemplo y la ilustración a continuación.

## Un gráfico de cascada necesita "Establecer punto como total" 

![todo:image_alt_text](set-as-total1.png)

Esta imagen muestra un gráfico WaterFall en Excel. Podemos ver que hay cuatro puntos de datos empezando con "Total", y se usan para contar todos los puntos de datos anteriores. En esta imagen, las configuraciones no son exactamente correctas. Cuando seleccionamos el punto "Total 2024", podemos ver que la opción "Establecer como total" no está marcada en Excel. Adjunto abajo está el [archivo Excel de ejemplo](SampleSheet.xlsx) que necesita ser modificado, y usaremos Script Aspose.Cells for Java a través de C++ para configurarlo correctamente.

## Usar Script Aspose.Cells for Java a través de C++ para "Establecer punto como total" 

Usamos el siguiente código para configurar el archivo correctamente:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Chart Subtotals Example</title>
    </head>
    <body>
        <h1>Set Chart Subtotals Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the chart named "Graphiq5"
            const chart = worksheet.charts.get("Graphiq5");

            // set some points as total column 
            // In this example, we set points 0, 4, 8, 12 as total
            chart.nSeries.get(0).layoutProperties.subtotals = [0, 4, 8, 12];

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Puedes obtener el siguiente [archivo de salida correcto](output.xlsx)

Como se muestra en la figura a continuación, los cuatro puntos de datos "Total" están configurados correctamente, y puedes ver la diferencia respecto a la gráfica anterior.

![todo:image_alt_text](set-as-total2.png)
