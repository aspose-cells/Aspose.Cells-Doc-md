---
title: Extrahieren Sie Text aus der SmartArt Form des Zahnradtyps
type: docs
weight: 500
url: /de/net/extract-text-from-the-gear-type-smartart-shape/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells kann Text aus der SmartArt-Form des Zahnradtyps extrahieren. Dazu sollten Sie zuerst die SmartArt-Form in eine Gruppenform mit der Methode [**Shape.GetResultOfSmartArt()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/getresultofsmartart) konvertieren. Anschließend sollten Sie das Array aller Einzelformen, die die Gruppenform bilden, mit der Methode [**GroupShape.GetGroupedShapes()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape/methods/getgroupedshapes) abrufen. Schließlich können Sie alle Einzelformen nacheinander in einer Schleife durchlaufen und ihren Text mit der Eigenschaft [**Shape.Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) extrahieren.

## **Text aus dem SmartArt-Form 'Zahnräder' extrahieren**

Der folgende Beispielcode lädt die [Beispieldatei Excel](67338483.xlsx) mit der SmartArt-Form des Zahnradtyps. Anschließend werden die Texte aus den einzelnen Formen extrahiert, wie oben diskutiert. Bitte beachten Sie die Konsolenausgabe des folgenden Codes zur Referenz.

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.cs" >}}

## **Konsolenausgabe**

{{< highlight java >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
