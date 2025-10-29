---
title: 对齐设置
linktitle: 对齐设置
description: 在Aspose.Cells库中，你可以使用单元格对齐设置，通过JavaScript via C++调整文本的布局和显示。本文提供了详细的步骤和示例代码，帮助你使用Aspose.Cells进行单元格对齐设置。
keywords: Aspose.Cells，单元格对齐，水平对齐，垂直对齐，文本换行JavaScript via C++
type: docs
weight: 20
url: /zh/javascript-cpp/cells-alignment-settings/
---

## **配置对齐设置**

### **Microsoft Excel中的对齐设置**

任何使用Microsoft Excel格式化单元格的人都会熟悉Microsoft Excel中的对齐设置。

从上面的图中可以看出，有不同种类的对齐选项：

- 文本对齐(水平和垂直)
- 缩进
- 方向
- 文本控制
- 文本方向

Aspose.Cells完全支持所有这些对齐设置，并在下面详细讨论。

### **Aspose.Cells中的对齐设置**

Aspose.Cells 提供了一个类 [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)，代表一个 Excel 文件。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) 类包含一个 [**Worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) 集合，可以访问 Excel 文件中的每一个工作表。一个工作表由 [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 类提供了一个 [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) 集合。[**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) 集合中的每个项目代表一个 [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) 类的对象。

Aspose.Cells 提供 [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) 和 [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-) 方法，用于 [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) 类中获取和设置单元格的格式。[**Style**](https://reference.aspose.com/cells/javascript-cpp/style) 类提供了有用的属性，用于配置对齐设置。

使用 [**TextAlignmentType**](https://reference.aspose.com/cells/javascript-cpp/textalignmenttype) 枚举选择任何文本对齐类型。[**TextAlignmentType**](https://reference.aspose.com/cells/javascript-cpp/textalignmenttype) 枚举中预定义的文本对齐类型包括：

|**文本对齐类型**|**描述**|
| :- | :- |
|Bottom|表示底部文本对齐
|Center|表示居中文本对齐
|CenterAcross|表示跨列居中文本对齐
|Distributed|表示分散文本对齐
|Fill|表示填充文本对齐
|General|表示常规文本对齐
|Justify|表示两端对齐文本对齐
|Left|表示左对齐文本对齐
|Right|表示右对齐文本对齐
|Top|表示顶部文本对齐|
|JustifiedLow|用于阿拉伯文本具有调整的卡什达长度。|
|ThaiDistributed|分布泰文，因为每个字符被视为一个单词。|

{{% alert color="primary" %}}

您也可以使用 [**Style.isJustifyDistributed(boolean)**](https://reference.aspose.com/cells/javascript-cpp/style/#isJustifyDistributed-boolean-) 方法应用分散对齐设置。

{{% /alert %}}

#### **水平对齐**

使用 [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) 对象的 [**horizontalAlignment**](https://reference.aspose.com/cells/javascript-cpp/style/#horizontalAlignment-textalignmenttype-) 方法水平对齐文本。

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

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the worksheet
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.putValue("Visit Aspose!");

            // Setting the horizontal alignment of the text in the "A1" cell
            const style = cell.style;
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```



#### **垂直对齐**

与水平对齐类似，使用 [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) 对象的 [**verticalAlignment**](https://reference.aspose.com/cells/javascript-cpp/style/#verticalAlignment-textalignmenttype-) 方法垂直对齐文本。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Create Workbook Example</h1>
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
            // Instantiate a Workbook object
            const workbook = new Workbook();

            // Clearing all the worksheets
            workbook.worksheets.clear();

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Setting the horizontal/vertical alignment of the text in the "A1" cell via style
            const style = cell.style;
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```


#### **缩进**

可以通过 [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) 对象的 [**indentLevel**](https://reference.aspose.com/cells/javascript-cpp/style/#indentLevel-number-) 方法设置单元格中文本的缩进级别。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Set Cell Indent Level Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

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

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Setting the horizontal alignment of the text in the "A1" cell
            const style = cell.style;

            // Setting the indentation level of the text (inside the cell) to 2
            style.indentLevel = 2;

            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
    </body>
</html>
```



#### **方向**

通过 [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) 对象的 [**rotationAngle**](https://reference.aspose.com/cells/javascript-cpp/style/#rotationAngle-number-) 方法设置单元格中文本的方向（旋转）。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Modify Cell</h1>
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
            // This example creates a new workbook, updates A1, sets rotation, and saves the file.
            const fileInput = document.getElementById('fileInput');

            // Instantiate a new Workbook (blank)
            const workbook = new Workbook();

            // Obtain reference to the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Getting the style of the cell
            const style = cell.style;

            // Setting the rotation of the text (inside the cell) to 25
            style.rotationAngle = 25;

            // Assign the modified style back to the cell
            cell.style = style;

            // Save the Excel file in Excel 97-2003 format and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and modified successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

#### **文本控制**

以下部分讨论了如何通过设置文本换行、缩小以适应和其他格式设置选项来控制文本。

##### **自动换行文本**

在单元格中换行文本可以更容易阅读：单元格的高度会调整以适应全部文本，而不是裁剪或溢出到相邻的单元格。通过 [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) 对象的 [**isTextWrapped(boolean)**](https://reference.aspose.com/cells/javascript-cpp/style/#isTextWrapped-boolean-) 方法开启或关闭文本换行。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Wrapping Text Example</title>
    </head>
    <body>
        <h1>Wrapping Text Example</h1>
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

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Open first Worksheet in the workbook
            const ws = workbook.worksheets.get(0);

            // Get Worksheet Cells Collection
            const cells = ws.cells;

            // Increase the width of First Column Width
            cells.columns.get(0).width = 35;

            // Increase the height of first row
            cells.rows.get(0).height = 36;

            // Add Text to the First Cell
            const cellRef = cells.checkCell(0, 0);
            cellRef.value = "I am using the latest version of Aspose.Cells to test this functionality";

            // Make Cell's Text wrap
            const style = cellRef.style;
            style.isTextWrapped = true;
            cellRef.style = style;

            // Save Excel File
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'WrappingText.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **缩小以适应**

一种字段中换行文本的选项是缩小文本大小以适应单元格尺寸。这通过将 [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) 对象的 [**shrinkToFit(boolean)**](https://reference.aspose.com/cells/javascript-cpp/style/#shrinkToFit-boolean-) 方法设置为 **true** 实现。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Cell Style Example</title>
    </head>
    <body>
        <h1>Set Cell Style Example</h1>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Obtain the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Getting the style of the cell
            const style = cell.style;

            // Shrinking the text to fit according to the dimensions of the cell
            style.shrinkToFit = true;

            // Applying the style back to the cell
            cell.style = style;

            // Saving the Excel file in Excel97To2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and styled successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```


##### **合并单元格**

像 Microsoft Excel 一样，Aspose.Cells 支持将多个单元格合并为一个。Aspose.Cells 提供两种方法，一种是调用 [**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) 集合的 [**merge**](https://reference.aspose.com/cells/javascript-cpp/cells/#merge-number-number-number-number-) 方法。[**merge**](https://reference.aspose.com/cells/javascript-cpp/cells/#merge-number-number-number-number-) 方法需要以下参数来合并单元格：

- 第一行：开始合并的第一行。
- 第一列：开始合并的第一列。
- 行数：要合并的行数。
- 列数：要合并的列数。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Merge Cells and Style Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Create a Workbook.
            const wbk = new Workbook(new Uint8Array(arrayBuffer));

            // Create a Worksheet and get the first sheet.
            const worksheet = wbk.worksheets.get(0);

            // Create a Cells object to fetch all the cells.
            const cells = worksheet.cells;

            // Merge some Cells (C6:E7) into a single C6 Cell.
            cells.merge(5, 2, 2, 3);

            // Input data into C6 Cell.
            const cell = cells.get(5, 2);
            cell.value = "This is my value";

            // Create a Style object to fetch the Style of C6 Cell.
            const style = cell.style;

            // Create a Font object
            const font = style.font;

            // Set the name.
            font.name = "Times New Roman";

            // Set the font size.
            font.size = 18;

            // Set the font color
            font.color = AsposeCells.Color.Blue;

            // Bold the text
            font.isBold = true;

            // Make it italic
            font.isItalic = true;

            // Set the background color of C6 Cell to Red
            style.foregroundColor = AsposeCells.Color.Red;
            style.pattern = AsposeCells.BackgroundType.Solid;

            // Apply the Style to C6 Cell.
            cell.style = style;

            // Save the Workbook.
            const outputData = wbk.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'mergingcells.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


另一种方法是首先调用 [**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) 集合的 [**createRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-) 方法创建要合并的单元格范围。[**createRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-) 方法接受与上面讨论的 [**merge**](https://reference.aspose.com/cells/javascript-cpp/cells/#merge-number-number-number-number-) 方法相同的参数集，并返回一个 [**Range**](https://reference.aspose.com/cells/javascript-cpp/range) 对象。[**Range**](https://reference.aspose.com/cells/javascript-cpp/range) 对象还提供一个 [**merge**](https://reference.aspose.com/cells/javascript-cpp/range/#merge--) 方法，将指定范围中的单元格范围合并。

##### **文本方向**

可以设置单元格中文本的阅读顺序。阅读顺序是以字符、单词等显示的视觉顺序。例如，英语是从左到右的语言，而阿拉伯语是从右到左的语言。

读取顺序由 [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) 对象的 [**textDirection**](https://reference.aspose.com/cells/javascript-cpp/style/#textDirection-textdirectiontype-) 属性设置。Aspose.Cells 在 [**TextDirectionType**](https://reference.aspose.com/cells/javascript-cpp/textdirectiontype) 枚举中预定义了文本方向类型。

|**文本方向类型**|**描述**|
| :- | :- |
|Context|与第一个输入字符的语言一致的阅读顺序
|LeftToRight|从左到右的阅读顺序
|RightToLeft|从右到左的阅读顺序

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Modify A1 and Save</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TextDirectionType } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Obtaining the reference of first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "I am using the latest version of Aspose.Cells to test this functionality.";

            // Gets style in the "A1" cell
            const style = cell.style;

            // Shrinking the text to fit according to the dimensions of the cell
            style.textDirection = TextDirectionType.LeftToRight;

            // Apply the style back to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## **高级主题**
- [更改单元格对齐方式并保留现有格式](/cells/zh/javascript-cpp/change-cells-alignment-and-keep-existing-formatting/)
- [换行和文本换行](/cells/zh/javascript-cpp/line-breaks-and-text-wrapping/)
