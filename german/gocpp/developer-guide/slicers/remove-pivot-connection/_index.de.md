---
title: Pivot Verbindung mit Golang über C++ entfernen
linktitle: Pivot Verbindung entfernen
type: docs
weight: 30
url: /de/go-cpp/remove-pivot-connection/
description: Erfahren Sie, wie Sie die Pivot Verbindung mit der Aspose.Cells Bibliothek in C++ entfernen.
keywords: Entfernen Sie die Pivot Verbindung ohne Office 2013, Office 2016, Office 2019 und Office 365.
---

## **Mögliche Verwendungsszenarien**

Wenn Sie den Slicer und die Pivot-Tabelle in Excel trennen möchten, müssen Sie mit der rechten Maustaste auf den Slicer klicken und das Element "Berichtsverbindungen..." auswählen. In der Optionsliste können Sie das Kontrollkästchen bedienen. Ebenso, wenn Sie den Slicer und die Pivot-Tabelle mithilfe der Aspose.Cells-API programmgesteuert trennen möchten, verwenden Sie bitte die Methode [**Slicer.RemovePivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/go-cpp/slicer/removepivotconnection/). Es wird den Slicer und die Pivot-Tabelle trennen.

## **Slicer und Pivot-Tabelle dissoziieren**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](remove-pivot-connection.xlsx), die einen vorhandenen Slicer enthält. Es greift auf die Slicer zu und entkoppelt dann den Slicer und die Pivot-Tabelle. Schließlich speichert er die Arbeitsmappe als [Ausgabe-Excel-Datei](remove-pivot-connection-out.xlsx). 

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemovePivotConnection.go" >}}
