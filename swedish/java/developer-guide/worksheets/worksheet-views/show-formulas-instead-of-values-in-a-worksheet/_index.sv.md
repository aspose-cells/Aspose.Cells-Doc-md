---
title: Visa formler istället för värden i ett kalkylblad
type: docs
weight: 100
url: /sv/java/show-formulas-instead-of-values-in-a-worksheet/
---
{{% alert color="primary" %}}

Det är möjligt att visa formler istället för beräknade värden i Microsoft Excel med hjälp av t*Visa formler* alternativ från**Formler**band. När formler visas visar Microsoft Excel formler i kalkylbladet. Du kan uppnå samma sak med Aspose.Cells.

{{% /alert %}} 

Aspose.Cells tillhandahåller en[**Worksheet.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas) fast egendom. Ställ in detta på**Sann**för att ställa in Microsoft Excel för att visa formler.

Följande bild visar kalkylbladet som har en formel i cell A3: =Sum(A1:A2).

**Arbetsblad med formel i cell A3**

![todo:image_alt_text](show-formulas-instead-of-values-in-a-worksheet_1.png)

 Följande bild visar formeln istället för det beräknade värdet, aktiverat genom att ställa in[**Worksheet.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas) egendom till**Sann** med Aspose.Cells.

**Arbetsbladet visar nu formeln istället för det beräknade värdet**

![todo:image_alt_text](show-formulas-instead-of-values-in-a-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ShowFormulas-ShowFormulas.java" >}}
