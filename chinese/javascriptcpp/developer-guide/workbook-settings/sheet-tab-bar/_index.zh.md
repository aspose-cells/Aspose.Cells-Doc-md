---
title: 如何通过 JavaScript 和 C++ 控制工作表标签栏
linktitle: 如何控制选项卡工具栏
type: docs
weight: 600
url: /zh/javascript-cpp/how-to-control-sheet-tab-bar/
description: 学习如何使用 Aspose.Cells for JavaScript 通过 C++ 控制工作表标签栏。
keywords: 如何通过 C++ 操作 JavaScript 控制工作表标签栏，设置工作表标签栏，控制工作表标签栏 JavaScript。  
---

## **可能的使用场景**  
当你需要调整 Excel 表格栏的显示时，需要了解如何控制工作表标签栏，例如隐藏或显示工作表标签栏、改变标签栏宽度、指定第一个可见标签等。 Aspose.Cells for JavaScript 通过 C++ 支持这些功能。Aspose.Cells 提供以下属性和方法帮助你实现目标。

- [**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--)
- [**WorkbookSettings.sheetTabBarWidth**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#sheetTabBarWidth--)
- [**WorkbookSettings.firstVisibleTab**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#firstVisibleTab--)

## **如何通过 Aspose.Cells for JavaScript 通过 C++ 控制工作表标签栏**  
此示例演示如何：

1. 创建一个工作簿。
1. 在第一个工作表中的单元格中添加数据。
1. 显示工作表标签并设置标签栏的宽度。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Populate Worksheet and Save</h1>
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
            const resultDiv = document.getElementById('result');

            // If a file is provided, load it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells (converted putValue -> value assignment)
            let cell = cells.get("A1");
            cell.value = "Fruit";
            cell = cells.get("B1");
            cell.value = "Count";
            cell = cells.get("C1");
            cell.value = "Price";

            cell = cells.get("A2");
            cell.value = "Apple";
            cell = cells.get("A3");
            cell.value = "Mango";
            cell = cells.get("A4");
            cell.value = "Blackberry";
            cell = cells.get("A5");
            cell.value = "Cherry";

            // Display the sheet tab and set the width of the tab bar (converted getters/setters -> properties)
            workbook.settings.showTabs = true;
            workbook.settings.sheetTabBarWidth = 150;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

结果文件预览：  
<br>  
<image src="result.png" width="70%" />
