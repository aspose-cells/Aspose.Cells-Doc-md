---
title: C++ ile JavaScript üzerinden Primitif Olmayan Şekil Verilerinin Yerlestirilmesi
linktitle: Non Primitive Şekildeki Veri
type: docs
weight: 300
url: /tr/javascript-cpp/data-in-non-primitive-shape/
description: C++ ile Aspose.Cells for JavaScript üzerinden primitif olmayan şekillere nasıl erişeceğinizi ve onları nasıl manipüle edeceğinizi öğrenin.
---

## **Basit olmayan Şeklin Verilerine Erişmek**  

Bazı durumlarda, yerleşik olmayan bir şekilden veriye erişmeniz gerekebilir. Yerleşik şekiller basit şekiller olarak adlandırılırken, diğerleri basit olmayan şekiller olarak adlandırılır. Örneğin, farklı eğri bağlantılı çizgiler kullanarak kendi şekillerinizi tanımlayabilirsiniz.  

## **Basit Olmayan Bir Şekil**  

Aspose.Cells for JavaScript üzerinden C++ ile primitif olmayan şekiller [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/javascript-cpp/autoshapetype/) türüne atanır. Türlerini [**Shape.autoShapeType**](https://reference.aspose.com/cells/javascript-cpp/shape/#autoShapeType--) özelliği kullanarak kontrol edebilirsiniz.  

Non-primitif şekil verilerine [**Shape.paths**](https://reference.aspose.com/cells/javascript-cpp/shape/#paths--) özelliğini kullanarak erişin. Bu, non-primitif şekli oluşturan tüm bağlantılı yolları döndürür. Bu yollar, her biri noktaları içeren segmentlerin listesini tutan [**ShapePath**](https://reference.aspose.com/cells/javascript-cpp/shapepath) tipiyle temsil edilir.  

|**Primitif Olmayan Bir Şeklin Örneğini Gösterir**|  
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
