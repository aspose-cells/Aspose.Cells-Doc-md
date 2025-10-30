---
title: Cambia il formato di una cella
linktitle: Cambia il formato di una cella
description: Come utilizzare la libreria Aspose.Cells in JavaScript tramite C++ per modificare la formattazione delle celle, inclusi font, colore, bordo, ecc. Regolando queste proprietà, hai un maggiore controllo sull aspetto delle celle.
keywords: Aspose.Cells, formattazione celle, JavaScript via C++, font, colore, bordo
type: docs
weight: 20
url: /it/javascript-cpp/how-to-change-format-of-cell/
---

## **Possibili Scenari di Utilizzo**
Quando si desidera evidenziare determinati dati, è possibile modificare lo stile delle celle.

## **Come cambiare il formato di una cella in Excel**

Per cambiare il formato di una singola cella in Excel, seguire questi passaggi:

1. Apri Excel e apri il foglio di lavoro che contiene la cella da formattare.

2. Trova la cella che si desidera formattare.

3. Fai clic con il pulsante destro del mouse sulla cella e seleziona "Formato celle" dal menu contestuale. In alternativa, è possibile selezionare la cella e andare alla scheda Home nel nastro di Excel, fare clic sul menu a discesa "Formato" nel gruppo "Celle" e selezionare "Formato celle".

4. Comparirà la finestra di dialogo "Formato celle". Qui è possibile scegliere varie opzioni di formattazione da applicare alla cella selezionata. Ad esempio, è possibile cambiare lo stile del carattere, la dimensione del carattere, il colore del carattere, il formato numerico, i bordi, il colore di sfondo, ecc. Esplora le diverse schede nella finestra di dialogo per accedere alle varie opzioni di formattazione.

5. Dopo aver apportato le modifiche di formattazione desiderate, fare clic sul pulsante "OK" per applicare la formattazione alla cella selezionata.


## **Come cambiare il formato di una cella usando JavaScript**

Per modificare il formato di una cella usando Aspose.Cells, puoi usare i seguenti metodi:
1. [Cell.style(Style)](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-)
2. [Cell.style(Style, explicitFlag)](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-boolean-)
3. [Cell.style(Style, StyleFlag)](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-styleflag-)


## **Codice di Esempio**
In questo esempio, creiamo una cartella di lavoro Excel, aggiungiamo alcuni dati di esempio, accediamo al primo foglio di lavoro e otteniamo due celle ("A2" e "B3"). Quindi, otteniamo lo stile della cella, impostiamo varie opzioni di formattazione (ad esempio, colore del font, grassetto) e cambiamo il formato della cella. Infine, salviamo la cartella di lavoro in un nuovo file.
![todo:image_alt_text](change-format.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Instantiating a Workbook object by opening the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells
            let cell = cells.get("A1");
            cell.value = "Fruit";
            cell = cells.get("B1");
            cell.value = "Count";
            cell = cells.get("C1");
            cell.value = "Price";

            cell = cells.get("A2");
            cell.value = "Apple";
            cell = cells.get("A3");
            cell.value = "Mango";
            cell = cells.get("A4");
            cell.value = "Blackberry";
            cell = cells.get("A5");
            cell.value = "Cherry";

            cell = cells.get("B2");
            cell.value = 5;
            cell = cells.get("B3");
            cell.value = 3;
            cell = cells.get("B4");
            cell.value = 6;
            cell = cells.get("B5");
            cell.value = 4;

            cell = cells.get("C2");
            cell.value = 5;
            cell = cells.get("C3");
            cell.value = 20;
            cell = cells.get("C4");
            cell.value = 30;
            cell = cells.get("C5");
            cell.value = 60;

            // Access the worksheet
            const worksheet = workbook.worksheets.get(0);

            const a2 = worksheet.cells.get("A2");

            // Get style of A2
            const style = a2.style;

            // Change the format
            style.font.color = AsposeCells.Color.Red;
            style.font.isBold = true;

            const flag = new AsposeCells.StyleFlag();
            flag.fontColor = true;
            // Apply style (assignment per conversion rules)
            a2.style = style;

            const b3 = worksheet.cells.get("B3");
            // Get style of B3
            const style2 = b3.style;

            // Change the format
            style2.font.color = AsposeCells.Color.Blue;
            style2.font.isItalic = true;
            b3.style = style2;

            // Saving the modified workbook and offering it for download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
