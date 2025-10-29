---
title: 使用JavaScript通过C++管理图片
linktitle: 管理图片
type: docs
weight: 10
url: /zh/javascript-cpp/managing-pictures/
description: 学习如何使用Aspose.Cells for JavaScript via C++在电子表格中添加和定位图片。
---

Aspose.Cells允许开发人员在运行时向电子表格添加图片。此外，可以在运行时控制这些图片的定位，更多细节将在接下来的章节中讨论。

本文说明了如何添加图片以及如何插入显示某些单元格内容的图片。

## **添加图片**

向电子表格中添加图片非常简单。只需几行代码：  
只需调用[**Add**](https://reference.aspose.com/cells/javascript-cpp/picturecollection/#add-number-number-string-)方法（封装在[**Pictures**](https://reference.aspose.com/cells/javascript-cpp/picturecollection)对象中）即可。[**Add**](https://reference.aspose.com/cells/javascript-cpp/picturecollection/#add-number-number-string-)方法接受以下参数：

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
        <p>Select an optional Excel file to update (or leave empty to create a new workbook), and select an image file to insert as a picture.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <input type="file" id="imageInput" accept="image/*" />
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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file to insert.</p>';
                return;
            }

            // Load existing workbook if provided, otherwise create a new one
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Read image file bytes
            const imageFile = imageInput.files[0];
            const imageArrayBuffer = await imageFile.arrayBuffer();
            const imageBytes = new Uint8Array(imageArrayBuffer);

            // Adding a picture at the location of a cell whose row and column indices are 5 (F6)
            worksheet.pictures.add(5, 5, imageBytes);

            // Saving the Excel file (Excel 97-2003 .xls format)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Picture added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **定位图片**

使用Aspose.Cells控制图片定位有两种可能的方法：

- 比例定位：定义相对于行高和列宽的位置。
- 绝对定位：定义图像插入页面的确切位置，例如距离单元格边缘左侧40像素，下面20像素。

### **比例定位**

开发者可以使用[**upperDeltaX**](https://reference.aspose.com/cells/javascript-cpp/shape/#upperDeltaX--)和[**upperDeltaY**](https://reference.aspose.com/cells/javascript-cpp/shape/#upperDeltaY--)属性通过[**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture/)对象将图片按比例定位到行高和列宽。通过传递其图片索引，您可以从[**Pictures**](https://reference.aspose.com/cells/javascript-cpp/picturecollection)集合中获取[**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture/)对象。此示例在F6单元格放置一张图片。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Add Picture to New Workbook</h1>
        <p>Select an image to insert into a new Excel workbook. The picture will be placed at cell F6 (row 5, column 5).</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <br/><br/>
        <label for="imageInput">Select image to insert:</label>
        <input type="file" id="imageInput" accept="image/*" />
        <br/><br/>
        <button id="runExample">Create Workbook and Add Picture</button>
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
            if (!imageInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an image file to insert.</p>';
                return;
            }

            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Add a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtain the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Read the selected image file as bytes
            const imageFile = imageInput.files[0];
            const arrayBuffer = await imageFile.arrayBuffer();
            const imageBytes = new Uint8Array(arrayBuffer);

            // Adding a picture at the location of a cell whose row and column indices are 5 (F6)
            const pictureIndex = worksheet.pictures.add(5, 5, imageBytes);

            // Accessing the newly added picture
            const picture = worksheet.pictures.get(pictureIndex);

            // Positioning the picture proportional to row height and column width (property assignments)
            picture.upperDeltaX = 200;
            picture.upperDeltaY = 200;

            // Saving the Excel file (Excel 97-2003 format)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and picture added successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **绝对定位**

开发者也可以使用[**left**](https://reference.aspose.com/cells/javascript-cpp/shape/#left--)和[**top**](https://reference.aspose.com/cells/javascript-cpp/shape/#top--)属性通过[**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture/)对象绝对定位图片。此示例在F6单元格放置一张图片，距离左侧60像素，距离顶部10像素。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Picture</title>
    </head>
    <body>
        <h1>Add Picture to Workbook Example</h1>
        <p>Select an image file to insert into a new Excel workbook:</p>
        <input type="file" id="fileInput" accept="image/*" />
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
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file.</p>';
                return;
            }

            // Read image file as bytes
            const imageFile = fileInput.files[0];
            const arrayBuffer = await imageFile.arrayBuffer();
            const imageBytes = new Uint8Array(arrayBuffer);

            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a picture at the location of a cell whose row and column indices are 5 in the worksheet ("F6")
            const pictureIndex = worksheet.pictures.add(5, 5, imageBytes);

            // Accessing the newly added picture
            const picture = worksheet.pictures.get(pictureIndex);

            // Absolute positioning of the picture in unit of pixels
            picture.left = 60;
            picture.top = 10;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Picture added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **基于单元格引用插入图片**

Aspose.Cells允许您在图像形状中显示工作表单元格的内容。您可以将图片链接到包含您要显示数据的单元格。由于单元格或单元格范围与图形对象链接，因此您对该单元格或单元格范围中的数据所做的更改将自动显示在图形对象中。

通过调用[**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-)方法（封装在[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)对象中）并指定[**formula**](https://reference.aspose.com/cells/javascript-cpp/picture/#formula--)属性的单元格范围，将图片添加到工作表。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
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
            // This example creates a new workbook, modifies cells and pictures, and saves it.
            const workbook = new Workbook();

            // Get the first worksheet's cells collection
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;

            // Add string values to the cells
            cells.get("A1").value = "A1";
            cells.get("C10").value = "C10";

            // Get pictures collection and add a blank picture to the D1 cell
            const picts = worksheet.pictures;
            const picIndex = picts.add(0, 3, 10, 6, null);
            const pic = picts.get(picIndex);

            // Specify the formula that refers to the source range of cells
            pic.formula = "A1:C10";

            // Update the shapes selected value in the worksheet
            worksheet.shapes.updateSelectedValue();

            // Save the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **高级主题**
- [使用单元格文本添加条件图标集](/cells/zh/javascript-cpp/add-conditional-icons-set-with-the-cell-text/)
- [从网址插入链接图片](/cells/zh/javascript-cpp/insert-a-linked-picture-from-web-address/)
- [基于单元格引用插入图片](/cells/zh/javascript-cpp/insert-a-picture-based-on-cell-reference/)
- [从URL中加载Web图像到Excel工作表](/cells/zh/javascript-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)
