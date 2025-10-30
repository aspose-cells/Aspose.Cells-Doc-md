---
title: Invia Forma in Primo Piano o Dietro all’interno dell’Foglio di Lavoro con JavaScript tramite C++
linktitle: Invia la forma avanti o indietro all interno del foglio di lavoro
type: docs
weight: 3400
url: /it/javascript-cpp/send-shape-front-or-back-inside-the-worksheet/
description: Impara come inviare una forma in primo piano o dietro in un foglio di lavoro usando Aspose.Cells for JavaScript via C++. 
---

## **Possibili Scenari di Utilizzo**

Quando ci sono più forme nello stesso punto, la loro visibilità è determinata dalle posizioni z-order. Aspose.Cells fornisce il metodo [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/javascript-cpp/shape/#toFrontOrBack-number-), che cambia la posizione z-order della forma. Per inviare una forma in secondo piano, utilizza un numero negativo come -1, -2, -3, ecc., e per portare una forma in primo piano, utilizza un numero positivo come 1, 2, 3, ecc.

## **Invia la forma avanti o indietro all'interno del foglio di lavoro**

Il seguente esempio spiega l'uso del metodo [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/javascript-cpp/shape/#toFrontOrBack-number-). Guarda il [file Excel di esempio](50528330.xlsx) usato nel codice e il [file Excel di output](50528331.xlsx) generato. Lo screenshot mostra l'effetto del codice sul file Excel di esempio dopo l'esecuzione.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Send Shapes Front or Back</title>
    </head>
    <body>
        <h1>Send Shapes to Front or Back Example</h1>
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
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Access first and fourth shapes
            const shape1 = worksheet.shapes.get(0);
            const shape4 = worksheet.shapes.get(3);

            // Print the Z-Order position of shape1
            resultDiv.innerHTML = `<p>Z-Order Shape 1: ${shape1.zOrderPosition}</p>`;

            // Send this shape to front
            shape1.toFrontOrBack(2);

            // Print the Z-Order position of shape4
            resultDiv.innerHTML += `<p>Z-Order Shape 4: ${shape4.zOrderPosition}</p>`;

            // Send this shape to back
            shape4.toFrontOrBack(-2);

            // Saving the modified Excel file and preparing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputToFrontOrBack.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML += '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
