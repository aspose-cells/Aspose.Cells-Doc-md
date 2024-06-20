---
title: Pivot Verbindung hinzufügen
type: docs
weight: 30
url: /de/java/add-pivot-connection/
description: Erfahren Sie, wie Sie eine Pivot Verbindung mit der Aspose.Cells Java Bibliothek hinzufügen.
keywords: Pivot Verbindung hinzufügen ohne Office 2013, Office 2016, Office 2019 und Office 365.
---

## **Mögliche Verwendungsszenarien**

Wenn Sie in Excel einen Slicer und einen Pivot-Table verknüpfen möchten, müssen Sie mit der rechten Maustaste auf den Slicer klicken und den Punkt "Berichtsverbindungen..." auswählen. In der Optionsliste können Sie das Kontrollkästchen bedienen. Ebenso, wenn Sie Slicer und Pivot-Table mit dem Aspose.Cells Java-API programmgesteuert verknüpfen möchten, verwenden Sie bitte die Methode [**Slicer.addPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#addPivotConnection(com.aspose.cells.PivotTable)/). Sie wird Slicer und Pivot-Table verknüpfen.

## **Slicer und PivotTable verknüpfen**

Der folgende Beispielcode lädt die [Beispieldatei](add-pivot-connection.xlsx), die bereits einen Slicer enthält. Er greift auf den Slicer zu und verknüpft dann den Slicer und die Pivot-Tabelle. Schließlich speichert er die Arbeitsmappe als [Ausgabe-Excel-Datei](add-pivot-connection-out.xlsx). 


## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-Adding-Pivot-Connection.java" >}}
