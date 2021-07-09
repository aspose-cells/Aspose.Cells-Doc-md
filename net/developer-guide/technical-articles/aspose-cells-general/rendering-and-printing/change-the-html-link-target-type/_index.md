---
title: Change the HTML Link Target Type
type: docs
weight: 320
url: /net/change-the-html-link-target-type/
---

{{% alert color="primary" %}}

Aspose.Cells allows you to change the HTML link target type. HTML link looks like this

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

As you can see the target attribute in the above HTML link is **_self**. You can control this target attribute using the [**HtmlSaveOptions.LinkTargetType**](https://apireference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype) property. This property takes the [**HtmlLinkTargetType**](https://apireference.aspose.com/cells/net/aspose.cells/htmllinktargettype) enum which has the following values.

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

The following code illustrates the usage of [**HtmlSaveOptions.LinkTargetType**](https://apireference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype) property. It changes the link target type to **blank**. By default, it is the **parent**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ChangeHtmlLinkTarget-1.cs" >}}
