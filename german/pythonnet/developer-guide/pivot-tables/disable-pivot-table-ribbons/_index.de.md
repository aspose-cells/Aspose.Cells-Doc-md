---
title: Deaktivieren Sie die Pivot-Tabellen-Menübänder
type: docs
weight: 90
url: /de/python-net/disable-pivot-table-ribbons/
description: So deaktivieren Sie Pivot-Table-Menübänder mit Aspose.Cells for Python via .NET.
keywords: Disable Pivot Table Ribbons.
---
{{% alert color="primary" %}}

Auf Pivot-Tabellen basierende Berichte sind nützlich, aber fehleranfällig, wenn Zielbenutzer nicht über detaillierte Excel-Kenntnisse verfügen, um diese Berichte zu konfigurieren. Unter diesen Umständen möchten Organisationen verhindern, dass Benutzer einen auf einer Pivot-Tabelle basierenden Bericht ändern können. Gängige Pivot-Tabellenfunktionen wie das Hinzufügen zusätzlicher Filter, Slicer, Felder oder das Ändern der Reihenfolge bestimmter Dinge im Bericht werden meist nicht jedem Benutzer empfohlen. Andererseits sollen diese Benutzer auch die Möglichkeit haben, den Bericht zu aktualisieren und vorhandene Filter oder Slicer zu verwenden. Aspose.Cells for Python via .NET bietet Entwicklern diese Möglichkeit, um Benutzer daran zu hindern, diese Berichte während der Erstellung dieser Berichte zu ändern. Zu diesem Zweck bietet Excel eine Funktion zum Deaktivieren des Pivot-Tabellen-Menübands und das Gleiche wird von Aspose.Cells for Python via .NET bereitgestellt, dh Entwickler können das Menüband deaktivieren, das Steuerelemente zum Ändern dieser Berichte enthält.

{{% /alert %}}

##  **Deaktivieren Sie das Pivot-Table-Menüband mit PivotTable.EnableWizard**

 Der folgende Code demonstriert diese Funktion, indem er von einem Blatt aus auf eine Pivot-Tabelle zugreift und diese dann festlegt[**enable_wizard**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/enable_wizard/) auf *falsch**. Eine Beispiel-Pivot-Tabellendatei kann hier heruntergeladen werden[Verknüpfung](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-DisablePivotTableRibbon.py" >}}
