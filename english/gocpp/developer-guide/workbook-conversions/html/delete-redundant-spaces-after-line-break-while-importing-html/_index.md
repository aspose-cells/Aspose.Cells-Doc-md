---
title: Delete redundant spaces after line break while importing HTML with Golang via C++
linktitle: Delete redundant spaces after line break while importing HTML
type: docs
weight: 20
url: /go-cpp/delete-redundant-spaces-after-line-break-while-importing/
description: Learn how to delete redundant spaces after line breaks while importing HTML using Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Please use [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getdeleteredundantspaces/) property and set it **true** to delete all the redundant spaces coming after the line break tag. By default, this property is **false** and redundant spaces are preserved in the output Excel files.

{{% /alert %}}

## Effect of setting the HTMLLoadOptions.DeleteRedundantSpaces property to false and true

The following screenshot shows the effect of setting this property to **false** and **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## Delete redundant spaces after line break while importing HTML

### Programming Sample

The following sample code shows the usage of the [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getdeleteredundantspaces/) property. Please set it **true** or **false** to get the output as shown in the above screenshot.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteRedundantSpacesAfterLineBreakWhileImportingHtml.go" >}}