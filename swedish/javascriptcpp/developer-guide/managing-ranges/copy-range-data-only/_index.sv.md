---
title: Kopiera endast område data med JavaScript via C++
linktitle: Kopiera endast dataområde
type: docs
weight: 600
url: /sv/javascript-cpp/copy-range-data-only/
description: Lär dig hur du kopierar data från ett område av celler till ett annat med Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}  
Ibland behöver du kopiera data från en cellintervall till en annan, kopiera bara datan, inte formateringen. Aspose.Cells erbjuder den här funktionen.  

Den här artikeln ger en exempelkod som använder Aspose.Cells för att kopiera ett datintervall.  
{{% /alert %}}  

Detta exempel visar hur man:  

1. Skapa en arbetsbok.  
1. Lägga till data till celler i den första arbetsboken.  
1. Skapa en [**Range**](https://reference.aspose.com/cells/javascript-cpp/range).  
1. Skapa ett [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-objekt med specificerade formateringsattribut.  
1. Tillämpa stilformatering på området.  
1. Skapa en annan cellintervall.  
1. Kopiera data från det första området till det andra området.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Copy Range Data Example</title>
    </head>
    <body>
        <h1>Copy Range Data Example</h1>
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
            // If a file is provided, open it; otherwise create a new blank workbook
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
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
                    const cell = cells.get(i, j);
                    cell.value = `${i},${j}`;
                }
            }

            // Create a range (A1:D3).
            const range = cells.createRange("A1", "D3");

            // Create a style object.
            const style = workbook.createStyle();
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

            // Create the style flag object.
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

            // Copy the range data only.
            range2.copyData(range);

            // Save the workbook and provide download link.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CopyRangeData.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
