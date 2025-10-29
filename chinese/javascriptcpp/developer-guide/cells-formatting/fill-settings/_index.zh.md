---
title: 填充设置
linktitle: 填充设置
description: 学习如何使用Aspose.Cells for JavaScript via C++自定义填充设置、背景和样式。
keywords: Aspose.Cells，单元格，填充设置，背景，样式，JavaScript via C++
type: docs
weight: 50
url: /zh/javascript-cpp/cells-fill-settings/
---

## **颜色和背景图案**

Microsoft Excel可以设置单元格的前景（轮廓）和背景（填充）颜色以及背景图案。

Aspose.Cells还以灵活的方式支持这些功能。在本主题中，我们将学习如何使用Aspose.Cells来使用这些功能。

### **设置颜色和背景图案**

Aspose.Cells 提供一个类 [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) 来表示一个 Microsoft Excel 文件。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) 类包含一个 [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) 集合，可访问 Excel 文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 类提供一个 [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) 集合。[**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) 集合中的每一项代表一个 [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) 类的对象。

[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)具有[**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--)属性，用于获取和设置单元格的格式。[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)类提供了设置单元格前景色和背景色的属性。Aspose.Cells提供了包含预定义背景图案类型的[**BackgroundType**](https://reference.aspose.com/cells/javascript-cpp/backgroundtype)枚举，具体如下。

|**背景图案**|**描述**|
| :- | :- |
|DiagonalCrosshatch|代表对角线交叉图案
|DiagonalStripe|代表对角线条纹图案
|Gray6|代表6.25%灰色图案
|Gray12|代表12.5%灰色图案
|Gray25|代表25%灰色图案
|Gray50|代表50%灰色图案
|Gray75|代表75%灰色图案
|HorizontalStripe|代表水平条纹图案
|None|代表无背景
|ReverseDiagonalStripe|代表反对角线条纹图案
|Solid|代表实线图案
|ThickDiagonalCrosshatch|代表粗对角线交叉图案
|ThinDiagonalCrosshatch|代表细对角线交叉图案
|ThinDiagonalStripe|代表细对角线条纹图案
|ThinHorizontalCrosshatch|代表细水平交叉图案
|ThinHorizontalStripe|代表细水平条纹图案
|ThinReverseDiagonalStripe|代表细反对角线条纹图案
|ThinVerticalStripe|代表细竖条纹图案|
|VerticalStripe|代表竖条纹图案|

在下面的示例中，A1单元格的前景色已设置，但A2配置为具有前景色和背景色的垂直条纹背景模式。

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

            // Adding a new worksheet to the Workbook object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Define a Style and get the A1 cell style
            let style = worksheet.cells.get("A1").style;

            // Setting the foreground color to yellow
            style.foregroundColor = AsposeCells.Color.Yellow;

            // Setting the background pattern to vertical stripe
            style.pattern = AsposeCells.BackgroundType.VerticalStripe;

            // Apply the style to A1 cell
            worksheet.cells.get("A1").style = style;

            // Get the A2 cell style
            style = worksheet.cells.get("A2").style;

            // Setting the foreground color to blue
            style.foregroundColor = AsposeCells.Color.Blue;

            // Setting the background color to yellow
            style.backgroundColor = AsposeCells.Color.Yellow;

            // Setting the background pattern to vertical stripe
            style.pattern = AsposeCells.BackgroundType.VerticalStripe;

            // Apply the style to A2 cell
            worksheet.cells.get("A2").style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and ready for download.</p>';
        });
    </script>
</html>
```


### **重要知识**

{{% alert color="primary" %}}

- 要设置单元格的前景色或背景色，可以使用 [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) 对象的 [**foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundColor-color-) 或 [**backgroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#backgroundColor-color-) 属性。只有在配置了 [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) 对象的 [**pattern**](https://reference.aspose.com/cells/javascript-cpp/style/#pattern-backgroundtype-) 属性后，这两个属性才会生效。
- [**foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundColor-color-) 属性设置单元格的色调颜色。[**pattern**](https://reference.aspose.com/cells/javascript-cpp/style/#pattern-backgroundtype-) 属性指定用于前景或背景色的背景图案类型。Aspose.Cells 提供了一个枚举 [**BackgroundType**](https://reference.aspose.com/cells/javascript-cpp/backgroundtype)，其中包含一组预定义的背景图案类型。
- 如果从 [**BackgroundType**](https://reference.aspose.com/cells/javascript-cpp/backgroundtype) 枚举中选择 *BackgroundType.None* 值，则不应用前景色。同样，如果选择 *BackgroundType.None* 或 *BackgroundType.Solid* 值，也不会应用背景色。
- 在检索单元格的阴影/填充颜色时，如果 [**style.pattern**](https://reference.aspose.com/cells/javascript-cpp/style/#pattern-backgroundtype-) 是 *BackgroundType.None*，[**style.foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundColor--) 将返回 *Color.Empty*。

{{% /alert %}}

### **应用梯度填充效果**

要将所需的渐变填充效果应用到单元格中，请相应地使用 [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) 对象的 [**twoColorGradient**](https://reference.aspose.com/cells/javascript-cpp/style/#twoColorGradient-color-color-gradientstyletype-number-) 属性。

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
        const { Workbook, SaveFormat, Color, GradientStyleType, TextAlignmentType } = AsposeCells;

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

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            const worksheet = workbook.worksheets.get(0);

            worksheet.cells.get(2, 1).putValue("test");

            const style = worksheet.cells.get("B3").style;

            style.isGradient = true;
            style.twoColorGradient = [ new Color(255, 255, 255), new Color(79, 129, 189), GradientStyleType.Horizontal, 1 ];
            style.font.color = Color.Red;
            style.horizontalAlignment = TextAlignmentType.Center;
            style.verticalAlignment = TextAlignmentType.Center;

            worksheet.cells.get("B3").style = style;

            worksheet.cells.rowHeightPixel = [2, 53];

            worksheet.cells.merge(2, 1, 1, 2);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## **颜色和调色板**

调色板是在创建图像时可用的颜色数量。在演示文稿中使用标准调色板可以让用户创建一致的外观。每个Microsoft Excel（97-2003）文件都有一个包含可应用于单元格、字体、网格线、图形对象、填充和图表中的线条的56种颜色的调色板。

使用 Aspose.Cells 不仅可以使用调色板的现有颜色，还可以使用自定义颜色。在使用自定义颜色之前，首先将其添加到调色板中。

本主题讨论如何向调色板中添加自定义颜色。

### **向调色板中添加自定义颜色**

Aspose.Cells 支持 Microsoft Excel 的 56 种颜色调色板。要使用在调色板中未定义的自定义颜色，需要将颜色添加到调色板中。

Aspose.Cells 提供一个类 [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)，代表一个 Microsoft Excel 文件。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) 类提供一个 [**changePalette**](https://reference.aspose.com/cells/javascript-cpp/workbook/#changePalette-color-number-) 方法，接受以下参数以添加自定义颜色以修改调色板：

- Custom Color，要添加的自定义颜色。
- Index，自定义颜色在调色板中的索引，将替换指定的颜色。应该在 0-55 之间。

下面的示例在应用于字体之前向调色板中添加了自定义颜色（兰花紫）。

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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Checks if a color is in the palette for the spreadsheet.
            console.log(workbook.isColorInPalette(AsposeCells.Color.Orchid));

            // Adding Orchid color to the palette at 55th index
            workbook.changePalette(AsposeCells.Color.Orchid, 55);

            console.log(workbook.isColorInPalette(AsposeCells.Color.Orchid));

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.putValue("Hello Aspose!");

            // Defining new Style object
            const styleObject = workbook.createStyle();
            // Setting the Orchid (custom) color to the font
            styleObject.font.color = workbook.colors[55];

            // Applying the style to the cell
            cell.style = styleObject;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


{{% alert color="primary" %}}

调色板只能容纳 56 种颜色。当向调色板中添加自定义颜色时，调色板会改变，文件中用先前颜色格式化的任何元素也会发生变化。因此，在更改调色板时，请务必小心。此外，在 XLS（Excel 97 - 2003）文件格式中，这是唯一的限制，XLSX 或其他高级 MS Excel（2007/2010 或 2013）文件格式则没有这种限制。

{{% /alert %}}
