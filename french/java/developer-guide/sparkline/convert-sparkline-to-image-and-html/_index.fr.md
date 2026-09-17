---
title: Convertir une sparkline en image et en HTML avec Aspose.Cells for Java
description: Apprenez à rendre les sparklines Aspose.Cells en images autonomes pour les intégrer dans des cellules et à exporter des feuilles de calcul enrichies de sparklines vers HTML à l'aide de HtmlSaveOptions.
linktitle: Convertir une sparkline en image et en HTML
keywords: Aspose.Cells, Java, sparkline, Sparkline.toImage, Cell.EmbeddedImage, HtmlSaveOptions, rendre sparkline, convertir sparkline en image, exporter sparkline en HTML
type: docs
weight: 120
url: /fr/java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Les sparklines sont des mini-graphiques placés à l'intérieur des cellules d'une feuille de calcul. Aspose.Cells vous permet d'extraire chaque sparkline sous forme d'image autonome (pour l'intégrer dans une autre cellule ou dans un rapport externe) et également d'exporter la feuille de calcul enrichie de sparklines au format HTML pour une distribution via navigateur. La propriété `Cell.EmbeddedImage` utilisée dans cet article est disponible dans **Aspose.Cells 26.5 et versions ultérieures**.

## **Introduction**
Les sparklines offrent un moyen compact de visualiser des tendances directement dans une feuille de calcul. Bien que les utilisateurs d'Excel les voient en place, de nombreux scénarios réels exigent qu'une sparkline quitte la cellule — par exemple, pour être intégrée dans une autre cellule sous forme d'image statique, jointe à un e-mail automatisé, ou rendue dans le cadre d'un rapport HTML publié sur le web.
Aspose.Cells prend en charge ces deux opérations. La méthode `Sparkline.toImage` effectue le rendu d'une sparkline individuelle dans un flux, et les octets résultants peuvent être affectés à `Cell.EmbeddedImage` (via `setEmbeddedImage`) afin que l'image soit stockée dans une seule cellule du classeur. Par ailleurs, `HtmlSaveOptions` permet de convertir l'intégralité du classeur — sparklines incluses — en un fichier HTML autonome. Cet article présente ces deux workflows de bout en bout.

## **Workflow 1 — Rendre les sparklines en images et les intégrer dans des cellules**
Dans ce workflow, vous allez créer une feuille de calcul contenant une petite plage de valeurs sources, attacher trois groupes de sparklines différents (Line, Column et Stacked/Win-Loss) à cette plage, effectuer le rendu de chaque groupe en PNG, puis écrire ces octets PNG dans des cellules adjacentes sous forme d'images intégrées. Le résultat final est un fichier `.xlsx` unique contenant à la fois les sparklines actives et leurs équivalents sous forme d'images rendues.

### **Instructions étape par étape**
1. Définissez un répertoire de travail et assurez-vous qu'il existe sur le disque.
2. Créez un nouveau `Workbook` et obtenez une référence à la première `Worksheet`.
3. Remplissez les cellules `A1` à `E1` avec cinq valeurs numériques d'exemple (par exemple, des ventes quotidiennes ou des relevés de température).
4. Ajoutez trois objets `SparklineGroup` à la feuille de calcul en appelant `worksheet.getSparklineGroups().add(...)` :
   - Un groupe `SparklineType.LINE` ancré à `F1`, avec une plage de données `A1:E1`.
   - Un groupe `SparklineType.COLUMN` ancré à `G1`, avec une plage de données `A1:E1`.
   - Un groupe `SparklineType.STACKED` (win/loss) ancré à `H1`, avec une plage de données `A1:E1`.
5. Construisez une instance de `ImageOrPrintOptions` et appelez `setImageType(ImageType.PNG)` afin que chaque sparkline soit rendue sous forme de PNG transparent.
6. Appelez `workbook.save("output_with_sparklines.xlsx")` pour enregistrer le classeur sur le disque.

```java
import com.aspose.cells.*;
import java.io.*;
// Créer un nouveau classeur et accéder à la première feuille de calcul
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Remplir des données d'exemple dans les cellules A1:E1
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Ajouter un groupe de sparklines de type Ligne ancré à F1 (colonne 5, ligne 0)
CellArea lineArea = CellArea.createCellArea(5, 0, 5, 0);
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);
// Ajouter un groupe de sparklines de type Colonne ancré à G1 (colonne 6, ligne 0)
CellArea columnArea = CellArea.createCellArea(6, 0, 6, 0);
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);
// Ajouter un groupe de sparklines de type Victoire/Défaite (Empilé) ancré à H1 (colonne 7, ligne 0)
CellArea stackedArea = CellArea.createCellArea(7, 0, 7, 0);
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);
// Configurer les options d'image pour la sortie PNG
ImageOrPrintOptions imageOptions = new ImageOrPrintOptions();
imageOptions.setImageType(ImageType.PNG);
// Convertir la sparkline Ligne en image et l'incorporer dans la cellule F2
Sparkline lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
ByteArrayOutputStream lineMs = new ByteArrayOutputStream();
lineSp.toImage(lineMs, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(lineMs.toByteArray());
// Convertir la sparkline Colonne en image et l'incorporer dans la cellule G2
Sparkline columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
ByteArrayOutputStream columnMs = new ByteArrayOutputStream();
columnSp.toImage(columnMs, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(columnMs.toByteArray());
// Convertir la sparkline Victoire/Défaite en image et l'incorporer dans la cellule H2
Sparkline stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
ByteArrayOutputStream stackedMs = new ByteArrayOutputStream();
stackedSp.toImage(stackedMs, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(stackedMs.toByteArray());
// Enregistrer le classeur sur le disque
workbook.save("output_with_sparklines.xlsx");
```

Le code ci-dessus produit un classeur dans lequel chaque représentation visuelle d'une sparkline est dupliquée sous deux formes : la sparkline native active ancrée à la ligne 1, et une image PNG statique intégrée directement dans une cellule voisine de la ligne 2. Comme les images vivent dans le fichier lui-même, le classeur reste un artefact autonome unique qui peut être envoyé par e-mail ou archivé sans rompre les références aux images intégrées. Effectuez le rendu de chaque groupe de sparklines en PNG, convertissez le `ByteArrayOutputStream` en `byte[]`, et affectez le tableau à la propriété `EmbeddedImage` de la cellule cible via `setEmbeddedImage(byte[])` — c'est cette affectation qui fait de l'image une partie du contenu stocké de la cellule.

{{% alert color="primary" %}}
Comme chaque groupe de sparklines est ancré à une seule cellule, vous pouvez y accéder via l'indexeur `group.getSparklines().get(0)` au lieu d'énumérer avec une boucle `for`. Cela permet de garder le code de rendu court et correspond au schéma typique « une sparkline par cellule d'ancrage ». Le stockage des octets de l'image via `Cell.EmbeddedImage` (défini via `setEmbeddedImage`) nécessite Aspose.Cells 26.5 ou version ultérieure.

## **Workflow 2 — Exporter la feuille de calcul avec sparklines vers HTML**
Une fois que le classeur contient des sparklines actives (et éventuellement des équivalents sous forme d'images intégrées), la feuille de calcul entière peut être publiée sur le web en l'enregistrant au format HTML. La classe `HtmlSaveOptions` expose les paramètres dont vous avez besoin pour contrôler cet export ; dans ce workflow, vous réutiliserez le fichier `output_with_sparklines.xlsx` produit par le Workflow 1 et le convertirez en un document HTML propre d'une seule page.

### **Instructions étape par étape**
1. Assurez-vous que le fichier `output_with_sparklines.xlsx` produit par le Workflow 1 est disponible sur le disque dans votre répertoire de travail.
2. Chargez ce fichier dans une nouvelle instance de `Workbook`.
3. Instanciez `HtmlSaveOptions` et appelez `setExportActiveWorksheetOnly(true)` afin que le fichier HTML résultant contienne uniquement la feuille de calcul active plutôt que l'intégralité du classeur.
4. Appelez `workbook.save("sparklines.html", htmlOptions)` pour écrire la sortie HTML sur le disque.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("output_with_sparklines.xlsx");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

Le code ci-dessus prend le classeur enrichi de sparklines du Workflow 1 et le transforme en un fichier HTML portable. Les sparklines sont conservées en tant que rendus SVG ou PNG inline dans le HTML généré, en fonction du mode d'export, de sorte que les utilisateurs finaux puissent visualiser les tendances dans n'importe quel navigateur moderne sans avoir besoin d'Excel installé. En définissant `ExportActiveWorksheetOnly` à `true` via `setExportActiveWorksheetOnly(true)`, vous évitez de publier par inadvertance des feuilles cachées ou des données auxiliaires — seule la feuille de calcul actuellement visible par l'utilisateur est exportée.

{{% alert color="primary" %}}
La classe `HtmlSaveOptions` offre des propriétés supplémentaires pour ajuster finement la sortie, telles que `ExportHiddenWorksheet`, `ExportImagesAsBase64`, et `Encoding`. Ajustez-les selon les besoins de votre cible de déploiement.

## **Résumé de l'API**
Les workflows ci-dessus reposent sur un petit ensemble d'API Aspose.Cells fonctionnant ensemble.
- `SparklineGroup` et l'accesseur de collection `worksheet.getSparklineGroups()` sont utilisés pour déclarer le type (Line, Column, Stacked), la plage de données, et la cellule d'ancrage de chaque groupe de sparklines. Dans cet article, chaque groupe est ancré à une seule cellule, de sorte que le groupe est atteint via `worksheet.getSparklineGroups().get(i)`.
- `Sparkline` et l'indexeur `group.getSparklines().get(0)` renvoient la sparkline individuelle au sein d'un groupe. Comme chaque groupe de l'exemple contient exactement une sparkline, aucune boucle `for` n'est nécessaire.
- `Sparkline.toImage(Stream, ImageOrPrintOptions)` est la méthode de rendu qui écrit une image de la sparkline dans un `Stream` fourni. La méthode renvoie `void` ; vous lisez les octets à partir du flux après l'appel.
- `HtmlSaveOptions.setExportActiveWorksheetOnly(boolean)` restreint l'export HTML à la feuille de calcul active. C'est l'une des propriétés les plus utilisées de `HtmlSaveOptions` lors de la génération de rapports d'une seule page.
- `ImageOrPrintOptions.setImageType(ImageType)` se trouve dans le package `com.aspose.cells.drawing` et sélectionne le format d'image (par exemple, `ImageType.PNG`) utilisé lors du rendu avec `toImage` et lors de l'impression des feuilles de calcul en images.

## **Articles connexes**
- [Sparklines dans Aspose.Cells for Java](/cells/fr/java/sparkline/)
- [Insertion d'une image dans une cellule](/cells/fr/java/inserting-an-image-into-a-cell/)
- [Rendu de tableau à cellule unique SmartMarker | Aspose.Cells Java](/cells/fr/java/SmartMarker-Single-Cell-Array-Rendering/)
{{% /alert %}}

{{% /alert %}}

{{% /alert %}}`java

{{< app/cells/assistant language="java" >}}