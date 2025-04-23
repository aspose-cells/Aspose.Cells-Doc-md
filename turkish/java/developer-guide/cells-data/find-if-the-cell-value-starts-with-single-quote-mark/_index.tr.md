---
title: Hücre değerinin tek tek tırnak işaretiyle başlayıp başlamadığını bul
type: docs
weight: 610
url: /tr/java/find-if-the-cell-value-starts-with-single-quote-mark/
---

{{% alert color="primary" %}} 

Aspose.Cells artık hücre değerinin önce tek tırnak işaretiyle başlayıp başlamadığını bulmak için [Style.QuotePrefix](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) özelliğini sağlar. Bu özelliğin öncesinde, örnek ve 'örnek gibi dizgiler arasında ayrım yapmanın bir yolu yoktu.

{{% /alert %}} 
## **Hücre Değerinin Tek Tırnak İşareti ile Başlayıp Başlamadığını Bulma**
Aşağıdaki örnek kod, dizgilerin örnek ve 'örnek gibi ayrıştırılmasının [Cell.StringValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue) özelliğiyle mümkün olmadığını açıklar. Bu nedenle [Style.QuotePrefix](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) özelliğini kullanarak ayrıştırmamız gerekmektedir.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-DetectCellValueStartsWithSingleQuote.java" >}}
{{< app/cells/assistant language="java" >}}
