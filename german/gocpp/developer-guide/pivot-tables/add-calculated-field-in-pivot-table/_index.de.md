---
title: Berechnetes Feld in PivotTable mit Golang via C++ hinzufügen
linktitle: Erstellen Sie ein berechnetes Feld im Pivot Table
type: docs
weight: 130
url: /de/go-cpp/add-calculated-field-in-pivot-table/
description: Wie man ein berechnetes Feld in Pivot Tabelle mit Aspose.Cells for C++ hinzufügt.
keywords: Hinzufügen eines berechneten Felds im Pivot Table.
---

## **Mögliche Verwendungsszenarien**
Wenn Sie eine Pivot-Tabelle basierend auf bekannten Daten erstellen, stellen Sie fest, dass die Daten darin nicht das sind, was Sie wollen. Die Daten, die Sie wollen, sind die Kombination dieser Originaldaten. Zum Beispiel müssen Sie die ursprünglichen Daten addieren, subtrahieren, multiplizieren und dividieren, bevor Sie die Daten wollen. Zu diesem Zeitpunkt müssen Sie ein berechnetes Feld erstellen und die entsprechende Formel für die Berechnung festlegen. Führen Sie dann einige Statistiken und andere Operationen auf dem berechneten Feld durch. 

## **Füge ein berechnetes Feld in eine Pivot-Tabelle in Excel ein**
Fügen Sie ein berechnetes Feld in eine Pivot-Tabelle in Excel ein, befolgen Sie diese Schritte:

1. Wählen Sie die Pivot-Tabelle aus, zu der Sie ein berechnetes Feld hinzufügen möchten. 
2. Gehen Sie zum Register PivotTable Analyse in der Menüleiste.
3. Klicken Sie auf "Felder, Elemente und Sets" und wählen Sie dann "Berechnetes Feld" im Dropdown-Menü aus.
4. Geben Sie im Feld "Name" einen Namen für das berechnete Feld ein.
5. Geben Sie im Feld "Formel" die Formel für die Berechnung ein, die Sie unter Verwendung der entsprechenden Feldnamen und mathematischen Operatoren in der Pivot-Tabelle durchführen möchten. 
<br>
<img src="1.png" width=80% />
6. Klicken Sie auf "OK", um das berechnete Feld zu erstellen.
7. Das neue berechnete Feld wird im Bereich Wertliste der Pivot-Tabelle unter den Werten angezeigt.
8. Ziehen Sie das berechnete Feld in den Wertebereich der Pivot-Tabelle, um die berechneten Werte anzuzeigen.
<br>
<img src="2.png" width=80% />

## **Berechnetes Feld in Pivot-Tabelle mit C++ hinzufügen**
Fügen Sie ein berechnetes Feld zu einer Excel-Datei mit Aspose.Cells hinzu. Bitte beachten Sie den folgenden Beispielcode. Nach Ausführung des Beispielcodes wird eine Pivot-Tabelle mit einem berechneten Feld zum Arbeitsblatt hinzugefügt.
1. Legen Sie die Originaldaten fest und erstellen Sie eine Pivot-Tabelle. 
2. Erstellen Sie das berechnete Feld gemäß dem vorhandenen PivotField in der Pivot-Tabelle.
3. Fügen Sie das berechnete Feld in den Datenbereich ein. 
4. Schließlich wird die Arbeitsmappe im [XLSX-Ausgabeformat](out.xlsx) gespeichert. 

## **Beispielcode**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddCalculatedFieldInPivotTable.go" >}}
