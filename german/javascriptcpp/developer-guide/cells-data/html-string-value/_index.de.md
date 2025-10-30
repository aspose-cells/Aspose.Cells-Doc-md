---
title: HTML Rich Text in der Zelle hinzufügen
linktitle: Html String Wert
type: docs
weight: 50
url: /de/javascript-cpp/adding-html-rich-text-inside-the-cell/
description: Erfahren Sie, wie Sie HTML Reichtest innerhalb der Zelle mit der Aspose.Cells for JavaScript via C++ API hinzufügen.
keywords: HTML Reichtest innerhalb der Zelle in JavaScript via C++ hinzufügen, HTML Reichtest in der Zelle in JavaScript via C++ setzen, HTML Reichtest in der Zelle in JavaScript via C++ hinzufügen
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt die Umwandlung von Microsoft Excel-orientiertem HTML in XLS/XLSX-Format. Das bedeutet, dass das von Microsoft Excel generierte HTML mit Aspose.Cells wieder in XLS/XLSX konvertiert werden kann.

Ebenso kann Aspose.Cells einfaches HTML in HTML-Rich-Text umwandeln. Aspose.Cells bietet die [**Cell.htmlString**](https://reference.aspose.com/cells/javascript-cpp/cell/#htmlString-string-)-Eigenschaft, die ein solches einfaches HTML akzeptieren und in formatierten Zellentext umwandeln kann.

{{% /alert %}}

Im folgenden Beispielcode wird gezeigt, wie man HTML-Rich-Text in der Zelle hinzufügt. Bitte beachten Sie den Screenshot der Ausgabedatei in Excel.

![todo:image_alt_text](adding-html-rich-text-inside-the-cell_1)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells HTML String Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            let workbook;

            // If a file is provided, open it; otherwise create a new workbook
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Set HTML formatted string to the cell (converted setter -> property)
            cell.htmlString = "<Font Style=\"FONT-WEIGHT: bold;FONT-STYLE: italic;TEXT-DECORATION: underline;FONT-FAMILY: Arial;FONT-SIZE: 11pt;COLOR: #ff0000;\">This is simple HTML formatted text.</Font>";

            // Save the workbook to XLSX format and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML string written to A1. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## Verwandte Artikel

- [Listenpunkte anzeigen, indem Sie den Zellenwert mit HTML einstellen](/cells/de/javascript-cpp/display-bullets-by-setting-cell-value-using/)
- [Holen Sie sich HTML5-String aus der Zelle](/cells/de/javascript-cpp/get-html5-string-from-cell/)
