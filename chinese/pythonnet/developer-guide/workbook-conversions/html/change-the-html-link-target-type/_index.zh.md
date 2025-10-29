---
title: 更改HTML链接的目标类型
type: docs
weight: 320
url: /zh/python-net/change-the-html-link-target-type/
description: 此主题展示了如何使用Aspose.Cells for Python via NET更改HTML链接的目标类型
keywords: 更改HTML链接的目标类型，空链接类型，父链接类型，顶层链接类型，自身链接类型
---

{{% alert color="primary" %}}

Aspose.Cells for Python via NET允许您更改HTML链接的目标类型。HTML链接如下所示

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

如您所见，上述HTML链接中的target属性是**_self**。您可以使用[**HtmlSaveOptions.link_target_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/link_target_type/)属性来控制此target属性。此属性采用了[**HtmlLinkTargetType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmllinktargettype)枚举，其具有以下值。

- HtmlLinkTargetType.BLANK
- HtmlLinkTargetType.PARENT
- HtmlLinkTargetType.SELF
- HtmlLinkTargetType.TOP

{{% /alert %}}

以下代码说明了[**HtmlSaveOptions.link_target_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/link_target_type/)属性的用法。它将链接目标类型更改为**BLANK**。默认情况下为**PARENT**。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ChangeHtmlLinkTarget-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
