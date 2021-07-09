---
title: Formatting List Object
type: docs
weight: 30
url: /pythonjava/formatting-list-object/
---

## **Formatting List Object**
A table is a series of rows and columns that contain related data managed independently from the data in other rows and columns. By default, every column in the table has filtering enabled in the header row so that you can filter or sort your list object data quickly. You can add a total row (a special row in a list that provides a selection of aggregate functions useful for working with numerical data) to the list object that provides a drop-down list of aggregate functions for each total row cell.

Aspose.Cells supports formatting List objects. For this, thee API provides the [ListObject](https://apireference.aspose.com/cells/python/asposecells.api/ListObject) and [TableStyleType](https://apireference.aspose.com/cells/python/asposecells.api/TableStyleType) classes. The [TableStyleType](https://apireference.aspose.com/cells/python/asposecells.api/TableStyleType) class contains constants that represent the built-in table styles. The following code snippet creates a new List Object and sets it table style type to [TABLE_STYLE_MEDIUM_10](https://apireference.aspose.com/cells/python/asposecells.api/tablestyletype#TABLE_STYLE_MEDIUM_10)



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-FormatListObject.py" >}}
