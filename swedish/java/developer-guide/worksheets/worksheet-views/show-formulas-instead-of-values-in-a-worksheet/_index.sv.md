---
title: Visa formler istället för värden i ett arbetsblad
type: docs
weight: 100
url: /sv/java/show-formulas-instead-of-values-in-a-worksheet/
---

{{% alert color="primary" %}}

Det är möjligt att visa formler istället för beräknade värden i Microsoft Excel genom att använda t*Visa formler* alternativet från **Formler**-fliken. När formler visas visar Microsoft Excel formler i arbetsbladet. Du kan uppnå samma sak med Aspose.Cells.

{{% /alert %}} 

Aspose.Cells tillhandahåller en [**Worksheet.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas) egenskap. Ställ in den på **true** för att få Microsoft Excel att visa formler.

Följande bild visar arbetsbladet som har en formel i cell A3: =Sum(A1:A2).

**Arbetsblad med formel i cell A3**

![todo:image_alt_text](show-formulas-instead-of-values-in-a-worksheet_1.png)

Följande bild visar formeln istället för det beräknade värdet, aktiverat genom att ställa in [**Worksheet.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas) egenskapen till **true** med Aspose.Cells.

**Arbetsblad visar nu formeln istället för det beräknade värdet**

![todo:image_alt_text](show-formulas-instead-of-values-in-a-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ShowFormulas-ShowFormulas.java" >}}
{{< app/cells/assistant language="java" >}}
