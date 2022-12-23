---
title: Convertir Excel en HTML avec info-bulle
type: docs
weight: 200
url: /fr/net/convert-excel-to-html-with-tooltip/
---
## **Convertir Excel en HTML avec info-bulle**

Il peut arriver que le texte soit coupé dans le HTML généré et que vous souhaitiez afficher le texte complet sous forme d'info-bulle sur l'événement de survol. Aspose.Cells prend en charge cela en fournissant**[HtmlSaveOptions.AddTooltipText](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/addtooltiptext)** la propriété. Réglage de la**[HtmlSaveOptions.AddTooltipText](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/addtooltiptext)** propriété à**vrai** ajoutera le texte complet sous forme d'info-bulle dans le HTML généré.

L'image suivante montre l'info-bulle dans le fichier HTML généré.

![tâche : image_autre_texte](convert-excel-to-html-with-tooltip_1.jpg)

 L'exemple de code suivant charge le[fichier excel source](98107416.xlsx) et génère le[fichier de sortie HTML](98107417.zip) avec l'info-bulle.

Exemple de code

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToHtmlWithTooltip-1.cs" >}}
