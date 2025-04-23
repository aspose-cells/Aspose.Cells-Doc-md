---
title: Paramètres d alignement
linktitle: Paramètres d alignement
description: Dans la bibliothèque Aspose.Cells, vous pouvez utiliser les réglages d alignement de la cellule pour ajuster la disposition et l affichage du texte en utilisant Node.js via C++. Ce document fournit des étapes détaillées et un code d exemple pour utiliser Aspose.Cells pour les réglages d alignement de la cellule.
keywords: Aspose.Cells, alignement de cellule, alignement horizontal, alignement vertical, retour à la ligne du texte Node.js via C++
type: docs
weight: 20
url: /fr/nodejs-cpp/cells-alignment-settings/
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

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) permettant d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fournit une collection [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Chaque élément de cette collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).

Aspose.Cells fournit les méthodes [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) et [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) pour la classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) qui permettent de récupérer et de définir le formatage d'une cellule. La classe [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) offre des propriétés utiles pour configurer les réglages d'alignement.

Sélectionnez n'importe quel type d'alignement du texte en utilisant l'énumération [**TextAlignmentType**](https://reference.aspose.com/cells/nodejs-cpp/textalignmenttype). Les types d'alignement de texte prédéfinis dans l'énumération [**TextAlignmentType**](https://reference.aspose.com/cells/nodejs-cpp/textalignmenttype) sont :

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

Vous pouvez également appliquer le réglage de distribution justifiée à l'aide de la méthode [**Style.setIsJustifyDistributed(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsJustifyDistributed-boolean-).

{{% /alert %}}

#### **Alignement horizontal**

Utilisez la méthode [**setHorizontalAlignment**](https://reference.aspose.com/cells/nodejs-cpp/style/#setHorizontalAlignment-textalignmenttype-) de l'objet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) pour aligner le texte horizontalement.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-HorizontalAlignment.js" >}}



#### **Alignement vertical**

De même que pour l'alignement horizontal, utilisez la méthode [**setVerticalAlignment**](https://reference.aspose.com/cells/nodejs-cpp/style/#setVerticalAlignment-textalignmenttype-) de l'objet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) pour aligner le texte verticalement.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-VerticalAlignment.js" >}}


#### **Indentation**

Il est possible de définir le niveau d'indentation du texte dans une cellule avec la méthode [**setIndentLevel**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIndentLevel-number-) de l'objet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-Indentation.js" >}}



#### **Orientation**

Définissez l'orientation (rotation) du texte dans une cellule avec la méthode [**setRotationAngle**](https://reference.aspose.com/cells/nodejs-cpp/style/#setRotationAngle-number-) de l'objet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-Orientation.js" >}}

#### **Contrôle du texte**

La section suivante aborde comment contrôler le texte en définissant le retour à la ligne, le rétrécissement pour s'adapter et d'autres options de mise en forme.

##### **Retour à la ligne du texte**

Le retour à la ligne du texte dans une cellule facilite sa lecture : la hauteur de la cellule s'ajuste pour contenir tout le texte, au lieu de le couper ou de déborder dans les cellules adjacentes. Activez ou désactivez le retour à la ligne avec la méthode [**setIsTextWrapped(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsTextWrapped-boolean-) de l'objet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-WrapText.js" >}}


##### **Rétrécissement pour s'adapter**

Une option pour le retour à la ligne dans un champ est de réduire la taille du texte pour qu'il s'adapte aux dimensions de la cellule. Cela se fait en réglant la méthode [**setShrinkToFit(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setShrinkToFit-boolean-) de l'objet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) sur **true**.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-ShrinkToFit.js" >}}


##### **Fusion de cellules**

Comme Microsoft Excel, Aspose.Cells supporte la fusion de plusieurs cellules en une seule. Aspose.Cells offre deux approches pour cette tâche. L'une consiste à appeler la méthode [**merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/#merge-number-number-number-number-) de la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). La méthode [**merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/#merge-number-number-number-number-) prend les paramètres suivants pour fusionner les cellules :

- Première rangée : la première rangée à partir de laquelle commencer la fusion.
- Première colonne : la première colonne à partir de laquelle commencer la fusion.
- Nombre de rangées : le nombre de rangées à fusionner.
- Nombre de colonnes : le nombre de colonnes à fusionner.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-MergeCells.js" >}}


L'autre méthode consiste à d'abord appeler la méthode [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) de la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) pour créer une plage de cellules à fusionner. La méthode [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) prend le même ensemble de paramètres que celle de la méthode [**merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/#merge-number-number-number-number-) évoquée ci-dessus et retourne un objet [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range). L'objet [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) offre également une méthode [**merge**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--) qui fusionne la plage spécifiée dans l'objet [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range).

##### **Direction du texte**

Il est possible de définir l'ordre de lecture du texte dans les cellules. L'ordre de lecture est l'ordre visuel dans lequel les caractères, les mots, etc. sont affichés. Par exemple, l'anglais est une langue de gauche à droite tandis que l'arabe est une langue de droite à gauche.

L'ordre de lecture est défini avec la propriété [**TextDirection**](https://reference.aspose.com/cells/nodejs-cpp/style/#setTextDirection-textdirectiontype-) de l'objet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style). Aspose.Cells fournit des types de direction de texte prédéfinis dans l'énumération [**TextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/textdirectiontype).

|**Types de direction du texte**|**Description**|
| :- | :- |
|Context|L'ordre de lecture en accord avec la langue du premier caractère saisi|
|LeftToRight|Ordre de lecture de gauche à droite|
|RightToLeft|Ordre de lecture de droite à gauche|

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-TextDirection.js" >}}


## **Sujets avancés**
- [Modifier l'alignement des cellules et conserver la mise en forme existante](/cells/fr/nodejs-cpp/change-cells-alignment-and-keep-existing-formatting/)
- [Sauts de ligne et retour à la ligne](/cells/fr/nodejs-cpp/line-breaks-and-text-wrapping/)

