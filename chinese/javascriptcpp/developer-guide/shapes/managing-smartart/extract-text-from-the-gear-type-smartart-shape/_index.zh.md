---
title: 使用JavaScript通过C++提取Gear类型SmartArt形状中的文本
linktitle: 从齿轮型智能图形中提取文本
type: docs
weight: 500
url: /zh/javascript-cpp/extract-text-from-the-gear-type-smartart-shape/
description: 学习如何使用Aspose.Cells for Java脚本通过C++从Gear类型SmartArt形状中提取文本
---

## **可能的使用场景**

Aspose.Cells可以从Gear类型Smart Art形状中提取文本。为此，你应首先使用[**Shape.resultOfSmartArt**](https://reference.aspose.com/cells/javascript-cpp/shape/#resultOfSmartArt--)属性将Smart Art形状转换为组形状，然后使用[**GroupShape.groupedShapes**](https://reference.aspose.com/cells/javascript-cpp/groupshape/#groupedShapes--)属性获取组成该组形状的所有单个形状的数组，最后可以在循环中逐一迭代所有单个形状并使用[**Shape.text**](https://reference.aspose.com/cells/javascript-cpp/shape/#text--)属性提取其文本。

## **从齿轮型智能图形中提取文本**

以下示例代码加载包含齿轮型智能图形的[sample Excel文件](67338483.xlsx)。然后按上述步骤从其各个形状中提取文本。请参阅下面提供的代码的控制台输出以供参考。

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Extract Gear SmartArt Text Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access first shape.
            const shape = worksheet.shapes.get(0);

            // Get the result of gear type smart art shape in the form of group shape.
            const groupShape = shape.resultOfSmartArt;

            // Get the list of individual shapes consisting of group shape.
            const shapes = groupShape.groupedShapes;

            // Extract the text of gear type shapes and display them.
            const results = [];
            for (let i = 0; i < shapes.count; i++) {
                const s = shapes.get(i);

                if (s.type === AsposeCells.AutoShapeType.Gear9 || s.type === AsposeCells.AutoShapeType.Gear6) {
                    const text = s.text;
                    results.push(text);
                    console.log("Gear Type Shape Text: " + text);
                }
            }

            if (results.length) {
                document.getElementById('result').innerHTML = '<p style="color: green;">Found gear shape texts:</p><ul>' + results.map(t => '<li>' + t + '</li>').join('') + '</ul>';
            } else {
                document.getElementById('result').innerHTML = '<p style="color: orange;">No gear type SmartArt shapes found in the first shape.</p>';
            }
        });
    </script>
</html>
```

## **控制台输出**

{{< highlight javascript >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
