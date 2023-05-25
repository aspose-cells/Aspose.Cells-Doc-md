---
title: Sortir une page vierge lorsqu'il n'y a rien à imprimer
type: docs
weight: 80
url: /fr/java/output-blank-page-when-there-is-nothing-to-print/
---
##  **Scénarios d'utilisation possibles**

Si la feuille est vide, Aspose.Cells n'imprimera rien lorsque vous exporterez la feuille de calcul vers l'image. Vous pouvez modifier ce comportement en utilisant[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint)propriété. Lorsque vous le définirez sur *true**, il imprimera la page vierge.

##  **Sortir une page vierge lorsqu'il n'y a rien à imprimer**

L'exemple de code suivant crée le classeur vide qui a une feuille de calcul vide et restitue la feuille de calcul vide à une image après avoir défini le[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint)propriété comme *vrai**. Par conséquent, il génère la page vierge car il n'y a rien à imprimer que vous pouvez voir ci-dessous.

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

##  **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.java" >}}
