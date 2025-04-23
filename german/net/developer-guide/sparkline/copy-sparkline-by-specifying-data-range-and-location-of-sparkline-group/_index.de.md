---
title: Sparkline kopieren durch Festlegen des Datenbereichs und des Speicherorts der Sparkline Gruppe
type: docs
weight: 300
url: /de/net/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
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

Aspose.Cells bietet die SparklineCollection.Add(dataRange, row, column)-Methode, um den Datenbereich und den Speicherort einer Sparkline-Gruppe anzugeben. Der folgende Beispielscode lädt die Quelldatei wie im obigen Screenshot gezeigt, greift dann auf die erste Sparkline-Gruppe zu und fügt Datenbereiche und Positionen in der Sparkline-Gruppe hinzu. Schließlich schreibt er die Ausgabedatei auf die Festplatte, die auch im obigen Screenshot gezeigt wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopySparkline-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
