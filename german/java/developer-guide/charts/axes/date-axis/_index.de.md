---
title: Datumsachse
description: Lernen Sie, wie Sie die Datumsachse in Aspose.Cells for Java verwalten. Unser Leitfaden wird Ihnen helfen, zu verstehen, wie Sie mit verschiedenen Datumsformaten, Zeitskalen und Tick Etikettenfrequenzen arbeiten.
keywords: Aspose.Cells for Java, Datumsachse, verwalten, Datumsformate, Zeitskalen, Tick Etikettenfrequenzen.
type: docs
weight: 200
url: /de/java/date-axis/
---

## **Mögliche Verwendungsszenarien**
Wenn Sie ein Diagramm aus Arbeitsblattdaten erstellen, die Datumsangaben verwenden und die Daten entlang der horizontalen (Kategorie-) Achse im Diagramm dargestellt werden, ändert Aspose.cells automatisch die Kategorieachse in eine Datums (Zeitskala-) Achse.
Eine Datumsachse zeigt Daten in chronologischer Reihenfolge in bestimmten Intervallen oder Basiswerten an, wie die Anzahl der Tage, Monate oder Jahre, auch wenn die Datumsangaben auf dem Arbeitsblatt nicht in aufeinanderfolgender Reihenfolge oder in den gleichen Basiswerten vorliegen.
Standardmäßig bestimmt Aspose.cells die Basiswerte für die Datumsachse aufgrund des kleinsten Unterschieds zwischen zwei Datumsangaben in den Arbeitsblattdaten. Wenn beispielsweise Daten für Aktienkurse vorliegen, bei denen der kleinste Unterschied zwischen den Daten sieben Tage beträgt, setzt Excel die Basiswerte auf Tage, aber Sie können die Basiswerte in Monate oder Jahre ändern, wenn Sie die Wertentwicklung der Aktien über einen längeren Zeitraum sehen möchten.
## **Behandeln Sie die Datumsachse wie Microsoft Excel**
Bitte sehen Sie sich den folgenden Beispielcode an, der eine neue Excel-Datei erstellt und die Werte des Diagramms im ersten Arbeitsblatt platziert. 
Dann fügen wir ein Diagramm hinzu und setzen den Typ des [**Axis**](https://reference.aspose.com/cells/java/com.aspose.cells/axis/) 
auf [**TimeScale**](https://reference.aspose.com/cells/java/com.aspose.cells/categorytype/#TIME-SCALE) und setzen dann die Basiswerte auf Tage.

![todo:image_alt_text](excel.png)

Der folgende Beispielcode generiert die [Ausgabedatei Excel](DateAxis.xlsx).

## **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DateAxis.java" >}}
{{< app/cells/assistant language="java" >}}
