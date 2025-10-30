---
title: Beräkna Page Setup Skaleringsfaktor med JavaScript via C++
linktitle: Beräkna siduppsättningsskalningsfaktorn
type: docs
weight: 300
url: /sv/javascript-cpp/calculate-page-setup-scaling-factor/
description: Denna artikel ger exempel på kod som förklarar hur man använder JavaScript API via C++ för att beräkna sidinställningens skaleringsfaktor med hjälp av Passa till n sida(r) bred och m hög alternativ för Excel ark programmatisk.
keywords: Passa till n sida bred och m hög Excel JavaScript via C++, beräkna sidinställningens skaleringsfaktor JavaScript via C++
---

{{% alert color="primary" %}}

 När du ställer in sidinställningens skalningsfaktor med **Passa till n sida(n) bred och m hög**-alternativet, beräknar Microsoft Excel sidinställningens skalningsfaktor. Du kan beräkna samma sak med [**SheetRender.pageScale**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#pageScale--)-egenskapen. Den här egenskapen returnerar ett dubbelt värde som kan omvandlas till procentandel. Om den till exempel returnerar 0,5 betyder det att skalningsfaktorn är 50 %.

{{% /alert %}}

Följande exempelkod illustrerar hur man beräknar sidlayoutskalningsfaktorn med hjälp av [**SheetRender.pageScale**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#pageScale--)-egenskapen.

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
