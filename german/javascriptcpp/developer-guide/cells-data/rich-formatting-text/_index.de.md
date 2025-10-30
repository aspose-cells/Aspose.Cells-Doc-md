---
title: Zugriff und Aktualisierung der Teile von Rich Text einer Zelle
linktitle: Rich Text Formatierung
type: docs
weight: 40
url: /de/javascript-cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: Lernen Sie, wie Sie mit der Aspose.Cells for JavaScript via C++ API auf und die Teile des Rich Texts einer Zelle aktualisieren.
keywords: Zugriff und Aktualisierung des Rich Texts einer Zelle, Abrufen des Rich Texts einer Zelle, Rich Text einer Zelle bearbeiten, Rich Text einer Zelle abrufen, Rich Text einer Zelle aktualisieren, Rich Text einer Zelle ändern
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScript via C++ ermöglicht es Ihnen, auf die Komponenten des Rich Texts der Zelle zuzugreifen und sie zu aktualisieren. Dafür können Sie die Eigenschaften [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) und [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-) verwenden. Diese Eigenschaften geben und nehmen ein Array von [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting) Objekten, mit denen Sie verschiedene Schriftarteigenschaften wie Schriftname, Schriftfarbe, Fettdruck etc. anpassen können.

{{% /alert %}}

## **Teile des Rich-Texts der Zelle zugreifen und aktualisieren**

Der folgende Code demonstriert die Verwendung der Eigenschaften [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) und [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-) anhand der [Excel-Quelldatei](5112369.xlsx), die Sie über den bereitgestellten Link herunterladen können. Die Quelldatei enthält in Zelle A1 einen Rich Text mit 3 Teilen, die jeweils eine andere Schriftart besitzen. Das folgende Code-Snippet greift auf diese Teile zu und aktualisiert den ersten Teil mit einem neuen Schriftartnamen. Abschließend wird die Arbeitsmappe als [Ausgabedatei](5112366.xlsx) gespeichert. Nach dem Öffnen wird die Schrift des ersten Abschnitts in **"Arial"** geändert sein.

### JavaScript-Code zum Zugriff auf und Aktualisieren der Rich-Text-Abschnitte einer Zelle

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Update Cell Character Font Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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

            // Ensure Aspose.Cells is initialized
            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet and its cells
            const cells = workbook.worksheets.get(0).cells;
            const cell = cells.get("A1");

            console.log("Before updating the font settings....");
            let fnts = cell.characters;
            const count = fnts.length;
            for (let i = 0; i < count; i++) {
                console.log(fnts[i].font.name);
            }

            // Modify the first FontSetting Font Name
            fnts[0].font.name = "Arial";

            // And update it using characters property
            cell.characters = fnts;

            console.log("After updating the font settings....");

            fnts = cell.characters;

            for (let i = 0; i < count; i++) {
                console.log(fnts[i].font.name);
            }

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### Von der Beispiellösung generierte Konsolenausgabe



{{< highlight java >}}

Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}
