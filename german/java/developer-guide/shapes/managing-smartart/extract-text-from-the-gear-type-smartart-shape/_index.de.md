---
title: Extrahieren Sie Text aus der SmartArt Form des Zahnradtyps
type: docs
weight: 130
url: /de/java/extract-text-from-the-gear-type-smartart-shape/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells kann Text aus der SmartArt-Form „Gear Type“ extrahieren. Hierzu sollten Sie zuerst die SmartArt-Form in eine Gruppenform mit der Methode [**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#getResultOfSmartArt--) konvertieren. Anschließend können Sie mit der Methode [**GroupShape.getGroupedShapes()**](https://reference.aspose.com/cells/java/com.aspose.cells/groupshape#getGroupedShapes--) das Array aller einzelnen Formen der Gruppenform abrufen. Schließlich können Sie alle einzelnen Formen nacheinander in einer Schleife durchlaufen und ihren Text mit der Eigenschaft [**Shape.Text**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Text) extrahieren.

## **Text aus dem SmartArt-Form 'Zahnräder' extrahieren**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](67338510.xlsx), die die „Gear Type“-SmartArt-Form enthält. Anschließend wird der Text aus ihren einzelnen Formen entsprechend extrahiert. Bitte beachten Sie die Konsolenausgabe des untenstehenden Beispielcodes als Referenz.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.java" >}}

## **Konsolenausgabe**

{{< highlight java >}}

Gear Type Shape Text: Nice Gear Type Shape Text: Good Gear Type Shape Text: Excellent

{{< /highlight >}}
