---
title: Sparkline kopieren, indem Datenbereich und Standort der Sparkline Gruppe mit Golang via C++ angegeben werden
linktitle: Kopieren Sie Sparkline durch Festlegen des Datenbereichs und des Standorts
type: docs
weight: 300
url: /de/go-cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
description: Erfahren Sie, wie Sie Sparklines durch Festlegen des Datenbereichs und des Standorts mit Aspose.Cells for C++ kopieren.
---

{{% alert color="primary" %}}

Microsoft Excel ermöglicht es Ihnen, eine Sparkline zu kopieren, indem Sie den Datenbereich und den Speicherort einer Sparkline-Gruppe angeben. Aspose.Cells unterstützt diese Funktion.

{{% /alert %}}

Um eine Sparkline in andere Zellen in Microsoft Excel zu kopieren:

1. Wählen Sie die Zelle aus, die die Sparkline enthält.
1. Wählen Sie **Daten bearbeiten** im **Sparkline**-Abschnitt des **Entwurfs**-Registers aus.
1. Wählen Sie **Gruppenposition & Daten bearbeiten** aus.
1. Geben Sie den Datenbereich und den Speicherort an.
1. Klicken Sie auf **OK**.

Aspose.Cells bietet die Methode `SparklineCollection.Add(dataRange, Zeile, Spalte)`, um den Datenbereich und den Standort einer Sparkline-Gruppe festzulegen. Der folgende Beispielcode lädt die Quellen-Excel-Datei, wie im obigen Screenshot gezeigt, greift auf die erste Sparkline-Gruppe zu und fügt Datenbereiche und Standorte in die Sparkline-Gruppe ein. Abschließend wird die Ausgabedatei auf die Festplatte geschrieben, die ebenfalls im obigen Screenshot zu sehen ist.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopySparklineBySpecifyingDataRangeAndLocationOfSparklineGroup.go" >}}
