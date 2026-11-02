---
title: Insertion d’une image dans une cellule
linktitle: Insertion d’une image dans une cellule
description: Aspose.Cells for JavaScript via C++ est une bibliothèque permettant de travailler avec des fichiers de tableur. Cet article explique comment ajuster exactement une image à une seule cellule, soit en plaçant une image flottante au-dessus de la cellule, soit en incorporant l’image directement dans la cellule.
keywords: Aspose.Cells, bibliothèque JavaScript via C++, tableur, insérer une image, incorporer une image, image dans une cellule, ajuster une image à une cellule, Pictures, EmbeddedImage
type: docs
weight: 80
url: /fr/javascript-cpp/inserting-an-image-into-a-cell/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells fournit deux méthodes distinctes pour associer une image à une seule cellule. Une image flottante est une forme située sur la couche de dessin de la feuille de calcul et qui recouvre visuellement une plage de cellules, tandis qu’une image incorporée est stockée dans la cellule elle-même et s’adapte automatiquement à sa zone d’affichage. Choisissez l’approche qui correspond le mieux à vos exigences de mise en page.
{{% /alert %}}

## **Introduction**
L’ajustement exact d’une image à une seule cellule est une exigence courante lors de la conception de tableurs qui servent de rapports visuels, de catalogues de produits, d’annuaires du personnel, de tableaux de bord ou de listes d’inventaire. Au lieu d’étirer une image sur plusieurs cellules ou de la placer librement sur une feuille de calcul, vous pouvez vouloir une image nette, liée à la cellule et qui reste alignée sur la cellule qui la contient.
Aspose.Cells prend en charge ce scénario de deux façons complémentaires :
- **Approche 1 — Placer une image flottante au-dessus d’une cellule.** Ajoutez un `Picture` à la feuille de calcul, définissez son placement à l’aide de `picture.setPlacement(PlacementType.MoveAndSize)` et ajustez ses cellules d’ancrage au moyen de `picture.setUpperLeftRow()`, `picture.setUpperLeftColumn()`, `picture.setLowerRightRow()` et `picture.setLowerRightColumn()` afin que l’image recouvre exactement une seule cellule.
- **Approche 2 — Incorporer directement une image dans une cellule.** Affectez à la cellule un `Buffer` contenant les données de l’image avec `cell.setEmbeddedImage(imageBuffer)`. L’image s’adapte automatiquement à la zone d’affichage de la cellule et se déplace avec elle.
La suite de cet article présente les deux approches, explique les API pertinentes et montre comment les utiliser dans le code.

## **Approche 1 : Placer une image au-dessus d’une cellule**
Une image flottante est un objet `Picture` qui se trouve sur la couche de dessin de la feuille de calcul. Bien qu’elle ne fasse pas partie d’une cellule en particulier, elle est ancrée à une plage de cellules. Les cellules d’ancrage de l’image — ses coins supérieur gauche et inférieur droit — déterminent son étendue visuelle sur la feuille de calcul. Par défaut, une image nouvellement ajoutée couvre plusieurs cellules.
Pour faire couvrir **exactement une seule cellule** à une image flottante, vous devez :
1. Ajouter l’image à l’aide de `worksheet.getPictures().add(row, column, imageBuffer)`, où `imageBuffer` est un `Buffer` contenant les données de l’image. Cette opération ancre la nouvelle image à la cellule indiquée.
2. Définir les quatre valeurs d’ancrage afin que le rectangle englobant de l’image coïncide avec la cellule cible.
3. Appeler `picture.setPlacement(PlacementType.MoveAndSize)` afin que l’image se déplace et se redimensionne avec la cellule sous-jacente lorsque l’utilisateur modifie la largeur de colonne ou la hauteur de ligne.

### **Ancrage de l’image à une seule cellule**
L’ancrage de l’image est défini par quatre accesseurs d’index commençant à zéro :
- `picture.getUpperLeftRow()` et `picture.setUpperLeftRow(value)` — l’index de ligne du bord supérieur de l’image.
- `picture.getUpperLeftColumn()` et `picture.setUpperLeftColumn(value)` — l’index de colonne du bord gauche de l’image.
- `picture.getLowerRightRow()` et `picture.setLowerRightRow(value)` — l’index de ligne du bord inférieur de l’image. Pour placer le bord inférieur de l’image au bas de la ligne `r`, définissez cette valeur à `r + 1`.
- `picture.getLowerRightColumn()` et `picture.setLowerRightColumn(value)` — l’index de colonne du bord droit de l’image. Pour placer le bord droit de l’image à droite de la colonne `c`, définissez cette valeur à `c + 1`.

{{% alert color="primary" %}}
Les index de ligne et de colonne dans Aspose.Cells sont **indexés à partir de zéro**. La cellule C6 a l’index de ligne 5 et l’index de colonne 2. Les erreurs de décalage d’une unité sur l’ancrage inférieur droit constituent la source la plus fréquente d’images qui semblent chevaucher la cellule adjacente.
{{% /alert %}}

### **Contrôle du comportement de placement**
`picture.getPlacement()` et `picture.setPlacement(value)` utilisent l’enum `PlacementType` pour contrôler le comportement de l’image lorsque l’utilisateur redimensionne la ligne ou la colonne située en dessous. La valeur recommandée pour une image occupant une seule cellule est `PlacementType.MoveAndSize`, qui oblige l’image à se déplacer et à se redimensionner avec la cellule sous-jacente, tout en conservant son ajustement exact.

### **Instructions pas à pas**
1. Créez un nouveau `Workbook` (ou ouvrez-en un existant).
2. Accédez à la `Worksheet` cible via `workbook.getWorksheets().getAt(0)`.
3. Lisez le fichier d’image du disque dans un `Buffer`, par exemple à l’aide de Node.js `fs.readFileSync`.
4. Appelez `worksheet.getPictures().add(5, 2, imageBuffer)` pour ajouter une image ancrée à la cellule C6. La méthode renvoie l’index de la nouvelle image dans la collection `Pictures` ; utilisez-le pour récupérer le `Picture` correspondant.
5. Définissez les quatre coordonnées d’ancrage afin que l’image couvre uniquement la cellule C6 : `picture.setUpperLeftRow(5)`, `picture.setUpperLeftColumn(2)`, `picture.setLowerRightRow(6)` et `picture.setLowerRightColumn(3)`.
6. Appelez `picture.setPlacement(PlacementType.MoveAndSize)` pour maintenir l’image alignée sur C6 lorsque la colonne ou la ligne est redimensionnée.
7. Facultativement, ajoutez un texte d’exemple aux cellules environnantes pour démontrer que seule la cellule C6 contient l’image.
8. Enregistrez le classeur sur le disque dans un fichier `.xlsx`.
Le code suivant illustre l’approche complète.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".png,image/png" />
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
            const fileInput = document.getElementById('fileInput');
            const file = fileInput.files[0];
            if (!file) {
                document.getElementById('result').innerHTML =
                    '<p style="color: red;">Please select a PNG image.</p>';
                return;
            }
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const imageData = new Uint8Array(await file.arrayBuffer());
            const picIndex = worksheet.pictures.add(5, 2, imageData);
            const picture = worksheet.pictures.get(picIndex);
            picture.upperLeftRow = 5;
            picture.upperLeftColumn = 2;
            picture.lowerRightRow = 6;
            picture.lowerRightColumn = 3;
            picture.placement = AsposeCells.Drawing.PlacementType.MoveAndSize;
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Approche 2 : Incorporer directement une image dans une cellule**
Aspose.Cells expose également un mécanisme plus simple pour les images liées à une cellule : la méthode `cell.setEmbeddedImage(imageBuffer)`. L’affectation de données d’image à l’aide de cette méthode rattache l’image à la cellule elle-même, comme s’il s’agissait de contenu en ligne.

### **Fonctionnement des images incorporées**
- L’image est stockée dans le contenu de la cellule plutôt que sous la forme d’une forme sur la couche de dessin.
- L’image s’adapte automatiquement aux limites de rendu de la cellule. Aucune coordonnée d’ancrage ni aucun paramètre de placement n’est requis.
- La cellule reste une véritable cellule, avec une adresse réelle, qui peut être référencée par des formules, triée dans le cadre d’une ligne ou utilisée dans d’autres opérations au niveau de la cellule.
Ainsi, `cell.setEmbeddedImage(imageBuffer)` constitue l’option la plus concise lorsque votre objectif est simplement d’obtenir « une image qui réside dans cette cellule ».

### **Instructions pas à pas**
1. Créez un nouveau `Workbook` (ou ouvrez-en un existant).
2. Accédez à la `Worksheet` cible via `workbook.getWorksheets().getAt(0)`.
3. Lisez le fichier d’image du disque dans un `Buffer`, par exemple à l’aide de Node.js `fs.readFileSync`.
4. Obtenez une référence vers la cellule cible — soit via `worksheet.getCells().get("C6")`, soit via `worksheet.getCells().get(5, 2)`.
5. Passez le `Buffer` à la cellule avec `cell.setEmbeddedImage(imageBuffer)`.
6. Facultativement, ajustez la hauteur de ligne et la largeur de colonne de la ligne et de la colonne cibles afin de donner à l’image incorporée un aspect plus prédominant.
7. Enregistrez le classeur sur le disque dans un fichier `.xlsx`.
Le code suivant illustre l’approche complète.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".png,.jpg,.jpeg" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook } = AsposeCells;
        const asposeReady = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files || fileInput.files.length === 0) {
                result.innerHTML = '<p style="color: red;">Please select an image file.</p>';
                return;
            }
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            // Obtenir la cellule cible C6
            const cell = worksheet.cells.get("C6");
            // Lire le fichier image dans un tableau d'octets
            const imageData = new Uint8Array(await fileInput.files[0].arrayBuffer());
            // Intégrer directement l'image dans la cellule
            cell.embeddedImage = imageData;
            // Ajuster éventuellement la hauteur de ligne et la largeur de colonne afin que l'image intégrée soit plus visible
            worksheet.cells.setColumnWidth(2, 30); // Colonne C (index 2)
            worksheet.cells.setRowHeight(5, 100); // Ligne 6 (index 5)
            // Enregistrer le classeur obtenu dans un fichier .xlsx
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Choix de l’approche appropriée**
Les deux approches permettent d’obtenir une image ajustée à une seule cellule, mais elles diffèrent par le mode de stockage de l’image et son comportement :
- **Utilisez une image flottante (approche 1) lorsque :**
  - Vous avez besoin d’un contrôle précis du placement, de la superposition ou de l’alignement avec d’autres objets de dessin.
  - Vous souhaitez que l’image se comporte comme une forme pouvant être sélectionnée, réordonnée ou regroupée avec d’autres formes.
  - Vous exigez la compatibilité avec du code existant qui fonctionne déjà avec la collection `Pictures` accessible via `worksheet.getPictures()`.
  - Vous devez calculer dynamiquement les coordonnées d’ancrage selon la mise en page de la feuille de calcul.
- **Utilisez une image incorporée (approche 2) lorsque :**
  - Vous souhaitez effectuer l’insertion la plus simple possible d’une image dans une cellule.
  - L’image doit accompagner la cellule dans ses déplacements, à l’instar de tout autre contenu de cellule.

## Articles connexes
- [Caméra Excel dans Aspose.Cells for JavaScript via C++](/cells/fr/javascript-cpp/excel-camera/)

{{< app/cells/assistant language="javascript-cpp" >}}