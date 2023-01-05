---
title: Benutzerdefinierte Segment- oder Sektorfarben im Kreisdiagramm
type: docs
weight: 30
url: /de/java/custom-slice-or-sector-colors-in-pie-chart/
---
{{% alert color="primary" %}}

In diesem Artikel wird erläutert, wie Sie Kreisdiagrammsegmenten/Sektoren benutzerdefinierte Farben hinzufügen. Standardmäßig verwenden Tortendiagramme die Excel-Standardvorlage Microsoft. Um andere Farben zu verwenden, ist es möglich, die Farben im Diagramm neu zu definieren.

{{% /alert %}}

So legen Sie die benutzerdefinierte Farbe für die einzelnen Segmente oder Sektoren eines Tortendiagramms fest:

1.  Greife auf ... zu[**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) Objekt[**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint).
1.  Weisen Sie mit dem eine Farbe Ihrer Wahl zu[**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor)Methode.

In diesem Artikel wird auch erklärt, wie Sie Folgendes einstellen:

- Die Kategoriedaten eines Diagramms.
- Ein mit einer Zelle verknüpfter Diagrammtitel.
- Die Einstellungen für die Schriftart des Diagrammtitels.
- Die Position der Legende.

{{% alert color="primary" %}}

[**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor) ist nicht spezifisch für Tortendiagramme, sondern kann für alle Arten von Diagrammen verwendet werden.

{{% /alert %}}

**Benutzerdefinierte Slice-Farben im Kreisdiagramm**

![todo: Bild_alt_Text](custom-slice-or-sector-colors-in-pie-chart_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSliceOrSectorColorsPieChart-CustomSliceOrSectorColorsPieChart.java" >}}
