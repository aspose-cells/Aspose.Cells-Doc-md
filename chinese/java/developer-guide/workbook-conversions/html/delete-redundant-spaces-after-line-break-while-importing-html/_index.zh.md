---
title: 导入HTML时删除换行后多余空格
type: docs
weight: 620
url: /zh/java/delete-redundant-spaces-after-line-break-while-importing/
---

{{% alert color="primary" %}} 

请使用[HtmlLoadOptions.DeleteRedundantSpaces](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#DeleteRedundantSpaces)属性，并将其设置为**true**以删除换行标记后的所有多余空格。默认情况下，此属性为**false**，并且输出的Excel文件中保留了多余的空格。

{{% /alert %}} 
## **将HtmlLoadOptions.DeleteRedundantSpaces属性设置为false和true的效果**
以下截图显示了将此属性设置为**false**和**true**的效果。

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)
## **在导入HTML时删除换行后的多余空格**
以下示例代码显示了[HtmlLoadOptions.DeleteRedundantSpaces](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#DeleteRedundantSpaces)属性的用法。请将其设置为**true**或**false**，以获得上述截图中显示的输出。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-DeleteRedundantSpacesFromHtml-1.java" >}}
