---
title: Données en forme non primitive avec JavaScript via C++
linktitle: Données dans une forme non primitive
type: docs
weight: 300
url: /fr/javascript-cpp/data-in-non-primitive-shape/
description: Apprenez à accéder et manipuler les formes non primitives en Aspose.Cells for JavaScript via C++.
---

## **Accès aux données d'une forme non primitive**  

Parfois, vous avez besoin d'accéder aux données d'une forme qui n'est pas intégrée. Les formes intégrées sont appelées formes primitives; celles qui ne le sont pas sont appelées non primitives. Par exemple, vous pouvez définir vos propres formes en utilisant différentes lignes connectées par courbe.  

## **Une forme non primitive**  

Dans Aspose.Cells for JavaScript via C++, les formes non primitives se voient attribuer le type [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/javascript-cpp/autoshapetype/). Vous pouvez vérifier leur type en utilisant la propriété [**Shape.autoShapeType**](https://reference.aspose.com/cells/javascript-cpp/shape/#autoShapeType--).  

Accédez aux données de la forme en utilisant la propriété [**Shape.paths**](https://reference.aspose.com/cells/javascript-cpp/shape/#paths--). Elle renvoie tous les chemins connectés qui composent la forme non primitive. Ces chemins sont de type [**ShapePath**](https://reference.aspose.com/cells/javascript-cpp/shapepath) qui contient une liste de tous les segments, lesquels contiennent à leur tour les points dans chaque segment.  

|**Montre un exemple d'une forme non primitive**|  
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
