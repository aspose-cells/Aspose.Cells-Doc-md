---  
title: Measure the Width and Height of the Cell Value in Unit of Pixels  
linktitle: Measure the Size  
type: docs  
weight: 260  
url: /javascript-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/  
description: Learn how to Measure the Width and Height of the Cell Value in Unit of Pixels through the Aspose.Cells for JavaScript via C++.  
keywords: Measure the Width of the Cell Value in Unit of Pixels JavaScript via C++, Measure the Height of the Cell Value in Unit of Pixels JavaScript via C++, Get the Width of the Cell Value in Unit of Pixels JavaScript via C++, Get the Height of the Cell Value in Unit of Pixels JavaScript via C++  
---  

{{% alert color="primary" %}}  

Sometimes you need to calculate the width and height of a cell value to fit the cell value inside the cell. Aspose.Cells provides [**Cell.widthOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#widthOfValue--) and [**Cell.heightOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#heightOfValue--) methods for this purpose. By using these methods, you can calculate the width and height of the cell value, then set the column width and row height of that cell respectively; this will adjust or fit the cell value inside the cell.  

Alternatively, you can also [autofit rows and columns of your cell or range of cells](/cells/javascript-cpp/autofit-rows-and-columns/) using Aspose.Cells APIs.  

{{% /alert %}}  

The following code explains the use of [**Cell.widthOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#widthOfValue--) and [**Cell.heightOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#heightOfValue--) methods.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Cell Size Example</h1>
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

            // Create or load workbook
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

            // Access cell B2 and add a value inside it
            const cell = worksheet.cells.get("B2");
            cell.value = "Welcome to Aspose!";

            // Enlarge its font to size 16
            const style = cell.style;
            style.font.size = 16;
            cell.style = style;

            // Calculate the width and height of the cell value in units of pixels
            const widthOfValue = cell.widthOfValue;
            const heightOfValue = cell.heightOfValue;

            // Print both values to the page
            document.getElementById('result').innerHTML = `<p>Width of Cell Value: ${widthOfValue}</p><p>Height of Cell Value: ${heightOfValue}</p>`;

            // Set the row height and column width to adjust/fit the cell value inside the cell
            worksheet.cells.setColumnWidthPixel(1, widthOfValue);
            worksheet.cells.setRowHeightPixel(1, heightOfValue);

            // Save the output Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```


## **Advanced topics**  
- [Get Text Width of Cell Value](/cells/javascript-cpp/get-text-width-of-cell-value/)