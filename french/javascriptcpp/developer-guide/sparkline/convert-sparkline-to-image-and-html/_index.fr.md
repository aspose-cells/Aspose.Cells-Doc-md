---
title: Convertir une sparkline en image et en HTML avec Aspose.Cells for JavaScript via C++
linktitle: Convertir une sparkline en image et en HTML avec Aspose.Cells for JavaScript via C++
description: Découvrez comment rendre les sparklines d’Aspose.Cells en images autonomes pour les incorporer dans des cellules et exporter les feuilles de calcul contenant des sparklines vers HTML à l’aide de HtmlSaveOptions.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, sparkline, sparkline.toImage, cell.embeddedImage, HtmlSaveOptions, rendu de sparkline, conversion de sparkline en image, export de sparkline vers HTML
type: docs
weight: 120
url: /fr/javascript-cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Les sparklines sont de petits graphiques qui s’affichent dans les cellules d’une feuille de calcul. Aspose.Cells permet d’extraire chaque sparkline sous forme d’image autonome, afin de l’incorporer dans une autre cellule ou un rapport externe, ainsi que d’exporter la feuille de calcul entière, riche en sparklines, vers HTML pour consultation dans un navigateur. La propriété `cell.embeddedImage` utilisée dans cet article est disponible dans **Aspose.Cells 26.5 et versions ultérieures**.
{{% /alert %}}

## **Introduction**
Les sparklines constituent un moyen compact de visualiser directement les tendances au sein d’une feuille de calcul. Bien que les utilisateurs d’Excel les aperçoivent directement dans les cellules, dans de nombreux cas concrets, une sparkline doit être extraite de sa cellule, par exemple pour être incorporée sous forme d’image statique dans une autre cellule, jointe à un e-mail automatisé ou rendue dans un rapport HTML publié sur le web.
Aspose.Cells prend en charge ces deux opérations. La méthode `sparkline.toImage` rend une sparkline isolée sous forme de `Buffer`, et les octets obtenus peuvent être affectés à `cell.embeddedImage` afin que l’image soit stockée dans une seule cellule du classeur. Par ailleurs, `HtmlSaveOptions` permet de convertir l’ensemble du classeur, y compris les sparklines, en un fichier HTML autonome. Cet article présente ces deux processus de bout en bout.

## **Processus 1 — Rendre les sparklines en images et les incorporer dans les cellules**
Dans ce processus, vous allez créer une feuille de calcul contenant une petite plage de valeurs sources, associer trois groupes de sparklines distincts (Ligne, Colonne et Gagnant/Perdu) à cette plage, rendre chaque groupe sous forme de PNG, puis écrire les octets PNG dans des cellules adjacentes en tant qu’images incorporées. Le résultat final est un fichier `.xlsx` unique contenant à la fois les sparklines natives et dynamiques et leurs versions statiques sous forme d’images.

### **Instructions pas à pas**
1. Créez un nouveau `Workbook` et obtenez une référence vers le premier `Worksheet`.
2. Remplissez les cellules `A1` à `E1` avec cinq valeurs numériques d’exemple, par exemple les ventes quotidiennes ou les relevés de température.
3. Ajoutez trois objets `SparklineGroup` à la feuille de calcul en appelant `worksheet.getSparklineGroups().add(...)` :
   - Un groupe `SparklineType.Line` ancré à `F1`, avec la plage de données `A1:E1`.
   - Un groupe `SparklineType.Column` ancré à `G1`, avec la plage de données `A1:E1`.
   - Un groupe `SparklineType.Stacked` (gagnant/perdu) ancré à `H1`, avec la plage de données `A1:E1`.
4. Construisez une instance `ImageOrPrintOptions` et définissez sa propriété `imageType` sur `ImageType.Png` afin que chaque sparkline soit rendue sous forme d’image PNG.
5. Enregistrez le classeur sous `output_with_sparklines.xlsx`.

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
        const { Workbook, CellArea, ImageOrPrintOptions } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // Créer un nouveau classeur et accéder à la première feuille de calcul
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // Remplir les cellules A1:E1 avec des données d'exemple
            cells.get("A1").value = 5;
            cells.get("B1").value = -3;
            cells.get("C1").value = 8;
            cells.get("D1").value = -2;
            cells.get("E1").value = 6;
            // Ajouter un groupe de sparklines de type ligne ancré à F1 (colonne 5, ligne 0)
            const lineArea = new CellArea();
            lineArea.startColumn = 5;
            lineArea.endColumn = 5;
            lineArea.startRow = 0;
            lineArea.endRow = 0;
            const lineIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Line,
                "A1:E1",
                false,
                lineArea
            );
            // Ajouter un groupe de sparklines de type colonne ancré à G1 (colonne 6, ligne 0)
            const columnArea = new CellArea();
            columnArea.startColumn = 6;
            columnArea.endColumn = 6;
            columnArea.startRow = 0;
            columnArea.endRow = 0;
            const columnIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Column,
                "A1:E1",
                false,
                columnArea
            );
            // Ajouter un groupe de sparklines Gains/Pertes (empilées) ancré à H1 (colonne 7, ligne 0)
            const stackedArea = new CellArea();
            stackedArea.startColumn = 7;
            stackedArea.endColumn = 7;
            stackedArea.startRow = 0;
            stackedArea.endRow = 0;
            const stackedIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Stacked,
                "A1:E1",
                false,
                stackedArea
            );
            // Configurer les options d'image pour la sortie PNG
            const imageOptions = new ImageOrPrintOptions();
            imageOptions.imageType = AsposeCells.ImageType.Png;
            // Convertir la sparkline de type ligne en image et l'incorporer dans la cellule F2
            const lineSp = worksheet.sparklineGroups.get(lineIdx).sparklines.get(0);
            cells.get("F2").embeddedImage = lineSp.toImage(imageOptions);
            // Convertir la sparkline de type colonne en image et l'incorporer dans la cellule G2
            const columnSp = worksheet.sparklineGroups.get(columnIdx).sparklines.get(0);
            cells.get("G2").embeddedImage = columnSp.toImage(imageOptions);
            // Convertir la sparkline Gains/Pertes en image et l'incorporer dans la cellule H2
            const stackedSp = worksheet.sparklineGroups.get(stackedIdx).sparklines.get(0);
            cells.get("H2").embeddedImage = stackedSp.toImage(imageOptions);
            // Enregistrer le classeur sur le disque
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_with_sparklines.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

Le code ci-dessus produit un classeur dans lequel chaque représentation visuelle d’une sparkline se présente sous deux formes : la sparkline native et dynamique, ancrée à la ligne 1, et une image PNG statique, incorporée directement dans une cellule voisine de la ligne 2. Comme les images sont stockées dans le fichier lui-même, le classeur reste un artefact unique et autonome, qui peut être envoyé par e-mail ou archivé sans rompre les références aux images incorporées.

{{% alert color="primary" %}}
Comme chaque groupe de sparklines est ancré à une seule cellule, vous pouvez y accéder à l’aide de l’indexeur `group.getSparklines()[0]` plutôt que d’énumérer la collection. Cela permet de raccourcir le code de rendu et correspond au modèle courant « une sparkline par cellule d’ancrage ». Le stockage des octets de l’image via `cell.embeddedImage` est disponible dans Aspose.Cells 26.5 et versions ultérieures.
{{% /alert %}}

## **Processus 2 — Exporter vers HTML la feuille de calcul contenant des sparklines**
Une fois que le classeur contient des sparklines natives et dynamiques ainsi que, facultativement, des images incorporées équivalentes, la feuille de calcul entière peut être publiée sur le web en l’enregistrant au format HTML. La classe `HtmlSaveOptions` expose les paramètres de configuration nécessaires pour contrôler cet export. Dans ce processus, vous réutiliserez le fichier `output_with_sparklines.xlsx` produit par le Processus 1 et le convertirez en un document HTML propre sur une seule page.

### **Instructions pas à pas**
1. Assurez-vous que le fichier `output_with_sparklines.xlsx` produit par le Processus 1 est disponible sur le disque dans votre répertoire de travail.
2. Chargez ce fichier dans une nouvelle instance de `Workbook`.
3. Créez une instance de `HtmlSaveOptions` et définissez sa propriété `exportActiveWorksheetOnly` sur `true` afin que le fichier HTML obtenu contienne uniquement la feuille de calcul active plutôt que le classeur entier.
4. Appelez `workbook.save("sparklines.html", htmlOptions)` pour écrire la sortie HTML sur le disque.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, HtmlSaveOptions } = AsposeCells;
        AsposeCells.onReady({
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
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            try {
                const file = fileInput.files[0];
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const htmlOptions = new HtmlSaveOptions();
                htmlOptions.exportActiveWorksheetOnly = true;
                const outputData = workbook.save(AsposeCells.SaveFormat.Html, htmlOptions);
                const blob = new Blob([outputData], { type: "text/html" });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "sparklines.html";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = `<p style="color: red;">${error.message}</p>`;
            }
        });
    </script>
</html>
```

Le code ci-dessus transforme le classeur riche en sparklines du Processus 1 en un fichier HTML portable. Les groupes de sparklines sont rendus sous forme d’images intégrées dans le tableau HTML généré, si bien que les utilisateurs finaux peuvent consulter les tendances dans n’importe quel navigateur moderne sans avoir à installer Excel. En définissant `exportActiveWorksheetOnly` sur `true`, vous évitez de publier par inadvertance des feuilles masquées ou des données auxiliaires : seule la feuille de calcul actuellement visible par l’utilisateur est exportée.

{{% alert color="primary" %}}
La classe `HtmlSaveOptions` propose des propriétés supplémentaires pour affiner la sortie, telles que `exportHiddenWorksheet`, `exportImagesAsBase64` et `encoding`. Ajustez-les selon les besoins de votre environnement de déploiement.
{{% /alert %}}

## **Résumé de l’API**
Les processus ci-dessus reposent sur un petit ensemble d’API Aspose.Cells qui fonctionnent conjointement.
- `SparklineGroup` et l’accesseur de collection `worksheet.getSparklineGroups()` sont utilisés pour déclarer le type (Ligne, Colonne, Empilé), la plage de données et la cellule d’ancrage de chaque groupe de sparklines. Dans cet article, chaque groupe est ancré à une seule cellule ; le groupe est donc accessible via `worksheet.getSparklineGroups()[i]`.
- `Sparkline` et l’indexeur `group.getSparklines()[0]` donnent accès à la sparkline individuelle contenue dans un groupe. Comme chaque groupe de l’exemple contient exactement une sparkline, aucune boucle d’itération n’est nécessaire.
- `sparkline.toImage(imageOrPrintOptions)` est la méthode de rendu qui renvoie une image de la sparkline sous forme de `Buffer`. Les octets renvoyés peuvent être affectés directement à `cell.embeddedImage`.
- `HtmlSaveOptions.exportActiveWorksheetOnly` (un booléen) limite l’exportation au format HTML à la feuille de calcul active. Il s’agit de l’une des propriétés les plus couramment utilisées sur `HtmlSaveOptions` lors de la génération de rapports sur une seule page.
- `ImageOrPrintOptions.imageType` sélectionne le format d’image, par exemple `ImageType.Png`, utilisé lors du rendu avec `toImage` et lors de l’impression des feuilles de calcul sous forme d’images.

{{< app/cells/assistant language="javascript-cpp" >}}