---
title: 更改HTML链接的目标类型
type: docs
weight: 450
url: /zh/java/change-the-html-link-target-type/
---

{{% alert color="primary" %}} 

Aspose.Cells 允许您更改 HTML 链接的目标类型。HTML 链接如下所示：

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

如您所见，上述 HTML 链接中的目标属性为 **_self**。您可以使用 [HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType) 属性来控制此目标属性。该属性使用 [HtmlLinkTargetType](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlLinkTargetType) 枚举，该枚举具有以下值。

- [BLANK](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#BLANK)
- [PARENT](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#PARENT)
- [SELF](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#SELF)
- [TOP](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#TOP)

{{% /alert %}} 
## **更改 HTML 链接的目标类型**
以下代码说明了 [HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType) 属性的用法。它将链接的目标类型更改为 **blank**。默认情况下为 **parent**。您可以从此链接获取[源 Excel 文件](5472932.xlsx)，但您可以使用包含 HTML 超链接的任何 Excel 文件来运行此代码。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeHTMLLinkTargetType-ChangeHTMLLinkTargetType.java" >}}
{{< app/cells/assistant language="java" >}}
