---
title : "Reusing Style Objects" 
description : "" 
weight : 20396 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/stl-dtfmt/reusing+style+objects/
---

# Aspose.Cells for .NET : Reusing Style Objects


Reusing style objects can save memory and make a program faster.

To apply some formatting to a large range of cells in a worksheet:

1.  Create a style object.
2.  Specify the attributes.
3.  Apply the style to the cells in the range.

Because the [Cell.GetStyle](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/getstyle)/[Cell.SetStyle](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/setstyle) approach uses a lot less memory, and is efficient, the older `Cell.Style` property which consumed a lot of unnecessary memory, was removed with the release of Aspose.Cells 7.1.0.

