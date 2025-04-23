---
title: Diagramme anpassen
description: Lernen Sie, wie man Diagramme in Aspose.Cells für Python via .NET anpasst. Unser Leitfaden zeigt Ihnen, wie Sie Diagramm Layouts ändern, Datenreihen hinzufügen und formatieren, Achsen anpassen und verschiedene Formatierungsoptionen anwenden, um das Erscheinungsbild und die Benutzerfreundlichkeit Ihrer Diagramme zu verbessern.
keywords: Aspose.Cells für Python via .NET, Diagrammerstellung, Anpassung, Layouts, Datenreihen, Achsen, Formatierung, Erscheinungsbild, Benutzerfreundlichkeit.
type: docs
weight: 40
url: /de/python-net/customizing-charts/
---

{{% alert color="primary" %}}

## **Erstellen von benutzerdefinierten Diagrammen**

Bisher haben wir bei der Diskussion über Diagramme Standarddiagramme betrachtet, die ihre Standard-Formatierungseinstellungen haben. Wir definieren nur die Datenquelle, setzen einige Eigenschaften, und das Diagramm wird mit den Standardformatierungen erstellt. Die Aspose.Cells für Python via .NET APIs unterstützen auch die Erstellung benutzerdefinierter Diagramme, mit denen Entwickler eigene Formatierungen festlegen können.

Entwickler können benutzerdefinierte Diagramme zur Laufzeit mit Aspose.Cells für Python via .NET erstellen.

Ein Diagramm besteht aus einer Datenreihe. Jede Datenreihe in Aspose.Cells für Python via .NET wird durch ein [**Series**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series)-Objekt dargestellt, während [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection)-Objekte als Sammlung von [**Series**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series)-Objekten dienen. Bei der Erstellung eines benutzerdefinierten Diagramms haben Entwickler die Freiheit, verschiedene Diagrammtypen für unterschiedliche Datenreihen zu verwenden (gesammelt im [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection)-Objekt).

Der nachstehende Beispielcode zeigt, wie benutzerdefinierte Diagramme erstellt werden können. In diesem Beispiel verwenden wir ein Säulendiagramm für die erste Datenreihe und ein Liniendiagramm für die zweite Reihe. Das Ergebnis ist, dass wir ein Säulendiagramm, kombiniert mit einem Liniendiagramm, dem Arbeitsblatt hinzufügen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-HowToCreateCustomChart-1.py" >}}

{{% alert color="primary" %}}

Derzeit unterstützt Aspose.Cells für Python via .NET nur benutzerdefinierte Diagramme, die Tortendiagramme, Linien-, Säulen- und gestapelte Säulendiagramme kombinieren, aber in zukünftigen Versionen werden weitere Diagramme unterstützt.

{{% /alert %}}
