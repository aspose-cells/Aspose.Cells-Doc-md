---
title: Leer y manipular gráficos de Excel 2016 con JavaScript mediante C++
linktitle: Leer y manipular gráficos de Excel 2016
description: Aprende cómo leer y manipular gráficos de Excel 2016 usando Aspose.Cells for JavaScript mediante C++. Esta guía mostrará cómo acceder y modificar diversas propiedades de los gráficos.
keywords: Aspose.Cells for JavaScript mediante C++, gráficos de Excel 2016, lectura, manipulación, etiquetas de datos, colores de series, diseño, gráficos jerárquicos, gráficos circulares.
type: docs
weight: 48
url: /es/javascript-cpp/read-and-manipulate-excel-2016-charts/
---

## **Escenarios de uso posibles**  
Aspose.Cells ahora admite la lectura y manipulación de gráficos de Microsoft Excel 2016 que no están presentes en Microsoft Excel 2013 o versiones anteriores.  
## **Leer y manipular los gráficos de Excel 2016**  
El siguiente código de ejemplo carga el archivo [Excel fuente](22774101.xlsx) que contiene gráficos de Excel 2016 en la primera hoja. Lee todos los gráficos uno por uno y cambia su título según su tipo de gráfico. La siguiente captura de pantalla muestra el archivo Excel fuente antes de la ejecución del código. Como se puede ver, el título del gráfico es el mismo para todos.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_1.png)

La siguiente captura de pantalla muestra el [archivo de Excel de salida](22774104.xlsx) después de la ejecución del código. Como puede ver, el título del gráfico se ha cambiado según su tipo de gráfico.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_2.png)  
## **Código de muestra**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read and Update Chart Titles</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Read selected file
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet which contains the charts
            const sheet = workbook.worksheets.get(0);

            // Access all charts one by one and read their types
            const chartsCount = sheet.charts.count;
            let logHtml = '<ul>';
            for (let i = 0; i < chartsCount; i++) {
                // Access the chart
                const ch = sheet.charts.get(i);

                // Read chart type
                const typeStr = ch.type.toString();
                console.log(typeStr);

                // Change the title of the chart
                ch.title.text = "Chart Type is " + typeStr;

                logHtml += `<li>Chart ${i}: ${typeStr}</li>`;
            }
            logHtml += '</ul>';

            // Save the workbook to a downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_excel2016Charts.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Charts updated successfully! Click the download link to get the modified file.</p>' + logHtml;
        });
    </script>
</html>
```  
## **Salida de la consola**  


{{< highlight javascript >}}  

 Waterfall  

Treemap  

Sunburst  

Histogram  

BoxWhisker  

{{< /highlight >}}  

## **Temas avanzados**  
- [Creación de gráfico de cascada](/cells/es/javascript-cpp/creating-waterfall-chart/)  
- [Creación de gráfico de mapa de árbol](/cells/es/javascript-cpp/creating-treemap-chart/)  
- [Creación de gráfico de ráfaga solar](/cells/es/javascript-cpp/creating-sunburst-chart/)
