---
title: Kopieren Sie die Sparkline, indem Sie den Datenbereich und den Speicherort der Sparkline-Gruppe angeben
type: docs
weight: 300
url: /de/net/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---
{{% alert color="primary" %}}

Microsoft Mit Excel können Sie eine Sparkline kopieren, indem Sie den Datenbereich und die Position einer Sparkline-Gruppe angeben. Aspose.Cells unterstützt diese Funktion.

{{% /alert %}}

So kopieren Sie eine Sparkline in andere Zellen in Microsoft Excel:

1. Wählen Sie die Zelle mit der Sparkline aus.
1.  Wählen**Daten bearbeiten** von dem**Sparkline** Abschnitt der**Design** Tab.
1.  Wählen**Standort und Daten der Gruppe bearbeiten**.
1. Geben Sie den Datenbereich und den Speicherort an.
1.  Klicken**OK**.

Aspose.Cells stellt die SparklineCollection.Add(dataRange, row, column)-Methode bereit, um den Datenbereich und die Position einer Sparkline-Gruppe anzugeben. Der folgende Beispielcode lädt die Excel-Quelldatei wie im obigen Screenshot gezeigt, greift dann auf die erste Sparkline-Gruppe zu und fügt Datenbereiche und Speicherorte in der Sparkline-Gruppe hinzu. Schließlich schreibt es die ausgegebene Excel-Datei auf die Festplatte, die auch im obigen Screenshot gezeigt wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopySparkline-1.cs" >}}
