---
title: 在使用JavaScript通过C++处理ODS文件中的背景
linktitle: 在ODS文件中使用背景
type: docs
weight: 150
url: /zh/javascript-cpp/working-with-background-in-ods-files/
description: 学习如何使用Aspose.Cells for JavaScript通过C++管理ODS文件中的背景。
---

## **ODS文件中的背景**  

可以将背景添加到ODS文件中的工作表。背景可以是彩色背景或图形背景。在打开文件时背景不可见，但如果文件作为PDF打印，则在生成的PDF中可以看到背景。在打印预览对话框中也可以看到背景。  

Aspose.Cells for JavaScript通过C++支持读取和添加ODS文件的背景信息。  

## **从ODS文件读取背景信息**  

Aspose.Cells for JavaScript通过C++提供[**OdsPageBackground**](https://reference.aspose.com/cells/javascript-cpp/odspagebackground)类管理ODS文件中的背景。以下示例演示了使用[**OdsPageBackground**](https://reference.aspose.com/cells/javascript-cpp/odspagebackground)类，加载源ODS文件（90112030.ods）并读取背景信息。请参考代码生成的控制台输出。  

### **示例代码**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>ODS Background Extraction Example</title>
    </head>
    <body>
        <h1>ODS Background Extraction Example</h1>
        <input type="file" id="fileInput" accept=".ods,.xls,.xlsx,.csv" />
        <button id="runExample">Extract Background</button>
        <a id="downloadLink" style="display: none;">Download Background Image</a>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an ODS/Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access ODS page background from the worksheet's page setup
            const background = worksheet.pageSetup.odsPageBackground;

            // Read background properties
            const backgroundType = background.type.toString();
            const backgroundPosition = background.graphicPositionType.toString();

            document.getElementById('result').innerHTML = `<p>Background Type: ${backgroundType}</p><p>Background Position: ${backgroundPosition}</p>`;

            // Get graphic data and prepare download link
            const graphicData = background.graphicData;
            const blob = new Blob([graphicData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'background.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Background Image';
        });
    </script>
</html>
```  

### **控制台输出**  

{{< highlight javascript >}}  
Background Type: Graphic  
Background Position: CenterCenter  
{{< /highlight >}}  

## **向ODS文件添加彩色背景**  

Aspose.Cells for Java脚本通过C++提供[**OdsPageBackground**](https://reference.aspose.com/cells/javascript-cpp/odspagebackground)类以管理ODS文件中的背景。下方代码示例演示了如何使用[**OdsPageBackground.color**](https://reference.aspose.com/cells/javascript-cpp/odspagebackground/#color--)属性为ODS文件添加颜色背景。请查看由代码生成的[输出ODS](90112031.ods)文件以供参考。  

### **示例代码**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Colored ODS Background</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
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

            // Instantiate a new workbook. If a file is provided, open it; otherwise create a new workbook.
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Populate cells (converted to property-style assignments)
            worksheet.cells.get(0, 0).value = 1;
            worksheet.cells.get(1, 0).value = 2;
            worksheet.cells.get(2, 0).value = 3;
            worksheet.cells.get(3, 0).value = 4;
            worksheet.cells.get(4, 0).value = 5;
            worksheet.cells.get(5, 0).value = 6;
            worksheet.cells.get(0, 1).value = 7;
            worksheet.cells.get(1, 1).value = 8;
            worksheet.cells.get(2, 1).value = 9;
            worksheet.cells.get(3, 1).value = 10;
            worksheet.cells.get(4, 1).value = 11;
            worksheet.cells.get(5, 1).value = 12;

            // Configure ODS page background (converted getters/setters to properties)
            const background = worksheet.pageSetup.odsPageBackground;
            background.color = AsposeCells.Color.Azure;
            background.type = AsposeCells.OdsPageBackgroundType.Color;

            // Save the workbook as ODS and provide download link
            const outputData = workbook.save(SaveFormat.Ods);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ColoredBackground.ods';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download ColoredBackground.ods';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **向ODS文件添加图形背景**  

Aspose.Cells for Java脚本通过C++提供[**OdsPageBackground**](https://reference.aspose.com/cells/javascript-cpp/odspagebackground)类以管理ODS文件中的背景。下方代码示例演示了如何使用[**OdsPageBackground.graphicData**](https://reference.aspose.com/cells/javascript-cpp/odspagebackground/#graphicData--)属性为ODS文件添加图形背景。请查看由代码生成的[输出ODS](90112030.ods)文件以供参考。  

### **示例代码**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Graphic Background Example</h1>
        <p>Select a background image to embed into a new workbook as an ODS page background.</p>
        <input type="file" id="imageInput" accept="image/*" />
        <button id="runExample">Create Workbook with Graphic Background</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, OdsPageBackgroundType, OdsPageBackgroundGraphicType } = AsposeCells;

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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');
            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select a background image file.</p>';
                return;
            }

            // Read selected image file
            const file = imageInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const imageBytes = new Uint8Array(arrayBuffer);

            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Populate some cells
            worksheet.cells.get(0, 0).value = 1;
            worksheet.cells.get(1, 0).value = 2;
            worksheet.cells.get(2, 0).value = 3;
            worksheet.cells.get(3, 0).value = 4;
            worksheet.cells.get(4, 0).value = 5;
            worksheet.cells.get(5, 0).value = 6;
            worksheet.cells.get(0, 1).value = 7;
            worksheet.cells.get(1, 1).value = 8;
            worksheet.cells.get(2, 1).value = 9;
            worksheet.cells.get(3, 1).value = 10;
            worksheet.cells.get(4, 1).value = 11;
            worksheet.cells.get(5, 1).value = 12;

            // Access ODS page background via pageSetup property
            const background = worksheet.pageSetup.oDSPageBackground;
            background.type = OdsPageBackgroundType.Graphic;
            background.graphicData = imageBytes;
            background.graphicType = OdsPageBackgroundGraphicType.Area;

            // Save the workbook as ODS and provide download link
            const outputData = workbook.save(SaveFormat.Ods);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'GraphicBackground.ods';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download ODS File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the ODS file.</p>';
        });
    </script>
</html>
```
