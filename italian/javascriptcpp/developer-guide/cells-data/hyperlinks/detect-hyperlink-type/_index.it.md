---
title: Rileva il tipo di collegamento ipertestuale
type: docs
weight: 160
url: /it/javascript-cpp/detect-hyperlink-type/
description: Impara come rilevare il tipo di collegamento ipertestuale tramite Aspose.Cells for JavaScript tramite API C++.
keywords: Rileva il tipo di collegamento ipertestuale JavaScript tramite C++, Rileva il tipo di collegamento ipertestuale JavaScript tramite C++, Ottieni il tipo di collegamento ipertestuale JavaScript tramite C++
---

## **Rilevare il tipo di collegamento ipertestuale**

Un file Excel può avere diversi tipi di collegamenti ipertestuali come esterni, riferimento a cella, percorso del file, ecc. Aspose.Cells for JavaScript tramite C++ supporta la funzione di rilevamento del tipo di collegamento ipertestuale. I tipi di collegamenti ipertestuali sono rappresentati dall’enumerazione [**TargetModeType**](https://reference.aspose.com/cells/javascript-cpp/targetmodetype). L’enumerazione [**TargetModeType**](https://reference.aspose.com/cells/javascript-cpp/targetmodetype) ha i seguenti membri.

- Esterno: collegamento esterno
- FilePath: Percorso locale e completo ai file/cartelle.
- Email: Email
- RiferimentoCella: Link a cella o intervallo nominato.

Per controllare il tipo di collegamento ipertestuale, la classe [**Hyperlink**](https://reference.aspose.com/cells/javascript-cpp/hyperlink) fornisce una proprietà [**linkType**](https://reference.aspose.com/cells/javascript-cpp/hyperlink/#linkType--) con un tipo di ritorno [**TargetModeType**](https://reference.aspose.com/cells/javascript-cpp/targetmodetype). Il seguente frammento di codice dimostra l’uso della proprietà [**linkType**](https://reference.aspose.com/cells/javascript-cpp/hyperlink/#linkType--) usando questo [file Excel di origine](94896195.xlsx).

### Codice Sorgente

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Link Types Example</title>
    </head>
    <body>
        <h1>Link Types Example</h1>
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

                // Get the first (default) worksheet
                const worksheet = workbook.worksheets.get(0);

                // Create a range A1:A7 (original code created A1:B7 but used A1 to A7 in parameters)
                const range = worksheet.cells.createRange("A1", "A7");

                // Get Hyperlinks in range
                const hyperlinks = range.hyperlinks;

                let outputHtml = '<p>Hyperlinks found:</p><ul>';
                if (typeof hyperlinks.forEach === 'function') {
                    hyperlinks.forEach(link => {
                        outputHtml += `<li>${link.textToDisplay}: ${link.linkType}</li>`;
                    });
                } else {
                    for (let i = 0; i < hyperlinks.count; i++) {
                        const link = hyperlinks.get(i);
                        outputHtml += `<li>${link.textToDisplay}: ${link.linkType}</li>`;
                    }
                }
                outputHtml += '</ul>';

                resultDiv.innerHTML = outputHtml;
            });
        });
    </script>
</html>
```


Di seguito è riportato l'output generato dal frammento di codice indicato sopra.

### Output della console
