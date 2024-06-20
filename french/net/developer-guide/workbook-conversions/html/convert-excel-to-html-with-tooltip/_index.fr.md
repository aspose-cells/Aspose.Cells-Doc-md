---
title: Convertir Excel en HTML avec info bulle
type: docs
weight: 200
url: /fr/net/convert-excel-to-html-with-tooltip/
---

## **Convertir Excel en HTML avec info-bulle**

Il peut y avoir des cas où le texte est coupé dans le HTML généré et vous souhaitez afficher le texte complet sous forme d'info-bulle lors de l'événement de survol. Aspose.Cells prend en charge cela en fournissant la propriété [**HtmlSaveOptions.AddTooltipText**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/addtooltiptext). Définir la propriété [**HtmlSaveOptions.AddTooltipText**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/addtooltiptext) sur **true** ajoutera le texte complet sous forme d'info-bulle dans le HTML généré.

L'image suivante montre l'info-bulle dans le fichier HTML généré.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

Le code d'exemple suivant charge le [fichier Excel source](98107416.xlsx) et génère le [fichier HTML de sortie](98107417.zip) avec l'info-bulle.

Code d'exemple

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToHtmlWithTooltip-1.cs" >}}
