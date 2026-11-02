---
title: 智能标记单单元格数组渲染 | Aspose.Cells for JavaScript via C++
description: 了解如何借助 Aspose.Cells for JavaScript via C++，使用智能标记中的 ArrayAsSingle 和 ExtraDelimiter 属性将数组数据呈现到单个单元格中。
linktitle: 智能标记单单元格数组渲染 | Aspose.Cells
url: /zh/javascript-cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++ 库, 电子表格, 智能标记, ArrayAsSingle, ExtraDelimiter, 单单元格数组, 数组呈现, 模板
type: docs
weight: 195
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 支持通过智能标记将数组数据呈现到单个单元格中。通过结合使用 `ArrayAsSingle` 属性和 `ExtraDelimiter` 属性，开发者可以控制数组元素在单个单元格内的分隔方式，从而为报表和模板提供灵活的格式设置。
{{% /alert %}}

## **简介**
Aspose.Cells 中的智能标记是一项强大的基于模板的功能，可使用 `&=DataSource.Field` 等标记表达式动态填充电子表格数据。该标记置于设计器工作簿中；当 `WorkbookDesigner` 处理模板时，这些标记将替换为所提供数据源中的值。
默认情况下，当智能标记引用数组属性（例如 `&=DataSource.Numbers`）时，引擎会展开数组，并将每个元素分别放入相邻的单元格中——可以水平排列在一行中，也可以垂直排列在一列中。尽管此行为在许多场景中都很方便，但在某些情况下，您可能希望将整个数组呈现到一个单元格中，将各元素连接起来，并使用所选分隔符进行分隔。
在智能标记标记中结合使用 `ArrayAsSingle` 和 `ExtraDelimiter` 属性，正好可以满足这一需求。它们使您仍可直接使用数组数据源，同时保持报表布局紧凑且可预测。

## **为什么需要此功能**

### **默认数组展开行为**
当智能标记引用数组属性时，Aspose.Cells 默认会将数组展开到多个单元格中。例如，对于包含四个字符串的数组，`&=Product.Tags` 之类的标记会将每个值放入各自的单元格中，从而将其他模板内容向外推移，并可能破坏精心设计的报表布局。

### **使用场景限制**
默认的数组展开行为在许多实际场景中并不理想：
- **摘要类报表**：需要每条记录仅占一行的紧凑布局。
- **标签、标注或关键字列表**：需要在单个单元格中显示以逗号或管道符分隔的值。
- **筛选标签或状态指示器**：需要将多个值集中显示在一处以提高可读性。
- **下游管道**（CSV 导出、PDF 呈现、邮件合并）：每个单元格需要一个合并后的值，而不是扩展后的区域。
- **跨平台兼容性**：某些使用方无法处理跨多个单元格扩展的数组。

### **此功能填补的空白**
如果缺少内置机制，开发者将不得不在 JavaScript 中预处理数据，在绑定到工作簿设计器之前将数组合并为带分隔符的字符串。这会重复实现逻辑、复杂化数据模型，并增加出错的可能性。`ArrayAsSingle` 和 `ExtraDelimiter` 属性无需此类变通做法，可直接在智能标记内以声明方式处理格式设置。

## **功能优势**
在智能标记中使用 `ArrayAsSingle` 和 `ExtraDelimiter` 属性可获得多项优势：
- **单单元格容纳**：所有数组元素都呈现于同一个单元格中，使布局紧凑且可预测。
- **自定义分隔符控制**：可指定任意分隔字符串，如逗号、分号、连字符、管道符、换行符或自定义文本。
- **基于模板的格式设置**：无需额外代码预处理数据；格式规则直接写在智能标记标记内。
- **更整洁的报表**：数组数据不会再将相邻的模板内容推移到其他行或列。
- **多样的数据类型**：适用于字符串、数字、日期以及可使用分隔符连接的任何其他数据类型。
- **向后兼容性**：省略这些属性时，将保留原有的数组展开行为，因此现有模板无需修改即可继续使用。

## **如何使用此功能**

### **智能标记语法**
`ArrayAsSingle` 和 `ExtraDelimiter` 属性以键值对形式传入标准智能标记的括号内。一般语法如下：

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
        const { Workbook, WorkbookDesigner } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const product = {
                Tags: ["C#", "Aspose", "SmartMarker", "Excel"]
            };
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Tags";
            cells.get("A2").value = '&=Product.Tags(arrayasSingle=true, extraDelimiter=", ")';
            const designer = new WorkbookDesigner();
            designer.setWorkbook(workbook);
            designer.setDataSource("Product", product);
            designer.process();
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_arraySingle.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

该标记由以下部分组成：
- `&=DataSource.ArrayProperty` — 引用绑定数据源中数组属性的标准智能标记。
- `arrayasSingle=true` — 指示引擎将整个数组呈现到单个单元格中。仅 `true` 值会触发单单元格行为。
- `extraDelimiter=", "` — 定义数组元素之间放置的分隔符。该值为字符串字面量，可以是空字符串、单字符或多字符字符串。

{{% alert color="primary" %}}
`extraDelimiter` 属性接受任何字符串字面量，包括多字符分隔符、自定义文本或转义序列（例如用于换行分隔输出的 `\n`）。如果数组为空，结果单元格将保持空白。
{{% /alert %}}

### **分步工作流**
以下工作流介绍了如何使用智能标记将数组呈现到单个单元格中。
1. **准备数据源**：创建一个对象或数据结构，该对象或数据结构公开一个返回数组的属性。此属性可以返回字符串数组、数字数组或任何其他受支持的值类型数组。
2. **创建设计器工作簿**：创建一个新的 `Workbook`，添加标题行，并放置一个引用数组属性的智能标记单元格，同时指定 `arrayasSingle` 和 `extraDelimiter` 属性。
3. **实例化 WorkbookDesigner**：创建一个 `WorkbookDesigner` 对象，将设计器工作簿附加到该对象，并使用 `setDataSource` 方法绑定数据源。
4. **处理标记**：调用 `workbookDesigner.process()` 方法展开智能标记，并使用实际数据填充工作簿。
5. **保存结果**：将生成的工作簿以 XLSX 或其他受支持的文件格式保存到磁盘。

### **代码示例 1 — 基本字符串数组呈现**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample" disabled>Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        class Student {
            constructor(scores) {
                this.Scores = scores;
            }
        }
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            document.getElementById("runExample").disabled = false;
            console.log("Aspose.Cells initialized");
        });
        document.getElementById("runExample").addEventListener("click", async () => {
            const student = new Student([95, 88, 76, 100, 67]);
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Scores";
            cells.get("A2").value = student.Scores.join(" - ");
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById("downloadLink");
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_numericArray.xlsx";
            downloadLink.style.display = "block";
            document.getElementById("result").innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **代码示例 2 — 使用自定义分隔符呈现数字数组**

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
        const { Workbook, WorkbookDesigner, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const order = {
                Items: ["Apple", "Banana", "Cherry", "Date"]
            };
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            // Section 1: Default Smart Marker - values spread horizontally across cells
            cells.get("A1").value = "Default Spreading Behavior:";
            cells.get("A2").value = "&=Order.Items";
            // Section 2: New single-cell rendering using arrayasSingle and extraDelimiter
            cells.get("A4").value = "Single Cell Rendering (arrayasSingle=true):";
            cells.get("A5").value = '&=Order.Items(arrayasSingle=true, extraDelimiter="; ")';
            // Bind the data source and process Smart Markers
            const designer = new WorkbookDesigner();
            designer.setWorkbook(workbook);
            designer.setDataSource("Order", order);
            designer.process();
            // Save the resulting workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_comparison.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **代码示例 3 — 比较默认行为与 ArrayAsSingle 行为**

### **注意事项与最佳实践**
使用 `ArrayAsSingle` 和 `ExtraDelimiter` 属性时，请注意以下事项：
- `extraDelimiter` 值被视为字符串字面量；请转义模板处理器可能会解释的特殊字符。
- `arrayasSingle` 属性接受布尔值（`true` / `false`）。仅 `true` 会触发单单元格行为；任何其他值均回退为默认的数组展开行为。
- 如果数组为空或 null，单元格将保持为空（或根据数据类型包含空字符串）。
- 此功能既适用于对象数据源，也适用于表格数据源，后者可以将某一列拆分为数组。
- 若要使用换行分隔输出，请将 `\n` 作为分隔符值。

{{< app/cells/assistant language="javascript-cpp" >}}