---
title: Afficher une page blanche lorsqu il n y a rien à imprimer
type: docs
weight: 80
url: /fr/java/output-blank-page-when-there-is-nothing-to-print/
---

## **Scénarios d'utilisation possibles**

Si la feuille est vide, alors Aspose.Cells n'imprimera rien lors de l'exportation de la feuille de calcul en image. Vous pouvez changer ce comportement en utilisant la propriété [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint). Lorsque vous la définirez sur **true**, cela affichera la page blanche.

## **Afficher une page vierge lorsqu'il n'y a rien à imprimer**

Le code d'exemple suivant crée le classeur vide qui contient une feuille de calcul vide et rend la feuille de calcul vide en image après avoir défini la propriété [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint) sur **true**. Par conséquent, cela génère une page blanche car il n'y a rien à imprimer, comme vous pouvez le voir ci-dessous.

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.java" >}}
