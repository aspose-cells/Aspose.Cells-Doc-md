---
title: Aufteilen des Bildschirms des Excel Arbeitsblatts
linktitle: Bildschirm aufteilen
type: docs
weight: 190
url: /de/net/how-to-split-screen-of-excel-worksheet
description: In diesem Artikel erfahren Sie, wie Sie bestimmte Zeilen und/oder Spalten in separaten Fenstern anzeigen können, indem Sie das Arbeitsblatt programmgesteuert in zwei oder vier Teile aufteilen mithilfe der C# Bibliothek mit .NET API.
keywords: Obere Zeilen einfrieren, Oberste Zeile einfrieren.
---

## **Einführung**

In diesem Artikel erfahren Sie, wie man bestimmte Zeilen und/oder Spalten in separate Fenster aufteilt, indem man das Arbeitsblatt in zwei oder vier Teile aufteilt. Wenn Sie mit großen Datenmengen arbeiten, müssen Sie gleichzeitig verschiedene Teile desselben Arbeitsblatts sehen, um verschiedene Teilmengen von Daten vergleichen zu können. Mit der Funktion zum Aufteilen des Bildschirms können Sie Ihre Anforderungen erfüllen.

## **Wie man den Bildschirm in Excel aufteilt**
Um ein Arbeitsblatt in zwei oder vier Teile aufzuteilen, führen Sie folgende Schritte aus:

1. Wählen Sie die Zeile/Spalte/Zelle aus, vor der Sie den Split platzieren möchten.
2. Klicken Sie im Register Ansicht auf der Registerkarte Fenster in der Gruppe Windows auf die Schaltfläche Split.

**![Bildschirm teilen](Split-Screen.png)**

## **Arbeitsblatt vertikal in Spalten teilen**

Um zwei Bereiche des Tabellenblatts vertikal zu trennen, wählen Sie die Spalte rechts von der Spalte aus, an der die Trennung erscheinen soll, und klicken Sie auf die Schaltfläche Split in Excel.

Es ist einfach, das Arbeitsblatt vertikal in Spalten programmgesteuert mit Aspose.Cells for .Net zu teilen, wir müssen nur eine Zelle in der obersten Reihe als aktive Zelle auswählen und dann
mit der Methode [**Worksheet.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/) teilen.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Vertically-Split.cs" >}}

## **Arbeitsblatt horizontal in Zeilen teilen**
Um Ihr Excel-Fenster horizontal zu trennen, wählen Sie die Zeile unterhalb der Zeile, an der die Trennung in Excel erfolgen soll.

Es ist einfach, das Arbeitsblatt horizontal in Zeilen programmgesteuert mit Aspose.Cells for .Net zu teilen, wir müssen nur eine Zelle in der linken Spalte als aktive Zelle auswählen und dann
mit der Methode [**Worksheet.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/) teilen.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Horizontally-Split.cs" >}}

## **Arbeitsblatt in vier Teile teilen**
Um vier verschiedene Abschnitte desselben Arbeitsblatts gleichzeitig anzuzeigen, teilen Sie Ihren Bildschirm sowohl vertikal als auch horizontal in Excel.

Es ist einfach, das Arbeitsblatt vertikal in Spalten programmgesteuert mit Aspose.Cells for .Net zu teilen, wir müssen nur eine Zelle nicht in der ersten Zeile und Spalte als aktive Zelle auswählen und dann
mit der Methode [**Worksheet.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/) teilen.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Split-Four.cs" >}}

## **So entfernen Sie die Trennung**
Um die Trennung des Arbeitsblatts zu entfernen, klicken Sie einfach erneut auf die Schaltfläche Split.

Aspose.Cells for .Net bietet eine Methode [**Worksheet.RemoveSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/removesplit/) zum Entfernen der Trennungseinstellung.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Remove-Split.cs" >}}
