---
title: Ändra HTML länkmåltyp
type: docs
weight: 320
url: /sv/net/change-the-html-link-target-type/
---
{{% alert color="primary" %}}

Aspose.Cells låter dig ändra HTML länkmåltyp. HTML länken ser ut så här

{{< highlight "java" >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Som du kan se är target-attributet i länken ovan HTML **_self**. Du kan styra detta målattribut med egenskapen [**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype). Den här egenskapen tar [**HtmlLinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmllinktargettype) enum som har följande värden.

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

 Följande kod illustrerar användningen av[**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype) fast egendom. Det ändrar länkmåltypen till**tom**. Som standard är det**förälder**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ChangeHtmlLinkTarget-1.cs" >}}
