---
title: Erstellen Sie ein berechnetes Feld im Pivot Table
type: docs
weight: 130
url: /de/java/add-calculated-field-in-pivot-table/
description: Wie man ein berechnetes Feld in einem Pivot Table mit Aspose.Cells hinzufügt.
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
5. Geben Sie im Feld "Formel" die Formel ein, die Sie unter Verwendung der entsprechenden Feldnamen des PivotTables und mathematischer Operatoren ausführen möchten. 
<br>
<img src="1.png" width=80% />
6. Klicken Sie auf "OK", um das berechnete Feld zu erstellen.
7. Das neue berechnete Feld wird im Bereich Wertliste der Pivot-Tabelle unter den Werten angezeigt.
8. Ziehen Sie das berechnete Feld in den Wertebereich der Pivot-Tabelle, um die berechneten Werte anzuzeigen.
<br>
<img src="2.png" width=80% />

## **Berechnetes Feld im PivotTable hinzufügen**
Bitte beachten Sie den folgenden Beispielcode. Der Code setzt zunächst die ursprünglichen Daten und erstellt ein PivotTable. Erstellt dann das berechnete Feld entsprechend dem vorhandenen PivotField in der Pivottabelle und fügt das berechnete Feld dem Datenbereich hinzu. Schließlich speichert es die Arbeitsmappe im [output XLSX](out.xlsx)-Format. Nach Ausführen des Beispielcodes wird ein PivotTable mit berechnetem Feld zum Arbeitsblatt hinzugefügt.

## **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-Add-calculated-field-in-PivotTable.java" >}}
{{< app/cells/assistant language="java" >}}
