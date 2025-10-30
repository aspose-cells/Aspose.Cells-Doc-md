---
title: Geben Sie den Autor an, während Sie die Arbeitsmappe mit JavaScript via C++ vor Schreibschutz schützen
linktitle: Autor beim Schreibschutz des Arbeitsmappenschreibens spezifizieren
type: docs
weight: 40
url: /de/javascript-cpp/specify-author-while-write-protecting-workbook/
description: Geben Sie während des Schreibschutzes einer Arbeitsmappe mit Aspose.Cells for JavaScript via C++ einen Autorennamen an.
---

## **Mögliche Verwendungsszenarien**

Sie können beim Schutz Ihres Arbeitsblatts mit Aspose.Cells API einen Autorennamen angeben. Bitte verwenden Sie dazu die Eigenschaft [**Workbook.author**](https://reference.aspose.com/cells/javascript-cpp/writeprotection/#author--).

## **Autor beim Schreibschutz des Arbeitsmappenschreibens spezifizieren**

Der folgende Beispielcode zeigt die Verwendung der Eigenschaft [**Workbook.author**](https://reference.aspose.com/cells/javascript-cpp/writeprotection/#author--). Der Code erstellt ein leeres Arbeitsbuch, schützt es mit einem Passwort, gibt den Autorennamen an und speichert es als [Ausgabedatei Excel](67338582.xlsx). Die folgende Bildschirmaufnahme zeigt den Effekt des Beispielcodes auf die Ausgabedatei Excel zu Ihrer Referenz.

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Author While Write Protecting Workbook</h1>
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
            // Create empty workbook.
            const workbook = new Workbook();

            // Write protect workbook with password.
            workbook.settings.writeProtection.password = "1234";

            // Specify author while write protecting workbook.
            workbook.settings.writeProtection.author = "SimonAspose";

            // Save the workbook in XLSX format.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and write-protected successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
