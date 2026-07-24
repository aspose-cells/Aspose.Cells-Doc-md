---
title: Pivot Filter
type: docs
weight: 130
url: /de/java/add-or-clear-pivot-filter/
description: Lernen Sie, wie Sie mit der Aspose.Cells Java Bibliothek einen Filter in das PivotTable hinzufügen.
keywords: Hinzufügen eines Filters in einer Pivot Tabelle ohne Office 2013, Office 2016, Office 2019 und Office 365.
---

## **Mögliche Verwendungsszenarien**
Wenn Sie ein PivotTable mit bekannten Daten erstellen und das PivotTable filtern möchten, müssen Sie Filter lernen und verwenden. Es kann Ihnen helfen, die Daten, die Sie effektiv filtern möchten, auszuwählen. Mit der Aspose.Cells Java-API können Sie Filter auf Feldwerte in Pivot-Tabellen hinzufügen. 

## **Filter in Pivot-Tabelle in Excel hinzufügen**
Filter in Pivot-Tabelle in Excel hinzufügen, folgen Sie diesen Schritten:

1. Wählen Sie die Pivot-Tabelle aus, aus der Sie den Filter löschen möchten. 
2. Klicken Sie auf den Dropdown-Pfeil für den Filter, den Sie in der Pivot-Tabelle hinzufügen möchten.
3. Wählen Sie "Top 10" aus dem Dropdown-Menü.
<br>
<img src="3.png" width=80% />
4. Legen Sie den Anzeigemodus und die Filteranzahl fest.
<br>
<img src="4.png" width=80% />

## **Filter in Pivot-Tabelle hinzufügen**
Bitte beachten Sie den folgenden Beispielcode. Es setzt die Daten und erstellt ein PivotTable basierend darauf. Fügt dann ein Filter auf das Zeilenfeld der Pivottabelle hinzu. Schließlich speichert es die Arbeitsmappe im [output XLSX](out.xlsx)-Format. Nach Ausführen des Beispielcodes wird ein PivotTable mit Top-10-Filter zum Arbeitsblatt hinzugefügt.

### **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-Add-filter-in-PivotTable.java" >}}


## **Filter in Pivot-Tabelle in Excel löschen**
Filter in Pivot-Tabelle in Excel löschen, befolgen Sie diese Schritte:

1. Wählen Sie die Pivot-Tabelle aus, aus der Sie den Filter löschen möchten. 
2. Klicken Sie auf den Dropdown-Pfeil für den Filter, den Sie in der Pivot-Tabelle löschen möchten.
3. Wählen Sie "Filter löschen" aus dem Dropdown-Menü aus.
<br>
<img src="1.png" width=80% />
4. Wenn Sie alle Filter aus der Pivot-Tabelle löschen möchten, können Sie auch auf die Schaltfläche "Filter löschen" im PivotTable-Analyse-Tab im Menüband in Excel klicken.
<br>
<img src="2.png" width=80% />

## **Filter in Pivot-Tabelle löschen**
Bitte beachten Sie den folgenden Beispielcode. Er setzt die Daten und erstellt eine Pivot-Tabelle basierend darauf. Fügen Sie dann einen Filter auf das Zeilenfeld der Pivot-Tabelle hinzu. Schließlich speichert er die Arbeitsmappe im Format [Ausgabexlsx](out_add.xlsx). Nach Ausführung des Beispielscodes wird ein Pivot-Table mit Top10-Filter zum Arbeitsblatt hinzugefügt. Nach Hinzufügen eines Filters, wenn wir unverarbeitete Daten benötigen, können wir den Filter auf einem spezifischen Pivotfeld löschen. Nach Ausführung des Codes zum Löschen des Filters wird der Filter auf dem spezifischen Pivot-Feld gelöscht. Bitte überprüfen Sie das [Ausgabexlsx](out_delete.xlsx).

### **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-Clear-filter-in-PivotTable.java" >}}
{{< app/cells/assistant language="java" >}}
