---
title: Data Sortering
type: docs
weight: 130
url: /sv/javascript-cpp/sort-data-of-excel/
description: Lär dig att sortera data med hjälp av Aspose.Cells for JavaScript via C++ API.
keywords: Sortera data i stigande eller fallande ordning, Sortera data baserat på bakgrundsfärg
---

{{% alert color="primary" %}}

Datasortering är en av Microsoft Excels många användbara funktioner. Det gör det möjligt för användare att ordna data för att göra det enklare att överblicka. Aspose.Cells for JavaScript via C++ låter utvecklare sortera kalkylbladdata alfabetiskt eller numeriskt, vilket fungerar på samma sätt som Microsoft Excel gör för att sortera data.

{{% /alert %}}

## **Sortering av data i Microsoft Excel**

För att sortera data i Microsoft Excel:

1. Välj **Data** från **Sortera**-menyn. Sorteringsdialogen visas.
1. Välj ett sorteringsalternativ.

I allmänhet utförs sortering på en lista - definierad som en sammanhängande grupp data där data visas i kolumner.

## **Sortera data med Aspose.Cells**

Aspose.Cells for JavaScript via C++ tillhandahåller klassen [**DataSorter**](https://reference.aspose.com/cells/javascript-cpp/datasorter) som används för att sortera data i stigande eller fallande ordning. Klassen har några viktiga medlemmar, till exempel egenskaper som Key1 ... Key3 och Order1 ... Order3. Dessa medlemmar används för att definiera sorterade nycklar och ange nyckelordning.

Du måste definiera nycklar och ange sorteringsordningen innan du implementerar datasortering. Klassen tillhandahåller metoden [**DataSorter.sort**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sort-cells-cellarea-) som används för att utföra datasortering baserat på celldata i ett arbetsblad.

Metoden [**DataSorter.sort**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sort-cells-cellarea-) accepterar följande parametrar:

- [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells), cellerna för det underliggande arbetsbladet.
- [**CellArea**](https://reference.aspose.com/cells/javascript-cpp/cellarea), cellområdet. Definiera cellområdet innan du tillämpar datasortering.

Detta exempel använder mallfilen "Bok1.xls" skapad i Microsoft Excel. Efter att koden har utförts sorteras data på lämpligt sätt.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>DataSorter Example</title>
    </head>
    <body>
        <h1>DataSorter Example</h1>
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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the workbook datasorter object.
            const sorter = workbook.dataSorter;

            // Set the first order for datasorter object.
            sorter.order1 = AsposeCells.SortOrder.Descending;
            // Define the first key.
            sorter.key1 = 0;
            // Set the second order for datasorter object.
            sorter.order2 = AsposeCells.SortOrder.Ascending;
            // Define the second key.
            sorter.key2 = 1;

            // Create a cells area (range).
            const ca = new AsposeCells.CellArea();
            // Specify the start row index.
            ca.startRow = 0;
            // Specify the start column index.
            ca.startColumn = 0;
            // Specify the last row index.
            ca.endRow = 13;
            // Specify the last column index.
            ca.endColumn = 1;

            // Sort data in the specified data range (A1:B14)
            sorter.sort(workbook.worksheets.get(0).cells, ca);

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sorting completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Om du vill sortera *FrånVänsterTillHöger*, använd attributet [**DataSorter.sortLeftToRight**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sortLeftToRight-boolean-).

{{% /alert %}}

### **Sortera data med bakgrundsfärg**

Excel erbjuder funktioner för att sortera data baserat på bakgrundsfärg. Samma funktion finns tillgänglig med Aspose.Cells for JavaScript via C++ med DataSorter där [**SortOnType**](https://reference.aspose.com/cells/javascript-cpp/sortontype/).CellColor kan användas i [**DataSorter.addKey**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#addColorKey-number-sortontype-sortorder-color-) för att sortera data baserat på bakgrundsfärgen. Alla celler som innehåller vald färg i [**DataSorter.addKey**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#addColorKey-number-sortontype-sortorder-color-)-funktionen placeras överst eller längst ner enligt SortOrder-inställningen och ordningen för de återstående cellerna ändras inte alls.

Följande är provfiler som kan laddas ned för att testa denna funktion:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Custom Sort by Cell Color</title>
    </head>
    <body>
        <h1>Custom Sort by Cell Color Example</h1>
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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the data sorter (converted from getDataSorter())
            const sorter = workbook.dataSorter;

            // Add key for second column for red color
            sorter.addKey(1, AsposeCells.SortOnType.CellColor, AsposeCells.SortOrder.Descending, AsposeCells.Color.Red);

            // Perform the sort on the first worksheet cells (converted from getWorksheets().get(0).getCells())
            sorter.sort(workbook.worksheets.get(0).cells, AsposeCells.CellArea.createCellArea("A2", "C6"));

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSortData_CustomSortList.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Sorted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sorting completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Fortsatta ämnen**
- [Sortera Data i Kolumn med Anpassad Sorteringslista](/cells/sv/javascript-cpp/sort-data-in-column-with-custom-sort-list/)
- [Angivande av sorteringsvarning vid sortering av data](/cells/sv/javascript-cpp/specifying-sort-warning-while-sorting-data/)
