---
title: Geteilter Bildschirm des Excel-Arbeitsblatts
linktitle: Geteilter Bildschirm
type: docs
weight: 190
url: /de/net/how-to-split-screen-of-excel-worksheet
description: In diesem Artikel erfahren Sie, wie Sie bestimmte Zeilen und/oder Spalten in separaten Bereichen anzeigen, indem Sie das Arbeitsblatt mithilfe der Bibliothek C# mit .NET API programmgesteuert in zwei oder vier Teile aufteilen.
keywords: Freeze top rows, Feeze top row.
---
{{% alert color="primary" %}}

In diesem Artikel erfahren Sie, wie Sie bestimmte Zeilen und/oder Spalten in separaten Bereichen anzeigen, indem Sie das Arbeitsblatt in zwei oder vier Teile aufteilen.
Wenn wir mit großen Datenmengen arbeiten, müssen wir jeweils einige Bereiche desselben Arbeitsblatts sehen, um verschiedene Teilmengen von Daten vergleichen zu können.
Die Split-Screen-Funktion kann Ihren Anforderungen gerecht werden.

{{% /alert %}}

##  **So teilen Sie den Bildschirm in Excel**
Gehen Sie wie folgt vor, um ein Arbeitsblatt in zwei oder vier Teile aufzuteilen:

1. Wählen Sie die Zeile/Spalte/Zelle aus, vor der Sie die Teilung platzieren möchten.
2. Klicken Sie auf der Registerkarte „Ansicht“ in der Gruppe „Windows“ auf die Schaltfläche „Teilen“.

**![Geteilter Bildschirm](Split-Screen.png)**

##  **Teilen Sie das Arbeitsblatt vertikal in Spalten auf**

Um zwei Bereiche der Tabelle vertikal zu trennen, wählen Sie die Spalte rechts neben der Spalte aus, in der die Aufteilung erfolgen soll, und klicken Sie in Excel auf die Schaltfläche „Teilen“.

Mit Aspose.Cells für .Net ist es einfach, ein Arbeitsblatt programmgesteuert vertikal in Spalten aufzuteilen. Wir müssen dann nur eine Zelle in der oberen Zeile als aktive Zelle auswählen
geteilt mit[**Arbeitsblatt.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/) Methode.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Vertically-Split.cs" >}}

##  **Arbeitsblatt horizontal in Zeilen aufteilen**
Um Ihr Excel-Fenster horizontal zu teilen, wählen Sie die Zeile unterhalb der Zeile aus, in der die Teilung in Excel erfolgen soll.

Mit Aspose.Cells für .Net ist es einfach, ein Arbeitsblatt programmgesteuert horizontal in Zeilen aufzuteilen. Wir müssen dann nur eine Zelle in der linken Spalte als aktive Zelle auswählen
geteilt mit[**Arbeitsblatt.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/) Methode.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Horizontally-Split.cs" >}}

##  **Teilen Sie das Arbeitsblatt in vier Teile**
Um vier verschiedene Abschnitte desselben Arbeitsblatts gleichzeitig anzuzeigen, teilen Sie Ihren Bildschirm in Excel sowohl vertikal als auch horizontal.

Mit Aspose.Cells für .Net ist es einfach, ein Arbeitsblatt programmgesteuert vertikal in Spalten aufzuteilen. Wir müssen dann nur eine Zelle, die sich nicht in der ersten Zeile und Spalte befindet, als aktive Zelle auswählen
geteilt mit[**Arbeitsblatt.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/) Methode.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Split-Four.cs" >}}

##  **So entfernen Sie Split**
Um die Arbeitsblattaufteilung aufzuheben, klicken Sie einfach erneut auf die Schaltfläche „Teilen“.

 Aspose.Cells für .Net bietet eine[**Arbeitsblatt.RemoveSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/removesplit/) Methode zum Entfernen der Split-Einstellung.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Remove-Split.cs" >}}