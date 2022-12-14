---
title: Sortir une page vierge lorsqu'il n'y a rien à imprimer
type: docs
weight: 90
url: /fr/net/output-blank-page-when-there-is-nothing-to-print/
---
## **Scénarios d'utilisation possibles**

Si la feuille est vide, Aspose.Cells n'imprimera rien lorsque vous exporterez la feuille de calcul vers l'image. Vous pouvez modifier ce comportement en utilisant[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/outputblankpagewhennothingtoprint) propriété. Quand vous le réglerez**vrai**, il imprimera la page vierge.

## **Sortir une page vierge lorsqu'il n'y a rien à imprimer**

L'exemple de code suivant crée le classeur vide qui a une feuille de calcul vide et restitue la feuille de calcul vide à une image après avoir défini le[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/outputblankpagewhennothingtoprint) propriété comme**vrai**. Par conséquent, il génère la page vierge car il n'y a rien à imprimer comme vous pouvez le voir dans l'image ci-dessous.

![tâche : image_autre_texte](output-blank-page-when-there-is-nothing-to-print_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.cs" >}}
