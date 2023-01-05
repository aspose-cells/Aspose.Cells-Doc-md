---
title: Passen Sie die Globalisierungseinstellungen für die Pivot-Tabelle an
type: docs
weight: 50
url: /de/net/customize-globalization-settings-for-pivot-table/
---
## **Mögliche Nutzungsszenarien**

 Manchmal möchten Sie die anpassen*Pivot-Summe, Zwischensumme, Gesamtsumme, Alle Elemente, Mehrere Elemente, Spaltenbeschriftungen, Zeilenbeschriftungen, Leerwerte*Text nach Ihren Wünschen. Aspose.Cells können Sie die Globalisierungseinstellungen der Pivot-Tabelle anpassen, um mit solchen Szenarien fertig zu werden. Sie können diese Funktion auch verwenden, um die Beschriftungen in andere Sprachen wie Arabisch, Hindi, Polnisch usw. zu ändern.

## **Passen Sie die Globalisierungseinstellungen für die Pivot-Tabelle an**

 Der folgende Beispielcode erläutert, wie die Globalisierungseinstellungen für die Pivot-Tabelle angepasst werden. Es schafft eine Klasse*CustomPivotTableGlobalizationSettings* von einer Basisklasse abgeleitet[**Globalisierungseinstellungen**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) und überschreibt alle notwendigen Methoden. Diese Methoden geben den benutzerdefinierten Text für die zurück*Pivot-Summe, Zwischensumme, Gesamtsumme, Alle Elemente, Mehrere Elemente, Spaltenbeschriftungen, Zeilenbeschriftungen, Leerwerte*. Dann weist es das Objekt dieser Klasse zu[**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) Eigentum. Der Code lädt die[Excel-Quelldatei](40468488.xlsx) die die Pivot-Tabelle enthält, aktualisiert und berechnet ihre Daten und speichert sie als[Ausgang PDF](40468487.pdf)Datei. Der folgende Screenshot zeigt die Auswirkung des Beispielcodes auf die Ausgabe PDF. Wie Sie im Screenshot sehen können, haben verschiedene Teile der Pivot-Tabelle jetzt einen benutzerdefinierten Text, der von den überschriebenen Methoden von zurückgegeben wird[**Globalisierungseinstellungen**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)Klasse.

![todo: Bild_alt_Text](customize-globalization-settings-for-pivot-table_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CustomizePivotTableGlobalSettings-CustomizePivotTableGlobalSettings.cs" >}}
