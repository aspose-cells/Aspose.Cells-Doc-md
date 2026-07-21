---
title: Pivot Tabellen Ribbons mit Golang via C++ deaktivieren
linktitle: Pivot Tabellen Ribbons deaktivieren
type: docs
weight: 90
url: /de/go-cpp/disable-pivot-table-ribbons/
description: Lernen Sie, wie Sie die Bänder in Pivot Tabellen in Excel Dateien mit Aspose.Cells for C++ deaktivieren.
---

{{% alert color="primary" %}}

Berichte auf Basis von Pivot-Tabellen sind nützlich, aber anfällig für Fehler, wenn die Zielbenutzer kein detailliertes Excel-Wissen haben, um diese Berichte zu konfigurieren. In solchen Fällen möchten Organisationen die Benutzer daran hindern, Änderungen an Pivot-Tabellenberichten vorzunehmen. Funktionen wie zusätzliche Filter, Slicer, Felder oder die Änderung der Reihenfolge im Bericht sind meistens nicht für jeden Benutzer geeignet. Andererseits sollen diese Benutzer den Bericht aktualisieren und vorhandene Filter oder Slicer verwenden können. Aspose.Cells bietet Entwicklern die Möglichkeit, Benutzer beim Ändern dieser Berichte zu beschränken. Dafür stellt Excel eine Funktion zum Deaktivieren des Pivot-Tabellen-Bandes bereit, die auch von Aspose.Cells unterstützt wird. Entwickler können das Band mit den Steuerelementen zur Bearbeitung dieser Berichte deaktivieren.

{{% /alert %}}

## **Pivot-Tabelle-Ribbon mit PivotTable.EnableWizard deaktivieren**

Das folgende Beispiel demonstriert diese Funktion, indem es auf eine Pivot-Tabelle in einem Blatt zugreift und dann [**GetEnableWizard()**](https://reference.aspose.com/cells/go-cpp/pivottable/getenablewizard/) auf **false** setzt. Eine Beispiel-Pivot-Tabellendatei kann von [diesem Link](pivot_table_test.xlsx) heruntergeladen werden.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisablePivotTableRibbons.go" >}}
