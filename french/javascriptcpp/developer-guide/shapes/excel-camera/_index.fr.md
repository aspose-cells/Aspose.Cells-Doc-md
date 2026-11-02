---
title: Caméra Excel dans Aspose.Cells for JavaScript via C++
linktitle: Caméra Excel dans Aspose.Cells for JavaScript via C++
description: Apprendre à utiliser la caméra Excel dans Aspose.Cells for JavaScript via C++ afin de créer une image dynamique liée à une plage de cellules qui s’actualise avec les données source et conserve l’intégralité de la mise en forme de la zone source.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, Caméra Excel, image dynamique, image liée, picture.formula, updateSelectedValue, createRange, toImage, Buffer
type: docs
weight: 90
url: /fr/javascript-cpp/excel-camera/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

La caméra Excel est un objet de feuille de calcul qui produit une image dynamique d’une plage de cellules et se superpose à la couche de dessin, comme une image ordinaire. Aspose.Cells prend en charge deux modes de création : une image dynamique qui s’actualise automatiquement chaque fois que les données source changent et une image statique qui capture un instantané d’une plage à un moment donné. Cet article présente les deux approches afin de vous aider à choisir celle qui convient à votre mise en page.

## Qu’est-ce que la caméra Excel ?
La caméra Excel est essentiellement un objet d’image ancré à une ligne et à une colonne déterminées sur la couche de dessin de la feuille de calcul. Contrairement à une image insérée ordinaire, la caméra est liée à une plage source à l’aide d’une formule de style A1 telle que `"A1:F10"`. Chaque fois qu’une cellule de cette plage change, l’image de la caméra est actualisée automatiquement afin de refléter le nouveau contenu. La caméra conserve l’intégralité de la mise en forme de la zone source — bordures, couleurs d’arrière-plan, polices et formats numériques — afin que tout ce qui est visible dans les cellules apparaisse également dans son image. Elle est donc particulièrement utile pour les tableaux de bord, les résumés, les panneaux latéraux et les mises en page de rapports, où vous souhaitez afficher un aperçu d’une zone distante sans faire défiler la feuille de calcul ni répéter les données. Deux précautions sont toutefois nécessaires : vous devez appeler `updateSelectedValue()` avant d’enregistrer le classeur, et le fichier doit être exporté au format HTML ou PDF, car ces formats s’appuient sur les données d’image incorporées plutôt que sur un recalcul en direct.

## Méthode 1 — Ajouter une image de caméra dynamique
La caméra dynamique est l’approche la plus courante et celle qui correspond le mieux à l’outil Caméra intégré à Excel. Elle consiste à ajouter une image sans contenu initial, puis à définir sa propriété `formula` afin qu’elle référence la plage source. Une fois la formule attribuée, l’appel à `updateSelectedValue()` actualise les données d’image incorporées afin de les synchroniser avec les cellules référencées. La caméra n’est pas implémentée au moyen d’une classe dédiée : elle repose entièrement sur le type standard `Picture`.
Les principales API sont :
- `worksheet.getPictures().add(upperLeftRow, upperLeftColumn, null)` — ajoute une image ancrée à la ligne et à la colonne indiquées. Le passage de `null` pour le paramètre d’image crée une image vide qui sert d’emplacement pour une caméra dynamique. La méthode renvoie l’index de la nouvelle image.
- `worksheet.getPictures().get(index)` — récupère un objet `Picture` précis dans la collection.
- `picture.formula` — une propriété de type chaîne qui contient la référence de style A1 à la plage source reflétée par la caméra, telle que `"A1:F10"`.
- `picture.updateSelectedValue()` — une méthode sans valeur de retour qui actualise les données d’image incorporées à partir des cellules référencées par `formula`.

{{% alert color="primary" %}}
`updateSelectedValue()` DOIT être appelé avant l’enregistrement lorsque la sortie est au format HTML ou PDF ; sinon, le fichier exporté ne contiendra pas les données d’image et la caméra apparaîtra vide dans le résultat du rendu.
Le code suivant crée un classeur, ajoute une image vide ancrée à la ligne 10 et à la colonne 6, la lie à la plage source `A1:F10` au moyen de la propriété `formula`, actualise les données d’image incorporées, puis enregistre le classeur.
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "CameraDemo";
            // Dynamic Camera: add an empty picture, link it via Formula to A1:F10, then refresh
            const pictures = worksheet.pictures;
            const index = pictures.add(10, 6, null);
            const picture = pictures.get(0);
            picture.formula = "A1:F10";
            picture.updateSelectedValue();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_dynamic.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## Méthode 2 — Ajouter une image de caméra statique
La caméra statique est essentiellement un aperçu d’une plage de cellules rendu une seule fois. Au lieu de maintenir une liaison en direct, vous effectuez un rendu unique de la plage sous forme d’octets d’image, vous encapsulez ces octets dans un `Buffer`, puis vous les ajoutez comme une image ordinaire. Le contenu de l’image est ensuite figé au moment de sa création et ne s’actualise pas automatiquement lorsque les cellules source changent.
Les principales API sont :
- `cells.createRange(address)` — construit un objet `Range` à partir d’une adresse de style A1 telle que `"A1:F10"`.
- `range.toImage(options)` — effectue le rendu de la plage sous forme d’octets d’image. Le passage de `null` utilise les options de rendu par défaut ; des surcharges permettent un contrôle plus précis de la sortie.
- `Buffer.from(imageBytes)` — encapsule les octets d’image générés dans un objet `Buffer` qui peut être transmis à `worksheet.getPictures().add`.
- `worksheet.getPictures().add(upperLeftRow, upperLeftColumn, imageBuffer)` — ajoute l’image ancrée à la ligne et à la colonne indiquées, cette fois en transmettant le `Buffer` produit par le rendu.
Le code suivant crée un classeur, construit un objet `Range` pour `A1:F10`, effectue le rendu de la plage sous forme d’octets d’image via `range.toImage(null)`, encapsule les octets dans un `Buffer`, ajoute l’image ancrée à la ligne 10 et à la colonne 6, puis enregistre le classeur.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "CameraDemo";
            // Caméra statique : créer la plage, la rendre en octets, l'envelopper dans MemoryStream, l'ajouter comme image
            const range = worksheet.cells.createRange("A1:F10");
            const imageData = range.toImage();
            const pictures = worksheet.pictures;
            pictures.add(10, 6, imageData);
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_static.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## Choix entre la caméra dynamique et la caméra statique
- **Caméra dynamique :** se met à jour à chaque recalcul, permet l’exportation aux formats HTML et PDF après l’appel à `updateSelectedValue()` et conserve la liaison en direct pendant toute la durée de vie du fichier.
- **Caméra statique :** effectue un rendu unique qui n’est jamais actualisé ; elle est utile lorsque vous souhaitez incorporer un instantané visuel fixe lors de la génération plutôt qu’une représentation en direct des données.
Aspose.Cells prend en charge une caméra dynamique à actualisation automatique, fondée sur `picture.formula` et `updateSelectedValue()`, ainsi qu’une caméra statique à rendu unique, fondée sur `range.toImage` et un objet `Buffer`. Choisissez l’approche dynamique lorsque votre sortie doit rester synchronisée avec les cellules source et l’approche statique lorsque vous avez uniquement besoin d’un instantané visuel fixe lors de la génération.

## Articles connexes
- [Convertir un sparkline en image et HTML dans Aspose.Cells for JavaScript via C++](/cells/fr/javascript-cpp/convert-sparkline-to-image-and-html/)
- [Ajouter des champs de filtre à un tableau croisé dynamique dans Aspose.Cells for JavaScript via C++](/cells/fr/javascript-cpp/add-page-field-in-pivot-table/)
- [Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells for JavaScript via C++](/cells/fr/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}