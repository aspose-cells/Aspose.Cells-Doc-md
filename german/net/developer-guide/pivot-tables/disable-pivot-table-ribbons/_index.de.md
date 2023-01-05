---
title: Pivot-Tabellen-Menübänder deaktivieren
type: docs
weight: 90
url: /de/net/disable-pivot-table-ribbons/
---
{{% alert color="primary" %}}

Auf Pivot-Tabellen basierende Berichte sind nützlich, aber fehleranfällig, wenn Zielbenutzer keine detaillierten Excel-Kenntnisse haben, um diese Berichte zu konfigurieren. Unter diesen Umständen möchten Organisationen verhindern, dass Benutzer einen Pivot-Tabellen-basierten Bericht ändern können. Übliche Pivot-Tabellenfunktionen wie das Hinzufügen zusätzlicher Filter, Datenschnitte, Felder oder das Ändern der Reihenfolge bestimmter Dinge im Bericht werden meist nicht für jeden Benutzer empfohlen. Andererseits sollen diese Benutzer auch in der Lage sein, den Bericht zu aktualisieren und vorhandene Filter oder Datenschnitte zu verwenden. Aspose.Cells hat Entwicklern diese Möglichkeit bereitgestellt, um Benutzer daran zu hindern, diese Berichte zu ändern, während sie diese Berichte erstellen. Zu diesem Zweck bietet Excel eine Funktion zum Deaktivieren des Menübands der Pivot-Tabelle, und dasselbe wird von Aspose.Cells bereitgestellt, dh Entwickler können das Menüband deaktivieren, das Steuerelemente zum Ändern dieser Berichte enthält.

{{% /alert %}}

## **Deaktivieren Sie das PivotTable-Menüband mit PivotTable.EnableWizard**

Der folgende Code demonstriert diese Funktion, indem er von einem Blatt auf eine Pivot-Tabelle zugreift und dann eine Einstellung vornimmt[**EnableWizard**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/enablewizard) zu**FALSCH** . Beispiel-Pivot-Tabellendatei kann hier heruntergeladen werden[Verknüpfung](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-DisablePivotTableRibbon.cs" >}}
