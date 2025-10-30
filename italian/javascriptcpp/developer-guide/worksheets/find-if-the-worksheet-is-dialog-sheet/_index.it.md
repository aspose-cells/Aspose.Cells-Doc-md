---
title: Trovare se il foglio di lavoro è un foglio di dialogo con JavaScript tramite C++
linktitle: Verificare se il foglio di lavoro è un foglio di dialogo
type: docs
weight: 90
url: /it/javascript-cpp/find-if-the-worksheet-is-dialog-sheet/
description: Questo articolo fornisce istruzioni e codice di esempio per determinare programmaticamente se un foglio di lavoro di Excel è un foglio di dialogo usando Aspose.Cells for JavaScript tramite C++.
keywords: trovare il tipo di dialogo del foglio di lavoro Excel JavaScript tramite C++, dialogo del foglio di lavoro JavaScript tramite C++
---

## **Possibili Scenari di Utilizzo**

Il Foglio di Dialogo è un vecchio formato di foglio che contiene una finestra di dialogo. Tale foglio potrebbe essere stato inserito da una versione più vecchia di Microsoft Excel ad esempio 2003, come mostrato in questa schermata. Può anche essere inserito con VBA in versioni più recenti ad esempio Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Puoi determinare se il foglio è un foglio di dialogo o di altro tipo tramite la proprietà [**Worksheet.type**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#type--) fornita da Aspose.Cells for JavaScript tramite C++. Se restituisce il valore di enumerazione [**SheetType.Dialog**](https://reference.aspose.com/cells/javascript-cpp/sheettype), significa che stai trattando con un foglio di dialogo.

## **Trova se il foglio di lavoro è un foglio di dialogo**

Il codice di esempio seguente carica il [file Excel di esempio](64716820.xlsx) che contiene un foglio di dialogo. Controlla la proprietà [**Worksheet.type**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#type--), la confronta con [**SheetType.Dialog**](https://reference.aspose.com/cells/javascript-cpp/sheettype) e quindi stampa il messaggio. Per favore, guarda l’output della console del codice di esempio di seguito per ulteriori informazioni.

## **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Detect Dialog Sheet</title>
    </head>
    <body>
        <h1>Detect if Worksheet Is a Dialog Sheet</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Find if the sheet type is dialog and print the message
            if (ws.type === AsposeCells.SheetType.Dialog) {
                document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet is a Dialog Sheet.</p>';
            } else {
                document.getElementById('result').innerHTML = '<p>Worksheet is NOT a Dialog Sheet.</p>';
            }
        });
    </script>
</html>
```

## **Output della console**

{{< highlight js >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
