---
title: Obtenez DrawObject et Bound lors du rendu au format PDF à l'aide de la classe DrawObjectEventHandler
type: docs
weight: 60
url: /fr/java/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---
## **Scénarios d'utilisation possibles**

Aspose.Cells fournit une classe abstraite[**DrawObjectEventHandlerDrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) qui a un[**dessiner()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)) méthode. L'utilisateur peut implémenter[**DrawObjectEventHandlerDrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)et utiliser le[**dessiner()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)) méthode pour obtenir le[**DessinerObjet**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)et**Bondir**lors du rendu d'Excel au format PDF ou Image. Voici une brève description des paramètres de[**dessiner()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)) méthode.

-  drawObject :[**DessinerObjet**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)sera initialisé et retourné lors du rendu

- x : à gauche de[**DessinerObjet**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- y : Haut de[**DessinerObjet**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- largeur : Largeur de[**DessinerObjet**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- hauteur : Hauteur de[**DessinerObjet**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

Si vous convertissez un fichier Excel en PDF, vous pouvez utiliser[**DrawObjectEventHandlerDrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)classe avec[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler). De même, si vous convertissez un fichier Excel en image, vous pouvez utiliser[**DrawObjectEventHandlerDrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)classe avec[**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DrawObjectEventHandler).

## **Obtenez DrawObject et Bound lors du rendu au format Pdf à l'aide de la classe DrawObjectEventHandler**

Veuillez consulter l'exemple de code suivant. Il charge le[exemple de fichier Excel](64716843.xlsx)et l'enregistre sous[PDF de sortie](64716842.pdf). Lors du rendu au format PDF, il utilise[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler)propriété et capture le[**DessinerObjet**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) et**Bondir** de cellules et d'objets existants, par exemple des images, etc. Si le type drawObject est Cell, il imprime ses Bound et StringValue. Et si le type drawObject est Image, il imprime son Bound et Shape Name. Veuillez consulter la sortie de la console de l'exemple de code ci-dessous pour plus d'aide.

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.java" >}}

## **Sortie console**

{{< highlight "java" >}}

[X]: 153.60349 [Y]: 82.94118 [Width]: 103.203476 [Height]: 14.470589 [Cell Value]: This is sample text.

\----------------------

[X]: 267.28854 [Y]: 153.12354 [Width]: 161.25542 [Height]: 128.78824 [Shape Name]: Sun

\----------------------

{{< /highlight >}}
