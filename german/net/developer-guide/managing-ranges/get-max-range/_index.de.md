---
title: Ermitteln Sie die maximale Reichweite in einem Arbeitsblatt
type: docs
weight: 360
url: /de/net/get-max-range-in-a-worksheet/
description: In diesem Artikel wird beschrieben, wie Sie den maximalen Bereich, den maximalen Datenbereich und den maximalen Anzeigebereich von Excel-Dateien mit Aspose.Cells für die .Net-Bibliothek erhalten.
---
{{% alert color="primary" %}} 

Beim Lesen von Daten aus dem Arbeitsblatt müssen wir die maximale Fläche kennen.

Beim Kopieren aller Daten aus einem Arbeitsblatt müssen wir die maximale Fläche kennen.

Beim Exportieren eines bestimmten Bereichs in HTML und PDF müssen wir den maximalen Bereich kennen.

 Aspose.Cells für .Net enthält verschiedene Möglichkeiten, den maximalen Bereich in einem Arbeitsblatt zu ermitteln.


{{% /alert %}} 



##  **Maximale Reichweite erreichen**
 In Aspose.Cells, wenn die[**Reihe**](https://reference.aspose.com/cells/net/aspose.cells/row) Und[**Spalte**](https://reference.aspose.com/cells/net/aspose.cells/column) Wenn Objekte initialisiert werden, werden diese Zeilen und Spalten bis zum maximalen Bereich gezählt, auch wenn in leeren Zeilen oder Spalten keine Daten vorhanden sind.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Range.cs" >}}

##  **Maximale Datenreichweite abrufen**
In den meisten Fällen müssen wir nur alle Bereiche abrufen, die alle Daten enthalten, auch wenn die leeren Zellen außerhalb des Bereichs formatiert sind.
Und die Einstellungen zu Formen, Tabellen und Pivottables werden ignoriert.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Data-Range.cs" >}}

##  **Maximale Anzeigereichweite erreichen**
Wenn wir alle Daten aus dem Arbeitsblatt nach HTML, PDF oder Bilder exportieren, müssen wir einen Bereich erhalten, der alle sichtbaren Objekte enthält, einschließlich Daten, Stile, Grafiken, Tabellen und Pivot-Tabellen.
Die folgenden Codes zeigen, wie der maximale Anzeigebereich in HTML gerendert wird:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Display-Range.cs" >}}

 Hier ist[Quell-Excel-Datei](Book1.xlsx).
