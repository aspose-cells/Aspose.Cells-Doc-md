---
title: Calculer le facteur d échelle de mise en page avec JavaScript via C++
linktitle: Calculer le facteur d échelle de la mise en page
type: docs
weight: 300
url: /fr/javascript-cpp/calculate-page-setup-scaling-factor/
description: Cet article fournit un code d exemple expliquant comment utiliser l API JavaScript via C++ pour calculer le facteur d échelle de mise en page en utilisant l option Ajuster à n page(s) en largeur par m en hauteur d une feuille Excel de manière programmatique.
keywords: Ajuster à n pages en largeur par m en hauteur Excel JavaScript via C++, calculer le facteur d échelle de mise en page JavaScript via C++
---

{{% alert color="primary" %}}

Lorsque vous définissez la mise à l’échelle de la mise en page en utilisant l’option **Ajuster à n page(s) en largeur par m en hauteur**, Microsoft Excel calcule le facteur d’échelle de la mise en page. Vous pouvez calculer la même chose en utilisant la propriété [**SheetRender.pageScale**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#pageScale--). Cette propriété retourne une valeur double qui peut être convertie en pourcentage. Par exemple, si elle retourne 0,5 cela signifie que le facteur d’échelle est de 50%.

{{% /alert %}}

Le code d'exemple suivant illustre comment calculer le facteur d'échelle de la mise en page en utilisant la propriété [**SheetRender.pageScale**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#pageScale--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Page Scale</title>
    </head>
    <body>
        <h1>Page Scale Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, SheetRender, ImageOrPrintOptions, PaperSizeType, Utils } = AsposeCells;

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

            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Put some data in these cells
            worksheet.cells.get("A4").putValue("Test");
            worksheet.cells.get("S4").putValue("Test");

            // Set paper size
            worksheet.pageSetup.paperSize = PaperSizeType.PaperA4;

            // Set fit to pages wide as 1
            worksheet.pageSetup.fitToPagesWide = 1;

            // Calculate page scale via sheet render
            const sr = new SheetRender(worksheet, new ImageOrPrintOptions());

            // Convert page scale double value to percentage
            const strPageScale = (sr.pageScale * 100).toFixed(0) + "%";

            // Write the page scale value
            document.getElementById('result').innerHTML = `<p>Page Scale: ${strPageScale}</p>`;
            console.log(strPageScale);
        });
    </script>
</html>
```
