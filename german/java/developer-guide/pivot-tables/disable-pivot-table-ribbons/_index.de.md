---
title: Pivot-Tabellen-Menübänder deaktivieren
type: docs
weight: 40
url: /de/java/disable-pivot-table-ribbons/
---
{{% alert color="primary" %}}

Auf Pivot-Tabellen basierende Berichte sind nützlich, aber fehleranfällig, wenn Zielbenutzer keine detaillierten Excel-Kenntnisse haben, um diese Berichte zu konfigurieren. Unter diesen Umständen möchten Organisationen verhindern, dass Benutzer einen Pivot-Tabellen-basierten Bericht ändern können. Übliche Pivot-Tabellenfunktionen wie das Hinzufügen zusätzlicher Filter, Datenschnitte, Felder oder das Ändern der Reihenfolge bestimmter Dinge im Bericht werden meist nicht für jeden Benutzer empfohlen. Andererseits sollen diese Benutzer auch in der Lage sein, den Bericht zu aktualisieren und vorhandene Filter oder Datenschnitte zu verwenden. Aspose.Cells hat Entwicklern diese Möglichkeit bereitgestellt, um Benutzer daran zu hindern, diese Berichte zu ändern, während sie diese Berichte erstellen. Zu diesem Zweck bietet Excel eine Funktion zum Deaktivieren des Menübands der Pivot-Tabelle, und dasselbe wird von Aspose.Cells bereitgestellt, dh Entwickler können das Menüband deaktivieren, das Steuerelemente zum Ändern dieser Berichte enthält.

{{% /alert %}}

## **Deaktivieren Sie das PivotTable-Menüband mit PivotTable.setEnableWizard**

Der folgende Code demonstriert diese Funktion, indem er von einem Blatt aus auf eine Pivot-Tabelle zugreift und dann die[**setEnableWizard**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#EnableWizard) um dieses Flag zu setzen**FALSCH** . Beispiel-Pivot-Tabellendatei kann hier heruntergeladen werden[Verknüpfung](71630876.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-DisablePivotTableRibbon-1.java" >}}
