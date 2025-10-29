---
title: 使用JavaScript通过C++禁用Excel中的兼容性检查器
linktitle: 在Excel中禁用兼容性检查程序
type: docs
weight: 170
url: /zh/javascript-cpp/disable-compatibility-checker-in-excel/
description: 学习如何通过Aspose.Cells for JavaScript通过C++ API禁用兼容性检查器。
keywords: JavaScript 禁用兼容性检查器，Excel 在 JavaScript 中通过 C++ 禁用兼容性检查器，禁用工作簿中的兼容性检查器。
---

## 在 JavaScript 中禁用 Excel 工作表的兼容性检查器  

{{% alert color="primary" %}}  
Microsoft Excel的兼容性检查器在将文件保存为较早文件格式时可能会出现功能问题或保真度丢失。 兼容性检查器是Microsoft Office Excel 2007和Microsoft Excel 2010的功能。  

当您从Excel 2007或Excel 2010将工作簿保存在较早的版本中（Excel 97至Excel 2003），兼容性检查程序将扫描工作簿，以查看它是否包含较早版本不支持的功能。为了帮助您决定如何处理兼容性问题，兼容性检查程序显示带有选项的对话框。它还可用于创建有关工作簿中任何问题的报告，或者禁用该功能。  

有时，你需要为特定的电子表格禁用兼容性检查器。通过Aspose.Cells的API，你可以以编程方式实现此功能，避免用户在手动在Microsoft Excel中重新保存文件时弹出兼容性检查器对话框带来的困扰或困惑。  
{{% /alert %}}  

## **如何使用Microsoft Excel禁用兼容性检查器**  

要在Microsoft Excel中禁用兼容性检查程序（例如Microsoft Excel 2007/2010）：  

- （Excel 2007）在办公按钮上，单击**准备**，然后单击**运行兼容性检查**，然后清除**保存此工作簿时检查兼容性**选项。  
- （Excel 2010）单击“文件”选项卡，然后单击**信息**，再单击“检查问题”，再单击“检查兼容性”，最后清除“保存此工作簿时检查兼容性”选项。  

## **如何使用Aspose.Cells API禁用兼容性检查器**  

将[**Workbook.checkCompatibility**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#checkCompatibility--)属性设置为**false**以禁用Microsoft Excel的兼容性检查器。  

### **代码示例**  

以下示例代码演示如何通过 C++ 使用 Aspose.Cells for JavaScript 来禁用兼容性检查器。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Disable Compatibility Checker Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Disable the compatibility checker
            workbook.settings.checkCompatibility = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_BK_CompCheck.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Compatibility check disabled. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
