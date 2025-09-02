---
title: Working with the ThreeDFormat of Shape or Chart with JavaScript via C++
linktitle: Working with the ThreeDFormat of Shape or Chart
type: docs
weight: 250
url: /javascript-cpp/working-with-the-threedformat-of-shape-or-chart/
---

## **Possible Usage Scenarios**
Aspose.Cells for JavaScript via C++ provides the [Shape.threeDFormat](https://reference.aspose.com/cells/javascript-cpp/shape/#threeDFormat--) property along with [ThreeDFormat](https://reference.aspose.com/cells/javascript-cpp/threedformat) class to work with the 3-D Format of shape or chart. The [ThreeDFormat](https://reference.aspose.com/cells/javascript-cpp/threedformat) class contains different properties which can be set to achieve different results as per application requirements.

## **Working with the ThreeDFormat of Shape or Chart**
The following sample code loads the [source excel file](5115419.xlsx) and accesses the first shape in the first worksheet and sets the sub-properties of [Shape.threeDFormat](https://reference.aspose.com/cells/javascript-cpp/shape/#threeDFormat--) property and then saves the workbook in the [output excel file](5115410.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Apply 3D Format Example</title>
    </head>
    <body>
        <h1>Apply 3D Format to Shape</h1>
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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const ws = workbook.worksheets.get(0);

            const sh = ws.shapes.get(0);

            const n3df = sh.threeDFormat;
            n3df.contourWidth = 17;
            n3df.extrusionHeight = 32;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">3D formatting applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```