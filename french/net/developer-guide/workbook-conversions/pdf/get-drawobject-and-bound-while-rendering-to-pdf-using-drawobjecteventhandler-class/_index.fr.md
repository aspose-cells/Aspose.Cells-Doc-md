---
title: Obtenez DrawObject et Bound lors du rendu au format PDF à l'aide de la classe DrawObjectEventHandler
type: docs
weight: 70
url: /fr/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---
## **Scénarios d'utilisation possibles**

 Aspose.Cells fournit une classe abstraite[**DrawObjectEventHandlerDrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) qui a un[**Dessiner()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw)méthode. L'utilisateur peut implémenter[**DrawObjectEventHandlerDrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) et utiliser le[**Dessiner()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw) méthode pour obtenir le[**DessinerObjet**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)et lié lors du rendu d'Excel en PDF ou en image. Voici une brève description des paramètres de[**Dessiner()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw)méthode.

-  drawObject :[**DessinerObjet**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) sera initialisé et retourné lors du rendu

- x : à gauche de[**DessinerObjet**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- y : Haut de[**DessinerObjet**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- largeur : Largeur de[**DessinerObjet**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- hauteur : Hauteur de[**DessinerObjet**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

Si vous convertissez un fichier Excel en PDF, vous pouvez utiliser[**DrawObjectEventHandlerDrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)classe avec[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler) . De même, si vous convertissez un fichier Excel en image, vous pouvez utiliser[**DrawObjectEventHandlerDrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)classe avec[**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/drawobjecteventhandler).

## **Obtenez DrawObject et Bound lors du rendu au format Pdf à l'aide de la classe DrawObjectEventHandler**

 Veuillez consulter l'exemple de code suivant. Il charge le[exemple de fichier Excel](64716821.xlsx) et l'enregistre sous[PDF de sortie](64716822.pdf). Lors du rendu au format PDF, il utilise[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler)propriété et capture le[**DessinerObjet**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) et Liaison de cellules et d'objets existants, par exemple des images, etc. Si le[**DessinerObjet**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) type est Cell, il imprime ses Bound et StringValue. Et si le[**DessinerObjet**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)type est Image, il imprime son Bound et Shape Name. Veuillez consulter la sortie de la console de l'exemple de code ci-dessous pour plus d'aide.

## **Exemple de code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.cs" >}}

## **Sortie console**

{{< highlight "java" >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
