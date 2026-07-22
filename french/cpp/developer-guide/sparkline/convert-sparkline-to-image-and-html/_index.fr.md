---
title: Convertir un sparkline en image et HTML avec Aspose.Cells for C++
linktitle: Convert Sparkline to Image and HTML
description: Apprenez à restituer les sparklines Aspose.Cells en images autonomes pour les intégrer dans des cellules et à exporter des feuilles de calcul contenant des sparklines au format HTML à l'aide de HtmlSaveOptions.
keywords: Aspose.Cells, C++, sparkline, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, restituer sparkline, convertir sparkline en image, exporter sparkline en HTML
type: docs
weight: 120
url: /fr/cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Les sparklines sont des mini-graphiques placés à l'intérieur des cellules d'une feuille de calcul. Aspose.Cells vous permet d'extraire chaque sparkline en tant qu'image autonome (pour l'intégrer dans une autre cellule ou un rapport externe) et également d'exporter la feuille de calcul entière contenant des sparklines au format HTML pour une distribution via navigateur. La propriété `Cell.EmbeddedImage` utilisée dans cet article est disponible dans **Aspose.Cells 26.5 et versions ultérieures**.
{{% /alert %}}

## **Introduction**

Les sparklines constituent un moyen compact de visualiser des tendances directement à l'intérieur d'une feuille de calcul. Alors que les utilisateurs d'Excel les voient en place, de nombreux scénarios réels nécessitent que le sparkline quitte la cellule — par exemple, pour être intégré dans une cellule différente sous forme d'image statique, joint à un e-mail automatisé, ou restitué dans le cadre d'un rapport HTML publié sur le web.

Aspose.Cells prend en charge ces deux opérations. La méthode `Sparkline.ToImage` restitue un sparkline individuel dans un flux, et les octets résultants peuvent être assignés à `Cell.EmbeddedImage` afin que l'image soit stockée à l'intérieur d'une seule cellule du classeur. Par ailleurs, `HtmlSaveOptions` vous permet de convertir l'ensemble du classeur — sparklines inclus — en un fichier HTML autonome. Cet article présente ces deux flux de travail de bout en bout.

## **Flux de travail 1 — Restituer les sparklines en images et les intégrer dans des cellules**

Dans ce flux de travail, vous allez construire une feuille de calcul contenant une petite plage de valeurs sources, attacher trois groupes de sparklines différents (Ligne, Colonne et Empilé/Win-Loss) à cette plage, restituer chaque groupe au format PNG, et écrire ces octets PNG dans des cellules adjacentes en tant qu'images intégrées. Le résultat final est un fichier `.xlsx` unique qui contient à la fois les sparklines natifs et leurs équivalents sous forme d'images rendues.

### **Instructions étape par étape**

1. Définissez un répertoire de travail et assurez-vous qu'il existe sur le disque.
2. Créez un nouveau `Workbook` et obtenez une référence à la première `Worksheet`.
3. Remplissez les cellules `A1` à `E1` avec cinq valeurs numériques d'exemple (par exemple, des ventes quotidiennes ou des relevés de température).
4. Ajoutez trois objets `SparklineGroup` à la feuille de calcul en appelant `worksheet.SparklineGroups.Add(...)` :
   - Un groupe `SparklineType.Line` ancré à `F1`, avec la plage de données `A1:E1`.
   - Un groupe `SparklineType.Column` ancré à `G1`, avec la plage de données `A1:E1`.
   - Un groupe `SparklineType.Stacked` (win/loss) ancré à `H1`, avec la plage de données `A1:E1`.
5. Construisez une instance `ImageOrPrintOptions` et définissez son `ImageType` à `ImageType.Png` afin que chaque sparkline soit restitué sous forme de PNG transparent.
6. Pour chacun des trois groupes, restituez son sparkline unique en utilisant `group.Sparklines[0].ToImage(memoryStream, imageOptions)`, convertissez le `MemoryStream` en `Vector<uint8_t>`, et assignez le tableau à `worksheet.Cells["F2"].EmbeddedImage`, `worksheet.Cells["G2"].EmbeddedImage`, et `worksheet.Cells["H2"].EmbeddedImage` respectivement.
7. Enregistrez le classeur sous le nom `output_with_sparklines.xlsx`.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);

    CellArea lineArea;
    lineArea.StartColumn = 5;
    lineArea.EndColumn = 5;
    lineArea.StartRow = 0;
    lineArea.EndRow = 0;
    int lineIdx = worksheet.GetSparklineGroups().Add(SparklineType::Line, U16String("A1:E1"), false, lineArea);

    CellArea columnArea;
    columnArea.StartColumn = 6;
    columnArea.EndColumn = 6;
    columnArea.StartRow = 0;
    columnArea.EndRow = 0;
    int columnIdx = worksheet.GetSparklineGroups().Add(SparklineType::Column, U16String("A1:E1"), false, columnArea);

    CellArea stackedArea;
    stackedArea.StartColumn = 7;
    stackedArea.EndColumn = 7;
    stackedArea.StartRow = 0;
    stackedArea.EndRow = 0;
    int stackedIdx = worksheet.GetSparklineGroups().Add(SparklineType::Stacked, U16String("A1:E1"), false, stackedArea);

    ImageOrPrintOptions imageOptions;
    imageOptions.SetImageType(ImageType::Png);

    Sparkline lineSp = worksheet.GetSparklineGroups().Get(lineIdx).GetSparklines().Get(0);
    Vector<uint8_t> lineImg = lineSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"F2").SetEmbeddedImage(lineImg);

    Sparkline columnSp = worksheet.GetSparklineGroups().Get(columnIdx).GetSparklines().Get(0);
    Vector<uint8_t> columnImg = columnSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"G2").SetEmbeddedImage(columnImg);

    Sparkline stackedSp = worksheet.GetSparklineGroups().Get(stackedIdx).GetSparklines().Get(0);
    Vector<uint8_t> stackedImg = stackedSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"H2").SetEmbeddedImage(stackedImg);

    workbook.Save(u"output_with_sparklines.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

Le code ci-dessus produit un classeur dans lequel chaque représentation visuelle d'un sparkline est dupliquée sous deux formes : le sparkline natif et actif ancré à la ligne 1, et une image PNG statique intégrée directement dans une cellule voisine de la ligne 2. Comme les images vivent à l'intérieur du fichier lui-même, le classeur reste un artefact autonome unique qui peut être envoyé par e-mail ou archivé sans rompre les références aux images intégrées. Restituez chaque groupe de sparklines en PNG, convertissez le `MemoryStream` en `Vector<uint8_t>`, et assignez le tableau à la propriété `EmbeddedImage` de la cellule cible — c'est cette affectation qui fait de l'image une partie du contenu stocké de la cellule.

{{% alert color="primary" %}}
Comme chaque groupe de sparklines est ancré à une seule cellule, vous pouvez y accéder via l'indexeur `group.Sparklines[0]` au lieu d'énumérer avec `foreach`. Cela permet de garder le code de rendu court et correspond au schéma typique « un sparkline par cellule d'ancrage ». Le stockage des octets de l'image via `Cell.EmbeddedImage` nécessite Aspose.Cells 26.5 ou une version ultérieure.
{{% /alert %}}

## **Flux de travail 2 — Exporter la feuille de calcul contenant des sparklines en HTML**

Une fois que le classeur contient des sparklines actifs (et éventuellement leurs équivalents en images intégrées), la feuille de calcul entière peut être publiée sur le web en l'enregistrant au format HTML. La classe `HtmlSaveOptions` expose les paramètres dont vous avez besoin pour contrôler cette exportation ; dans ce flux de travail, vous allez réutiliser le fichier `output_with_sparklines.xlsx` produit par le Flux de travail 1 et le convertir en un document HTML propre, d'une seule page.

### **Instructions étape par étape**

1. Assurez-vous que le fichier `output_with_sparklines.xlsx` produit par le Flux de travail 1 est disponible sur le disque dans votre répertoire de travail.
2. Chargez ce fichier dans une nouvelle instance `Workbook`.
3. Instanciez `HtmlSaveOptions` et définissez sa propriété `ExportActiveWorksheetOnly` à `true` afin que le fichier HTML résultant contienne uniquement la feuille de calcul active plutôt que l'ensemble du classeur.
4. Appelez `workbook.Save("sparklines.html", htmlOptions)` pour écrire le résultat HTML sur le disque.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook(u"output_with_sparklines.xlsx");
    HtmlSaveOptions htmlOptions;
    htmlOptions.SetExportActiveWorksheetOnly(true);
    workbook.Save(u"sparklines.html", htmlOptions);

    Aspose::Cells::Cleanup();
    return 0;
}
```

Le code ci-dessus prend le classeur contenant des sparklines du Flux de travail 1 et le transforme en un fichier HTML portable. Les sparklines sont conservés sous forme de rendus SVG ou PNG intégrés dans le HTML généré, selon le mode d'exportation, afin que les utilisateurs finaux puissent visualiser les tendances dans n'importe quel navigateur moderne sans avoir besoin d'Excel installé. En définissant `ExportActiveWorksheetOnly` à `true`, vous évitez de publier accidentellement des feuilles masquées ou des données auxiliaires — seule la feuille de calcul actuellement visible par l'utilisateur est exportée.

{{% alert color="primary" %}}
La classe `HtmlSaveOptions` offre des propriétés supplémentaires pour affiner la sortie, telles que `ExportHiddenWorksheet`, `ExportImagesAsBase64`, et `Encoding`. Ajustez-les selon les besoins de votre cible de déploiement.
{{% /alert %}}

## **Résumé de l'API**

Les flux de travail ci-dessus s'appuient sur un petit ensemble d'APIs Aspose.Cells travaillant ensemble.

- `SparklineGroup` et l'accesseur de collection `worksheet.SparklineGroups` sont utilisés pour déclarer le type (Line, Column, Stacked), la plage de données, et la cellule d'ancrage pour chaque groupe de sparklines. Dans cet article, chaque groupe est ancré à une seule cellule, de sorte que le groupe est atteint via `worksheet.SparklineGroups[i]`.
- `Sparkline` et l'indexeur `group.Sparklines[0]` renvoient le sparkline individuel à l'intérieur d'un groupe. Comme chaque groupe dans l'exemple contient exactement un sparkline, aucune boucle `foreach` n'est nécessaire.
- `Sparkline.ToImage(Stream, ImageOrPrintOptions)` est la méthode de rendu qui écrit une image du sparkline dans un `Stream` fourni. La méthode renvoie `void` ; vous lisez les octets à partir du flux après l'appel.
- `Cell.EmbeddedImage` est une propriété `Vector<uint8_t>` qui stocke une image à l'intérieur d'une seule cellule. Elle est disponible dans **Aspose.Cells 26.5 et versions ultérieures** et constitue la méthode recommandée pour réinjecter un sparkline rendu par `ToImage` dans le même classeur.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (un `bool`) restreint l'exportation HTML à la feuille de calcul active. C'est l'une des propriétés les plus couramment utilisées sur `HtmlSaveOptions` lors de la génération de rapports d'une seule page.
- `ImageOrPrintOptions.ImageType` se trouve dans le namespace `Aspose.Cells.Drawing` et sélectionne le format d'image (par exemple, `ImageType.Png`) utilisé lors du rendu avec `ToImage` et lors de l'impression des feuilles de calcul en images.

## **Articles connexes**

- [Sparklines dans Aspose.Cells for C++](/cells/fr/cpp/sparkline/)
- [Insertion d'une image dans une cellule](/cells/fr/cpp/inserting-an-image-into-a-cell/)
- [Rendu de tableau à cellule unique SmartMarker | Aspose.Cells for C++](/cells/fr/cpp/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="cpp" >}}