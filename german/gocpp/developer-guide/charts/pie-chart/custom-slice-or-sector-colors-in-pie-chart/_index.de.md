---
title: Benutzerdefinierte Farben für Scheiben oder Sektoren im Kreisdiagramm mit Golang über C++
linktitle: Benutzerdefinierte Slice oder Sektorenfarben in einem Tortendiagramm
description: Lernen Sie, wie man Aspose.Cells for C++ verwendet, um die Farben von Sektoren und Segmenten in einem Tortendiagramm anzupassen. Unser Leitfaden zeigt, wie man jeder Scheibe, jedem Sektor oder Segment eine einzigartige Farbe zuweist, um die visuelle Attraktivität und die Datenpräsentation zu verbessern.
keywords: Aspose.Cells for C++, Tortendiagramm, Benutzerdefinierte Segmentfarben, Benutzerdefinierte Sektorfarbe, Visueller Reiz, Datenpräsentation.
type: docs
weight: 60
url: /de/go-cpp/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

In diesem Artikel wird erläutert, wie benutzerdefinierte Farben zu Tortendiagrammslices/Sektoren hinzugefügt werden. Standardmäßig verwenden Tortendiagramme die Microsoft Excel-Standardvorlage. Um andere Farben zu verwenden, definieren Sie die Farben im Diagramm neu.

{{% /alert %}}

Um eine benutzerdefinierte Farbe für die einzelnen Slices oder Sektoren eines Tortendiagramms festzulegen:

1. Greifen Sie auf das [**Series**](https://reference.aspose.com/cells/go-cpp/series/)-Objekt's [**ChartPoint**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/) zu.
1. Weisen Sie die Farbe Ihrer Wahl mit der [**ChartPoint.GetForegroundColor()**](https://reference.aspose.com/cells/go-cpp/area/getforegroundcolor/)-Eigenschaft zu.

In diesem Artikel wird auch erläutert, wie:

- Die Kategoriedaten eines Diagramms.
- Ein Diagrammtitel, der mit einer Zelle verknüpft ist.
- Die Schriftarteinstellungen des Diagrammtitels.
- Die Position der Legende.

{{% alert color="primary" %}}

[**ChartPoint.GetForegroundColor()**](https://reference.aspose.com/cells/go-cpp/area/getforegroundcolor/) ist nicht spezifisch für Tortendiagramme, kann aber für alle Arten von Diagrammen verwendet werden.

{{% /alert %}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CustomSliceOrSectorColorsInPieChart.go" >}}
