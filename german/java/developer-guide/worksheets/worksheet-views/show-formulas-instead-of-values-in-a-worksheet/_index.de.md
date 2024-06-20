---
title: Formeln anstelle von Werten in einem Arbeitsblatt anzeigen
type: docs
weight: 100
url: /de/java/show-formulas-instead-of-values-in-a-worksheet/
---

{{% alert color="primary" %}}

Es ist möglich, in Microsoft Excel Formeln anstelle von berechneten Werten anzuzeigen, indem Sie die *Formeln* Option im **Formeln**-Menüband verwenden. Wenn Formeln angezeigt werden, zeigt Microsoft Excel die Formeln im Arbeitsblatt an. Sie können dasselbe erreichen, indem Sie Aspose.Cells verwenden.

{{% /alert %}} 

Aspose.Cells bietet eine [**Worksheet.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas)-Eigenschaft. Setzen Sie dies auf **true**, um Microsoft Excel anzuzeigen Formeln einstellen.

Im folgenden Bild wird das Arbeitsblatt gezeigt, das eine Formel in Zelle A3 enthält: =Sum(A1:A2).

**Arbeitsblatt mit Formel in Zelle A3**

![todo:image_alt_text](show-formulas-instead-of-values-in-a-worksheet_1.png)

Im folgenden Bild wird die Formel anstelle des berechneten Werts angezeigt, indem die [**Worksheet.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas)-Eigenschaft auf **true** mit Aspose.Cells eingestellt wird.

**Arbeitsblatt zeigt jetzt die Formel anstelle des berechneten Werts**

![todo:image_alt_text](show-formulas-instead-of-values-in-a-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ShowFormulas-ShowFormulas.java" >}}
