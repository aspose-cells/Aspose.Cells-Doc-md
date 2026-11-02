---
title: 使用 Aspose.Cells for JavaScript via C++ 将迷你图转换为图像和 HTML
linktitle: 使用 Aspose.Cells for JavaScript via C++ 将迷你图转换为图像和 HTML
description: 了解如何使用 HtmlSaveOptions 将 Aspose.Cells 迷你图呈现为可嵌入单元格的独立图像，并将包含迷你图的工作表导出为 HTML
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, 迷你图, sparkline.toImage, cell.embeddedImage, HtmlSaveOptions, 呈现迷你图, 将迷你图转换为图像, 将迷你图导出为 HTML
type: docs
weight: 120
url: /zh/javascript-cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
迷你图是置于工作表单元格内的小型图表。Aspose.Cells 支持将每个迷你图提取为独立图像（用于嵌入另一个单元格或外部报告），也支持将整个包含迷你图的工作表导出为 HTML，以便在浏览器中分发。本文使用的 `cell.embeddedImage` 属性从 **Aspose.Cells 26.5 及更高版本**开始提供。
{{% /alert %}}

## **简介**
迷你图是一种直接在工作表内可视化趋势的紧凑方式。虽然 Excel 用户可以在原位置查看迷你图，但许多实际场景需要将迷你图移出单元格，例如将其作为静态图片嵌入另一个单元格、附加到自动发送的电子邮件中，或作为发布到网页的 HTML 报告的一部分进行呈现。
Aspose.Cells 支持这两种操作。`sparkline.toImage` 方法将单个迷你图呈现为 `Buffer`，生成的字节可赋给 `cell.embeddedImage`，从而将图片存储在工作簿的单个单元格中。此外，`HtmlSaveOptions` 可将整个工作簿（包括迷你图）转换为单个自包含 HTML 文件。本文将完整讲解这两种工作流。

## **工作流 1 — 将迷你图呈现为图像并嵌入单元格**
在此工作流中，您将创建一个包含一小段源值区域的工作表，为该区域附加三个不同的迷你图组（`Line`、`Column` 和 `Stacked`/胜负型），将每个组呈现为 PNG，并将这些 PNG 字节作为嵌入图像写入相邻单元格。最终结果是一个 `.xlsx` 文件，其中同时包含动态迷你图及其呈现后的图片对应项。

### **分步说明**
1. 创建新的 `Workbook`，并获取第一个 `Worksheet` 的引用。
2. 使用五个示例数值填充 `A1` 到 `E1` 的单元格（例如每日销售额或温度读数）。
3. 通过调用 `worksheet.getSparklineGroups().add(...)`，向工作表添加三个 `SparklineGroup` 对象：
   - 一个以 `F1` 为锚点、数据区域为 `A1:E1` 的 `SparklineType.Line` 组。
   - 一个以 `G1` 为锚点、数据区域为 `A1:E1` 的 `SparklineType.Column` 组。
   - 一个以 `H1` 为锚点、数据区域为 `A1:E1` 的 `SparklineType.Stacked`（胜负型）组。
4. 创建 `ImageOrPrintOptions` 实例，并将其 `imageType` 属性设置为 `ImageType.Png`，使每个迷你图呈现为 PNG 图片。
6. 将工作簿保存为 `output_with_sparklines.xlsx`。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, CellArea, ImageOrPrintOptions } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // 创建一个新的工作簿并访问第一个工作表
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // 在 A1:E1 单元格中填充示例数据
            cells.get("A1").value = 5;
            cells.get("B1").value = -3;
            cells.get("C1").value = 8;
            cells.get("D1").value = -2;
            cells.get("E1").value = 6;
            // 添加以 F1（列 5，行 0）为锚点的折线迷你图组
            const lineArea = new CellArea();
            lineArea.startColumn = 5;
            lineArea.endColumn = 5;
            lineArea.startRow = 0;
            lineArea.endRow = 0;
            const lineIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Line,
                "A1:E1",
                false,
                lineArea
            );
            // 添加以 G1（列 6，行 0）为锚点的列迷你图组
            const columnArea = new CellArea();
            columnArea.startColumn = 6;
            columnArea.endColumn = 6;
            columnArea.startRow = 0;
            columnArea.endRow = 0;
            const columnIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Column,
                "A1:E1",
                false,
                columnArea
            );
            // 添加以 H1（列 7，行 0）为锚点的盈亏（堆积）迷你图组
            const stackedArea = new CellArea();
            stackedArea.startColumn = 7;
            stackedArea.endColumn = 7;
            stackedArea.startRow = 0;
            stackedArea.endRow = 0;
            const stackedIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Stacked,
                "A1:E1",
                false,
                stackedArea
            );
            // 配置 PNG 输出的图像选项
            const imageOptions = new ImageOrPrintOptions();
            imageOptions.imageType = AsposeCells.ImageType.Png;
            // 将折线迷你图转换为图像并嵌入 F2 单元格
            const lineSp = worksheet.sparklineGroups.get(lineIdx).sparklines.get(0);
            cells.get("F2").embeddedImage = lineSp.toImage(imageOptions);
            // 将列迷你图转换为图像并嵌入 G2 单元格
            const columnSp = worksheet.sparklineGroups.get(columnIdx).sparklines.get(0);
            cells.get("G2").embeddedImage = columnSp.toImage(imageOptions);
            // 将盈亏迷你图转换为图像并嵌入 H2 单元格
            const stackedSp = worksheet.sparklineGroups.get(stackedIdx).sparklines.get(0);
            cells.get("H2").embeddedImage = stackedSp.toImage(imageOptions);
            // 将工作簿保存到磁盘
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_with_sparklines.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

上述代码生成的工作簿中，迷你图的每种视觉表示都以两种形式存在：一种是锚定在第 1 行的动态原生迷你图，另一种是直接嵌入第 2 行相邻单元格中的静态 PNG 图片。由于这些图片存储在文件内部，因此工作簿仍是单一的自包含文件，可以通过电子邮件发送或归档，而不会破坏嵌入图像引用。

{{% alert color="primary" %}}
由于每个迷你图组都锚定在一个单元格中，因此可以通过索引器 `group.getSparklines()[0]` 直接访问，而无需枚举集合。这样既可缩短呈现代码，也符合典型的“每个锚定单元格对应一个迷你图”模式。通过 `cell.embeddedImage` 存储图片字节需要 Aspose.Cells 26.5 或更高版本。
{{% /alert %}}

## **工作流 2 — 将迷你图工作表导出为 HTML**
工作簿中包含动态迷你图（以及可选的嵌入式图片对应项）后，即可将整个工作表保存为 HTML 并发布到网页。`HtmlSaveOptions` 类提供控制此次导出所需的各项选项；在此工作流中，将复用工作流 1 生成的 `output_with_sparklines.xlsx` 文件，并将其转换为简洁的单页 HTML 文档。

### **分步说明**
1. 确保工作流 1 生成的 `output_with_sparklines.xlsx` 文件在工作目录中可用。
2. 将该文件加载到新的 `Workbook` 实例中。
3. 实例化 `HtmlSaveOptions`，并将其 `exportActiveWorksheetOnly` 属性设置为 `true`，使生成的 HTML 文件仅包含活动工作表，而非整个工作簿。
4. 调用 `workbook.save("sparklines.html", htmlOptions)`，将 HTML 输出写入磁盘。

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
        const { Workbook, HtmlSaveOptions } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            try {
                const file = fileInput.files[0];
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const htmlOptions = new HtmlSaveOptions();
                htmlOptions.exportActiveWorksheetOnly = true;
                const outputData = workbook.save(AsposeCells.SaveFormat.Html, htmlOptions);
                const blob = new Blob([outputData], { type: "text/html" });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "sparklines.html";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = `<p style="color: red;">${error.message}</p>`;
            }
        });
    </script>
</html>
```

上述代码将工作流 1 中包含迷你图的工作簿转换为可移植的 HTML 文件。迷你图组会呈现为生成的 HTML 表格中的内嵌图片，因此最终用户无需安装 Excel，即可在任何现代浏览器中查看趋势。将 `exportActiveWorksheetOnly` 设置为 `true` 可以避免意外发布隐藏工作表或辅助数据，导出内容仅限于当前用户可见的工作表。

{{% alert color="primary" %}}
`HtmlSaveOptions` 类还提供其他属性，可用于微调输出，例如 `exportHiddenWorksheet`、`exportImagesAsBase64` 和 `encoding`。请根据部署目标调整这些属性。
{{% /alert %}}

## **API 摘要**
上述工作流依赖一小组协同工作的 Aspose.Cells API。
- `SparklineGroup` 及其集合访问器 `worksheet.getSparklineGroups()` 用于声明每个迷你图组的类型（`Line`、`Column`、`Stacked`）、数据区域和锚定单元格。本文中的每个组均锚定到一个单元格，因此可通过 `worksheet.getSparklineGroups()[i]` 访问该组。
- `Sparkline` 及索引器 `group.getSparklines()[0]` 返回组中的单个迷你图。由于示例中的每个组恰好包含一个迷你图，因此无需使用迭代循环。
- `sparkline.toImage(imageOrPrintOptions)` 是呈现方法，它以 `Buffer` 的形式返回迷你图图片。返回的字节可直接赋给 `cell.embeddedImage`。
- `HtmlSaveOptions.exportActiveWorksheetOnly`（布尔值）将 HTML 导出限制为活动工作表。在生成单页报告时，它是 `HtmlSaveOptions` 上最常用的属性之一。
- `ImageOrPrintOptions.imageType` 选择图片格式（例如 `ImageType.Png`），该格式用于通过 `toImage` 进行呈现以及将工作表打印为图片。

{{< app/cells/assistant language="javascript-cpp" >}}