---
title: Pivot Tabellen Ribbons deaktivieren
type: docs
weight: 90
url: /de/net/disable-pivot-table-ribbons/
---

{{% alert color="primary" %}}

Berichterstellung auf Basis von Pivot-Tabellen ist nützlich, aber anfällig für Fehler, wenn die Zielbenutzer nicht über ein detailliertes Wissen über Excel verfügen, um diese Berichte zu konfigurieren. In solchen Fällen wird die Organisation wollen, dass Benutzer davon abgehalten werden, einen Pivot-Tabellen-basierten Bericht zu ändern. Gängige Pivot-Tabellen-Funktionen wie das Hinzufügen zusätzlicher Filter, Slicer, Felder oder das Ändern der Reihenfolge bestimmter Dinge im Bericht werden in der Regel nicht für jeden Benutzer empfohlen. Andererseits sollen diese Benutzer auch in der Lage sein, den Bericht zu aktualisieren und vorhandene Filter oder Slicer zu verwenden. Aspose.Cells hat den Entwicklern diese Möglichkeit zur Verfügung gestellt, Benutzer daran zu hindern, diese Berichte zu ändern, während sie diese Berichte erstellen. Zu diesem Zweck bietet Excel eine Funktion zum Deaktivieren des Ribbon für Pivot-Tabellen, und dasselbe wird von Aspose.Cells bereitgestellt, d.h. der Entwickler kann das Ribbon deaktivieren, das Steuerelemente zur Änderung dieser Berichte enthält.

{{% /alert %}}

## **Pivot-Tabelle-Ribbon mit PivotTable.EnableWizard deaktivieren**

Der folgende Code demonstriert diese Funktion, indem er auf eine Pivot-Tabelle aus einem Blatt zugreift und dann [**EnableWizard**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/enablewizard) auf **false** setzt. Die Beispieldatei für die Pivot-Tabelle kann von diesem [Link](pivot_table_test.xlsx) heruntergeladen werden.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-DisablePivotTableRibbon.cs" >}}
