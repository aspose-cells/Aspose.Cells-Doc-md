---
title: Utilizza la proprietà Sheet.SheetId di OpenXml usando Aspose.Cells for JavaScript tramite C++
linktitle: Utilizzare la proprietà Sheet.SheetId di OpenXml utilizzando Aspose.Cells
type: docs
weight: 200
url: /it/javascript-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/
description: Questo articolo dimostra come utilizzare la proprietà Sheet.SheetId di OpenXml usando Excel manipulation con Aspose.Cells for JavaScript tramite C++ programmaticamente.
keywords: ID foglio proprietà di openxml JavaScript tramite C++, ID foglio di lavoro Excel JavaScript tramite C++
---

## **Possibili Scenari di Utilizzo**

La proprietà *Sheet.SheetId* è disponibile all’interno del modulo *DocumentFormat.OpenXml.Spreadsheet* ed è parte di OpenXml. Puoi vedere questa proprietà e il suo valore all’interno di *workbook.xml* come mostrato nello screenshot seguente. Aspose.Cells fornisce la proprietà equivalente come [**Worksheet.tabId**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#tabId--).

![todo:image_alt_text](utilize-sheet-sheetid-property-of-openxml-using-aspose-cells_1.png)

## **Utilizza la proprietà Sheet.SheetId di OpenXml usando Aspose.Cells for JavaScript tramite C++**

Il codice di esempio seguente carica il [file Excel di esempio](51740716.xlsx), legge il suo ID della scheda o tabulato, quindi ne assegna un nuovo ID della scheda e lo salva come [file Excel di output](51740717.xlsx). Si prega di vedere anche l'output della console del codice sottostante per un riferimento.

## **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Sheet Id Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Print its Sheet or Tab Id on console and show in page
            console.log("Sheet or Tab Id: " + ws.tabId);
            resultDiv.innerHTML = `<p>Original Sheet or Tab Id: ${ws.tabId}</p>`;

            // Change Sheet or Tab Id
            ws.tabId = 358;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSheetId.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML += `<p style="color: green;">Sheet Id changed to ${ws.tabId}. Click the download link to get the modified file.</p>`;
        });
    </script>
</html>
```

## **Output della console**

{{< highlight text >}}

Sheet or Tab Id: 1297

{{< /highlight >}}
