---
title: Trimma ledande tomma rader och kolumner vid export av kalkylblad till CSV format med JavaScript via C++
linktitle: Strimla ledande tomma rader och kolumner vid export av kalkylblad till CSV format
type: docs
weight: 100
url: /sv/javascript-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Lär dig att trimma ledande tomma rader och kolumner när du exporterar kalkylblad till CSV format med hjälp av Aspose.Cells for JavaScript via C++.
---

## **Möjliga användningsscenario**

Ibland har din Excel eller CSV-fil ledande tomma kolumner eller rader. Till exempel, överväg den här raden

{{< highlight javascript >}}

 ,,,data1,data2

{{< /highlight >}}

Här är de första tre cellerna eller kolumnerna tomma. När du öppnar en sådan CSV-fil i Microsoft Excel, då tar Microsoft Excel bort dessa ledande tomma rader och kolumner.

Som standard sparar inte Aspose.Cells for JavaScript via C++ ledande tomma kolumner och rader vid sparning, men om du vill ta bort dem, precis som Microsoft Excel gör, tillhandahåller Aspose.Cells egenskapen [**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn--). Ange den till **true** så kommer alla ledande tomma rader och kolumner att tas bort vid sparning.

{{% alert color="primary" %}}

Före släppet av Aspose.Cells for JavaScript via C++ 20.4 var det inbyggda värdet av [**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn--) **falskt**. Sedan 20.4-uppdateringen är standardvärdet för [**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn--) **sant.**

{{% /alert %}}

## **Rensa ledande blanka rader och kolumner vid export av kalkylblad till CSV-format**

Följande exempel laddar [käll-Excel-filen](sampleTrimBlankColumns.xlsx) som har två ledande tomma kolumner. Den sparar först filen som CSV utan några ändringar, och ställer sedan in [**TxtSaveOptions.trimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#trimLeadingBlankRowAndColumn--)-egenskapen till **true** och sparar den igen. Skärmbilden visar [käll-Excel-fil](sampleTrimBlankColumns.xlsx), [utdata CSV utan trimning](outputWithoutTrimBlankColumns.csv) och [utdata CSV med trimning](outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Trim Blank Columns</title>
    </head>
    <body>
        <h1>Trim Blank Columns Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink1" style="display: none;">Download Result 1</a>
        <a id="downloadLink2" style="display: none; margin-left: 10px;">Download Result 2</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtSaveOptions, Utils } = AsposeCells;

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

            // Load source workbook
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Save in csv format (without trimming)
            const outputData1 = wb.save(SaveFormat.Csv);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'outputWithoutTrimBlankColumns.csv';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download CSV Without Trimming';

            // Now save again with TrimLeadingBlankRowAndColumn as true
            const opts = new TxtSaveOptions();
            opts.trimLeadingBlankRowAndColumn = true;

            // Save in csv format (with trimming)
            const outputData2 = wb.save(opts);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'outputTrimBlankColumns.csv';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download CSV With Trimmed Blank Columns';

            resultDiv.innerHTML = '<p style="color: green;">Files generated. Use the links above to download the CSVs.</p>';
        });
    </script>
</html>
```
