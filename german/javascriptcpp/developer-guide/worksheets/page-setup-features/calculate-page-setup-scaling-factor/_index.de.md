---
title: Bereitstellungs Scaling Faktor mit JavaScript via C++ berechnen
linktitle: Berechnen des Maßstabsfaktors für die Seiteneinrichtung
type: docs
weight: 300
url: /de/javascript-cpp/calculate-page-setup-scaling-factor/
description: Dieser Artikel enthält Beispielcode, der erklärt, wie die JavaScript API über C++ verwendet wird, um den Skalierungsfaktor der Seiteneinrichtung mithilfe der Option „Anpassen auf n Seite(n) breit und m hoch“ des Excel Arbeitsblatts programmatisch zu berechnen.
keywords: Anpassen auf n Seite(n) breit und m hoch Excel JavaScript via C++, Skalierungsfaktor der Seiteneinrichtung berechnen mit JavaScript via C++
---

{{% alert color="primary" %}}

Wenn Sie die Skalierung der Seiteneinrichtung mit der Option **Auf n Seite(n) breit und m hoch** festlegen, berechnet Microsoft Excel den Skalierungsfaktor der Seiteneinrichtung. Sie können dasselbe mit der Eigenschaft [**SheetRender.pageScale**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#pageScale--) berechnen. Diese Eigenschaft gibt einen Doppeldoppelwert zurück, der in Prozent umgerechnet werden kann. Wenn er 0,5 zurückgibt, bedeutet dies, dass der Skalierungsfaktor 50% ist.

{{% /alert %}}

Der folgende Beispielcode veranschaulicht, wie der Maßstabsfaktor für die Seiteneinrichtung mit der Eigenschaft [**SheetRender.pageScale**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#pageScale--) berechnet wird.

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
