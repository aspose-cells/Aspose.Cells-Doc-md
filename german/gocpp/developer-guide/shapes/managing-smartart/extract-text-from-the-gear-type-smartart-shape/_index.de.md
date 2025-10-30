---
title: Text aus der Gear Type SmartArt Form mit Golang über C++ extrahieren
linktitle: Extrahieren Sie Text aus der SmartArt Form des Zahnradtyps
type: docs
weight: 500
url: /de/go-cpp/extract-text-from-the-gear-type-smartart-shape/
description: Erfahren Sie, wie Sie mit Aspose.Cells for C++ Text aus SmartArt Shapes vom Getriebetyp in Excel extrahieren, inklusive Schritt für Schritt Anleitung und Codebeispielen.
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells for C++ kann Text aus SmartArt Shape vom Getriebetyp extrahieren. Folgen Sie dazu diesen Schritten:
1. Konvertieren Sie SmartArt Shape mit der Methode [**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/go-cpp/) in eine Gruppierungsform.
2. Rufen Sie alle einzelnen Formen ab, die die Gruppierungsform bilden, mit der Methode [**GroupShape::GetGroupedShapes()**](https://reference.aspose.com/cells/go-cpp/).
3. Durchlaufen Sie jede einzelne Form und extrahieren Sie Text mit der Methode [**GetText()**](https://reference.aspose.com/cells/go-cpp/).

## **Text aus dem SmartArt-Form 'Zahnräder' extrahieren**

Der folgende Beispielcode lädt eine [Beispieldatei Excel](67338483.xlsx), die eine Smart Art Shape vom Getriebetyp enthält, und extrahiert Text aus ihren einzelnen Formen. Die Ergebnisse sind in der untenstehenden Konsolenausgabe ersichtlich.

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExtractTextFromTheGearTypeSmartartShape.go" >}}
## **Konsolenausgabe**

{{< highlight java >}}
Gear Type Shape Text: Nice
Gear Type Shape Text: Good
Gear Type Shape Text: Excellent
{{< /highlight >}}
