---
title: Change the HTML Link Target Type
type: docs
weight: 320
url: /python-net/change-the-html-link-target-type/
description: This topic shows you how to change the HTML Link Target Type using Aspose.Cells for Python via .NET.
keywords: Change the HTML Link Target Type, blank target type, parent target type, top target type, self target type.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET allows you to change the HTML link target type. The HTML link looks like this:

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

As you can see, the target attribute in the above HTML link is **_self**. You can control this target attribute using the [**HtmlSaveOptions.link_target_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/link_target_type/) property. This property takes the [**HtmlLinkTargetType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmllinktargettype) enum, which has the following values.

- HtmlLinkTargetType.BLANK
- HtmlLinkTargetType.PARENT
- HtmlLinkTargetType.SELF
- HtmlLinkTargetType.TOP

{{% /alert %}}

The following code illustrates the usage of the [**HtmlSaveOptions.link_target_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/link_target_type/) property. It changes the link target type to **BLANK**; by default, it is **PARENT**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ChangeHtmlLinkTarget-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
