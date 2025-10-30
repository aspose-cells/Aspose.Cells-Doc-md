---
title: Sortera data i kolumn med anpassad sorteringslista
type: docs
weight: 290
url: /sv/javascript-cpp/sort-data-in-column-with-custom-sort-list/
description: Lär dig att sortera data i kolumnen med en anpassad lista med hjälp av API t Aspose.Cells for JavaScript via C++.
keywords: Sortera Data i Kolumn med Anpassad Sorteringslista, Sortera data med anpassad lista.
---

## **Möjliga användningsscenario**

Du kan sortera data i en kolumn med en anpassad lista. Detta kan göras med [**DataSorter.addKey**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#addKey-number-sortorder-string-)-metoden. Men, denna metod fungerar endast om objekten i den anpassade listan inte innehåller kommatecken. Om de har kommatecken som "USA,US", "China,CN" etc., måste du använda [**DataSorter.addKey(number, SortOrder, string[])**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#addKey-number-sortorder-stringarray-)-metoden. Här är det sista parametern inte en String, utan en array av strängar.

## **Sortera Data i Kolumn med Anpassad Sorteringslista**

Följande exempel på kod förklarar hur man använder [**DataSorter.addKey(number, SortOrder, string[])**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#addKey-number-sortorder-stringarray-)-metoden för att sortera data med en anpassad sorteringslista. Se [exempel-Excel fil](50528327.xlsx) som används i denna kod och [utdata Excel-fil](50528328.xlsx) som genereras av den. Följande skärmbild visar effekten av koden på exempel-Excel-filen vid körning.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Custom Sort List</title>
    </head>
    <body>
        <h1>Custom Sort List Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Specify cell area - sort from A1 to A40
            const ca = AsposeCells.CellArea.createCellArea("A1", "A40");

            // Create Custom Sort list
            const customSortList = ["USA,US", "Brazil,BR", "China,CN", "Russia,RU", "Canada,CA"];

            // Add Key for Column A, Sort it in Ascending Order with Custom Sort List
            wb.dataSorter.addKey(0, AsposeCells.SortOrder.Ascending, customSortList);

            wb.dataSorter.sort(ws.cells, ca);

            // Save the output Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSortData_CustomSortList.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sorting completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
