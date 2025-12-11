---
title: Copy Range Style Only with Golang via C++
linktitle: Copy Range Style Only
type: docs
weight: 620
url: /go-cpp/copy-range-style-only/
description: Learn how to copy only the style of a range in Excel using Aspose.Cells with Golang via C++.
---

{{% alert color="primary" %}}

[Copy Range Data Only](/cells/cpp/copy-range-data-only/) and [Copy Range Data with Style](/cells/cpp/copy-range-data-with-style/) explain how to copy data from a range to another on its own or together with formatting. It is also possible to copy only the formatting. This article shows how.

{{% /alert %}} 

This example creates a workbook, populates it with data, and copies a range's style only.

1. Create a range.  
1. Create a [**Style**](https://reference.aspose.com/cells/go-cpp/style/) object with specified formatting attributes.  
1. Apply the style formatting to the range.  
1. Create a second range of cells.  
1. Copy the first range's formatting to the second range.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyRangeStyleOnly.go" >}}