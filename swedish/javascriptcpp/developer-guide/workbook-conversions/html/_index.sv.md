---
title: HTML med JavaScript via C++
linktitle: HTML
type: docs
weight: 230
url: /sv/javascript-cpp/convert-excel-to-html/
---

## **Konvertera Excelfil till HTML**
Aspose.Cells API stöder export av kalkylblad till HTML-format. För detta använder Aspose.Cells klassen [**HtmlSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions) för att ge flexibilitet att kontrollera flera aspekter av utdata-HTML:en.

Nedan visas ett kodexempel för att spara en arbetsbok som en HTML-fil med JavaScript via C++:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Convert Excel to HTML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to HTML</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Saving the workbook to HTML format
            const outputData = workbook.save(SaveFormat.Html);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```


## **Konvertera Excel arbetsbok till MHTML-filer**
MHTML kombinerar normalt HTML med externa resurser (det vill säga innehåll som vanligtvis länkas in, såsom bilder, animationer, ljud och liknande) i en fil. De används för e-postmeddelanden med filändelsen .mht. Aspose.Cells stöder läsning och skrivning av MHTML-filer.

Nedan visas ett kodexempel för att spara en arbetsbok som en MHTML-fil med JavaScript via C++:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Save as MHT</title>
    </head>
    <body>
        <h1>Save Excel as MHT Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load your source workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save file to MHT format
            const outputData = workbook.save(SaveFormat.MHtml);
            const blob = new Blob([outputData], { type: 'application/octet-stream' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.mht';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download MHT File';

            resultDiv.innerHTML = '<p style="color: green;">File converted to MHT successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```

## **Fortsatta ämnen**
- [Justera kolumner och rader automatiskt vid inläsning av HTML i arbetsboken](/cells/sv/javascript-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/)
- [Undvik exponentiell notation av stora tal vid import från HTML](/cells/sv/javascript-cpp/avoid-exponential-notation-of-large-numbers-while-importing/)
- [Ändra HTML-länkens målknapptype](/cells/sv/javascript-cpp/change-the-html-link-target-type/)
- [Konvertera Excel till HTML med verktygstips](/cells/sv/javascript-cpp/convert-excel-to-html-with-tooltip/)
- [Create Transparent Image of Excel Worksheet](/cells/sv/javascript-cpp/create-transparent-image-of-excel-worksheet/)
- [Ta bort överflödiga mellanslag efter radbrytning vid import av HTML](/cells/sv/javascript-cpp/delete-redundant-spaces-after-line-break-while-importing/)
- [Inaktivera nivånedstiällda avslöjade kommentarer vid sparning till HTML](/cells/sv/javascript-cpp/disable-downlevel-revealed-comments-while-saving-to/)
- [Inaktivera export av ramscript och dokumentegenskaper](/cells/sv/javascript-cpp/disable-exporting-frame-scripts-and-document-properties/)
- [Excel till HTML - Använd PresentationPreference-alternativet för bättre layout](/cells/sv/javascript-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/)
- [Uteslut oanvända stilar under Excel till HTML-konvertering](/cells/sv/javascript-cpp/exclude-unused-styles-during-excel-to-html-conversion/)
- [Expandera text från höger till vänster vid export av Excel-fil till HTML](/cells/sv/javascript-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/)
- [Exportera DataBar, ColorScale och IconSet villkorlig formatering vid Excel till HTML-omvandling](/cells/sv/javascript-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/)
- [Exportera kommentarer vid sparande av Excel-fil till HTML](/cells/sv/javascript-cpp/export-comments-while-saving-excel-file-to/)
- [Exportera dokumentarbetsboks- och arbetsbladsegenskaper vid konvertering från Excel till HTML](/cells/sv/javascript-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/)
- [Exportera Excel till HTML med rutnätslinjer](/cells/sv/javascript-cpp/export-excel-to-html-with-gridlines/)
- [Exportera utskriftsområde till HTML](/cells/sv/javascript-cpp/export-print-area-range-to/)
- [Exportera liknande kantstilmall när kantstil inte stöds av webbläsare](/cells/sv/javascript-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
- [Exportera arbetsbladets CSS separat i utdata-HTML-filen](/cells/sv/javascript-cpp/export-worksheet-css-separately-in-output/)
- [Dölja överlagt innehåll med CrossHideRight vid sparande till HTML](/cells/sv/javascript-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/)
- [Förprefixa tabellens elementstilar med HtmlSaveOptions.TableCssId-egenskapen](/cells/sv/javascript-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [Förhindra export av dolda arbetsbladsinnehåll när du sparar till HTML](/cells/sv/javascript-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/)
- [Ange sökväg till exporterad arbetsbokhtml-fil via IFilePathProvider-gränssnittet](/cells/sv/javascript-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/)
- [Identifiera självstängande taggar](/cells/sv/javascript-cpp/recognise-self-closing-tags/)
- [Rendera gradientfyllning för WordArt vid konvertering av kalkylblad till HTML](/cells/sv/javascript-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/)
- [Ange kolumnbredd till skalbar enhet som em eller procent](/cells/sv/javascript-cpp/set-column-width-to-scalable-unit-like-em-or-percent/)
- [Ange standardfonten vid rendering av kalkylblad till HTML](/cells/sv/javascript-cpp/set-default-font-while-rendering-spreadsheet-to/)
- [Ange hur man korsar sträng i utmatnings-HTML med HtmlCrossType](/cells/sv/javascript-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
- [Stödjer layouten för DIV-taggar vid laddning av HTML till excel arbetsbok](/cells/sv/javascript-cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)

- [Aktivera CSS Anpassade Egenskaper under sparande till HTML](/cells/sv/javascript-cpp/enable-css-custom-properties-while-saving-to-html/)
