---
title: 通过C++使用JavaScript获取区域的地址、单元格数量、偏移、整列和整个行
linktitle: 获取范围的地址、单元格计数、偏移、整列和整行
type: docs
weight: 330
url: /zh/javascript-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
---

## **可能的使用场景**
Aspose.Cells for JavaScript via C++ 提供了Range对象，该对象具有多种实用方法，方便用户轻松处理Excel区域。本文介绍了Range对象的以下方法或属性的用法。

- **地址**

获取范围的地址。

- **单元格计数**

获取范围中的所有单元格数。

- **偏移**

通过偏移获取范围。

- **整列**

获取代表包含指定范围的整列（或多列）的 Range 对象。

- **整行**

获取代表包含指定范围的整行（或多行）的 Range 对象。

## **获取范围的地址、单元格计数、偏移、整列和整行**
下面的示例代码解释了上述方法和属性的用法。请参考以下给出的代码的控制台输出。

## **示例代码**
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
            // This example creates ranges on a new empty workbook and prints info to the page.
            const resultEl = document.getElementById('result');
            resultEl.innerHTML = '';

            // Create empty workbook.
            const wb = new Workbook();

            // Access first worksheet.
            const ws = wb.worksheets.get(0);

            // Create range A1:B3.
            console.log("Creating Range A1:B3\n");
            let rng = ws.cells.createRange("A1:B3");

            // Print range address and cell count.
            const lines = [];
            lines.push("Range Address: " + rng.address);
            lines.push("Range row Count: " + rng.rowCount);
            lines.push("Range column Count: " + rng.columnCount);

            // Formatting console output.
            lines.push("----------------------");
            lines.push("");

            // Create range A1.
            console.log("Creating Range A1\n");
            rng = ws.cells.createRange("A1");

            // Print range offset, entire column and entire row.
            lines.push("Offset: " + rng.offset(2, 2).address);
            lines.push("Entire Column: " + rng.entireColumn.address);
            lines.push("Entire Row: " + rng.entireRow.address);

            // Formatting console output.
            lines.push("----------------------");
            lines.push("");

            // Display results
            resultEl.innerHTML = '<pre>' + lines.join("\n") + '</pre>';
        });
    </script>
</html>
```

## **控制台输出**
{{< highlight javascript >}}
 Creating Range A1:B3

Range Address: A1:B3

Cell Count: 6

\----------------------

Creating Range A1

Offset: C3

Entire Column: A:A

Entire Row: 1:1

\----------------------

{{< /highlight >}}
