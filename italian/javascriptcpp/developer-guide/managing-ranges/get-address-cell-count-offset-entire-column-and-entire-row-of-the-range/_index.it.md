---
title: Ottieni indirizzo, conteggio delle celle, offset, intera colonna e intera riga dell intervallo con JavaScript tramite C++
linktitle: Ottenere Conteggio Cellule Indirizzo Spostamento Intera Colonna e Intera Riga della Gamma
type: docs
weight: 330
url: /it/javascript-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
---

## **Possibili Scenari di Utilizzo**
Aspose.Cells for JavaScript tramite C++ fornisce l'oggetto Range che ha vari metodi utili che facilitano l'utente a lavorare facilmente con gli intervalli di Excel. Questo articolo illustra l'uso dei seguenti metodi o proprietà dell'oggetto Range.

- **Indirizzo**

Ottiene l'indirizzo della gamma.

- **Conteggio celle**

Ottiene il conteggio di tutte le celle nella gamma.

- **Spostamento**

Ottiene la gamma per spostamento.

- **Intera Colonna**

Restituisce un oggetto Range che rappresenta l'intera colonna (o colonne) che contiene il range specificato.

- **Intera Riga**

Restituisce un oggetto Range che rappresenta l'intera riga (o righe) che contiene il range specificato.

## **Ottieni Indirizzo, Conteggio Celle, Spostamento, Intera Colonna e Intera Riga del Range**
Il seguente codice di esempio spiega l'uso dei metodi e delle proprietà come discusso in precedenza. Si prega di consultare l'output della console del codice fornito di seguito per un riferimento.

## **Codice di Esempio**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            // This example creates ranges on a new empty workbook and prints info to the page.
            const resultEl = document.getElementById('result');
            resultEl.innerHTML = '';

            // Create empty workbook.
            const wb = new Workbook();

            // Access first worksheet.
            const ws = wb.worksheets.get(0);

            // Create range A1:B3.
            console.log("Creating Range A1:B3\n");
            let rng = ws.cells.createRange("A1:B3");

            // Print range address and cell count.
            const lines = [];
            lines.push("Range Address: " + rng.address);
            lines.push("Range row Count: " + rng.rowCount);
            lines.push("Range column Count: " + rng.columnCount);

            // Formatting console output.
            lines.push("----------------------");
            lines.push("");

            // Create range A1.
            console.log("Creating Range A1\n");
            rng = ws.cells.createRange("A1");

            // Print range offset, entire column and entire row.
            lines.push("Offset: " + rng.offset(2, 2).address);
            lines.push("Entire Column: " + rng.entireColumn.address);
            lines.push("Entire Row: " + rng.entireRow.address);

            // Formatting console output.
            lines.push("----------------------");
            lines.push("");

            // Display results
            resultEl.innerHTML = '<pre>' + lines.join("\n") + '</pre>';
        });
    </script>
</html>
```

## **Output della console**
{{< highlight javascript >}}
 Creating Range A1:B3

Range Address: A1:B3

Cell Count: 6

\----------------------

Creating Range A1

Offset: C3

Entire Column: A:A

Entire Row: 1:1

\----------------------

{{< /highlight >}}
