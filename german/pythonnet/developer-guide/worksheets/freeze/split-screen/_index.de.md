---
title: Aufteilen des Bildschirms des Excel Arbeitsblatts
linktitle: Bildschirm aufteilen
type: docs
weight: 190
url: /de/python-net/how-to-split-screen-of-excel-worksheet
description: In diesem Artikel erfahren Sie, wie Sie bestimmte Zeilen und/oder Spalten in separaten Fenstern anzeigen können, indem Sie das Arbeitsblatt programmgesteuert mit Aspose.Cells für Python via .NET APIs in zwei oder vier Teile aufteilen.
keywords: Python Excel Bibliothek, Python Einfrieren oberer Zeilen, Python Obere Zeile einfrieren, Python Arbeitsblatt vertikal auf Spalten aufteilen, Python Arbeitsblatt horizontal auf Zeilen aufteilen, Python Arbeitsblatt in vier Teile aufteilen Python Wie man die Aufteilung entfernt.
---

## **Einführung**

In diesem Artikel erfahren Sie, wie man bestimmte Zeilen und/oder Spalten in separate Fenster aufteilt, indem man das Arbeitsblatt in zwei oder vier Teile aufteilt. Wenn Sie mit großen Datenmengen arbeiten, müssen Sie gleichzeitig verschiedene Teile desselben Arbeitsblatts sehen, um verschiedene Teilmengen von Daten vergleichen zu können. Mit der Funktion zum Aufteilen des Bildschirms können Sie Ihre Anforderungen erfüllen.

## **Wie man den Bildschirm in Excel aufteilt**
Um ein Arbeitsblatt in zwei oder vier Teile aufzuteilen, führen Sie folgende Schritte aus:

1. Wählen Sie die Zeile/Spalte/Zelle aus, vor der Sie den Split platzieren möchten.
2. Klicken Sie im Register Ansicht auf der Registerkarte Fenster in der Gruppe Windows auf die Schaltfläche Split.

**![Bildschirm teilen](Split-Screen.png)**

## **Wie man ein Arbeitsblatt vertikal in Spalten aufteilt**

Um zwei Bereiche des Tabellenblatts vertikal zu trennen, wählen Sie die Spalte rechts von der Spalte aus, an der die Trennung erscheinen soll, und klicken Sie auf die Schaltfläche Split in Excel.

Es ist einfach, ein Arbeitsblatt vertikal in Spalten programmgesteuert mit Aspose.Cells für Python via .NET aufzuteilen, wir müssen nur eine Zelle in der obersten Zeile als aktive Zelle auswählen, dann
mit der Methode [**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/) teilen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Vertically-Split.py" >}}

## **Wie man ein Arbeitsblatt horizontal in Zeilen aufteilt**
Um Ihr Excel-Fenster horizontal zu trennen, wählen Sie die Zeile unterhalb der Zeile, an der die Trennung in Excel erfolgen soll.

Es ist einfach, ein Arbeitsblatt horizontal in Zeilen programmgesteuert mit Aspose.Cells für Python via .NET aufzuteilen, wir müssen nur eine Zelle in der linken Spalte als aktive Zelle auswählen, dann
mit der Methode [**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/) teilen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Horizontally-Split.py" >}}

## **Wie man ein Arbeitsblatt in vier Teile aufteilt**
Um vier verschiedene Abschnitte desselben Arbeitsblatts gleichzeitig anzuzeigen, teilen Sie Ihren Bildschirm sowohl vertikal als auch horizontal in Excel.

Es ist einfach, ein Arbeitsblatt vertikal in Spalten programmgesteuert mit Aspose.Cells für Python via .NET aufzuteilen, wir müssen nur eine Zelle nicht in der ersten Zeile und Spalte als aktive Zelle auswählen, dann
mit der Methode [**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/) teilen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Split-Four.py" >}}

## **Wie man die Aufteilung entfernt**
Um die Trennung des Arbeitsblatts zu entfernen, klicken Sie einfach erneut auf die Schaltfläche Split.

Aspose.Cells für Python via .NET bietet eine [**Worksheet.remove_split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/remove_split/)-Methode zum Entfernen der Aufteilungseinstellung an.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Remove-Split.py" >}}
