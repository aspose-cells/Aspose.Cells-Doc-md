---
title: Enable CSS Custom Properties while saving to HTML with Python.NET
linktitle: Enable CSS Custom Properties while saving to HTML
type: docs
weight: 320
url: /python-net/enable-css-custom-properties-while-saving-to-html/
description: Learn how to enable CSS custom properties when saving Excel files to HTML using Aspose.Cells for Python via .NET API.
---

## **Possible Usage Scenarios**

When you save your Excel file to HTML, for scenarios where there are multiple occurrences of one base64 image, using CSS custom properties allows the image data to be saved only once. This improves the performance of the resultant HTML. Use the [**HtmlSaveOptions.enable_css_custom_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/enable_css_custom_properties/) attribute and set it to **True** while saving to HTML.

![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg)

## **Enable CSS Custom Properties while saving to HTML**

The following sample code demonstrates using the [**HtmlSaveOptions.enable_css_custom_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/enable_css_custom_properties/) attribute. The screenshot shows the effect when this property is not set to True. Download the [sample Excel file](50528260.xlsx) used in this code and the [output HTML](50528261.zip) generated for reference.

## **Sample Code**

```python
import os
from aspose.cells import Workbook, HtmlSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "source")
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")

# Load sample workbook
wb = Workbook(os.path.join(source_dir, "sampleEnableCssCustomProperties.xlsx"))

# Configure HTML save options
opts = HtmlSaveOptions()
opts.export_images_as_base64 = True
opts.enable_css_custom_properties = True

# Save the workbook in HTML
wb.save(os.path.join(output_dir, "outputEnableCssCustomProperties.html"), opts)
```
{{< app/cells/assistant language="python-net" >}}