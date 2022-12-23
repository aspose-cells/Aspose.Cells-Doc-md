---
title: Ändern Sie den Linkzieltyp HTML
type: docs
weight: 450
url: /de/java/change-the-html-link-target-type/
---
{{% alert color="primary" %}} 

Mit Aspose.Cells können Sie den Linkzieltyp HTML ändern. HTML Link sieht so aus:

{{< highlight "java" >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Wie Sie sehen können, ist das Zielattribut im obigen HTML-Link **_self**. Sie können dieses Zielattribut mit der Eigenschaft [HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType) steuern. Diese Eigenschaft übernimmt die Enumeration [HtmlLinkTargetType](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlLinkTargetType) mit den folgenden Werten.

- [LEER](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#BLANK)
- [ELTERNTEIL](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#PARENT)
- [SELBST](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#SELF)
- [OBEN](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#TOP)

{{% /alert %}} 
## **Ändern Sie den Linkzieltyp HTML**
 Der folgende Code veranschaulicht die Verwendung von[HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType) Eigentum. Es ändert den Zieltyp des Links in**leer**. Standardmäßig ist es die**Elternteil** . Sie können die bekommen[Excel-Quelldatei](5472932.xlsx) Von diesem Link aus können Sie jedoch jede Excel-Datei verwenden, die einen HTML-Hyperlink enthält, um diesen Code auszuführen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeHTMLLinkTargetType-ChangeHTMLLinkTargetType.java" >}}
