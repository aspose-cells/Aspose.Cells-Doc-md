---
title: How to Scale a Worksheet with JavaScript via C++
linktitle: How to Scale a Worksheet
type: docs
weight: 130
url: /javascript-cpp/how-to-scale-a-worksheet/
description: This article shows you code explaining how to scale a worksheet using Aspose.Cells for JavaScript via C++.
keywords: JavaScript scale a worksheet, How to Scale a Worksheet using JavaScript via C++, Scale a worksheet in JavaScript via C++.
---

## **Possible Usage Scenarios**
Scaling a worksheet can be useful for various reasons, depending on the context in which you are working. Here are a few common reasons for scaling a worksheet:
1. **Fit to Page:** To ensure that all the content fits on a single page or a specific number of pages when printing, making it easier to read and manage without having to flip through multiple pages.

2. **Presentation:** To make the worksheet look more organized and professional, particularly when sharing it with others in meetings or reports.

3. **Readability:** To adjust the size of the text and other elements for better readability, especially for people who may have difficulty reading smaller fonts.

4. **Space Management:** To optimize the use of space on a worksheet, ensuring that there is no unnecessary white space and that all important information is visible without excessive scrolling.

5. **Data Visualization:** In the case of charts and graphs, scaling can help make them more comprehensible by adjusting the size to fit the available space appropriately.

6. **Consistency:** To maintain a consistent look and feel across multiple worksheets or documents, which is particularly important in professional and educational settings.

## **How to Scale a Worksheet in Excel**
Scaling a worksheet in Excel can help you fit your content onto a single page or a specified number of pages when printing. Here are the steps to scale a worksheet:

1. **Open Your Worksheet:** Open the Excel worksheet that you want to scale.

2. **Go to the Page Layout Tab:** Click on the Page Layout tab in the Ribbon.

3. **Scale to Fit Group:** In the Page Layout tab, find the Scale to Fit group. Here you have options to adjust the scaling.  
   - **Width:** This option allows you to specify how many pages wide the printed worksheet will be.  
   - **Height:** This option allows you to specify how many pages tall the printed worksheet will be.  
   - **Scale:** You can also set a custom scaling percentage here.  
   <br>
   <img src="1.png" width=60% />

4. **Adjust Width and Height:** Set the Width and Height to your desired number of pages. For example, set both to 1 page if you want the worksheet to fit on one page.

5. **Adjust Scaling Percentage (if needed):** If you prefer to set a specific scaling percentage, adjust the Scale box. For instance, setting it to 50 % will make everything half the size.

## **How to Scale a Worksheet Using JavaScript via C++**
Aspose.Cells for JavaScript via C++ is a powerful library for working with Excel files programmatically. To scale a worksheet using Aspose.Cells, you need to follow these steps: load the [sample file](sample.xlsx) and adjust the print settings so that the content fits the desired number of pages or a specific percentage of the original size.

### **Example: Fit to Page**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Fit To Page Example</title>
    </head>
    <body>
        <h1>Fit Worksheet to One Page</h1>
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
            
            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            
            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);
            
            // Access the PageSetup object
            const pageSetup = sheet.pageSetup;
            
            // Set the worksheet to fit to 1 page wide and 1 page tall
            pageSetup.fitToPagesWide = 1;
            pageSetup.fitToPagesTall = 1;
            
            // Saving the modified workbook and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_fit_to_page.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
            
            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet fitted to one page. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
<br>
<img src="3.png" width=60% />

### **Example: Scale to Percentage**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Scale Worksheet</title>
    </head>
    <body>
        <h1>Scale Worksheet Example</h1>
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
            
            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            
            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);
            
            // Access the PageSetup object
            const pageSetup = sheet.pageSetup;
            
            // Set the scaling to a specific percentage (e.g., 75%)
            pageSetup.zoom = 75;
            
            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_scaled_percentage.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Scaled Workbook';
            
            document.getElementById('result').innerHTML = '<p style="color: green;">Scaling applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
<br>
<img src="2.png" width=60% />