---
title: Working with the Shadow Effect of Shape or Chart with JavaScript via C++
linktitle: Working with the Shadow Effect of Shape or Chart
type: docs
weight: 220
url: /javascript-cpp/working-with-the-shadow-effect-of-shape-or-chart/
description: Learn how to work with the shadow effect of shapes or charts using Aspose.Cells for JavaScript via C++.
---

## **Possible Usage Scenarios**  
Aspose.Cells for JavaScript via C++ provides the [Shape.shadowEffect](https://reference.aspose.com/cells/javascript-cpp/shape/#shadowEffect--) property along with the [ShadowEffect](https://reference.aspose.com/cells/javascript-cpp/shadoweffect) class to work with the shadow effect of **a** shape or chart. The [ShadowEffect](https://reference.aspose.com/cells/javascript-cpp/shadoweffect) class contains the following properties which can be set to achieve different results as per application requirements.  

- [ShadowEffect.angle](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#angle--)  
- [ShadowEffect.blur](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#blur--)  
- [ShadowEffect.color](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#color--)  
- [ShadowEffect.distance](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#distance--)  
- [ShadowEffect.presetType](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#presetType--)  
- [ShadowEffect.size](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#size--)  
- [ShadowEffect.transparency](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#transparency--)  

## **Working with the Shadow Effect of Shape or Chart**  
The following sample code loads the **source Excel file** ([5115425.xlsx](5115425.xlsx)), accesses the first shape in the first worksheet, sets the sub‑properties of the [Shape.shadowEffect](https://reference.aspose.com/cells/javascript-cpp/shape/#shadowEffect--) property, and then saves the workbook to the **output Excel file** ([5115411.xlsx](5115411.xlsx)).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Shape Shadow Effect Example</h1>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);
            const shape = worksheet.shapes.get(0);

            const shadowEffect = shape.shadowEffect;
            shadowEffect.angle = 150;
            shadowEffect.blur = 4;
            shadowEffect.distance = 45;
            shadowEffect.transparency = 0.3;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shadow effect applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```