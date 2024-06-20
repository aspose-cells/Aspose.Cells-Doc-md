---
title: Masquer le contenu superposé lors de la conversion d Excel en HTML
type: docs
weight: 40
url: /fr/python-java/hide-overlaid-content-while-converting-excel-to/
---

## **Masquer le contenu superposé lors de la conversion d'Excel en HTML**
Lorsque vous enregistrez votre fichier Excel en HTML, vous pouvez spécifier différents types de croisement pour les chaînes de cellules. Par défaut, Aspose.Cells génère du HTML selon Microsoft Excel, mais lorsque vous modifiez le [HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType) en [CROSS_HIDE_RIGHT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT), cela masque toutes les chaînes sur le côté droit de la cellule qui sont superposées ou chevauchent la chaîne de la cellule.

Le code d'exemple suivant charge le [fichier Excel d'exemple](sampleHidingOverlaidContentWithCrossHideRight.xlsx) et le sauvegarde en [HTML de sortie](HTML-outputHidingOverlaidContentWithCrossHideRight.zip) après avoir défini le [HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType) en [CROSS_HIDE_RIGHT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT). La capture d'écran explique comment [CROSS_HIDE_RIGHT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT) affecte le HTML de sortie par rapport à la sortie par défaut.

![todo:image_alt_text](Hiding-Overlaid-Content-With-CrossHideRight.png)
## **Code d'exemple**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
