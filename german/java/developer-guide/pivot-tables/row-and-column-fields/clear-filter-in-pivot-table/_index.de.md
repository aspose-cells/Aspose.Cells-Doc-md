---
title: Filter in Pivot Tabelle löschen
type: docs
weight: 130
url: /de/java/clear-filter-in-pivot-table/
description: Wie man PivotFilter aus dem spezifischen PivotField in der Pivot Tabelle mit Aspose.Cells löscht.
keywords: PivotFilter in Pivot Tabelle löschen.
---

## **Mögliche Verwendungsszenarien**
Wenn Sie eine Pivot-Tabelle mit bekannten Daten erstellen und die Pivot-Tabelle filtern möchten, müssen Sie Filter lernen und verwenden. Es kann Ihnen helfen, die Daten, die Sie effektiv filtern möchten, herauszufiltern. Mit der Aspose.Cells-API können Sie Filter auf Feldwerte in Pivot-Tabellen anwenden. 

## **Filter in Pivot-Tabelle in Excel löschen**
Filter in Pivot-Tabelle in Excel löschen, befolgen Sie diese Schritte:

1. Wählen Sie die Pivot-Tabelle aus, aus der Sie den Filter löschen möchten. 
2. Klicken Sie auf den Dropdown-Pfeil für den Filter, den Sie in der Pivot-Tabelle löschen möchten.
3. Wählen Sie "Filter löschen" aus dem Dropdown-Menü aus.
<img src="1.png" width=80% />
4. Wenn Sie alle Filter aus der Pivot-Tabelle löschen möchten, können Sie auch auf die Schaltfläche "Filter löschen" im PivotTable-Analyse-Tab im Menüband in Excel klicken.
<img src="2.png" width=80% />

## **Filter in Pivot-Tabelle löschen**
Bitte beachten Sie den folgenden Beispielcode. Er setzt die Daten und erstellt eine Pivot-Tabelle basierend darauf. Fügen Sie dann einen Filter auf das Zeilenfeld der Pivot-Tabelle hinzu. Schließlich speichert er die Arbeitsmappe im Format [Ausgabexlsx](out_add.xlsx). Nach Ausführung des Beispielscodes wird ein Pivot-Table mit Top10-Filter zum Arbeitsblatt hinzugefügt. Nach Hinzufügen eines Filters, wenn wir unverarbeitete Daten benötigen, können wir den Filter auf einem spezifischen Pivotfeld löschen. Nach Ausführung des Codes zum Löschen des Filters wird der Filter auf dem spezifischen Pivot-Feld gelöscht. Bitte überprüfen Sie das [Ausgabexlsx](out_delete.xlsx).

## **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-Clear-filter-in-PivotTable.java" >}}
