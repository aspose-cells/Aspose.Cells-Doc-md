---
title: Aggiungi filigrana WordArt al foglio di lavoro con JavaScript tramite C++
linktitle: Gestire WordArt
type: docs
weight: 180
url: /it/javascript-cpp/add-wordart-watermark-to-worksheet/
description: Impara come aggiungere WordArt come filigrana di sfondo a un foglio di lavoro usando Aspose.Cells for JavaScript tramite C++.
---

{{% alert color="primary" %}} 

Usa WordArt per aggiungere effetti speciali al testo nei fogli di calcolo. Ad esempio, distendi un titolo sulla parte superiore del file, decora il testo e fai adattare il testo a una forma preimpostata, o applica il testo a un foglio di Excel come un watermark di sfondo. Il WordArt diventa un oggetto che puoi spostare o posizionare nei fogli di calcolo per aggiungere decorazioni.

{{% /alert %}} 

L'esempio seguente mostra come aggiungere una forma WordArt per impostare un watermark di sfondo per un foglio di lavoro.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Watermark Example</h1>
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

            // If a file is provided, open it. Otherwise create a new workbook.
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get the first default sheet
            const sheet = workbook.worksheets.get(0);

            // Add Watermark
            const wordart = sheet.shapes.addTextEffect(AsposeCells.MsoPresetTextEffect.TextEffect1,
                "CONFIDENTIAL", "Arial Black", 50, false, true, 18, 8, 1, 1, 130, 800);

            // Get the fill format of the word art
            const wordArtFormat = wordart.fill;            

            // Set the transparency
            wordArtFormat.transparency = 0.9;

            // Make the line invisible
            const lineFormat = wordart.line;
            lineFormat.visible = false;

            // Saving the modified Excel file (Excel97-2003 format .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Watermark_Test.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File with Watermark';

            document.getElementById('result').innerHTML = '<p style="color: green;">Watermark added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Argomenti avanzati**
- [Aggiungi testo Word Art con stili incorporati](/cells/it/javascript-cpp/add-word-art-text-with-built-in-styles/)
- [Bloccare WordArt Come Filigrana](/cells/it/javascript-cpp/locking-wordart-watermark/)
- [Imposta lo stile predefinito di WordArt al testo della forma](/cells/it/javascript-cpp/set-preset-wordart-style-to-the-text-of-the-shape/)
