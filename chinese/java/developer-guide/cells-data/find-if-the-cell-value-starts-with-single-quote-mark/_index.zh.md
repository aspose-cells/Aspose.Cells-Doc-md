---
title: 查找单元格值是否以单引号开始
type: docs
weight: 610
url: /zh/java/find-if-the-cell-value-starts-with-single-quote-mark/
---

{{% alert color="primary" %}} 

Aspose.Cells现在提供了Style.QuotePrefix属性，用于查找单元格值是否以单引号开始。在添加此属性之前，没有办法区分例如样本和'样本等字符串。

{{% /alert %}} 
## **查找单元格值是否以单引号开始**
以下示例代码说明，像样本和'样本这样的字符串不能通过Cell.StringValue属性进行区分。因此，我们必须使用Style.QuotePrefix属性进行区分。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-DetectCellValueStartsWithSingleQuote.java" >}}
{{< app/cells/assistant language="java" >}}
