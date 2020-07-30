---
title : "Reusing Style Objects" 
description : "" 
weight : 16396 
toc : false
type: docs
url: /java/developerguide/technicalarticles/stl-dtfmt/reusing+style+objects/
---

# Aspose.Cells for Java : Reusing Style Objects


Reusing style objects can save memory and make the program execute faster.

To apply some formatting to a large range of cells in a worksheet:

1.  Create a style object.
2.  Specify the attributes.
3.  Apply the style to the cells in the range.


The same process as discussed above could also be accomplished as follow.

Because the [Cell.getStyle](https://apireference.aspose.com/java/cells/com.aspose.cells/cell#getStyle()) and [Cell.setStyle](https://apireference.aspose.com/java/cells/com.aspose.cells/cell#setStyle(com.aspose.cells.Style)) methods use a lot less memory and are efficient, the older Cell.getStyle() property which consumed a lot of unnecessary memory, was removed with the release of Aspose.Cells 7.1.0.

