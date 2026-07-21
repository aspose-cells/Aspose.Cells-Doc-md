---
title: Inaktivera pivottabellribbon
type: docs
weight: 90
url: /sv/javascript-cpp/disable-pivot-table-ribbons/
description: Hur man inaktiverar Pivotdiagramflikar med Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells for JavaScript via C++ Excel, Excel JavaScript via C++ bibliotek, inaktivera Pivotdiagramflikar med Aspose.Cells for JavaScript via C++ Excel bibliotek.
---

{{% alert color="primary" %}}

Pivotdiagrambaserade rapporter är användbara men benägna att ge fel om mål användare inte har detaljerad kunskap om Excel för att konfigurera dessa rapporter. I dessa fall vill organisationer begränsa användare från att kunna ändra en pivotdiagramrapport. Vanliga funktioner som att lägga till ytterligare filter, skivare, fält eller ändra ordningen för vissa saker i rapporten rekommenderas oftast inte för alla användare. Å andra sidan ska dessa användare också kunna uppdatera rapporten och använda befintliga filter eller skivare. Aspose.Cells for JavaScript via C++ har gett denna möjlighet till utvecklare för att begränsa användare från att ändra dessa rapporter medan de skapas. För detta ändamål ger Excel en funktion för att inaktivera pivotdiagramfliken och samma funktion erbjuds av Aspose.Cells for JavaScript via C++, dvs utvecklaren kan inaktivera fliken som innehåller kontroller för att ändra dessa rapporter.

{{% /alert %}}

## **Hur man inaktiverar Pivotdiagramflik med Aspose.Cells for JavaScript via C++**

Följande kod visar den här funktionen genom att komma åt en pivottabell från ett blad och sedan ställa in [**enableWizard**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#enableWizard-boolean-) till **false**. Provfilen för pivottabell kan laddas ned från denna [länk](pivot_table_test.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Disable Pivot Table Wizard Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the pivot table in the first sheet
            const pt = workbook.worksheets.get(0).pivotTables.get(0);

            // Disable ribbon for this pivot table
            pt.enableWizard = false;

            // Save output file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table wizard disabled successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
