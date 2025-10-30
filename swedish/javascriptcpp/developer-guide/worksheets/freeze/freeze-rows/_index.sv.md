---
title: Frys översta rad(er) av Excel arbetsblad med JavaScript via C++
linktitle: Frys rader
type: docs
weight: 190
url: /sv/javascript-cpp/how-to-freeze-rows-of-excel-worksheet
description: I denna artikel lär du dig hur man fryser översta rader av Excel arbetsblad programatiskt med JavaScript biblioteket och C++ API.
keywords: Frys översta rader, frys översta rad med JavaScript via C++.
---

## **Introduktion**

I denna artikel lär vi oss hur man fryser översta rad(rader). När du har mycket data under en gemensam rubrik kan det vara svårt att se rubriken när du skrollar ner i arbetsbladet. Du kan frysa översta rad(rader) så att du kan se den frysta delen även när resten av datan skrollas. Det är enkelt att se rubriker i de översta raderna.

## **Frysa rader i Excel**

**![Frysa översta rad(er) i Excel](Freeze-Rows.png)**

1. Om du vill frysa översta rad(er), välj först raden under den rad som ska frysas.
2. Klicka på Visa > Frysa rader.
3. I rullgardinsmenyn, klicka på Frysa översta rad.
4. Om du skrollar nedåt, är den första raden alltid i översta vyn.

**![Frysen rad](Frozen-Row.png)**

Som du kan se är den första raden fryst; den första raden behålls alltid högst upp när du skrollar ner.

Frys rader låter dig visa din stora data utan att hålla koll på radetiketten.

## **Frys rader med Aspose.Cells for JavaScript via C++**
Det är enkelt att frysa rad(er) med Aspose.Cells for JavaScript via C++. 
Använd [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-)-metoden för att frysa rad(er) vid vald rad.
1. Konstruera Arbetsbok för att öppna filen eller skapa en tom fil.
2. Frysa den första raden med Worksheet.freezePanes()-metoden.
3. Spara filen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Freeze Panes</title>
    </head>
    <body>
        <h1>Freeze Panes Example</h1>
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

            // Instantiate a new Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Freezing panes at the cell B2 on the first worksheet
            const worksheet = workbook.worksheets.get(0);
            worksheet.freezePanes("A2", 1, 0);

            // Saving the file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'frozen.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Frozen Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Freeze panes applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Bifogad [provkäll-Excel-fil](../Freeze.xlsx).
