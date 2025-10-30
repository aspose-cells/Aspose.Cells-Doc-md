---
title: Leggi il sottotitolo del grafico da un file ODS utilizzando JavaScript via C++
linktitle: Leggi il sottotitolo del grafico dal file ODS
description: Impara come usare Aspose.Cells for JavaScript via C++ per leggere il sottotitolo del grafico da un file OpenDocument Spreadsheet (ODS). La nostra guida dimostrerà come estrarre e accedere al sottotitolo di un grafico per ulteriori analisi o visualizzazioni.
keywords: Aspose.Cells for JavaScript via C++, Leggi il sottotitolo del grafico, OpenDocument Spreadsheet, File ODS, Estrazione del grafico, Analisi dei Dati.
type: docs
weight: 160
url: /it/javascript-cpp/read-chart-subtitle-from-ods-file/
---

## **Leggi il sottotitolo del grafico dal file ODS**

Aspose.Cells ti consente di leggere i sottotitoli dei grafici nei file ODS utilizzando la proprietà [**Chart.subTitle**](https://reference.aspose.com/cells/javascript-cpp/chart/#subTitle--). Il seguente esempio di codice carica il [file ODS di esempio](89620481.ods) e legge il sottotitolo del grafico usando la proprietà [**Chart.subTitle**](https://reference.aspose.com/cells/javascript-cpp/chart/#subTitle--) e lo stampa nella Finestrella della Console. Per favore, consulta l'output della console del codice sottostante come riferimento.

## **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Get Chart Subtitle</title>
    </head>
    <body>
        <h1>Get Chart Subtitle Example</h1>
        <input type="file" id="fileInput" accept=".ods,.xls,.xlsx,.csv" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel or ODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Accessing chart subtitle text (converted from getSubTitle().getText())
            const subtitleText = chart.subTitle.text;

            console.log("Chart Subtitle: " + subtitleText);
            document.getElementById('result').innerHTML = '<p>Chart Subtitle: ' + (subtitleText ?? '') + '</p>';
        });
    </script>
</html>
```

## **Output della console**

{{< highlight javascript >}}

Chart Subtitle: Sample Chart Subtitle

{{< /highlight >}}
