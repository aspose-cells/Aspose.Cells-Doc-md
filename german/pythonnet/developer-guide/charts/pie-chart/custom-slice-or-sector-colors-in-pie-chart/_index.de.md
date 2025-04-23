---
title: Benutzerdefinierte Slice oder Sektorenfarben in einem Tortendiagramm
description: Erfahren Sie, wie Sie Aspose.Cells für Python via .NET verwenden, um die Farbzuweisung für Scheiben und Sektoren in einem Kreisdiagramm zu personalisieren. Unser Leitfaden zeigt, wie Sie für jeden Abschnitt, Sektor oder Legion individuelle Farben festlegen, um die visuelle Attraktivität und die Datenvisualisierung zu verbessern.
keywords: Aspose.Cells für Python via .NET, Kreisdiagramm, Benutzerdefinierte Scheibefarben, Benutzerdefinierte Sektorfarben, Visuelle Attraktivität, Datenvisualisierung.
type: docs
weight: 60
url: /de/python-net/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

In diesem Artikel wird erläutert, wie benutzerdefinierte Farben zu Tortendiagrammslices/Sektoren hinzugefügt werden. Standardmäßig verwenden Tortendiagramme die Microsoft Excel-Standardvorlage. Um andere Farben zu verwenden, definieren Sie die Farben im Diagramm neu.

{{% /alert %}}

Um eine benutzerdefinierte Farbe für die einzelnen Slices oder Sektoren eines Tortendiagramms festzulegen:

1. Greifen Sie auf das [**Series**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series)-Objekt's [**ChartPoint**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint) zu.
1. Weisen Sie die Farbe Ihrer Wahl mit der [**ChartPoint.area.foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/area/foreground_color)-Eigenschaft zu.

In diesem Artikel wird auch erläutert, wie:

- Die Kategoriedaten eines Diagramms.
- Ein Diagrammtitel, der mit einer Zelle verknüpft ist.
- Die Schriftarteinstellungen des Diagrammtitels.
- Die Position der Legende.

{{% alert color="primary" %}}

[**ChartPoint.area.foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/area/foreground_color) ist nicht spezifisch für Tortendiagramme, kann aber für alle Arten von Diagrammen verwendet werden.

{{% /alert %}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CustomSliceSectorColorsPieChart-1.py" >}}
