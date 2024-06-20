---
title: Paramètres d alignement
description: Dans la bibliothèque Aspose.Cells, vous pouvez utiliser les paramètres d alignement des cellules pour ajuster la mise en page et l affichage du texte. En ajustant des paramètres tels que l alignement horizontal, l alignement vertical et le retour à la ligne du texte, vous avez un contrôle accru sur la façon dont le texte circule dans les cellules. Ce document vous fournira des étapes détaillées et un code d exemple pour vous aider à comprendre rapidement comment utiliser Aspose.Cells pour les paramètres d alignement des cellules.
keywords: Aspose.Cells, alignement des cellules, alignement horizontal, alignement vertical, retour à la ligne
type: docs
weight: 20
url: /fr/net/cells-alignment-settings/
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

Tous ces paramètres d'alignement sont entièrement pris en charge par Aspose.Cells et sont discutés plus en détail ci-dessous.

### **Paramètres d'alignement dans Aspose.Cells**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Chaque élément de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

Aspose.Cells fournit les méthodes [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) et [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) pour la classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) qui sont utilisées pour obtenir et définir le formatage d'une cellule. La classe [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) fournit des propriétés utiles pour configurer les paramètres d'alignement.

Sélectionnez n'importe quel type d'alignement de texte en utilisant l'énumération [**TextAlignmentType**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype). Les types d'alignement de texte prédéfinis dans l'énumération [**TextAlignmentType**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype) sont:

|**Types d'alignement de texte**|**Description**|
| :- | :- |
|Bottom|Représente un alignement de texte en bas|
|Center|Représente un alignement de texte au centre|
|CenterAcross|Représente un alignement de texte centré sur plusieurs cellules|
|Distributed|Représente un alignement de texte distribué|
|Fill|Représente un alignement de texte en remplissage|
|General|Représente un alignement de texte général|
|Justify|Représente un alignement de texte justifié|
|Left|Représente un alignement de texte à gauche|
|Right|Représente un alignement de texte à droite|
|Top|Représente un alignement de texte en haut|
|JustifiedLow|Aligne le texte avec une longueur de kashida ajustée pour le texte arabe.|
|ThaiDistributed|Distribue le texte thaïlandais en particulier, car chaque caractère est traité comme un mot.|

{{% alert color="primary" %}}

Vous pouvez également appliquer le paramètre de justifier distribué en utilisant la propriété [**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/isjustifydistributed).

{{% /alert %}}

#### **Alignement horizontal**

Utilisez la propriété [**HorizontalAlignment**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/horizontalalignment) de l'objet [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) pour aligner le texte horizontalement.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.cs" >}}

#### **Alignement vertical**

Tout comme l'alignement horizontal, utilisez la propriété [**VerticalAlignment**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/verticalalignment) de l'objet [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) pour aligner le texte verticalement.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.cs" >}}

#### **Indentation**

Il est possible de définir le niveau d'indentation du texte dans une cellule avec la propriété [**IndentLevel**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/indentlevel) de l'objet [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Indentation-1.cs" >}}

#### **Orientation**

Définissez l'orientation (rotation) du texte dans une cellule avec la propriété [**RotationAngle**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/rotationangle) de l'objet [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Orientation-1.cs" >}}

#### **Contrôle du texte**

La section suivante aborde comment contrôler le texte en définissant le retour à la ligne, le rétrécissement pour s'adapter et d'autres options de mise en forme.

##### **Retour à la ligne du texte**

Le retour à la ligne du texte dans une cellule facilite sa lecture : la hauteur de la cellule s'adapte pour contenir tout le texte, au lieu de le couper ou de le faire déborder dans les cellules adjacentes. Définissez le retour à la ligne sur ou hors avec la propriété [**IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped) de l'objet [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

##### **Rétrécissement pour s'adapter**

Une option pour le retour à la ligne du texte dans un champ est de rétrécir la taille du texte pour s'adapter aux dimensions d'une cellule. Cela se fait en définissant la propriété [**IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped) de l'objet [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) sur **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.cs" >}}

##### **Fusion de cellules**

Comme Microsoft Excel, Aspose.Cells prend en charge la fusion de plusieurs cellules en une seule. Aspose.Cells propose deux approches à cette tâche. Une façon est d'appeler la méthode [**Merge**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). La méthode [**Merge**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) prend les paramètres suivants pour fusionner les cellules :

- Première rangée : la première rangée à partir de laquelle commencer la fusion.
- Première colonne : la première colonne à partir de laquelle commencer la fusion.
- Nombre de rangées : le nombre de rangées à fusionner.
- Nombre de colonnes : le nombre de colonnes à fusionner.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}

L'autre façon consiste à appeler d'abord la méthode [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) de la [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection pour créer une plage de cellules à fusionner. La méthode [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) prend le même ensemble de paramètres que la méthode [**Merge**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) discutée ci-dessus et renvoie un objet [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range). L'objet [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) fournit également une méthode [**Merge**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge) qui fusionne la plage spécifiée dans l'objet [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range).

##### **Direction du texte**

Il est possible de définir l'ordre de lecture du texte dans les cellules. L'ordre de lecture est l'ordre visuel dans lequel les caractères, les mots, etc. sont affichés. Par exemple, l'anglais est une langue de gauche à droite tandis que l'arabe est une langue de droite à gauche.

L'ordre de lecture est défini avec la propriété [**TextDirection**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/textdirection) de l'objet [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style). Aspose.Cells fournit des types de direction de texte prédéfinis dans l'énumération [**TextDirectionType**](https://reference.aspose.com/cells/net/aspose.cells/textdirectiontype).

|**Types de direction du texte**|**Description**|
| :- | :- |
|Context|L'ordre de lecture en accord avec la langue du premier caractère saisi|
|LeftToRight|Ordre de lecture de gauche à droite|
|RightToLeft|Ordre de lecture de droite à gauche|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChangeTextDirection-1.cs" >}}

## **Sujets avancés**
- [Modifier l'alignement des cellules et conserver la mise en forme existante](/cells/fr/net/change-cells-alignment-and-keep-existing-formatting/)
- [Sauts de ligne et retour à la ligne](/cells/fr/net/line-breaks-and-text-wrapping/)

