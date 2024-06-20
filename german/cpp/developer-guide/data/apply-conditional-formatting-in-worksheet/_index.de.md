---
title: Bedingte Formatierung im Arbeitsblatt anwenden
type: docs
weight: 40
url: /de/cpp/apply-conditional-formatting-in-worksheet/
---

## **Mögliche Anwendungsszenarien**
Aspose.Cells ermöglicht es Ihnen, alle Arten von bedingter Formatierung wie Formel, Über Durchschnitt, Farbskala, Datenleiste, Symbolset, Top 10 usw. hinzuzufügen. Es stellt die Klasse [FormatCondition](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/) zur Verfügung, die alle notwendigen Methoden zum Anwenden der gewünschten bedingten Formatierung enthält. Hier ist eine Liste einiger Get-Methoden.

- [GetAboveAverage()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getaboveaverage/)
- [GetColorScale()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getcolorscale)
- [GetDataBar()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getdatabar)
- [GetIconSet()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/geticonset)
- [GetTop10()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/gettop10)
## **Bedingte Formatierung auf Arbeitsblatt anwenden**
Der folgende Beispielcode zeigt, wie eine bedingte Formatierung des Zellwerts in den Zellen A1 und B2 hinzugefügt werden kann. Bitte beachten Sie die durch den Code generierte [Ausgabedatei](23167004.xlsx) und den folgenden Screenshot, der die Wirkung des Codes auf die [Ausgabedatei](23167004.xlsx) erläutert. Wenn Sie einen Wert in Zelle A2 und B2 eingeben, der größer als 100 ist, wird die rote Füllfarbe in Zelle A1 und B2 verschwinden.

![todo:image_alt_text](apply-conditional-formatting-in-worksheet_1.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ApplyConditionalFormattingInWorksheet-new.cpp" >}}
