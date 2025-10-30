---
title: Ritaglia le righe e le colonne vuote iniziali durante l esportazione di fogli di calcolo in formato CSV con JavaScript via C++
linktitle: Tagliare le righe e le colonne vuote iniziali durante l esportazione di fogli di calcolo in formato CSV
type: docs
weight: 100
url: /it/javascript-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Impara come ritagliare le righe e le colonne vuote iniziali quando si esportano fogli di calcolo in formato CSV utilizzando Aspose.Cells for JavaScript via C++.
---

## **Possibili Scenari di Utilizzo**

A volte, il tuo file Excel o CSV contiene colonne o righe iniziali vuote. Ad esempio, considera questa riga

{{< highlight javascript >}}

 ,,,data1,data2

{{< /highlight >}}

Qui le prime tre celle o colonne sono vuote. Quando apri un file CSV del genere in Microsoft Excel, allora Microsoft Excel scarta queste righe e colonne vuote iniziali.

Per impostazione predefinita, Aspose.Cells for JavaScript via C++ non elimina le colonne e le righe vuote iniziali al salvataggio, ma se vuoi rimuoverle proprio come fa Microsoft Excel, Aspose.Cells offre la proprietà [**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn--). Configurala su **true** e tutte le righe e colonne vuote iniziali verranno eliminate al salvataggio.

{{% alert color="primary" %}}

 Prima del rilascio di Aspose.Cells for JavaScript via C++ 20.4, il valore predefinito di [**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn--) era **false**. Dalla versione 20.4, il valore predefinito di [**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn--) è **true**.

{{% /alert %}}

## **Taglia righe e colonne vuote iniziali durante l'esportazione di fogli di calcolo nel formato CSV**

Il seguente esempio di codice carica il [file Excel di origine](sampleTrimBlankColumns.xlsx) che ha due colonne vuote all'inizio. Prima salva il file Excel in formato CSV senza modifiche e poi imposta la proprietà [**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn--) su **true** e lo salva di nuovo. Lo screenshot mostra il [file Excel di origine](sampleTrimBlankColumns.xlsx), il [file CSV di output senza ritaglio](outputWithoutTrimBlankColumns.csv) e il [file CSV di output con ritaglio](outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Trim Blank Columns</title>
    </head>
    <body>
        <h1>Trim Blank Columns Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink1" style="display: none;">Download Result 1</a>
        <a id="downloadLink2" style="display: none; margin-left: 10px;">Download Result 2</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtSaveOptions, Utils } = AsposeCells;

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

            // Load source workbook
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Save in csv format (without trimming)
            const outputData1 = wb.save(SaveFormat.Csv);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'outputWithoutTrimBlankColumns.csv';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download CSV Without Trimming';

            // Now save again with TrimLeadingBlankRowAndColumn as true
            const opts = new TxtSaveOptions();
            opts.trimLeadingBlankRowAndColumn = true;

            // Save in csv format (with trimming)
            const outputData2 = wb.save(opts);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'outputTrimBlankColumns.csv';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download CSV With Trimmed Blank Columns';

            resultDiv.innerHTML = '<p style="color: green;">Files generated. Use the links above to download the CSVs.</p>';
        });
    </script>
</html>
```
