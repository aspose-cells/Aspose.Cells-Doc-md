---
title: Extrahieren Sie Text aus der SmartArt Form des Zahnradtyps
type: docs
weight: 500
url: /de/python-net/extract-text-from-the-gear-type-smartart-shape/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells kann Text aus der SmartArt-Form des Zahnradtyps extrahieren. Dazu sollten Sie zuerst die SmartArt-Form in eine Gruppenform mit der Methode [**Shape.get_result_of_smart_art()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/get_result_of_smart_art) konvertieren. Anschließend sollten Sie das Array aller Einzelformen, die die Gruppenform bilden, mit der Methode [**GroupShape.get_grouped_shapes()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupshape/get_grouped_shapes) abrufen. Schließlich können Sie alle Einzelformen nacheinander in einer Schleife durchlaufen und ihren Text mit der Eigenschaft [**Shape.text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) extrahieren.

## **Text aus dem SmartArt-Form 'Zahnräder' extrahieren**

Der folgende Beispielcode lädt die [Beispieldatei Excel](67338483.xlsx) mit der SmartArt-Form des Zahnradtyps. Anschließend werden die Texte aus den einzelnen Formen extrahiert, wie oben diskutiert. Bitte beachten Sie die Konsolenausgabe des folgenden Codes zur Referenz.

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-ExtractTextFromGearTypeSmartArtShape.py" >}}

## **Konsolenausgabe**

{{< highlight java >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
