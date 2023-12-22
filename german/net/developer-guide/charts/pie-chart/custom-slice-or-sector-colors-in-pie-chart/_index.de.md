---
title: Benutzerdefinierte Segment- oder Sektorfarben im Kreisdiagramm
description: Erfahren Sie, wie Sie mit Aspose.Cells for .NET die Farben von Segmenten und Sektoren in einem Kreisdiagramm anpassen. Unser Leitfaden zeigt, wie Sie jedem Abschnitt, Sektor oder jeder Legion eindeutige Farben zuweisen, um die visuelle Attraktivität und Datendarstellung zu verbessern.
keywords: Aspose.Cells for .NET, Pie Chart, Custom Slice Colors, Custom Sector Colors, Visual Appeal, Data Representation.
type: docs
weight: 60
url: /de/net/custom-slice-or-sector-colors-in-pie-chart/
---
{{% alert color="primary" %}}

In diesem Artikel wird erläutert, wie Sie benutzerdefinierte Farben zu Kreisdiagrammabschnitten/-sektoren hinzufügen. Standardmäßig verwenden Kreisdiagramme die Excel-Standardvorlage Microsoft. Um andere Farben zu verwenden, definieren Sie die Farben im Diagramm neu.

{{% /alert %}}

So legen Sie eine benutzerdefinierte Farbe für die einzelnen Abschnitte oder Sektoren eines Kreisdiagramms fest:

1.  Greife auf ... zu[**Serie**](https://reference.aspose.com/cells/net/aspose.cells.charts/series) Objekt[**ChartPoint**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint).
1. Weisen Sie die Farbe Ihrer Wahl zu[**ChartPoint.Area.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells.drawing/area/properties/foregroundcolor)Eigentum.

In diesem Artikel wird außerdem Folgendes erläutert:

- Die Kategoriedaten eines Diagramms.
- Ein Diagrammtitel, der mit einer Zelle verknüpft ist.
- Die Einstellungen für die Schriftart des Diagrammtitels.
- Die Position der Legende.

{{% alert color="primary" %}}

[**ChartPoint.Area.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells.drawing/area/properties/foregroundcolor) ist nicht spezifisch für Kreisdiagramme, kann aber für alle Arten von Diagrammen verwendet werden.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomSliceSectorColorsPieChart-1.cs" >}}
