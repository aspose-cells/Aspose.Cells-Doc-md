---
title: Ändra typen av HTML länkens mål med Golang via C++
linktitle: Ändra HTML länkens målknapptype
type: docs
weight: 320
url: /sv/go-cpp/change-the-html-link-target-type/
description: Lär dig hur man ändrar HTML länkmålstyp med Aspose.Cells for C++. Kontrollera mål attributet i HTML länkar programatiskt.
---

{{% alert color="primary" %}}

Aspose.Cells tillåter dig att ändra målet för HTML-länken. HTML-länken ser ut så här

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Som du kan se är målattributet i ovanstående HTML-länk **_self**. Du kan kontrollera det här målattributet med hjälp av egenskapen [**GetLinkTargetType()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getlinktargettype/). Den här egenskapen tar [**HtmlLinkTargetType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmllinktargettype/) uppräkningen som har följande värden.

- HtmlLinkTargetType::Blank
- HtmlLinkTargetType::Parent
- HtmlLinkTargetType::Self
- HtmlLinkTargetType::Top

{{% /alert %}}

Följande kod illustrerar användningen av egenskapen [**GetLinkTargetType()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getlinktargettype/). Den ändrar länkens måltyp till **blank**. Som standard är det **parent**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeTheHtmlLinkTargetType.go" >}}
