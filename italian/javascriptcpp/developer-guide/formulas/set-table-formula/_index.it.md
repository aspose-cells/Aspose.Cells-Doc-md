---
title: Propagare automaticamente la formula in tabella o oggetto elenco durante l inserimento dei dati nelle nuove righe con JavaScript tramite C++
linktitle: Imposta la formula tabella
type: docs
weight: 260
url: /it/javascript-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: Impara come propagare automaticamente le formule in tabelle o oggetti elenco durante l inserimento di dati nelle nuove righe usando Aspose.Cells for JavaScript tramite C++.
---

## **Possibili Scenari di Utilizzo**
A volte vuoi che una formula nel tuo Tabella o Oggetto Elenco si propaghi automaticamente alle nuove righe durante l'inserimento di nuovi dati. Questo è il comportamento predefinito di Microsoft Excel. Per ottenere la stessa funzionalità con Aspose.Cells for JavaScript tramite C++, usa la proprietà [ListColumn.formula](https://reference.aspose.com/cells/javascript-cpp/listcolumn/#formula--).

## **Propaga automaticamente la formula in Tabella o Oggetto Elenco durante l'inserimento di nuovi dati**
Il codice di esempio seguente crea una Tabella o Oggetto Elenco in modo che la formula nella colonna B si propaghi automaticamente alle nuove righe quando inserisci nuovi dati. Verifica il [file Excel generato](5115469.xlsx) con questo codice. Se inserisci un numero nella cella A3, vedrai che la formula nella cella B2 si propaga automaticamente nella cella B3.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells ListObject Example</h1>
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
            // Create workbook object
            const book = new Workbook();

            // Access first worksheet
            const sheet = book.worksheets.get(0);

            // Add column headings in cell A1 and B1
            sheet.cells.get(0, 0).value = "Column A";
            sheet.cells.get(0, 1).value = "Column B";

            // Add list object, set its name and style
            const listObject = sheet.listObjects.get(
                sheet.listObjects.add(0, 0, 1, sheet.cells.maxColumn, true)
            );
            listObject.tableStyleType = AsposeCells.TableStyleType.TableStyleMedium2;
            listObject.displayName = "Table";

            // Set the formula of second column so that it propagates to new rows automatically while entering data
            listObject.listColumns.get(1).formula = "=[Column A] + 1";

            // Save the workbook in xlsx format
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
