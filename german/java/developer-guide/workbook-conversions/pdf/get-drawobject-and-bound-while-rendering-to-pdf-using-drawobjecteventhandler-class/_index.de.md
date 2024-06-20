---
title: Holen Sie sich DrawObject und Bound während des Renderns im PDF mit der DrawObjectEventHandler Klasse
type: docs
weight: 60
url: /de/java/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells bietet eine abstrakte Klasse [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler), die eine Methode [**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)) hat. Der Benutzer kann [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) implementieren und die Methode [**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)) nutzen, um das [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) und **Bound** beim Rendern von Excel in PDF oder Bild zu erhalten. Hier ist eine kurze Beschreibung der Parameter der Methode [**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)).

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) wird initialisiert und zurückgegeben beim Rendern

- x: Links von [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- y: Oben von [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- width: Breite von [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- height: Höhe von [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

Wenn Sie eine Excel-Datei in PDF rendern, können Sie die Klasse [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) mit [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler) nutzen. Ebenso, wenn Sie eine Excel-Datei in Bild rendern, können Sie die Klasse [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) mit [**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DrawObjectEventHandler) nutzen.

## **Holen Sie sich DrawObject und Bound beim Rendern in PDF unter Verwendung der DrawObjectEventHandler-Klasse**

Bitte beachten Sie den folgenden Beispielcode. Es lädt die [Beispiel-Excel-Datei](64716843.xlsx) und speichert sie als [Ausgabe-PDF](64716842.pdf). Beim Rendern in PDF nutzt es die Eigenschaft [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler) und erfasst das [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) und **Bound** bereits vorhandener Zellen und Objekte wie z. B. Bilder usw. Wenn der drawObject-Typ Cell ist, gibt es seinen Bound und StringValue aus. Und wenn der drawObject-Typ Image ist, gibt es seinen Bound und Shape-Name aus. Bitte sehen Sie die Konsolenausgabe des unten gegebenen Beispielcodes für weitere Hilfe.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.java" >}}

## **Konsolenausgabe**

{{< highlight java >}}

[X]: 153.60349 [Y]: 82.94118 [Width]: 103.203476 [Height]: 14.470589 [Cell Value]: This is sample text.

\----------------------

[X]: 267.28854 [Y]: 153.12354 [Width]: 161.25542 [Height]: 128.78824 [Shape Name]: Sun

\----------------------

{{< /highlight >}}
