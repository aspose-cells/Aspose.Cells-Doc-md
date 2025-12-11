---
title: Determine if Shape is Smart Art Shape with JavaScript via C++
linktitle: Determine if Shape is Smart Art Shape
type: docs
weight: 400
url: /javascript-cpp/determine-if-shape-is-smart-art-shape/
description: Learn how to determine if a shape in Excel is a Smart Art shape using Aspose.Cells for JavaScript via C++.
---

## **Possible Usage Scenarios**  

SmartArt shapes are special shapes in Microsoft Excel that allow you to create complex diagrams automatically. You can determine whether a shape is a SmartArt shape or a normal shape using the **Shape.isSmartArt()** property.  

## **Determine if Shape is SmartArt Shape**  

The following sample code loads the [sample Excel file](55541792.xlsx) containing a SmartArt shape, as shown in this screenshot. It then prints the value of the **Shape.isSmartArt()** property of the first shape. Please see the console output of the sample code given below.  

![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)  

## **Sample Code**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            
            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);
            
            // Accessing the first shape
            const shape = worksheet.shapes.get(0);
            
            // Determine if shape is SmartArt (converted to property access)
            const isSmartArt = shape.isSmartArt;
            
            document.getElementById('result').innerHTML = `<p>Is Smart Art Shape: ${isSmartArt}</p>`;
        });
    </script>
</html>
```  

## **Console Output**  

{{< highlight java >}}  

Is Smart Art Shape: True  

{{< /highlight >}}