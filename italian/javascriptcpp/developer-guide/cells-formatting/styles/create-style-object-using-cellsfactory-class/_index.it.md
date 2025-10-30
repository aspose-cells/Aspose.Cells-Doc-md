---
title: Creare un oggetto di stile utilizzando la classe CellsFactory
linktitle: Creare un oggetto di stile utilizzando la classe CellsFactory
description: Impara come creare un oggetto stile di cella utilizzando la classe CellsFactory in Aspose.Cells for JavaScript via C++. Personalizza l aspetto delle celle del foglio di calcolo secondo necessità.
keywords: Aspose.Cells, JavaScript via C++, foglio elettronico, oggetto stile, stile cella, personalizzazione
type: docs
weight: 70
url: /it/javascript-cpp/create-style-object-using-cellsfactory-class/
---

## **Crea un oggetto Style utilizzando la classe CellsFactory**
Il seguente esempio di codice crea un oggetto [Style](https://reference.aspose.com/cells/javascript-cpp/style) utilizzando la classe [CellsFactory](https://reference.aspose.com/cells/javascript-cpp/cellsfactory) e quindi imposta lo Stile Predefinito del workbook. Scarica il [file Excel di output](5115153.xlsx) per vedere i risultati di questo codice di riferimento.


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
