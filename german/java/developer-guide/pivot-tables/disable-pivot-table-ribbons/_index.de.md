---
title: Pivot Tabellen Ribbons deaktivieren
type: docs
weight: 40
url: /de/java/disable-pivot-table-ribbons/
---

{{% alert color="primary" %}}

Berichterstellung auf Basis von Pivot-Tabellen ist nützlich, aber anfällig für Fehler, wenn die Zielbenutzer nicht über ein detailliertes Wissen über Excel verfügen, um diese Berichte zu konfigurieren. In solchen Fällen wird die Organisation wollen, dass Benutzer davon abgehalten werden, einen Pivot-Tabellen-basierten Bericht zu ändern. Gängige Pivot-Tabellen-Funktionen wie das Hinzufügen zusätzlicher Filter, Slicer, Felder oder das Ändern der Reihenfolge bestimmter Dinge im Bericht werden in der Regel nicht für jeden Benutzer empfohlen. Andererseits sollen diese Benutzer auch in der Lage sein, den Bericht zu aktualisieren und vorhandene Filter oder Slicer zu verwenden. Aspose.Cells hat den Entwicklern diese Möglichkeit zur Verfügung gestellt, Benutzer daran zu hindern, diese Berichte zu ändern, während sie diese Berichte erstellen. Zu diesem Zweck bietet Excel eine Funktion zum Deaktivieren des Ribbon für Pivot-Tabellen, und dasselbe wird von Aspose.Cells bereitgestellt, d.h. der Entwickler kann das Ribbon deaktivieren, das Steuerelemente zur Änderung dieser Berichte enthält.

{{% /alert %}}

## **Deaktivieren des Pivot-Tabellenbands mithilfe von PivotTable.setEnableWizard**

Der folgende Code demonstriert diese Funktion, indem er auf eine Pivot-Tabelle von einem Blatt zugreift und dann den [**setEnableWizard**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#EnableWizard) aufruft, um dieses Flag auf **falsch** zu setzen. Die Beispieldatei der Pivot-Tabelle kann von diesem [Link](71630876.xlsx) heruntergeladen werden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-DisablePivotTableRibbon-1.java" >}}
