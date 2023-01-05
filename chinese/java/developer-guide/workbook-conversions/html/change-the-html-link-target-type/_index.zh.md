---
title: 更改 HTML 链接目标类型
type: docs
weight: 450
url: /zh/java/change-the-html-link-target-type/
---
{{% alert color="primary" %}} 

Aspose.Cells 允许您更改 HTML 链接目标类型。 HTML 链接如下所示：

{{< highlight "java" >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

可以看到上面HTML链接中的target属性是**_self**。您可以使用 [HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType) 属性控制此目标属性。此属性采用具有以下值的 [HtmlLinkTargetType](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlLinkTargetType) 枚举。

- [空白的](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#BLANK)
- [家长](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#PARENT)
- [自己](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#SELF)
- [最佳](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#TOP)

{{% /alert %}} 
## **更改 HTML 链接目标类型**
下面的代码说明了使用[HtmlSaveOptions.setLinkTargetType() 方法](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType)财产。它将链接目标类型更改为**空白的**.默认情况下，它是**父母**.你可以获得[源文件](5472932.xlsx)但是，通过此链接，您可以使用其中包含 HTML 超链接的任何 Excel 文件来运行此代码。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeHTMLLinkTargetType-ChangeHTMLLinkTargetType.java" >}}
