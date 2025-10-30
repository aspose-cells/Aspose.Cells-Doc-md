---
title: Konvertera numerisk textdata till nummer
type: docs
weight: 900
url: /sv/javascript-cpp/convert-text-numeric-data-to-number/
description: Lär dig hur du konverterar nummer som är lagrade som text i Excel till nummer med Aspose.Cells for JavaScript via C++ API.
keywords: excel konvertera text till nummer, excel konvertera text till nummer JavaScript kod, excel konvertera numerisk data till nummer, excel konvertera numerisk data till nummer JavaScript kod, excel konvertera numerisk text till nummer, excel konvertera numerisk text till nummer JavaScript kod, excel konvertera numerisk text till nummer med JavaScript kod, konvertera numerisk text till nummer i excel med JavaScript kod, konvertera numerisk text till nummer i excel med JavaScript kod, konvertera numerisk sträng till nummer i excel med JavaScript kod, excel konvertera text numerisk data till nummer JavaScript kod, excel konvertera numerisk sträng till nummer JavaScript kod
---

## **Möjliga användningsscenario**
Ibland vill du konvertera numerisk data inmatad som text till nummer. Du kan skriva in nummer som text i Microsoft Excel genom att sätta ett apostrof före ett nummer, till exempel **'12345**. Excel behandlar då numret som en sträng. Aspose.Cells for JavaScript via C++ låter dig konvertera strängar till nummer.


## Hur man konverterar nummer som lagras som text till nummer i Excel
Du kan konvertera nummer som lagras som text till nummer genom att följa några enkla steg.
1. Välj en enda cell eller ett cellintervall som har en felindikator i övre vänstra hörnet.
1. Bredvid den valda cellen eller cellintervallet klickar du på felknappen som visas. På menyn klickar du på Konvertera till Nummer. 
<br>
<img src="4.png" width=70% />
1. Om varningsknappen inte är tillgänglig, välj en kolumn med detta problem. Om du inte vill konvertera hela kolumnen kan du istället välja en eller flera celler. Se bara till att cellerna du väljer är i samma kolumn, annars fungerar inte den här processen. Knappen Text till kolumner används vanligtvis för att dela upp en kolumn, men den kan också användas för att konvertera en enda kolumn med text till nummer. På fliken Data, klicka på Text till kolumner.
<br>
<img src="1.png" width=70% />
1. Klicka på Avsluta-knappen i popup-rutan.
<br>
<img src="2.png" width=70% />
1. Siffrorna som är lagrade som text omvandlas till nummer.
<br>
<img src="3.png" width=70% />

## Hur konverterar man nummer lagrade som text till nummer med Aspose.Cells for JavaScript via C++
Aspose.Cells for JavaScript via C++ tillhandahåller metoden [**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/javascript-cpp/cells/#convertStringToNumericValue--), som kan användas för att konvertera all text- eller numerisk data till nummer.

Följande skärmdump visar strängnumren i cellerna **A1:A17**. Strängnumren är vänsterjusterade.
<br>
<img src="5.png" width=70% />

Dessa strängnummer har konverterats till nummer med [**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/javascript-cpp/cells/#convertStringToNumericValue--) i följande skärmdump. Som du kan se är de nu högerjusterade.
<br>
<img src="6.png" width=70% />

## JavaScript-kod för att konvertera textbaserad numerisk data till faktiska nummer

Följande kodexempel visar hur du konverterar all strängnumriska data till faktiska nummer i alla arbetsblad.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Strings to Numeric Values in All Sheets</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook object with the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access worksheets collection
            const sheets = workbook.worksheets;
            const sheetcount = sheets.count;

            // Iterate through all worksheets and convert strings to numeric values
            for (let i = 0; i < sheetcount; i++) {
                const sheet = sheets.get(i);
                sheet.cells.convertStringToNumericValue();
            }

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
