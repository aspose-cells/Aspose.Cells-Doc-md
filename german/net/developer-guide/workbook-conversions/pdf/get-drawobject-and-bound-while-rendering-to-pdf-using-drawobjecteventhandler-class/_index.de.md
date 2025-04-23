---
title: Holen Sie sich DrawObject und Bound während des Renderns im PDF mit der DrawObjectEventHandler Klasse
type: docs
weight: 70
url: /de/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells bietet eine abstrakte Klasse [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler), die eine Methode [**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw) hat. Der Benutzer kann [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) implementieren und die Methode [**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw) nutzen, um den [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) und Bound beim Rendern von Excel in PDF oder Bild zu erhalten. Hier ist eine kurze Beschreibung der Parameter der Methode [**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw).

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) wird initialisiert und beim Rendern zurückgegeben

- x: Links von [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- y: Oben von [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- width: Breite von [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- height: Höhe von [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

Wenn Sie eine Excel-Datei in PDF rendert, können Sie die Klasse [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) mit [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler) nutzen. Ebenso, wenn Sie eine Excel-Datei in ein Bild rendern, können Sie die Klasse [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) mit [**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/drawobjecteventhandler) nutzen.

## **Holen Sie sich DrawObject und Bound beim Rendern in PDF unter Verwendung der DrawObjectEventHandler-Klasse**

Bitte beachten Sie den folgenden Beispielcode. Es lädt die [Beispiel-Excel-Datei](64716821.xlsx) und speichert sie als [Ausgabe-PDF](64716822.pdf). Beim Rendern in PDF nutzt es die Eigenschaft [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler) und erfasst das [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) und Bound der vorhandenen Zellen und Objekte wie z.B. Bilder usw. Wenn der [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)-Typ eine Zelle ist, druckt er ihre Bound und String-Wert. Und wenn der [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)-Typ ein Bild ist, druckt er seine Bound und den Shape-Namen. Bitte sehen Sie die Konsolenausgabe des untenstehenden Beispielcodes für mehr Hilfe.

## **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.cs" >}}

## **Konsolenausgabe**

{{< highlight java >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
