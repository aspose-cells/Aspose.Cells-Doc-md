---
title: JavaScriptを使用した非プリミティブ形状のデータ操作（C++経由）
linktitle: 非原始の形のデータ
type: docs
weight: 300
url: /ja/javascript-cpp/data-in-non-primitive-shape/
description: C++経由のAspose.Cells for JavaScriptで、非プリミティブ形状にアクセスし操作する方法を学びます。
---

## **非原始の形のデータへのアクセス**  

時々、ビルトインでない形状からデータにアクセスする必要があります。ビルトインの形状は原始形状と呼ばれ、そうでないものは非原始形状と呼ばれます。例えば、異なる曲線接続線を使用して独自の形状を定義することができます。  

## **非原始の形状**  

C++経由のAspose.Cells for JavaScriptでは、非プリミティブ形状は[**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/javascript-cpp/autoshapetype/)型と割り当てられます。[**Shape.autoShapeType**](https://reference.aspose.com/cells/javascript-cpp/shape/#autoShapeType--)プロパティを使用してその型を確認できます。  

[**Shape.paths**](https://reference.aspose.com/cells/javascript-cpp/shape/#paths--)プロパティを使用してシェイプデータにアクセスします。これにより、非プリミティブシェイプを構成するすべての接続されたパスが取得できます。これらのパスは[**ShapePath**](https://reference.aspose.com/cells/javascript-cpp/shapepath)タイプであり、すべてのセグメントのリストを保持し、それぞれのセグメントにはポイントが含まれています。  

|**非原始の形状の例を示す**|  
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
