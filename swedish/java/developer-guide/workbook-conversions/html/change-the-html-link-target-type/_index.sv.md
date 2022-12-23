---
title: Ändra HTML länkmåltyp
type: docs
weight: 450
url: /sv/java/change-the-html-link-target-type/
---
{{% alert color="primary" %}} 

Aspose.Cells låter dig ändra HTML länkmåltyp. HTML länken ser ut så här:

{{< highlight "java" >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Som du kan se är target-attributet i länken ovan HTML **_self**. Du kan styra detta målattribut med egenskapen [HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType). Den här egenskapen tar [HtmlLinkTargetType](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlLinkTargetType) enum som har följande värden.

- [TOM](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#BLANK)
- [FÖRÄLDER](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#PARENT)
- [SJÄLV](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#SELF)
- [TOPP](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#TOP)

{{% /alert %}} 
## **Ändra HTML länkmåltyp**
 Följande kod illustrerar användningen av[HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType) fast egendom. Det ändrar länkmåltypen till**tom**. Som standard är det**förälder** . Du kan få[source excel-fil](5472932.xlsx) från denna länk kan du dock använda valfri excel-fil som innehåller en HTML hyperlänk inuti den för att köra den här koden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeHTMLLinkTargetType-ChangeHTMLLinkTargetType.java" >}}
