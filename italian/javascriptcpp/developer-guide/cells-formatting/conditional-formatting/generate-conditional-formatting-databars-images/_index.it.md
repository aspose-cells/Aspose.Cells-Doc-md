---
title: Genera immagini di formattazione condizionale DataBars
linktitle: Genera immagini di formattazione condizionale DataBars
description: Aspose.Cells è una libreria JavaScript per lavorare con i file di fogli di calcolo. Supporta la generazione di barre dati formattate condizionalmente e immagini, consentendo agli utenti di personalizzare la visualizzazione del foglio di calcolo in base al valore delle celle. Questo articolo introdurrà come usare la libreria Aspose.Cells per generare barre dati e immagini formattate condizionalmente.
keywords: Aspose.Cells, Formattazione condizionale, Barre dati, Immagini, Fogli di calcolo, JavaScript via C++
type: docs
weight: 40
url: /it/javascript-cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

A volte è necessario generare immagini delle barre di dati formattate condizionalmente. È possibile utilizzare il [**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/javascript-cpp/databar/#toImage-cell-imageorprintoptions-) metodo di Aspose.Cells per generare queste immagini. Questo articolo mostra come generare un'immagine di DataBar utilizzando Aspose.Cells.

{{% /alert %}}

Il seguente esempio di codice genera l'immagine DataBar della cella C1. Prima accede all'oggetto condizione di formato della cella, e da quell'oggetto, accede all'oggetto [**DataBar**](https://reference.aspose.com/cells/javascript-cpp/databar) e usa il suo metodo [**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/javascript-cpp/databar/#toImage-cell-imageorprintoptions-) per generare l'immagine della cella. Infine, salva l'immagine sul disco.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Generate DataBar Image</title>
    </head>
    <body>
        <h1>Generate DataBar Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Creating a workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the cell which contains conditional formatting databar
            const cell = worksheet.cells.get("C1");

            // Create and get the conditional formatting of the worksheet
            const idx = worksheet.conditionalFormattings.add();
            const fcc = worksheet.conditionalFormattings.get(idx);
            fcc.addCondition(AsposeCells.FormatConditionType.DataBar);
            fcc.addArea(AsposeCells.CellArea.createCellArea("C1", "C4"));

            // Access the conditional formatting databar
            const dbar = fcc.get(0).dataBar;

            // Create image or print options
            const opts = new AsposeCells.ImageOrPrintOptions();
            opts.imageType = AsposeCells.ImageType.Png;

            // Get the image bytes of the databar
            const imgBytes = dbar.toImage(cell, opts);

            // Create a blob and provide download link
            const blob = new Blob([imgBytes], { type: "image/png" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputGenerateDatabarImage.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Generated DataBar Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image generated successfully! Click the download link to save the PNG file.</p>';
        });
    </script>
</html>
```
