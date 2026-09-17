---
title: Convertir les sparklines en image et HTML dans Aspose.Cells for C++
description: Apprenez à rendre les sparklines Aspose.Cells en images autonomes pour les intégrer dans des cellules et à exporter des feuilles de calcul riches en sparklines vers HTML à l'aide de HtmlSaveOptions.
linktitle: Convertir une sparkline en image et HTML
keywords: Aspose.Cells, C++, sparkline, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, rendre sparkline, convertir sparkline en image, exporter sparkline en HTML
type: docs
weight: 120
url: /fr/cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Les sparklines sont des graphiques miniatures placés dans les cellules d'une feuille de calcul. Aspose.Cells vous permet d'extraire chaque sparkline sous forme d'image autonome (pour l'intégrer dans une autre cellule ou dans un rapport externe) et également d'exporter la feuille de calcul complète, riche en sparklines, vers HTML pour une distribution via navigateur. La propriété Cell.EmbeddedImage utilisée dans cet article est disponible dans Aspose.Cells 26.5 et versions ultérieures.

## **Introduction**
Les sparklines offrent un moyen compact de visualiser les tendances directement dans une feuille de calcul. Bien que les utilisateurs d'Excel les voient en place, de nombreux scénarios réels nécessitent qu'une sparkline quitte la cellule — par exemple, pour être intégrée dans une autre cellule en tant qu'image statique, jointe à un e-mail automatisé, ou rendue dans le cadre d'un rapport HTML publié sur le web.
Aspose.Cells prend en charge ces deux opérations. La méthode Sparkline.ToImage restitue une sparkline individuelle sous forme de tableau d'octets Vector<uint8_t>, et les octets résultants peuvent être assignés à Cell.EmbeddedImage afin que l'image soit stockée dans une seule cellule du classeur. Par ailleurs, HtmlSaveOptions vous permet de convertir l'intégralité du classeur — sparklines incluses — en un fichier HTML autonome. Cet article vous guide pas à pas à travers ces deux flux de travail.

## **Flux de travail 1 — Rendre les sparklines en images et les intégrer dans des cellules**
Dans ce flux de travail, vous allez construire une feuille de calcul contenant une petite plage de valeurs sources, attacher trois groupes de sparklines différents (Ligne, Colonne et Empilé/Win-Loss) à cette plage, rendre chaque groupe en PNG, et écrire ces octets PNG dans les cellules adjacentes en tant qu'images intégrées. Le résultat final est un unique fichier .xlsx qui contient à la fois les sparklines actives et leurs équivalents en images rendues.

### **Instructions étape par étape**
1. Définissez un répertoire de travail et assurez-vous qu'il existe sur le disque.
2. Créez un nouveau Workbook et obtenez une référence à la première Worksheet.
3. Remplissez les cellules A1 à E1 avec cinq valeurs numériques d'exemple (par exemple, des ventes quotidiennes ou des relevés de température).
4. Ajoutez trois objets SparklineGroup à la feuille de calcul en appelant worksheet.SparklineGroups.Add(...):
   - Un groupe SparklineType.Line ancré sur F1, avec la plage de données A1:E1.
   - Un groupe SparklineType.Column ancré sur G1, avec la plage de données A1:E1.
   - Un groupe SparklineType.Stacked (win/loss) ancré sur H1, avec la plage de données A1:E1.
5. Créez une instance ImageOrPrintOptions et définissez sa propriété ImageType sur ImageType.Png afin que chaque sparkline soit rendue sous forme de PNG transparent.
6. Pour chacun des trois groupes, rendez sa sparkline unique en utilisant group.Sparklines[0].ToImage(imageOptions) — l'appel renvoie directement les octets de l'image sous forme de Vector<uint8_t> — et assignez le tableau à worksheet.GetCells().Get("F2"].EmbeddedImage, worksheet.GetCells().Get("G2"].EmbeddedImage, et worksheet.GetCells().Get("H2"].EmbeddedImage respectivement.
7. Enregistrez le classeur sous output_with_sparklines.xlsx.

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

Le code ci-dessus produit un classeur où chaque représentation visuelle d'une sparkline est dupliquée sous deux formes : la sparkline native et active ancrée à la ligne 1, et une image PNG statique intégrée directement dans une cellule voisine à la ligne 2. Comme les images vivent dans le fichier lui-même, le classeur reste un artefact unique et autonome qui peut être envoyé par e-mail ou archivé sans rompre les références aux images intégrées. Rendez chaque groupe de sparklines en PNG — Sparkline.ToImage(ImageOrPrintOptions) renvoie directement les octets de l'image sous forme de Vector<uint8_t> — et assignez le tableau à la propriété EmbeddedImage de la cellule cible — l'assignation est ce qui fait que l'image fait partie du contenu stocké de la cellule.

{{% alert color="primary" %}}
Parce que chaque groupe de sparklines est ancré sur une seule cellule, vous pouvez l'adresser via l'indexeur group.Sparklines[0] au lieu d'énumérer avec foreach. Cela permet de garder le code de rendu court et correspond au modèle typique « une sparkline par cellule d'ancrage ». Le stockage des octets de l'image via Cell.EmbeddedImage nécessite Aspose.Cells 26.5 ou version ultérieure.

## **Flux de travail 2 — Exporter la feuille de calcul avec sparklines vers HTML**
Une fois que le classeur contient des sparklines actives (et éventuellement leurs équivalents en images intégrées), la feuille de calcul entière peut être publiée sur le web en l'enregistrant au format HTML. La classe HtmlSaveOptions expose les paramètres dont vous avez besoin pour contrôler cet export ; dans ce flux de travail, vous réutiliserez le fichier output_with_sparklines.xlsx produit par le flux de travail 1 et le convertirez en un document HTML propre d'une seule page.

### **Instructions étape par étape**
1. Assurez-vous que le fichier output_with_sparklines.xlsx produit par le flux de travail 1 est disponible sur le disque dans votre répertoire de travail.
2. Chargez ce fichier dans une nouvelle instance Workbook.
3. Instanciez HtmlSaveOptions et définissez sa propriété ExportActiveWorksheetOnly sur true afin que le fichier HTML résultant ne contienne que la feuille de calcul active plutôt que le classeur entier.
4. Appelez workbook.Save("sparklines.html", htmlOptions) pour écrire la sortie HTML sur le disque.

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

Le code ci-dessus prend le classeur riche en sparklines du flux de travail 1 et le transforme en un fichier HTML portable. Les sparklines sont conservées sous forme de rendus SVG ou PNG intégrés dans le HTML généré, selon le mode d'export, afin que les utilisateurs finaux puissent visualiser les tendances dans n'importe quel navigateur moderne sans avoir besoin d'Excel installé. En définissant ExportActiveWorksheetOnly sur true, vous évitez de publier accidentellement des feuilles cachées ou des données auxiliaires — seule la feuille de calcul actuellement visible par l'utilisateur est exportée.

{{% alert color="primary" %}}
La classe HtmlSaveOptions offre des propriétés supplémentaires pour affiner la sortie, telles que ExportHiddenWorksheet, ExportImagesAsBase64, et Encoding. Ajustez-les selon les besoins de votre cible de déploiement.

## **Résumé de l'API**
Les flux de travail ci-dessus reposent sur un petit ensemble d'API Aspose.Cells travaillant ensemble.
- SparklineGroup et l'accesseur de collection worksheet.SparklineGroups sont utilisés pour déclarer le type (Line, Column, Stacked), la plage de données et la cellule d'ancrage pour chaque groupe de sparklines. Dans cet article, chaque groupe est ancré sur une seule cellule, de sorte que le groupe est atteint via worksheet.SparklineGroups[i].
- Sparkline et l'indexeur group.Sparklines[0] renvoient la sparkline individuelle à l'intérieur d'un groupe. Comme chaque groupe de l'exemple contient exactement une sparkline, aucune boucle foreach n'est requise.
- Sparkline.ToImage(ImageOrPrintOptions) est la méthode de rendu qui renvoie une image de la sparkline directement sous forme de tableau d'octets Vector<uint8_t>.
- HtmlSaveOptions.ExportActiveWorksheetOnly (un bool) restreint l'export HTML à la feuille de calcul active. C'est l'une des propriétés les plus couramment utilisées sur HtmlSaveOptions lors de la génération de rapports d'une seule page.
- ImageOrPrintOptions.ImageType se trouve dans l'espace de noms Aspose.Cells.Drawing et sélectionne le format d'image (par exemple, ImageType.Png) utilisé lors du rendu avec ToImage et lors de l'impression de feuilles de calcul en images.

## **Articles connexes**
- [Sparklines dans Aspose.Cells for C++](/cells/fr/cpp/sparkline/)
- [Inserting an Image into a Cell](/cells/fr/cpp/inserting-an-image-into-a-cell/)
- [SmartMarker Single Cell Array Rendering | Aspose.Cells for C++](/cells/fr/cpp/SmartMarker-Single-Cell-Array-Rendering/)
{{% /alert %}}

{{% /alert %}}

{{% /alert %}}

- `/cells/cpp/sparkline/` - this is the parent topic for sparklines
- `/cells/cpp/inserting-an-image-into-a-cell/` - unrelated
- `/cells/cpp/SmartMarker-Single-Cell-Array-Rendering/` - unrelated
If the rule explicitly says not to include these, I should remove them. But that leaves just the heading with no content. Hmm.
- "dans les cellules d'une feuille de calcul" - correct
- "à la feuille de calcul" - correct
- "du classeur" - correct
- "aux cellules" - correct
- "dans une feuille de calcul" - correct
- "Workbook, Worksheet, Cells, Cell, Style, etc." - these are class names, keep in English
- "SparklineGroup, Sparkline, SparklineType" - keep in English
- "ImageOrPrintOptions, HtmlSaveOptions" - keep in English
- "Vector<uint8_t>" - keep in English
"and write those PNG bytes into adjacent cells as embedded images"
"et écrire ces octets PNG dans les cellules adjacentes en tant qu'images intégrées"
"the workbook remains a single self-contained artifact"
"le classeur reste un artefact unique et autonome"
"Render each sparkline group as a PNG — Sparkline.ToImage(ImageOrPrintOptions) returns the picture bytes directly as a Vector<uint8_t> — and assign the array to the EmbeddedImage property of the target cell"
"Rendez chaque groupe de sparklines en PNG — Sparkline.ToImage(ImageOrPrintOptions) renvoie directement les octets de l'image sous forme de Vector<uint8_t> — et assignez le tableau à la propriété EmbeddedImage de la cellule cible"Three closing tags. The original has 3 alert blocks but each has a duplicate open, so 3 actual closes + 3 extras = 6 closes. And I count 3 opens + 3 malformed "opens" (which are actually duplicates of opens, not real opens). So 3 real opens + 3 malformed opens = 6 opens visually but only 3 actual open tags. Then 6 closes at the end. That doesn't match.So after first paragraph: OPEN 1 still open.After this: OPEN 1 still open, OPEN 3 still open.After this: OPEN 1 still open, OPEN 3 still open, OPEN 5 still open.CLOSE 4 closes OPEN 5, CLOSE 5 closes OPEN 3, CLOSE 6 closes OPEN 1.
"Learn how to render Aspose.Cells sparklines to standalone images for cell embedding and export sparkline-rich worksheets to HTML using HtmlSaveOptions."
Also, the inline code in prose like `Sparkline.ToImage`, `Cell.EmbeddedImage`, `HtmlSaveOptions`, etc. - these are API identifiers, keep in English.
The class names like `Workbook`, `Worksheet`, `Cell`, `ImageOrPrintOptions`, `HtmlSaveOptions`, `SparklineGroup`, `Sparkline`, `SparklineType` - keep in English.
Method names like `Add`, `ToImage`, `Save` - keep in English.
Property names like `Sparklines`, `SparklineGroups`, `EmbeddedImage`, `ImageType`, `ExportActiveWorksheetOnly` - keep in English.
Enum values like `ImageType.Png`, `SparklineType.Line`, `SparklineType.Column`, `SparklineType.Stacked` - keep in English.
linktitle: Convertir une sparkline en image et HTML
keywords: Aspose.Cells, C++, sparkline, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, rendre sparkline, convertir sparkline en image, exporter sparkline en HTML
type: docs
weight: 120
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"

{{< app/cells/assistant language="cpp" >}}