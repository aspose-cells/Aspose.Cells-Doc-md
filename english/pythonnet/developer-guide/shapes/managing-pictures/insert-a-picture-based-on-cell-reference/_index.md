---
title: Insert a Picture Based on Cell Reference
type: docs
weight: 150
url: /python-net/insert-a-picture-based-on-cell-reference/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes you have an empty picture and need to show data or content in the picture by setting a cell reference in the Formula Bar. Aspose.Cells for Python via .NET supports this feature (Microsoft Excel 2010).

{{% /alert %}}

## Inserting a Picture Based on Cell Reference

Aspose.Cells for Python via .NET supports displaying the content of a worksheet cell in an image shape. You can link the picture to the cell that contains the data you want to display. Since the cells or cell ranges are linked to the graphic object, changes that you make to the data in those cells or ranges automatically appear in the graphic object. You can add a picture to the worksheet by calling the **add_picture** method of the **ShapeCollection** collection (encapsulated in the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) object). Specify the cell range by using the **formula** attribute of the **Picture** object.

### Code Example

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Pictures-InsertPictureCellReference-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
