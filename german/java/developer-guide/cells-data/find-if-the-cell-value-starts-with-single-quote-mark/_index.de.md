---
title: Überprüfen Sie, ob der Zellenwert mit einem einfachen Anführungszeichen beginnt
type: docs
weight: 610
url: /de/java/find-if-the-cell-value-starts-with-single-quote-mark/
---

{{% alert color="primary" %}} 

Aspose.Cells bietet nun die Eigenschaft [Style.QuotePrefix](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) um festzustellen, ob der Zellenwert mit einem einzelnen Anführungszeichen beginnt. Vor dieser Eigenschaft gab es keine Möglichkeit, zwischen Zeichenfolgen wie Beispiel und 'Beispiel zu unterscheiden.

{{% /alert %}} 
## **Finden, ob der Zellenwert mit einem einzelnen Anführungszeichen beginnt**
Der folgende Beispielcode erklärt, dass die Zeichenfolgen wie Beispiel und 'Beispiel nicht mit der Eigenschaft [Cell.StringValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue) unterschieden werden können. Daher müssen wir die Eigenschaft [Style.QuotePrefix](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) verwenden, um sie zu unterscheiden.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-DetectCellValueStartsWithSingleQuote.java" >}}
