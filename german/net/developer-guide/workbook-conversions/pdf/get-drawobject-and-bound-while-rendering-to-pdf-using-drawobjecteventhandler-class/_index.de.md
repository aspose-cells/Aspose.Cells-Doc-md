---
title: Holen Sie sich DrawObject und Bound beim Rendern auf PDF mithilfe der DrawObjectEventHandler-Klasse
type: docs
weight: 70
url: /de/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---
## **Mögliche Nutzungsszenarien**

 Aspose.Cells stellt eine abstrakte Klasse bereit[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) das hat ein[**Ziehen()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw)Methode. Der Benutzer kann implementieren[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) und nutze die[**Ziehen()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw) Methode, um die zu erhalten[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)und Bound beim Rendern von Excel auf PDF oder Image. Hier ist eine kurze Beschreibung der Parameter der[**Ziehen()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw)Methode.

-  drawObject:[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) wird beim Rendern initialisiert und zurückgegeben

- x: Links von[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- y: Spitze von[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- Breite: Breite von[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- Höhe: Höhe von[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

Wenn Sie eine Excel-Datei in PDF rendern, können Sie sie verwenden[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)Klasse mit[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler) . Wenn Sie eine Excel-Datei in ein Bild rendern, können Sie auf ähnliche Weise verwenden[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)Klasse mit[**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/drawobjecteventhandler).

## **Holen Sie sich DrawObject und Bound beim Rendern in PDF mit der Klasse DrawObjectEventHandler**

 Bitte sehen Sie sich den folgenden Beispielcode an. Es lädt die[Beispiel-Excel-Datei](64716821.xlsx) und speichert es als[Ausgang PDF](64716822.pdf). Beim Rendern auf PDF wird es verwendet[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler)Eigentum und erfasst die[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) und Bound bestehender Zellen und Objekte zB Bilder etc. Wenn die[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) type ist Cell, es druckt seinen Bound und StringValue. Und wenn die[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)type ist Image, es gibt seinen Bound- und Shape-Namen aus. Weitere Hilfe finden Sie in der Konsolenausgabe des unten angegebenen Beispielcodes.

## **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.cs" >}}

## **Konsolenausgabe**

{{< highlight "java" >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
