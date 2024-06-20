---
title: Paramètres d alignement
type: docs
weight: 20
url: /fr/java/cells-alignment-settings/
---

## **Configuration des paramètres d'alignement**

## **Paramètres d'alignement dans Microsoft Excel**

Toute personne ayant utilisé Microsoft Excel pour formater des cellules sera familière avec les paramètres d'alignement dans Microsoft Excel.

Comme vous pouvez le voir sur la figure ci-dessus, il existe différents types d'options d'alignement :

- Alignement du texte (horizontal et vertical)
- Retrait.
- Orientation.
- Contrôle du texte.
- Direction du texte.

Tous ces paramètres d'alignement sont entièrement pris en charge par Aspose.Cells et sont discutés plus en détail ci-dessous.

## **Paramètres d'alignement dans Aspose.Cells**

Aspose.Cells fournit les méthodes [**GetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle) et [**SetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle) pour la classe [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) qui sont utilisées pour obtenir et définir le formatage d'une cellule. La classe [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/style) fournit des propriétés utiles pour configurer les paramètres d'alignement.

Sélectionnez n'importe quel type d'alignement de texte en utilisant l'énumération [**TextAlignmentType**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype). Les types d'alignement de texte prédéfinis dans l'énumération [**TextAlignmentType**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype) sont:

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

Vous pouvez également appliquer le paramètre de justifier distribué en utilisant la propriété [**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsJustifyDistributed).

{{% /alert %}}

## **Alignement horizontal, vertical et indentation**

Utilisez la propriété [**HorizontalAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/style#horizontalalignment) pour aligner le texte horizontalement et la propriété [**VerticalAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/style#verticalalignment) pour aligner le texte verticalement.
Il est possible de définir le niveau d'indentation du texte dans une cellule avec la propriété [**IndentLevel**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IndentLevel) 
et cela ne s'applique qu'en cas d'alignement horizontal à gauche ou à droite.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-1.java" >}}


## **Orientation**

Définissez l'orientation (rotation) du texte dans une cellule avec la propriété [**RotationAngle**](https://reference.aspose.com/cells/java/com.aspose.cells/style#RotationAngle)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-Orientation-1.java" >}}

## **Contrôle du texte**

La section suivante aborde comment contrôler le texte en définissant le retour à la ligne, le rétrécissement pour s'adapter et d'autres options de mise en forme.

### **Retour à la ligne du texte**

Le renvoi à la ligne du texte dans une cellule facilite la lecture : la hauteur de la cellule s'ajuste pour contenir tout le texte, au lieu de le couper ou le faire déborder sur les cellules adjacentes. Définissez le renvoi à la ligne du texte sur ou hors avec la propriété [**IsTextWrapped**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsTextWrapped)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LineBreakTextWrapping-WrapText-1.java" >}}

### **Rétrécissement pour s'adapter**

Une option pour le renvoi à la ligne du texte dans un champ est de réduire la taille du texte pour l'adapter aux dimensions de la cellule. Cela se fait en définissant la propriété [**ShrinkToFit**](https://reference.aspose.com/cells/java/com.aspose.cells/style#ShrinkToFit) à **true**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ShrinkingToFit-1.java" >}}

### **Fusion de cellules**

Comme Microsoft Excel, Aspose.Cells prend en charge la fusion de plusieurs cellules en une seule. Aspose.Cells propose deux approches pour cette tâche. Une manière est d'appeler la méthode [**Merge**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge(int,%20int,%20int,%20int)). La méthode prend les paramètres suivants pour fusionner les cellules:

- Première rangée : la première rangée à partir de laquelle commencer la fusion.
- Première colonne : la première colonne à partir de laquelle commencer la fusion.
- Nombre de rangées : le nombre de rangées à fusionner.
- Nombre de colonnes : le nombre de colonnes à fusionner.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "MergingCellsInWorksheet.-1.java" >}}


### **Direction du texte**

Il est possible de définir l'ordre de lecture du texte dans les cellules. L'ordre de lecture est l'ordre visuel dans lequel les caractères, les mots, etc. sont affichés. Par exemple, l'anglais est une langue de gauche à droite tandis que l'arabe est une langue de droite à gauche.

L'ordre de lecture est défini avec la propriété [**TextDirection**](https://reference.aspose.com/cells/java/com.aspose.cells/style#TextDirection). Aspose.Cells fournit des types de direction de texte prédéfinis dans l'énumération [**TextDirectionType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextDirection).

|**Types de direction du texte**|**Description**|
| :- | :- |
|Context|L'ordre de lecture en accord avec la langue du premier caractère saisi|
|LeftToRight|Ordre de lecture de gauche à droite|
|RightToLeft|Ordre de lecture de droite à gauche|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ChangeTextDirection-1.java" >}}

## **Sujets avancés**
- [Modifier l'alignement des cellules et conserver la mise en forme existante](/cells/fr/java/change-cells-alignment-and-keep-existing-formatting/)
- [Sauts de ligne et retour à la ligne](/cells/fr/java/line-breaks-and-text-wrapping/)
