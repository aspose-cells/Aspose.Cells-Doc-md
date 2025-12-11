---  
title: Tile Picture as a Texture inside the Shape with JavaScript via C++  
linktitle: Tile Picture as a Texture inside the Shape  
type: docs  
weight: 1700  
url: /javascript-cpp/tile-picture-as-a-texture-inside-the-shape/  
description: Learn how to tile a small picture as a texture inside a shape using Aspose.Cells for JavaScript via C++.  
---  

## **Possible Usage Scenarios**  

When the picture is small and does not cover the entire surface of the shape while maintaining its quality, you have the option to tile it. Tiling fills the shape surface with a small image by repeating it as if it were tiles.  

## **Tile Picture as a Texture inside the Shape**  

You can fill the shape surface with an image and tile it using the [**Shape.isTiling()**](https://reference.aspose.com/cells/javascript-cpp/texturefill/#isTiling--) property by setting it **true**. Please see the following sample code, its [sample Excel file](46465050.xlsx) as well as the screenshot for reference.  

## **Screenshot**  

![todo:image_alt_text](tile-picture-as-a-texture-inside-the-shape_1.png)  

## **Sample Code**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Texture Fill IsTiling Example</title>
    </head>
    <body>
        <h1>Texture Fill IsTiling Example</h1>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first shape inside the worksheet
            const shape = worksheet.shapes.get(0);

            // Tile Picture as a Texture inside the Shape
            shape.fill.textureFill.isTiling = true;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputTextureFill_IsTiling.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Texture fill set to tiling. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```