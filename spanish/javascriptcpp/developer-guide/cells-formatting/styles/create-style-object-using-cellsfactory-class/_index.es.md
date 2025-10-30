---
title: Crear objeto de estilo usando la clase CellsFactory
linktitle: Crear objeto de estilo usando la clase CellsFactory
description: Aprende cómo crear un objeto de estilo de celda usando la clase CellsFactory en Aspose.Cells for JavaScript vía C++. Personaliza la apariencia de las celdas de la hoja de cálculo según sea necesario.
keywords: Aspose.Cells, JavaScript vía C++, hoja de cálculo electrónica, objeto de estilo, estilo de celda, personalización
type: docs
weight: 70
url: /es/javascript-cpp/create-style-object-using-cellsfactory-class/
---

## **Crear objeto de estilo usando la clase CellsFactory**
El siguiente ejemplo de código crea un objeto [Style](https://reference.aspose.com/cells/javascript-cpp/style) usando la clase [CellsFactory](https://reference.aspose.com/cells/javascript-cpp/cellsfactory) y luego establece el Estilo Predeterminado del libro. Descarga el [archivo Excel de salida](5115153.xlsx) para ver los resultados de este código como referencia.


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook with Default Style</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsFactory, BackgroundType, Color, Utils } = AsposeCells;

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
            // Create a Style object using CellsFactory class
            const cf = new CellsFactory();
            const st = cf.createStyle();

            // Set the Style fill color to Yellow
            st.pattern = BackgroundType.Solid;
            st.foregroundColor = Color.Yellow;

            // Create a workbook and set its default style using the created Style object
            const wb = new Workbook();
            wb.defaultStyle = st;

            // Save the workbook
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```
