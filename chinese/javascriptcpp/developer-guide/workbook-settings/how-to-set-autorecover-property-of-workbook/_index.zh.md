---
title: 如何通过 C++ 和 JavaScript 设置工作簿的自动恢复属性
linktitle: 如何设置工作簿的AutoRecover属性
type: docs
weight: 220
url: /zh/javascript-cpp/how-to-set-autorecover-property-of-workbook/
description: 学习如何使用 Aspose.Cells for JavaScript 通过 C++ 设置工作簿的自动恢复属性。
---

{{% alert color="primary" %}}  
你可以使用Aspose.Cells设置工作簿的AutoRecover属性。该属性的默认值为**true**。当你将其设置为**false**时，Microsoft Excel会禁用该Excel文件的自动恢复（自动保存）功能。  

Aspose.Cells提供了[**Workbook.autoRecover**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#autoRecover--)属性来启用或禁用此选项。  
{{% /alert %}}  

以下代码说明了如何使用工作簿的[**Workbook.autoRecover**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#autoRecover--)属性。代码先读取该属性的默认值（为**true**），然后将其设置为**false**并保存工作簿。再一次读取工作簿时，该属性的值为**false**。  

## 通过 JavaScript 设置工作簿的自动恢复属性的代码示例  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - AutoRecover</title>
    </head>
    <body>
        <h1>AutoRecover Property Example</h1>
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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            // Create workbook object
            const workbook = new Workbook();

            // Read AutoRecover property
            const autoRecoverBefore = workbook.settings.autoRecover;
            resultDiv.innerHTML += `<p>AutoRecover before: ${autoRecoverBefore}</p>`;

            // Set AutoRecover property to false
            workbook.settings.autoRecover = false;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download output_out.xlsx';

            // Read the saved workbook again from the saved data
            const workbook2 = new Workbook(new Uint8Array(outputData));

            // Read AutoRecover property
            const autoRecoverAfter = workbook2.settings.autoRecover;
            resultDiv.innerHTML += `<p>AutoRecover after reload: ${autoRecoverAfter}</p>`;
        });
    </script>
</html>
```  

## **输出**  



{{< highlight java >}}  
AutoRecover: True  
AutoRecover: False  
{{< /highlight >}}
