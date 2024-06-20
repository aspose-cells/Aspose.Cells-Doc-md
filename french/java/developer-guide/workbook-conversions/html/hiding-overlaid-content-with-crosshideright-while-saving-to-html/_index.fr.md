---
title: Masquer le contenu superposé avec CrossHideRight lors de l enregistrement en HTML
type: docs
weight: 100
url: /fr/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/
---

## **Scénarios d'utilisation possibles**

Lorsque vous enregistrez votre fichier Excel au format HTML, vous pouvez spécifier différents types de croix pour les chaînes de cellules. Par défaut, Aspose.Cells génère un HTML selon Microsoft Excel, mais lorsque vous changez le [**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType) en [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT), cela masque toutes les chaînes du côté droit de la cellule qui sont superposées ou en recouvrement avec la chaîne de cellule.

## **Masquer le contenu superposé avec CrossHideRight lors de l'enregistrement au format HTML**

Le code d'exemple suivant charge le [fichier Excel d'exemple](64716916.xlsx) et l'enregistre dans le [fichier HTML de sortie](64716915.zip) après avoir défini le [**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType) comme [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT). La capture d'écran explique comment [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT) affecte le fichier HTML de sortie à partir de la sortie par défaut.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.java" >}}
