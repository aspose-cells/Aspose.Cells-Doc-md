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

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReuseStyleObjects-ReuseStyleObjects.java" >}}

The same process as discussed above could also be accomplished as follow.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReuseStyleObjects2.java" >}}

{{% alert color="primary" %}}

Because the [**Cell.getStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle()) and [**Cell.setStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle(com.aspose.cells.Style)) methods use a lot less memory and are efficient, the older *Cell.getStyle()* property which consumed a lot of unnecessary memory, was removed with the release of *Aspose.Cells 7.1.0*.

{{% /alert %}}
