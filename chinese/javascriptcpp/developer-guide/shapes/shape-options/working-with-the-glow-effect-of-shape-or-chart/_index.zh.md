---
title: 使用 C++ 通过 JavaScript 操作形状或图表的发光效果
linktitle: 处理形状或图表的发光效果
type: docs
weight: 240
url: /zh/javascript-cpp/working-with-the-glow-effect-of-shape-or-chart/
description: 学习如何使用 C++ 通过 JavaScript 操作形状或图表的发光效果。
---

## **可能的使用场景**  
Aspose.Cells 提供 [Shape.glow](https://reference.aspose.com/cells/javascript-cpp/shape/#glow--) 属性及 [GlowEffect](https://reference.aspose.com/cells/javascript-cpp/gloweffect/) 类，用于设置形状或图表的发光效果。 [GlowEffect](https://reference.aspose.com/cells/javascript-cpp/gloweffect/) 类包含多个属性，可以根据应用需求设置不同效果。  

- [GlowEffect.size](https://reference.aspose.com/cells/javascript-cpp/gloweffect/#size--)  
- [GlowEffect.transparency](https://reference.aspose.com/cells/javascript-cpp/gloweffect/#transparency--)  
- [发光效果.颜色](https://reference.aspose.com/cells/javascript-cpp/gloweffect/#color--)  

## **处理形状或图表的发光效果**  
下方示例代码加载 [源 Excel 文件](5115407.xlsx)，访问第一个工作表中的第一个形状，设置 [Shape.glow](https://reference.aspose.com/cells/javascript-cpp/shape/#glow--) 属性的子属性，并将工作簿保存为 [输出 Excel 文件](5115414.xlsx)。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Glow Effect</title>
    </head>
    <body>
        <h1>Apply Glow Effect to First Shape</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Apply Glow Effect</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first shape
            const shape = worksheet.shapes.get(0);

            // Set the glow effect of the shape, Set its Size and Transparency properties
            const glowEffect = shape.glow;
            glowEffect.size = 30;
            glowEffect.transparency = 0.4;

            // Save the workbook in xlsx format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Glow effect applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
