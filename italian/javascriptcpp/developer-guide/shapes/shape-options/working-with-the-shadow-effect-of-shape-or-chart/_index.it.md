---
title: Lavorare con l effetto Ombra di Forma o Grafico con JavaScript via C++
linktitle: Lavorare con l Effetto Ombra di una Forma o di un Grafico
type: docs
weight: 220
url: /it/javascript-cpp/working-with-the-shadow-effect-of-shape-or-chart/
description: Impara come lavorare con l effetto ombra di forme o grafici usando Aspose.Cells for JavaScript via C++.
---

## **Possibili Scenari di Utilizzo**  
Aspose.Cells for JavaScript via C++ fornisce la proprietà [Shape.shadowEffect](https://reference.aspose.com/cells/javascript-cpp/shape/#shadowEffect--) insieme alla classe [ShadowEffect](https://reference.aspose.com/cells/javascript-cpp/shadoweffect) per lavorare con l'effetto ombra di forma o grafico. La classe [ShadowEffect](https://reference.aspose.com/cells/javascript-cpp/shadoweffect) contiene le seguenti proprietà che possono essere impostate per ottenere risultati diversi secondo le esigenze dell'applicazione.  

- [ShadowEffect.angle](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#angle--)  
- [ShadowEffect.blur](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#blur--)  
- [ShadowEffect.color](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#color--)  
- [ShadowEffect.distance](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#distance--)  
- [ShadowEffect.presetType](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#presetType--)  
- [ShadowEffect.size](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#size--)  
- [EffettoOmbra.transparenza](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#transparency--)  

## **Lavorare con l'Effetto Ombra della forma o del grafico**  
Il seguente esempio di codice carica il [file excel di origine](5115425.xlsx) e accede alla prima forma nel primo foglio di lavoro impostando le sottopropietà della proprietà [Forma.effettoOmbra](https://reference.aspose.com/cells/javascript-cpp/shape/#shadowEffect--) e poi salva il workbook nel [file excel di output](5115411.xlsx).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Shape Shadow Effect Example</h1>
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
            const shape = worksheet.shapes.get(0);

            const shadowEffect = shape.shadowEffect;
            shadowEffect.angle = 150;
            shadowEffect.blur = 4;
            shadowEffect.distance = 45;
            shadowEffect.transparency = 0.3;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shadow effect applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
