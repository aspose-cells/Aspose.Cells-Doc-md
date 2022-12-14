---
title: Spécifiez comment croiser la chaîne dans le HTML de sortie à l'aide de HtmlCrossType
type: docs
weight: 140
url: /fr/java/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---
## **Scénarios d'utilisation possibles**

Lorsque la cellule contient du texte ou une chaîne mais qu'elle est plus grande que la largeur de la cellule, la chaîne déborde si la cellule suivante dans la colonne suivante est nulle ou vide. Lorsque vous enregistrez votre fichier Excel en HTML, vous pouvez contrôler ce débordement en précisant le type croisé à l'aide de la[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)énumération. Il a les valeurs suivantes

- [**HtmlCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT): Affichage comme MS Excel qui dépend de la cellule suivante. Si la cellule suivante est nulle, la chaîne se croisera ou sera tronquée.

- [**HtmlCrossType.MS_EXPORT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#MS_EXPORT): Affichez la chaîne comme MS Excel exportant HTML.

- [**HtmlCrossType.CROSS**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS) : Afficher la chaîne croisée HTML, les performances de création de fichiers HTML volumineux seront plus de dix fois plus rapides qu'en définissant la valeur sur[**DÉFAUT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT) ou[**FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL).

- [**HtmlCrossType.CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT): Afficher la chaîne croisée HTML et masquer la chaîne de droite lorsque les textes se chevauchent.

- [**HtmlCrossType.FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL): affiche uniquement la chaîne dans la largeur de la cellule.

## **Spécifiez comment croiser la chaîne dans le HTML de sortie à l'aide de HtmlCrossType**

L'exemple de code suivant charge le[exemple de fichier Excel](51740747.xlsx)et l'enregistre au format HTML en spécifiant différents[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)Veuillez télécharger le[sortie HTML](51740745.zip) fichiers générés avec ce code. L'exemple de fichier Excel contient l'image bordée de rouge comme indiqué dans cette capture d'écran qui montre l'effet de la[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)valeurs sur le HTML de sortie.

![tâche : image_autre_texte](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.java" >}}
