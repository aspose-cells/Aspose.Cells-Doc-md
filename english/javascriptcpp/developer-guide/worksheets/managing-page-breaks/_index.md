---
title: Managing Page Breaks with JavaScript via C++
linktitle: Managing Page Breaks
type: docs
weight: 30
url: /javascript-cpp/managing-page-breaks/
description: This article provides sample code and explains how to add, clear, or delete specific page breaks in Excel worksheets programmatically using Aspose.Cells for JavaScript via C++.
keywords: page breaks JavaScript via C++, excel page breaks JavaScript via C++, clear page break JavaScript via C++, delete specific page break JavaScript via C++
---

{{% alert color="primary" %}}

According to the definition, a page break is a place in a flow of text where one page ends and the next begins. Microsoft Excel lets users add page breaks into any selected cell of a worksheet.

When a page break is added at a cell, the page ends at that point and the remaining data after the break is printed on the next page. In simple words, page breaks divide your worksheet into multiple pages according to your specifications. You can also add page breaks to your worksheets at runtime using Aspose.Cells. Aspose.Cells allows developers to add two kinds of page breaks:

- Horizontal page break
- Vertical page break

In the rest of the discussion, we will describe how you can add horizontal or vertical page breaks into your worksheets using Aspose.Cells.

{{% /alert %}}

## **Page Breaks**

Aspose.Cells for JavaScript via C++ provides a [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) class that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) class contains a [**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) collection that allows access to each worksheet in the Excel file.

A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) class provides a wide range of properties and methods used to manage a worksheet.

To add the page breaks, use the [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) class' [**worksheet.horizontalPageBreaks**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#horizontalPageBreaks--) and [**worksheet.verticalPageBreaks**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#verticalPageBreaks--) properties.

The [**worksheet.horizontalPageBreaks**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#horizontalPageBreaks--) and [**worksheet.verticalPageBreaks**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#verticalPageBreaks--) properties are collections that may contain several page breaks. Each collection contains several methods for managing horizontal and vertical page breaks.

### **Adding Page Breaks**

To add a page break in a worksheet, insert vertical and horizontal page breaks at the specified cell by calling the [**HorizontalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/horizontalpagebreakcollection/#add-number-number-number-) and [**VerticalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/verticalpagebreakcollection/#add-number-number-number-) methods. Each **add** method takes the name of the cell where the break should be added.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Adding Page Breaks Example</h1>
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

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add a page break at cell Y30
            worksheet.horizontalPageBreaks.add("Y30");
            worksheet.verticalPageBreaks.add("Y30");

            // Save the Excel file (Excel 97-2003 format .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddingPageBreaks_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page breaks added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

In page break preview or print preview modes, you can see how these page breaks work.

{{% /alert %}}

### **Removing Specific Page Break**

To remove a specific page break, call the [**HorizontalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/javascript-cpp/horizontalpagebreakcollection/#removeAt-number-) and [**VerticalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/javascript-cpp/verticalpagebreakcollection/#removeAt-number-) methods. Each **removeAt** method takes the index of the page break to be removed.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Remove Specific Page Break Example</title>
    </head>
    <body>
        <h1>Remove Specific Page Break Example</h1>
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
            
            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            
            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);
            
            // Removing a specific page break
            worksheet.horizontalPageBreaks.removeAt(0);
            worksheet.verticalPageBreaks.removeAt(0);
            
            // Saving the Excel file (Excel 97-2003 format for .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RemoveSpecificPageBreak_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
            
            document.getElementById('result').innerHTML = '<p style="color: green;">Page breaks removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Important to Know**

When you set **fitToPages** properties (that is [**PageSetup.fitToPagesTall**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesTall--) and [**PageSetup.fitToPagesWide**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesWide--)) in page setup settings, the page break settings are affected, so if you print the worksheet, the page break settings are ignored even though they remain set.