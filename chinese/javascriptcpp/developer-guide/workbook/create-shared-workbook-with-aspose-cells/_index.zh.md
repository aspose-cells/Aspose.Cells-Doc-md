---
title: 使用Aspose.Cells for JavaScript通过C++创建共享工作簿
linktitle: 使用Aspose.Cells创建共享工作簿
type: docs
weight: 40
url: /zh/javascript-cpp/create-shared-workbook-with-aspose-cells/
description: 学习如何使用Aspose.Cells for JavaScript通过C++创建共享工作簿。
---

## **可能的使用场景**  

 Microsoft Excel允许你将工作簿作为共享，如以下截图所示。当你共享工作簿时，多个用户可以在网络上编辑工作簿。Aspose.Cells for JavaScript通过C++可以让你使用[**WorkbookSettings.shared**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#shared--)属性创建共享工作簿。  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **使用Aspose.Cells创建共享工作簿**  

以下示例代码通过将[**WorkbookSettings.shared**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#shared--)属性设置为**true**，创建一个共享工作簿。当您在Microsoft Excel中打开[输出Excel文件](55541786.xlsx)时，您将看到**共享**与输出工作簿的名称，如截图所示。  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **示例代码**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Shared Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="createShared" disabled>Create Shared Workbook</button>
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
            document.getElementById('createShared').disabled = false;
        });

        document.getElementById('createShared').addEventListener('click', async () => {
            const wb = new Workbook();

            // Share the Workbook (converted getter/setter to property)
            wb.settings.shared = true;

            // Save the Shared Workbook
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSharedWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Shared Workbook';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shared workbook created successfully! Click the download link to save the file.</p>';
        });
    </script>
</html>
```
