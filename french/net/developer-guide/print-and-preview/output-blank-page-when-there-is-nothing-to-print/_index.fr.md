---
title: Afficher une page blanche lorsqu il n y a rien à imprimer
type: docs
weight: 90
url: /fr/net/output-blank-page-when-there-is-nothing-to-print/
---

## **Scénarios d'utilisation possibles**

Si la feuille est vide, alors Aspose.Cells n'imprimera rien lors de l'exportation de la feuille de calcul en image. Vous pouvez changer ce comportement en utilisant [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/outputblankpagewhennothingtoprint) propriété. Lorsque vous la définirez sur **true**, cela imprimera la page blanche.

## **Afficher une page vierge lorsqu'il n'y a rien à imprimer**

Le code d'exemple suivant crée le classeur vide qui a une feuille de calcul vide et rend la feuille de calcul vide en une image après avoir défini la [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/outputblankpagewhennothingtoprint) propriété comme **true**. Par conséquent, cela génère une page blanche car il n'y a rien à imprimer, ce que vous pouvez voir dans l'image ci-dessous.

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
