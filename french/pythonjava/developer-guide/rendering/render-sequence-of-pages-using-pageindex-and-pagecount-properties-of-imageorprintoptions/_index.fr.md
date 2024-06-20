---
title: Rendre une séquence de pages à l aide des propriétés PageIndex et PageCount de ImageOrPrintOptions
type: docs
weight: 10
url: /fr/python-java/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/
---

## **Séquence de rendu des pages à l'aide des propriétés PageIndex et PageCount d'ImageOrPrintOptions**
Vous pouvez rendre une séquence de pages de votre fichier Excel en images en utilisant Aspose.Cells avec les propriétés [ImageOrPrintOptions.PageIndex](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageIndex) et [ImageOrPrintOptions.PageCount](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageCount). Ces propriétés sont utiles lorsque vous avez par exemple des milliers de pages dans votre feuille de calcul mais que vous voulez en rendre seulement certaines. Cela permet non seulement d'économiser du temps de traitement, mais aussi de réduire la consommation de mémoire du processus de rendu.

Le code d'exemple suivant charge le fichier Excel d'exemple et rend uniquement les pages 4, 5, 6 et 7 en utilisant les propriétés [ImageOrPrintOptions.PageIndex](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageIndex) et [ImageOrPrintOptions.PageCount](https://reference.aspose.com/cells/python/asposecells.api/ImageOrPrintOptions#PageCount). Voici les images des pages rendues générées par le code d'exemple.

|![todo:image_alt_text](outputImage-4.png)|![todo:image_alt_text](outputImage-5.png)|
| :- | :- |
|![todo:image_alt_text](outputImage-6.png)|![todo:image_alt_text](outputImage-7.png)|



## **Code d'exemple**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderLimitedNoOfSequentialPages.py" >}}
