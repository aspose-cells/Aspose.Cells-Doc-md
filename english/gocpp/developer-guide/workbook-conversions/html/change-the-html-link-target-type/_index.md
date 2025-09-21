---
title: Change the HTML Link Target Type with Golang via C++
linktitle: Change the HTML Link Target Type
type: docs
weight: 320
url: /go-cpp/change-the-html-link-target-type/
description: Learn how to change the HTML link target type using Aspose.Cells for C++. Control the target attribute in HTML links programmatically.
---

{{% alert color="primary" %}}

Aspose.Cells allows you to change the HTML link target type. HTML link looks like this

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

As you can see the target attribute in the above HTML link is **_self**. You can control this target attribute using the [**GetLinkTargetType()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getlinktargettype/) property. This property takes the [**HtmlLinkTargetType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmllinktargettype/) enum which has the following values.

- HtmlLinkTargetType::Blank
- HtmlLinkTargetType::Parent
- HtmlLinkTargetType::Self
- HtmlLinkTargetType::Top

{{% /alert %}}

The following code illustrates the usage of [**GetLinkTargetType()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getlinktargettype/) property. It changes the link target type to **blank**. By default, it is the **parent**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeTheHtmlLinkTargetType.go" >}}