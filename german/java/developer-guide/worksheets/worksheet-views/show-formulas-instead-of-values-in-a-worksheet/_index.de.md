---
title: Formeln statt Werte in einem Arbeitsblatt anzeigen
type: docs
weight: 100
url: /de/java/show-formulas-instead-of-values-in-a-worksheet/
---
{{% alert color="primary" %}}

Es ist möglich, Formeln anstelle von berechneten Werten in Microsoft Excel mit t anzuzeigen*Formeln anzeigen* Möglichkeit aus der**Formeln**Schleife. Wenn Formeln angezeigt werden, zeigt Microsoft Excel Formeln im Arbeitsblatt an. Dasselbe erreichen Sie mit Aspose.Cells.

{{% /alert %}} 

Aspose.Cells bietet eine[**Arbeitsblatt.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas) Eigentum. Stellen Sie dies ein**wahr**um Microsoft Excel so einzustellen, dass Formeln angezeigt werden.

Das folgende Bild zeigt das Arbeitsblatt mit einer Formel in Zelle A3: =Sum(A1:A2).

**Arbeitsblatt mit Formel in Zelle A3**

![todo: Bild_alt_Text](show-formulas-instead-of-values-in-a-worksheet_1.png)

 Das folgende Bild zeigt die Formel anstelle des berechneten Werts, aktiviert durch die Einstellung von[**Arbeitsblatt.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas) Eigentum zu**wahr** mit Aspose.Cells.

**Das Arbeitsblatt zeigt jetzt die Formel anstelle des berechneten Werts**

![todo: Bild_alt_Text](show-formulas-instead-of-values-in-a-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ShowFormulas-ShowFormulas.java" >}}
