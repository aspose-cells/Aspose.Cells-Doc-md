---
title: 设置工作簿的公式计算模式通过JavaScript用C++
linktitle: 设置工作簿的公式计算模式
description: 本文介绍如何用Aspose.Cells for JavaScript通过C++设置Microsoft Excel中工作簿的公式计算模式。通过加载现有Excel文件或创建新文件，使用Aspose.Cells提供的属性设置公式计算模式并获得结果，最后保存修改后的Excel文件。
keywords: Aspose.Cells，Excel，工作簿，公式计算模式，设置，JavaScript通过C++
type: docs
weight: 110
url: /zh/javascript-cpp/setting-formula-calculation-mode-of-workbook/
---

{{% alert color="primary" %}}  
Microsoft Excel允许您设置公式计算模式，即公式计算的方式。有三种可能的值：  

- 自动 - 每当有变更时重新计算，并且每次打开工作簿时。  
- 自动除数据表外 - 每当有变更时重新计算，但是不包括数据表。  
- 手动 - 仅当用户通过按F9或CTRL+ALT+F9明确请求时，或者保存工作簿时重新计算。  
{{% /alert %}}  

在Microsoft Excel中设置公式计算模式：  

1. 选择**公式**然后**计算选项**。  
1. 选择其中一个选项。  

Aspose.Cells for JavaScript通过C++还允许您使用[**FormulaSettings.calculationMode**](https://reference.aspose.com/cells/javascript-cpp/formulasettings/#calculationMode--)模式属性设置**公式计算模式**。您可以将其赋值为具有以下值之一的[**CalcModeType**](https://reference.aspose.com/cells/javascript-cpp/calcmodetype)枚举：  

- CalcModeType.Automatic  
- CalcModeType.AutomaticExceptTable  
- CalcModeType.Manual  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            // Creating a workbook
            const workbook = new Workbook();

            // Set the Formula Calculation Mode to Manual
            workbook.settings.formulaSettings.calculationMode = AsposeCells.CalcModeType.Manual;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
