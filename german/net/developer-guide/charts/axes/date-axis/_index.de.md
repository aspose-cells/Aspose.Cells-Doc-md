---
title: Datumsachse
type: docs
weight: 200
url: /de/net/date-axis/
---
## **Mögliche Nutzungsszenarien**
Wenn Sie ein Diagramm aus Arbeitsblattdaten erstellen, das Datumsangaben verwendet, und die Datumsangaben entlang der horizontalen Achse (Kategorie) im Diagramm dargestellt werden, ändert Aspose.cells automatisch die Kategorieachse in eine Datumsachse (Zeitskala).
Eine Datumsachse zeigt Daten in chronologischer Reihenfolge in bestimmten Intervallen oder Basiseinheiten an, z. B. die Anzahl der Tage, Monate oder Jahre, auch wenn die Daten auf dem Arbeitsblatt nicht in fortlaufender Reihenfolge oder in denselben Basiseinheiten sind.
Standardmäßig bestimmt Aspose.cells die Basiseinheiten für die Datumsachse basierend auf der kleinsten Differenz zwischen zwei Datumsangaben in den Arbeitsblattdaten. Wenn Sie beispielsweise Daten für Aktienkurse haben, bei denen die kleinste Differenz zwischen Datumsangaben sieben Tage beträgt, legt Excel die Basiseinheit auf Tage fest, aber Sie können die Basiseinheit auf Monate oder Jahre ändern, wenn Sie die Wertentwicklung der Aktie überblicken möchten einen längeren Zeitraum.
## **Behandeln Sie die Datumsachse wie Microsoft Excel**
 Bitte sehen Sie sich den folgenden Beispielcode an, der eine neue Excel-Datei erstellt und Werte des Diagramms in das erste Arbeitsblatt einfügt.
 Dann fügen wir ein Diagramm hinzu und legen den Typ fest[**Achse**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis) 
 zu[**Zeitstrahl**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis/categorytype/) und stellen Sie dann die Basiseinheiten auf Tage ein.

![todo: Bild_alt_Text](excel.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DateAxis.cs" >}}
