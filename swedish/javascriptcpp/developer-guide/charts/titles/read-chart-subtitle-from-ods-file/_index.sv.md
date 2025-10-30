---
title: Läs diagram undertext från ODS fil med JavaScript via C++
linktitle: Läs diagramrubriken från en ODS fil
description: Lär dig hur du använder Aspose.Cells for JavaScript via C++ för att läsa diagramets undertext från en OpenDocument Spreadsheet (ODS) fil. Vår guide visar hur man hämtar och får åtkomst till diagramets undertext för vidare analys eller visning.
keywords: Aspose.Cells for JavaScript via C++, Läs diagramundertext, OpenDocument Spreadsheet, ODS fil, Diagramutdragning, Dataanalys.
type: docs
weight: 160
url: /sv/javascript-cpp/read-chart-subtitle-from-ods-file/
---

## **Läs diagramunderrubrik från ODS-fil**

Aspose.Cells ger dig möjligheten att läsa diagramundertexter i ODS-filer genom att använda egenskapen [**Chart.subTitle**](https://reference.aspose.com/cells/javascript-cpp/chart/#subTitle--). Följande exempel laddar [exempel ODS-fil](89620481.ods) och läser diagramundertexten med egenskapen [**Chart.subTitle**](https://reference.aspose.com/cells/javascript-cpp/chart/#subTitle--) och skriver ut den i Konsolfönstret. Se ofta kodens utdata nedan för referens.

## **Exempelkod**

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

## **Konsoloutput**

{{< highlight javascript >}}

Chart Subtitle: Sample Chart Subtitle

{{< /highlight >}}
