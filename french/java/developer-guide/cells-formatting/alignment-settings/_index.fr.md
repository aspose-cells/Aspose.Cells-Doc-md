---
title: Paramètres d'alignement
type: docs
weight: 20
url: /fr/java/cells-alignment-settings/
---
## **Configuration des paramètres d'alignement**

## **Paramètres d'alignement dans Microsoft Excel**

Quiconque a utilisé Microsoft Excel pour formater des cellules connaîtra les paramètres d'alignement dans Microsoft Excel.

Comme vous pouvez le voir sur la figure ci-dessus, il existe différents types d'options d'alignement :

- Alignement du texte (horizontal et vertical)
- Échancrure.
- Orientation.
- Contrôle du texte.
- Sens du texte.

Tous ces paramètres d'alignement sont entièrement pris en charge par Aspose.Cells et sont discutés plus en détail ci-dessous.

## **Paramètres d'alignement dans Aspose.Cells**

 Aspose.Cells fournit[**ObtenirStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle) et[**DéfinirStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle) méthodes pour la[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) class qui sont utilisées pour obtenir et définir la mise en forme d'une cellule. Le[**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/style)fournit des propriétés utiles pour configurer les paramètres d'alignement.

 Sélectionnez n'importe quel type d'alignement de texte à l'aide de la[**Type d'alignement de texte**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype) énumération. Les types d'alignement de texte prédéfinis dans le[**Type d'alignement de texte**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype)l'énumération sont :

|**Types d'alignement de texte**|**Description**|
|:- |:- |
|Fond|Représente l'alignement du texte inférieur|
|Centre|Représente l'alignement du texte au centre|
|CenterAcross|Représente le centre sur l'alignement du texte|
|Distribué|Représente l'alignement de texte distribué|
|Remplir|Représente l'alignement du texte de remplissage|
|Général|Représente l'alignement général du texte|
|Justifier|Représente l'alignement du texte justifié|
|Gauche|Représente l'alignement du texte à gauche|
|Droit|Représente l'alignement du texte à droite|
|Haut|Représente l'alignement supérieur du texte|
|JustifiéBas|Aligne le texte avec une longueur kashida ajustée pour le texte arabe.|
|ThaïDistribué|Distribue le texte thaï en particulier, car chaque caractère est traité comme un mot.|

{{% alert color="primary" %}}

 Vous pouvez également appliquer le paramètre de justification distribuée à l'aide de la[**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsJustifyDistributed) la propriété.

{{% /alert %}}

## **Alignement horizontal, vertical et indentation**

 Utilisez le[**AlignementHorizontal**](https://reference.aspose.com/cells/java/com.aspose.cells/style#horizontalalignment) propriété pour aligner le texte horizontalement et[**Alignement vertical**](https://reference.aspose.com/cells/java/com.aspose.cells/style#verticalalignment)propriété pour aligner le texte verticalement.
 Il est possible de définir le niveau d'indentation du texte dans une cellule avec la[**Niveau d'indentation**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IndentLevel) la propriété
et tt n'a d'effet que lorsque l'alignement horizontal est à gauche ou à droite.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-1.java" >}}


## **Orientation**

 Définissez l'orientation (rotation) du texte dans une cellule avec la[**Angle de rotation**](https://reference.aspose.com/cells/java/com.aspose.cells/style#RotationAngle)la propriété.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-Orientation-1.java" >}}

## **Contrôle du texte**

La section suivante explique comment contrôler le texte en définissant l'habillage du texte, le rétrécissement et d'autres options de formatage.

### **Habillage du texte**

 L'habillage du texte dans une cellule facilite la lecture : la hauteur de la cellule s'ajuste pour s'adapter à tout le texte, au lieu de le couper ou de déborder dans les cellules adjacentes. Activez ou désactivez l'habillage du texte avec le[**EstEnveloppéTexte**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsTextWrapped)la propriété.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LineBreakTextWrapping-WrapText-1.java" >}}

### **Rétrécir pour s'adapter**

 Une option d'habillage du texte dans un champ consiste à réduire la taille du texte pour l'adapter aux dimensions d'une cellule. Cela se fait en réglant le[**Réduire pour s'adapter**](https://reference.aspose.com/cells/java/com.aspose.cells/style#ShrinkToFit) la propriété. à**vrai**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ShrinkingToFit-1.java" >}}

### **Fusion Cells**

 Comme Microsoft Excel, Aspose.Cells prend en charge la fusion de plusieurs cellules en une seule. Aspose.Cells propose deux approches pour cette tâche. Une façon consiste à appeler le[**Fusionner**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge(int,%20int,%20int,%20int)) méthode. La méthode prend les paramètres suivants pour fusionner les cellules :

- Première ligne : la première ligne à partir de laquelle commencer la fusion.
- Première colonne : la première colonne à partir de laquelle commencer la fusion.
- Nombre de lignes : le nombre de lignes à fusionner.
- Nombre de colonnes : le nombre de colonnes à fusionner.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "MergingCellsInWorksheet.-1.java" >}}


### **Sens du texte**

Il est possible de définir l'ordre de lecture du texte dans les cellules. L'ordre de lecture est l'ordre visuel dans lequel les caractères, les mots, etc. sont affichés. Par exemple, l'anglais est une langue de gauche à droite tandis que l'arabe est une langue de droite à gauche.

 L'ordre de lecture est défini avec le[**Direction du texte**](https://reference.aspose.com/cells/java/com.aspose.cells/style#TextDirection) la propriété. Aspose.Cells fournit des types de direction de texte prédéfinis dans le[**TextDirectionType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextDirection)énumération.

|**Types d'orientation du texte**|**Description**|
|:- |:- |
|Contexte|L'ordre de lecture cohérent avec la langue du premier caractère saisi|
|De gauche à droite|Ordre de lecture de gauche à droite|
|De droite à gauche|Ordre de lecture de droite à gauche|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ChangeTextDirection-1.java" >}}

## **Sujets avancés**
- [Modifier l'alignement Cells et conserver la mise en forme existante](/cells/fr/java/change-cells-alignment-and-keep-existing-formatting/)
- [Sauts de ligne et retour à la ligne](/cells/fr/java/line-breaks-and-text-wrapping/)
