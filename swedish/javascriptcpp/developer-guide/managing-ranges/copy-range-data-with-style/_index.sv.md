---
title: Kopiera område data med stil med JavaScript via C++
linktitle: Kopiera dataområde med stil
type: docs
weight: 610
url: /sv/javascript-cpp/copy-range-data-with-style/
description: Lär dig hur du kopierar ett område av celler med formatering med Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

[Kopiera data i område endast](/cells/sv/javascript-cpp/copy-range-data-only/) förklarar hur man kopierar datan från ett område av celler till ett annat. Specifikt tillämpar den en ny uppsättning stilar till de kopierade cellerna. Aspose.Cells kan också kopiera ett område helt med formatering. Denna artikel förklarar hur.

{{% /alert %}}

Aspose.Cells erbjuder en serie klasser och metoder för att arbeta med områden, till exempel [**createRange(string, string)**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-), [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag/) och [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/cells/#applyStyle-style-styleflag-).

Detta exempel:

1. Skapar en arbetsbok.  
2. Fyller ett antal celler i det första kalkbladet med data.  
3. Skapar en [**Range**](https://reference.aspose.com/cells/javascript-cpp/range/).  
4. Skapar ett [**Style**](https://reference.aspose.com/cells/javascript-cpp/style/)-objekt med angivna formateringsattribut.  
5. Tillämpar stilen på dataområdet.  
6. Skapar ett andra cellområde.  
7. Kopierar data med formatering från det första området till det andra området.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Copy Range Example</h1>
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
            if (fileInput.files.length && fileInput.files[0]) {
                // If a file is provided, open it and modify
            } else {
                // No file provided, will create a new workbook
            }

            // Instantiate or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get the first Worksheet Cells.
            const cells = workbook.worksheets.get(0).cells;

            // Fill some sample data into the cells.
            for (let i = 0; i < 50; i++) {
                for (let j = 0; j < 10; j++) {
                    cells.get(i, j).value = `${i},${j}`;
                }
            }

            // Create a range (A1:D3).
            const range = cells.createRange("A1", "D3");

            // Create a style object.
            let style = workbook.createStyle();
            // Specify the font attribute.
            style.font.name = "Calibri";
            // Specify the shading color.
            style.foregroundColor = AsposeCells.Color.Yellow;
            style.pattern = AsposeCells.BackgroundType.Solid;
            // Specify the border attributes.
            style.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.TopBorder).color = AsposeCells.Color.Blue;
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Blue;
            style.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.LeftBorder).color = AsposeCells.Color.Blue;
            style.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.RightBorder).color = AsposeCells.Color.Blue;

            // Create the styleflag object.
            const flag1 = new AsposeCells.StyleFlag();
            // Implement font attribute
            flag1.fontName = true;
            // Implement the shading / fill color.
            flag1.cellShading = true;
            // Implement border attributes.
            flag1.borders = true;
            // Set the Range style.
            range.applyStyle(style, flag1);

            // Create a second range (C10:F12).
            const range2 = cells.createRange("C10", "F12");

            // Copy the range data with formatting.
            range2.copy(range);

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CopyRange.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
