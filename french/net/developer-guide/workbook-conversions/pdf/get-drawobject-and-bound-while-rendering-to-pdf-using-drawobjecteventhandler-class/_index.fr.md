---
title: Obtenez DrawObject et Bound lors du rendu au format PDF en utilisant la classe DrawObjectEventHandler
type: docs
weight: 70
url: /fr/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells fournit une classe abstraite [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) qui a une méthode [**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw). L'utilisateur peut implémenter [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) et utiliser la méthode [**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw) pour obtenir [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) et Bound lors du rendu Excel au format PDF ou Image. Voici une brève description des paramètres de la méthode [**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw).

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) sera initialisé et renvoyé lors du rendu

- x: Gauche de [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- y: Haut de [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- largeur: Largeur de [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- hauteur: Hauteur de [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

Si vous convertissez un fichier Excel en PDF, vous pouvez utiliser la classe [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) avec [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler). De même, si vous convertissez un fichier Excel en Image, vous pouvez utiliser la classe [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) avec [**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/drawobjecteventhandler).

## **Obtenez DrawObject et Bound lors du rendu au format Pdf en utilisant la classe DrawObjectEventHandler**

Veuillez voir le code d'exemple suivant. Il charge le [fichier Excel d'exemple](64716821.xlsx) et l'enregistre en [PDF de sortie](64716822.pdf). Lors du rendu au format PDF, il utilise la propriété [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler) et capture [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) et Bound des cellules et objets existants tels que des images, etc. Si le type [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) est Cellule, il affiche sa Bound et StringValue. Et si le type [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) est Image, il affiche sa Bound et le nom de la forme. Veuillez consulter la sortie console du code d'exemple ci-dessous pour plus d'aide.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.cs" >}}

## **Sortie console**

{{< highlight java >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
