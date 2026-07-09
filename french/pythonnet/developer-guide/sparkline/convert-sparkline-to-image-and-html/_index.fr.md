---
title: Convertir une sparkline en image et en HTML dans Aspose.Cells for Python via .NET
linktitle: Convert Sparkline to Image and HTML
description: Apprenez à rendre les sparklines Aspose.Cells sous forme d'images autonomes pour l'intégration dans des cellules et à exporter des feuilles de calcul riches en sparklines au format HTML à l'aide de HtmlSaveOptions en Python via .NET.
keywords: Aspose.Cells, Python via .NET, sparkline, sparkline.to_image, cell.embedded_image, HtmlSaveOptions, rendre une sparkline, convertir une sparkline en image, exporter une sparkline au format HTML
type: docs
weight: 120
url: /fr/python-net/convert-sparkline-to-image-and-html/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Les sparklines sont des mini-graphiques placés à l'intérieur des cellules d'une feuille de calcul. Aspose.Cells vous permet d'extraire chaque sparkline sous forme d'image autonome (pour l'intégrer dans une autre cellule ou un rapport externe) et également d'exporter la feuille de calcul entière, riche en sparklines, au format HTML pour une distribution via navigateur. La propriété `cell.embedded_image` utilisée dans cet article est disponible dans **Aspose.Cells 26.5 et versions ultérieures**.
{{% /alert %}}

## **Introduction**

Les sparklines constituent un moyen compact de visualiser des tendances directement dans une feuille de calcul. Bien que les utilisateurs d'Excel les voient en place, de nombreux scénarios réels nécessitent qu'une sparkline quitte la cellule — par exemple, pour être intégrée dans une autre cellule sous forme d'image statique, jointe à un e-mail automatisé, ou rendue dans le cadre d'un rapport HTML publié sur le web.

Aspose.Cells prend en charge ces deux opérations. La méthode `sparkline.to_image` restitue une sparkline individuelle dans un flux, et les octets résultants peuvent être affectés à `cell.embedded_image` afin que l'image soit stockée dans une seule cellule du classeur. Par ailleurs, `HtmlSaveOptions` vous permet de convertir le classeur entier — y compris les sparklines — en un fichier HTML autonome. Cet article présente les deux workflows de bout en bout.

## **Workflow 1 — Rendre les sparklines sous forme d'images et les intégrer dans des cellules**

Dans ce workflow, vous allez créer une feuille de calcul contenant une petite plage de valeurs sources, attacher trois groupes de sparklines différents (Ligne, Colonne et Empilé/Win-Loss) à cette plage, rendre chaque groupe au format PNG et écrire ces octets PNG dans des cellules adjacentes sous forme d'images intégrées. Le résultat final est un fichier `.xlsx` unique qui contient à la fois les sparklines actives et leurs équivalents sous forme d'images rendues.

### **Instructions étape par étape**

1. Définissez un répertoire de travail et assurez-vous qu'il existe sur le disque.
2. Créez un nouveau `Workbook` et obtenez une référence à la première `Worksheet`.
3. Remplissez les cellules `A1` à `E1` avec cinq valeurs numériques d'exemple (par exemple, des ventes quotidiennes ou des relevés de température).
4. Ajoutez trois objets `SparklineGroup` à la feuille de calcul en appelant `worksheet.sparkline_groups.add(...)` :
   - Un groupe `SparklineType.LINE` ancré en `F1`, avec une plage de données `A1:E1`.
   - Un groupe `SparklineType.COLUMN` ancré en `G1`, avec une plage de données `A1:E1`.
   - Un groupe `SparklineType.STACKED` (win/loss) ancré en `H1`, avec une plage de données `A1:E1`.
5. Créez une instance `ImageOrPrintOptions` et définissez son `image_type` sur `ImageType.PNG` afin que chaque sparkline soit rendue sous forme de PNG transparent.
6. Pour chacun des trois groupes, rendez sa sparkline unique à l'aide de `group.sparklines[0].to_image(memory_stream, image_options)`, convertissez le flux `BytesIO` en un objet `bytes`, et affectez le tableau à `worksheet.cells["F2"].embedded_image`, `worksheet.cells["G2"].embedded_image`, et `worksheet.cells["H2"].embedded_image` respectivement.
7. Enregistrez le classeur sous `output_with_sparklines.xlsx`.

```python
import aspose.cells as ac

# Créer un nouveau classeur et accéder à la première feuille de calcul
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Remplir les cellules A1:E1 avec des données d'exemple
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# Ajouter un groupe de sparklines de type Ligne ancré à F1 (colonne 5, ligne 0)
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, line_area)

# Ajouter un groupe de sparklines de type Colonne ancré à G1 (colonne 6, ligne 0)
column_area = ac.CellArea()
column_area.start_column = 6
column_area.end_column = 6
column_area.start_row = 0
column_area.end_row = 0
column_idx = worksheet.sparkline_groups.add(ac.SparklineType.COLUMN, "A1:E1", False, column_area)

# Ajouter un groupe de sparklines Win/Loss (Empilé) ancré à H1 (colonne 7, ligne 0)
stacked_area = ac.CellArea()
stacked_area.start_column = 7
stacked_area.end_column = 7
stacked_area.start_row = 0
stacked_area.end_row = 0
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)

# Configurer les options d'image pour la sortie PNG
image_options = ac.ImageOrPrintOptions()
image_options.image_type = ac.ImageType.PNG

# Convertir la sparkline Ligne en image et l'incorporer dans la cellule F2
line_sp = worksheet.sparkline_groups[line_idx].sparklines[0]
ms = ac.MemoryStream()
line_sp.to_image(ms, image_options)
worksheet.cells["F2"].embedded_image = ms.to_array()

# Convertir la sparkline Colonne en image et l'incorporer dans la cellule G2
column_sp = worksheet.sparkline_groups[column_idx].sparklines[0]
ms = ac.MemoryStream()
column_sp.to_image(ms, image_options)
worksheet.cells["G2"].embedded_image = ms.to_array()

# Convertir la sparkline Win/Loss en image et l'incorporer dans la cellule H2
stacked_sp = worksheet.sparkline_groups[stacked_idx].sparklines[0]
ms = ac.MemoryStream()
stacked_sp.to_image(ms, image_options)
worksheet.cells["H2"].embedded_image = ms.to_array()

# Enregistrer le classeur sur le disque
workbook.save("output_with_sparklines.xlsx")
```

Le code ci-dessus produit un classeur dans lequel chaque représentation visuelle d'une sparkline est dupliquée sous deux formes : la sparkline native active ancrée à la ligne 1, et une image PNG statique intégrée directement dans une cellule voisine à la ligne 2. Comme les images vivent dans le fichier lui-même, le classeur reste un artefact autonome unique qui peut être envoyé par e-mail ou archivé sans rompre les références d'images intégrées. Rendez chaque groupe de sparklines au format PNG, convertissez le flux `BytesIO` en un objet `bytes`, et affectez les octets à la propriété `embedded_image` de la cellule cible — c'est l'affectation qui fait de l'image une partie du contenu stocké de la cellule.

{{% alert color="primary" %}}
Comme chaque groupe de sparklines est ancré à une seule cellule, vous pouvez y accéder via l'indexeur `group.sparklines[0]` au lieu d'énumérer avec une boucle `for`. Cela permet de garder le code de rendu concis et correspond au modèle typique « une sparkline par cellule d'ancrage ». Le stockage des octets de l'image via `cell.embedded_image` nécessite Aspose.Cells 26.5 ou version ultérieure.
{{% /alert %}}

## **Workflow 2 — Exporter la feuille de calcul des sparklines au format HTML**

Une fois que le classeur contient des sparklines actives (et éventuellement des images intégrées correspondantes), la feuille de calcul entière peut être publiée sur le web en l'enregistrant au format HTML. La classe `HtmlSaveOptions` expose les paramètres dont vous avez besoin pour contrôler cet export ; dans ce workflow, vous allez réutiliser le fichier `output_with_sparklines.xlsx` produit par le Workflow 1 et le convertir en un document HTML propre et d'une seule page.

### **Instructions étape par étape**

1. Assurez-vous que le fichier `output_with_sparklines.xlsx` produit par le Workflow 1 est disponible sur le disque dans votre répertoire de travail.
2. Chargez ce fichier dans une nouvelle instance `Workbook`.
3. Instanciez `HtmlSaveOptions` et définissez sa propriété `export_active_worksheet_only` sur `True` afin que le fichier HTML résultant contienne uniquement la feuille de calcul active plutôt que le classeur entier.
4. Appelez `workbook.save("sparklines.html", html_options)` pour écrire la sortie HTML sur le disque.

```python
import aspose.cells as ac

workbook = ac.Workbook("output_with_sparklines.xlsx")
html_options = ac.HtmlSaveOptions()
html_options.export_active_worksheet_only = True
workbook.save("sparklines.html", html_options)
```

Le code ci-dessus prend le classeur riche en sparklines du Workflow 1 et le transforme en un fichier HTML portable. Les sparklines sont conservées sous forme de rendus SVG ou PNG inline dans le HTML généré, selon le mode d'export, de sorte que les utilisateurs finaux peuvent visualiser les tendances dans n'importe quel navigateur moderne sans avoir besoin d'Excel installé. En définissant `export_active_worksheet_only` sur `True`, vous évitez de publier accidentellement des feuilles masquées ou des données auxiliaires — seule la feuille de calcul actuellement visible par l'utilisateur est exportée.

{{% alert color="primary" %}}
La classe `HtmlSaveOptions` offre des propriétés supplémentaires pour affiner la sortie, telles que `export_hidden_worksheet`, `export_images_as_base64`, et `encoding`. Ajustez-les selon les besoins de votre cible de déploiement.
{{% /alert %}}

## **Résumé de l'API**

Les workflows ci-dessus reposent sur un petit ensemble d'API Aspose.Cells travaillant ensemble.

- `SparklineGroup` et l'accesseur de collection `worksheet.sparkline_groups` sont utilisés pour déclarer le type (Ligne, Colonne, Empilé), la plage de données et la cellule d'ancrage de chaque groupe de sparklines. Dans cet article, chaque groupe est ancré à une seule cellule, de sorte que le groupe est accessible via `worksheet.sparkline_groups[i]`.
- `Sparkline` et l'indexeur `group.sparklines[0]` renvoient la sparkline individuelle à l'intérieur d'un groupe. Comme chaque groupe de l'exemple contient exactement une sparkline, aucune boucle `for` n'est requise.
- `sparkline.to_image(Stream, ImageOrPrintOptions)` est la méthode de rendu qui écrit une image de la sparkline dans un flux fourni. La méthode renvoie `None` ; vous lisez les octets du flux après l'appel.
- `cell.embedded_image` est une propriété de type `bytes` qui stocke une image dans une seule cellule. Elle est disponible dans **Aspose.Cells 26.5 et versions ultérieures** et constitue la méthode recommandée pour réinjecter une sparkline rendue par `to_image` dans le même classeur.
- `html_save_options.export_active_worksheet_only` (un `bool`) limite l'exportation HTML à la feuille de calcul active. C'est l'une des propriétés les plus couramment utilisées de `HtmlSaveOptions` lors de la génération de rapports d'une seule page.
- `image_or_print_options.image_type` se trouve dans le namespace `aspose.cells.drawing` et sélectionne le format d'image (par exemple, `ImageType.PNG`) utilisé lors du rendu avec `to_image` et lors de l'impression des feuilles de calcul en images.

## **Articles connexes**

- [Sparklines in Aspose.Cells for Aspose.Cells for Python via .NET](/cells/fr/python-net/sparkline/)
- [Inserting an Image into a Cell](/cells/fr/python-net/inserting-an-image-into-a-cell/)
- [SmartMarker Single Cell Array Rendering | Aspose.Cells for Aspose.Cells for Python via .NET](/cells/fr/python-net/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="python" >}}