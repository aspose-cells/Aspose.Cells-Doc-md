---
title: Pivot Filter mit Golang via C++
linktitle: Pivot Filter
type: docs
weight: 130
url: /de/go-cpp/add-or-clear-pivot-filter/
description: Erfahren Sie, wie Sie in Pivot Tabellen mit Aspose.Cells und C++ einen Filter hinzufügen.
keywords: Hinzufügen eines Filters in einer Pivot Tabelle ohne Office 2013, Office 2016, Office 2019 und Office 365.
---

## **Mögliche Verwendungsszenarien**
Wenn Sie eine Pivot-Tabelle mit bekannten Daten erstellen und filtern möchten, lernen und verwenden Sie den Filter. Er kann Ihnen helfen, die gewünschten Daten effizient herauszufiltern. Mit der API von Aspose.Cells können Sie Filter auf Felder in Pivot-Tabellen hinzufügen und löschen. 

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
Bitte sehen Sie sich den folgenden Beispielcode an. Es legt die Daten fest und erstellt darauf basierend eine Pivot-Tabelle. Fügen Sie dann einen Filter im Zeilenfeld der Pivot-Tabelle hinzu. Schließlich speichert es die Arbeitsmappe im Format [output XLSX](filterout.xlsx). Nach Ausführung des Beispielcodes wird eine Pivot-Tabelle mit einem Top-10-Filter zum Arbeitsblatt hinzugefügt.

### **Beispielcode**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddFilterInPivotTable.go" >}}
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
Filter in Pivot-Tabelle löschen mit Aspose.Cells. Bitte beachten Sie den folgenden Beispielcode. 
1. Daten setzen und eine Pivot-Tabelle basierend darauf erstellen. 
2. Einen Filter auf das Zeilenfeld der Pivot-Tabelle hinzufügen. 
3. Die Arbeitsmappe im Format [output XLSX](out_add.xlsx) speichern. Nach Ausführung des Beispielcodes wird eine Pivot-Tabelle mit einem Top10-Filter zum Arbeitsblatt hinzugefügt. 
4. Den Filter auf einem bestimmten Pivot-Feld löschen. Nach Ausführung des Codes zum Löschen des Filters wird der Filter auf dem spezifischen Pivot-Feld gelöscht. Bitte prüfen Sie das [output XLSX](out_delete.xlsx).

### **Beispielcode**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddFilterInPivotTable-1.go" >}}
