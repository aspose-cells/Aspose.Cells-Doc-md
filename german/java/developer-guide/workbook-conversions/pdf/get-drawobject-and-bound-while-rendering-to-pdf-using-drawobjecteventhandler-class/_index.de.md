---
title: Holen Sie sich DrawObject und Bound beim Rendern auf PDF mithilfe der DrawObjectEventHandler-Klasse
type: docs
weight: 60
url: /de/java/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---
## **Mögliche Nutzungsszenarien**

Aspose.Cells stellt eine abstrakte Klasse bereit[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) das hat ein[**zeichnen()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)) Methode. Der Benutzer kann implementieren[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)und nutze die[**zeichnen()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float))-Methode, um die[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)und**Gebunden**beim Rendern von Excel auf PDF oder Image. Hier ist eine kurze Beschreibung der Parameter der[**zeichnen()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)) Methode.

-  drawObject:[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)wird beim Rendern initialisiert und zurückgegeben

- x: Links von[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- y: Spitze von[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- Breite: Breite von[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- Höhe: Höhe von[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

Wenn Sie eine Excel-Datei in PDF rendern, können Sie sie verwenden[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)Klasse mit[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler). Wenn Sie eine Excel-Datei in ein Bild rendern, können Sie auf ähnliche Weise verwenden[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)Klasse mit[**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DrawObjectEventHandler).

## **Holen Sie sich DrawObject und Bound beim Rendern in PDF mit der Klasse DrawObjectEventHandler**

Bitte sehen Sie sich den folgenden Beispielcode an. Es lädt die[Beispiel-Excel-Datei](64716843.xlsx)und speichert es als[Ausgang PDF](64716842.pdf). Beim Rendern auf PDF wird es verwendet[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler)Eigentum und erfasst die[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) und**Gebunden**bestehender Zellen und Objekte, zB Bilder usw. Wenn der drawObject-Typ Cell ist, werden Bound und StringValue ausgegeben. Und wenn der drawObject-Typ Image ist, gibt es seinen Bound- und Shape-Namen aus. Weitere Hilfe finden Sie in der Konsolenausgabe des unten angegebenen Beispielcodes.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.java" >}}

## **Konsolenausgabe**

{{< highlight "java" >}}

[X]: 153.60349 [Y]: 82.94118 [Width]: 103.203476 [Height]: 14.470589 [Cell Value]: This is sample text.

\----------------------

[X]: 267.28854 [Y]: 153.12354 [Width]: 161.25542 [Height]: 128.78824 [Shape Name]: Sun

\----------------------

{{< /highlight >}}
