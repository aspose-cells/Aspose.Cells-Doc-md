---
title: Avgör om pappersstorleken för arbetsbladet är Automatisk med JavaScript via C++
linktitle: Bestäm om Papper Storleken på Arbetsbladet är Automatisk
type: docs
weight: 90
url: /sv/javascript-cpp/determine-if-paper-size-of-worksheet-is-automatic/
description: Denna artikel förklarar hur man använder JavaScript API med C++ tillägg för att avgöra om pappersstorleken för ett arbetsblad är inställd på automatisk programmatisk.
keywords: Avgör om pappersstorleken för arbetsbladet är automatisk JavaScript via C++
---

## **Möjliga användningsscenario**

Det mesta av tiden är pappersstorleken för arbetsbladet automatisk. När den är automatisk är den ofta inställd på *Letter*. Ibland ställer användaren in pappersstorleken på arbetsbladet efter sina behov. I detta fall är pappersstorleken inte automatisk. Du kan ta reda på om arbetsbladets pappersstorlek är automatisk eller inte med hjälp av [**Worksheet.isAutomaticPaperSize()**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#isAutomaticPaperSize--)-egenskapen.

## **Avgöra om sidstorleken för arbetsbladet är automatisk**

Den provkod som ges nedan laddar följande två Excel-filer

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

och ta reda på om papperstorleken på deras första arbetsblad är automatisk eller inte. I Microsoft Excel kan du kontrollera om papperstorleken är automatisk eller inte via fönstret Sidlayout som visas i denna skärmbild.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - PageSetup IsAutomaticPaperSize</title>
    </head>
    <body>
        <h1>PageSetup IsAutomaticPaperSize Example</h1>
        <p>Select two Excel files to compare the PageSetup.isAutomaticPaperSize property:</p>
        <input type="file" id="fileInput1" accept=".xls,.xlsx,.csv" />
        <input type="file" id="fileInput2" accept=".xls,.xlsx,.csv" />
        <br/><br/>
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
            const fileInput1 = document.getElementById('fileInput1');
            const fileInput2 = document.getElementById('fileInput2');
            const resultDiv = document.getElementById('result');

            if (!fileInput1.files.length || !fileInput2.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select both Excel files.</p>';
                return;
            }

            const file1 = fileInput1.files[0];
            const file2 = fileInput2.files[0];

            const arrayBuffer1 = await file1.arrayBuffer();
            const arrayBuffer2 = await file2.arrayBuffer();

            // Instantiating Workbook objects from uploaded files
            const wb1 = new Workbook(new Uint8Array(arrayBuffer1));
            const wb2 = new Workbook(new Uint8Array(arrayBuffer2));

            // Access first worksheet of both workbooks
            const ws11 = wb1.worksheets.get(0);
            const ws12 = wb2.worksheets.get(0);

            // Read the PageSetup.isAutomaticPaperSize property of both worksheets
            const isAuto1 = ws11.pageSetup.isAutomaticPaperSize;
            const isAuto2 = ws12.pageSetup.isAutomaticPaperSize;

            // Display results
            resultDiv.innerHTML = `
                <p>First Worksheet of First Workbook - IsAutomaticPaperSize: ${isAuto1}</p>
                <p>First Worksheet of Second Workbook - IsAutomaticPaperSize: ${isAuto2}</p>
            `;
        });
    </script>
</html>
```

## **Konsoloutput**



{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
