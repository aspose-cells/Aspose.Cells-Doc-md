---
title: Data Filtering
type: docs
weight: 85
url: /javascript-cpp/data-filtering/
description: Learn how to add a data filter by using the Aspose.Cells for JavaScript via C++ API.
keywords: Add Filter by Color JavaScript via C++, Add Date Filters JavaScript via C++, Add Number Filters JavaScript via C++, Add Dynamic Filter JavaScript via C++, Add Text Filters JavaScript via C++, Add custom filter with Contains JavaScript via C++, Add custom filter with NotContains JavaScript via C++, Add custom filter with BeginsWith JavaScript via C++, Add custom filter with EndsWith JavaScript via C++
---

{{% alert color="primary" %}}
Microsoft Excel provides some good features to autofilter worksheet data. Aspose.Cells fully supports Microsoft Excel's autofilter features. This article explains how to use the features in Microsoft Excel, and how to code them using Aspose.Cells for JavaScript via C++.
{{% /alert %}}

## **Autofilter Data**

Autofiltering is the quickest way to select only those items from the worksheet that you want to display in a list. The autofilter feature allows users to filter items in a list according to a set of criteria. Filter based on text, numbers, or dates.

### **Autofilter in Microsoft Excel**

To activate the autofilter feature in Microsoft Excel:

1. Click the heading row in a worksheet.  
2. From the **Data** menu, select **Filter** and then **AutoFilter**.

When you apply an autofilter to a worksheet, filter switches (black arrows) appear to the right of the column headings.

1. Click a filter arrow to see a list of filter options.

Some of the autofilter options are:

| **Options**        | **Description**                                                                 |
|--------------------|---------------------------------------------------------------------------------|
| All                | Show all items in the list once.                                                |
| Custom             | Customize filter criteria like contains / not contains                         |
| Filter by Color    | Filters based on filled color                                                  |
| Date Filters       | Filters rows based on different date criteria                                  |
| Number Filters     | Different types of filter on numbers like comparison, averages, and Top 10 etc. |
| Text Filters       | Different filters like begins with, ends with, contains etc.                    |
| Blanks/Non Blanks  | These filters can be implemented through the Text Filter Blank option          |

Users manually filter their worksheet data in Microsoft Excel using these options.

### **Autofilter with Aspose.Cells for JavaScript via C++**

Aspose.Cells provides the [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) class that represents an Excel file. The Workbook class contains a **Worksheets** collection that allows access to each worksheet in the Excel file.

A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) class. The Worksheet class provides a wide range of properties and methods to manage worksheets. To create an autofilter, use the **AutoFilter** property of the Worksheet class. The **AutoFilter** property is an object of the **AutoFilter** class, which provides the **Range** property for specifying the range of cells that make up a heading row. An autofilter is applied to the range of cells that is the heading row.

In each worksheet, you can only specify one filter range. This limitation is imposed by Microsoft Excel. For custom data filtering, use the **AutoFilter.Custom** method.

In the example given below, we have created the same AutoFilter using Aspose.Cells for JavaScript via C++ as we created using Microsoft Excel in the above section.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells AutoFilter Example</title>
    </head>
    <body>
        <h1>AutoFilter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;
        
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
            
            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            
            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);
            
            // Creating AutoFilter by giving the cells range of the heading row
            worksheet.autoFilter.range = "A1:B1";
            
            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
            
            resultDiv.innerHTML = '<p style="color: green;">AutoFilter created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

#### **Different Types of Filter**

Aspose.Cells provides multiple options to apply different types of filters such as Color Filter, Date Filter, Number Filter, Text Filter, Blank Filters, and Non‑Blank Filters.

##### **Fill Color**

Aspose.Cells provides a function **AddFillColorFilter** to filter data based upon the fill‑color property of the cells. In the example given below, a template file having different fill colors in the first column of the sheet is used to test the color‑filtering function. Sample files can be downloaded from the following links.

1. [ColouredCells.xlsx](72417315.xlsx)  
2. [FilteredColouredCells.xlsx](72417316.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Filter Coloured Cells Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiating a CellsColor object for foreground color
            const clrForeground = workbook.createCellsColor();
            clrForeground.color = AsposeCells.Color.fromArgb(255, 0, 0); // Red color

            // Instantiating a CellsColor object for background color
            const clrBackground = workbook.createCellsColor();
            clrBackground.color = AsposeCells.Color.fromArgb(255, 255, 255); // White color

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Call AddFillColorFilter function to apply the filter
            worksheet.autoFilter.addFillColorFilter(0, AsposeCells.BackgroundType.Solid, clrForeground, clrBackground);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredColouredCells.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Date**

Different types of date filters can be implemented, such as filtering all the rows having dates in January 2018. The following sample code demonstrates this filter using the **AddDateFilter** function. Sample files are given below.

1. [Date.xlsx](72417317.xlsx)  
2. [FilteredDate.xlsx](72417318.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Date Filter</title>
    </head>
    <body>
        <h1>Date Filter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Call AddDateFilter function to apply the filter
            worksheet.autoFilter.addDateFilter(0, AsposeCells.DateTimeGroupingType.Month, 2018, 1, 0, 0, 0, 0);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredDate.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Dynamic Date**

Sometimes dynamic filters are required based on date, such as all the cells having dates in January irrespective of the year. In this case, the **DynamicFilter** function is used, as shown in the following sample code. Sample files are given below.

1. [Date.xlsx](72417317.xlsx)  
2. [FilteredDynamicDate.xlsx](72417319.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Filter Dynamic Date Example</h1>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Call DynamicFilter function to apply the filter
            worksheet.autoFilter.dynamic_Filter(0, AsposeCells.DynamicFilterType.January);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredDynamicDate.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Number**

Custom filters can be applied using Aspose.Cells, such as selecting cells that have numbers between a given range. The following example demonstrates the usage of the **Custom()** function to filter numbers. Sample files are given below.

1. [Number.xlsx](72417320.xlsx)  
2. [FilteredNumber.xlsx](72417321.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Filter Numbers</title>
    </head>
    <body>
        <h1>Filter Numbers Example</h1>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Call Custom function to apply the filter
            worksheet.autoFilter.custom(0, AsposeCells.FilterOperatorType.GreaterOrEqual, 5, true, AsposeCells.FilterOperatorType.LessOrEqual, 10);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredNumber.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Text**

If a column contains text and you want to select cells containing a particular string, the **Filter()** function can be used. In the following example, the template file contains a list of countries, and the row to be selected contains a specific country name. Sample files are given below.

1. [Text.xlsx](72417322.xlsx)  
2. [FilteredText.xlsx](72417323.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Filter AutoFilter Example</h1>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Call Filter function to apply the filter
            const autoFilter = worksheet.autoFilter;
            autoFilter.filter(0, "Angola");

            // Call refresh function to update the worksheet
            autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredText.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Blanks**

If a column contains text such that a few cells are blank, and you need to filter rows where blank cells are present, the **MatchBlanks()** function can be used as demonstrated below. Sample files are given below.

1. [Blank.xlsx](72417324.xlsx)  
2. [FilteredBlank.xlsx](72417325.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Filter Blank Rows Example</title>
    </head>
    <body>
        <h1>Filter Blank Rows Example</h1>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Call MatchBlanks function to apply the filter
            worksheet.autoFilter.matchBlanks(0);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredBlank.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filtering completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Non Blanks**

When cells containing any text are to be filtered, use the **MatchNonBlanks** filter function as demonstrated below. Sample files are given below.

1. [Blank.xlsx](72417324.xlsx)  
2. [FilteredNonBlank.xlsx](72417326.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Filter Non-Blank Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Read the selected file
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Call MatchNonBlanks function to apply the filter
            worksheet.autoFilter.matchNonBlanks(0);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredNonBlank.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Custom filter with Contains**

Excel provides custom filters that filter rows which contain a specific string. This feature is available in Aspose.Cells and is demonstrated below by filtering the names in the sample file. Sample files are given below.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)  
2. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells AutoFilter Example</title>
    </head>
    <body>
        <h1>AutoFilter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FilterOperatorType } = AsposeCells;
        
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

            // Creating AutoFilter by giving the cells range
            worksheet.autoFilter.range = "A1:A18";

            // Initialize filter for rows containing the string "Ba"
            worksheet.autoFilter.custom(0, FilterOperatorType.Contains, "Ba");

            // Refresh the filter to show/hide filtered rows
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outSourseSampleCountryNames.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Custom filter with NotContains**

Excel provides custom filters that filter rows which do not contain a specific string. This feature is available in Aspose.Cells and is demonstrated below by filtering the names in the sample file.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells AutoFilter Example</title>
    </head>
    <body>
        <h1>AutoFilter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FilterOperatorType } = AsposeCells;
        
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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Creating AutoFilter by giving the cells range
            worksheet.autoFilter.range = "A1:A18";

            // Initialize filter for rows not containing the string "Be"
            worksheet.autoFilter.custom(0, FilterOperatorType.NotContains, "Be");

            // Refresh the filter to show/hide filtered rows
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outSourseSampleCountryNames.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Custom filter with BeginsWith**

Excel provides custom filters that filter rows which begin with a specific string. This feature is available in Aspose.Cells and is demonstrated below by filtering the names in the sample file.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Filter Countries Starting With "Ba"</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FilterOperatorType } = AsposeCells;
        
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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Creating AutoFilter by giving the cells range
            worksheet.autoFilter.range = "A1:A18";

            // Initialize filter for rows starting with the string "Ba"
            worksheet.autoFilter.custom(0, FilterOperatorType.BeginsWith, "Ba");

            // Refresh the filter to show/hide filtered rows
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outSourseSampleCountryNames.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Custom filter with EndsWith**

Excel provides custom filters that filter rows which end with a specific string. This feature is available in Aspose.Cells and is demonstrated below by filtering the names in the sample file.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply AutoFilter Example</h1>
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
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Creating AutoFilter by giving the cells range
            const autoFilter = worksheet.autoFilter;
            autoFilter.range = "A1:A18";

            // Initialize filter for rows ending with the string "ia"
            autoFilter.custom(0, AsposeCells.FilterOperatorType.EndsWith, "ia");

            // Refresh the filter to show/hide filtered rows
            autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outSourseSampleCountryNames.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Advanced Topics**
- [Apply Advanced Filter of Microsoft Excel to Display Records Meeting Complex Criteria](/cells/javascript-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Get All Hidden Rows Indices after Refreshing AutoFilter](/cells/javascript-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/)