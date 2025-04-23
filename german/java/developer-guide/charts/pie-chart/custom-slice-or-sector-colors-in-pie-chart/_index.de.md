---
title: Benutzerdefinierte Slice oder Sektorenfarben in einem Tortendiagramm
type: docs
weight: 30
url: /de/java/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

Dieser Artikel erklärt, wie benutzerdefinierte Farben zu Tortendiagrammschnitten/Sektoren hinzugefügt werden können. Standardmäßig verwendet ein Tortendiagramm die Vorlage von Microsoft Excel. Um andere Farben zu verwenden, ist es möglich, die Farben im Diagramm neu zu definieren.

{{% /alert %}}

Um die benutzerdefinierte Farbe für die einzelnen Slices oder Sektoren des Tortendiagramms festzulegen:

1. Greifen Sie auf das [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)-Objekt's [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint) zu.
1. Weisen Sie eine Farbe Ihrer Wahl mithilfe der Methode [**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor) zu.

In diesem Artikel wird auch erläutert, wie:

- Die Kategoriedaten eines Diagramms.
- Ein Diagrammtitel, der mit einer Zelle verknüpft ist.
- Die Schriftarteinstellungen des Diagrammtitels.
- Die Position der Legende.

{{% alert color="primary" %}}

[**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor) ist nicht spezifisch für Tortendiagramme, sondern kann für alle Arten von Diagrammen verwendet werden.

{{% /alert %}}

**Benutzerdefinierte Schnittfarben im Tortendiagramm**

![todo:image_alt_text](custom-slice-or-sector-colors-in-pie-chart_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSliceOrSectorColorsPieChart-CustomSliceOrSectorColorsPieChart.java" >}}
{{< app/cells/assistant language="java" >}}
