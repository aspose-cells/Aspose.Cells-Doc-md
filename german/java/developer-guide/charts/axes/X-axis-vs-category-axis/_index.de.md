---
title: X Achse Vs. Kategorieachse
description: Lernen Sie, wie Sie zwischen der X Achse und der Kategoriesachse in Aspose.Cells for Java unterscheiden. Unser Leitfaden wird Ihnen helfen, die Unterschiede in ihrer Verwendung und Eigenschaften zu verstehen und sie gemäß Ihren Anforderungen zu konfigurieren.
keywords: Aspose.Cells for Java, X Achse, Kategoriesachse, Unterschied, Verwendung, Eigenschaften, Konfiguration.
type: docs
weight: 180
url: /de/java/x-axis-vs-category-axis/
---

## **Mögliche Verwendungsszenarien**
Es gibt verschiedene Arten von X-Achsen. Während die Y-Achse eine Werttyp-Achse ist, kann die X-Achse eine Kategorietyp-Achse oder eine Werttyp-Achse sein. Bei Verwendung einer Wertachse wird die Daten als fortlaufend variierende numerische Daten behandelt, und der Marker wird an einem Punkt entlang der Achse platziert, der entsprechend seinem numerischen Wert variiert. Bei Verwendung einer Kategorieachse wird die Daten als Sequenz von nicht-numerischen Textetiketten behandelt, und der Marker wird an einem Punkt entlang der Achse platziert, entsprechend seiner Position in der Sequenz. Das folgende Beispiel verdeutlicht den Unterschied zwischen Wert- und Kategorieachsen.
Unsere Beispieldaten werden in der [Beispiel-Tabellendatei](sample.png) unten dargestellt. Die erste Spalte enthält unsere X-Achsendaten, die als Kategorien oder als Werte behandelt werden können. Beachten Sie, dass die Zahlen nicht gleichmäßig verteilt sind und auch nicht numerisch geordnet erscheinen.

![todo:image_alt_text](sample.png)
## **Behandeln Sie X- und Kategorieachse wie in Microsoft Excel**
Wir werden diese Daten in zwei Arten von Diagrammen darstellen, das erste Diagramm ist ein XY (Punkte) Diagramm mit X als Wertachse, das zweite Diagramm ist ein Liniendiagramm mit X als Kategorieachse.

![todo:image_alt_text](compare.png)

Der folgende Beispielcode generiert die [Ausgabedatei Excel](XAxis.xlsx).

## **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "X-axis-vs-category-axis.java" >}}
