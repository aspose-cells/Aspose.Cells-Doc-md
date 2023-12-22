---
title: Anpassen von Diagrammen
description: Erfahren Sie, wie Sie Diagramme anpassen unter Aspose.Cells for .NET. Unser Leitfaden zeigt Ihnen, wie Sie Diagrammlayouts ändern, Datenreihen hinzufügen und formatieren, Achsen anpassen und verschiedene Formatierungsoptionen anwenden, um das Erscheinungsbild und die Benutzerfreundlichkeit Ihrer Diagramme zu verbessern.
keywords: Aspose.Cells for .NET, charting, customization, layouts, data series, axes, formatting, appearance, usability.
type: docs
weight: 40
url: /de/net/customizing-charts/
---
{{% alert color="primary" %}}

##  **Erstellen benutzerdefinierter Diagramme**

Bisher haben wir uns bei der Besprechung von Diagrammen mit Standarddiagrammen befasst, die über ihre Standardformatierungseinstellungen verfügen. Wir definieren nur die Datenquelle, legen einige Eigenschaften fest und das Diagramm wird mit seinen Standardformateinstellungen erstellt. Aber Aspose.Cells APIs unterstützen auch die Erstellung benutzerdefinierter Diagramme, die es Entwicklern ermöglichen, Diagramme mit ihren eigenen Formateinstellungen zu erstellen.

Entwickler können mit Aspose.Cells zur Laufzeit benutzerdefinierte Diagramme erstellen.

 Ein Diagramm besteht aus einer Datenreihe. Jede Datenreihe in Aspose.Cells wird durch a dargestellt[**Serie**](https://reference.aspose.com/cells/net/aspose.cells.charts/series) Objekt während[**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) Das Objekt dient als Sammlung von[**Serie**](https://reference.aspose.com/cells/net/aspose.cells.charts/series)Objekte. Beim Erstellen eines benutzerdefinierten Diagramms haben Entwickler die Freiheit, verschiedene Diagrammtypen für unterschiedliche Datenreihen (gesammelt in) zu verwenden[**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)Objekt).

Der folgende Beispielcode zeigt, wie Sie benutzerdefinierte Diagramme erstellen. In diesem Beispiel verwenden wir ein Säulendiagramm für die erste Datenreihe und ein Liniendiagramm für die zweite Reihe. Das Ergebnis ist, dass wir dem Arbeitsblatt ein Säulendiagramm in Kombination mit einem Liniendiagramm hinzufügen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateCustomChart-1.cs" >}}

{{% alert color="primary" %}}

Derzeit unterstützt Aspose.Cells nur benutzerdefinierte Diagramme, die Kreis-, Linien-, Säulen- und Säulenstapeldiagramme kombinieren. In zukünftigen Versionen werden jedoch weitere Diagramme unterstützt.

{{% /alert %}}
