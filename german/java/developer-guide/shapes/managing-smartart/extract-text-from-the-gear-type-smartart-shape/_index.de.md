---
title: Extrahieren Sie Text aus der SmartArt-Form vom Typ Zahnrad
type: docs
weight: 130
url: /de/java/extract-text-from-the-gear-type-smartart-shape/
---
## **Mögliche Nutzungsszenarien**

Aspose.Cells kann Text aus der Gear Type Smart Art Shape extrahieren. Um dies zu tun, sollten Sie zuerst Smart Art Shape mithilfe von in Group Shape umwandeln[**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#getResultOfSmartArt()) Methode. Dann sollten Sie das Array aller individuellen Formen erhalten, die die Gruppenform bilden, indem Sie die verwenden[**GroupShape.getGroupedShapes()**](https://reference.aspose.com/cells/java/com.aspose.cells/groupshape#getGroupedShapes()) Methode. Schließlich können Sie alle einzelnen Formen nacheinander in einer Schleife durchlaufen und ihren Text mithilfe von extrahieren[**Form.Text**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Text)Eigentum.

## **Extrahieren Sie Text aus der SmartArt-Form vom Typ Zahnrad**

Der folgende Beispielcode lädt die[Beispiel-Excel-Datei](67338510.xlsx)das Gear Type Smart Art Shape enthält. Dann extrahiert es den Text aus seinen einzelnen Formen, wie oben besprochen. Bitte sehen Sie sich die Konsolenausgabe des unten angegebenen Codes als Referenz an.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.java" >}}

## **Konsolenausgabe**

{{< highlight "java" >}}

Gear Type Shape Text: Nice Gear Type Shape Text: Good Gear Type Shape Text: Excellent

{{< /highlight >}}
