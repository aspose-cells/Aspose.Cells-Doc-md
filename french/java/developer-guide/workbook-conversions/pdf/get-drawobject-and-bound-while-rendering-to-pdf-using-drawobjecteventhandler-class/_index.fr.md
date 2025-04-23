---
title: Obtenez DrawObject et Bound lors du rendu au format PDF en utilisant la classe DrawObjectEventHandler
type: docs
weight: 60
url: /fr/java/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells fournit une classe abstraite [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) qui possède une méthode [**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw-com.aspose.cells.DrawObject-float-float-float-float-). L'utilisateur peut implémenter [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) et utiliser la méthode [**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw-com.aspose.cells.DrawObject-float-float-float-float-) pour obtenir [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) et **Bound** lors du rendu d'Excel en PDF ou en image. Voici une brève description des paramètres de la méthode [**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw-com.aspose.cells.DrawObject-float-float-float-float-).

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) sera initialisé et retourné lors du rendu

- x: Gauche de [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- y: Haut de [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- largeur: Largeur de [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- hauteur: Hauteur de [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

Si vous générez un fichier Excel au format PDF, vous pouvez utiliser la classe [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) avec [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler). De même, si vous générez un fichier Excel au format Image, vous pouvez utiliser la classe [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) avec [**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DrawObjectEventHandler).

## **Obtenez DrawObject et Bound lors du rendu au format Pdf en utilisant la classe DrawObjectEventHandler**

Veuillez consulter le code d'exemple suivant. Il charge le [fichier Excel d'exemple](64716843.xlsx) et le sauvegarde en [PDF de sortie](64716842.pdf). Lors du rendu en PDF, il utilise la propriété [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler) et capture le [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) et **Bound** des cellules et des objets existants, tels que les images, etc. Si le type de drawObject est Cell, il affiche son Bound et StringValue. Et si le type de drawObject est Image, il affiche son Bound et Nom de forme. Veuillez consulter la sortie de la console du code d'exemple ci-dessous pour plus d'aide.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.java" >}}

## **Sortie console**

{{< highlight java >}}

[X]: 153.60349 [Y]: 82.94118 [Width]: 103.203476 [Height]: 14.470589 [Cell Value]: This is sample text.

\----------------------

[X]: 267.28854 [Y]: 153.12354 [Width]: 161.25542 [Height]: 128.78824 [Shape Name]: Sun

\----------------------

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
