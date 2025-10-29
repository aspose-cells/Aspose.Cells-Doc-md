---
title: 如何旋转单元格文本
linktitle: 如何旋转单元格文本  
type: docs  
weight: 80  
url: /zh/javascript-cpp/how-to-rotate-text-of-cell/  
description: 学习如何使用 Aspose.Cells for JavaScript 通过 C++ 来编程旋转单元格中的文本。  
keywords: JavaScript 通过 C++ 旋转工作簿中单元格的文本，编程方式设置工作簿中单元格的旋转角度，JavaScript 如何在 Excel 中旋转单元格的文本。  
---

## **在 Aspose.Cells for JavaScript 通过 C++ 中旋转单元格文本。**

Aspose.Cells 是一个功能强大的 JavaScript 组件，允许开发者以编程方式操作 Excel 电子表格。Aspose.Cells 提供的功能之一是旋转单元格，可以自定义文本的方向，提升数据的视觉表现。在本文档中，我们将介绍如何使用 Aspose.Cells 旋转单元格。

## **如何在Excel中旋转单元格中的文本**
要在Excel中旋转单元格，您可以按照以下步骤操作：
1. 打开Excel并选择您要旋转的单元格或单元格范围。
1. 右键单击所选单元格，并从上下文菜单中选择“格式单元格”。或者，您还可以在Excel功能区中的“主页”选项卡中，单击“单元格”组中的“格式”下拉菜单，然后选择“格式单元格”。
1. 在“格式单元格”对话框中，转到“对齐”选项卡。
1. 在“方向”部分下，您将看到旋转文本的选项。您可以直接在“度数”框中输入所需的旋转角度。正值逆时针旋转文本，负值顺时针旋转文本。
<br>
![todo:image_alt_text](alignment.png)
1. 选择所需的旋转后，单击“确定”以应用更改。所选单元格现在将根据您选择的旋转角度或方向进行旋转。

## **如何使用Aspose.Cells API旋转单元格文本**

[**Style.rotationAngle(number)**](https://reference.aspose.com/cells/javascript-cpp/style/#rotationAngle-number-)属性使旋转单元格更加方便。要在Aspose.Cells中旋转单元格，您需要按照以下步骤操作：
1. 加载Excel工作簿  
<br>
首先，您需要使用Aspose.Cells加载Excel工作簿。您可以使用Workbook类打开现有的Excel文件或创建新文件。 

1. 访问工作表  
<br>
加载工作簿后，您需要访问要旋转单元格的工作表。您可以通过索引或名称访问工作表。 

1. 旋转单元格文本  
<br>
现在您已经可以访问工作表，就可以通过修改所需单元格的样式对象来旋转单元格。样式对象允许您设置各种格式选项，包括旋转。 

1. 保存工作簿  
<br>
旋转单元格后，您可以使用Save方法将修改后的工作簿保存回文件或流。

## **JavaScript 示例代码**

请参阅以下代码，它创建了一个工作簿对象，并为多个单元格设置不同的旋转角度。截图显示了示例代码执行后的结果。
<br>
<img src="rotation.png" width=80% />

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Rotate Text in Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
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

        document.getElementById('runExample').addEventListener('click', async () => {
            // Creating a new Workbook (blank)
            const workbook = new Workbook();

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Row index of the cell
            let row = 0;
            // Column index of the cell
            let column = 0; 

            let a1 = worksheet.cells.get(row, column);
            a1.putValue("a1 rotate text");
            let a1Style = a1.style;

            // Set the rotation angle in degrees
            a1Style.rotationAngle = 45; 
            a1.style = a1Style;

            // set Column index of the cell
            column = 1;
            let b1 = worksheet.cells.get(row, column);
            b1.putValue("b1 rotate text");
            let b1Style = b1.style;

            // Set the rotation angle in degrees
            b1Style.rotationAngle = 255;
            b1.style = b1Style;

            // set Column index of the cell
            column = 2;
            let c1 = worksheet.cells.get(row, column);
            c1.putValue("c1 rotate text");
            let c1Style = c1.style;

            // Set the rotation angle in degrees
            c1Style.rotationAngle = -90;
            c1.style = c1Style;

            // set Column index of the cell
            column = 3;
            let d1 = worksheet.cells.get(row, column);
            d1.putValue("d1 rotate text");
            let d1Style = d1.style;

            // Set the rotation angle in degrees
            d1Style.rotationAngle = -90;
            d1.style = d1Style;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
