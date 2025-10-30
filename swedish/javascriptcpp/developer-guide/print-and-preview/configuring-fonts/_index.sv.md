---
title: Konfigurera teckensnitt för rendering av kalkylblad med JavaScript via C++
linktitle: Konfigurera teckensnitt för rendering av kalkylblad
type: docs
weight: 10
url: /sv/javascript-cpp/configuring-fonts-for-rendering-spreadsheets/
description: Lär dig hur du konfigurerar teckensnitt för rendering av kalkylblad med hjälp av Aspose.Cells for JavaScript via C++. Se till att teckensnitt är tillgängliga för optimal konverteringskvalitet.
---

## **Möjliga användningsscenario**

Aspose.Cells API:er ger möjlighet att rendera kalkylblad i bildformat samt konvertera dem till PDF- och XPS-format. För att maximera konverteringskvaliteten är det nödvändigt att de teckensnitt som används i kalkylbladet finns tillgängliga i operativsystemets standardfontkatalog. Om de nödvändiga teckensnitten inte finns, kommer Aspose.Cells API:er att försöka ersätta de nödvändiga teckensnitten med de tillgängliga.

## **Val av teckensnitt**

Nedan är processen som Aspose.Cells API: er följer bakom scenen.

1. API försöker hitta teckensnitten på filsystemet som matchar det exakta teckensnittsnamnet som används i kalkylbladet.
1. Om API inte kan hitta teckensnitten med det exakta namnet försöker det använda standardteckensnittet som anges under arbetsbokens [**DefaultStyle.font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) egenskap.
1. Om API inte kan hitta teckensnittet som definieras under arbetsbokens [**DefaultStyle.font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) egenskap försöker det använda teckensnittet som anges under [**PdfSaveOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#defaultFont--) eller [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--) egenskap.
1. Om API inte kan hitta teckensnittet som definieras under [**PdfSaveOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#defaultFont--) eller [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--) egenskap försöker den använda teckensnittet som anges under [**FontConfigs.defaultFontName**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#defaultFontName--) egenskap.
1. Om API inte kan hitta teckensnittet som definieras under [**FontConfigs.defaultFontName**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#defaultFontName--) egenskapen försöker det välja de mest lämpliga teckensnitten från alla tillgängliga teckensnitt.
1. Slutligen, om API inte hittar några teckensnitt på filsystemet, renderar den kalkylbladet med Arial.

## **Ange anpassade typsnittsmappar**

Aspose.Cells API söker i operativsystemets standardfontkatalog efter de nödvändiga teckensnitten. Om de inte finns där, söker API:erna i anpassade (användardefinierade) kataloger. Klassen [**FontConfigs**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs) har exponerat flera sätt att ange anpassade fontkataloger som beskrivs nedan.

1. [**FontConfigs.fontFolder(string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolder-string-boolean-): Metoden är användbar om det endast finns en mapp att ange.
1. [**FontConfigs.fontFolders(string[], boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolders-stringarray-boolean-): Metoden är användbar när typsnitten finns i flera mappar och användaren vill ange alla mapparna separat istället för att kombinera alla typsnitt i en enda mapp.
1. [**FontConfigs.fontSources(FontSourceBase[])**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSources-fontsourcebasearray-): Mekanismen är användbar när användaren vill ladda typsnitt från flera mappar eller en enda typsnittsfil eller typsnittsdata från en byte-array.

{{% alert color="primary" %}}

Både [**FontConfigs.fontFolder(string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolder-string-boolean-) och [**FontConfigs.fontFolders(string[], boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolders-stringarray-boolean-) metoder accepterar en Boolean typ som andra parameter. Att passera **true** som andra parameter kommer att dirigera Aspose.Cells API:erna att söka igenom undermapparna efter teckensnittsfilerna.

{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Font Configuration Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Font Configuration Example</h1>
        <p>Select an Excel file (optional) and font resources to configure Aspose.Cells font sources in the browser.</p>

        <label>Excel File (optional):</label>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <br/><br/>

        <label>Font File (.ttf/.otf) (optional):</label>
        <input type="file" id="fontFileInput" accept=".ttf,.otf" />
        <br/><br/>

        <label>Font Folder (optional, select a folder):</label>
        <input type="file" id="fontFolderInput" webkitdirectory directory multiple />
        <br/><br/>

        <button id="runExample">Configure Fonts</button>
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
            const fontFileInput = document.getElementById('fontFileInput');
            const fontFolderInput = document.getElementById('fontFolderInput');
            const resultDiv = document.getElementById('result');

            // Basic validation: ensure at least one font resource is provided (file or folder)
            if (!fontFileInput.files.length && !fontFolderInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select at least one font file or a font folder.</p>';
                return;
            }

            // Defining string variables to store paths/names to font folders & font file
            // (In browser environment we use simple names or uploaded file names)
            const fontFolder1 = "Arial";
            const fontFolder2 = "Calibri";
            const fontFile = "arial.ttf";

            // Setting first font folder (converted from setFontFolder)
            AsposeCells.FontConfigs.fontFolder = fontFolder1;
            // Preserve the subfolder-search flag from original API call as a separate property
            AsposeCells.FontConfigs.fontFolderSearchSubFolders = true;

            // Setting both font folders (converted from setFontFolders)
            AsposeCells.FontConfigs.fontFolders = [fontFolder1, fontFolder2];
            // Preserve the subfolder-search flag as a separate property
            AsposeCells.FontConfigs.fontFoldersSearchSubFolders = false;

            // Defining FolderFontSource
            const sourceFolder = new AsposeCells.FolderFontSource(fontFolder1, false);

            // Defining FileFontSource
            const sourceFile = new AsposeCells.FileFontSource(fontFile);

            // Defining MemoryFontSource
            let memoryFontBytes = new Uint8Array([]);
            if (fontFileInput.files.length) {
                const ff = fontFileInput.files[0];
                const arrayBuffer = await ff.arrayBuffer();
                memoryFontBytes = new Uint8Array(arrayBuffer);
            } else if (fontFolderInput.files.length) {
                // If a folder was provided, try to find a .ttf/.otf inside it and use the first found
                const files = Array.from(fontFolderInput.files);
                const fontCandidate = files.find(f => f.name.toLowerCase().endsWith('.ttf') || f.name.toLowerCase().endsWith('.otf'));
                if (fontCandidate) {
                    const arrayBuffer = await fontCandidate.arrayBuffer();
                    memoryFontBytes = new Uint8Array(arrayBuffer);
                }
            }
            const sourceMemory = new AsposeCells.MemoryFontSource(memoryFontBytes);

            // Setting font sources (converted from setFontSources)
            AsposeCells.FontConfigs.fontSources = [sourceFolder, sourceFile, sourceMemory];

            // Provide feedback to the user
            resultDiv.innerHTML = '<p style="color: green;">Font configuration applied successfully.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Använd gärna någon av ovan nämnda metoder i början av applikationen, det vill säga; innan du anropar några andra objekt i Aspose.Cells API:erna.

{{% /alert %}} {{% alert color="primary" %}}

Om alla ovan nämnda metoder används för att ställa in teckensnittskällor, kommer endast de senaste inställningarna att träda i kraft.

{{% /alert %}}

## **Mekanism för typsnittsutbyte**

Aspose.Cells API:er ger också möjlighet att specificera ersättningsteckensnitt för rendering. Denna mekanism är användbar när ett nödvändigt teckensnitt inte finns på maskinen där konverteringen sker. Användare kan ange en lista med teckensnittsnamn som ett alternativ till det ursprungliga nödvändiga teckensnittet. För att göra detta har Aspose.Cells API:er exponerat metoden [**FontConfigs.fontSubstitutes(string, string[])**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSubstitutes-string-stringarray-) som tar emot 2 parametrar. Den första är av typen **string**, vilken är namnet på teckensnittet som ska ersättas. Den andra är en array av typen **string**, där användare kan ange en lista med teckensnittsnamn som ersättning för det ursprungliga teckensnittet (specificerat i den första parametern).

Här är ett enkelt användningsscenario.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Substituting the Arial font with Times New Roman & Calibri
            // Converted from: AsposeCells.FontConfigs.setFontSubstitutes("Arial", ["Times New Roman", "Calibri"]);
            AsposeCells.FontConfigs.fontSubstitutes = { "Arial": ["Times New Roman", "Calibri"] };

            // Saving the (possibly modified) workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the processed file.</p>';
        });
    </script>
</html>
```

## **Informationssamling**

Förutom ovan nämnda metoder har Aspose.Cells API:er även tillhandahållit möjligheter att samla information om vilka källor och ersättningar som har ställts in.

1. [**FontConfigs.fontSources**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSources--) metoden returnerar en array av typen [**FontSourceBase**](https://reference.aspose.com/cells/javascript-cpp/fontsourcebase) som innehåller listan över angivna fontkällor. Om inga källor har ställts in, returnerar metoden [**FontConfigs.fontSources**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSources--) en tom array.
1. [**FontConfigs.fontSubstitutes(string)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSubstitutes-string-) metoden tar emot en parameter av typen **string** för att specificera teckensnittnamnet för vilket ersättning har ställts in. Om ingen ersättning har ställts in för det angivna teckensnittet, returnerar metod [**FontConfigs.fontSubstitutes(string)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSubstitutes-string-) null.

## **Fortsatta ämnen**
- [Ange standardtypsnitt vid rendering av kalkylark till bilder](/cells/sv/javascript-cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [Ställ in egenskapen DefaultFont för PdfSaveOptions och ImageOrPrintOptions för att prioritera](/cells/sv/javascript-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Stödda teckensnittsformat](/cells/sv/javascript-cpp/supported-font-formats/)
- [Kalkylblad till bild - Ställ in pixelformat för den renderade bilden](/cells/sv/javascript-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
