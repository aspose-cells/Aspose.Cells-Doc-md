---
title: 通过C++用JavaScript更改刻度标签方向
linktitle: 更改刻度标签方向
description: 学习如何在Aspose.Cells for JavaScript中通过C++更改刻度标签的方向。我们的指南将帮助您理解如何调整轴上刻度标签的方向，包括水平、垂直和倾斜的布局。
keywords: Aspose.Cells for JavaScript via C++，刻度标签，方向，布局，轴线，水平，垂直，倾斜。
type: docs
weight: 170
url: /zh/javascript-cpp/change-tick-label-direction/
---

## **更改刻度标签方向**

Aspose.Cells 通过使用 [**TickLabels.directionType**](https://reference.aspose.com/cells/javascript-cpp/ticklabels/#directionType--) 属性提供更改图表刻度标签方向的能力。 [**TickLabels.directionType**](https://reference.aspose.com/cells/javascript-cpp/ticklabels/#directionType--) 属性接受 [**ChartTextDirectionType**](https://reference.aspose.com/cells/javascript-cpp/charttextdirectiontype) 枚举值。 [**ChartTextDirectionType**](https://reference.aspose.com/cells/javascript-cpp/charttextdirectiontype) 枚举包含以下成员：

- 水平
- 垂直
- 旋转90度
- 旋转270度
- 堆叠

以下图像比较了源文件和输出文件

### **源文件图像**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **输出文件图像**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

以下代码片段将刻度标签方向从Rotate90更改为水平方向

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Change Tick Label Direction Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartTextDirectionType } = AsposeCells;

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
            const result = document.getElementById('result');

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);

            const chart = worksheet.charts.get(0);

            chart.categoryAxis.tickLabels.directionType = ChartTextDirectionType.Horizontal;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputChangeChartDataLableDirection.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            result.innerHTML = '<p style="color: green;">Tick label direction changed. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

可以从以下链接下载源文件和输出文件。

[源文件](105480221.xlsx)

[输出文件](105480223.xlsx)
