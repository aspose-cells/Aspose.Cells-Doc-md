---
title: Specificera sorteringsvarning vid sortering av data
type: docs
weight: 140
url: /sv/javascript-cpp/specifying-sort-warning-while-sorting-data/
description: Lär dig att ange sortvarningsmeddelande vid sortering av data med hjälp av API t Aspose.Cells for JavaScript via C++.
keywords: Lägg till sorteringsvarning vid sortering av data, ställ in sorteringsvarning vid sortering av data, välj sorteringsvarning vid sortering av data.
---

## **Möjliga användningsscenario**

Vänligen ta hänsyn till denna textuella data dvs. {11, 111, 22}. Denna textuella data sorteras eftersom, i termer av text, kommer 111 före 22. Men om du vill sortera denna data inte som text utan som siffror, så blir den {11, 22, 111} eftersom talmässigt kommer 111 efter 22. Aspose.Cells for JavaScript via C++ tillhandahåller egenskapen `{0}` för att hantera detta. Sätt egenskapen till **true** så kommer din textuella data att sorteras som numerisk data. Följande skärmbild visar varningsmeddelandet för sortering som visas av Microsoft Excel när textuell data som ser ut som numerisk data sorteras.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Exempelkod**

Den följande exemplarkoden illustrerar användningen av [**DataSorter.sortAsNumber**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sortAsNumber-boolean-)-egenskapen enligt tidigare förklaring. Kontrollera dess [exempelfil för Excel](43352075.xlsx) och [utdatafil för Excel](43352076.xlsx) för mer hjälp.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Sort As Number Example</title>
    </head>
    <body>
        <h1>Sort As Number Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper, CellArea, SortOrder } = AsposeCells;

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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Create your cell area.
            const ca = AsposeCells.CellArea.createCellArea("A1", "A20");

            // Create your sorter.
            const sorter = workbook.dataSorter;

            // Find the index for column A.
            const idx = CellsHelper.columnNameToIndex("A");

            // Add key in sorter, it will sort in Ascending order.
            sorter.addKey(idx, SortOrder.Ascending);

            // Set sort as number
            sorter.sortAsNumber = true;

            // Perform sort.
            sorter.sort(worksheet.cells, ca);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSortAsNumber.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sort completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
