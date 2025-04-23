---
title: Ändern Sie den HTML Linkzieltyp
type: docs
weight: 450
url: /de/java/change-the-html-link-target-type/
---

{{% alert color="primary" %}} 

Aspose.Cells ermöglicht es Ihnen, den HTML-Link-Zieltyp zu ändern. Ein HTML-Link sieht so aus :

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Wie Sie sehen können, ist das target-Attribut im obigen HTML-Link **_self**. Sie können dieses target-Attribut mithilfe der [HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType)-Eigenschaft steuern. Diese Eigenschaft nimmt das [HtmlLinkTargetType](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlLinkTargetType)-Enum, das die folgenden Werte enthält.

- [BLANK](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#BLANK)
- [PARENT](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#PARENT)
- [SELF](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#SELF)
- [TOP](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#TOP)

{{% /alert %}} 
## **Ändern Sie den HTML-Link-Zieltyp**
Der folgende Code veranschaulicht die Verwendung der [HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType)-Eigenschaft. Er ändert den Link-Zieltyp auf **_blank**. Standardmäßig ist es **_parent**. Sie können die [Ausgangs-Excel-Datei](5472932.xlsx) von diesem Link erhalten, jedoch können Sie jede Excel-Datei verwenden, die einen HTML-Hyperlink enthält, um diesen Code auszuführen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeHTMLLinkTargetType-ChangeHTMLLinkTargetType.java" >}}
{{< app/cells/assistant language="java" >}}
