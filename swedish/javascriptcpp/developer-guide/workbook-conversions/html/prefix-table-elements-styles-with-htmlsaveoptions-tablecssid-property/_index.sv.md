---
title: Första tabell element stilar med HtmlSaveOptions.tableCssId egenskap i JavaScript via C++
linktitle: Första tabell element stilar med HtmlSaveOptions.tableCssId egenskap
type: docs
weight: 110
url: /sv/javascript-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
description: Lär dig hur man prefixar tabell element stilar i HTML med Aspose.Cells for JavaScript via C++.
---

## **Möjliga användningsscenario**

Aspose.Cells låter dig prefixa tabell element stilar med [**HtmlSaveOptions.tableCssId**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#tableCssId--) egenskap. Anta att du ställer in denna egenskap med något värde som **MyTest_TableCssId**, då kommer du att hitta tabell element stilar som visas nedan:

{{< highlight javascript >}}
 table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.
{{< /highlight >}}

Följande skärmbild visar effekten av att använda [**HtmlSaveOptions.tableCssId**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#tableCssId--) egenskap på utdata HTML.

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## ** Prefix Tabell Element Stilar med HtmlSaveOptions.tableCssId egenskap**

Följande exempel kod visar hur man använder [**HtmlSaveOptions.tableCssId**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#tableCssId--) egenskap. Kontrollera [utdata HTML](60489790.zip) som genererats av koden för referens.

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Set Cell Style and Save as HTML with Table CSS ID</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Color } = AsposeCells;

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
            if (fileInput.files.length === 0) {
                // No file selected - create a new workbook as in original JavaScript sample
                const wb = new Workbook();

                // Access first worksheet
                const ws = wb.worksheets.get(0);

                // Access cell B5 and put value inside it
                const cell = ws.cells.get("B5");
                cell.value = "This is some text.";

                // Set the style of the cell - font color is Red
                const st = cell.style;
                st.font.color = Color.Red;
                cell.style = st;

                // Specify html save options - specify table css id
                const opts = new HtmlSaveOptions();
                opts.tableCssId = "MyTest_TableCssId";

                // Save the workbook in html
                const outputData = wb.save(SaveFormat.Html, opts);
                const blob = new Blob([outputData], { type: 'text/html' });
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'outputTableCssId.html';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download HTML File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the HTML file.</p>';
                return;
            }

            // If a file is provided, open it and apply the same changes
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access cell B5 and put value inside it
            const cell = ws.cells.get("B5");
            cell.value = "This is some text.";

            // Set the style of the cell - font color is Red
            const st = cell.style;
            st.font.color = Color.Red;
            cell.style = st;

            // Specify html save options - specify table css id
            const opts = new HtmlSaveOptions();
            opts.tableCssId = "MyTest_TableCssId";

            // Save the workbook in html
            const outputData = wb.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputTableCssId.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
