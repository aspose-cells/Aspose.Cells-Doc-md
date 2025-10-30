---
title: Arbete med reflektionseffekt av Shape eller Diagram med JavaScript via C++
linktitle: Att arbeta med reflektionseffekten i formen eller diagrammet
type: docs
weight: 210
url: /sv/javascript-cpp/working-with-the-reflection-effect-of-shape-or-chart/
description: Lär dig hur man arbetar med reflektionseffekten av former eller diagram med Aspose.Cells for JavaScript via C++. Ställ in olika reflektionsegenskaper för att uppnå önskade resultat.
---

## **Möjliga användningsscenario**
Aspose.Cells for JavaScript via C++ tillhandahåller egenskapen [Shape.reflection](https://reference.aspose.com/cells/javascript-cpp/shape/#reflection--) tillsammans med klassen [ReflectionEffect](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect) för att arbeta med reflektionseffekten av form eller diagram. Klassen [ReflectionEffect](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect) innehåller följande egenskaper som kan ställas in för att uppnå olika resultat enligt applikationskrav.

- [ReflectionEffect.blur](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#blur--)
- [ReflectionEffect.direction](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#direction--)
- [ReflectionEffect.distance](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#distance--)
- [ReflectionEffect.fadeDirection](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#fadeDirection--)
- [ReflectionEffect.rotWithShape](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#rotWithShape--)
- [ReflectionEffect.size](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#size--)
- [ReflectionEffect.transparency](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#transparency--)
- [Reflektionsexempel kod laddar [källfils excel](5115424.xlsx) och tar den första formen i standardarbetsbladet. Den ställer in olika egenskaper för [Shape.reflection](https://reference.aspose.com/cells/javascript-cpp/shape/#reflection--) och sparar sedan arbetsboken i [utdata excel](5115423.xlsx).](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#type--)

## **Att arbeta med reflektionseffekten i formen eller diagrammet**
The following sample code loads the [source excel file](5115424.xlsx) and accesses the first shape in the default worksheet. It sets different properties of the [Shape.reflection](https://reference.aspose.com/cells/javascript-cpp/shape/#reflection--) and then saves the workbook in the [output excel file](5115423.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Shape Reflection Effect Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
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

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first shape
            const shape = worksheet.shapes.get(0);

            // Set the reflection effect of the shape, set its Blur, Size, Transparency and Distance properties
            const reflectionEffect = shape.reflection;
            reflectionEffect.blur = 30;
            reflectionEffect.size = 90;
            reflectionEffect.transparency = 0;
            reflectionEffect.distance = 80;

            // Save the workbook in xlsx format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Reflection effect updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
