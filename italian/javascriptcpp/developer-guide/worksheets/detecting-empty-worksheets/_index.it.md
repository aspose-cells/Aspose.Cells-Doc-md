---
title: Rilevare fogli di lavoro vuoti con JavaScript tramite C++
linktitle: Rilevamento di fogli di lavoro vuoti
type: docs
weight: 410
url: /it/javascript-cpp/detecting-empty-worksheets/
description: Questo articolo ti mostra come rilevare programmaticamente i fogli di lavoro vuoti dei file Excel usando API JavaScript con libreria C++.
keywords: rilevare foglio di lavoro vuoto JavaScript tramite C++, trovare foglio di lavoro Excel vuoto JavaScript tramite C++
---

## **Controllare le celle popolate**

I fogli di lavoro possono avere uno o più celle riempite con valori, dove un valore può essere semplice (testo, numerico, data/ora) o una formula o un valore basato su formula. In questo caso, è facile rilevare se un dato foglio di lavoro è vuoto o meno. Tutto ciò che dobbiamo verificare sono le proprietà [**Cells.maxDataRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataRow--) o [**Cells.maxDataColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataColumn--). Se le suddette proprietà restituiscono zero o valori positivi, significa che una o più celle sono state popolate; tuttavia, se qualcuna di queste proprietà restituisce -1, indica che nessuna delle celle è stata popolata nel foglio di lavoro dato.

{{% alert color="primary" %}}

Le collezioni di righe & colonne hanno indici basati su zero; pertanto, una cella alla riga 0 e colonna 0 indica la prima cella nel foglio di lavoro, che è A1.

{{% /alert %}}

## **Controllare le celle inizializzate vuote**

Tutte le celle che hanno valori sono automaticamente inizializzate; tuttavia, esiste la possibilità che un foglio di lavoro abbia celle con solo formattazione applicata. In tal caso, le proprietà [**Cells.maxDataRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataRow--) o [**Cells.maxDataColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataColumn--) restituiranno -1 indicando l’assenza di valori popolati, ma le celle inizializzate a causa della formattazione delle celle non possono essere rilevate con questo metodo. Per verificare se un foglio di lavoro ha celle inizializzate vuote, è consigliabile usare il metodo `Enumerator.MoveNext` sull’iteratore acquisito dalla collezione [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Se il metodo `Enumerator.MoveNext` restituisce **true**, significa che ci sono una o più celle inizializzate nel foglio di lavoro dato.

## **Controllare le forme**

Potrebbe essere che un dato foglio di lavoro non abbia celle popolate; tuttavia, potrebbe contenere forme & oggetti come controlli, grafici, immagini, e così via. Se dobbiamo verificare se un foglio di lavoro contiene qualche forma, possiamo farlo ispezionando la proprietà [**ShapeCollection.count**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#count--). Un valore positivo indica la presenza di forme nel foglio di lavoro.

## **Esempio di programmazione**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Non-Empty Worksheets Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const book = new Workbook(new Uint8Array(arrayBuffer));

            const messages = [];

            // Loop over all worksheets in the workbook
            for (let i = 0; i < book.worksheets.count; i++) {
                const sheet = book.worksheets.get(i);
                // Check if worksheet has populated cells
                if (sheet.cells.maxDataRow !== -1) {
                    messages.push(`${sheet.name} is not empty because one or more cells are populated`);
                }
                // Check if worksheet has shapes
                else if (sheet.shapes.count > 0) {
                    messages.push(`${sheet.name} is not empty because there are one or more shapes`);
                }
                // Check if worksheet has empty initialized cells
                else {
                    const range = sheet.cells.maxDisplayRange;
                    const rangeIterator = range.getEnumerator();
                    if (rangeIterator.moveNext()) {
                        messages.push(`${sheet.name} is not empty because one or more cells are initialized`);
                    }
                }
            }

            if (messages.length) {
                resultDiv.innerHTML = '<ul>' + messages.map(m => `<li>${m}</li>`).join('') + '</ul>';
            } else {
                resultDiv.innerHTML = '<p style="color: green;">No non-empty worksheets found.</p>';
            }
        });
    </script>
</html>
```
