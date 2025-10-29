---
title: 基于单元格引用插入图片，使用JavaScript通过C++
linktitle: 基于单元格引用插入图片
type: docs
weight: 150
url: /zh/javascript-cpp/insert-a-picture-based-on-cell-reference/
description: 学习如何基于单元格引用在工作表中插入图片，使用Aspose.Cells for JavaScript通过C++。显示单元格中的数据在图片中。
---

{{% alert color="primary" %}}
有时您会有一张空白图片，并且需要通过在公式栏中设置单元格引用来显示图片中的数据或内容。Aspose.Cells支持此功能（Microsoft Excel 2010）。
{{% /alert %}}

## 根据单元格引用插入图片

Aspose.Cells for JavaScript通过C++支持在图片形状中显示工作表单元格的内容。你可以将图片链接到包含你想显示的数据的单元格。由于单元格或单元格区域与图形对象链接，修改该单元格或区域中的数据会自动显示在图形对象中。通过调用[**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-)方法，将图片添加到工作表中（封装在[**ShapeCollection**](https://reference.aspose.com/cells/javascript-cpp/shapecollection)集合中，属于[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)对象）。使用[**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture)对象的[**Picture.formula**](https://reference.aspose.com/cells/javascript-cpp/picture/#formula--)属性指定单元格区域。

### 代码示例

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Referenced Picture Example</h1>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();
            // Get the first worksheet's cells collection
            const cells = workbook.worksheets.get(0).cells;

            // Add string values to the cells
            cells.get("A1").value = "A1";
            cells.get("C10").value = "C10";

            // Get the conditional icon's image data
            const imagedata = AsposeCells.ConditionalFormattingIcon.iconImageData(AsposeCells.IconSetType.TrafficLights31, 0);
            // Create a stream based on the image data
            const stream = Uint8Array.from(imagedata);

            // Add a blank picture to the D1 cell
            const pic = workbook.worksheets.get(0).shapes.addPicture(0, 3, stream, 10, 10);
            // Specify the formula that refers to the source range of cells
            pic.formula = "A1:C10";
            // Update the shapes selected value in the worksheet
            workbook.worksheets.get(0).shapes.updateSelectedValue();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'referencedpicture.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
