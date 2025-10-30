---
title: Få textbredd av cellvärde
type: docs
weight: 50
url: /sv/javascript-cpp/get-text-width-of-cell-value/
description: Lär dig hur du hämtar tekstbredd för cellvärde genom Aspose.Cells for JavaScript via C++ API.
keywords: Hämta tekstbredd för cellvärde JavaScript via C++, Få textbredd för cellvärde JavaScript via C++
---

## **Få textens bredd av cellvärdet**

Ibland kan utvecklare behöva beräkna bredden på cellens värde för att arrangera data i en layout. Aspose.Cells for JavaScript via C++ tillhandahåller [**CellsHelper.textWidth(string, Font, number)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#textWidth-string-font-number-) metoden, som tillåter utvecklare att få textbredden för cellens värde. Följande exempel på kod illustrerar hur man använder [**CellsHelper.textWidth(string, Font, number)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#textWidth-string-font-number-) för att få åtkomst till textbredden för cellens värde.

Källfilen som används i den följande kodsnutten bifogas för din referens.

[Källfil](96928090.xlsx)

## Exempelkod

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Text Width Example</title>
    </head>
    <body>
        <h1>Get Text Width Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and A1 cell
            const worksheet = workbook.worksheets.get(0);
            const cell = worksheet.cells.get("A1");

            // Accessing default font style
            const font = workbook.defaultStyle.font;

            // Calculating text width using CellsHelper (converted getter name to property)
            const textWidth = AsposeCells.CellsHelper.textWidth(cell.stringValue, font, 1);

            resultDiv.innerHTML = `<p style="color: green;">Text width: ${textWidth}</p>`;
        });
    </script>
</html>
```
