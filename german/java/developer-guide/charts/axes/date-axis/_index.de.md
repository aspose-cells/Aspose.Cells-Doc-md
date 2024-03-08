---
title: Datumsachse
description: Erfahren Sie, wie Sie die Datumsachse verwalten unter Aspose.Cells for Java. Unser Leitfaden hilft Ihnen zu verstehen, wie Sie mit verschiedenen Datumsformaten, Zeitskalen und Teilstrich-Beschriftungshäufigkeiten arbeiten.
keywords: Aspose.Cells for Java, date axis, manage, date formats, time scales, tick label frequencies.
type: docs
weight: 200
url: /de/java/date-axis/
---
##  **Mögliche Nutzungsszenarien**
Wenn Sie ein Diagramm aus Arbeitsblattdaten erstellen, das Datumsangaben verwendet, und die Datumsangaben entlang der horizontalen Achse (Kategorie) im Diagramm dargestellt werden, ändert Aspose.cells die Kategorieachse automatisch in eine Datumsachse (Zeitskala).
Eine Datumsachse zeigt Datumsangaben in chronologischer Reihenfolge in bestimmten Intervallen oder Basiseinheiten an, z. B. die Anzahl der Tage, Monate oder Jahre, auch wenn die Datumsangaben auf dem Arbeitsblatt nicht in sequentieller Reihenfolge oder in denselben Basiseinheiten vorliegen.
Standardmäßig bestimmt Aspose.cells die Basiseinheiten für die Datumsachse basierend auf der kleinsten Differenz zwischen zwei beliebigen Datumsangaben in den Arbeitsblattdaten. Wenn Sie beispielsweise über Daten zu Aktienkursen verfügen, bei denen die kleinste Differenz zwischen den Daten sieben Tage beträgt, legt Excel die Basiseinheit auf Tage fest. Sie können die Basiseinheit jedoch in Monate oder Jahre ändern, wenn Sie die Wertentwicklung der Aktie über einen längeren Zeitraum sehen möchten einen längeren Zeitraum.
##  **Behandeln Sie die Datumsachse wie Microsoft in Excel**
 Bitte sehen Sie sich den folgenden Beispielcode an, der eine neue Excel-Datei erstellt und Werte des Diagramms in das erste Arbeitsblatt einfügt.
 Dann fügen wir ein Diagramm hinzu und legen den Typ fest[**Achse**](https://reference.aspose.com/cells/java/com.aspose.cells/axis/) 
 Zu[**Zeitstrahl**](https://reference.aspose.com/cells/java/com.aspose.cells/categorytype/#TIME-SCALE) und stellen Sie dann die Basiseinheiten auf Tage ein.

![todo:image_alt_text](excel.png)

 Der folgende Beispielcode generiert die[Excel-Datei ausgeben](DateAxis.xlsx).

##  **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DateAxis.java" >}}
