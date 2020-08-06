---
title: Reusing Style Objects
type: docs
weight: 60
url: /java/reusing-style-objects/
---

{{% alert color="primary" %}} 

Reusing style objects can save memory and make the program execute faster.

{{% /alert %}} 

To apply some formatting to a large range of cells in a worksheet:

1. Create a style object.
1. Specify the attributes.
1. Apply the style to the cells in the range.

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-articles-ReuseStyleObjects-ReuseStyleObjects.java" >}}

The same process as discussed above could also be accomplished as follow.

{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "ReuseStyleObjects2.java" >}}

{{% alert color="primary" %}} 

Because the [Cell.getStyle](https://apireference.aspose.com/java/cells/com.aspose.cells/cell#getStyle\(\)) and [Cell.setStyle](https://apireference.aspose.com/java/cells/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) methods use a lot less memory and are efficient, the older Cell.getStyle() property which consumed a lot of unnecessary memory, was removed with the release of Aspose.Cells 7.1.0.

{{% /alert %}}
