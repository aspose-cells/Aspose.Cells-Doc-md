---
title: Passen Sie die Globalisierungseinstellungen für die Pivot-Tabelle an
type: docs
weight: 20
url: /de/java/customize-globalization-settings-for-pivot-table/
---
## **Mögliche Nutzungsszenarien**

 Manchmal möchten Sie die anpassen*Pivot-Summe, Zwischensumme, Gesamtsumme, Alle Elemente, Mehrere Elemente, Spaltenbeschriftungen, Zeilenbeschriftungen, Leerwerte*Text nach Ihren Wünschen. Aspose.Cells können Sie die Globalisierungseinstellungen der Pivot-Tabelle anpassen, um mit solchen Szenarien fertig zu werden. Sie können diese Funktion auch verwenden, um die Beschriftungen in andere Sprachen wie Arabisch, Hindi, Polnisch usw. zu ändern.

## **Passen Sie die Globalisierungseinstellungen für die Pivot-Tabelle an**

 Der folgende Beispielcode erläutert, wie die Globalisierungseinstellungen für die Pivot-Tabelle angepasst werden. Es schafft eine Klasse*CustomPivotTableGlobalizationSettings* von einer Basisklasse abgeleitet[**Globalisierungseinstellungen**](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings) und überschreibt alle notwendigen Methoden. Diese Methoden geben den benutzerdefinierten Text für die zurück*Pivot-Summe, Zwischensumme, Gesamtsumme, Alle Elemente, Mehrere Elemente, Spaltenbeschriftungen, Zeilenbeschriftungen, Leerwerte* . Dann weist es das Objekt dieser Klasse zu[**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) Eigentum. Der Code lädt die[Excel-Quelldatei](40468491.xlsx) die die Pivot-Tabelle enthält, aktualisiert und berechnet ihre Daten und speichert sie als[Ausgabedatei PDF](40468490.pdf) . Der folgende Screenshot zeigt die Auswirkung des Beispielcodes auf die Ausgabe PDF. Wie Sie im Screenshot sehen können, haben verschiedene Teile der Pivot-Tabelle jetzt einen benutzerdefinierten Text, der von den überschriebenen Methoden von zurückgegeben wird[**Globalisierungseinstellungen**](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings)Klasse.

![todo: Bild_alt_Text](customize-globalization-settings-for-pivot-table_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-CustomizeGlobalizationSettingsforPivotTable-1.java" >}}
