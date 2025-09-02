---
title: HTML with JavaScript via C++
linktitle: HTML
type: docs
weight: 230
url: /javascript-cpp/convert-excel-to-html/
---

## **Converting Excel Workbook to HTML**
The Aspose.Cells API provides support for exporting spreadsheets to HTML format. For this purpose, Aspose.Cells uses the [**HtmlSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions) class to provide the flexibility to control several aspects of the output HTML.

The code example below shows how to save a workbook as an HTML file using JavaScript via C++:

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


## **Converting Excel Workbook to MHTML Files**
MHTML combines normal HTML with external resources (that is, content that is usually linked in, like images, animations, audio, and so on) into one file. They are used for emails with the .mht file extension. Aspose.Cells supports reading and writing MHTML files.

The code example below shows how to save a workbook as an MHTML file using JavaScript via C++:

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

## **Advance topics**
- [AutoFit Columns and Rows while loading HTML in Workbook](/cells/javascript-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/)
- [Avoid exponential notation of large numbers while importing from HTML](/cells/javascript-cpp/avoid-exponential-notation-of-large-numbers-while-importing/)
- [Change the HTML Link Target Type](/cells/javascript-cpp/change-the-html-link-target-type/)
- [Convert Excel to HTML with tooltip](/cells/javascript-cpp/convert-excel-to-html-with-tooltip/)
- [Create Transparent Image of Excel Worksheet](/cells/javascript-cpp/create-transparent-image-of-excel-worksheet/)
- [Delete redundant spaces after line break while importing HTML](/cells/javascript-cpp/delete-redundant-spaces-after-line-break-while-importing/)
- [Disable Downlevel Revealed Comments while saving to HTML](/cells/javascript-cpp/disable-downlevel-revealed-comments-while-saving-to/)
- [Disable Exporting Frame Scripts and Document Properties](/cells/javascript-cpp/disable-exporting-frame-scripts-and-document-properties/)
- [Excel to HTML - Use PresentationPreference Option for Better Layout](/cells/javascript-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/)
- [Exclude Unused Styles during Excel to HTML conversion](/cells/javascript-cpp/exclude-unused-styles-during-excel-to-html-conversion/)
- [Expanding text from right to left while exporting Excel file to HTML](/cells/javascript-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/)
- [Export DataBar, ColorScale and IconSet Conditional Formatting while Excel to HTML Conversion](/cells/javascript-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/)
- [Export Comments while Saving Excel file to HTML](/cells/javascript-cpp/export-comments-while-saving-excel-file-to/)
- [Export Document Workbook and Worksheet Properties in Excel to HTML conversion](/cells/javascript-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/)
- [Export Excel to HTML with GridLines](/cells/javascript-cpp/export-excel-to-html-with-gridlines/)
- [Export print area range to HTML](/cells/javascript-cpp/export-print-area-range-to/)
- [Export similar Border Style when Border Style is not supported by Web Browsers](/cells/javascript-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
- [Export Worksheet CSS Separately in Output HTML](/cells/javascript-cpp/export-worksheet-css-separately-in-output/)
- [Hiding Overlaid Content with CrossHideRight while saving to HTML](/cells/javascript-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/)
- [Prefix Table Elements Styles with HtmlSaveOptions.TableCssId property](/cells/javascript-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [Prevent Exporting Hidden Worksheet Contents on Saving to HTML](/cells/javascript-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/)
- [Provide exported worksheet html file path via IFilePathProvider interface](/cells/javascript-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/)
- [Recognise Self Closing Tags](/cells/javascript-cpp/recognise-self-closing-tags/)
- [Render Gradient Fill for the WordArt while Converting Spreadsheets to HTML](/cells/javascript-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/)
- [Set column width to scalable unit like em or percent](/cells/javascript-cpp/set-column-width-to-scalable-unit-like-em-or-percent/)
- [Set Default Font while rendering spreadsheet to HTML](/cells/javascript-cpp/set-default-font-while-rendering-spreadsheet-to/)
- [Specify how to cross string in output HTML using HtmlCrossType](/cells/javascript-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
- [Support the layout of DIV tags while loading HTML to excel workbook](/cells/javascript-cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)

- [Enable CSS Custom Properties while saving to HTML](/cells/javascript-cpp/enable-css-custom-properties-while-saving-to-html/)