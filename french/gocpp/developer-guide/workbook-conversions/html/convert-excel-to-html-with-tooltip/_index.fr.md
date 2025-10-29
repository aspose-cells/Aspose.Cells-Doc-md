---
title: Convertir Excel en HTML avec infobulle en utilisant C++
linktitle: Convertir Excel en HTML avec info bulle
type: docs
weight: 200
url: /fr/go-cpp/convert-excel-to-html-with-tooltip/
description: Convertissez Excel en HTML tout en ajoutant des infobulles avec Aspose.Cells en utilisant C++.
---

## **Convertir Excel en HTML avec info-bulle**

Il peut arriver que le texte soit coupé dans le HTML généré et vous souhaitez afficher le texte complet en tant que tooltip lors du survol. Aspose.Cells le supporte en utilisant la propriété [**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getaddtooltiptext/). En définissant la propriété [**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getaddtooltiptext/) à **true**, le texte complet sera ajouté en tant que tooltip dans le HTML généré.

L'image suivante montre l'info-bulle dans le fichier HTML généré.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

Le code d'exemple suivant charge le [fichier Excel source](98107416.xlsx) et génère le [fichier HTML de sortie](98107417.zip) avec l'infobulle.

Code d'exemple

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelToHtmlWithTooltip.go" >}}
