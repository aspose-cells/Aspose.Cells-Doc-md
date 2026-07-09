---
title: Convertir un sparkline en image et HTML avec Aspose.Cells for .NET
linktitle: Convert Sparkline to Image and HTML
description: Apprenez à convertir des sparklines Aspose.Cells en images autonomes pour les intégrer dans des cellules et à exporter des feuilles de calcul contenant des sparklines vers HTML à l'aide de HtmlSaveOptions.
keywords: Aspose.Cells, .NET, sparkline, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, rendu de sparkline, convertir un sparkline en image, exporter un sparkline vers HTML
type: docs
weight: 120
url: /fr/net/convert-sparkline-to-image-and-html/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Les sparklines sont des graphiques miniatures placés à l'intérieur des cellules d'une feuille de calcul. Aspose.Cells vous permet d'extraire chaque sparkline sous forme d'image autonome (pour l'intégrer dans une autre cellule ou un rapport externe) et d'exporter également la feuille de calcul entière, contenant les sparklines, vers HTML pour une diffusion basée sur navigateur. La propriété `Cell.EmbeddedImage` utilisée dans cet article est disponible dans **Aspose.Cells 26.5 et versions ultérieures**.
{{% /alert %}}

## **Introduction**

Les sparklines constituent un moyen compact de visualiser des tendances directement à l'intérieur d'une feuille de calcul. Alors que les utilisateurs d'Excel les voient en place, de nombreux scénarios réels nécessitent qu'un sparkline quitte la cellule — par exemple, pour être intégré dans une autre cellule en tant qu'image statique, joint à un e-mail automatisé, ou rendu dans le cadre d'un rapport HTML publié sur le web.

Aspose.Cells prend en charge ces deux opérations. La méthode `Sparkline.ToImage` restitue un sparkline individuel vers un flux, et les octets résultants peuvent être affectés à `Cell.EmbeddedImage` afin que l'image soit stockée à l'intérieur d'une seule cellule du classeur. Par ailleurs, `HtmlSaveOptions` vous permet de convertir le classeur entier — y compris les sparklines — en un fichier HTML autonome. Cet article vous guide à travers ces deux flux de travail, de bout en bout.

## **Flux de travail 1 — Rendre les sparklines en images et les intégrer dans les cellules**

Dans ce flux de travail, vous allez construire une feuille de calcul qui contient une petite plage de valeurs sources, attacher trois groupes de sparklines différents (Ligne, Colonne et Empilé/Win-Loss) à cette plage, rendre chaque groupe en tant que PNG, et écrire ces octets PNG dans des cellules adjacentes en tant qu'images intégrées. Le résultat final est un seul fichier `.xlsx` qui contient à la fois les sparklines actifs et leurs contreparties sous forme d'images rendues.

### **Instructions étape par étape**

1. Définissez un répertoire de travail et assurez-vous qu'il existe sur le disque.
2. Créez un nouveau `Workbook` et obtenez une référence à la première `Worksheet`.
3. Remplissez les cellules `A1` à `E1` avec cinq valeurs numériques d'exemple (par exemple, des ventes quotidiennes ou des relevés de température).
4. Ajoutez trois objets `SparklineGroup` à la feuille de calcul en appelant `worksheet.SparklineGroups.Add(...)` :
   - Un groupe `SparklineType.Line` ancré à `F1`, avec la plage de données `A1:E1`.
   - Un groupe `SparklineType.Column` ancré à `G1`, avec la plage de données `A1:E1`.
   - Un groupe `SparklineType.Stacked` (win/loss) ancré à `H1`, avec la plage de données `A1:E1`.
5. Créez une instance d'`ImageOrPrintOptions` et définissez sa propriété `ImageType` sur `ImageType.Png` afin que chaque sparkline soit rendu en tant que PNG transparent.
6. Pour chacun des trois groupes, rendez son sparkline unique à l'aide de `group.Sparklines[0].ToImage(memoryStream, imageOptions)`, convertissez le `MemoryStream` en `byte[]`, et affectez le tableau à `worksheet.Cells["F2"].EmbeddedImage`, `worksheet.Cells["G2"].EmbeddedImage`, et `worksheet.Cells["H2"].EmbeddedImage` respectivement.
7. Enregistrez le classeur sous le nom `output_with_sparklines.xlsx`.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;
using Aspose.Cells.Rendering;

// Créer un nouveau classeur et accéder à la première feuille de calcul
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Remplir les cellules A1:E1 avec des données d'exemple
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);

// Ajouter un groupe de graphiques sparkline en ligne ancré en F1 (colonne 5, ligne 0)
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);

// Ajouter un groupe de graphiques sparkline en colonnes ancré en G1 (colonne 6, ligne 0)
CellArea columnArea = new CellArea();
columnArea.StartColumn = 6;
columnArea.EndColumn = 6;
columnArea.StartRow = 0;
columnArea.EndRow = 0;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);

// Ajouter un groupe de graphiques sparkline Win/Loss (empilé) ancré en H1 (colonne 7, ligne 0)
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 7;
stackedArea.EndColumn = 7;
stackedArea.StartRow = 0;
stackedArea.EndRow = 0;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);

// Configurer les options d'image pour la sortie PNG
ImageOrPrintOptions imageOptions = new ImageOrPrintOptions();
imageOptions.ImageType = ImageType.Png;

// Convertir le graphique sparkline en ligne en image et l'intégrer dans la cellule F2
Sparkline lineSp = worksheet.SparklineGroups[lineIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    lineSp.ToImage(ms, imageOptions);
    worksheet.Cells["F2"].EmbeddedImage = ms.ToArray();
}

// Convertir le graphique sparkline en colonnes en image et l'intégrer dans la cellule G2
Sparkline columnSp = worksheet.SparklineGroups[columnIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    columnSp.ToImage(ms, imageOptions);
    worksheet.Cells["G2"].EmbeddedImage = ms.ToArray();
}

// Convertir le graphique sparkline Win/Loss en image et l'intégrer dans la cellule H2
Sparkline stackedSp = worksheet.SparklineGroups[stackedIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    stackedSp.ToImage(ms, imageOptions);
    worksheet.Cells["H2"].EmbeddedImage = ms.ToArray();
}

// Enregistrer le classeur sur le disque
workbook.Save("output_with_sparklines.xlsx");
```

Le code ci-dessus produit un classeur dans lequel chaque représentation visuelle d'un sparkline est dupliquée sous deux formes : le sparkline natif et actif ancré à la ligne 1, et une image PNG statique intégrée directement dans une cellule voisine de la ligne 2. Étant donné que les images résident à l'intérieur du fichier lui-même, le classeur reste un artefact unique et autonome qui peut être envoyé par e-mail ou archivé sans rompre les références aux images intégrées. Rendez chaque groupe de sparklines en PNG, convertissez le `MemoryStream` en `byte[]`, et affectez le tableau à la propriété `EmbeddedImage` de la cellule cible — l'affectation est ce qui fait de l'image une partie du contenu stocké de la cellule.

{{% alert color="primary" %}}
Étant donné que chaque groupe de sparklines est ancré à une seule cellule, vous pouvez y accéder via l'indexeur `group.Sparklines[0]` au lieu d'énumérer avec `foreach`. Cela permet de garder le code de rendu concis et correspond au modèle typique « un sparkline par cellule d'ancrage ». Le stockage des octets de l'image via `Cell.EmbeddedImage` nécessite Aspose.Cells 26.5 ou une version ultérieure.
{{% /alert %}}

## **Flux de travail 2 — Exporter la feuille de calcul contenant les sparklines vers HTML**

Une fois que le classeur contient des sparklines actifs (et éventuellement leurs contreparties sous forme d'images intégrées), la feuille de calcul entière peut être publiée sur le web en l'enregistrant au format HTML. La classe `HtmlSaveOptions` expose les paramètres dont vous avez besoin pour contrôler cet export ; dans ce flux de travail, vous réutiliserez le fichier `output_with_sparklines.xlsx` produit par le flux de travail 1 et le convertirez en un document HTML propre et monopage.

### **Instructions étape par étape**

1. Assurez-vous que le fichier `output_with_sparklines.xlsx` produit par le flux de travail 1 est disponible sur le disque dans votre répertoire de travail.
2. Chargez ce fichier dans une nouvelle instance de `Workbook`.
3. Instanciez `HtmlSaveOptions` et définissez sa propriété `ExportActiveWorksheetOnly` sur `true` afin que le fichier HTML résultant contienne uniquement la feuille de calcul active plutôt que le classeur entier.
4. Appelez `workbook.Save("sparklines.html", htmlOptions)` pour écrire la sortie HTML sur le disque.

```csharp
using System;
using System.IO;
using Aspose.Cells;

Workbook workbook = new Workbook("output_with_sparklines.xlsx");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.ExportActiveWorksheetOnly = true;
workbook.Save("sparklines.html", htmlOptions);
```

Le code ci-dessus prend le classeur contenant les sparklines issu du flux de travail 1 et le transforme en un fichier HTML portable. Les sparklines sont conservés en tant que rendus SVG ou PNG intégrés dans le HTML généré, selon le mode d'export, de sorte que les utilisateurs finaux peuvent visualiser les tendances dans n'importe quel navigateur moderne sans avoir besoin d'Excel installé. En définissant `ExportActiveWorksheetOnly` sur `true`, vous évitez de publier accidentellement des feuilles masquées ou des données auxiliaires — seule la feuille de calcul actuellement visible pour l'utilisateur est exportée.

{{% alert color="primary" %}}
La classe `HtmlSaveOptions` offre des propriétés supplémentaires pour affiner la sortie, telles que `ExportHiddenWorksheet`, `ExportImagesAsBase64`, et `Encoding`. Ajustez-les selon les besoins de votre cible de déploiement.
{{% /alert %}}

## **Résumé de l'API**

Les flux de travail ci-dessus s'appuient sur un petit ensemble d'API Aspose.Cells travaillant ensemble.

- `SparklineGroup` et l'accesseur de collection `worksheet.SparklineGroups` sont utilisés pour déclarer le type (Ligne, Colonne, Empilé), la plage de données, et la cellule d'ancrage de chaque groupe de sparklines. Dans cet article, chaque groupe est ancré à une seule cellule, de sorte que le groupe est atteint via `worksheet.SparklineGroups[i]`.
- `Sparkline` et l'indexeur `group.Sparklines[0]` renvoient le sparkline individuel à l'intérieur d'un groupe. Étant donné que chaque groupe dans l'exemple contient exactement un sparkline, aucune boucle `foreach` n'est nécessaire.
- `Sparkline.ToImage(Stream, ImageOrPrintOptions)` est la méthode de rendu qui écrit une image du sparkline dans un `Stream` fourni. La méthode renvoie `void` ; vous lisez les octets du flux après l'appel.
- `Cell.EmbeddedImage` est une propriété `byte[]` qui stocke une image à l'intérieur d'une seule cellule. Elle est disponible dans **Aspose.Cells 26.5 et versions ultérieures** et constitue la méthode recommandée pour réinjecter un sparkline rendu par `ToImage` dans le même classeur.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (un `bool`) limite l'export HTML à la feuille de calcul active. C'est l'une des propriétés les plus couramment utilisées de `HtmlSaveOptions` lors de la génération de rapports monopages.
- `ImageOrPrintOptions.ImageType` se trouve dans l'espace de noms `Aspose.Cells.Drawing` et sélectionne le format d'image (par exemple, `ImageType.Png`) utilisé lors du rendu avec `ToImage` et lors de l'impression des feuilles de calcul en images.

## **Articles connexes**

- [Sparklines dans Aspose.Cells for .NET](/cells/fr/net/sparkline/)
- [Insérer une image dans une cellule](/cells/fr/net/inserting-an-image-into-a-cell/)
- [Rendu de tableau à cellule unique avec SmartMarker | Aspose.Cells .NET](/cells/fr/net/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="csharp" >}}