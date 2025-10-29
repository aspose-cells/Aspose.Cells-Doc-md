---
title: 通过C++用JavaScript格式化单元格
description: 学习如何在Aspose.Cells for JavaScript via C++中格式化和样式化单元格，包括数字格式化、日期格式化、字体样式和其他单元格样式选项。我们的指南将帮助你创建漂亮且专业的电子表格。
keywords: Aspose.Cells for JavaScript通过C++，单元格格式化、样式、数字格式化、日期格式化、字体样式、单元格样式选项、电子表格、创建、专业外观、格式化行列。
linktitle: 格式单元格
type: docs
weight: 120
url: /zh/javascript-cpp/cells-formatting/
---

## **介绍**

{{% alert color="primary" %}}

Aspose.Cells提供[Cell](https://reference.aspose.com/cells/javascript-cpp/cell)类的[**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--)和[**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-)方法，用于获取/设置单元格的格式样式。Aspose.Cells还提供一个[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)类。

{{% /alert %}}

## **如何使用样式方法格式化单元格**

在单元格上应用不同种类的格式样式，设置背景或前景颜色、边框、字体、水平和垂直对齐、缩进级别、文本方向、旋转角度等。

### **如何使用样式方法**

如果开发人员需要对不同的单元格应用不同的格式，可以先用 [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) 方法获取单元格的 [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) ，指定样式属性，然后用 [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-) 方法应用格式。下面的示例演示了如何对一个单元格使用多种格式。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Styling Example</h1>
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

            // Instantiate or load workbook
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
            cell.value = "Hello Aspose!";

            // Defining a Style object
            let style;

            // Get the style from A1 cell
            style = cell.style;

            // Setting the vertical alignment
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the horizontal alignment
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the font color of the text
            style.font.color = AsposeCells.Color.Green;

            // Setting to shrink according to the text contained in it
            style.shrinkToFit = true;

            // Setting the bottom border color to red
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Red;

            // Setting the bottom border type to medium
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Medium;

            // Applying the style to A1 cell
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

### **如何使用样式对象为不同单元格设置格式**

如果开发人员需要对不同的单元格应用相同的样式，可以使用 [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) 对象。请按照以下步骤使用 [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) 对象：

1. 通过调用 [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) 类的 [**createStyle()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#createStyle--) 方法添加 [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) 对象
2. 访问新添加的 [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) 对象
3. 设置 [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) 对象的属性/特性以应用所需的格式
4. 将配置好的 [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) 对象赋值给目标单元格

这种方法可以极大地提高您的应用程序的效率，并节省内存。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Style Cells</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TextAlignmentType, Color, BorderType, CellBorderType } = AsposeCells;

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

            // Add a new worksheet to the workbook
            const i = workbook.worksheets.add();

            // Obtain the newly added worksheet by index
            const worksheet = workbook.worksheets.get(i);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Set value of A1
            cell.value = "Hello Aspose!";

            // Create a new style
            const style = workbook.createStyle();

            // Set vertical and horizontal alignment
            style.verticalAlignment = TextAlignmentType.Center;
            style.horizontalAlignment = TextAlignmentType.Center;

            // Set font color
            style.font.color = Color.Green;

            // Shrink to fit
            style.shrinkToFit = true;

            // Set bottom border color and style
            style.borders.get(BorderType.BottomBorder).color = Color.Red;
            style.borders.get(BorderType.BottomBorder).lineStyle = CellBorderType.Medium;

            // Apply style to A1
            cell.style = style;

            // Apply same style to B1, C1, D1
            worksheet.cells.get("B1").style = style;
            worksheet.cells.get("C1").style = style;
            worksheet.cells.get("D1").style = style;

            // Save workbook to XLS format and provide download link
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

### **如何使用Microsoft Excel 2007预定义样式**

如果您需要为Microsoft Excel 2007应用不同的格式样式，请使用Aspose.Cells API应用样式。下面的示例演示了如何使用这种方法在单元格上应用预定义样式。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Workbook and Set Cell Style Example</h1>
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
            // Instantiate a new Workbook.
            const workbook = new Workbook();

            // Create a style object.
            const style = workbook.createStyle();

            // Access the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Input a value to A1 cell.
            cell.putValue("Test");

            // Apply the style to the cell.
            cell.style = style;

            // Saving the Excel 2007 file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```



## **如何格式化单元格中的选定字符**

处理字体设置解释了如何格式化单元格中的文本，但它只解释了如何格式化所有单元格内容。如果您只想格式化选定的字符怎么办？

Aspose.Cells 也支持此功能。本文将说明如何有效使用此功能。

### **如何格式化选定的字符**

Aspose.Cells 提供了一个表示 Microsoft Excel 文件的类 [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)类包含一个 [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) 集合，可以访问Excel文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 类提供一个 [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) 集合。[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) 集合中的每个项目代表一个 [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) 类的对象。

[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) 类提供了 [**characters(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-number-number-) 方法，接受以下参数以选择单元格内部的字符范围：

- **起始索引**，选择开始的字符的索引。
- **字符数**，要选择的字符数。

[**characters(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-number-number-) 方法返回 [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting) 类的实例，允许开发者以与格式化单元格相同的方式格式化字符，示例如下。在输出文件中，单元格A1中的“Visit”将采用默认字体格式，“Aspose!”将加粗且为蓝色。

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
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first (default) worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Setting the font of selected characters to bold and color to blue
            const charRange = cell.characters(6, 7);
            charRange.font.isBold = true;
            charRange.font.color = AsposeCells.Color.Blue;

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

{{% alert color="primary" %}}

如果你对格式化单元格中的部分富文本感兴趣，可以考虑使用 {0} & {1} 方法。使用 {2} 方法访问文本部分，然后使用 {3} 方法进行修改，而 {4} 方法返回一个 {4} 对象数组，可以操控以设置字体名称、字体颜色、加粗等属性，使用 {5} 方法应用更改。

{{% /alert %}}

## **如何格式化行和列**

有时，开发人员需要在行或列上应用相同的格式。逐个单元格应用格式通常需要更长时间，不是一个好的解决方案。
为解决这个问题，Aspose.Cells提供了一个在本文中详细讨论的简单、快速的方法。

### **格式化行和列**

Aspose.Cells 提供一个代表 Microsoft Excel 文件的类 [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) 类包含一个 [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) 集合，可以访问Excel文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 类提供一个 [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) 集合。[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) 集合提供一个 [**rows**](https://reference.aspose.com/cells/javascript-cpp/cells/#rows--) 集合。

### **如何格式化一行**

[**rows**](https://reference.aspose.com/cells/javascript-cpp/cells/#rows--) 集合中的每个项代表一个 [**Row**](https://reference.aspose.com/cells/javascript-cpp/row) 对象。[**Row**](https://reference.aspose.com/cells/javascript-cpp/row) 对象提供用于设置行格式的 [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/row/#applyStyle-style-styleflag-) 方法。若要对一行应用相同的格式，可以使用 [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) 对象。以下步骤演示了如何使用它。

1. 通过调用 [**createStyle()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#createStyle--) 类的 [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) 方法，将 [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) 对象添加到 [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) 类中。
2. 设置 [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) 对象的属性以应用格式设置。
3. 将相关属性开启到 [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag) 对象。
4. 将配置好的 [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) 对象分配给 [**Row**](https://reference.aspose.com/cells/javascript-cpp/row) 对象。

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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Obtaining the reference of the first (default) worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Adding a new Style to the styles
            const style = workbook.createStyle();

            // Setting the vertical alignment of the text in the "A1" cell
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the horizontal alignment of the text in the "A1" cell
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the font color of the text in the "A1" cell
            style.font.color = AsposeCells.Color.Green;

            // Shrinking the text to fit in the cell
            style.shrinkToFit = true;

            // Setting the bottom border color of the cell to red
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Red;

            // Setting the bottom border type of the cell to medium
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Medium;

            // Creating StyleFlag
            const styleFlag = new AsposeCells.StyleFlag();
            styleFlag.horizontalAlignment = true;
            styleFlag.verticalAlignment = true;
            styleFlag.shrinkToFit = true;
            styleFlag.borders = true;
            styleFlag.fontColor = true;

            // Accessing a row from the Rows collection
            const row = worksheet.cells.rows.get(0);

            // Assigning the Style object to the Style property of the row
            row.applyStyle(style, styleFlag);

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
</html>
```

### **如何格式化一列**

[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) 集合还提供一个 [**columns**](https://reference.aspose.com/cells/javascript-cpp/cells/#columns--) 集合。每个项代表一个 [**Column**](https://reference.aspose.com/cells/javascript-cpp/column) 对象。类似于 [**Row**](https://reference.aspose.com/cells/javascript-cpp/row) 对象，[**Column**](https://reference.aspose.com/cells/javascript-cpp/column) 也提供 [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/row/#applyStyle-style-styleflag-) 方法用于格式化列。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Style and Column Apply Example</h1>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Obtain the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add a new Style to the styles
            const style = workbook.createStyle();

            // Set vertical and horizontal alignment
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;

            // Set font color
            style.font.color = AsposeCells.Color.Green;

            // Shrink to fit
            style.shrinkToFit = true;

            // Set bottom border color and style
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Red;
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Medium;

            // Create and configure StyleFlag
            const styleFlag = new AsposeCells.StyleFlag();
            styleFlag.horizontalAlignment = true;
            styleFlag.verticalAlignment = true;
            styleFlag.shrinkToFit = true;
            styleFlag.borders = true;
            styleFlag.fontColor = true;

            // Access first column and apply style
            const column = worksheet.cells.getColumns().get(0);
            column.applyStyle(style, styleFlag);

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Style applied to column successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **高级主题**
- [对齐设置](/cells/zh/javascript-cpp/cells-alignment-settings/)
- [边框设置](/cells/zh/javascript-cpp/cells-border-settings/)
- [设置Excel和ODS文件的条件格式。](/cells/zh/javascript-cpp/conditional-formatting/)
- [Excel 主题和颜色](/cells/zh/javascript-cpp/excel-themes-and-colors/)
- [填充设置](/cells/zh/javascript-cpp/cells-fill-settings/)
- [字体设置](/cells/zh/javascript-cpp/cells-font-settings/)
- [在工作簿中格式化工作表单元格](/cells/zh/javascript-cpp/format-worksheet-cells-in-a-workbook/)
- [实现1904日期系统](/cells/zh/javascript-cpp/implement-1904-date-system/)
- [合并和取消合并单元格](/cells/zh/javascript-cpp/merging-and-unmerging-cells/)
- [数字设置](/cells/zh/javascript-cpp/cells-number-settings/)
- [获取和设置单元格的样式](/cells/zh/javascript-cpp/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)
