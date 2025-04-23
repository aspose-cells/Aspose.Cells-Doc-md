---
title: Rendre une séquence de pages à l aide des propriétés PageIndex et PageCount de ImageOrPrintOptions
type: docs
weight: 110
url: /fr/python-net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/

---

## **Scénarios d'utilisation possibles**

Vous pouvez rendre une séquence de pages de votre fichier Excel en images en utilisant Aspose.Cells pour Python via .NET avec les propriétés [**ImageOrPrintOptions.page_index**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_index) et [**ImageOrPrintOptions.page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_count). Ces propriétés sont utiles lorsqu'il y a beaucoup de pages, par exemple des milliers, dans votre feuille de calcul, mais que vous souhaitez en rendre seulement quelques-unes. Cela permet non seulement d'économiser du temps de traitement, mais aussi de réduire la consommation de mémoire du processus de rendu.

## **Séquence de rendu des pages à l'aide des propriétés PageIndex et PageCount d'ImageOrPrintOptions**

Le code d'exemple suivant charge le [fichier Excel d'exemple](55541781.xlsx) et ne rend que les pages 4, 5, 6 et 7 en utilisant les propriétés [**ImageOrPrintOptions.page_index**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_index) et [**ImageOrPrintOptions.page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_count). Voici les pages rendues générées par le code.

|![todo:image_alt_text](1)|![todo:image_alt_text](2)|
| :- | :- |
|![todo:image_alt_text](3)|![todo:image_alt_text](4)|

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-RenderLimitedNoOfSequentialPages-1.py" >}}
