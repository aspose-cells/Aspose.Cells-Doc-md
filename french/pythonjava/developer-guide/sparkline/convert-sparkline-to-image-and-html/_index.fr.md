---
title: Convertir Sparkline en image et HTML dans Aspose.Cells for Python via Java
linktitle: Convert Sparkline to Image and HTML
description: Apprenez à rendre les sparklines Aspose.Cells sous forme d'images autonomes pour l'incorporation dans des cellules et à exporter des feuilles de calcul riches en sparklines vers HTML à l'aide de HtmlSaveOptions.
keywords: Aspose.Cells, Python via Java, sparkline, Sparkline.toImage, Cell.embeddedImage, HtmlSaveOptions, rendre sparkline, convertir sparkline en image, exporter sparkline en HTML
type: docs
weight: 120
url: /fr/python-java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Les sparklines sont des mini-graphiques placés à l'intérieur des cellules d'une feuille de calcul. Aspose.Cells vous permet d'extraire chaque sparkline sous forme d'image autonome (pour l'incorporer dans une autre cellule ou un rapport externe) et également d'exporter la feuille de calcul entière riche en sparklines vers HTML pour une distribution basée sur un navigateur. La propriété `Cell.embedded_image` utilisée dans cet article est disponible dans **Aspose.Cells 26.5 et versions ultérieures**.
{{% /alert %}}

## **Introduction**

Les sparklines sont un moyen compact de visualiser des tendances directement à l'intérieur d'une feuille de calcul. Bien que les utilisateurs d'Excel les voient en place, de nombreux scénarios réels nécessitent que la sparkline quitte la cellule — par exemple, pour être intégrée dans une autre cellule sous forme d'image statique, jointe à un e-mail automatisé, ou rendue dans le cadre d'un rapport HTML publié sur le web.

Aspose.Cells prend en charge ces deux opérations. La méthode `Sparkline.to_image` rend une sparkline individuelle dans un flux, et les octets résultants peuvent être assignés à `Cell.embedded_image` afin que l'image soit stockée à l'intérieur d'une seule cellule du classeur. Séparément, `HtmlSaveOptions` vous permet de convertir le classeur entier — sparklines incluses — en un fichier HTML autonome. Cet article présente les deux flux de travail de bout en bout.

## **Workflow 1 — Render Sparklines to Images and Embed Them Into Cells**

Dans ce flux de travail, vous allez créer une feuille de calcul qui contient une petite plage de valeurs sources, attacher trois groupes de sparklines différents (Ligne, Colonne et Empilé/Perte-Gain) à cette plage, rendre chaque groupe en PNG, et écrire ces octets PNG dans des cellules adjacentes en tant qu'images intégrées. Le résultat final est un fichier `.xlsx` unique qui contient à la fois les sparklines actives et leurs contreparties en images rendues.

### **Step-by-Step Instructions**

1. Définissez un répertoire de travail et assurez-vous qu'il existe sur le disque.
2. Créez un nouveau `Workbook` et obtenez une référence à la première `Worksheet`.
3. Remplissez les cellules `A1` à `E1` avec cinq valeurs numériques d'exemple (par exemple, des ventes quotidiennes ou des relevés de température).
4. Ajoutez trois objets `SparklineGroup` à la feuille de calcul en appelant `worksheet.sparkline_groups.add(...)` :
   - Un groupe `SparklineType.LINE` ancré à `F1`, avec la plage de données `A1:E1`.
   - Un groupe `SparklineType.COLUMN` ancré à `G1`, avec la plage de données `A1:E1`.
   - Un groupe `SparklineType.STACKED` (perte/gain) ancré à `H1`, avec la plage de données `A1:E1`.
5. Créez une instance `ImageOrPrintOptions` et définissez son `image_type` sur `ImageType.PNG` afin que chaque sparkline soit rendue sous forme de PNG transparent.
6. Pour chacun des trois groupes, rendez sa sparkline unique à l'aide de `group.sparklines[0].to_image(byte_array_output_stream, image_options)`, convertissez le `ByteArrayOutputStream` en `byte[]` (ou lisez son `to_byte_array()` dans des `bytes` Python), et assignez les octets à `worksheet.cells["F2"].embedded_image`, `worksheet.cells["G2"].embedded_image`, et `worksheet.cells["H2"].embedded_image` respectivement.
7. Enregistrez le classeur sous `output_with_sparklines.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType, ImageType, ImageOrPrintOptions, Sparkline
from jpype import JClass

ByteArrayOutputStream = JClass('java.io.ByteArrayOutputStream')

# Créer un nouveau classeur et accéder à la première feuille de calcul
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Remplir les cellules A1:E1 avec des données d'exemple
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)

# Ajouter un groupe de sparklines de type Ligne ancré à F1 (colonne 5, ligne 0)
lineArea = CellArea()
lineArea.setStartColumn(5)
lineArea.setEndColumn(5)
lineArea.setStartRow(0)
lineArea.setEndRow(0)
lineIdx = worksheet.getSparklineGroups().add(SparklineType.Line, "A1:E1", False, lineArea)

# Ajouter un groupe de sparklines de type Colonne ancré à G1 (colonne 6, ligne 0)
columnArea = CellArea()
columnArea.setStartColumn(6)
columnArea.setEndColumn(6)
columnArea.setStartRow(0)
columnArea.setEndRow(0)
columnIdx = worksheet.getSparklineGroups().add(SparklineType.Column, "A1:E1", False, columnArea)

# Ajouter un groupe de sparklines Win/Loss (Empilé) ancré à H1 (colonne 7, ligne 0)
stackedArea = CellArea()
stackedArea.setStartColumn(7)
stackedArea.setEndColumn(7)
stackedArea.setStartRow(0)
stackedArea.setEndRow(0)
stackedIdx = worksheet.getSparklineGroups().add(SparklineType.Stacked, "A1:E1", False, stackedArea)

# Configurer les options d'image pour la sortie PNG
imageOptions = ImageOrPrintOptions()
imageOptions.setImageType(ImageType.Png)

# Convertir la sparkline de type Ligne en image et l'incorporer dans la cellule F2
lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
lineSp.toImage(ms, imageOptions)
worksheet.getCells().get("F2").setEmbeddedImage(ms.toByteArray())

# Convertir la sparkline de type Colonne en image et l'incorporer dans la cellule G2
columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
columnSp.toImage(ms, imageOptions)
worksheet.getCells().get("G2").setEmbeddedImage(ms.toByteArray())

# Convertir la sparkline Win/Loss en image et l'incorporer dans la cellule H2
stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
stackedSp.toImage(ms, imageOptions)
worksheet.getCells().get("H2").setEmbeddedImage(ms.toByteArray())

# Enregistrer le classeur sur le disque
workbook.save("output_with_sparklines.xlsx")

jpype.shutdownJVM()
```

Le code ci-dessus produit un classeur où chaque représentation visuelle d'une sparkline est dupliquée sous deux formes : la sparkline native active ancrée à la ligne 1, et une image PNG statique intégrée directement dans une cellule voisine de la ligne 2. Étant donné que les images vivent à l'intérieur du fichier lui-même, le classeur reste un artefact autonome unique qui peut être envoyé par e-mail ou archivé sans casser les références d'images intégrées. Rendez chaque groupe de sparklines en PNG, convertissez le `ByteArrayOutputStream` en `byte[]` (ou utilisez `to_byte_array()` pour obtenir un objet `bytes` Python), et assignez le tableau à la propriété `embedded_image` de la cellule cible — l'assignation est ce qui fait que l'image fait partie du contenu stocké de la cellule.

{{% alert color="primary" %}}
Parce que chaque groupe de sparklines est ancré à une seule cellule, vous pouvez y accéder via l'indexeur `group.sparklines[0]` au lieu d'énumérer avec une boucle `for`. Cela permet de garder le code de rendu court et correspond au modèle typique « une sparkline par cellule d'ancrage ». Le stockage des octets d'image via `Cell.embedded_image` nécessite Aspose.Cells 26.5 ou une version ultérieure.
{{% /alert %}}

## **Workflow 2 — Export the Sparkline Worksheet to HTML**

Une fois que le classeur contient des sparklines actives (et éventuellement des contreparties en images intégrées), la feuille de calcul entière peut être publiée sur le web en l'enregistrant au format HTML. La classe `HtmlSaveOptions` expose les paramètres dont vous avez besoin pour contrôler cet export ; dans ce flux de travail, vous réutiliserez le fichier `output_with_sparklines.xlsx` produit par le flux de travail 1 et le convertirez en un document HTML propre et d'une seule page.

### **Step-by-Step Instructions**

1. Assurez-vous que le fichier `output_with_sparklines.xlsx` produit par le flux de travail 1 est disponible sur le disque dans votre répertoire de travail.
2. Chargez ce fichier dans une nouvelle instance `Workbook`.
3. Instanciez `HtmlSaveOptions` et définissez sa propriété `export_active_worksheet_only` sur `True` afin que le fichier HTML résultant ne contienne que la feuille de calcul active plutôt que le classeur entier.
4. Appelez `workbook.save("sparklines.html", html_options)` pour écrire la sortie HTML sur le disque.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, HtmlSaveOptions

workbook = Workbook("output_with_sparklines.xlsx")
htmlOptions = HtmlSaveOptions()
htmlOptions.setExportActiveWorksheetOnly(True)
workbook.save("sparklines.html", htmlOptions)

jpype.shutdownJVM()
```

Le code ci-dessus prend le classeur riche en sparklines du flux de travail 1 et le transforme en un fichier HTML portable. Les sparklines sont conservées sous forme de rendus SVG ou PNG en ligne à l'intérieur du HTML généré, selon le mode d'export, de sorte que les utilisateurs finaux puissent consulter les tendances dans n'importe quel navigateur moderne sans avoir besoin d'Excel installé. En définissant `export_active_worksheet_only` sur `True`, vous évitez de publier accidentellement des feuilles cachées ou des données auxiliaires — seule la feuille de calcul actuellement visible par l'utilisateur est exportée.

{{% alert color="primary" %}}
La classe `HtmlSaveOptions` offre des propriétés supplémentaires pour affiner la sortie, telles que `export_hidden_worksheet`, `export_images_as_base64`, et `encoding`. Ajustez-les selon les besoins de votre cible de déploiement.
{{% /alert %}}

## **API Summary**

Les flux de travail ci-dessus s'appuient sur un petit ensemble d'APIs Aspose.Cells travaillant ensemble.

- `SparklineGroup` et l'accesseur de collection `worksheet.sparkline_groups` sont utilisés pour déclarer le type (Line, Column, Stacked), la plage de données et la cellule d'ancrage pour chaque groupe de sparklines. Dans cet article, chaque groupe est ancré à une seule cellule, donc le groupe est atteint via `worksheet.sparkline_groups[i]`.
- `Sparkline` et l'indexeur `group.sparklines[0]` renvoient la sparkline individuelle à l'intérieur d'un groupe. Parce que chaque groupe dans l'exemple contient exactement une sparkline, aucune boucle `for` n'est nécessaire.
- `Sparkline.to_image(OutputStream, ImageOrPrintOptions)` est la méthode de rendu qui écrit une image de la sparkline dans un `OutputStream` fourni (tel qu'un `ByteArrayOutputStream`). La méthode renvoie `void` ; vous lisez les octets depuis le flux après l'appel.
- `Cell.embedded_image` est une propriété `byte[]` qui stocke une image à l'intérieur d'une seule cellule. Elle est disponible dans **Aspose.Cells 26.5 et versions ultérieures** et constitue la méthode recommandée pour faire un aller-retour d'une sparkline rendue par `to_image` dans le même classeur.
- `HtmlSaveOptions.export_active_worksheet_only` (un `bool`) restreint l'export HTML à la feuille de calcul active. C'est l'une des propriétés les plus couramment utilisées sur `HtmlSaveOptions` lors de la génération de rapports d'une seule page.
- `ImageOrPrintOptions.image_type` se trouve dans le namespace `com.aspose.cells.drawing` et sélectionne le format d'image (par exemple, `ImageType.PNG`) utilisé lors du rendu avec `to_image` et lors de l'impression de feuilles de calcul en images.

## **Related Articles**

- [Sparklines dans Aspose.Cells for Python via Java](/cells/fr/python-java/sparkline/)
- [Insertion d'une image dans une cellule](/cells/fr/python-java/inserting-an-image-into-a-cell/)

{{< app/cells/assistant language="python" >}}