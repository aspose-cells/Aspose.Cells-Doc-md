---
title: Pivot Verbindung entfernen
type: docs
weight: 30
url: /de/java/remove-pivot-connection/
description: Erfahren Sie, wie Sie die Pivot Verbindung mit der Aspose.Cells Java Bibliothek entfernen können.
keywords: Entfernen Sie die Pivot Verbindung ohne Office 2013, Office 2016, Office 2019 und Office 365.
---

## **Mögliche Verwendungsszenarien**

Wenn Sie den Slicer und die Pivot-Tabelle in Excel trennen möchten, müssen Sie mit der rechten Maustaste auf den Slicer klicken und das Element "Berichtsverbindungen..." auswählen. In der Optionsliste können Sie das Kontrollkästchen bedienen. Ebenso, wenn Sie den Slicer und die Pivot-Tabelle mithilfe der Aspose.Cells-API programmgesteuert trennen möchten, verwenden Sie bitte die Methode [**Slicer.removePivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#removePivotConnection-com.aspose.cells.PivotTable-). Es wird den Slicer und die Pivot-Tabelle trennen.

## **Slicer entfernen**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](remove-pivot-connection.xlsx), die einen vorhandenen Slicer enthält. Es greift auf die Slicer zu und entkoppelt dann den Slicer und die Pivot-Tabelle. Schließlich speichert er die Arbeitsmappe als [Ausgabe-Excel-Datei](remove-pivot-connection-out.xlsx). 


## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-Removing-Pivot-Connection.java" >}}
{{< app/cells/assistant language="java" >}}
