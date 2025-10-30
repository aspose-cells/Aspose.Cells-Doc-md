---
title: Globalisierungs Einstellungen für Pivot Tabelle mit Golang via C++ anpassen
linktitle: Anpassen der Globalisierungseinstellungen für den Pivot Tabellen
type: docs
weight: 50
url: /de/go-cpp/customize-globalization-settings-for-pivot-table/
description: Lernen Sie, wie man die Globalisierungseinstellungen der Pivot Tabelle mit Aspose.Cells for C++ anpasst.
---

## **Mögliche Verwendungsszenarien**

Manchmal möchten Sie den Text *Pivot Total, Sub Total, Grand Total, All Items, Multiple Items, Column Labels, Row Labels, Blank Values* nach Ihren Anforderungen anpassen. Aspose.Cells for C++ ermöglicht es Ihnen, die Globalisierungseinstellungen der Pivot-Tabelle für solche Szenarien zu konfigurieren. Mit dieser Funktion können Sie auch die Labels in andere Sprachen wie Arabisch, Hindi, Polnisch usw. ändern.

## **Anpassen der Globalisierungseinstellungen für den Pivot-Tabellen**

Der folgende Beispielcode erklärt, wie man die Globalisierungseinstellungen für die Pivot-Tabelle in C++ anpasst. Er erstellt eine Klasse *CustomPivotTableGlobalizationSettings*, die von der Basisklasse [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/pivotglobalizationsettings/) abgeleitet ist und alle notwendigen Methoden überschreibt. Diese Methoden geben angepassten Text für verschiedene Elemente der Pivot-Tabelle zurück. Anschließend weist der Code diese Implementierung der [**WorkbookSettings.GetPivotSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getpivotsettings/)-Eigenschaft zu. Das Beispiel lädt eine [Quelldatei](40468488.xlsx), aktualisiert die Pivot-Daten und speichert sie als [Ausgabepdf](40468487.pdf). Das unten stehende Bild zeigt die angepassten Labels im Output.

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CustomizeGlobalizationSettingsForPivotTable.go" >}}
