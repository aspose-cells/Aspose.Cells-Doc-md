---
title: Change Cells Alignment and Keep Existing Formatting
linktitle: Change Cells Alignment and Keep Existing Formatting
description: Use the Aspose.Cells library to change cell alignment and preserve existing formatting in JavaScript via C++
keywords: Aspose.Cells, JavaScript via C++, Cell alignment, preserve existing formatting
type: docs
weight: 340
url: /javascript-cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **Possible Usage Scenarios**

Sometimes, you want to change the alignment of multiple cells but also want to keep existing formatting. Aspose.Cells for JavaScript via C++ allows you to do it using the [**StyleFlag.alignments(boolean)**](https://reference.aspose.com/cells/javascript-cpp/styleflag/#alignments-boolean-) method. If you set it to **true**, changes in alignment will take place; otherwise, they will not. Please note that the [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag) object is passed as a parameter to the [**Range.applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/range/#applyStyle-style-styleflag-) method, which actually applies the formatting to a range of cells.

## **Change Cells Alignment and Keep Existing Formatting**

The following sample code loads the [sample Excel file](67338585.xlsx), creates the range, and center‑aligns it horizontally and vertically, keeping the existing formatting intact. The following screenshot compares the sample Excel file with the [output Excel file](67338586.xlsx) and shows that all existing formatting of the cells is the same, except that the cells are now center‑aligned horizontally and vertically.

![Change cells alignment while preserving formatting](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Sample Code**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Change Cells Alignment and Keep Existing Formatting</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, TextAlignmentType, Utils } = AsposeCells;
        
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
            
            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            
            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);
            
            // Create cells range
            const range = worksheet.cells.createRange("B2:D7");
            
            // Create style object
            const style = workbook.createStyle();
            
            // Set the horizontal and vertical alignment to center using property assignments
            style.horizontalAlignment = TextAlignmentType.Center;
            style.verticalAlignment = TextAlignmentType.Center;
            
            // Create style flag object
            const flag = new StyleFlag();
            flag.alignments = true; // Set style flag alignments to true
            
            // Apply style to range of cells
            range.applyStyle(style, flag);
            
            // Save the workbook in XLSX format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputChangeCellsAlignmentAndKeepExistingFormatting.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
            
            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```