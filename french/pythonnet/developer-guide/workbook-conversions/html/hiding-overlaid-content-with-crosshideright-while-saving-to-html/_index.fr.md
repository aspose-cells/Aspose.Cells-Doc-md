---
title: Masquer le contenu superposé avec CrossHideRight lors de l enregistrement en HTML
type: docs
weight: 100
url: /fr/python-net/hiding-overlaid-content-with-crosshideright-while-saving-to/
---

## **Scénarios d'utilisation possibles**

Lorsque vous enregistrez votre fichier Excel en HTML, vous pouvez spécifier différents types de croisement pour les chaînes de cellules. Par défaut, Aspose.Cells pour Python via .NET génère du HTML selon Microsoft Excel, mais lorsque vous changez le type de croisement en [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype/), il cache toutes les chaînes situées à droite de la cellule qui sont superposées ou chevauchent la chaîne de la cellule.

## **Masquer le contenu superposé avec CrossHideRight lors de l'enregistrement en HTML**

Le code d'exemple suivant charge le [fichier Excel d'exemple](64716894.xlsx) et l'enregistre en [HTML de sortie](64716893.zip) après avoir défini [**HtmlSaveOptions.html_cross_string_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/html_cross_string_type) comme [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype/). La capture d'écran explique comment [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype/) affecte le HTML de sortie par rapport à la sortie par défaut.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
{{< app/cells/assistant language="python-net" >}}
