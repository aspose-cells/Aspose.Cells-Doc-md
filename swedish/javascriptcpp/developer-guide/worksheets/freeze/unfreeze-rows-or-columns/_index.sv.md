---
title: Återställa rader eller kolumner med JavaScript via C++
linktitle: Avfrys fönster
type: docs
weight: 190
url: /sv/javascript-cpp/unfreeze-rows-or-columns-of-excel-worksheet
description: I denna artikel lär du dig hur man avfryser rader, kolumner eller fönsterprogrammerat med JavaScript API med C++.
keywords: Avfrysa fönster, Avfrysa rader, Avfrysa kolumner, avFreeze fönster JavaScript via C++.
---

## **Introduktion**

I denna artikel lär vi oss hur man avfryser rader, kolumner och paneler. Om arbetsbladen i Excel-filer är frysta, vill vi ibland avfrysa arbetsbladet eller justera frysta rader, kolumner eller paneler.


## **I Excel**

1. Klicka på fliken Visa > Frys fönster > Avfrys fönster.

**![avfrysta fönster i Excel](Avfrys-Fönster.png)**




## **Avfrysa Rader, Kolumner eller Fönster med Aspose.Cells for JavaScript via C++**
Det är enkelt att avfrysa fönster med Aspose.Cells for JavaScript via C++. Använd [**Worksheet.unFreezePanes()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#unFreezePanes--)-metoden för att avfrysa fönster.

1. Konstruera arbetsboken för att öppna den frysta filen.
2. Avfrysa fönster med Worksheet.unFreezePanes() metod.
3. Spara filen.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example - Unfreeze Panes</title>
    </head>
    <body>
        <h1>Unfreeze Panes Example</h1>
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

            // Accessing the first worksheet and unfreezing panes
            const worksheet = workbook.worksheets.get(0);
            worksheet.unFreezePanes();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Unfrozen.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unfrozen Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Panes unfrozen successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Bifogad [provkälla för Excel-filen](Fryst.xlsx).
