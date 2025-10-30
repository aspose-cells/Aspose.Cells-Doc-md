---
title: X Achse vs. Kategorieachse mit Golang über C++
linktitle: X Achse Vs. Kategorieachse
description: Lernen Sie, wie Sie zwischen der X Achse und der Kategorieachse in Aspose.Cells for C++ unterscheiden. Unser Leitfaden hilft Ihnen, die Unterschiede in ihrer Verwendung und ihren Eigenschaften zu verstehen und sie nach Ihren Bedürfnissen zu konfigurieren.
keywords: Aspose.Cells for C++, X Achse, Kategorieachse, Unterschied, Verwendung, Eigenschaften, Konfiguration.
type: docs
weight: 180
url: /de/go-cpp/X-axis-vs-category-axis/
---

## **Mögliche Verwendungsszenarien**
Es gibt verschiedene Arten von X-Achsen. Während die Y-Achse eine Werttyp-Achse ist, kann die X-Achse eine Kategorietyp-Achse oder eine Werttyp-Achse sein. Bei Verwendung einer Wertachse wird die Daten als fortlaufend variierende numerische Daten behandelt, und der Marker wird an einem Punkt entlang der Achse platziert, der entsprechend seinem numerischen Wert variiert. Bei Verwendung einer Kategorieachse wird die Daten als Sequenz von nicht-numerischen Textetiketten behandelt, und der Marker wird an einem Punkt entlang der Achse platziert, entsprechend seiner Position in der Sequenz. Das folgende Beispiel verdeutlicht den Unterschied zwischen Wert- und Kategorieachsen.
Unsere Beispieldaten werden in der [Beispiel-Tabellendatei](sample.png) unten dargestellt. Die erste Spalte enthält unsere X-Achsendaten, die als Kategorien oder als Werte behandelt werden können. Beachten Sie, dass die Zahlen nicht gleichmäßig verteilt sind und auch nicht numerisch geordnet erscheinen.

![todo:image_alt_text](sample.png)

## **Behandeln Sie X- und Kategorieachse wie in Microsoft Excel**
Wir werden diese Daten auf zwei Arten von Diagrammen anzeigen, das erste Diagramm ist XY (Streu) Diagramm X als Wertachse, das zweite Diagramm ist Linien-Diagramm X als Kategorieachse.

![todo:image_alt_text](compare.png)

## **Beispielcode**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-XAxisVsCategoryAxis.go" >}}
