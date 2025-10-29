---
title: Работа с данными в нелегPrimitive форме с помощью JavaScript через C++
linktitle: Данные в не примитивной форме
type: docs
weight: 300
url: /ru/javascript-cpp/data-in-non-primitive-shape/
description: Узнайте, как получать доступ и управлять нелег Primitive формами в Aspose.Cells for JavaScript через C++.
---

## **Доступ к данным не примитивной формы**  

Иногда вам может потребоваться получить доступ к данным из формы, которая не встроена. Встроенные формы называют примитивными, а те, которых нет, называют не примитивными. Например, вы можете определить свои собственные формы, используя разные кривые соединенные линии.  

## **Форма не примитивной формы**  

В Aspose.Cells for JavaScript через C++ нелег Primitive формы имеют тип [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/javascript-cpp/autoshapetype/). Вы можете проверить их тип с помощью свойства [**Shape.autoShapeType**](https://reference.aspose.com/cells/javascript-cpp/shape/#autoShapeType--).  

Доступ к данным фигуры с помощью свойства [**Shape.paths**](https://reference.aspose.com/cells/javascript-cpp/shape/#paths--). Оно возвращает все связанные пути, составляющие нел primitives фигуру. Эти пути типа [**ShapePath**](https://reference.aspose.com/cells/javascript-cpp/shapepath), которые содержат список всех сегментов, каждый из которых содержит точки.  

|**Показывает пример нетипичной формы**|  
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
