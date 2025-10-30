---
title: Aggiungi filigrana WordArt al grafico con JavaScript via C++
linktitle: Aggiungere WordArt come Filigrana al Grafico
description: Impara come usare Aspose.Cells for JavaScript via C++ per aggiungere una filigrana WordArt a un grafico in Microsoft Excel. La nostra guida dimostrerà come creare e posizionare una filigrana WordArt per migliorare l’appeal visivo e l’unicità del tuo grafico.
keywords: Aspose.Cells for JavaScript, Filigrana WordArt, Filigrana del grafico, Microsoft Excel, Appeal Visivo, Unicità del Grafico.
type: docs
weight: 50
url: /it/javascript-cpp/add-wordart-watermark-to-chart/
---

{{% alert color="primary" %}}  

Puoi usare WordArt per aggiungere effetti speciali al testo nei fogli di calcolo. Ad esempio, estendere un titolo, decorare il testo, far si che il testo si adatti a una forma predefinita o applicare il testo interessato all'area di tracciamento di un grafico come filigrana. Il WordArt diventa un oggetto che puoi spostare o posizionare nei tuoi fogli di calcolo per aggiungere decorazioni.  

L'esempio seguente mostra come aggiungere una forma WordArt come filigrana per l'area di tracciamento del grafico.  

{{% /alert %}}  

L'esempio seguente mostra come aggiungere una forma WordArt come watermark all'area di trama di un grafico esistente.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add WordArt Watermark to Chart</h1>
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

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet's first chart
            const chart = workbook.worksheets.get(0).charts.get(0);

            // Add a WordArt watermark (shape) to the chart's plot area
            const wordart = chart.shapes.addTextEffectInChart(AsposeCells.MsoPresetTextEffect.TextEffect2,
                "CONFIDENTIAL", "Arial Black", 66, false, false, 1200, 500, 2000, 3000);

            // Get the shape's fill format and set transparency
            const wordArtFormat = wordart.fill;
            wordArtFormat.transparency = 0.9;

            // Get the line format and set weight to invisible (0.0)
            const lineFormat = wordart.line;
            lineFormat.weight = 0.0;

            // Save the modified workbook to a downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">WordArt watermark added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
