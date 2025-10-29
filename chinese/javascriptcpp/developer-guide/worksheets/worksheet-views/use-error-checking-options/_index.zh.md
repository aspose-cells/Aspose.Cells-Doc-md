---
title: 使用 C++ 的 JavaScript 错误检查选项
linktitle: 使用错误检查选项
type: docs
weight: 140
url: /zh/javascript-cpp/use-error-checking-options/
description: 学习如何在 Excel 工作表中通过 C++ 编程方式使用错误检查选项。
keywords: 在 Excel 中使用 JavaScript 通过 C++ 将号码存储为文本，错误检查 Excel 选项 JavaScript 通过 C++
---

{{% alert color="primary" %}}  
Microsoft Excel允许用户定义错误检查选项和规则。当创建公式时，用户通常会看到错误检查，单元格右上角的小三角形突出显示当单元格存在问题时。Excel提供帮助用户纠正常见问题的信息。  
{{% /alert %}}  

## **错误类型**  

 表示公式无法返回结果的错误（如将数字除以零）需要立即处理，会在单元格中显示错误值。点击绿色三角会显示感叹号，点击会打开选项列表。  

 可以使用选项解决错误或忽略。忽略错误意味着该错误在后续错误检查中不会再次显示。  

 Aspose.Cells提供错误检查选项功能。[**ErrorCheckOption**](https://reference.aspose.com/cells/javascript-cpp/errorcheckoption)类管理不同类型的错误检查，例如，将文本存储的数字、公式计算错误和验证错误。使用[**ErrorCheckType**](https://reference.aspose.com/cells/javascript-cpp/errorchecktype)枚举设置所需的错误检查。  

## **作为文本存储的数字**  

有时，数字可能被格式化并作为文本存储在单元格中。这可能会导致计算出现问题或产生令人困惑的排序顺序。格式为文本的数字在单元格中是左对齐而不是右对齐的。如果应执行单元格上的公式未返回值，则检查公式引用的单元格中的对齐方式 - 可能是其中一些或全部的单元格被格式为文本。  

可以使用错误检查选项快速将作为文本存储的数字转换为实际数字。在Microsoft Excel 2003中：  

1. 在“工具”菜单上，单击“选项”。  
1. 选择“错误检查”选项卡。  
   **将作为文本存储的数字** 选项默认为选中状态。  
1. 取消其选中状态。  

以下示例代码显示如何使用Aspose.Cells APIs在模板XLS文件中禁用工作表中的文本存储的数字错误检查选项。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Error Check Options</title>
    </head>
    <body>
        <h1>Error Check Options Example</h1>
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

            // Instantiate a Workbook by reading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Instantiate the error checking options
            const opts = sheet.errorCheckOptions;

            const index = opts.add();
            const opt = opts.get(index);
            // Disable the numbers stored as text option
            // Converted from opt.setErrorCheck(type, value) to a property-style assignment
            opt.errorCheck = opt.errorCheck || {};
            opt.errorCheck[AsposeCells.ErrorCheckType.NumberStoredAsText] = false;
            // Set the range
            opt.addRange(AsposeCells.CellArea.createCellArea(0, 0, 1000, 50));

            // Save the Excel file and prepare download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_test.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
