---
title: Sparkline kopieren durch Festlegen des Datenbereichs und des Speicherorts der Sparkline Gruppe
type: docs
weight: 300
url: /de/python-net/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---

{{% alert color="primary" %}}

Microsoft Excel erlaubt das Kopieren eines Sparkline, indem man den Datenbereich und den Ort der Sparkline-Gruppe angibt. Aspose.Cells für Python via .NET unterstützt dieses Feature.

{{% /alert %}}

Um eine Sparkline in andere Zellen in Microsoft Excel zu kopieren:

1. Wählen Sie die Zelle aus, die die Sparkline enthält.
1. Wählen Sie **Daten bearbeiten** im **Sparkline**-Abschnitt des **Entwurfs**-Registers aus.
1. Wählen Sie **Gruppenposition & Daten bearbeiten** aus.
1. Geben Sie den Datenbereich und den Speicherort an.
1. Klicken Sie auf **OK**.

Aspose.Cells für Python via .NET bietet die Methode SparklineCollection.Add(datenBereich, Zeile, Spalte) an, um den Datenbereich und den Ort einer Sparkline-Gruppe festzulegen. Das folgende Beispiel lädt die Quelldatei Excel wie im Screenshot oben, greift auf die erste Sparkline-Gruppe zu und fügt Datenbereiche und Orte in die Sparkline-Gruppe ein. Abschließend wird die Ausgabedatei auf die Festplatte geschrieben, die ebenfalls im obigen Screenshot sichtbar ist.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Sparklines-CopySparkline-1.py" >}}

