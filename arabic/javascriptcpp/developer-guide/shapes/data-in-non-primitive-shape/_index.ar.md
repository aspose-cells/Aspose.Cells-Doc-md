---
title: البيانات في الشكل غير الأساسي باستخدام جافا سكريبت عبر ++C
linktitle: البيانات في شكل غير الذي يتميز ببساطة
type: docs
weight: 300
url: /ar/javascript-cpp/data-in-non-primitive-shape/
description: تعلم كيفية الوصول إلى الأشكال غير الأساسية والتلاعب بها في Aspose.Cells for Javaسكريبت عبر ++C.
---

## **الوصول إلى بيانات الشكل غير الذي يتميز ببساطة**  

في بعض الأحيان، تحتاج إلى الوصول إلى البيانات من شكل ليس مدمجًا. يطلق على الأشكال المدمجة ، الأشكال الأساسية ، ويطلق على الأشكال التي ليست كذلك ، الأشكال غير الأساسية. على سبيل المثال، يمكنك تحديد أشكالك الخاصة باستخدام خطوط متصلة مختلفة.  

## **الشكل غير الأساسي**  

في Aspose.Cells for Javaسكريبت عبر ++C، تُعيّن الأشكال غير الأساسية على أنها [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/javascript-cpp/autoshapetype/). يمكنك التحقق من نوعها باستخدام خاصية [**Shape.autoShapeType**](https://reference.aspose.com/cells/javascript-cpp/shape/#autoShapeType--).  

الوصول إلى بيانات الشكل باستخدام خاصية [**Shape.paths**](https://reference.aspose.com/cells/javascript-cpp/shape/#paths--). وتُرجع كافة المسارات المرتبطة التي تتكون منها الشكل غير البدائي. هذه المسارات من النوع [**ShapePath**](https://reference.aspose.com/cells/javascript-cpp/shapepath) وتحتوي على قائمة بجميع القطاعات التي تحتوي بدورها على النقاط في كل قطاع.  

|**يظهر مثالًا على شكل غير أساسي**|  
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
