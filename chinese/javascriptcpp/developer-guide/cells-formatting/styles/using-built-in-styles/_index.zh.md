---
title: 使用内置样式
linktitle: 使用内置样式
type: docs
weight: 80
url: /zh/javascript-cpp/using-built-in-styles/
description: 使用 JavaScript 结合 Aspose.Cells for JavaScript 通过 C++ 使用 Excel 内置样式的代码。
keywords: JavaScript 使用 Excel 内置样式，JavaScript 编程方式应用样式到工作簿，编程应用样式到工作簿，JavaScript 在 Excel 中应用内置样式，JavaScript 在工作簿中应用内置样式，JavaScript 代码应用内置样式到工作簿，JavaScript 代码在 Excel 工作簿中应用内置样式。
---

{{% alert color="primary" %}}  
Aspose.Cells提供了一个大量的可重复使用的样式集合，用于对电子表格文档中的单元格进行格式化。我们可以在工作簿中使用内置样式，也可以创建自定义样式。  
{{% /alert %}}  

## **如何使用内置样式**  

方法 [**Workbook.createBuiltinStyle(BuiltinStyleType)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#createBuiltinStyle-builtinstyletype-) 和枚举 [**BuiltinStyleType**](https://reference.aspose.com/cells/javascript-cpp/builtinstyletype) 使使用内置样式变得更加方便。以下是所有可能的内置样式列表:  

- TwentyPercentAccent1
- TwentyPercentAccent2
- TwentyPercentAccent3
- TwentyPercentAccent4
- TwentyPercentAccent5
- TwentyPercentAccent6
- FortyPercentAccent1
- FortyPercentAccent2
- FortyPercentAccent3
- FortyPercentAccent4
- FortyPercentAccent5
- FortyPercentAccent6
- SixtyPercentAccent1
- SixtyPercentAccent2
- SixtyPercentAccent3
- SixtyPercentAccent4
- 六成口音5
- 六成口音6
- 口音1
- 口音2
- 口音3
- 口音4
- 口音5
- 口音6
- 不良
- 计算
- 检查单元格
- 逗号
- 逗号1
- 货币
- 货币1
- 说明文本
- 好
- 标题1
- 标题2
- 标题3
- 标题4
- 超链接
- 后缀超链接
- 输入
- 链接单元格
- 中性
- 正常
- 注释
- 输出
- 百分比
- 标题
- 总计
- 警告文本
- 行级别
- 列级别


## JavaScript 代码使用内置样式  
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
        <a id="downloadLink1" style="display: none; margin-right: 10px;">Download Output.xlsx</a>
        <a id="downloadLink2" style="display: none;">Download Output.out.ods</a>
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

        document.getElementById('runExample').addEventListener('click', () => {
            // Creating a new Workbook
            const workbook = new Workbook();

            // Creating a built-in style (Title)
            const style = workbook.createBuiltinStyle(AsposeCells.BuiltinStyleType.Title);

            // Accessing first worksheet, its cells, and cell A1
            const worksheet = workbook.worksheets.get(0);
            const cell = worksheet.cells.get("A1");

            // Setting cell value and style (converted setter)
            cell.putValue("Aspose");
            cell.style = style;

            // Auto-fit column and row
            worksheet.autoFitColumn(0);
            worksheet.autoFitRow(0);

            // Save as XLSX
            const outputData1 = workbook.save(SaveFormat.Xlsx);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'Output.xlsx';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download Output.xlsx';

            // Save as ODS
            const outputData2 = workbook.save(SaveFormat.Ods);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'Output.out.ods';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download Output.out.ods';

            document.getElementById('result').innerHTML = '<p style="color: green;">Files generated. Click the download links to save them.</p>';
        });
    </script>
</html>
```
