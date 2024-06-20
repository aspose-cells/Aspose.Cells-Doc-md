---
title: Convertir Excel en HTML avec info bulle
type: docs
weight: 150
url: /fr/java/convert-excel-to-html-with-tooltip/
---

## **Convertir Excel en HTML avec info-bulle**

Il peut arriver que le texte soit tronqué dans le HTML généré et que vous souhaitiez afficher le texte complet sous forme d'info-bulle lors de l'événement de survol. Aspose.Cells prend en charge cela en fournissant la propriété [**HtmlSaveOptions.AddTooltipText**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#AddTooltipText). La définition de la propriété [**HtmlSaveOptions.AddTooltipText**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#AddTooltipText) sur **true** ajoutera le texte complet comme info-bulle dans le HTML généré.

L'image suivante montre l'info-bulle dans le fichier HTML généré.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

L'exemple de code suivant charge le [fichier Excel source](AddTooltipToHtmlSample.xlsx) et génère le [fichier HTML de sortie](AddTooltipToHtmlSample_out.zip) avec l'infobulle.

## Code d'exemple

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToHtmlWithTooltip-1.java" >}}
