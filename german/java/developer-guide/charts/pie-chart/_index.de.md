---
title: Erstellung eines Tortendiagramms mit Führungslinien
linktitle: Tortendiagramm
type: docs
weight: 170
url: /de/java/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

Dieser Artikel erklärt, wie man ein Kreisdiagramm mit Führungslinien von Grund auf erstellt, während man die Aspose.Cells for Java-API verwendet. In Excel ist die Option 'Führungslinien anzeigen' standardmäßig aktiviert, sodass beim Erstellen eines Kreisdiagramms in Excel die Führungslinien angezeigt werden. Beim Erstellen eines ähnlichen Diagramms mit Aspose.Cells-APIs müssen Sie jedoch explizit die [**Series.HasLeaderLines**](https://reference.aspose.com/cells/java/com.aspose.cells/series#HasLeaderLines)-Eigenschaft festlegen.

{{% /alert %}}

## **Erstellen eines Tortendiagramms mit Führungslinien**

Um die Verwendung der Aspose.Cells for Java-API zum Erstellen eines Kreisdiagramms mit Führungslinien zu demonstrieren, werden wir zunächst ein neues [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) erstellen und Daten eingeben, die als Datenquelle für die Seriendaten dienen. Sobald die Daten vorhanden sind, fügen wir eine [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) vom Typ [**Pie**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PIE) zur Diagrammsammlung hinzu und setzen ihre verschiedenen Aspekte, um die gewünschte Diagrammansicht zu erhalten.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePieChartWithLeaderLines-CreatePieChartWithLeaderLines.java" >}}

**Ergebnis Kreisdiagramm**

![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)

## Verwandte Artikel

- [Erstellen und Anpassen von Diagrammen](/cells/de/java/creating-and-customizing-charts/)
- [Diagrammformatierung](/cells/de/java/chart-formatting/)
