---
title: Pivot Verbindung mit Golang über C++ hinzufügen
linktitle: Pivot Verbindung hinzufügen
type: docs
weight: 30
url: /de/go-cpp/add-pivot-connection/
description: Erfahren Sie, wie Sie eine Pivot Verbindung mit der Aspose.Cells Bibliothek in C++ hinzufügen.
keywords: Pivot Verbindung hinzufügen ohne Office 2013, Office 2016, Office 2019 und Office 365.
---

## **Mögliche Verwendungsszenarien**

Wenn Sie Slicer und Pivot-Tabelle in Excel verknüpfen möchten, müssen Sie mit einem Rechtsklick auf den Slicer die Option "Berichtsverbindungen..." auswählen. In der Optionsliste können Sie die Kontrollkästchen verwenden. Ebenso, wenn Sie Slicer und Pivot-Tabelle programmgesteuert mit der Aspose.Cells-API verknüpfen möchten, verwenden Sie bitte die [**Slicer.AddPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/go-cpp/slicer/addpivotconnection/)-Methode. Damit können Sie Slicer und Pivot-Tabelle verknüpfen.

## **Slicer und PivotTable verknüpfen**

Der folgende Beispielcode lädt die [Beispieldatei](add-pivot-connection.xlsx), die bereits einen Slicer enthält. Er greift auf den Slicer zu und verknüpft dann den Slicer und die Pivot-Tabelle. Schließlich speichert er die Arbeitsmappe als [Ausgabe-Excel-Datei](add-pivot-connection-out.xlsx). 

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddPivotConnection.go" >}}
