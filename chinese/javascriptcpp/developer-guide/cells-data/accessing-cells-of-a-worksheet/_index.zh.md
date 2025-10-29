---
title: 访问工作表的单元格
type: docs
weight: 10
url: /zh/javascript-cpp/accessing-cells-of-a-worksheet/
description: 本文介绍了如何使用Aspose.Cells for JavaScript通过C++ API获取工作表的最大显示范围并访问单元格。
keywords: 获取单元格对象，访问单元格，获取工作表的最大显示范围。 
---

{{% alert color="primary" %}}

我们知道，所有工作表可能包含基本存储在单元格中的数据（由此构成一个工作表）。单元格是工作表的基本部分，用于构建整个工作表，作为行和列的序列。在尝试访问工作表中的数据之前，我们需要访问其单元格。因此，在本主题中，我们将讨论一些基本方法，以便在运行时使用Aspose.Cells for JavaScript通过C++访问工作表单元格。

{{% /alert %}}

## **如何访问单元格**

Aspose.Cells for JavaScript通过C++提供了一个类，[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)，它代表一个Excel文件。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)类包含一个[**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection)，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)类提供了一个[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)集合，代表工作表中的所有单元格。

我们可以使用[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)集合来访问工作表中的单元格。Aspose.Cells for JavaScript通过C++提供了三种基本方法来访问工作表中的单元格：

1. 使用单元格名称。
1. 使用单元格的行和列索引。
1. 使用[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)集合中的单元格索引

 我们已经提到第3种方法是最快的，第1种方法是最慢的。三种方法之间的性能差异非常小，因此无论您使用哪种方法，都不用担心性能降级。

### **如何通过单元格名称获取单元格对象**

开发者可以通过将单元格名称作为索引传递给[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)集合中的[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)类，访问任何特定的单元格。

如果一开始创建一个空白工作表，则[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)集合的计数为零。当您使用此方法访问单元格时，它会检查该单元格是否存在于集合中。如果存在，它会返回集合中的单元格对象，否则，它会创建一个新的[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)对象，将该对象添加到[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)集合中，然后返回该对象。这种方法是如果你熟悉Microsoft Excel，访问单元格最容易的方法，但与其他方法相比速度较慢。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Read Cell Example</h1>
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

            // Using the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its name
            const cell = worksheet.cells.get("A1");

            // Output the cell's string value to the page
            document.getElementById('result').innerHTML = `<p>Cell A1 value: ${cell.stringValue}</p>`;
        });
    </script>
</html>
```

### **如何通过单元格的行和列索引获取单元格对象**

开发者可以通过将单元格的行和列索引传递给[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)集合中的[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)类，访问任何特定的单元格。

这种方法的工作方式与第一种方法相同。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read Cell Value</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Using the first worksheet in workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its row and column (A1 -> 0,0)
            const cell = worksheet.cells.get(0, 0);

            // Printing the string value of the cell
            const value = cell.stringValue;
            console.log(value);
            resultDiv.innerHTML = `<p>Cell A1 value: ${value}</p>`;
        });
    </script>
</html>
```

### **如何通过单元格索引在单元格集合中获取单元格对象**

还可以通过将单元格的数字索引传递给[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)集合来访问单元格。

如果你使用此方法访问单元格，如果单元格的数字索引超出范围，可能会抛出异常。这是最快的访问单元格的方法，但需要注意的是，如果你用此方法访问单元格对象，添加新单元格后，数字索引可能会发生变化。[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)集合中的单元格对象会根据行和列索引内部排序。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read Cell String Value</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Using the Sheet 1 in Workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its row and column.
            const cell = worksheet.cells.get(0, 0);

            // Output the string value of the cell
            console.log(cell.stringValue);
            resultDiv.innerHTML = `<p>Cell (0,0) string value: <strong>${cell.stringValue}</strong></p>`;
        });
    </script>
</html>
```

## **如何获取工作表的最大显示范围**

Aspose.Cells for JavaScript通过C++允许开发者访问工作表的最大显示范围。最大显示范围 - 即第一和最后一个有内容的单元格之间的范围 - 在需要复制、选择或在图片中显示工作表全部内容时非常有用。

可以使用[**Cells.maxDisplayRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDisplayRange--)访问工作表的最大显示范围。以下示例代码演示了如何访问[**maxDisplayRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDisplayRange--)属性。

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

            // Ensure Aspose.Cells is initialized
            await AsposeCells.onReady();

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Access the Maximum Display Range
            const range = worksheet.cells.maxDisplayRange;

            // Print / display the Maximum Display Range RefersTo property
            const refersTo = range.refersTo;
            resultDiv.innerHTML = `<p style="color: green;">Maximum Display Range: ${refersTo}</p>`;
        });
    </script>
</html>
```
