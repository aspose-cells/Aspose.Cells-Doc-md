---
title: Ändra HTML länkens målknapptype
type: docs
weight: 450
url: /sv/java/change-the-html-link-target-type/
---

{{% alert color="primary" %}} 

Aspose.Cells tillåter dig att ändra HTML-länkens målknapptype. HTML-länken ser ut så här:

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Som du kan se är målattributet i ovanstående HTML-länk **_self**. Du kan kontrollera detta målattribut genom att använda egenskapen [HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType). Denna egenskap tar [HtmlLinkTargetType](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlLinkTargetType)-enumet som har följande värden.

- [BLANK](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#BLANK)
- [PARENT](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#PARENT)
- [SELF](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#SELF)
- [TOP](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#TOP)

{{% /alert %}} 
## **Ändra HTML-länkens målknapptype**
Följande kod illustrerar användningen av [HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType)-egenskapen. Den ändrar länkens målknapptype till **blank**. Som standard är det **förälder**. Du kan hämta [käll excelfilen](5472932.xlsx) från den här länken, men du kan använda vilken excelfil som helst som innehåller en HTML-hyperlänk inuti den för att köra denna kod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeHTMLLinkTargetType-ChangeHTMLLinkTargetType.java" >}}
