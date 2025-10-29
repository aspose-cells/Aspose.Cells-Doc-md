---
title: Travailler avec l effet de réflexion d une forme ou d un graphique avec JavaScript via C++
linktitle: Travailler avec l effet de réflexion de la forme ou du graphique
type: docs
weight: 210
url: /fr/javascript-cpp/working-with-the-reflection-effect-of-shape-or-chart/
description: Apprenez comment travailler avec l effet de réflexion des formes ou des graphiques en utilisant Aspose.Cells for JavaScript via C++. Définissez diverses propriétés de réflexion pour obtenir les résultats souhaités.
---

## **Scénarios d'utilisation possibles**
Aspose.Cells for JavaScript via C++ fournit la propriété [Shape.reflection](https://reference.aspose.com/cells/javascript-cpp/shape/#reflection--) ainsi que la classe [ReflectionEffect](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect) pour travailler avec l'effet de réflexion d'une forme ou d'un graphique. La classe [ReflectionEffect](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect) contient les propriétés suivantes qui peuvent être définies pour obtenir différents résultats selon les besoins de l'application.

- [ReflexionEffet.blur](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#blur--)
- [ReflexionEffet.direction](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#direction--)
- [ReflexionEffet.distance](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#distance--)
- [ReflexionEffet.fadeDirection](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#fadeDirection--)
- [ReflexionEffet.rotWithShape](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#rotWithShape--)
- [ReflexionEffet.size](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#size--)
- [ReflexionEffet.transparency](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#transparency--)
- [ReflexionEffet.type](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#type--)

## **Travailler avec l'effet de réflexion de la forme ou du graphique**
Le code d'exemple suivant charge le [fichier excel source](5115424.xlsx) et accède à la première forme dans la feuille de calcul par défaut. Il règle différentes propriétés de [Shape.reflection](https://reference.aspose.com/cells/javascript-cpp/shape/#reflection--) puis enregistre le classeur dans le [fichier excel de sortie](5115423.xlsx).

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
