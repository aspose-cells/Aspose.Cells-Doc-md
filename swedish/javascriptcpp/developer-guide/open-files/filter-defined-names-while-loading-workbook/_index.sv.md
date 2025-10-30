---
title: Filtrera definierade namn vid laddning av arbetsbok med JavaScript via C++
linktitle: Filtrera definierade namn när arbetsboken laddas
type: docs
weight: 50
url: /sv/javascript-cpp/filter-defined-names-while-loading-workbook/
---

## **Möjliga användningsscenario**

Aspose.Cells låter dig filtrera eller ta bort definierade namn som finns i arbetsboken. Vänligen använd [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions/) för att ladda definierade namn och [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions/) för att ta bort dem vid inläsning av arbetsboken. Observera, om du tar bort definierade namn kan formlerna i arbetsboken gå sönder.

## **Filtrera Definierade namn vid inläsning av arbetsbok**

Följande exempel laddar [exempel Excel-fil](61767860.xlsx) som har en formel i cell **C1** som innehåller de definierade namnen, dvs. *=SUM(MyName1, MyName2)*. Eftersom vi använder [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions/) för att ta bort de definierade namnen vid inläsning av arbetsboken, bryts formeln i cell C1 i [utgångs Excel-fil](61767861.xlsx) och du ser *#NAME?* istället. Se skärmbilden nedan som visar hur koden påverkar exempel-Excel-filen.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Filter Defined Names While Loading Workbook</title>
    </head>
    <body>
        <h1>Filter Defined Names While Loading Workbook</h1>
        <input type="file" id="fileInput" accept=".xlsx,.xls" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFilter, LoadDataFilterOptions, Utils } = AsposeCells;

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

            // Specify the load options
            let opts = new LoadOptions();
            // We do not want to load defined names
            opts.loadFilter = new LoadFilter(~LoadDataFilterOptions.DefinedNames);

            // Load the workbook with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Save the output Excel file, it will break the formula in C1 if defined names were removed
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputFilterDefinedNamesWhileLoadingWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">FilterDefinedNamesWhileLoadingWorkbook executed successfully. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
