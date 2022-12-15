---
title: 导入 HTML 时删除换行后的多余空格
type: docs
weight: 620
url: /zh/java/delete-redundant-spaces-after-line-break-while-importing/
---
{{% alert color="primary" %}} 

请用[HtmlLoadOptions.DeleteRedundantSpaces](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#DeleteRedundantSpaces)属性并设置它**真的**删除换行标记后的所有冗余空格。默认情况下，此属性是**错误的**并且在输出的 excel 文件中保留了多余的空格。

{{% /alert %}} 
## **将 HtmlLoadOptions.DeleteRedundantSpaces 属性设置为 false 和 true 的效果**
下面的截图展示了将这个属性设置为的效果**错误的**和**真的**.

![待办事项：图像_替代_文本](delete-redundant-spaces-after-line-break-while-importing-html_1.png)
## **导入 HTML 时删除换行后的多余空格**
下面的示例代码显示了[HtmlLoadOptions.DeleteRedundantSpaces](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#DeleteRedundantSpaces)财产。请设定**真的**或者**错误的**获得如上图所示的输出。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-DeleteRedundantSpacesFromHtml-1.java" >}}
