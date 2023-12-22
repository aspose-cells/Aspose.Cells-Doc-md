---
title: X-Achse vs. Kategorieachse
description: Erfahren Sie in Aspose.Cells for .NET, wie Sie zwischen der X-Achse und der Kategorieachse unterscheiden können. Unser Leitfaden hilft Ihnen, die Unterschiede in ihrer Verwendung und ihren Eigenschaften zu verstehen und sie entsprechend Ihren Anforderungen zu konfigurieren.
keywords: Aspose.Cells for .NET, X axis, Category axis, difference, usage, properties, configuration.
type: docs
weight: 180
url: /de/net/X-axis-vs-category-axis/
---
##  **Mögliche Nutzungsszenarien**
Es gibt verschiedene Arten von X-Achsen. Während die Y-Achse eine Achse vom Typ „Wert“ ist, kann die X-Achse eine Achse vom Typ „Kategorie“ oder eine Achse vom Typ „Wert“ sein. Bei Verwendung einer Wertachse werden die Daten als sich kontinuierlich ändernde numerische Daten behandelt, und die Markierung wird an einem Punkt entlang der Achse platziert, der entsprechend ihrem numerischen Wert variiert. Bei Verwendung einer Kategorieachse werden die Daten als Folge nicht numerischer Textbeschriftungen behandelt, und die Markierung wird entsprechend ihrer Position in der Folge an einem Punkt entlang der Achse platziert. Das folgende Beispiel veranschaulicht den Unterschied zwischen Wert- und Kategorieachsen.
 Unsere Beispieldaten werden im angezeigt[Beispieltabellendatei](sample.png) unten. Die erste Spalte enthält unsere X-Achsendaten, die als Kategorien oder als Werte behandelt werden können. Beachten Sie, dass die Zahlen nicht gleichmäßig verteilt sind und auch nicht in numerischer Reihenfolge erscheinen.

![todo:image_alt_text](sample.png)
##  **Behandeln Sie die X- und Kategorieachse wie Microsoft Excel**
Wir werden diese Daten in zwei Arten von Diagrammen anzeigen: Das erste Diagramm ist ein XY-Diagramm (Streudiagramm) X als Wertachse, das zweite Diagramm ist ein Liniendiagramm X als Kategorieachse.

![todo:image_alt_text](compare.png)
##  **Beispielcode**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "X-axis-vs-category-axis.cs" >}}
