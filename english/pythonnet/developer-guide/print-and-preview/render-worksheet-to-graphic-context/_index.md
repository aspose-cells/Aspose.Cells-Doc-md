---
title: Render Worksheet to Graphic Context with Python.NET
linktitle: Render Worksheet to Graphic Context
type: docs
weight: 300
url: /python-net/render-worksheet-to-graphic-context/
description: Learn how to render Excel worksheets to graphic contexts using Aspose.Cells for Python via .NET.
---

{{% alert color="primary" %}}

Aspose.Cells can render worksheets to graphic contexts. The graphic context can be anything like an image file, screen, or printer. Please use one of the following methods to render worksheets to graphic contexts:

- [**sheet_render.to_image(page_index, g, x, y)**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.sheetrender/to_image/)
- [**sheet_render.to_image(page_index, g, x, y, width, height)**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.sheetrender/to_image/)

{{% /alert %}}

The following code illustrates how to use Aspose.Cells to render a worksheet to a graphic context. Executing the code will render the entire worksheet and fill the remaining empty space with blue color in the graphics context, saving the image as **OutputImage_out_.png**. You can use any source Excel file with this code. Please read the code comments for better understanding.

```python
import os
from aspose.cells import Workbook
from aspose.cells.rendering import ImageOrPrintOptions, SheetRender
from aspose.pydrawing import Bitmap, Graphics, Color
from aspose.pydrawing import Imaging

# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Create workbook object from source file
workbook = Workbook(os.path.join(data_dir, "SampleBook.xlsx"))

# Access first worksheet
worksheet = workbook.worksheets[0]

# Create empty Bitmap
bmp = Bitmap(1100, 600)

# Create Graphics Context
g = Graphics.from_image(bmp)
g.clear(Color.blue)

# Set one page per sheet to true in image or print options
opts = ImageOrPrintOptions()
opts.one_page_per_sheet = True

# Render worksheet to graphics context
sr = SheetRender(worksheet, opts)
sr.to_image(0, g, 0, 0)

# Save the graphics context image in Png format
bmp.save(os.path.join(data_dir, "OutputImage_out.png"), Imaging.ImageFormat.png)
```