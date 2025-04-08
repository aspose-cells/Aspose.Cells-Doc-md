---
title: Generate Thumbnail of the Worksheet with Python via .NET
linktitle: Generate Thumbnail of the Worksheet
type: docs
weight: 110
url: /python-net/generate-thumbnail-of-the-worksheet/
description: Learn how to generate worksheet thumbnails as images using Aspose.Cells for Python via .NET API for document previews and web applications.
keywords: Python Excel Thumbnail, Worksheet to Image Python, Generate Worksheet Preview Python, Aspose.Cells Python Thumbnail
---

{{% alert color="primary" %}} 

It can be useful to generate thumbnails from worksheets. A thumbnail is a small image that can be pasted into a Word document or a PowerPoint presentation to give a preview of what's on the worksheet. It can be added to a webpage with a link to download the original document and has a host of other uses.

{{% /alert %}} 

Aspose.Cells for Python via .NET allows you to output worksheets to image files, making thumbnail generation straightforward. The sample code below demonstrates how to output worksheets to image files:

```python
import clr
clr.AddReference("Aspose.Cells")
clr.AddReference("System.Drawing")

from Aspose.Cells import Workbook, ImageOrPrintOptions, SheetRender
from System.Drawing import Bitmap

# Instantiate a new workbook
workbook = Workbook("input.xlsx")

# Get the first worksheet
worksheet = workbook.worksheets[0]

# Create image options
img_options = ImageOrPrintOptions()
img_options.set_desired_size(100, 100)  # Set thumbnail size
img_options.vertical_resolution = 300
img_options.horizontal_resolution = 300

# Create sheet render
sheet_render = SheetRender(worksheet, img_options)

# Save thumbnail image
sheet_render.to_image(0, "thumbnail.png")
```

```python
import os
from aspose.cells import Workbook, ImageOrPrintOptions, ImageType, SheetRender
from aspose.pydrawing import Bitmap, Graphics

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
# Source directory
current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, "source")
output_dir = os.path.join(current_dir, "output")

# Instantiate and open an Excel file
book = Workbook(os.path.join(source_dir, "sampleGenerateThumbnailOfWorksheet.xlsx"))

# Define ImageOrPrintOptions
img_options = ImageOrPrintOptions()

# Specify the image format
img_options.image_type = ImageType.JPEG

# Set the vertical and horizontal resolution
img_options.vertical_resolution = 200
img_options.horizontal_resolution = 200

# One page per sheet is enabled
img_options.one_page_per_sheet = True

# Get the first worksheet
sheet = book.worksheets[0]

# Render the sheet with respect to specified image/print options
sr = SheetRender(sheet, img_options)

# Render the image for the sheet
bmp = sr.to_image(0)

# Create a bitmap
thumb = Bitmap(600, 600)

# Get the graphics for the bitmap
gr = Graphics.from_image(thumb)

if bmp is not None:
    # Draw the image
    gr.draw_image(bmp, 0, 0, 600, 600)

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Save the thumbnail
thumb.save(os.path.join(output_dir, "outputGenerateThumbnailOfWorksheet.bmp"))
```

**Key modifications:**
- Added Python.NET imports for CLR and System.Drawing
- Converted PascalCase method names to snake_case (SetDesiredSize → set_desired_size)
- Removed explicit type declarations in favor of Python's dynamic typing
- Used Python-style object instantiation
- Maintained original technical parameters (resolution, image size)
- Updated API references to Python.NET conventions
- Added proper path handling (though original example uses simple filename)