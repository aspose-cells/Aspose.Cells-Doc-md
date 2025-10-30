---
title: Kontrollera anpassad nummerformatering vid inställning av Style.Custom egenskap
linktitle: Kontrollera anpassad nummerformatering vid inställning av Style.Custom egenskap
description: Aspose.Cells är ett JavaScript bibliotek för att arbeta med kalkylbladsfiler, vilket stöder kontroll av anpassade nummerformat vid formatering. Denna artikel visar hur du använder Aspose.Cells biblioteket för att kontrollera anpassade nummerformat för att säkerställa att formateringen är korrekt.
keywords: Aspose.Cells, JavaScript bibliotek, kalkylblad, formatering, anpassad nummerformat, kontroll, validering
type: docs
weight: 170
url: /sv/javascript-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **Möjliga användningsscenario**

Om du tilldelar ett ogiltigt anpassat nummerformat till egenskapen [**Style.custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-) kommer Aspose.Cells for JavaScript via C++ inte att kasta något undantag. Men om du vill att Aspose.Cells ska kontrollera om det tilldelade anpassade nummerformatet är giltigt eller inte, ställ in egenskapen [**Workbook.settings.checkCustomNumberFormat**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#checkCustomNumberFormat-boolean-) till **true**.

## ** Kontrollera anpassat nummerformat vid inställning av Style.custom egenskap**

Följande exempel kod tilldelar ett ogiltigt anpassat nummerformat till egenskapen [**Style.custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-). Eftersom vi redan har ställt in egenskapen [**Workbook.settings.checkCustomNumberFormat**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#checkCustomNumberFormat-boolean-) till **true**, kastar det ett undantag, t.ex. Ogiltigt nummerformat. Läs gärna kommentaren i koden för mer hjälp.

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Check Custom Number Format</h1>
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new empty workbook if no file is provided
                workbook = new Workbook();
            }

            // Setting this property to true will make Aspose.Cells throw an exception
            // when invalid custom number format is assigned to Style.custom property
            workbook.settings.checkCustomNumberFormat = true;

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access cell A1 and put some number to it
            const cell = sheet.cells.get("A1");
            cell.value = 2347;

            // Access cell's style and set its Style.custom property
            const style = cell.style;

            // This line will throw exception if workbook.settings.checkCustomNumberFormat is set to true
            style.custom = "ggg @ fff"; // Invalid custom number format

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
