---
title: Cómo crear un gráfico TreeMap con JavaScript vía C++
linktitle: Cómo crear un gráfico TreeMap
description: Aprende a crear un gráfico Treemap en Aspose.Cells for JavaScript vía C++. Nuestra guía te ayudará a entender las diversas propiedades y opciones de formato disponibles para los gráficos Treemap, incluyendo colores, etiquetas y representación de datos.
keywords: Aspose.Cells for JavaScript vía C++, gráfico Treemap, crear, propiedades, formato, colores, etiquetas, representación de datos, gráfico circular, gráfico jerárquico.
type: docs
weight: 161
url: /es/javascript-cpp/creating-treemap-chart/
---

## **Escenarios de uso posibles**  
Un gráfico Treemap proporciona una vista jerárquica de sus datos y facilita detectar patrones, como cuáles son los artículos más vendidos de una tienda. Las ramas del árbol están representadas por rectángulos y cada subrama se muestra como un rectángulo más pequeño. El gráfico Treemap muestra categorías por color y proximidad y puede mostrar fácilmente muchos datos que serían difíciles con otros tipos de gráficos.  

![todo:image_alt_text](sample.png)  
## **Gráfico TreeMap**  
Después de ejecutar el código a continuación, verá el gráfico TreeMap como se muestra a continuación.  

![todo:image_alt_text](result.png)  
## **Código de muestra**  
El siguiente código de muestra carga el [archivo de Excel de muestra](treemap.xlsx) y genera el [archivo de Excel de salida](out.xlsx).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Treemap Chart Example</title>
    </head>
    <body>
        <h1>Treemap Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, FillType } = AsposeCells;

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

            // Instantiate Workbook with uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);
            // Add a Treemap chart at row 5, column 6 with height 20 and width 12
            const pieIdx = worksheet.charts.add(ChartType.Treemap, 5, 6, 20, 12);
            // Retrieve the Chart object
            const chart = worksheet.charts.get(pieIdx);
            // Set the legend to be shown
            chart.showLegend = true;
            // Set the chart title text
            chart.title.text = "TreeMap Chart";
            // Add series data range (D2:F13)
            chart.nSeries.add("D2:F13", true);
            // Set category data (A2:C13)
            chart.nSeries.setCategoryData("A2:C13");
            // Show the DataLabels with category names for first series
            chart.nSeries.get(0).dataLabels.showCategoryName = true;
            // Fill the PlotArea area with nothing
            chart.plotArea.area.fillFormat.fillType = FillType.None;

            // Save the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Treemap chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
