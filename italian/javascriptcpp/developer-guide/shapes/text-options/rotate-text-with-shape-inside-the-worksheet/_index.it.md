---
title: Ruotare il testo con forma all interno del foglio di lavoro usando JavaScript tramite C++
linktitle: Ruota il testo con la forma all interno del foglio di lavoro
type: docs
weight: 1300
url: /it/javascript-cpp/rotate-text-with-shape-inside-the-worksheet/
description: Impara come ruotare il testo con la forma all interno di un foglio di lavoro Excel usando Aspose.Cells for JavaScript tramite C++.
---

## **Possibili Scenari di Utilizzo**

Puoi aggiungere del testo all’interno di qualsiasi forma utilizzando Microsoft Excel. Se aggiungi una forma usando la vecchia versione di Microsoft Excel 2003, il testo non ruoterà con la forma. Se invece usi versioni più recenti di Microsoft Excel, ad esempio 2007, 2010, 2013 o 2016, ecc., il testo ruoterà con la forma. Puoi controllare se il testo deve ruotare con la forma o meno usando la proprietà [**ShapeTextAlignment.rotateTextWithShape**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/#rotateTextWithShape--). Il valore predefinito è **true**, che significa che il testo ruoterà con la forma, ma se lo imposti come **false**, il testo non ruoterà con la forma.

## **Ruota il testo con la forma all'interno del foglio di lavoro**

Il seguente codice di esempio carica il [file Excel di esempio](64716896.xlsx) che ha una forma triangolare e il suo testo ruota con la forma. Se apri il file Excel di esempio in Microsoft Excel e ruoti la forma triangolare, il testo ruoterà anche con essa. Il codice imposta poi la proprietà [**ShapeTextAlignment.rotateTextWithShape**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/#rotateTextWithShape--) come **false** e lo salva come [file Excel di output](64716897.xlsx). Se ora apri il file Excel di output in Microsoft Excel e ruoti la forma triangolare, il testo non ruoterà con essa. Consulta la schermata seguente che mostra l'effetto del codice sul file Excel di esempio per riferimento.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Rotate Text With Shape</title>
    </head>
    <body>
        <h1>Rotate Text With Shape Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access cell B4 and add message inside it.
            const cellB4 = worksheet.cells.get("B4");
            cellB4.value = "Text is not rotating with shape because RotateTextWithShape is false.";

            // Access first shape.
            const shape = worksheet.shapes.get(0);

            // Access shape text alignment.
            const shapeTextAlignment = shape.textBody.textAlignment;

            // Do not rotate text with shape by setting RotateTextWithShape as false.
            shapeTextAlignment.rotateTextWithShape = false;

            // Saving the modified Excel file and providing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRotateTextWithShapeInsideWorksheet.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
