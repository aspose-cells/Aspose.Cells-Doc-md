---
title: Cómo crear un gráfico Sunburst con JavaScript vía C++
linktitle: Cómo crear un gráfico de anillo solar
description: Aprende a crear un gráfico Sunburst en Aspose.Cells for JavaScript vía C++, un gráfico que presenta datos en un círculo. Nuestra guía te ayudará a configurar varias propiedades y formatos de tu gráfico, incluyendo etiquetas de datos, leyendas, colores y más.
keywords: Aspose.Cells for JavaScript vía C++, gráfico de Sunburst, crear, establecer propiedades, etiquetas de datos, leyenda, formato, color, círculo, renderizado de datos.
type: docs
weight: 162
url: /es/javascript-cpp/creating-sunburst-chart/
---

## **Escenarios de uso posibles**
Los gráficos de árbol de mapa son buenos para comparar proporciones dentro de la jerarquía; sin embargo, los gráficos de árbol de mapa no son ideales para mostrar niveles jerárquicos entre las categorías más grandes y cada punto de datos. Un gráfico de estallido solar es mucho mejor para mostrar eso. El gráfico de estallido solar es ideal para mostrar datos jerárquicos. Cada nivel de la jerarquía se representa mediante un aro o círculo, con el círculo más interior como la cima de la jerarquía. Un gráfico de estallido solar sin datos jerárquicos (un nivel de categorías) se parece a un gráfico de dona. Sin embargo, un gráfico de estallido solar con múltiples niveles de categorías muestra cómo los anillos exteriores se relacionan con los interiores. El gráfico de estallido solar es más efectivo para mostrar cómo un aro se divide en sus piezas contribuyentes, mientras que otro tipo de gráfico jerárquico, el gráfico de mapa de árbol, es ideal para comparar tamaños relativos.

![todo:image_alt_text](sample.png)
## **Gráfico de ráfaga solar**
Después de ejecutar el código a continuación, verá el gráfico de ráfaga solar como se muestra a continuación.

![todo:image_alt_text](result.png)
## **Código de muestra**
El siguiente código de muestra carga el [archivo de Excel de muestra](sunburst.xlsx) y genera el [archivo de Excel de salida](out.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Sunburst Chart Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Sunburst Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);

            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.Sunburst, 5, 6, 25, 12);
            const chart = worksheet.charts.get(pieIdx);

            chart.showLegend = true;
            chart.title.text = "Sunburst Chart";
            chart.nSeries.add("D2:D16", true);
            chart.nSeries.categoryData = "A2:C16";
            chart.nSeries.get(0).dataLabels.showCategoryName = true;
            chart.plotArea.area.fillFormat.fillType = AsposeCells.FillType.None;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sunburst chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
