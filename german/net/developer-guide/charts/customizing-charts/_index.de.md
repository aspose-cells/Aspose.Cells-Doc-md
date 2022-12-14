---
title: Anpassen von Diagrammen
type: docs
weight: 40
url: /de/net/customizing-charts/
---
{{% alert color="primary" %}}

## **Erstellen von benutzerdefinierten Diagrammen**

Bisher haben wir uns bei der Erörterung von Diagrammen mit Standarddiagrammen befasst, die über ihre Standardformatierungseinstellungen verfügen. Wir definieren nur die Datenquelle, legen ein paar Eigenschaften fest und das Diagramm wird mit seinen Standardformateinstellungen erstellt. Aber Aspose.Cells-APIs unterstützen auch das Erstellen benutzerdefinierter Diagramme, mit denen Entwickler Diagramme mit ihren eigenen Formateinstellungen erstellen können.

Entwickler können mit Aspose.Cells zur Laufzeit benutzerdefinierte Diagramme erstellen.

 Ein Diagramm besteht aus einer Datenreihe. Jede Datenreihe in Aspose.Cells wird durch a dargestellt[**Serie**](https://reference.aspose.com/cells/net/aspose.cells.charts/series) Objekt während[**SerieSammlung**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) Objekt dient als Sammlung von[**Serie**](https://reference.aspose.com/cells/net/aspose.cells.charts/series)Objekte. Beim Erstellen eines benutzerdefinierten Diagramms haben Entwickler die Freiheit, verschiedene Arten von Diagrammen für verschiedene Datenreihen (gesammelt in der[**SerieSammlung**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)Objekt).

Der folgende Beispielcode zeigt, wie benutzerdefinierte Diagramme erstellt werden. In diesem Beispiel verwenden wir ein Säulendiagramm für die erste Datenreihe und ein Liniendiagramm für die zweite Reihe. Das Ergebnis ist, dass wir dem Arbeitsblatt ein Säulendiagramm in Kombination mit einem Liniendiagramm hinzufügen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateCustomChart-1.cs" >}}

{{% alert color="primary" %}}

Derzeit unterstützt Aspose.Cells nur benutzerdefinierte Diagramme, die Torten-, Linien-, Säulen- und Säulenstapeldiagramme kombinieren, aber in zukünftigen Versionen werden weitere Diagramme unterstützt.

{{% /alert %}}
