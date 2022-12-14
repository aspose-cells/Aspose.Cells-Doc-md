---
title: Masquer le contenu superposé avec CrossHideRight lors de l'enregistrement au format HTML
type: docs
weight: 100
url: /fr/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/
---
## **Scénarios d'utilisation possibles**

Lorsque vous enregistrez votre fichier Excel au format HTML, vous pouvez spécifier différents types croisés pour les chaînes de cellules. Par défaut, Aspose.Cells génère du HTML selon Microsoft Excel mais lorsque vous modifiez le[**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType)à[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT)ensuite, il masque toutes les chaînes du côté droit de la cellule qui sont superposées ou qui se chevauchent avec la chaîne de cellule.

## **Masquer le contenu superposé avec CrossHideRight lors de l'enregistrement au format HTML**

L'exemple de code suivant charge le[exemple de fichier Excel](64716916.xlsx)et l'enregistre dans[sortie HTML](64716915.zip)après avoir réglé le[**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType)comme[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT). La capture d'écran explique comment[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT)affecte la sortie HTML de la sortie par défaut.

![tâche : image_autre_texte](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.java" >}}
