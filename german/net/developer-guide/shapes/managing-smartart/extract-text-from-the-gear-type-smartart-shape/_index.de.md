---
title: Extrahieren Sie Text aus der SmartArt-Form vom Typ Zahnrad
type: docs
weight: 500
url: /de/net/extract-text-from-the-gear-type-smartart-shape/
---
## **Mögliche Nutzungsszenarien**

 Aspose.Cells kann Text aus der Gear Type Smart Art Shape extrahieren. Um dies zu tun, sollten Sie zuerst Smart Art Shape mithilfe von in Group Shape umwandeln[**Shape.GetResultOfSmartArt()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/getresultofsmartart) Methode. Dann sollten Sie das Array aller individuellen Formen erhalten, die die Gruppenform bilden, indem Sie die verwenden[**GroupShape.GetGroupedShapes()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape/methods/getgroupedshapes) Methode. Schließlich können Sie alle einzelnen Formen nacheinander in einer Schleife durchlaufen und ihren Text mithilfe von extrahieren[**Form.Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)Eigentum.

## **Extrahieren Sie Text aus der SmartArt-Form vom Typ Zahnrad**

 Der folgende Beispielcode lädt die[Beispiel-Excel-Datei](67338483.xlsx) das Gear Type Smart Art Shape enthält. Dann extrahiert es den Text aus seinen einzelnen Formen, wie oben besprochen. Bitte sehen Sie sich die Konsolenausgabe des unten angegebenen Codes als Referenz an.

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.cs" >}}

## **Konsolenausgabe**

{{< highlight "java" >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
