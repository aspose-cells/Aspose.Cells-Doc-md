---
title: Filter in der Pivot-Tabelle löschen
type: docs
weight: 130
url: /de/java/clear-filter-in-pivot-table/
description: So löschen Sie PivotFilter aus dem spezifischen PivotField in der Pivot-Tabelle mit Aspose.Cells.
keywords: Clear PivotFilter in pivot table.
---
##  **Mögliche Nutzungsszenarien**
 Wenn Sie eine Pivot-Tabelle mit bekannten Daten erstellen und die Pivot-Tabelle filtern möchten, müssen Sie den Filter erlernen und verwenden. Es kann Ihnen dabei helfen, die gewünschten Daten effektiv herauszufiltern. Mithilfe von Aspose.Cells API können Sie Feldwerte in Pivot-Tabellen filtern.

##  **Filter in der Pivot-Tabelle in Excel löschen**
Um den Filter in der Pivot-Tabelle in Excel zu löschen, gehen Sie folgendermaßen vor:

1.  Wählen Sie die PivotTable aus, für die Sie den Filter löschen möchten.
2. Klicken Sie auf den Dropdown-Pfeil für den Filter, den Sie in der Pivot-Tabelle löschen möchten.
3. Wählen Sie „Filter löschen“ aus dem Dropdown-Menü.
<img src="1.png" width=80% />
4. Wenn Sie alle Filter aus der Pivot-Tabelle löschen möchten, können Sie auch auf der Registerkarte „PivotTable-Analyse“ im Menüband von Excel auf die Schaltfläche „Filter löschen“ klicken.
<img src="2.png" width=80% />

##  **Filter in der Pivot-Tabelle löschen**
 Bitte sehen Sie sich den folgenden Beispielcode an. Es legt die Daten fest und erstellt darauf basierend eine PivotTable. Fügen Sie dann einen Filter zum Zeilenfeld der Pivot-Tabelle hinzu. Schließlich wird die Arbeitsmappe gespeichert[Ausgabe XLSX](out_add.xlsx) Format. Nach der Ausführung des Beispielcodes wird dem Arbeitsblatt eine Pivot-Tabelle mit Top10-Filter hinzugefügt. Wenn wir nach dem Hinzufügen eines Filters ungefilterte Daten benötigen, können wir den Filter für ein bestimmtes Pivotfeld löschen. Nach der Ausführung des Codes zum Löschen des Filters wird der Filter für das jeweilige Pivotfeld gelöscht. Bitte überprüfen Sie die[Ausgabe XLSX](out_delete.xlsx).

##  **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-Clear-filter-in-PivotTable.java" >}}