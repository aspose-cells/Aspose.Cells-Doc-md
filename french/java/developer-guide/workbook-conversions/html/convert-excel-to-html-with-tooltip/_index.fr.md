---
title: Convertir Excel en HTML avec info-bulle
type: docs
weight: 150
url: /fr/java/convert-excel-to-html-with-tooltip/
---
## **Convertir Excel en HTML avec info-bulle**

Il peut arriver que le texte soit coupé dans le HTML généré et que vous souhaitiez afficher le texte complet sous forme d'info-bulle sur l'événement de survol. Aspose.Cells prend en charge cela en fournissant**[HtmlSaveOptions.AddTooltipText](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#AddTooltipText)**la propriété. Réglage de la**[HtmlSaveOptions.AddTooltipText](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#AddTooltipText)**propriété à**vrai**ajoutera le texte complet sous forme d'info-bulle dans le HTML généré.

L'image suivante montre l'info-bulle dans le fichier HTML généré.

![tâche : image_autre_texte](convert-excel-to-html-with-tooltip_1.jpg)

L'exemple de code suivant charge le[fichier excel source](AddTooltipToHtmlSample.xlsx)et génère le[fichier de sortie HTML](AddTooltipToHtmlSample_out.zip)avec l'info-bulle.

## Exemple de code

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToHtmlWithTooltip-1.java" >}}
