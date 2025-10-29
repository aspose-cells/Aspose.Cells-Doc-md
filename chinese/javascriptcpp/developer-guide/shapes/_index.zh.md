---
title: 用JavaScript通过C++插入Excel文件的图片和形状  
linktitle: 形状  
type: docs  
weight: 140  
url: /zh/javascript-cpp/insert-shapes/  
description: 使用Aspose.Cells for Java脚本通过C++管理Excel文件中的图片、OLE对象和形状。  
---  

{{% alert color="primary" %}}  
有时你需要在工作表中插入一些必要的形状。你可能需要在不同位置插入相同的形状，或者批量插入多个形状。  
不用担心！[Aspose.Cells](https://products.aspose.com/cells/)支持所有这些操作。  
{{% /alert %}}  

Excel中的形状主要分为以下几类：  
- **图片**  
- **Ole对象**  
- **线条**  
- **矩形**  
- **基本形状**  
- **方块箭头**  
- **方程式形状**  
- **流程图**  
- **星星和横幅**  
- **标注**  

本指南将从每个类别中选择一两个形状作为示例。通过这些例子，你将学习如何使用[Aspose.Cells](https://products.aspose.com/cells/)将指定形状插入到工作表中。  

## **用JavaScript在Excel工作表中添加图片**  

向电子表格中添加图片非常简单。只需几行代码：  
只需调用[**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/picturecollection/#add-number-number-number-number-uint8array-)方法（封装在[**Pictures**](https://reference.aspose.com/cells/javascript-cpp/picturecollection)对象中）即可。[**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/picturecollection/#add-number-number-number-number-uint8array-)方法接受以下参数：  

- **左上角行索引**，左上角行的索引。  
- **左上角列索引**，左上角列的索引。  
- **图像文件名**，图像文件的名称，包括完整路径。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Picture to Workbook Example</h1>
        <p>
            Optional: select an existing Excel file to modify, or leave empty to create a new workbook.
        </p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <p>
            Select an image to insert into the worksheet (required):
        </p>
        <input type="file" id="imageInput" accept="image/*" />
        <br/><br/>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file to insert.</p>';
                return;
            }

            // If an Excel file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const excelFile = fileInput.files[0];
                const arrayBuffer = await excelFile.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Add a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtain the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Read the selected image file as Uint8Array
            const imageFile = imageInput.files[0];
            const imageArrayBuffer = await imageFile.arrayBuffer();
            const imageBytes = new Uint8Array(imageArrayBuffer);

            // Adding a picture at the location of a cell whose row and column indices are 5 (F6)
            worksheet.pictures.add(5, 5, imageBytes);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Resulting Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Picture inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **用JavaScript在Excel工作表中插入OLE对象**  

Aspose.Cells支持在工作表中添加、提取和操作OLE对象。因此，Aspose.Cells具有[**OleObjectCollection**](https://reference.aspose.com/cells/javascript-cpp/oleobjectcollection)类，用于向集合列表中添加新的OLE对象。另一个类，[**OleObject**](https://reference.aspose.com/cells/javascript-cpp/oleobject)，表示OLE对象。它具有一些重要成员：  

- [**OleObject.imageData**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#imageData--)属性指定图像（图标）的字节数组数据。图像将显示在工作表中，用于展示OLE对象。  
- [**OleObject.objectData**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#objectData--)属性指定对象的数据，形式为字节数组。当双击OLE对象图标时，将在相关程序中显示这些数据。  

下面的示例演示了如何将一个或多个OLE对象添加到工作表中。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Insert OLE Object Example</h1>
        <p>
            Select an image to display as the OLE object's icon and an Excel file to embed as the OLE object.
        </p>
        <input type="file" id="imageInput" accept="image/*" />
        <input type="file" id="excelInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            const excelInput = document.getElementById('excelInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file for the OLE icon.</p>';
                return;
            }
            if (!excelInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file to embed.</p>';
                return;
            }

            const imageFile = imageInput.files[0];
            const excelFile = excelInput.files[0];

            // Read files as ArrayBuffers
            const imageArrayBuffer = await imageFile.arrayBuffer();
            const excelArrayBuffer = await excelFile.arrayBuffer();

            // Convert to Uint8Array for Aspose.Cells
            const imageData = new Uint8Array(imageArrayBuffer);
            const objectData = new Uint8Array(excelArrayBuffer);

            // Instantiate a new Workbook.
            const workbook = new Workbook();

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Add an Ole object into the worksheet with the image shown in MS Excel.
            sheet.oleObjects.add(14, 3, 200, 220, imageData);

            // Set embedded ole object data.
            sheet.oleObjects.get(0).objectData = objectData;

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: 'application/vnd.ms-excel' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">OLE object embedded successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **用JavaScript在Excel工作表中插入直线**  

线条的形状属于**线条**类别。  

*  

- 选择要插入线条的单元格  
- 点击“插入”菜单，然后点击“形状”  
- 然后，从“最近使用的形状”或“线条”中选择线条  

![](line.png)  

***使用Aspose.Cells***  

您可以使用以下方法在工作表中插入线条。  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
该方法返回一个 [LineShape](https://reference.aspose.com/cells/javascript-cpp/lineshape) 对象。  
{{% /alert %}}  

以下示例展示了如何在工作表中插入线条。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Add Line Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            document.getElementById('runExample').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                if (!fileInput.files.length) {
                    document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                // Create workbook from uploaded file
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Access first worksheet from the collection
                const sheet = workbook.worksheets.get(0);

                // Add the line to the worksheet
                sheet.shapes.addLine(2, 0, 2, 0, 100, 300);

                // Save workbook to XLSX format and create download link
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'sample.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Line added successfully! Click the download link to get the modified file.</p>';
            });
        });
    </script>
</html>
```  

执行上述代码，您将获得以下结果：  

![](line2.png)  

## **用JavaScript在Excel工作表中插入箭头线**  

箭头线条的形状属于**线条**类别。它是线条的一种特殊情况。  

*  

- 选择要插入箭头线的单元格  
- 点击“插入”菜单，然后点击“形状”  
- 然后，从“最近使用的形状”或“线条”选择箭头线条  

![](line_arrow1.png)  

***使用Aspose.Cells***  

您可以使用以下方法在工作表中插入箭头线。  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
该方法返回一个 [LineShape](https://reference.aspose.com/cells/javascript-cpp/lineshape) 对象。  
{{% /alert %}}  

以下示例展示了如何在工作表中插入箭头线条。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Line Arrow Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Loads the workbook which contains shapes
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the line arrow to the worksheet
            let s = sheet.shapes.addLine(2, 0, 2, 0, 100, 300); // method 1
            // let s = sheet.shapes.addAutoShape(AsposeCells.AutoShapeType.Line, 2, 0, 2, 0, 100, 300); // method 2
            // let s = sheet.shapes.addShape(AsposeCells.MsoDrawingType.Line, 2, 0, 2, 0, 100, 300); // method 3

            // add a arrow at the line begin
            s.line.beginArrowheadStyle = AsposeCells.MsoArrowheadStyle.Arrow; // arrow type
            s.line.beginArrowheadWidth = AsposeCells.MsoArrowheadWidth.Wide; // arrow width
            s.line.beginArrowheadLength = AsposeCells.MsoArrowheadLength.Short; // arrow length

            // add a arrow at the line end
            s.line.endArrowheadStyle = AsposeCells.MsoArrowheadStyle.ArrowOpen; // arrow type
            s.line.endArrowheadWidth = AsposeCells.MsoArrowheadWidth.Narrow; // arrow width
            s.line.endArrowheadLength = AsposeCells.MsoArrowheadLength.Long; // arrow length

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.with_arrow.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File with Arrow';

            document.getElementById('result').innerHTML = '<p style="color: green;">Arrow added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

执行上述代码，您将获得以下结果：  

![](line_arrow2.png)  

## **用JavaScript在Excel工作表中插入矩形**  

矩形的形状属于**矩形**类别。  

*  

- 选择要插入矩形的单元格  
- 点击“插入”菜单，然后点击“形状”  
- 然后，从“最近使用的形状”或“矩形”中选择矩形  

![](rectangle.png)  

***使用Aspose.Cells***  

您可以使用以下方法在工作表中插入矩形。  

{{% alert color="primary" %}}  
[**ShapeCollection.addRectangle(number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addRectangle-number-number-number-number-number-number-)  
该方法返回一个 [RectangleShape](https://reference.aspose.com/cells/javascript-cpp/rectangleshape) 对象。  
{{% /alert %}}  

以下示例展示了如何在工作表中插入矩形。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Rectangle</title>
    </head>
    <body>
        <h1>Add Rectangle to Worksheet</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Create workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the rectangle to the worksheet
            sheet.shapes.addRectangle(2, 0, 2, 0, 100, 300);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Rectangle added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

执行上述代码，您将获得以下结果：  

![](rectangle2.png)  

## **用JavaScript在Excel工作表中插入立方体**  

立方体的形状属于**基本形状**类别。  

*  

- 选择要插入立方体的单元格  
- 点击“插入”菜单，然后点击“形状”  
- 然后，从“基本形状”中选择立方体  

![](cube.png)  

***使用Aspose.Cells***  

您可以使用以下方法在工作表中插入立方体。  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
该方法返回一个 [Shape](https://reference.aspose.com/cells/javascript-cpp/shape) 对象。  
{{% /alert %}}  

以下示例展示了如何在工作表中插入立方体。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Cube</title>
    </head>
    <body>
        <h1>Add Cube to Worksheet</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the cube to the worksheet
            sheet.shapes.addAutoShape(AsposeCells.AutoShapeType.Cube, 2, 0, 2, 0, 100, 300);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            result.innerHTML = '<p style="color: green;">Cube added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

执行上述代码，您将获得以下结果：  

![](cube2.png)  

## **用JavaScript在Excel工作表中插入标注箭头**  

呼出四边形箭头的形状属于**块箭头**类别。  

*  

- 选择要插入标注四箭头的单元格  
- 点击“插入”菜单，然后点击“形状”  
- 然后，从“块箭头”中选择呼出四边形箭头  

![](callout_quad_arrow.png)  

***使用Aspose.Cells***  

您可以使用以下方法在工作表中插入标注四箭头  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
该方法返回一个 [Shape](https://reference.aspose.com/cells/javascript-cpp/shape) 对象。  
{{% /alert %}}  

以下示例展示如何向工作表插入调用箭头。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Callout Quad Arrow</title>
    </head>
    <body>
        <h1>Add Callout Quad Arrow Shape</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            const sheet = workbook.worksheets.get(0);

            sheet.shapes.addAutoShape(AutoShapeType.QuadArrowCallout, 2, 0, 2, 0, 100, 100);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shape added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

执行上述代码，您将获得以下结果：  

![](callout_quad_arrow2.png)  

## **使用JavaScript在Excel工作表插入乘号**  

乘号的形状属于 **方程式形状** 类别。  

*  

- 选择要插入乘法符号的单元格  
- 点击“插入”菜单，然后点击“形状”  
- 然后，从 **方程式形状** 中选择乘号  

![](multiplication_sign.png)  

***使用Aspose.Cells***  

您可以使用以下方法在工作表中插入乘法符号  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
该方法返回一个 [Shape](https://reference.aspose.com/cells/javascript-cpp/shape) 对象。  
{{% /alert %}}  

以下示例展示如何向工作表插入乘号。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Multiply Sign</title>
    </head>
    <body>
        <h1>Add Multiplication Sign to Worksheet</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the multiplication sign to the worksheet
            sheet.shapes.addAutoShape(AsposeCells.AutoShapeType.MathMultiply, 2, 0, 2, 0, 100, 100);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Multiplication sign added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

执行上述代码，您将获得以下结果：  

![](multiplication_sign2.png)  

## **使用JavaScript向Excel工作表插入多文档**  

多文档的形状属于 **流程图** 类别。  

*  

- 选择要插入多文档的单元格  
- 点击“插入”菜单，然后点击“形状”  
- 然后，从 **流程图** 中选择多文档  

![](multidocument.png)  

***使用Aspose.Cells***  

您可以使用以下方法在工作表中插入多文档。  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
该方法返回一个 [Shape](https://reference.aspose.com/cells/javascript-cpp/shape) 对象。  
{{% /alert %}}  

以下示例展示如何向工作表插入多文档。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            // Create workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the multidocument to the worksheet
            sheet.shapes.addAutoShape(AutoShapeType.FlowChartMultidocument, 2, 0, 2, 0, 100, 100);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

执行上述代码，您将获得以下结果：  

![](multidocument2.png)  

## **使用JavaScript在Excel工作表插入五角星**  

五角星的形状属于 **星星和旗帜** 类别。  

*  

- 选择要插入五角星的单元格  
- 点击“插入”菜单，然后点击“形状”  
- 然后，从 **星星与旗帜** 中选择五角星  

![](star_5_points.png)  

***使用Aspose.Cells***  

您可以使用以下方法在工作表中插入五角星  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
该方法返回一个 [Shape](https://reference.aspose.com/cells/javascript-cpp/shape) 对象。  
{{% /alert %}}  

以下示例展示如何向工作表插入五角星。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Star Shape</title>
    </head>
    <body>
        <h1>Add Five-Pointed Star to Worksheet</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Add the Five-pointed star to the worksheet
            sheet.shapes.addAutoShape(AutoShapeType.Star5, 2, 0, 2, 0, 100, 100);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Star shape added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

执行上述代码，您将获得以下结果：  

![](star_5_points2.png)  

## **使用JavaScript在Excel工作表插入思维泡泡云彩**  

思维云泡泡的形状属于 **注释** 类别。  

*  

- 选择要插入思维气泡云的单元格  
- 点击“插入”菜单，然后点击“形状”  
- 然后，从 **注释** 中选择思维云泡泡  

![](thought_bubble_cloud.png)  

***使用Aspose.Cells***  

您可以使用以下方法在工作表中插入思维气泡云。  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
该方法返回一个 [Shape](https://reference.aspose.com/cells/javascript-cpp/shape) 对象。  
{{% /alert %}}  

以下示例展示如何向工作表插入思维云泡泡。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Cloud Callout Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the thought bubble cloud to the worksheet
            sheet.shapes.addAutoShape(AutoShapeType.CloudCallout, 2, 0, 2, 0, 100, 100);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Cloud callout added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

执行上述代码，您将获得以下结果：  

![](thought_bubble_cloud2.png)  

## **高级主题**  
- [改变形状的调整值](/cells/zh/javascript-cpp/change-adjustment-values-of-the-shape/)  
- [在工作表之间复制形状](/cells/zh/javascript-cpp/copy-shapes-between-worksheets/)  
- [非原始形状中的数据](/cells/zh/javascript-cpp/data-in-non-primitive-shape/)  
- [查找工作表内形状的绝对位置](/cells/zh/javascript-cpp/finding-absolute-position-of-shape-inside-the-worksheet/)  
- [从形状获取连接点](/cells/zh/javascript-cpp/get-connection-points-from-shape/)  
- [管理控件](/cells/zh/javascript-cpp/managing-controls/)  
- [向工作表添加图标](/cells/zh/javascript-cpp/insert-svg-to-excel/)  
- [管理OLE对象](/cells/zh/javascript-cpp/managing-ole-objects/)  
- [管理图片](/cells/zh/javascript-cpp/managing-pictures/)  
- [管理智能图形](/cells/zh/javascript-cpp/managing-smartart/)  
- [管理文本框](/cells/zh/javascript-cpp/managing-textbox-of-excel/)  
- [在工作表中添加艺术字水印](/cells/zh/javascript-cpp/add-wordart-watermark-to-worksheet/)  
- [刷新链接形状的值](/cells/zh/javascript-cpp/refresh-values-of-linked-shapes/)  
- [在工作表内发送形状到最前或最后](/cells/zh/javascript-cpp/send-shape-front-or-back-inside-the-worksheet/)  
- [管理形状选项](/cells/zh/javascript-cpp/managing-shape-options/)  
- [管理形状文本选项](/cells/zh/javascript-cpp/managing-shape-text-options/)  
- [Web扩展 - 办公室加载项](/cells/zh/javascript-cpp/web-extensions-office-add-ins/)
