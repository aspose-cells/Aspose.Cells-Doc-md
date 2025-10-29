---
title: 如何防止用户用JavaScript通过C++打印Excel文件
linktitle: 如何防止用户打印Excel文件
type: docs
weight: 600
url: /zh/javascript-cpp/how-to-prevent-printing-excel/
description: 学习如何使用Aspose.Cells for JavaScript通过C++阻止用户打印Excel文件。
keywords: excel打印、防止excel打印、如何防止用户打印excel、excel防止打印、防止打印工作簿、使用VBA阻止用户打印整个工作簿
---

## **可能的使用场景**  
在日常工作中，Excel文件中可能包含一些重要信息；为了防止内部数据传播，公司不会允许我们打印。这份文件将告诉你如何阻止他人打印Excel文件。  

## **如何防止用户在MS-Excel中打印文件**  
您可以应用以下VBA代码以保护您的特定文件不被打印。  
1. 打开您不允许他人打印的工作簿。  
1. 在Excel功能区选择“开发者”标签，然后点击“控件”中的“查看代码”按钮。或者，您可以按下ALT + F11键打开Microsoft Visual Basic for Applications窗口。  
<br>  
<img src="1.png" width=70% />  
1. 然后在左侧项目资源管理器中，双击ThisWorkbook以打开模块，并添加一些VBA代码。  
<br>  
<img src="2.png" width=70% />  
1. 保存并关闭代码，返回到工作簿，现在当您打印示例文件时，将不允许打印，并会显示以下警告框：  
<br>  
<img src="3.png" width=70% />  

## **用Aspose.Cells for JavaScript通过C++防止用户打印Excel文件的方法**  

以下示例代码说明如何防止用户打印Excel文件：  

1. 加载[示例文件](sample.xlsx)。  
1. 从工作簿的VbaProject属性获取VbaModuleCollection对象。  
1. 通过"ThisWorkbook"名称获取VbaModule对象。  
1. 设置VbaModule的代码属性。  
1. 将示例文件保存为[xlsm格式](out.xlsm)。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Update VBA Module Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm" />
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

            // Accessing VBA project and its modules
            const modules = workbook.vbaProject.modules;
            const module = modules.get("ThisWorkbook");

            // Setting module codes (converted from setCodes -> codes assignment)
            module.codes = "Private Sub Workbook_BeforePrint(Cancel As Boolean)\r\n  Cancel = True\r\n  MsgBox \"Refusing to print in paperless office\"\r\nEnd Sub\r\n";

            // Saving the modified workbook as macro-enabled workbook
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">VBA module updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
