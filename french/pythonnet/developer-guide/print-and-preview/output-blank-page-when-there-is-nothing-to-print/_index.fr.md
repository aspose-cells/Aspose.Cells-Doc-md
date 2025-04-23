---
title: Afficher une page blanche lorsqu il n y a rien à imprimer
type: docs
weight: 90
url: /fr/python-net/output-blank-page-when-there-is-nothing-to-print/
---

## **Scénarios d'utilisation possibles**

Si la feuille est vide, alors Aspose.Cells pour Python via .NET n'affichera rien lors de l'exportation de la feuille de calcul en image. Vous pouvez modifier ce comportement en utilisant la propriété [**ImageOrPrintOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/output_blank_page_when_nothing_to_print). Lorsque vous la définissez à **true**, cela affichera la page blanche.

## **Afficher une page vierge lorsqu'il n'y a rien à imprimer**

Le code d'exemple suivant crée le classeur vide qui a une feuille de calcul vide et rend la feuille de calcul vide en une image après avoir défini la [**ImageOrPrintOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/output_blank_page_when_nothing_to_print) propriété comme **true**. Par conséquent, cela génère une page blanche car il n'y a rien à imprimer, ce que vous pouvez voir dans l'image ci-dessous.

![todo:image_alt_text](1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-OutputBlankPageWhenThereIsNothingToPrint-1.py" >}}

