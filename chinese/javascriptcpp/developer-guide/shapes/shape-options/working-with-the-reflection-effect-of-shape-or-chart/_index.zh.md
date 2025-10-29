---
title: 使用 C++ 通过 JavaScript 处理形状或图表的反射效果
linktitle: 处理形状或图表的倒影效果
type: docs
weight: 210
url: /zh/javascript-cpp/working-with-the-reflection-effect-of-shape-or-chart/
description: 学习如何利用 C++ 通过 JavaScript 设置形状或图表的反射效果，以实现不同的视觉效果。
---

## **可能的使用场景**
 Aspose.Cells for JavaScript 通过 C++ 提供 [Shape.reflection](https://reference.aspose.com/cells/javascript-cpp/shape/#reflection--) 属性和 [ReflectionEffect](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect) 类，用于设置形状或图表的反射效果。该类包含多个可以根据需求调整的属性。

- [ReflectionEffect.blur](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#blur--)
- [ReflectionEffect.d方向](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#direction--)
- [ReflectionEffect.距离](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#distance--)
- [ReflectionEffect.渐隐方向](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#fadeDirection--)
- [ReflectionEffect.与形状旋转同步](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#rotWithShape--)
- [ReflectionEffect.大小](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#size--)
- [ReflectionEffect.透明度](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#transparency--)
- [ReflectionEffect.类型](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#type--)

## **使用形状或图表的反射效果**
下方示例代码加载 [源 Excel 文件](5115424.xlsx)，获取默认工作表中的第一个形状，设置不同的 [Shape.reflection](https://reference.aspose.com/cells/javascript-cpp/shape/#reflection--) 属性，并将工作簿保存为 [输出 Excel 文件](5115423.xlsx)。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Shape Reflection Effect Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
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

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first shape
            const shape = worksheet.shapes.get(0);

            // Set the reflection effect of the shape, set its Blur, Size, Transparency and Distance properties
            const reflectionEffect = shape.reflection;
            reflectionEffect.blur = 30;
            reflectionEffect.size = 90;
            reflectionEffect.transparency = 0;
            reflectionEffect.distance = 80;

            // Save the workbook in xlsx format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Reflection effect updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
