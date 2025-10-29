---
title: 用JavaScript通过C++操作非原始形状的数据
linktitle: 非基本形状中的数据
type: docs
weight: 300
url: /zh/javascript-cpp/data-in-non-primitive-shape/
description: 学习如何访问和操作Aspose.Cells for JavaScript中的非原始形状。
---

## **访问非基本形状的数据**  

有时，您需要访问非内置形状的形状的数据。内置形状称为基本形状；而不是内置形状的称为非基本形状。例如，您可以使用不同的曲线连接线定义自己的形状。  

## **非基本形状**  

在 Aspose.Cells for JavaScript 通过 C++，非原始形状被赋予类型 [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/javascript-cpp/autoshapetype/)。您可以使用 [**Shape.autoShapeType**](https://reference.aspose.com/cells/javascript-cpp/shape/#autoShapeType--) 属性检查它们的类型。  

使用 [**Shape.paths**](https://reference.aspose.com/cells/javascript-cpp/shape/#paths--) 属性访问形状数据。它返回构成非原始形状的所有连接路径。这些路径的类型是 [**ShapePath**](https://reference.aspose.com/cells/javascript-cpp/shapepath)，包含一个段落列表，每个段落包含该段中的点。  

|**显示了非原始形状的示例**|  
| :- |  
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Non-Primitive Shape Paths Example</title>
    </head>
    <body>
        <h1>Non-Primitive Shape Paths Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, Utils } = AsposeCells;

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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);

            // Accessing the user defined shape
            const shape = worksheet.shapes.get(0);

            if (shape.autoShapeType === AsposeCells.AutoShapeType.NotPrimitive) 
            {
                // Access shape's data
                const shapePathCollection = shape.paths;

                // Build output
                let outputHtml = '<div><strong>Shape Path Points:</strong><br/><pre style="white-space: pre-wrap;">';

                // Access information of individual path
                for (let i = 0; i < shapePathCollection.count; i++) 
                {
                    const shapePath = shapePathCollection.get(i);
                    // Access path segment list
                    const pathSegments = shapePath.pathSegementList;

                    // Access individual path segment
                    for (let j = 0; j < pathSegments.count; j++)
                    {
                        const pathSegment = pathSegments.get(j);
                        // Gets the points in path segment
                        const segmentPoints = pathSegment.points;

                        for (let k = 0; k < segmentPoints.count; k++) 
                        {
                            const pathPoint = segmentPoints.get(k);
                            outputHtml += "X: " + pathPoint.x + ", Y: " + pathPoint.y + "\n";
                        }
                    }
                }

                outputHtml += '</pre></div>';
                document.getElementById('result').innerHTML = outputHtml;
            } else {
                document.getElementById('result').innerHTML = '<p>Shape is not a NonPrimitive auto-shape.</p>';
            }
        });
    </script>
</html>
```
