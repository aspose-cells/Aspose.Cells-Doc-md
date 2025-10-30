---
title: WortArt Wasserzeichen zum Arbeitsblatt mit JavaScript über C++ hinzufügen
linktitle: Verwalten von WordArt
type: docs
weight: 180
url: /de/javascript-cpp/add-wordart-watermark-to-worksheet/
description: Erfahren Sie, wie Sie WordArt als Hintergrund Wasserzeichen zu einem Arbeitsblatt mit Aspose.Cells for JavaScript über C++ hinzufügen.
---

{{% alert color="primary" %}} 

Verwenden Sie WordArt, um spezielle Texteffekte zu Tabellenkalkulationen hinzuzufügen. Zum Beispiel können Sie einen Titel über die Oberseite der Datei strecken, Text dekorieren und Text an eine Excel-Tabelle als Hintergrund-Wasserzeichen anwenden. Das WordArt wird zu einem Objekt, das Sie in Tabellenkalkulationen verschieben oder platzieren können, um Dekoration hinzuzufügen.

{{% /alert %}} 

Das folgende Beispiel zeigt, wie ein WordArt-Objekt hinzugefügt wird, um ein Hintergrundwasserzeichen für ein Arbeitsblatt festzulegen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Watermark Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

            // If a file is provided, open it. Otherwise create a new workbook.
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get the first default sheet
            const sheet = workbook.worksheets.get(0);

            // Add Watermark
            const wordart = sheet.shapes.addTextEffect(AsposeCells.MsoPresetTextEffect.TextEffect1,
                "CONFIDENTIAL", "Arial Black", 50, false, true, 18, 8, 1, 1, 130, 800);

            // Get the fill format of the word art
            const wordArtFormat = wordart.fill;            

            // Set the transparency
            wordArtFormat.transparency = 0.9;

            // Make the line invisible
            const lineFormat = wordart.line;
            lineFormat.visible = false;

            // Saving the modified Excel file (Excel97-2003 format .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Watermark_Test.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File with Watermark';

            document.getElementById('result').innerHTML = '<p style="color: green;">Watermark added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Erweiterte Themen**
- [Fügen Sie Word-Art-Text mit integrierten Stilen hinzu](/cells/de/javascript-cpp/add-word-art-text-with-built-in-styles/)
- [Sperren des WordArt-Wasserzeichens](/cells/de/javascript-cpp/locking-wordart-watermark/)
- [Voreingestellten WordArt-Stil auf den Text der Form setzen](/cells/de/javascript-cpp/set-preset-wordart-style-to-the-text-of-the-shape/)
