---
title: Lägga till HTML Rich Text inuti Cell
linktitle: HTML strängsvärde
type: docs
weight: 50
url: /sv/javascript-cpp/adding-html-rich-text-inside-the-cell/
description: Lär dig hur du lägger till HTML rik text inuti cellen via Aspose.Cells for JavaScript via C++ API.
keywords: Lägg till HTML rik text i cellen Javascript via C++, Sätt HTML rik text i cellen Javascript via C++, Lägg till HTML rik text i cellen Javascript via C++
---

{{% alert color="primary" %}}

Aspose.Cells stödjer konvertering av Microsoft Excel-inriktad HTML till XLS/XLSX-format. Det innebär att HTML som genereras av Microsoft Excel kan konverteras tillbaka till XLS/XLSX med hjälp av Aspose.Cells.

På samma sätt kan, om det finns enkel HTML, Aspose.Cells konvertera den till HTML Rich Text. Aspose.Cells tillhandahåller egenskapen [**Cell.htmlString**](https://reference.aspose.com/cells/javascript-cpp/cell/#htmlString-string-) som kan ta sådan enkel HTML och konvertera den till formaterad celltext.

{{% /alert %}}

Nedan kodprov visar hur du lägger till HTML-rich text inuti cellen. Se skärmbilden av den resulterande Excel-filen.

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


## Relaterade artiklar

- [Visa punktlistor genom att ställa in cellvärde med hjälp av HTML](/cells/sv/javascript-cpp/display-bullets-by-setting-cell-value-using/)
- [Hämta HTML5-sträng från cell](/cells/sv/javascript-cpp/get-html5-string-from-cell/)
