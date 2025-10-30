---
title: Ange hur du korsar sträng i utdata HTML med HtmlCrossType med JavaScript via C++
linktitle: Ange hur texten ska korsas i utdata HTML med HtmlCrossType
type: docs
weight: 140
url: /sv/javascript-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: Lär dig hur man kontrollerar strängöverflöd i HTML output genom att specificera HtmlCrossType i Aspose.Cells for JavaScript via C++.
---

## **Möjliga användningsscenario**

När en cell innehåller text eller sträng men är större än cellens bredd, överflödar texten om nästa cell i nästa kolumn är null eller tom. När du sparar ditt Excel-fil till HTML kan du kontrollera detta överflöd genom att specificera kors-typen med hjälp av [**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype) enum. Den har följande värden:

- **HtmlCrossType.Default**: Visas som MS Excel; beror på nästa cell. Om nästa cell är null, kommer strängen att korsas eller klippas av.

- **HtmlCrossType.MSExport**: Visa strängen som MS Excel exporterar HTML.

- **HtmlCrossType.Cross**: Visar HTML-korsad sträng; prestandan för att skapa stora HTML-filer blir mer än tio gånger snabbare än att ställa in värdet till Default eller FitToCell.

- **HtmlCrossType.FitToCell**: Visa endast strängen inom cellens bredd.

## **Ange hur man korsar sträng i utmatnings-HTML med HtmlCrossType**

Följande kodexempel laddar [exempel-Excelfil](51740732.xlsx) och sparar den i HTML-format genom att specificera olika [**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype). Vänligen ladda ner de [utdata-HTMLs](51740734.zip) som genererades med denna kod. Exempel-Excelfilen innehåller en bild kantad med rött som visas i denna skärmbild, vilket visar effekten av [**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype)-värdena på utdata HTML.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export HTML Cross String Type Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, HtmlCrossType, Utils } = AsposeCells;

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

            // Specify HTML Cross Type via HtmlSaveOptions
            const opts = new HtmlSaveOptions();
            // Applying the sequence of assignments as in the original JavaScript code
            opts.htmlCrossStringType = HtmlCrossType.Default;
            opts.htmlCrossStringType = HtmlCrossType.MSExport;
            opts.htmlCrossStringType = HtmlCrossType.Cross;
            opts.htmlCrossStringType = HtmlCrossType.FitToCell;

            // Save workbook to HTML using the specified options
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: "text/html" });
            const downloadLink = document.getElementById('downloadLink');
            const fileName = 'out' + opts.htmlCrossStringType + '.htm';
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = fileName;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML exported successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
