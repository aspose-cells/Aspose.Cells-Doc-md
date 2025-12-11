---  
title: Change Adjustment Values of the Shape with JavaScript via C++  
linktitle: Change Adjustment Values of the Shape  
type: docs  
weight: 2000  
url: /javascript-cpp/change-adjustment-values-of-the-shape/  
description: Learn how to change adjustment values of shapes in Excel using Aspose.Cells for JavaScript via C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells provides [**Shape.geometry**](https://reference.aspose.com/cells/javascript-cpp/shape/#geometry--) property to make changes to the adjustment points of shapes. In the Microsoft Excel UI, adjustments display as yellow diamond nodes. For example:  

- Rounded Rectangle has an adjustment to change the arc.  
- Triangle has an adjustment to change the location of the point.  
- Trapezoid has an adjustment to change the width of the top.  
- Arrows have two adjustments to change the shape of the head and tail.  

This article will explain the use of [**Shape.geometry**](https://reference.aspose.com/cells/javascript-cpp/shape/#geometry--) property to change the adjustment values of the different shapes.  
{{% /alert %}}  

## **Change Adjustment Values**  

The below code sample shows how to change adjustment values of the shape.  

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Shapes Adjust Values Example</title>
    </head>
    <body>
        <h1>Shapes Adjust Values Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm" />
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

            // Create workbook object from source Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first three shapes of the worksheet
            const shape1 = worksheet.shapes.get(0);
            const shape2 = worksheet.shapes.get(1);
            const shape3 = worksheet.shapes.get(2);

            // Change the adjustment values of the shapes
            shape1.geometry.shapeAdjustValues.get(0).value = 0.5;
            shape2.geometry.shapeAdjustValues.get(0).value = 0.8;
            shape3.geometry.shapeAdjustValues.get(0).value = 0.5;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shapes updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **How to Set or Change the RoundedRectangularCallout Tip Point in Excel**  

The following code example shows how to set or change a rounded rectangle callout tip point position in Excel.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells RoundedRectangularCallout Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink1" style="display: none; margin-right: 10px;"></a>
        <a id="downloadLink2" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoShapeType, Utils } = AsposeCells;
        
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
            // Create a new workbook
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);

            // Add a RoundedRectangularCallout to the worksheet
            const polygonShape = sheet.shapes.addAutoShape(AutoShapeType.RoundedRectangularCallout, 0, 0, 0, 0, 0, 0);

            // Shape positioning and sizing (converted from setters to property assignments)
            polygonShape.top = 200;
            polygonShape.left = 500;
            polygonShape.width = 200;
            polygonShape.height = 100;

            // Access shape geometry and adjust values (getters converted to properties)
            const shapeGuides = polygonShape.geometry.shapeAdjustValues;
            shapeGuides.add("adj1", 1.02167);
            shapeGuides.add("adj2", -0.295);
            shapeGuides.add("adj3", 0.16667);

            // Save the workbook to an in-memory file (res.xlsx)
            const outputData1 = workbook.save(SaveFormat.Xlsx);
            const uint8_1 = new Uint8Array(outputData1);
            const blob1 = new Blob([uint8_1], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'res.xlsx';
            downloadLink1.style.display = 'inline';
            downloadLink1.textContent = 'Download res.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">res.xlsx created. Reopening and modifying shape guides...</p>';

            // Read the saved workbook from the in-memory data
            const reopenedWorkbook = new Workbook(uint8_1);
            const reopenedSheet = reopenedWorkbook.worksheets.get(0);

            // Get the RoundedRectangularCallout from the worksheet
            const reopenedPolygonShape = reopenedSheet.shapes.get(0);
            const reopenedShapeGuides = reopenedPolygonShape.geometry.shapeAdjustValues;

            // Modify the first shape guide value (converted setter to property assignment)
            reopenedShapeGuides.get(0).value = 0.7;

            // Save the modified workbook to a second in-memory file (res-resave.xlsx)
            const outputData2 = reopenedWorkbook.save(SaveFormat.Xlsx);
            const uint8_2 = new Uint8Array(outputData2);
            const blob2 = new Blob([uint8_2], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'res-resave.xlsx';
            downloadLink2.style.display = 'inline';
            downloadLink2.textContent = 'Download res-resave.xlsx';

            document.getElementById('result').innerHTML += '<p style="color: green;">res-resave.xlsx created with modified shape guide.</p>';
        });
    </script>
</html>
```