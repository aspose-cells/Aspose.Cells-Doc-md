---
title: Paramètres d alignement
description: Dans la bibliothèque Aspose.Cells pour Python via .NET, vous pouvez utiliser les paramètres d alignement des cellules pour ajuster la disposition et l affichage du texte. En ajustant les réglages tels que l alignement horizontal, l alignement vertical et le retop d texte, vous avez plus de contrôle sur la façon dont le texte s écoule dans les cellules. Ce document vous fournira des étapes détaillées et un code d exemple pour vous aider à comprendre rapidement comment utiliser Aspose.Cells pour Python via .NET pour les réglages d alignement des cellules.
keywords: Aspose.Cells pour Python via .NET, alignement des cellules, alignement horizontal, alignement vertical, retop de texte
type: docs
weight: 20
url: /fr/python-net/cells-alignment-settings/
---

## **Configuration des paramètres d'alignement**

### **Paramètres d'alignement dans Microsoft Excel**

Toute personne ayant utilisé Microsoft Excel pour formater des cellules sera familière avec les paramètres d'alignement dans Microsoft Excel.

Comme vous pouvez le voir sur la figure ci-dessus, il existe différents types d'options d'alignement :

- Alignement du texte (horizontal et vertical)
- Retrait.
- Orientation.
- Contrôle du texte.
- Direction du texte.

Tous ces réglages d'alignement sont entièrement pris en charge par Aspose.Cells pour Python via .NET et sont discutés plus en détail ci-dessous.

### **Réglages d'alignement dans Aspose.Cells pour Python via .NET**

Aspose.Cells pour Python via .NET fournit une classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fournit une collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/). Chaque élément de la collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Aspose.Cells pour Python via .NET fournit des méthodes [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) et [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) pour la classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) qui sont utilisées pour obtenir et définir la mise en forme d'une cellule. La classe [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) offre des propriétés utiles pour configurer les réglages d'alignement.

Sélectionnez n'importe quel type d'alignement de texte en utilisant l'énumération [**TextAlignmentType**](https://reference.aspose.com/cells/python-net/aspose.cells/textalignmenttype). Les types d'alignement de texte prédéfinis dans l'énumération [**TextAlignmentType**](https://reference.aspose.com/cells/python-net/aspose.cells/textalignmenttype) sont:

|**Types d'alignement de texte**|**Description**|
| :- | :- |
|GENERAL|Représente un alignement de texte général|
|BOTTOM|Représente un alignement du texte en bas|
|CENTER|Représente un alignement du texte au centre|
|CENTER_ACROSS|Représente un alignement du texte centré à travers|
|DISTRIBUTED|Représente un alignement distribué du texte|
|FILL|Représente un alignement du texte rempli|
|JUSTIFY|Représente un alignement justifié du texte|
|LEFT|Représente un alignement du texte à gauche|
|RIGHT|Représente un alignement du texte à droite|
|TOP|Représente un alignement du texte en haut|
|JUSTIFIED_LOW|Aligne le texte avec une longueur de kasaida ajustée pour le texte arabe|
|THAI_DISTRIBUTED|Distribue le texte thaï de manière spéciale, chaque caractère étant traité comme un mot|

{{% alert color="primary" %}}

Vous pouvez également appliquer le paramètre de justifier distribué en utilisant la propriété [**Style.is_justify_distributed**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_justify_distributed).

{{% /alert %}}

#### **Alignement horizontal**

Utilisez la propriété [**horizontal_alignment**](https://reference.aspose.com/cells/python-net/aspose.cells/style/horizontal_alignment) de l'objet [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) pour aligner le texte horizontalement.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.py" >}}

#### **Alignement vertical**

Tout comme l'alignement horizontal, utilisez la propriété [**vertical_alignment**](https://reference.aspose.com/cells/python-net/aspose.cells/style/vertical_alignment) de l'objet [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) pour aligner le texte verticalement.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.py" >}}

#### **Indentation**

Il est possible de définir le niveau d'indentation du texte dans une cellule avec la propriété [**indent_level**](https://reference.aspose.com/cells/python-net/aspose.cells/style/indent_level) de l'objet [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-Indentation-1.py" >}}

#### **Orientation**

Définissez l'orientation (rotation) du texte dans une cellule avec la propriété [**rotation_angle**](https://reference.aspose.com/cells/python-net/aspose.cells/style/rotation_angle) de l'objet [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-Orientation-1.py" >}}

#### **Contrôle du texte**

La section suivante aborde comment contrôler le texte en définissant le retour à la ligne, le rétrécissement pour s'adapter et d'autres options de mise en forme.

##### **Retour à la ligne du texte**

Le retour à la ligne du texte dans une cellule facilite sa lecture : la hauteur de la cellule s'adapte pour contenir tout le texte, au lieu de le couper ou de le faire déborder dans les cellules adjacentes. Définissez le retour à la ligne sur ou hors avec la propriété [**is_text_wrapped**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_text_wrapped) de l'objet [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-LineBreakTextWrapping-WrapText-1.py" >}}

##### **Rétrécissement pour s'adapter**

Une option pour le retour à la ligne du texte dans un champ est de rétrécir la taille du texte pour s'adapter aux dimensions d'une cellule. Cela se fait en définissant la propriété [**is_text_wrapped**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_text_wrapped) de l'objet [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) sur **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.py" >}}

##### **Fusion de cellules**

Comme Microsoft Excel, Aspose.Cells pour Python via .NET supporte la fusion de plusieurs cellules en une seule. Aspose.Cells pour Python via .NET offre deux approches pour cette tâche. Une consiste à appeler la méthode [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/merge) de la collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/). La méthode [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/merge) prend les paramètres suivants pour fusionner les cellules :

- Première rangée : la première rangée à partir de laquelle commencer la fusion.
- Première colonne : la première colonne à partir de laquelle commencer la fusion.
- Nombre de rangées : le nombre de rangées à fusionner.
- Nombre de colonnes : le nombre de colonnes à fusionner.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Merging-MergingCellsInWorksheet.-1.py" >}}

L'autre façon consiste à appeler d'abord la méthode [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range) de la [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/) collection pour créer une plage de cellules à fusionner. La méthode [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range) prend le même ensemble de paramètres que la méthode [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/merge) discutée ci-dessus et renvoie un objet [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range). L'objet [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) fournit également une méthode [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/range/merge) qui fusionne la plage spécifiée dans l'objet [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range).

##### **Direction du texte**

Il est possible de définir l'ordre de lecture du texte dans les cellules. L'ordre de lecture est l'ordre visuel dans lequel les caractères, les mots, etc. sont affichés. Par exemple, l'anglais est une langue de gauche à droite tandis que l'arabe est une langue de droite à gauche.

L'ordre de lecture est défini avec la propriété [**text_direction**](https://reference.aspose.com/cells/python-net/aspose.cells/style/text_direction) de l'objet [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style). Aspose.Cells pour Python via .NET fournit des types de direction de texte prédéfinis dans l'énumération [**TextDirectionType**](https://reference.aspose.com/cells/python-net/aspose.cells/textdirectiontype).

|**Types de direction du texte**|**Description**|
| :- | :- |
|CONTEXTE|L'ordre de lecture conforme à la langue du premier caractère entré|
|GAUCHE_DROITE|Ordre de lecture de gauche à droite|
|DROITE_GAUCHE|Ordre de lecture de droite à gauche|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ChangeTextDirection-1.py" >}}

## **Sujets avancés**
- [Modifier l'alignement des cellules et conserver la mise en forme existante](/cells/fr/python-net/change-cells-alignment-and-keep-existing-formatting/)
- [Sauts de ligne et retour à la ligne](/cells/fr/python-net/line-breaks-and-text-wrapping/)


{{< app/cells/assistant language="python-net" >}}
