---
title: Rendre une séquence de pages à l aide des propriétés PageIndex et PageCount de ImageOrPrintOptions
type: docs
weight: 100
url: /fr/java/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/
---

## **Scénarios d'utilisation possibles**

Vous pouvez rendre une séquence de pages de votre fichier Excel en images en utilisant Aspose.Cells avec les propriétés [**ImageOrPrintOptions.PageIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#PageIndex) et [**ImageOrPrintOptions.PageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#PageCount). Ces propriétés sont utiles lorsqu'il y a par exemple des milliers de pages dans votre feuille de calcul, mais que vous ne souhaitez en rendre que certaines. Cela permet non seulement d'économiser du temps de traitement, mais aussi de réduire la consommation de mémoire du processus de rendu.

## **Séquence de rendu des pages à l'aide des propriétés PageIndex et PageCount d'ImageOrPrintOptions**

Le code d'exemple suivant charge le [fichier Excel d'exemple](55541812.xlsx) et ne rend que les pages 4, 5, 6 et 7 en utilisant les propriétés [**ImageOrPrintOptions.PageIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#PageIndex) et [**ImageOrPrintOptions.PageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#PageCount). Voici les pages rendues générées par le code.

|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_1.png)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_2.png)|
| :- | :- |
|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_3.png)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_4.png)|

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-RenderLimitedNoOfSequentialPages-1.java" >}}
{{< app/cells/assistant language="java" >}}
