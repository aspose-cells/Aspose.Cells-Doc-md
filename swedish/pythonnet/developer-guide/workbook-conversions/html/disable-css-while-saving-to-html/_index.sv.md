---
title: Inaktivera CSS under Sparande till HTML med Python.NET
linktitle: Inaktivera CSS under Sparande till HTML
type: docs
weight: 320
url: /sv/python-net/disable-css-while-saving-to-html/
description: Lär dig hur man inaktiverar CSS stilar när du sparar Excel filer till HTML format med Aspose.Cells för Python via .NET API.
---

## **Möjliga användningsscenario**

När du sparar din Excel-fil till en HTML för en enda sida, är CSS-element vanligtvis inbäddade i HTML-filen och finns i HEAD-sektionen. Om du bifogar denna fil som innehåll/kropp i ett email kommer CSS-elementen att tas bort av de flesta emailklienter, vilket resulterar i felaktig visning. Aspose.Cells för Python via .NET API introducerar ett alternativ som tillåter dig att tillfälligt inaktivera CSS, så att stilar kan appliceras direkt på HTML-elementen själva. Om du vill använda HTML som emailens innehåll/kropp, använd då egendefinierade [**HtmlSaveOptions.disable_css**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_css/)-egenskapen och sätt den till **True**.

## **Inaktivera CSS under Sparande till HTML**

Följande exempel visar användningen av [**HtmlSaveOptions.disable_css**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_css/) egenskapen.

## **Exempelkod**

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

# Create output directory if not exists
os.makedirs(output_dir, exist_ok=True)

# Save the workbook in html
wb.save(os.path.join(output_dir, "outputDisable.html"), opts)
```
{{< app/cells/assistant language="python-net" >}}
