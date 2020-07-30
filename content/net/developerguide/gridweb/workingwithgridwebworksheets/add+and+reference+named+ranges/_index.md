---
title : "Add and Reference Named Ranges" 
description : "" 
weight : 16694 
toc : false
type: docs
url: /net/developerguide/gridweb/workingwithgridwebworksheets/add+and+reference+named+ranges/
---

# Aspose.Cells for .NET : Add and Reference Named Ranges


Normally, column and row labels are used to uniquely refer to cells. But you can create descriptive names to represent cells, ranges of cells, formulas, or constant values. The word **Name** may refer to a string of characters that represents a cell, range of cells, formula, or constant value. For example, use easy-to-understand names, such as Products, to refer to hard to understand ranges, such as Sales!C20:C30. Labels can be used in formulas that refer to data on the same worksheet; if you want to represent a range on another worksheet, you may use a name. **Named ranges** is one of the most powerful features of Microsoft Excel. Users can assign a name to a range and use that name in formulas. Aspose.Cells.GridWeb supports this feature.

## Adding/Referencing Named Ranges in Formulas

The GridWeb control provides two classes (`GridName` and `GridNameCollection`) for working with named ranges. The following code snippet will help you understand how to create the Named Range and access it in the formulas.

