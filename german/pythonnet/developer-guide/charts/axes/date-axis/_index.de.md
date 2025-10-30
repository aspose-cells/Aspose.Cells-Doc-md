---
title: Datumsachse
description: Erfahren Sie, wie man den Datumsachsen in Aspose.Cells für Python via .NET verwaltet. Unser Leitfaden zeigt, wie man mit verschiedenen Datumsformaten, Zeitskalen und Tick Beschriftungsfrequenzen arbeitet.
keywords: Aspose.Cells für Python via .NET, Datenachse, verwalten, Datenformate, Zeitskalen, Tick Label Frequenzen.
type: docs
weight: 200
url: /de/python-net/date-axis/
---

## **Mögliche Verwendungsszenarien**
Wenn Sie ein Diagramm aus Arbeitsblattdaten erstellen, die Datumsangaben verwenden und die Daten entlang der horizontalen (Kategorie-) Achse im Diagramm dargestellt werden, ändert Aspose.cells automatisch die Kategorieachse in eine Datums (Zeitskala-) Achse.
Eine Datumsachse zeigt Daten in chronologischer Reihenfolge in bestimmten Intervallen oder Basiswerten an, wie die Anzahl der Tage, Monate oder Jahre, auch wenn die Datumsangaben auf dem Arbeitsblatt nicht in aufeinanderfolgender Reihenfolge oder in den gleichen Basiswerten vorliegen.
Standardmäßig bestimmt Aspose.cells die Basiswerte für die Datumsachse aufgrund des kleinsten Unterschieds zwischen zwei Datumsangaben in den Arbeitsblattdaten. Wenn beispielsweise Daten für Aktienkurse vorliegen, bei denen der kleinste Unterschied zwischen den Daten sieben Tage beträgt, setzt Excel die Basiswerte auf Tage, aber Sie können die Basiswerte in Monate oder Jahre ändern, wenn Sie die Wertentwicklung der Aktien über einen längeren Zeitraum sehen möchten.

## **Behandeln Sie die Datumsachse wie Microsoft Excel**
Bitte sehen Sie sich den folgenden Beispielcode an, der eine neue Excel-Datei erstellt und die Werte des Diagramms im ersten Arbeitsblatt platziert. 
Dann fügen wir ein Diagramm hinzu und setzen den Typ des [**Axis**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/axis) 
auf [**TIME_SCALE**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/categorytype/) und setzen dann die Basiswerte auf Tage.

![todo:image_alt_text](excel.png)

## **Beispielcode**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-DateAxis.py" >}}
{{< app/cells/assistant language="python-net" >}}
