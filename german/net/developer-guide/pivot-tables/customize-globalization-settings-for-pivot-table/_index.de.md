---
title: Passen Sie die Globalisierungseinstellungen für die Pivot-Tabelle an
type: docs
weight: 50
url: /de/net/customize-globalization-settings-for-pivot-table/
---
##  **Mögliche Nutzungsszenarien**

 Manchmal möchten Sie das anpassen*Pivot-Summe, Zwischensumme, Gesamtsumme, Alle Elemente, Mehrere Elemente, Spaltenbeschriftungen, Zeilenbeschriftungen, leere Werte*Text nach Ihren Wünschen. Mit Aspose.Cells können Sie die Globalisierungseinstellungen der Pivot-Tabelle anpassen, um mit solchen Szenarien umzugehen. Sie können diese Funktion auch verwenden, um die Beschriftungen in andere Sprachen wie Arabisch, Hindi, Polnisch usw. zu ändern.

##  **Passen Sie die Globalisierungseinstellungen für die Pivot-Tabelle an**

Im folgenden Beispielcode wird erläutert, wie Sie die Globalisierungseinstellungen für die Pivot-Tabelle anpassen. Es erstellt eine Klasse*BenutzerdefiniertePivotTableGlobalizationSettings* abgeleitet von einer Basisklasse[**PivotGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.settings/pivotglobalizationsettings/)und überschreibt alle notwendigen Methoden. Diese Methoden geben den benutzerdefinierten Text für *Pivot-Gesamtsumme, Zwischensumme, Gesamtsumme, alle Elemente, mehrere Elemente, Spaltenbeschriftungen, Zeilenbeschriftungen und leere Werte* zurück. Dann weist es das Objekt dieser Klasse zu[**WorkbookSettings.GlobalizationSettings.PivotSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/pivotsettings/) Eigentum. Der Code lädt die[Quell-Excel-Datei](40468488.xlsx) das die Pivot-Tabelle enthält, aktualisiert und berechnet deren Daten und speichert sie unter[Ausgabe PDF](40468487.pdf) Datei. Der folgende Screenshot zeigt die Auswirkung des Beispielcodes auf die Ausgabe PDF. Wie Sie im Screenshot sehen können, verfügen verschiedene Teile der Pivot-Tabelle nun über einen benutzerdefinierten Text, der von den überschriebenen Methoden von zurückgegeben wird[**PivotGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.settings/pivotglobalizationsettings/)Klasse.

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

##  **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CustomizePivotTableGlobalSettings-CustomizePivotTableGlobalSettings.cs" >}}
