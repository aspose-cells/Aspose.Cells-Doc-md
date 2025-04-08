---
title: Get DrawObject and Bound while Rendering to PDF using DrawObjectEventHandler Class with Python via .NET
linktitle: Get DrawObject and Bound
type: docs
weight: 70
url: /python-net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
description: Learn how to retrieve DrawObject and bounds during Excel to PDF conversion using Python via .NET with Aspose.Cells' event handling capabilities.
---

## **Possible Usage Scenarios**

Aspose.Cells provides an abstract class [**DrawObjectEventHandler**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/drawobjecteventhandler) which has a [**draw()**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/drawobjecteventhandler/draw/) method. Users can implement [**DrawObjectEventHandler**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/drawobjecteventhandler) and utilize the [**draw()**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/drawobjecteventhandler/draw/) method to get the [**DrawObject**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/drawobject) and bounds while rendering Excel to PDF or images. Here are the parameters of the [**draw()**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/drawobjecteventhandler/draw/) method:

- `draw_object`: [**DrawObject**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/drawobject) initialized and returned during rendering
- `x`: Left position of the object
- `y`: Top position of the object
- `width`: Width of the object
- `height`: Height of the object

When rendering to PDF, use [**PdfSaveOptions.draw_object_event_handler**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/). For image rendering, use [**ImageOrPrintOptions.draw_object_event_handler**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/).

## **Get DrawObject and Bound while Rendering to PDF**

The following code demonstrates how to:
1. Load a [sample Excel file](64716821.xlsx)
2. Convert it to [output PDF](64716822.pdf) 
3. Capture object bounds and properties during rendering

The custom handler prints:
- Cell bounds and values for cell objects
- Shape bounds and names for image objects

```python
import aspose.cells as ac
from aspose.cells.rendering import DrawObject, DrawObjectEventHandler

class CustomEventHandler(DrawObjectEventHandler):
    def draw(self, draw_object, x, y, width, height):
        if draw_object.type == ac.rendering.DrawObjectType.CELL:
            print(f"[X]: {x} [Y]: {y} [Width]: {width} [Height]: {height} [Cell Value]: {draw_object.cell.string_value}")
        elif draw_object.type == ac.rendering.DrawObjectType.IMAGE:
            print(f"[X]: {x} [Y]: {y} [Width]: {width} [Height]: {height} [Shape Name]: {draw_object.image_source.name}")
        print("----------------------")

# Load sample workbook
wb = ac.Workbook("64716821.xlsx")

# Configure PDF save options with custom handler
options = ac.PdfSaveOptions()
options.draw_object_event_handler = CustomEventHandler()

# Save to PDF with object tracking
wb.save("64716822.pdf", options)
```

## **Console Output**

{{< highlight python >}}
[X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.
----------------------
[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun
----------------------
{{< /highlight >}}

```python
import os
from aspose.cells import Workbook, PdfSaveOptions
from aspose.cells.rendering import DrawObjectEventHandler, DrawObjectEnum

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET

class GetDrawObjectAndBoundUsingDrawObjectEventHandler:
    class ClsDrawObjectEventHandler(DrawObjectEventHandler):
        def draw(self, draw_object, x, y, width, height):
            print("")
            
            if draw_object.type == DrawObjectEnum.CELL:
                cell_value = draw_object.cell.string_value
                print(f"[X]: {x} [Y]: {y} [Width]: {width} [Height]: {height} [Cell Value]: {cell_value}")
            
            if draw_object.type == DrawObjectEnum.IMAGE:
                shape_name = draw_object.shape.name
                print(f"[X]: {x} [Y]: {y} [Width]: {width} [Height]: {height} [Shape Name]: {shape_name}")
            
            print("----------------------")

    @staticmethod
    def run():
        # Load sample Excel file
        wb = Workbook("sampleGetDrawObjectAndBoundUsingDrawObjectEventHandler.xlsx")
        
        # Specify Pdf save options
        opts = PdfSaveOptions()
        
        # Assign the instance of DrawObjectEventHandler class
        opts.draw_object_event_handler = GetDrawObjectAndBoundUsingDrawObjectEventHandler.ClsDrawObjectEventHandler()
        
        # Save to Pdf format with Pdf save options
        wb.save("outputGetDrawObjectAndBoundUsingDrawObjectEventHandler.pdf", opts)
```