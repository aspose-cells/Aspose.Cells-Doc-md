---
title: 用 JavaScript 通过 C++ 管理 Excel 电子表格文件的设置
linktitle: 工作簿设置
type: docs
weight: 185
url: /zh/javascript-cpp/workbook-settings/
description: 使用 Aspose.Cells for JavaScript 通过 C++ 管理 Excel 文件的设置。
---

## **工作簿设置概览**
处理 Excel 文件涉及多种设置，可以通过 使用 Aspose.Cells for JavaScript 通过 C++ 以编程方式操控。本文件概述了如何有效管理这些设置。

## **可能的使用场景**
以下场景说明何时可能需要管理工作簿设置：
- 调整显示选项
- 设置计算模式
- 配置页面设置参数

## **使用 Aspose.Cells for JavaScript 通过 C++ 管理工作簿设置**
本示例演示如何管理诸如计算选项和显示设置的工作簿参数。

1. 创建新工作簿或加载现有工作簿。
2. 根据需求修改工作簿设置。
3. 保存工作簿以保存更改。

### **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Workbook Settings Example</h1>
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
            // Create a new workbook
            const workbook = new Workbook();

            // Access the settings of the workbook
            const settings = workbook.settings;
            settings.calculationMode = 1; // Manual calculation

            // Display options
            settings.showGridLines = false; // Disable gridlines

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'WorkbookSettingsExample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **关键工作簿设置属性与方法**
Aspose.Cells for JavaScript 通过 C++ 提供许多属性和方法来调整工作簿设置：
- **Workbook.settings**：访问工作簿的设置。
- **Settings.calculationMode**：设置工作簿的计算模式。
- **Settings.showGridLines**：启用或禁用显示的网格线。

## **结论**
在 Aspose.Cells for JavaScript 通过 C++ 中管理工作簿设置简单方便，并提供多种选项来自定义Excel文件的行为。利用这些设置，您可以根据具体需求定制工作簿。
