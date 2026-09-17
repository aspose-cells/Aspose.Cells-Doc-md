---
title: Convertir une sparkline en image et en HTML dans Aspose.Cells for .NET
linktitle: Convertir une sparkline en image et en HTML dans Aspose.Cells for .NET
description: Apprenez à convertir les sparklines Aspose.Cells en images autonomes pour l'insertion dans des cellules et à exporter des feuilles de calcul contenant des sparklines vers HTML à l'aide de HtmlSaveOptions.
keywords: Aspose.Cells, .NET, sparkline, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, rendre une sparkline, convertir une sparkline en image, exporter une sparkline vers HTML
type: docs
weight: 120
url: /fr/net/convert-sparkline-to-image-and-html/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Les sparklines sont des mini-graphiques placés à l'intérieur des cellules d'une feuille de calcul. Aspose.Cells vous permet d'extraire chaque sparkline sous forme d'image autonome (pour l'incorporer dans une autre cellule ou dans un rapport externe) et également d'exporter la feuille de calcul complète contenant des sparklines vers HTML pour une distribution via navigateur. La propriété `Cell.EmbeddedImage` utilisée dans cet article est disponible dans **Aspose.Cells 26.5 et versions ultérieures**.

## **Introduction**
Les sparklines offrent un moyen compact de visualiser des tendances directement dans une feuille de calcul. Si les utilisateurs d'Excel les voient à leur emplacement, de nombreux scénarios réels nécessitent que la sparkline quitte la cellule — par exemple, pour être incorporée dans une autre cellule sous forme d'image statique, jointe à un e-mail automatisé, ou rendue dans le cadre d'un rapport HTML publié sur le web.
Aspose.Cells prend en charge ces deux opérations. La méthode `Sparkline.ToImage` restitue une sparkline individuelle vers un flux, et les octets résultants peuvent être affectés à `Cell.EmbeddedImage` afin que l'image soit stockée dans une seule cellule du classeur. Par ailleurs, `HtmlSaveOptions` vous permet de convertir l'intégralité du classeur — sparklines incluses — en un fichier HTML autonome. Cet article présente ces deux flux de travail de bout en bout.

## **Flux de travail 1 — Rendre les sparklines en images et les incorporer dans des cellules**
Dans ce flux de travail, vous allez créer une feuille de calcul contenant une petite plage de valeurs sources, attacher trois groupes de sparklines différents (Ligne, Colonne et Empilé/Gain-Perte) à cette plage, rendre chaque groupe au format PNG, puis écrire ces octets PNG dans des cellules adjacentes en tant qu'images incorporées. Le résultat final est un fichier `.xlsx` unique qui contient à la fois les sparklines actives et leurs contreparties sous forme d'images rendues.

### **Instructions étape par étape**
1. Créez un nouveau `Workbook` et obtenez une référence à la première `Worksheet`.
2. Remplissez les cellules `A1` à `E1` avec cinq valeurs numériques d'exemple (par exemple, des ventes quotidiennes ou des relevés de température).
3. Ajoutez trois objets `SparklineGroup` à la feuille de calcul en appelant `worksheet.SparklineGroups.Add(...)` :
   - Un groupe `SparklineType.Line` ancré en `F1`, avec une plage de données `A1:E1`.
   - Un groupe `SparklineType.Column` ancré en `G1`, avec une plage de données `A1:E1`.
   - Un groupe `SparklineType.Stacked` (gain/perte) ancré en `H1`, avec une plage de données `A1:E1`.
4. Créez une instance d'`ImageOrPrintOptions` et définissez sa propriété `ImageType` sur `ImageType.Png` afin que chaque sparkline soit rendue sous forme d'image PNG.
5. Enregistrez le classeur sous le nom `output_with_sparklines.xlsx`.

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
// Remplir des données d'exemple dans les cellules A1:E1
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);
// Ajouter un groupe de sparklines de type Ligne ancré à F1 (colonne 5, ligne 0)
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);
// Ajouter un groupe de sparklines de type Colonne ancré à G1 (colonne 6, ligne 0)
CellArea columnArea = new CellArea();
columnArea.StartColumn = 6;
columnArea.EndColumn = 6;
columnArea.StartRow = 0;
columnArea.EndRow = 0;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);
// Ajouter un groupe de sparklines de type Win/Loss (Empilé) ancré à H1 (colonne 7, ligne 0)
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 7;
stackedArea.EndColumn = 7;
stackedArea.StartRow = 0;
stackedArea.EndRow = 0;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);
// Configurer les options d'image pour la sortie PNG
ImageOrPrintOptions imageOptions = new ImageOrPrintOptions();
imageOptions.ImageType = ImageType.Png;
// Convertir la sparkline de type Ligne en image et l'incorporer dans la cellule F2
Sparkline lineSp = worksheet.SparklineGroups[lineIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    lineSp.ToImage(ms, imageOptions);
    worksheet.Cells["F2"].EmbeddedImage = ms.ToArray();
}
// Convertir la sparkline de type Colonne en image et l'incorporer dans la cellule G2
Sparkline columnSp = worksheet.SparklineGroups[columnIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    columnSp.ToImage(ms, imageOptions);
    worksheet.Cells["G2"].EmbeddedImage = ms.ToArray();
}
// Convertir la sparkline de type Win/Loss en image et l'incorporer dans la cellule H2
Sparkline stackedSp = worksheet.SparklineGroups[stackedIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    stackedSp.ToImage(ms, imageOptions);
    worksheet.Cells["H2"].EmbeddedImage = ms.ToArray();
}
// Enregistrer le classeur sur le disque
workbook.Save("output_with_sparklines.xlsx");
```

Le code ci-dessus produit un classeur dans lequel chaque représentation visuelle d'une sparkline existe sous deux formes : la sparkline native active ancrée à la ligne 1, et une image PNG statique incorporée directement dans une cellule voisine de la ligne 2. Étant donné que les images sont stockées dans le fichier lui-même, le classeur reste un artefact autonome unique qui peut être envoyé par e-mail ou archivé sans rompre les références aux images incorporées.

{{% alert color="primary" %}}
Étant donné que chaque groupe de sparklines est ancré à une seule cellule, vous pouvez y accéder via l'indexeur `group.Sparklines[0]` au lieu d'énumérer avec `foreach`. Cela permet de garder le code de rendu concis et correspond au modèle typique « une sparkline par cellule d'ancrage ». Le stockage des octets de l'image via `Cell.EmbeddedImage` nécessite Aspose.Cells 26.5 ou version ultérieure.

## **Flux de travail 2 — Exporter la feuille de calcul contenant des sparklines vers HTML**
Une fois que le classeur contient des sparklines actives (et éventuellement leurs contreparties sous forme d'images incorporées), la feuille de calcul entière peut être publiée sur le web en l'enregistrant au format HTML. La classe `HtmlSaveOptions` expose les paramètres dont vous avez besoin pour contrôler cet export ; dans ce flux de travail, vous réutiliserez le fichier `output_with_sparklines.xlsx` produit par le flux de travail 1 et le convertirez en un document HTML propre et monopage.

### **Instructions étape par étape**
1. Assurez-vous que le fichier `output_with_sparklines.xlsx` produit par le flux de travail 1 est disponible sur le disque dans votre répertoire de travail.
2. Chargez ce fichier dans une nouvelle instance de `Workbook`.
3. Instanciez `HtmlSaveOptions` et définissez sa propriété `ExportActiveWorksheetOnly` sur `true` afin que le fichier HTML résultant ne contienne que la feuille de calcul active au lieu du classeur entier.
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

Le code ci-dessus prend le classeur contenant des sparklines du flux de travail 1 et le transforme en un fichier HTML portable. Les groupes de sparklines sont rendus sous forme d'images intégrées dans le tableau HTML généré, de sorte que les utilisateurs finaux peuvent visualiser les tendances dans n'importe quel navigateur moderne sans avoir besoin d'Excel installé. En définissant `ExportActiveWorksheetOnly` sur `true`, vous évitez de publier accidentellement des feuilles masquées ou des données auxiliaires — seule la feuille de calcul actuellement visible par l'utilisateur est exportée.

{{% alert color="primary" %}}
La classe `HtmlSaveOptions` offre des propriétés supplémentaires pour ajuster finement la sortie, telles que `ExportHiddenWorksheet`, `ExportImagesAsBase64` et `Encoding`. Ajustez-les selon les besoins de votre cible de déploiement.

## **Résumé de l'API**
Les flux de travail ci-dessus reposent sur un petit ensemble d'API Aspose.Cells travaillant ensemble.
- `SparklineGroup` et l'accesseur de collection `worksheet.SparklineGroups` sont utilisés pour déclarer le type (Ligne, Colonne, Empilé), la plage de données et la cellule d'ancrage de chaque groupe de sparklines. Dans cet article, chaque groupe est ancré à une seule cellule, donc le groupe est accessible via `worksheet.SparklineGroups[i]`.
- `Sparkline` et l'indexeur `group.Sparklines[0]` renvoient la sparkline individuelle au sein d'un groupe. Comme chaque groupe de l'exemple contient exactement une sparkline, aucune boucle `foreach` n'est nécessaire.
- `Sparkline.ToImage(Stream, ImageOrPrintOptions)` est la méthode de rendu qui écrit une image de la sparkline dans un `Stream` fourni. La méthode renvoie `void` ; vous lisez les octets depuis le flux après l'appel.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (un `bool`) restreint l'export HTML à la feuille de calcul active. C'est l'une des propriétés les plus couramment utilisées de `HtmlSaveOptions` lors de la génération de rapports monopage.
- `ImageOrPrintOptions.ImageType` se trouve dans l'espace de noms `Aspose.Cells.Drawing` et sélectionne le format d'image (par exemple, `ImageType.Png`) utilisé lors du rendu avec `ToImage` et lors de l'impression de feuilles de calcul en images.

## **Articles connexes**
- [Création de sparklines dans Aspose.Cells for .NET](/fr/net/creating-sparklines/)
{{% /alert %}}

{{% /alert %}}

{{% /alert %}}

{{< app/cells/assistant language="csharp" >}}