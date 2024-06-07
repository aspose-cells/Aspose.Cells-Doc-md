---
title: 通过 Aspose.Cells for .NET API 学习如何查找单元格值是否以单引号标记开头。
type: docs
weight: 610
url: /zh/java/find-if-the-cell-value-starts-with-single-quote-mark/
---

{{% alert color="primary" %}} 

现在Aspose.Cells提供了[Style.QuotePrefix](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix)属性，以查找单元格的值是否以单引号开始。在此属性之前，没有办法区分诸如sample和'sample之类的字符串。

{{% /alert %}} 
## **查找单元格值是否以单引号标记开始**
下面的示例代码解释了像sample和'sample之类的字符串无法通过[Cell.StringValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue)属性区分。因此，我们必须使用[Style.QuotePrefix](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix)属性来区分它们。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-DetectCellValueStartsWithSingleQuote.java" >}}
