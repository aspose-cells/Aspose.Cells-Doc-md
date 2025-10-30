---
title: Lavorare con l effetto alone di forma o grafico con JavaScript tramite C++
linktitle: Lavorare con l effetto Glow della forma o del grafico
type: docs
weight: 240
url: /it/javascript-cpp/working-with-the-glow-effect-of-shape-or-chart/
description: Impara come lavorare con l effetto alone di forme o grafici in JavaScript usando Aspose.Cells for JavaScript tramite C++.
---

## **Possibili Scenari di Utilizzo**  
Aspose.Cells fornisce la proprietà [Shape.glow](https://reference.aspose.com/cells/javascript-cpp/shape/#glow--) insieme alla classe [GlowEffect](https://reference.aspose.com/cells/javascript-cpp/gloweffect/) per lavorare con l'effetto alone di forma o grafico. La classe [GlowEffect](https://reference.aspose.com/cells/javascript-cpp/gloweffect/) contiene le seguenti proprietà che possono essere impostate per ottenere risultati diversi secondo le esigenze dell'applicazione.  

- [GlowEffect.size](https://reference.aspose.com/cells/javascript-cpp/gloweffect/#size--)  
- [GlowEffect.transparency](https://reference.aspose.com/cells/javascript-cpp/gloweffect/#transparency--)  
- [GlowEffect.color](https://reference.aspose.com/cells/javascript-cpp/gloweffect/#color--)  

## **Lavorare con l'effetto Glow della forma o del grafico**  
Il seguente esempio di codice carica il [file excel sorgente](5115407.xlsx) e accede alla prima forma nel primo foglio di lavoro impostando le sotto-proprietà della proprietà [Shape.glow](https://reference.aspose.com/cells/javascript-cpp/shape/#glow--) e quindi salva il workbook in [file excel di output](5115414.xlsx).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Glow Effect</title>
    </head>
    <body>
        <h1>Apply Glow Effect to First Shape</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Apply Glow Effect</button>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first shape
            const shape = worksheet.shapes.get(0);

            // Set the glow effect of the shape, Set its Size and Transparency properties
            const glowEffect = shape.glow;
            glowEffect.size = 30;
            glowEffect.transparency = 0.4;

            // Save the workbook in xlsx format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Glow effect applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
