---
title: Définir comment croiser la chaîne dans le HTML de sortie en utilisant HtmlCrossType
type: docs
weight: 140
url: /fr/java/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---

## **Scénarios d'utilisation possibles**

Lorsque la cellule contient du texte ou une chaîne mais qu'elle est plus grande que la largeur de la cellule, la chaîne déborde si la cellule suivante de la colonne suivante est nulle ou vide. Lorsque vous enregistrez votre fichier Excel au format HTML, vous pouvez contrôler ce débordement en spécifiant le type de croisement en utilisant l'énumération [**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType). Il a les valeurs suivantes

- [**HtmlCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT) : Afficher comme dans MS Excel, ce qui dépend de la cellule suivante. Si la cellule suivante est nulle, la chaîne sera coupée ou tronquée.

- [**HtmlCrossType.MS_EXPORT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#MS_EXPORT) : Afficher la chaîne comme dans MS Excel en exportant du HTML.

- [**HtmlCrossType.CROSS**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS) : Affiche la chaîne HTML croisée, la performance pour la création de grands fichiers HTML sera plus de dix fois plus rapide que si la valeur était définie sur [**DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT) ou [**FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL).

- [**HtmlCrossType.CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT) : Afficher une chaîne HTML croisée et masquer la chaîne de droite lorsque les textes se chevauchent.

- [**HtmlCrossType.FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL) : Affichage uniquement de la chaîne dans la largeur de la cellule.

## **Spécifier comment croiser la chaîne dans le HTML de sortie en utilisant HtmlCrossType**

Le code d'exemple suivant charge le [fichier Excel d'exemple](51740747.xlsx) et le sauvegarde au format HTML en spécifiant différents [**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType). Veuillez télécharger les fichiers HTML de sortie générés avec ce code. Le fichier Excel d'exemple contient l'image bordée de couleur rouge comme indiqué dans cette capture d'écran qui montre l'effet des valeurs [**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType) sur le HTML de sortie.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.java" >}}
