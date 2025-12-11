---
title: Convert the Smart Art to Group Shape with JavaScript via C++
linktitle: Convert the Smart Art to Group Shape
type: docs
weight: 200
url: /javascript-cpp/convert-the-smart-art-to-group-shape/
---

## **Possible Usage Scenarios**

You can convert a Smart Art shape into a Group shape using the [**Shape.resultOfSmartArt**](https://reference.aspose.com/cells/javascript-cpp/shape/#resultOfSmartArt--) method. It will enable you to handle the Smart Art shape like a group shape. Consequently, you will have access to the individual parts or shapes of the group shape.

## **Convert the Smart Art to Group Shape**

The following sample code loads the [sample Excel file](55541793.xlsx) containing a Smart Art shape as shown in this screenshot. It then converts the Smart Art shape into a Group shape and prints the `Shape.isGroup` property. Please see the console output of the sample code given below.

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **Sample Code**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Get Result of SmartArt</title>
    </head>
    <body>
        <h1>Get Result of SmartArt Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;
        
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
            const resultDiv = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first shape
            const shape = worksheet.shapes.get(0);

            // Determine if shape is Smart Art (property access, not method)
            const isSmartArt = shape.isSmartArt;

            // Determine if shape is a group shape (property access)
            const isGroup = shape.isGroup;

            // Convert Smart Art shape into group shape result and check if group (getResultOfSmartArt → resultOfSmartArt property)
            const resultOfSmartArtIsGroup = shape.resultOfSmartArt.isGroup;

            const html = [
                `<p>Is Smart Art Shape: ${isSmartArt}</p>`,
                `<p>Is Group Shape: ${isGroup}</p>`,
                `<p>Result of SmartArt is Group: ${resultOfSmartArtIsGroup}</p>`
            ].join('');

            resultDiv.innerHTML = html;
        });
    </script>
</html>
```

## **Console Output**

{{< highlight javascript >}}
Is Smart Art Shape: True
Is Group Shape: False
Is Group Shape: True
{{< /highlight >}}