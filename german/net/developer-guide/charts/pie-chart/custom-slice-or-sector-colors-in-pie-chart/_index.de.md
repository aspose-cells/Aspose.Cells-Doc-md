---
title: Benutzerdefinierte Segment- oder Sektorfarben im Kreisdiagramm
type: docs
weight: 60
url: /de/net/custom-slice-or-sector-colors-in-pie-chart/
---
{{% alert color="primary" %}}

In diesem Artikel wird erläutert, wie Sie Kreisdiagrammsegmenten/Sektoren benutzerdefinierte Farben hinzufügen. Standardmäßig verwenden Tortendiagramme die Excel-Standardvorlage Microsoft. Um andere Farben zu verwenden, definieren Sie die Farben im Diagramm neu.

{{% /alert %}}

So legen Sie eine benutzerdefinierte Farbe für die einzelnen Segmente oder Sektoren eines Tortendiagramms fest:

1.  Greife auf ... zu[**Serie**](https://reference.aspose.com/cells/net/aspose.cells.charts/series) Objekt[**ChartPoint**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint).
1.  Weisen Sie die Farbe Ihrer Wahl mit dem zu[**ChartPoint.Area.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells.drawing/area/properties/foregroundcolor)Eigentum.

In diesem Artikel wird außerdem erläutert, wie Sie:

- Die Kategoriedaten eines Diagramms.
- Ein mit einer Zelle verknüpfter Diagrammtitel.
- Die Einstellungen für die Schriftart des Diagrammtitels.
- Die Position der Legende.

{{% alert color="primary" %}}

[**ChartPoint.Area.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells.drawing/area/properties/foregroundcolor) ist nicht spezifisch für Tortendiagramme, kann aber für alle Arten von Diagrammen verwendet werden.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomSliceSectorColorsPieChart-1.cs" >}}
