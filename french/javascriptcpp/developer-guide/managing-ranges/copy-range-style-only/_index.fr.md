---
title: Copier le style uniquement de la plage avec JavaScript via C++
linktitle: Copier uniquement le style de la plage
type: docs
weight: 620
url: /fr/javascript-cpp/copy-range-style-only/
description: Apprenez comment copier uniquement le style d une plage tout en manipulant les données en Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}}

[Copier uniquement les données de la plage](/cells/fr/javascript-cpp/copy-range-data-only/) et [Copier les données de la plage avec style](/cells/fr/javascript-cpp/copy-range-data-with-style/) expliquent comment copier les données d'une plage à une autre seule ou avec toute la mise en forme. Il est également possible de copier uniquement la mise en forme. Cet article montre comment.

{{% /alert %}} 

Cet exemple crée un classeur, le remplit de données et copie uniquement le style d'une plage.

1. Créer une plage.
1. Créez un objet `Style` avec des attributs de mise en forme spécifiés.
1. Appliquer la mise en forme de style à la plage.
1. Créer une deuxième plage de cellules.
1. Copier la mise en forme de la première plage vers la deuxième plage.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Copy Range Style</h1>
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

            // Instantiate or load a Workbook.
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
                    cells.get(i, j).putValue(i.toString() + "," + j.toString());
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
            const top = style.borders.get(AsposeCells.BorderType.TopBorder);
            top.lineStyle = AsposeCells.CellBorderType.Thin;
            top.color = AsposeCells.Color.Blue;

            const bottom = style.borders.get(AsposeCells.BorderType.BottomBorder);
            bottom.lineStyle = AsposeCells.CellBorderType.Thin;
            bottom.color = AsposeCells.Color.Blue;

            const left = style.borders.get(AsposeCells.BorderType.LeftBorder);
            left.lineStyle = AsposeCells.CellBorderType.Thin;
            left.color = AsposeCells.Color.Blue;

            const right = style.borders.get(AsposeCells.BorderType.RightBorder);
            right.lineStyle = AsposeCells.CellBorderType.Thin;
            right.color = AsposeCells.Color.Blue;

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

            // Create a second range (C10:E13).
            const range2 = cells.createRange("C10", "E13");

            // Copy the range style only.
            range2.copyStyle(range);

            // Saving the modified Excel file as XLS (Excel97To2003)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'copyrangestyle.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
