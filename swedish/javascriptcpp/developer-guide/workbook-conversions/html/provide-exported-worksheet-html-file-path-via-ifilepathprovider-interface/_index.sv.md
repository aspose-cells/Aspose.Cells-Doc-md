---
title: Ange sökvägen till exporterad kalkylblad HTML fil via IFilePathProvider gränssnitt med JavaScript via C++
linktitle: Tillhandahålla sökväg för exporterad kalkylblads HTML fil via IFilePathProvider gränssnitt
type: docs
weight: 70
url: /sv/javascript-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **Möjliga användningsscenario**
 Anta att du har en Excel-fil med flera blad och du vill exportera varje blad till enskild HTML-fil. Om något av dina blad har länkar till andra blad kommer dessa länkar att brytas i den exporterade HTML. För att hantera detta problem tillhandahåller Aspose.Cells for JavaScript via C++ [IFilePathProvider](https://reference.aspose.com/cells/javascript-cpp/ifilepathprovider)-gränssnittet, som du kan implementera för att åtgärda brutna länkar.

## **Tillhandahålla sökväg för exporterad kalkylblads-HTML-fil via IFilePathProvider-gränssnitt**
Vänligen ladda ner [exempel Excel-fil](5115213.zip) som används i koden nedan och dess exporterade HTML-filer. Alla dessa filer är inne i Temp-katalogen. Extrahera den till C: -driven. Då blir den C:\Temp-mappen. Du öppnar Sheet1.html i webbläsaren och klickar på de två länkarna inuti den. Dessa länkar hänvisar till dessa två exporterade HTML-arbetsblad som finns i C:\Temp\OtherSheets-katalogen.

{{< highlight javascript >}}
 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1
{{< /highlight >}}

Den följande skärmbilden visar hur C:\Temp\Sheet1.html och dess länkar ser ut

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

Följande skärmbild visar HTML-källan. Som du kan se hänvisar länkarna nu till katalogen C:\Temp\OtherSheets. Detta uppnåddes med hjälp av [IFilePathProvider](https://reference.aspose.com/cells/javascript-cpp/ifilepathprovider)-gränssnittet.

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)

## **Exempelkod**
Vänligen notera att katalogen C:\Temp bara är för illustration. Du kan använda vilken katalog du vill och placera [exempel Excel-filen](5115211.xlsx) där och köra den medföljande exempel koden. Den kommer att skapa en underkatalog OtherSheets i din katalog och exportera andra och tredje arbetsbladets HTML inuti den. Ändra variabeln dirPath i koden innan du kör den och hänvisa till den katalog du önskar.

{{% alert color="primary" %}} 

Exempelkoden fungerar endast när du har satt Aspose.Cells-licensen. Om du försöker köra koden utan att ange licensen, kommer den att hamna i en oändlig loop. Därför har vi lagt till en kontroll för att skriva ut ett meddelande och stoppa exekveringen när licensen inte är inställd. Du kan antingen köpa en licens eller begära ett 30-dagars tillfälligt licens från Aspose.Purchase-teamet.

{{% /alert %}} 

Vänligen notera att kommentera ut dessa rader i koden kommer att bryta länkarna i Sheet1.html, och Sheet2.html eller Sheet3.html kommer inte att öppnas när deras länkar klickas i Sheet1.html.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Worksheet to HTML with FilePathProvider Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions } = AsposeCells;

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

        // Implementation of IFilePathProvider for browser
        class FilePathProvider extends AsposeCells.IFilePathProvider {
            constructor() {
                super();
            }

            // Converted method name from getFullName -> fullName per universal getter/setter conversion rule
            fullName(sheetName) {
                if (sheetName === "Sheet2") {
                    return "file:///OtherSheets/Sheet2.html";
                } else if (sheetName === "Sheet3") {
                    return "file:///OtherSheets/Sheet3.html";
                }
                return "";
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create HtmlSaveOptions and assign FilePathProvider (converted setter to property assignment)
            const options = new HtmlSaveOptions();
            options.filePathProvider = new FilePathProvider();

            // Save workbook to HTML using options
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">HTML exported successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - IFilePathProvider</title>
    </head>
    <body>
        <h1>Aspose.Cells IFilePathProvider Example (Browser)</h1>
        <p>Select the Sample_filepath.xlsx file to export worksheets to separate HTML files.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <div id="links"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Utils } = AsposeCells;

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

        // Implementation of IFilePathProvider interface for browser
        class FilePathProvider extends AsposeCells.IFilePathProvider {
            constructor() {
                super();
            }

            // Gets the full path of the file by worksheet name when exporting worksheet to html separately.
            // So the references among the worksheets could be exported correctly.
            getFullName(sheetName) {
                if (sheetName === "Sheet2") {
                    return "file:///OtherSheets/Sheet2.html";
                } else if (sheetName === "Sheet3") {
                    return "file:///OtherSheets/Sheet3.html";
                }
                return "";
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            const linksDiv = document.getElementById('links');
            linksDiv.innerHTML = '';
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select the Sample_filepath.xlsx file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Check license
            if (!workbook.isLicensed()) {
                resultDiv.innerHTML = '<p style="color: red;">You must set the license to execute this code successfully.</p>';
                return;
            }

            // Export each worksheet to separate HTML using HtmlSaveOptions and FilePathProvider
            const sheetCount = workbook.worksheets.count;

            for (let i = 0; i < sheetCount; i++) {
                // Set the active worksheet to current index
                workbook.worksheets.activeSheetIndex = i;

                // Create html save option
                const options = new HtmlSaveOptions();
                options.exportActiveWorksheetOnly = true;
                // Provide file path provider so hyperlinks among sheets are preserved correctly
                options.filePathProvider = new FilePathProvider();

                // Save the active worksheet to HTML (returns Uint8Array)
                const outputData = workbook.save(SaveFormat.Html, options);

                // Create downloadable blob for the HTML
                const blob = new Blob([outputData], { type: 'text/html' });

                // Determine filename similar to original logic
                const sheetIndex = i + 1;
                let filename = '';
                if (i === 0) {
                    filename = 'Sheet1.html';
                } else {
                    filename = `OtherSheets_Sheet${sheetIndex}_out.html`;
                }

                const link = document.createElement('a');
                link.href = URL.createObjectURL(blob);
                link.download = filename;
                link.textContent = 'Download ' + filename;
                link.style.display = 'block';
                linksDiv.appendChild(link);
            }

            resultDiv.innerHTML = '<p style="color: green;">Worksheets exported successfully! Use the links below to download each HTML file.</p>';
        });
    </script>
</html>
```
