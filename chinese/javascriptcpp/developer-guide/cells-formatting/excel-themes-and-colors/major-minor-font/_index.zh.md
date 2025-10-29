---
title: 标题和正文主题字体
linktitle: 标题和正文主题字体
description: Aspose.Cells 是一个通过 C++ 的 JavaScript 库，用于操作电子表格文件。它支持在 Excel 文档中设置标题和正文的主题字体，让用户可以自定义文档的外观和样式。本文将介绍如何使用 Aspose.Cells 库操作 Excel 文档中的标题和正文主题字体。
keywords: Aspose.Cells、Excel 文档、标题、正文、主题字体、外观、样式、通过 C++ 的 JavaScript
type: docs
weight: 120
url: /zh/javascript-cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

当区域设置改变时，默认字体会自动变化。

如果默认字体更改，行高和列宽也会更改，甚至可能会搅乱页面布局。

是什么导致默认字体更改？

如果设置了 Excel 主题字体，Excel 将根据当前语言环境自动在不同字体之间切换。

{{% /alert %}}

## **在Excel中设置标题和正文主题字体**

在 Excel 中，选择“开始”选项卡，点击字体下拉框，你会看到“主题字体”，顶部显示两个主题字体：Calibri Light（标题），和 Calibri（正文），设置为英语区域。

**![主题字体](Theme-Fonts.png)**

如果选择主题字体，字体名称在不同区域可能会显示不同。如果你不希望字体在不同区域自动变化，请不要选择这两个主题字体。

## **程序matically 更改标题和正文字体**
利用 C++ 的 Aspose.Cells for JavaScript，我们可以检查默认字体是否为主题字体，或使用 [**Font.schemeType**](https://reference.aspose.com/cells/javascript-cpp/font/#schemeType-fontschemetype-) 方法设置主题字体。

以下示例代码展示了如何操作主题字体。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Change Theme Font Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FontSchemeType, Utils } = AsposeCells;

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

            // Accessing and modifying the default style and its font scheme
            let defaultStyle = workbook.defaultStyle;
            let font = defaultStyle.font;
            let schemeType = font.schemeType;

            if (schemeType === FontSchemeType.Major || schemeType === FontSchemeType.Minor) {
                console.log("It's theme font");
            }

            // Change theme font to normal font
            font.schemeType = FontSchemeType.None;

            // Assign the modified default style back to the workbook
            workbook.defaultStyle = defaultStyle;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.modified.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Theme font changed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```



## **动态以编程方式获取本地主题字体**
有时，我们的服务器和用户的机器不在同一区域。我们如何获取用户希望进行文件处理的相同字体？

在使用 [**LoadOptions.region**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#region-countrycode-) 方法加载文件之前，我们必须设置系统区域设置。

以下示例代码展示了如何获取本地主题字体。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Default Style Local Font Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new LoadOptions.
            const options = new AsposeCells.LoadOptions();
            // Sets the customer's region
            options.region = AsposeCells.CountryCode.Japan;

            // Instantiate a new Workbook using the uploaded file and load options.
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Get the default style
            const defaultStyle = workbook.defaultStyle;

            // Gets customer's local font.
            const localFontName = defaultStyle.font.name;

            resultDiv.innerHTML = `<p style="color: green;">Local font name: ${localFontName}</p>`;
        });
    </script>
</html>
```
