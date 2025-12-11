---
title: Disable CSS while Saving to HTML with Python.NET
linktitle: Disable CSS while Saving to HTML
type: docs
weight: 320
url: /python-net/disable-css-while-saving-to-html/
description: Learn how to disable CSS styles when saving Excel files to HTML format using Aspose.Cells for Python via .NET API.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

When you save your Excel file to a single-page HTML, the CSS elements are usually embedded within the HTML file and placed in the **HEAD** section. If you attach this file as the content/body of an email, most email clients will strip out the CSS elements, resulting in improper rendering. The Aspose.Cells for Python via .NET API introduces an option that allows you to optionally disable CSS, enabling styles to be applied directly within the HTML elements themselves. If you want to set the HTML as the email's content/body, please use the **HtmlSaveOptions.disable_css** property and set it to **True**.

## **Disable CSS while Saving to HTML**

The following sample code shows the usage of the **HtmlSaveOptions.disable_css** property.

## **Sample Code**

```python
import os
from aspose.cells import Workbook, HtmlSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET

# Load sample workbook
current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, "source")
output_dir = os.path.join(current_dir, "output")

wb = Workbook(os.path.join(source_dir, "sampleDisableCss.xlsx"))

# Disable CSS
opts = HtmlSaveOptions()
opts.disable_css = True

# Create output directory if it does not exist
os.makedirs(output_dir, exist_ok=True)

# Save the workbook in HTML
wb.save(os.path.join(output_dir, "outputDisable.html"), opts)
```
{{< app/cells/assistant language="python-net" >}}
