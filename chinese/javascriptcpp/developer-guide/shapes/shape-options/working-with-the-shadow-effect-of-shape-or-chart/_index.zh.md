---
title: 使用 C++ 通过 JavaScript 操作形状或图表的阴影效果
linktitle: 使用形状或图表的阴影效果
type: docs
weight: 220
url: /zh/javascript-cpp/working-with-the-shadow-effect-of-shape-or-chart/
description: 学习如何用 C++ 通过 JavaScript 设置形状或图表的阴影效果。
---

## **可能的使用场景**  
 Aspose.Cells for JavaScript 通过 C++ 提供 [Shape.shadowEffect](https://reference.aspose.com/cells/javascript-cpp/shape/#shadowEffect--) 属性以及 [ShadowEffect](https://reference.aspose.com/cells/javascript-cpp/shadoweffect) 类，用于设置形状或图表的阴影效果。该类包含多个属性，可根据需求调节不同效果。  

- [ShadowEffect.angle](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#angle--)  
- [阴影效果模糊](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#blur--)  
- [阴影效果颜色](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#color--)  
- [阴影距离](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#distance--)  
- [阴影预设类型](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#presetType--)  
- [阴影大小](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#size--)  
- [阴影透明度](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#transparency--)  

## **使用 Aspose.Cells 处理形状或图表的阴影效果**  
以下示例代码加载[源Excel文件](5115425.xlsx)，访问第一个工作表中的第一个形状，设置[Shape.shadowEffect](https://reference.aspose.com/cells/javascript-cpp/shape/#shadowEffect--)属性的子属性，然后将工作簿保存到[输出Excel文件](5115411.xlsx)。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Shape Shadow Effect Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);
            const shape = worksheet.shapes.get(0);

            const shadowEffect = shape.shadowEffect;
            shadowEffect.angle = 150;
            shadowEffect.blur = 4;
            shadowEffect.distance = 45;
            shadowEffect.transparency = 0.3;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shadow effect applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
