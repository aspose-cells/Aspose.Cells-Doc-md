---
title: Convertir un sparkline en image et en HTML dans Aspose.Cells for Node.js via C++
linktitle: Convert Sparkline to Image and HTML
description: Apprenez à rendre les sparklines d'Aspose.Cells en images autonomes pour les incorporer dans des cellules et à exporter des feuilles de calcul riches en sparklines vers HTML à l'aide de HtmlSaveOptions.
keywords: Aspose.Cells, Node.js via C++, sparkline, Sparkline.toImage, cell.embeddedImage, HtmlSaveOptions, rendu de sparkline, convertir un sparkline en image, exporter un sparkline vers HTML
type: docs
weight: 120
url: /fr/nodejs-cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Les sparklines sont des mini-graphiques placés à l'intérieur des cellules d'une feuille de calcul. Aspose.Cells vous permet d'extraire chaque sparkline sous forme d'image autonome (pour l'incorporer dans une autre cellule ou dans un rapport externe) et d'exporter également la feuille de calcul complète, riche en sparklines, vers HTML pour une diffusion dans un navigateur. La propriété `cell.embeddedImage` utilisée dans cet article est disponible dans **Aspose.Cells 26.5 et versions ultérieures**.
{{% /alert %}}

## **Introduction**

Les sparklines sont un moyen compact de visualiser des tendances directement à l'intérieur d'une feuille de calcul. Alors que les utilisateurs d'Excel les voient en place, de nombreux scénarios réels exigent qu'un sparkline quitte la cellule — par exemple, pour être incorporé dans une autre cellule sous forme d'image statique, joint à un e-mail automatisé ou rendu dans le cadre d'un rapport HTML publié sur le web.

Aspose.Cells prend en charge ces deux opérations. La méthode `Sparkline.toImage` restitue un sparkline individuel vers un flux, et les octets résultants peuvent être assignés à `cell.embeddedImage` afin que l'image soit stockée à l'intérieur d'une seule cellule du classeur. Par ailleurs, `HtmlSaveOptions` vous permet de convertir le classeur entier — sparklines inclus — en un fichier HTML autonome. Cet article présente les deux flux de travail de bout en bout.

## **Flux de travail 1 — Rendre les sparklines en images et les incorporer dans les cellules**

Dans ce flux de travail, vous allez construire une feuille de calcul contenant une petite plage de valeurs sources, attacher trois groupes de sparklines différents (Ligne, Colonne et Empilé/Perte-Gain) à cette plage, rendre chaque groupe au format PNG, puis écrire ces octets PNG dans des cellules adjacentes sous forme d'images incorporées. Le résultat final est un fichier `.xlsx` unique qui contient à la fois les sparklines actifs et leurs équivalents sous forme d'images rendues.

### **Instructions étape par étape**

1. Définissez un répertoire de travail et assurez-vous qu'il existe sur le disque.
2. Créez un nouveau `Workbook` et obtenez une référence à la première `Worksheet`.
3. Remplissez les cellules `A1` à `E1` avec cinq valeurs numériques d'exemple (par exemple, des ventes quotidiennes ou des relevés de température).
4. Ajoutez trois objets `SparklineGroup` à la feuille de calcul en appelant `worksheet.sparklineGroups.add(...)` :
   - Un groupe `SparklineType.Line` ancré à `F1`, avec la plage de données `A1:E1`.
   - Un groupe `SparklineType.Column` ancré à `G1`, avec la plage de données `A1:E1`.
   - Un groupe `SparklineType.Stacked` (gain/perte) ancré à `H1`, avec la plage de données `A1:E1`.
5. Construisez une instance d'`ImageOrPrintOptions` et définissez sa propriété `ImageType` sur `ImageType.Png` afin que chaque sparkline soit rendu sous forme de PNG transparent.
6. Pour chacun des trois groupes, rendez l'unique sparkline du groupe à l'aide de `group.sparklines[0].toImage(memoryStream, imageOrPrintOptions)`, convertissez le flux en `Buffer` (ou `Uint8Array`), puis assignez les octets à `worksheet.cells["F2"].embeddedImage`, `worksheet.cells["G2"].embeddedImage` et `worksheet.cells["H2"].embeddedImage` respectivement.
7. Enregistrez le classeur sous le nom `output_with_sparklines.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Remplir les cellules A1:E1 avec des données d'exemple
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Ajouter un groupe de sparklines de type Ligne ancré en F1 (colonne 5, ligne 0)
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);

// Ajouter un groupe de sparklines de type Colonne ancré en G1 (colonne 6, ligne 0)
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(6);
columnArea.setEndColumn(6);
columnArea.setStartRow(0);
columnArea.setEndRow(0);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);

// Ajouter un groupe de sparklines Win/Loss (Empilé) ancré en H1 (colonne 7, ligne 0)
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(7);
stackedArea.setEndColumn(7);
stackedArea.setStartRow(0);
stackedArea.setEndRow(0);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);

// Configurer les options d'image pour la sortie PNG
let imageOptions = new AsposeCells.ImageOrPrintOptions();
imageOptions.setImageType(AsposeCells.ImageType.Png);

// Convertir la sparkline de type Ligne en image et l'incruster dans la cellule F2
let lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
let linePath = "line_sparkline.png";
lineSp.toImage(linePath, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(fs.readFileSync(linePath));

// Convertir la sparkline de type Colonne en image et l'incruster dans la cellule G2
let columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
let columnPath = "column_sparkline.png";
columnSp.toImage(columnPath, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(fs.readFileSync(columnPath));

// Convertir la sparkline Win/Loss en image et l'incruster dans la cellule H2
let stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
let stackedPath = "stacked_sparkline.png";
stackedSp.toImage(stackedPath, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(fs.readFileSync(stackedPath));

// Enregistrer le classeur sur le disque
workbook.save("output_with_sparklines.xlsx");
```

Le code ci-dessus produit un classeur dans lequel chaque représentation visuelle d'un sparkline est dupliquée sous deux formes : le sparkline natif et actif ancré à la ligne 1, et une image PNG statique incorporée directement dans une cellule voisine de la ligne 2. Étant donné que les images vivent dans le fichier lui-même, le classeur reste un artefact unique et autonome qui peut être envoyé par e-mail ou archivé sans rompre les références aux images incorporées. Rendez chaque groupe de sparklines au format PNG, convertissez le flux en `Buffer`, puis assignez le tableau à la propriété `embeddedImage` de la cellule cible — c'est cette assignation qui intègre l'image au contenu stocké de la cellule.

{{% alert color="primary" %}}
Étant donné que chaque groupe de sparklines est ancré à une seule cellule, vous pouvez y accéder via l'indexeur `group.sparklines[0]` au lieu d'énumérer avec `forEach`. Cela permet de garder le code de rendu court et correspond au modèle typique « un sparkline par cellule d'ancrage ». Le stockage des octets de l'image via `cell.embeddedImage` nécessite Aspose.Cells 26.5 ou une version ultérieure.
{{% /alert %}}

## **Flux de travail 2 — Exporter la feuille de calcul avec sparklines vers HTML**

Une fois que le classeur contient des sparklines actifs (et éventuellement leurs équivalents sous forme d'images incorporées), la feuille de calcul entière peut être publiée sur le web en l'enregistrant au format HTML. La classe `HtmlSaveOptions` expose les réglages dont vous avez besoin pour contrôler cet export ; dans ce flux de travail, vous allez réutiliser le fichier `output_with_sparklines.xlsx` produit par le flux de travail 1 et le convertir en un document HTML propre, d'une seule page.

### **Instructions étape par étape**

1. Assurez-vous que le fichier `output_with_sparklines.xlsx` produit par le flux de travail 1 est disponible sur le disque dans votre répertoire de travail.
2. Chargez ce fichier dans une nouvelle instance de `Workbook`.
3. Instanciez `HtmlSaveOptions` et définissez sa propriété `exportActiveWorksheetOnly` sur `true` afin que le fichier HTML résultant contienne uniquement la feuille de calcul active plutôt que le classeur entier.
4. Appelez `workbook.save("sparklines.html", htmlOptions)` pour écrire la sortie HTML sur le disque.

```javascript
let workbook = new AsposeCells.Workbook("output_with_sparklines.xlsx");
let htmlOptions = new AsposeCells.HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

Le code ci-dessus prend le classeur riche en sparklines du flux de travail 1 et le transforme en fichier HTML portable. Les sparklines sont conservés sous forme de rendus SVG ou PNG intégrés dans le HTML généré, selon le mode d'export, de sorte que les utilisateurs finaux peuvent consulter les tendances dans n'importe quel navigateur moderne sans avoir besoin d'Excel installé. En définissant `exportActiveWorksheetOnly` sur `true`, vous évitez de publier accidentellement des feuilles masquées ou des données auxiliaires — seule la feuille de calcul actuellement visible par l'utilisateur est exportée.

{{% alert color="primary" %}}
La classe `HtmlSaveOptions` propose des propriétés supplémentaires pour affiner la sortie, telles que `exportHiddenWorksheet`, `exportImagesAsBase64` et `encoding`. Ajustez-les selon les besoins de votre cible de déploiement.
{{% /alert %}}

## **Résumé de l'API**

Les flux de travail ci-dessus s'appuient sur un petit ensemble d'API d'Aspose.Cells travaillant ensemble.

- `SparklineGroup` et l'accesseur de collection `worksheet.sparklineGroups` sont utilisés pour déclarer le type (Ligne, Colonne, Empilé), la plage de données et la cellule d'ancrage pour chaque groupe de sparklines. Dans cet article, chaque groupe est ancré à une seule cellule, donc le groupe est accessible via `worksheet.sparklineGroups[i]`.
- `Sparkline` et l'indexeur `group.sparklines[0]` renvoient le sparkline individuel à l'intérieur d'un groupe. Étant donné que chaque groupe de l'exemple contient exactement un sparkline, aucune boucle `forEach` n'est nécessaire.
- `Sparkline.toImage(Stream, ImageOrPrintOptions)` est la méthode de rendu qui écrit une image du sparkline dans un `Stream` fourni. La méthode renvoie `void` ; vous lisez les octets du flux après l'appel.
- `cell.embeddedImage` est une propriété de type `Buffer` (ou `Uint8Array`) qui stocke une image à l'intérieur d'une seule cellule. Elle est disponible dans **Aspose.Cells 26.5 et versions ultérieures** et constitue la méthode recommandée pour réinjecter dans le même classeur un sparkline rendu par `toImage`.
- `htmlSaveOptions.exportActiveWorksheetOnly` (un `bool`) restreint l'export HTML à la feuille de calcul active. C'est l'une des propriétés les plus couramment utilisées sur `HtmlSaveOptions` lors de la génération de rapports d'une seule page.
- `imageOrPrintOptions.imageType` se trouve dans le namespace `Aspose.Cells.Drawing` et sélectionne le format d'image (par exemple, `ImageType.Png`) utilisé lors du rendu avec `toImage` et lors de l'impression des feuilles de calcul en images.

## **Articles connexes**

- [Sparklines dans Aspose.Cells pour Aspose.Cells for Node.js via C++](/cells/fr/nodejs-cpp/sparkline/)
- [Insertion d'une image dans une cellule](/cells/fr/nodejs-cpp/inserting-an-image-into-a-cell/)
- [Rendu de tableau de cellule unique SmartMarker | Aspose.Cells Node.js via C++](/cells/fr/nodejs-cpp/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="javascript" >}}