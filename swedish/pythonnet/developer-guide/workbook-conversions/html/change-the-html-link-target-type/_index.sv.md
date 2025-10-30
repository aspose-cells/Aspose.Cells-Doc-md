---
title: Ändra HTML länkens målknapptype
type: docs
weight: 320
url: /sv/python-net/change-the-html-link-target-type/
description: Denna artikel visar dig hur du ändrar HTML länkens måltyp med Aspose.Cells for Python via NET.
keywords: Ändra HTML länkens måltyp, måltyp tom, måltyp förälder, måltyp högst upp, själv måltyp.
---

{{% alert color="primary" %}}

Aspose.Cells for Python via NET tillåter dig att ändra HTML-länkens måltyp. HTML-länken ser ut så här

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Som du kan se är målattributet i ovanstående HTML-länk **_self**. Du kan kontrollera det här målattributet med hjälp av egenskapen [**HtmlSaveOptions.link_target_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/link_target_type/). Den här egenskapen tar [**HtmlLinkTargetType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmllinktargettype) uppräkningen som har följande värden.

- HtmlLinkTargetType.BLANK
- HtmlLinkTargetType.PARENT
- HtmlLinkTargetType.SELF
- HtmlLinkTargetType.TOP

{{% /alert %}}

Följande kod illustrerar användningen av egenskapen [**HtmlSaveOptions.link_target_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/link_target_type/). Den ändrar länkens måltyp till **BLANK**. Som standard är det **PARENT**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ChangeHtmlLinkTarget-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
