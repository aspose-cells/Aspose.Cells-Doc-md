---
title: Diagramme anpassen
description: Erfahren Sie, wie Sie Diagramme in Aspose.Cells for .NET anpassen. Unser Leitfaden zeigt Ihnen, wie Sie Diagrammlayouts ändern, Datenreihen hinzufügen und formatieren, Achsen anpassen und verschiedene Formatierungsoptionen anwenden können, um das Erscheinungsbild und die Benutzerfreundlichkeit Ihrer Diagramme zu verbessern.
keywords: Aspose.Cells for .NET, Diagrammerstellung, Anpassung, Layouts, Datenreihen, Achsen, Formatierung, Erscheinungsbild, Benutzerfreundlichkeit.
type: docs
weight: 40
url: /de/net/customizing-charts/
---

{{% alert color="primary" %}}

## **Erstellen von benutzerdefinierten Diagrammen**

Bisher haben wir bei der Besprechung von Diagrammen nur Standarddiagramme betrachtet, die ihre Standardformatierungseinstellungen haben. Wir definieren nur die Datenquelle, setzen einige Eigenschaften, und das Diagramm wird mit seinen Standardformatierungseinstellungen erstellt. Aber Aspose.Cells-APIs unterstützen auch die Erstellung benutzerdefinierter Diagramme, die es Entwicklern ermöglichen, Diagramme mit ihren eigenen Formatierungseinstellungen zu erstellen.

Entwickler können benutzerdefinierte Diagramme zur Laufzeit mithilfe von Aspose.Cells erstellen.

Ein Diagramm besteht aus einer Datenreihe. Jede Datenreihe in Aspose.Cells wird durch ein [**Series**](https://reference.aspose.com/cells/net/aspose.cells.charts/series)-Objekt repräsentiert, während ein [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)-Objekt als Sammlung von [**Series**](https://reference.aspose.com/cells/net/aspose.cells.charts/series)-Objekten dient. Beim Erstellen eines benutzerdefinierten Diagramms haben Entwickler die Freiheit, verschiedene Diagrammtypen für verschiedene Datenreihen (gesammelt im [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)-Objekt) zu verwenden.

Der nachstehende Beispielcode zeigt, wie benutzerdefinierte Diagramme erstellt werden können. In diesem Beispiel verwenden wir ein Säulendiagramm für die erste Datenreihe und ein Liniendiagramm für die zweite Reihe. Das Ergebnis ist, dass wir ein Säulendiagramm, kombiniert mit einem Liniendiagramm, dem Arbeitsblatt hinzufügen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateCustomChart-1.cs" >}}

{{% alert color="primary" %}}

Derzeit unterstützt Aspose.Cells nur benutzerdefinierte Diagramme, die Kuchen-, Linien-, Säulen- und Säulenanordnungsdiagramme kombinieren, aber in zukünftigen Versionen werden weitere Diagramme unterstützt.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
