---
title: Masquer le contenu superposé lors de la conversion d'Excel en HTML
type: docs
weight: 40
url: /fr/python-java/hide-overlaid-content-while-converting-excel-to/
---
## **Masquer le contenu superposé lors de la conversion d'Excel en HTML**
Lorsque vous enregistrez votre fichier Excel au HTML, vous pouvez spécifier différents types croisés pour les chaînes de cellules. Par défaut, Aspose.Cells génère HTML selon Microsoft Excel mais lorsque vous modifiez le[HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType)à[TRAVERSER_CACHER_DROIT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT)ensuite, il masque toutes les chaînes du côté droit de la cellule qui sont superposées ou qui se chevauchent avec la chaîne de cellule.

L'exemple de code suivant charge le[exemple de fichier Excel](sampleHidingOverlaidContentWithCrossHideRight.xlsx)et l'enregistre dans[sortie HTML](HTML-outputHidingOverlaidContentWithCrossHideRight.zip)après avoir réglé le[HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType)comme[TRAVERSER_CACHER_DROIT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT). La capture d'écran explique comment[TRAVERSER_CACHER_DROIT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT)affecte la sortie HTML de la sortie par défaut.

![tâche : image_autre_texte](Hiding-Overlaid-Content-With-CrossHideRight.png)
## **Exemple de code**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
