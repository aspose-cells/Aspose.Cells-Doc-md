---
title: Convertir Sparkline en image et HTML avec Aspose.Cells for Java
linktitle: Convert Sparkline to Image and HTML
description: Apprenez à rendre les sparklines Aspose.Cells en images autonomes pour l'intégration dans une cellule et à exporter des feuilles de calcul contenant des sparklines au format HTML à l'aide de HtmlSaveOptions.
keywords: Aspose.Cells, Java, sparkline, Sparkline.toImage, Cell.EmbeddedImage, HtmlSaveOptions, rendre sparkline, convertir sparkline en image, exporter sparkline en HTML
type: docs
weight: 120
url: /fr/java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Les sparklines sont des mini-graphiques placés à l'intérieur des cellules d'une feuille de calcul. Aspose.Cells vous permet d'extraire chaque sparkline sous forme d'image autonome (pour l'incorporer dans une autre cellule ou un rapport externe) et également d'exporter la feuille de calcul entière contenant des sparklines au format HTML pour une distribution basée sur un navigateur. La propriété `Cell.EmbeddedImage` utilisée dans cet article est disponible dans **Aspose.Cells 26.5 et versions ultérieures**.
{{% /alert %}}

## **Introduction**

Les sparklines constituent un moyen compact de visualiser des tendances directement à l'intérieur d'une feuille de calcul. Bien que les utilisateurs Excel les voient en place, de nombreux scénarios réels nécessitent que la sparkline quitte la cellule — par exemple, pour être intégrée dans une autre cellule sous forme d'image statique, jointe à un e-mail automatisé, ou rendue dans le cadre d'un rapport HTML publié sur le web.

Aspose.Cells prend en charge ces deux opérations. La méthode `Sparkline.toImage` rend une sparkline individuelle dans un flux, et les octets résultants peuvent être affectés à `Cell.EmbeddedImage` (via `setEmbeddedImage`) afin que l'image soit stockée à l'intérieur d'une seule cellule du classeur. Séparément, `HtmlSaveOptions` vous permet de convertir le classeur entier — sparklines incluses — en un fichier HTML autonome. Cet article vous guide à travers ces deux flux de travail de bout en bout.

## **Flux de travail 1 — Rendre les sparklines en images et les intégrer dans les cellules**

Dans ce flux de travail, vous allez construire une feuille de calcul qui contient une petite plage de valeurs sources, attacher trois groupes de sparklines différents (Ligne, Colonne et Empilée/Win-Loss) à cette plage, rendre chaque groupe sous forme de PNG, et écrire ces octets PNG dans des cellules adjacentes sous forme d'images intégrées. Le résultat final est un seul fichier `.xlsx` qui contient à la fois les sparklines actives et leurs contreparties d'image rendues.

### **Instructions étape par étape**

1. Définissez un répertoire de travail et assurez-vous qu'il existe sur le disque.
2. Créez un nouveau `Workbook` et obtenez une référence à la première `Worksheet`.
3. Remplissez les cellules `A1` à `E1` avec cinq valeurs numériques d'exemple (par exemple, des ventes quotidiennes ou des relevés de température).
4. Ajoutez trois objets `SparklineGroup` à la feuille de calcul en appelant `worksheet.getSparklineGroups().add(...)` :
   - Un groupe `SparklineType.LINE` ancré à `F1`, avec la plage de données `A1:E1`.
   - Un groupe `SparklineType.COLUMN` ancré à `G1`, avec la plage de données `A1:E1`.
   - Un groupe `SparklineType.STACKED` (win/loss) ancré à `H1`, avec la plage de données `A1:E1`.
5. Construisez une instance `ImageOrPrintOptions` et appelez `setImageType(ImageType.PNG)` afin que chaque sparkline soit rendue sous forme de PNG transparent.
6. Pour chacun des trois groupes, rendez sa sparkline unique en utilisant `group.getSparklines().get(0).toImage(byteArrayOutputStream, imageOptions)`, convertissez le `ByteArrayOutputStream` en `byte[]`, et affectez le tableau via `worksheet.getCells().get("F2").setEmbeddedImage(...)`, `worksheet.getCells().get("G2").setEmbeddedImage(...)`, et `worksheet.getCells().get("H2").setEmbeddedImage(...)` respectivement.
7. Appelez `workbook.save("output_with_sparklines.xlsx")` pour enregistrer le classeur sur le disque.

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

// Ajouter un groupe de sparklines Win/Loss (Empilé) ancré à H1 (colonne 7, ligne 0)
CellArea stackedArea = CellArea.createCellArea(7, 0, 7, 0);
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);

// Configurer les options d'image pour la sortie PNG
ImageOrPrintOptions imageOptions = new ImageOrPrintOptions();
imageOptions.setImageType(ImageType.PNG);

// Convertir la sparkline de type Ligne en image et l'incorporer dans la cellule F2
Sparkline lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
ByteArrayOutputStream lineMs = new ByteArrayOutputStream();
lineSp.toImage(lineMs, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(lineMs.toByteArray());

// Convertir la sparkline de type Colonne en image et l'incorporer dans la cellule G2
Sparkline columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
ByteArrayOutputStream columnMs = new ByteArrayOutputStream();
columnSp.toImage(columnMs, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(columnMs.toByteArray());

// Convertir la sparkline Win/Loss en image et l'incorporer dans la cellule H2
Sparkline stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
ByteArrayOutputStream stackedMs = new ByteArrayOutputStream();
stackedSp.toImage(stackedMs, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(stackedMs.toByteArray());

// Enregistrer le classeur sur le disque
workbook.save("output_with_sparklines.xlsx");
```

Le code ci-dessus produit un classeur dans lequel chaque représentation visuelle d'une sparkline est dupliquée sous deux formes : la sparkline native active ancrée à la ligne 1, et une image PNG statique intégrée directement dans une cellule voisine de la ligne 2. Étant donné que les images vivent à l'intérieur du fichier lui-même, le classeur reste un artefact unique et autonome qui peut être envoyé par e-mail ou archivé sans rompre les références d'image intégrées. Rendez chaque groupe de sparklines sous forme de PNG, convertissez le `ByteArrayOutputStream` en `byte[]`, et affectez le tableau à la propriété `EmbeddedImage` de la cellule cible via `setEmbeddedImage(byte[])` — l'affectation est ce qui fait que l'image fait partie du contenu stocké de la cellule.

{{% alert color="primary" %}}
Étant donné que chaque groupe de sparklines est ancré à une seule cellule, vous pouvez y accéder via l'indexeur `group.getSparklines().get(0)` au lieu d'énumérer avec une boucle `for`. Cela permet de garder le code de rendu court et correspond au modèle typique « une sparkline par cellule d'ancrage ». Le stockage des octets de l'image via `Cell.EmbeddedImage` (défini via `setEmbeddedImage`) nécessite Aspose.Cells 26.5 ou une version ultérieure.
{{% /alert %}}

## **Flux de travail 2 — Exporter la feuille de calcul avec sparklines au format HTML**

Une fois que le classeur contient des sparklines actives (et éventuellement des contreparties d'image intégrées), la feuille de calcul entière peut être publiée sur le web en l'enregistrant au format HTML. La classe `HtmlSaveOptions` expose les paramètres dont vous avez besoin pour contrôler cette exportation ; dans ce flux de travail, vous réutiliserez le fichier `output_with_sparklines.xlsx` produit par le Flux de travail 1 et le convertirez en un document HTML propre et d'une seule page.

### **Instructions étape par étape**

1. Assurez-vous que le fichier `output_with_sparklines.xlsx` produit par le Flux de travail 1 est disponible sur le disque dans votre répertoire de travail.
2. Chargez ce fichier dans une nouvelle instance `Workbook`.
3. Instanciez `HtmlSaveOptions` et appelez `setExportActiveWorksheetOnly(true)` afin que le fichier HTML résultant ne contienne que la feuille de calcul active plutôt que le classeur entier.
4. Appelez `workbook.save("sparklines.html", htmlOptions)` pour écrire la sortie HTML sur le disque.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook("output_with_sparklines.xlsx");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

Le code ci-dessus prend le classeur contenant des sparklines du Flux de travail 1 et le transforme en un fichier HTML portable. Les sparklines sont conservées sous forme de rendus SVG ou PNG intégrés dans le HTML généré, selon le mode d'exportation, de sorte que les utilisateurs finaux peuvent consulter les tendances dans n'importe quel navigateur moderne sans avoir besoin d'Excel installé. En définissant `ExportActiveWorksheetOnly` sur `true` via `setExportActiveWorksheetOnly(true)`, vous évitez de publier par inadvertance des feuilles masquées ou des données auxiliaires — seule la feuille de calcul actuellement visible pour l'utilisateur est exportée.

{{% alert color="primary" %}}
La classe `HtmlSaveOptions` offre des propriétés supplémentaires pour ajuster finement la sortie, telles que `ExportHiddenWorksheet`, `ExportImagesAsBase64`, et `Encoding`. Ajustez-les selon les besoins de votre cible de déploiement.
{{% /alert %}}

## **Résumé de l'API**

Les flux de travail ci-dessus s'appuient sur un petit ensemble d'API Aspose.Cells travaillant ensemble.

- `SparklineGroup` et l'accesseur de collection `worksheet.getSparklineGroups()` sont utilisés pour déclarer le type (Ligne, Colonne, Empilée), la plage de données et la cellule d'ancrage pour chaque groupe de sparklines. Dans cet article, chaque groupe est ancré à une seule cellule, donc le groupe est atteint via `worksheet.getSparklineGroups().get(i)`.
- `Sparkline` et l'indexeur `group.getSparklines().get(0)` renvoient la sparkline individuelle à l'intérieur d'un groupe. Étant donné que chaque groupe de l'exemple contient exactement une sparkline, aucune boucle `for` n'est requise.
- `Sparkline.toImage(Stream, ImageOrPrintOptions)` est la méthode de rendu qui écrit une image de la sparkline dans un `Stream` fourni. La méthode renvoie `void` ; vous lisez les octets depuis le flux après l'appel.
- `Cell.EmbeddedImage` est une propriété `byte[]` (affectée via `cell.setEmbeddedImage(byte[])`) qui stocke une image à l'intérieur d'une seule cellule. Elle est disponible dans **Aspose.Cells 26.5 et versions ultérieures** et constitue la méthode recommandée pour réinjecter une sparkline rendue par `toImage` dans le même classeur.
- `HtmlSaveOptions.setExportActiveWorksheetOnly(boolean)` restreint l'exportation HTML à la feuille de calcul active. C'est l'une des propriétés les plus couramment utilisées sur `HtmlSaveOptions` lors de la génération de rapports d'une seule page.
- `ImageOrPrintOptions.setImageType(ImageType)` se trouve dans le package `com.aspose.cells.drawing` et sélectionne le format d'image (par exemple, `ImageType.PNG`) utilisé lors du rendu avec `toImage` et lors de l'impression des feuilles de calcul en images.

## **Articles connexes**

- [Sparklines dans Aspose.Cells pour Aspose.Cells for Java](/cells/fr/java/sparkline/)
- [Insertion d'une image dans une cellule](/cells/fr/java/inserting-an-image-into-a-cell/)
- [Rendu de tableau à cellule unique SmartMarker | Aspose.Cells Java](/cells/fr/java/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="java" >}}