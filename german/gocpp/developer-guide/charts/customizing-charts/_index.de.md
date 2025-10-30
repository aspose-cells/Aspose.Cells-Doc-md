---
title: Diagramme mit Golang über C++ anpassen
linktitle: Diagramme anpassen
description: Erfahren Sie, wie Sie Diagramme in Aspose.Cells for C++ anpassen können. Unser Leitfaden zeigt Ihnen, wie Sie Diagrammlayouts ändern, Datenreihen hinzufügen und formatieren, Achsen anpassen und verschiedene Formatierungsoptionen anwenden, um das Aussehen und die Benutzerfreundlichkeit Ihrer Diagramme zu verbessern.
keywords: Aspose.Cells for C++, Diagrammerstellung, Anpassung, Layouts, Datenreihen, Achsen, Formatierung, Erscheinungsbild, Benutzerfreundlichkeit.
type: docs
weight: 40
url: /de/go-cpp/customizing-charts/
---


## **Erstellen von benutzerdefinierten Diagrammen**

Bisher haben wir bei der Diskussion über Diagramme standardisierte Diagramme mit ihren Standardformatierungseinstellungen betrachtet. Wir definieren nur die Datenquelle, setzen einige Eigenschaften und das Diagramm wird mit den Standardformatierungen erstellt. Aber Aspose.Cells APIs unterstützen auch die Erstellung von benutzerdefinierten Diagrammen, die es Entwicklern ermöglichen, Diagramme mit eigenen Formatierungseinstellungen zu erstellen.

Entwickler können benutzerdefinierte Diagramme zur Laufzeit mithilfe von Aspose.Cells erstellen.

Ein Diagramm besteht aus einer Datenreihe. Jede Datenreihe in Aspose.Cells wird durch ein [**Series**](https://reference.aspose.com/cells/go-cpp/series/)-Objekt repräsentiert, während ein [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/)-Objekt als Sammlung von [**Series**](https://reference.aspose.com/cells/go-cpp/series/)-Objekten dient. Beim Erstellen eines benutzerdefinierten Diagramms haben Entwickler die Freiheit, verschiedene Diagrammtypen für verschiedene Datenreihen (gesammelt im [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/)-Objekt) zu verwenden.

Der nachstehende Beispielcode zeigt, wie benutzerdefinierte Diagramme erstellt werden können. In diesem Beispiel verwenden wir ein Säulendiagramm für die erste Datenreihe und ein Liniendiagramm für die zweite Reihe. Das Ergebnis ist, dass wir ein Säulendiagramm, kombiniert mit einem Liniendiagramm, dem Arbeitsblatt hinzufügen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CustomizingCharts.go" >}}
{{% alert color="primary" %}}

Derzeit unterstützt Aspose.Cells nur benutzerdefinierte Diagramme, die Kreis-, Linien-, Säulen- und Säulenstapel-Diagramme kombinieren, aber in zukünftigen Versionen werden weitere Diagrammtypen unterstützt.

{{% /alert %}}
