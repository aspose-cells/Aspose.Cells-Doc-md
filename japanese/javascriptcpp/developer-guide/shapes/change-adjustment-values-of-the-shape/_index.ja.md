---
title: JavaScript（C++経由）でシェイプの調整値を変更する
linktitle: シェイプの調整値の変更
type: docs
weight: 2000
url: /ja/javascript-cpp/change-adjustment-values-of-the-shape/
description: Aspose.Cells for JavaScriptを使用してExcel内のシェイプの調整値を変更する方法を学びます。
---

{{% alert color="primary" %}}  
Aspose.Cells は、シェイプの調整ポイントを変更するための [**Shape.geometry**](https://reference.aspose.com/cells/javascript-cpp/shape/#geometry--) プロパティを提供します。Microsoft Excel の UI では、調整は黄色のダイヤモンドノードとして表示されます。例:  

- 角丸四角形は、円弧を変更するための調整があります  
- 三角形は、ポイントの位置を変更するための調整があります  
- 台形は、上部の幅を変更するための調整があります  
- 矢印には、頭部と末尾の形状を変更するための2つの調整があります  

この記事では、異なるシェイプの調整値を変更するための [**Shape.geometry**](https://reference.aspose.com/cells/javascript-cpp/shape/#geometry--) プロパティの使用方法について説明します。  
{{% /alert %}}  

## **調整値の変更**  

以下のコードサンプルは、シェイプの調整値を変更する方法を示しています。  

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

            // Create workbook object from source excel file
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

## **ExcelでRoundedRectangularCalloutの先端点を設定または変更する方法**  

以下のコード例は、Excelでラウンド長方形のコールアウトの先端点位置を設定または変更する方法を示しています。  

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
