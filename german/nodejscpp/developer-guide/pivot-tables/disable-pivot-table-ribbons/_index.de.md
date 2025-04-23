---
title: Pivot Tabellen Ribbons deaktivieren
type: docs
weight: 90
url: /de/nodejs-cpp/disable-pivot-table-ribbons/
description: Wie man Pivot Tabellen Ribbons mit Aspose.Cells for Node.js via C++ deaktiviert.
keywords: Aspose.Cells für Node.js Excel, Excel Node.js Bibliothek, Deaktivieren von Pivot Tabellen Ribbons mit Aspose.Cells for Node.js via C++ Excel Bibliothek.
---

{{% alert color="primary" %}}

Berichte auf Basis von Pivot-Tabellen sind nützlich, aber anfällig für Fehler, wenn Zielbenutzer nicht über detailliertes Excel-Wissen verfügen, um diese Berichte zu konfigurieren. In solchen Fällen möchten Organisationen möglicherweise die Benutzer daran hindern, einen Pivot-Tabellen-basierten Bericht zu ändern. Gängige Pivot-Tabellen-Funktionen wie das Hinzufügen zusätzlicher Filter, Slicer, Felder oder das Ändern der Reihenfolge bestimmter Elemente im Bericht sind meist nicht für jeden Benutzer geeignet. Andererseits sollen diese Benutzer auch in der Lage sein, den Bericht zu aktualisieren und bestehende Filter oder Slicer zu verwenden. Aspose.Cells for Node.js via C++ bietet Entwicklern diese Möglichkeit, Benutzer beim Ändern dieser Berichte zu beschränken, während sie diese Berichte erstellen. Zu diesem Zweck stellt Excel eine Funktion zum Deaktivieren des Pivot-Tabellen-Ribbons bereit, die auch von Aspose.Cells for Node.js via C++ bereitgestellt wird, d.h. der Entwickler kann das Ribbon deaktivieren, das Steuerungen zum Ändern dieser Berichte enthält.

{{% /alert %}}

## **Wie man das Pivot-Tabellen-Ribbon mit Aspose.Cells for Node.js via C++ deaktiviert**

Der folgende Code demonstriert diese Funktion, indem er auf eine Pivot-Tabelle aus einem Blatt zugreift und dann [**setEnableWizard**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setEnableWizard-boolean-) auf **false** setzt. Die Beispieldatei für die Pivot-Tabelle kann von diesem [Link](pivot_table_test.xlsx) heruntergeladen werden.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-DisablePivotTableRibbon.js" >}}
