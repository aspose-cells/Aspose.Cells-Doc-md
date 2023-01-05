---
title: Finden Sie heraus, ob der Zellenwert mit einem einfachen Anführungszeichen beginnt
type: docs
weight: 610
url: /de/java/find-if-the-cell-value-starts-with-single-quote-mark/
---
{{% alert color="primary" %}} 

 Aspose.Cells bietet jetzt die[Style.QuotePräfix](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) -Eigenschaft, um festzustellen, ob der Zellenwert mit einem einfachen Anführungszeichen beginnt. Vor dieser Eigenschaft gab es keine Möglichkeit, zwischen Zeichenketten wie sample und 'sample etc.

{{% /alert %}} 
## **Finden Sie heraus, ob der Zellenwert mit einem einfachen Anführungszeichen beginnt**
Der folgende Beispielcode erklärt, dass die Zeichenfolgen wie sample und 'sample nicht mit unterschieden werden können[Cell.StringValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue) Eigentum. Deshalb müssen wir verwenden[Style.QuotePräfix](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix)Eigenschaft, sie zu unterscheiden.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-DetectCellValueStartsWithSingleQuote.java" >}}
