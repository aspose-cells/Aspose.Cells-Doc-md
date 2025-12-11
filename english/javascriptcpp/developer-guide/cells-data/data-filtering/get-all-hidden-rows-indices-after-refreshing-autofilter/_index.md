---
title: Get All Hidden Rows Indices after Refreshing AutoFilter
type: docs  
weight: 320  
url: /javascript-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/  
description: Learn how to get all hidden rows indices after refreshing AutoFilter by using the Aspose.Cells for JavaScript via C++ API.  
keywords: Get All Hidden Rows Indices after Refreshing AutoFilter JavaScript via C++, Obtain All Hidden Rows Indices after Refreshing AutoFilter JavaScript via C++, Retrieve All Hidden Rows Indices after Refreshing AutoFilter JavaScript via C++  
---

## **Possible Usage Scenarios**  

When you apply the AutoFilter on worksheet cells, some of the rows get hidden automatically. However, it might be the case that some rows are already hidden manually by the Excel end user and are not hidden by an AutoFilter. This makes it difficult to know which rows are hidden by the AutoFilter and which are hidden manually by the Excel end user. Aspose.Cells for JavaScript via C++ deals with this problem using the `Array` [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#refresh-boolean-). This method returns the row indices of all rows that are hidden by the AutoFilter and not manually by the Excel end user.  

## **Get All Hidden Rows Indices after Refreshing AutoFilter**  

Please see the following sample code that loads the [sample Excel file](64716909.xlsx), which contains some rows hidden manually by the Excel end user. The code applies the AutoFilter and refreshes it using the `Array` [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#refresh-boolean-) method that returns the row indices of all rows hidden by the AutoFilter. It then prints the indices of the hidden rows on the console along with cell names and values.  

## **Sample Code**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Get Hidden Rows After Refreshing AutoFilter</title>
    </head>
    <body>
        <h1>Get Hidden Rows After Refreshing AutoFilter</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Apply AutoFilter
            worksheet.autoFilter.addFilter(0, "Orange");

            // True means it will refresh AutoFilter and return hidden rows.
            const rowIndices = worksheet.autoFilter.refresh(true);

            console.log("Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.");
            console.log("--------------------------");

            let output = '<p>Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.</p><pre>';
            rowIndices.forEach(r => {
                const cell = worksheet.cells.get(r, 0);
                console.log(`${r}\t${cell.name}\t${cell.stringValue}`);
                output += `${r}\t${cell.name}\t${cell.stringValue}\n`;
            });
            output += '</pre>';

            resultDiv.innerHTML = output;
        });
    </script>
</html>
```


## **Console Output**  

{{< highlight java >}}  

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.  

\--------------------------  

1       A2      Apple  

2       A3      Apple  

3       A4      Apple  

6       A7      Apple  

7       A8      Apple  

11      A12     Pear  

12      A13     Pear  

{{< /highlight >}}