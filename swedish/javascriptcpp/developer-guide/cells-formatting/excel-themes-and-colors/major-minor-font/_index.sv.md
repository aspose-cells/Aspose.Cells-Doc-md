---
title: Rubrik och brödtexttema font
linktitle: Rubrik och brödtexttema font
description: Aspose.Cells är ett JavaScript via C++ bibliotek för att arbeta med kalkylbladsfiler. Det stöder att ställa in rubrik och kroppsteman i Excel dokument, vilket möjliggör för användare att anpassa utseendet och stilen på dokumentet. Denna artikel introducerar hur man använder Aspose.Cells biblioteket för att arbeta med rubrik och kroppsteman i Excel dokument.
keywords: Aspose.Cells, Excel dokument, Rubrik, Kropp, Temafont, Utseende, Stil, JavaScript via C++
type: docs
weight: 120
url: /sv/javascript-cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

Standardteckensnittet ändras automatiskt när regionsinställningen ändras.

Om standardtypsnittet ändras, ändras också radhöjd och kolumnbredd, och det kan till och med förstöra sidlayouten.

Vad orsakade att standardtypsnittet ändrades?

Om Excel-tematypsnitt är inställt, kommer Excel automatiskt att växla mellan olika typsnitt baserat på den aktuella språkmiljön.

{{% /alert %}}

## **Rubrik- och brödtematypsnitt i Excel**

I Excel, välj Start-fliken, klicka på teckensnittets nedrullningsbara låda, du kommer att se "Tema teckensnitt" med två tema-typsnitt: Calibri Light (Rubriker) och Calibri (Kropp) överst med engelskt regionsinställning.

**![Tema Typsnitt](Tema-Typsnitt.png)**

Om Temateckensnitt är vald, visas teckensnittets namn på ett annat sätt i olika regioner. Om du inte vill att teckensnittet ska ändras automatiskt i olika regioner, välj inte de två Temateckensnitten.

## **Ändra rubrik och kroppens teckensnitt programmässigt**
Med Aspose.Cells for JavaScript via C++ kan vi kontrollera om standardsnittet är ett temabaserat typsnitt eller ställa in tematypsnittet med [**Font.schemeType**](https://reference.aspose.com/cells/javascript-cpp/font/#schemeType-fontschemetype-) metod.

Följande exempel visar hur man manipulerar tema-typsnitt.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Change Theme Font Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FontSchemeType, Utils } = AsposeCells;

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

            // Accessing and modifying the default style and its font scheme
            let defaultStyle = workbook.defaultStyle;
            let font = defaultStyle.font;
            let schemeType = font.schemeType;

            if (schemeType === FontSchemeType.Major || schemeType === FontSchemeType.Minor) {
                console.log("It's theme font");
            }

            // Change theme font to normal font
            font.schemeType = FontSchemeType.None;

            // Assign the modified default style back to the workbook
            workbook.defaultStyle = defaultStyle;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.modified.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Theme font changed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```



## **Dynamiskt hämtar lokalt tema-typsnitt programmässigt**
Ibland är våra servrar och användares maskiner inte i samma region. Hur kan vi få samma typsnitt som användarna vill för filbehandling?

Vi måste ställa in systemets regionala inställningar innan vi laddar filen med [**LoadOptions.region**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#region-countrycode-)-metoden.

Följande exempelkod visar hur man får lokaltematypsnitt.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Default Style Local Font Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new LoadOptions.
            const options = new AsposeCells.LoadOptions();
            // Sets the customer's region
            options.region = AsposeCells.CountryCode.Japan;

            // Instantiate a new Workbook using the uploaded file and load options.
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Get the default style
            const defaultStyle = workbook.defaultStyle;

            // Gets customer's local font.
            const localFontName = defaultStyle.font.name;

            resultDiv.innerHTML = `<p style="color: green;">Local font name: ${localFontName}</p>`;
        });
    </script>
</html>
```
