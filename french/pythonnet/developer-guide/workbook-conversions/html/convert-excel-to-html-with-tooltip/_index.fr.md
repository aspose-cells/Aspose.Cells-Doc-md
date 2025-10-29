---
title: Convertir Excel en HTML avec info bulle
type: docs
weight: 200
url: /fr/python-net/convert-excel-to-html-with-tooltip/
description: Ce sujet vous montre comment convertir Excel en HTML avec tooltip à l aide d Aspose.Cells pour Python via NET.
keywords: Python Convertir Excel en HTML avec tooltip, Convertir Excel en HTML avec tooltip Python via NET, Python via NET Excel en HTML avec tooltip, Classeur Python en HTML avec tooltip.
---

## **Convertir Excel en HTML avec info-bulle**

Il peut y avoir des cas où le texte est coupé dans le HTML généré et vous souhaitez afficher le texte complet sous forme d'info-bulle lors de l'événement de survol. Aspose.Cells prend en charge cela en fournissant la propriété [**HtmlSaveOptions.add_tooltip_text**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/add_tooltip_text/). Définir la propriété [**HtmlSaveOptions.add_tooltip_text**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/add_tooltip_text/) sur **true** ajoutera le texte complet sous forme d'info-bulle dans le HTML généré.

L'image suivante montre l'info-bulle dans le fichier HTML généré.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

Le code d'exemple suivant charge le [fichier Excel source](98107416.xlsx) et génère le [fichier HTML de sortie](98107417.zip) avec l'info-bulle.

Code d'exemple

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ConvertExcelFileToHtmlWithTooltip-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
