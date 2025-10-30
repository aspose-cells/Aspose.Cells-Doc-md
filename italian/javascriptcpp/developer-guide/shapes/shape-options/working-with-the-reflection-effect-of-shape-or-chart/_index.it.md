---
title: Lavorare con l effetto riflessione di forma o grafico con JavaScript tramite C++
linktitle: Lavorare con l effetto Reflex della forma o del grafico
type: docs
weight: 210
url: /it/javascript-cpp/working-with-the-reflection-effect-of-shape-or-chart/
description: Impara come lavorare con l effetto riflesso di forme o grafici usando Aspose.Cells for JavaScript via C++. Imposta varie proprietà di riflessione per ottenere i risultati desiderati.
---

## **Possibili Scenari di Utilizzo**
Aspose.Cells for JavaScript via C++ fornisce la proprietà [Shape.reflection](https://reference.aspose.com/cells/javascript-cpp/shape/#reflection--) insieme alla classe [ReflectionEffect](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect) per lavorare con l'effetto riflesso di forma o grafico. La classe [ReflectionEffect](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect) contiene le seguenti proprietà che possono essere impostate per ottenere risultati diversi in base alle esigenze dell'applicazione.

- [ReflectionEffect.blur](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#blur--)
- [ReflectionEffect.direction](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#direction--)
- [ReflectionEffect.distance](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#distance--)
- [ReflectionEffect.fadeDirection](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#fadeDirection--)
- [ReflectionEffect.rotWithShape](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#rotWithShape--)
- [ReflectionEffect.size](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#size--)
- [ReflectionEffect.transparency](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#transparency--)
- [ReflectionEffect.type](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#type--)

## **Lavorare con l'Effetto Riflessione di una Forma o di un Grafico**
Il seguente esempio di codice carica il [file excel di origine](5115424.xlsx) e accede alla prima forma nel foglio di lavoro predefinito. Imposta diverse proprietà di [Shape.reflection](https://reference.aspose.com/cells/javascript-cpp/shape/#reflection--) e poi salva il foglio di lavoro nel [file excel di output](5115423.xlsx).

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
