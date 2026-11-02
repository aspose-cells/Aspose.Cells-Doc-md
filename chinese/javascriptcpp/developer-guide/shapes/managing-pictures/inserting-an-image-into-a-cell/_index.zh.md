---
title: 将图像插入单元格
linktitle: 将图像插入单元格
description: Aspose.Cells for JavaScript via C++ 是一个用于处理电子表格文件的库。本文介绍如何使图片恰好适应单个单元格，既可以将浮动图片覆盖在单元格上，也可以将图像直接嵌入单元格中。
keywords: Aspose.Cells, JavaScript via C++ 库, 电子表格, 插入图像, 嵌入图像, 单元格中的图片, 使图像适应单元格, Pictures, EmbeddedImage
type: docs
weight: 80
url: /zh/javascript-cpp/inserting-an-image-into-a-cell/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 提供两种不同方式将图像与单个单元格关联。浮动图片是工作表绘图层上的形状，在视觉上叠加于单元格区域之上；嵌入图像则存储在单元格本身中，并自动缩放以适应单元格的显示区域。请选择最符合您布局要求的方法。
{{% /alert %}}

## **简介**
在设计用作可视化报表、产品目录、员工通讯录、仪表板或库存列表的电子表格时，使图片精确适配单个单元格是一项常见需求。与其将图像拉伸至多个单元格，或松散地放置在工作表上，您可能需要一个美观、与单元格绑定且始终与所属单元格保持对齐的图像。
Aspose.Cells 支持通过两种互补方式实现此场景：
- **方法 1 — 将浮动图片覆盖在单元格上。** 向工作表添加一个 `Picture`，通过 `picture.setPlacement(PlacementType.MoveAndSize)` 设置其放置方式，并通过 `picture.setUpperLeftRow()`、`picture.setUpperLeftColumn()`、`picture.setLowerRightRow()` 和 `picture.setLowerRightColumn()` 调整其锚定单元格，使图片恰好覆盖一个单元格。
- **方法 2 — 将图像直接嵌入单元格。** 通过 `cell.setEmbeddedImage(imageBuffer)` 为单元格设置包含图像数据的 `Buffer`。图像会自动缩放以适应单元格的显示区域，并随单元格一同移动。
下文将介绍这两种方法，解释相关 API，并展示如何在代码中使用它们。

## **方法 1：将浮动图片覆盖在单元格上**
浮动图片是位于工作表绘图层上的 `Picture` 对象。尽管它不属于任何单个单元格，但会锚定到一个单元格区域。图片的锚定单元格（即左上角和右下角所在的单元格）决定其在工作表上的视觉边界。默认情况下，刚添加的图片会横跨多个单元格。
若要让浮动图片**恰好覆盖一个单元格**，需执行以下操作：
1. 使用 `worksheet.getPictures().add(row, column, imageBuffer)` 添加图片，其中 `imageBuffer` 是包含图像数据的 `Buffer`。这会将新图片锚定到指定单元格。
2. 设置四个锚定值，使图片的边界矩形与目标单元格重合。
3. 调用 `picture.setPlacement(PlacementType.MoveAndSize)`，以便当用户调整列宽或行高时，图片能够随对应单元格一起移动和调整大小。

### **将图片锚定到单个单元格**
用于定义锚点的四个索引访问器均采用从零开始的索引：
- `picture.getUpperLeftRow()` 和 `picture.setUpperLeftRow(value)` — 图片上边缘的行索引。
- `picture.getUpperLeftColumn()` 和 `picture.setUpperLeftColumn(value)` — 图片左边缘的列索引。
- `picture.getLowerRightRow()` 和 `picture.setLowerRightRow(value)` — 图片下边缘的行索引。若要让图片下边缘与第 `r` 行的底边重合，请将其设为 `r + 1`。
- `picture.getLowerRightColumn()` 和 `picture.setLowerRightColumn(value)` — 图片右边缘的列索引。若要让图片右边缘与第 `c` 列的右边缘重合，请将其设为 `c + 1`。

{{% alert color="primary" %}}
Aspose.Cells 中的行索引和列索引采用**从零开始**的编号。单元格 C6 的行索引为 5，列索引为 2。右下角锚定值出现差一错误，是图片看似延伸至相邻单元格并与之重叠的最常见原因。
{{% /alert %}}

### **控制放置行为**
`picture.getPlacement()` 和 `picture.setPlacement(value)` 使用 `PlacementType` 枚举来控制用户调整图片所在行或列的大小时图片的行为。对于单单元格图片，推荐使用 `PlacementType.MoveAndSize`，这会使图片随对应单元格一起移动和调整大小，从而保持图片与单元格精确贴合。

### **分步说明**
1. 创建新的 `Workbook`（或打开现有工作簿）。
2. 通过 `workbook.getWorksheets().getAt(0)` 访问目标 `Worksheet`。
3. 例如，可使用 Node.js `fs.readFileSync` 将图像文件从磁盘读取到 `Buffer` 中。
4. 调用 `worksheet.getPictures().add(5, 2, imageBuffer)`，添加锚定到单元格 C6 的图片。该方法返回新图片在 `Pictures` 集合中的索引；使用该索引可获取相应的 `Picture`。
5. 设置四个锚定坐标，使图片仅覆盖单元格 C6：`picture.setUpperLeftRow(5)`、`picture.setUpperLeftColumn(2)`、`picture.setLowerRightRow(6)` 和 `picture.setLowerRightColumn(3)`。
6. 调用 `picture.setPlacement(PlacementType.MoveAndSize)`，以便调整列宽或行高时，图片仍与 C6 保持对齐。
7. 可以选择在外围单元格中添加示例文本，以演示只有单元格 C6 包含该图片。
8. 将工作簿保存到磁盘，文件格式为 `.xlsx`。
以下代码演示了完整的实现方式。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".png,image/png" />
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const file = fileInput.files[0];
            if (!file) {
                document.getElementById('result').innerHTML =
                    '<p style="color: red;">Please select a PNG image.</p>';
                return;
            }
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const imageData = new Uint8Array(await file.arrayBuffer());
            const picIndex = worksheet.pictures.add(5, 2, imageData);
            const picture = worksheet.pictures.get(picIndex);
            picture.upperLeftRow = 5;
            picture.upperLeftColumn = 2;
            picture.lowerRightRow = 6;
            picture.lowerRightColumn = 3;
            picture.placement = AsposeCells.Drawing.PlacementType.MoveAndSize;
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **方法 2：将图像直接嵌入单元格**
Aspose.Cells 还提供了一种更简单的机制来创建与单元格绑定的图像，即 `cell.setEmbeddedImage(imageBuffer)` 方法。通过此方法设置图像数据后，图像会附加到单元格本身，如同内嵌内容。

### **嵌入图像的工作方式**
- 图像作为单元格内容的一部分进行存储，而不是作为绘图层上的形状。
- 图像会自动缩放以适应单元格的呈现边界。无需设置锚定坐标或放置设置。
- 该单元格仍然是具有有效地址的常规单元格，可以由公式引用、作为行的一部分参与排序，或用于其他单元格级操作。
因此，当目标仅仅是“将图像存放在该单元格内”时，`cell.setEmbeddedImage(imageBuffer)` 是最简洁的选项。

### **分步说明**
1. 创建新的 `Workbook`（或打开现有工作簿）。
2. 通过 `workbook.getWorksheets().getAt(0)` 访问目标 `Worksheet`。
3. 例如，可使用 Node.js `fs.readFileSync` 将图像文件从磁盘读取到 `Buffer` 中。
4. 获取目标单元格的引用，可以使用 `worksheet.getCells().get("C6")` 或 `worksheet.getCells().get(5, 2)`。
5. 通过 `cell.setEmbeddedImage(imageBuffer)` 将 `Buffer` 传递给单元格。
6. 可以选择调整目标行的高度和目标列的宽度，使嵌入图像显示得更加醒目。
7. 将工作簿保存到磁盘，文件格式为 `.xlsx`。
以下代码演示了完整的实现方式。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".png,.jpg,.jpeg" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook } = AsposeCells;
        const asposeReady = AsposeCells.onReady({
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
            if (!fileInput.files || fileInput.files.length === 0) {
                result.innerHTML = '<p style="color: red;">Please select an image file.</p>';
                return;
            }
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            // 获取目标单元格 C6
            const cell = worksheet.cells.get("C6");
            // 将图像文件读入字节数组
            const imageData = new Uint8Array(await fileInput.files[0].arrayBuffer());
            // 将图像直接嵌入单元格
            cell.embeddedImage = imageData;
            // 可选择调整行高和列宽，使嵌入的图像更清晰可见
            worksheet.cells.setColumnWidth(2, 30); // C 列（索引 2）
            worksheet.cells.setRowHeight(5, 100); // 第 6 行（索引 5）
            // 将生成的工作簿保存为 .xlsx 文件
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **选择合适的方法**
两种方法都能生成适合单个单元格的图片，但二者在图片的存储方式和行为方面有所不同：
- **使用方法 1（浮动图片）的情形：**
  - 需要更精细地控制放置方式、层叠顺序，或图片与其他绘图对象的对齐。
  - 希望图片的行为类似于形状，可以选择、调整顺序或与其他形状组合。
  - 需要与现有通过 `worksheet.getPictures()` 访问 `Pictures` 集合的代码保持旧版兼容。
  - 需要根据工作表布局动态计算锚定坐标。
- **使用方法 2（嵌入图像）的情形：**
  - 希望以最简单的方式将图像插入单元格。
  - 图像应像其他单元格内容一样随单元格一同移动。

## 相关文章
- [Aspose.Cells for JavaScript via C++ 中的 Excel 照相机](/cells/zh/javascript-cpp/excel-camera/)
- [在 Aspose.Cells for JavaScript via C++ 中向数据透视表添加筛选字段](/cells/zh/javascript-cpp/add-page-field-in-pivot-table/)
- [在 Aspose.Cells for JavaScript via C++ 中对数据透视表应用样式](/cells/zh/javascript-cpp/apply-style-to-pivot-table/)
- [在 Aspose.Cells for JavaScript via C++ 中将迷你图转换为图像和 HTML](/cells/zh/javascript-cpp/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="javascript-cpp" >}}