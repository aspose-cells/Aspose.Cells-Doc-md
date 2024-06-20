---
title: Ändra HTML länkens målknapptype
type: docs
weight: 320
url: /sv/net/change-the-html-link-target-type/
---

{{% alert color="primary" %}}

Aspose.Cells tillåter dig att ändra målet för HTML-länken. HTML-länken ser ut så här

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Som du kan se är målattributet i ovanstående HTML-länk **_self**. Du kan kontrollera det här målattributet med hjälp av egenskapen [**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype). Den här egenskapen tar [**HtmlLinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmllinktargettype) uppräkningen som har följande värden.

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

Följande kod illustrerar användningen av egenskapen [**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype). Den ändrar länkens måltyp till **blank**. Som standard är det **parent**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ChangeHtmlLinkTarget-1.cs" >}}
