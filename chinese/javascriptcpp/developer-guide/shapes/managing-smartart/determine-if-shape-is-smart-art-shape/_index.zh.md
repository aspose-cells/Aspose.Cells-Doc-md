---
title: 使用JavaScript通过C++判断Shape是否为Smart Art Shape
linktitle: 确定形状是否为智能图形
type: docs
weight: 400
url: /zh/javascript-cpp/determine-if-shape-is-smart-art-shape/
description: 学习如何使用Aspose.Cells for Java脚本通过C++判断Excel中的形状是否为Smart Art
---

## **可能的使用场景**  

智能艺术形状是Microsoft Excel中的特殊形状，允许你自动创建复杂的图表。你可以使用[**Shape.isSmartArt()**](https://reference.aspose.com/cells/javascript-cpp/shape/#isSmartArt--)属性判断形状是智能艺术形状还是普通形状。  

## **确定形状是否为智能图形**  

以下示例代码加载包含智能艺术形状的[示例Excel文件](55541792.xlsx)，如截图所示。然后它打印第一个形状的[**Shape.isSmartArt()**](https://reference.aspose.com/cells/javascript-cpp/shape/#isSmartArt--)属性值，请查看示例代码控制台输出。  

![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)  

## **示例代码**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first shape
            const shape = worksheet.shapes.get(0);

            // Determine if shape is smart art (converted to property access)
            const isSmartArt = shape.isSmartArt;

            document.getElementById('result').innerHTML = `<p>Is Smart Art Shape: ${isSmartArt}</p>`;
        });
    </script>
</html>
```  

## **控制台输出**  

{{< highlight java >}}  

Is Smart Art Shape: True  

{{< /highlight >}}
