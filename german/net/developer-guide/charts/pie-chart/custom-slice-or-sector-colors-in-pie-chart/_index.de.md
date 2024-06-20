---
title: Benutzerdefinierte Slice oder Sektorenfarben in einem Tortendiagramm
description: Erfahren Sie, wie Sie Aspose.Cells for .NET verwenden, um Slice und Sektorenfarben in einem Tortendiagramm anzupassen. Unser Leitfaden wird zeigen, wie Sie einzigartige Farben für jeden Slice, Sektor oder Legion zuweisen können, um die visuelle Anziehungskraft und die Datenrepräsentation zu verbessern.
keywords: Aspose.Cells for .NET, Tortendiagramm, benutzerdefinierte Slice Farben, benutzerdefinierte Sektorfarben, visuelle Anziehungskraft, Datenrepräsentation.
type: docs
weight: 60
url: /de/net/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

In diesem Artikel wird erläutert, wie benutzerdefinierte Farben zu Tortendiagrammslices/Sektoren hinzugefügt werden. Standardmäßig verwenden Tortendiagramme die Microsoft Excel-Standardvorlage. Um andere Farben zu verwenden, definieren Sie die Farben im Diagramm neu.

{{% /alert %}}

Um eine benutzerdefinierte Farbe für die einzelnen Slices oder Sektoren eines Tortendiagramms festzulegen:

1. Greifen Sie auf das [**Series**](https://reference.aspose.com/cells/net/aspose.cells.charts/series)-Objekt's [**ChartPoint**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint) zu.
1. Weisen Sie die Farbe Ihrer Wahl mit der [**ChartPoint.Area.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells.drawing/area/properties/foregroundcolor)-Eigenschaft zu.

In diesem Artikel wird auch erläutert, wie:

- Die Kategoriedaten eines Diagramms.
- Ein Diagrammtitel, der mit einer Zelle verknüpft ist.
- Die Schriftarteinstellungen des Diagrammtitels.
- Die Position der Legende.

{{% alert color="primary" %}}

[**ChartPoint.Area.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells.drawing/area/properties/foregroundcolor) ist nicht spezifisch für Tortendiagramme, kann aber für alle Arten von Diagrammen verwendet werden.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomSliceSectorColorsPieChart-1.cs" >}}
