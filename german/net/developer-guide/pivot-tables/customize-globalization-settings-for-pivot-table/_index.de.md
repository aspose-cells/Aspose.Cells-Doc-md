---
title: Anpassen der Globalisierungseinstellungen für den Pivot Tabellen
type: docs
weight: 50
url: /de/net/customize-globalization-settings-for-pivot-table/
---

## **Mögliche Verwendungsszenarien**

Manchmal möchten Sie den *Pivot Total, Subtotal, Gesamtsumme, Alle Elemente, Mehrere Elemente, Spaltenbeschriftungen, Zeilenbeschriftungen, Leere Werte* Text entsprechend Ihren Anforderungen anpassen. Aspose.Cells ermöglicht es Ihnen, die Globalisierungseinstellungen der Pivot-Tabelle anzupassen, um mit solchen Szenarien umzugehen. Sie können diese Funktion auch verwenden, um die Beschriftungen in andere Sprachen wie Arabisch, Hindi, Polnisch usw. zu ändern.

## **Anpassen der Globalisierungseinstellungen für den Pivot-Tabellen**

Der folgende Beispielcode zeigt, wie Sie die Globalisierungseinstellungen für die Pivot-Tabelle anpassen können. Es erstellt eine Klasse *CustomPivotTableGlobalizationSettings*, die von einer Basisklasse [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.settings/pivotglobalizationsettings/) abgeleitet ist und alle erforderlichen Methoden überschreibt. Diese Methoden geben den angepassten Text für die *Pivot Total, Subtotal, Gesamtsumme, Alle Elemente, Mehrere Elemente, Spaltenbeschriftungen, Zeilenbeschriftungen, Leere Werte* zurück. Dann wird das Objekt dieser Klasse der Eigenschaft [**WorkbookSettings.GlobalizationSettings.PivotSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/pivotsettings/) zugewiesen. Der Code lädt die [Quelldatei Excel](40468488.xlsx), die die Pivot-Tabelle enthält, aktualisiert und berechnet ihre Daten und speichert sie als [Ausgabedatei PDF](40468487.pdf). Der folgende Screenshot zeigt die Auswirkung des Beispielcodes auf die Ausgabedatei PDF. Wie Sie im Screenshot sehen können, haben verschiedene Teile der Pivot-Tabelle jetzt einen angepassten Text, der von den überschriebenen Methoden der Klasse [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.settings/pivotglobalizationsettings/) zurückgegeben wird.

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CustomizePivotTableGlobalSettings-CustomizePivotTableGlobalSettings.cs" >}}
