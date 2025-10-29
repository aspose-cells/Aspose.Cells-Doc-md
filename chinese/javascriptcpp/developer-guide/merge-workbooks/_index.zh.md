---
title: 使用JavaScript via C++将多个工作簿合并为一个工作簿
linktitle: 工作簿合并器
type: docs
weight: 66
url: /zh/javascript-cpp/combine-multiple-workbooks-into-a-single-workbook/
description: 学习如何使用Aspose.Cells for JavaScript通过C++将多个工作簿合并为一个工作簿。 
---

{{% alert color="primary" %}}

有时，您需要将包含图片、图表和数据等内容的多个工作簿合并到一个工作簿中。Aspose.Cells for JavaScript通过C++支持此功能。本文展示如何创建控制台应用程序，并使用Aspose.Cells用几行简单的代码合并工作簿。

{{% /alert %}}

## **将具有图像和图表的工作簿合并**

该示例代码使用Aspose.Cells for JavaScript通过C++将两个工作簿合并为一个工作簿。代码加载源工作簿，使用[**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#combine-workbook-)方法将它们合并，然后保存输出的工作簿。

### **源工作簿**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **输出工作簿**

- [combined.xlsx](5473095.xlsx)

### **屏幕截图**

以下是源和输出工作簿的屏幕截图。

{{% alert color="primary" %}}

您可以使用任何源工作簿。这些图像仅用于说明目的。

{{% /alert %}}

**图表工作簿的第一个工作表 - 堆叠** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**图表工作簿的第二个工作表 - 折线** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**图片工作簿的第一个工作表 - 图片** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**组合工作簿中的三个工作表 - 堆叠、线条、图片** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Combine Workbooks Example</title>
    </head>
    <body>
        <h1>Combine Workbooks Example</h1>
        <p>Select two Excel files to combine:</p>
        <input type="file" id="fileInput1" accept=".xls,.xlsx" />
        <input type="file" id="fileInput2" accept=".xls,.xlsx" />
        <button id="runExample">Combine Workbooks</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            const fileInput1 = document.getElementById('fileInput1');
            const fileInput2 = document.getElementById('fileInput2');

            if (!fileInput1.files.length || !fileInput2.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select two Excel files.</p>';
                return;
            }

            const file1 = fileInput1.files[0];
            const file2 = fileInput2.files[0];

            const arrayBuffer1 = await file1.arrayBuffer();
            const arrayBuffer2 = await file2.arrayBuffer();

            // Open the first excel file.
            const sourceBook1 = new Workbook(new Uint8Array(arrayBuffer1));

            // Open the second excel file.
            const sourceBook2 = new Workbook(new Uint8Array(arrayBuffer2));

            // Combining the two workbooks
            sourceBook1.combine(sourceBook2);

            // Save the combined workbook and provide download link
            const outputData = sourceBook1.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Combined.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Combined Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbooks combined successfully! Click the download link to get the combined file.</p>';
        });
    </script>
</html>
```

## **高级主题**
- [将多个工作表合并成一个工作表](/cells/zh/javascript-cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [合并文件](/cells/zh/javascript-cpp/merge-files/)
