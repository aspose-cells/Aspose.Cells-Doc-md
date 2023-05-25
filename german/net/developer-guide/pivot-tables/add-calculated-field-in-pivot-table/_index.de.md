---
title: Berechnetes Feld zur Pivot-Tabelle hinzufügen
type: docs
weight: 130
url: /de/net/add-calculated-field-in-pivot-table/
description: So fügen Sie ein berechnetes Feld in der Pivot-Tabelle mit Aspose.Cells hinzu.
keywords: Adding a calculated field in pivot table.
---
##  **Mögliche Nutzungsszenarien**
 Wenn Sie eine Pivot-Tabelle auf der Grundlage bekannter Daten erstellen, stellen Sie fest, dass die darin enthaltenen Daten nicht Ihren Wünschen entsprechen. Die gewünschten Daten sind die Kombination dieser Originaldaten. Beispielsweise müssen Sie die Originaldaten addieren, subtrahieren, multiplizieren und dividieren, bevor Sie die Daten benötigen. Zu diesem Zeitpunkt müssen Sie ein berechnetes Feld erstellen und die entsprechende Berechnungsformel festlegen. Führen Sie dann einige Statistiken und andere Operationen für das berechnete Feld durch.

##  **Berechnetes Feld zur Pivot-Tabelle in Excel hinzufügen**
Führen Sie die folgenden Schritte aus, um ein berechnetes Feld in eine PivotTable in Excel einzufügen:

1.  Wählen Sie die PivotTable aus, zu der Sie ein berechnetes Feld hinzufügen möchten.
2. Gehen Sie im Menüband zur Registerkarte „PivotTable-Analyse“.
3. Klicken Sie auf „Felder, Elemente und Sätze“ und wählen Sie dann „Berechnetes Feld“ aus dem Dropdown-Menü aus.
4. Geben Sie im Feld „Name“ einen Namen für das berechnete Feld ein.
 5. Geben Sie im Feld „Formel“ die Formel für die Berechnung ein, die Sie durchführen möchten, indem Sie die entsprechenden PivotTable-Feldnamen und mathematischen Operatoren verwenden.
<br>
<img src="1.png" width=80% />
6. Klicken Sie auf „OK“, um das berechnete Feld zu erstellen.
7. Das neue berechnete Feld wird in der PivotTable-Feldliste im Abschnitt „Werte“ angezeigt.
8. Ziehen Sie das berechnete Feld in den Abschnitt „Werte“ der PivotTable, um die berechneten Werte anzuzeigen.
<br>
<img src="2.png" width=80% />

##  **Fügen Sie ein berechnetes Feld in der Pivot-Tabelle mit C# hinzu**
Fügen Sie ein berechnetes Feld mit Aspose.Cells zur Excel-Datei hinzu. Sehen Sie sich bitte den folgenden Beispielcode an. Nach der Ausführung des Beispielcodes wird dem Arbeitsblatt eine Pivot-Tabelle mit berechnetem Feld hinzugefügt.
1.  Legen Sie die Originaldaten fest und erstellen Sie eine Pivot-Tabelle.
2. Erstellen Sie das berechnete Feld entsprechend dem vorhandenen PivotField in der Pivot-Tabelle.
 3. Fügen Sie das berechnete Feld zum Datenbereich hinzu.
 4. Abschließend wird die Arbeitsmappe gespeichert[Ausgabe XLSX](out.xlsx) Format.

##  **Beispielcode**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-Add-calculated-field-in-PivotTable.cs" >}}
