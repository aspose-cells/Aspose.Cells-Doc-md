---
title: Convertir Excel en HTML avec une info-bulle
type: docs
weight: 200
url: /fr/python-net/convert-excel-to-html-with-tooltip/
description: Cette rubrique vous montre comment convertir Excel en HTML avec une info-bulle en utilisant Aspose.Cells for Python via NET.
keywords: Python Convert Excel to HTML with tooltip, Convert Excel to HTML with tooltip Python via NET, Python via NET Excel to HTML with tooltip, Python Workbook to HTML with tooltip.
---
##  **Convertir Excel en HTML avec une info-bulle**

Il peut arriver que le texte soit coupé dans le HTML généré et que vous souhaitiez afficher le texte complet sous forme d'info-bulle lors de l'événement de survol. Aspose.Cells soutient cela en fournissant**[HtmlSaveOptions.add_tooltip_text](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/add_tooltip_text/)** propriété. Réglage du**[HtmlSaveOptions.add_tooltip_text](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/add_tooltip_text/)** propriété à**vrai** ajoutera le texte complet sous forme d'info-bulle dans le HTML généré.

L'image suivante montre l'info-bulle dans le fichier HTML généré.

![tâche : image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

 L'exemple de code suivant charge le[fichier Excel source](98107416.xlsx) et génère le[sortie du fichier HTML](98107417.zip) avec l'info-bulle.

Exemple de code

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ConvertExcelFileToHtmlWithTooltip-1.py" >}}
