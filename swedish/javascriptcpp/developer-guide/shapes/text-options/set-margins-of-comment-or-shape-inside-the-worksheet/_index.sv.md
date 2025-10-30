---
title: Ställ in marginaler för kommentar eller form inne i arbetsbladet med JavaScript via C++
linktitle: Ställ in marginaler för kommentar eller shape i kalkylbladet
type: docs
weight: 1500
url: /sv/javascript-cpp/set-margins-of-comment-or-shape-inside-the-worksheet/
description: Lär dig att ställa in marginaler för kommentarer eller former inom ett Excel arbetsblad med Aspose.Cells for JavaScript via C++.
---

## **Möjliga användningsscenario**  

Aspose.Cells tillåter dig att ställa in marginalerna för vilken form eller kommentar som helst med hjälp av [**Shape.textBody.textAlignment**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/)-egenskapen. Denna egenskap returnerar objektet av [**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment)-klassen som har olika egenskaper, t.ex. [**ShapeTextAlignment.topMarginPt**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/#topMarginPt--), [**ShapeTextAlignment.leftMarginPt**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/#leftMarginPt--), [**ShapeTextAlignment.bottomMarginPt**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/#bottomMarginPt--), [**ShapeTextAlignment.rightMarginPt**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/#rightMarginPt--), etc., som kan användas för att ställa in topp-, vänster-, botten- och högermarginaler.  

## **Ställ in marginaler för kommentar eller shape i kalkylbladet**  

Se nedan kodexempel. Den laddar den [provExcel-filen](61767851.xlsx) som innehåller två former. Koden har åtkomst till formerna en i taget och ställer in deras topp-, vänster-, botten- och högermarginaler. Se den [utdataExcel-filen](61767852.xlsx) genererad av koden och skärmbild som visar effekten av koden på utdataExcel-filen.  

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)  

## **Exempelkod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Margins of Comment or Shape Example</title>
    </head>
    <body>
        <h1>Set Margins of Comment or Shape Inside The Worksheet</h1>
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

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            const shapes = ws.shapes;
            for (let i = 0; i < shapes.count; i++) {
                const sh = shapes.get(i);
                // Access the text alignment
                const txtAlign = sh.textBody.textAlignment;

                // Set auto margin false
                txtAlign.isAutoMargin = false;

                // Set the top, left, bottom and right margins
                txtAlign.topMarginPt = 10;
                txtAlign.leftMarginPt = 10;
                txtAlign.bottomMarginPt = 10;
                txtAlign.rightMarginPt = 10;
            }

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSetMarginsOfCommentOrShapeInsideTheWorksheet.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Margins updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
