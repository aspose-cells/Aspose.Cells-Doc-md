---
title: Anpassen der Globalisierungseinstellungen für den Pivot Tabellen
type: docs
weight: 20
url: /de/java/customize-globalization-settings-for-pivot-table/
---

## **Mögliche Verwendungsszenarien**

Manchmal möchten Sie den *Pivot Total, Subtotal, Gesamtsumme, Alle Elemente, Mehrere Elemente, Spaltenbeschriftungen, Zeilenbeschriftungen, Leere Werte* Text entsprechend Ihren Anforderungen anpassen. Aspose.Cells ermöglicht es Ihnen, die Globalisierungseinstellungen der Pivot-Tabelle anzupassen, um mit solchen Szenarien umzugehen. Sie können diese Funktion auch verwenden, um die Beschriftungen in andere Sprachen wie Arabisch, Hindi, Polnisch usw. zu ändern.

## **Anpassen der Globalisierungseinstellungen für den Pivot-Tabellen**

Der folgende Beispielcode erklärt, wie die Globalisierungseinstellungen für die Pivot-Tabelle angepasst werden. Es erstellt eine Klasse *CustomPivotTableGlobalizationSettings*, die von einer Basisklasse [**GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings) abgeleitet ist und alle erforderlichen Methoden überschreibt. Diese Methoden geben den angepassten Text für *Pivot Total, Sub Total, Grand Total, All Items, Multiple Items, Column Labels, Row Labels, Blank Values* zurück. Dann wird das Objekt dieser Klasse der Eigenschaft [**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) zugewiesen. Der Code lädt die [Quelldatei Excel](40468491.xlsx) mit der Pivot-Tabelle, aktualisiert und berechnet ihre Daten und speichert sie als [Ausgabedatei PDF](40468490.pdf). Der folgende Screenshot zeigt die Auswirkung des Beispielcodes auf die Ausgabedatei PDF. Wie im Screenshot zu sehen ist, haben verschiedene Teile der Pivot-Tabelle jetzt einen angepassten Text, der von den überschriebenen Methoden der Klasse [**GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings) zurückgegeben wird.

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-CustomizeGlobalizationSettingsforPivotTable-1.java" >}}
{{< app/cells/assistant language="java" >}}
