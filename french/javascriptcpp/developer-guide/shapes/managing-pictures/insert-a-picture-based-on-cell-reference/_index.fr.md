---
title: Insérer une image basée sur une référence de cellule avec JavaScript via C++
linktitle: Insérer une image basée sur la référence de la cellule
type: docs
weight: 150
url: /fr/javascript-cpp/insert-a-picture-based-on-cell-reference/
description: Apprenez comment insérer une image dans une feuille de calcul basée sur une référence de cellule en utilisant Aspose.Cells for JavaScript via C++. Afficher les données de la cellule dans une image.
---

{{% alert color="primary" %}}
Parfois, vous avez une image vide et vous devez afficher des données ou du contenu dans l'image en définissant une référence de cellule dans la barre de formule. Aspose.Cells prend en charge cette fonctionnalité (Microsoft Excel 2010).
{{% /alert %}}

## Insertion d'une image basée sur la référence de la cellule

Aspose.Cells for JavaScript via C++ prend en charge l'affichage du contenu d'une cellule de feuille de calcul dans une forme d'image. Vous pouvez lier l'image à la cellule contenant les données que vous souhaitez afficher. Étant donné que la cellule ou la plage de cellules est liée à l'objet graphique, les modifications apportées aux données dans cette cellule ou plage sont automatiquement reflétées dans l'objet graphique. Ajoutez une image à la feuille de calcul en appelant la méthode [**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-) de la collection [**ShapeCollection**](https://reference.aspose.com/cells/javascript-cpp/shapecollection) (encapsulée dans l'objet [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)). Spécifiez la plage de cellules en utilisant l'attribut [**Picture.formula**](https://reference.aspose.com/cells/javascript-cpp/picture/#formula--) de l'objet [**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture).

### Exemple de code

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Referenced Picture Example</h1>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();
            // Get the first worksheet's cells collection
            const cells = workbook.worksheets.get(0).cells;

            // Add string values to the cells
            cells.get("A1").value = "A1";
            cells.get("C10").value = "C10";

            // Get the conditional icon's image data
            const imagedata = AsposeCells.ConditionalFormattingIcon.iconImageData(AsposeCells.IconSetType.TrafficLights31, 0);
            // Create a stream based on the image data
            const stream = Uint8Array.from(imagedata);

            // Add a blank picture to the D1 cell
            const pic = workbook.worksheets.get(0).shapes.addPicture(0, 3, stream, 10, 10);
            // Specify the formula that refers to the source range of cells
            pic.formula = "A1:C10";
            // Update the shapes selected value in the worksheet
            workbook.worksheets.get(0).shapes.updateSelectedValue();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'referencedpicture.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
