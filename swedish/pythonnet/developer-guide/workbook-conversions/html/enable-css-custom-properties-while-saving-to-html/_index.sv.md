---
title: Aktivera CSS Anpassade Egenskaper under sparande till HTML med Python.NET
linktitle: Aktivera CSS Anpassade Egenskaper under sparande till HTML
type: docs
weight: 320
url: /sv/python-net/enable-css-custom-properties-while-saving-to-html/
description: Lär dig hur man aktiverar CSS anpassade egenskaper när du sparar Excel filer till HTML med Aspose.Cells för Python via .NET API.
---

## **Möjliga användningsscenario**

När du sparar din Excel-fil till HTML, för scenarier där samma base64-bild förekommer flera gånger, tillåter användningen av CSS anpassade egenskaper att bilddata endast sparas en gång. Detta förbättrar prestandan för den resulterande HTML:en. Använd [**HtmlSaveOptions.enable_css_custom_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/enable_css_custom_properties/)-attributet och sätt det till **True** när du sparar till HTML.

![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg)

## **Aktivera CSS Anpassade Egenskaper under sparande till HTML**

Följande exempel demonstrerar användningen av [**HtmlSaveOptions.enable_css_custom_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/enable_css_custom_properties/)-attributet. Skärmbilden visar effekten när denna egenskap inte är inställd på True. Ladda ner [exempel-Excelfilen](50528260.xlsx) som används i detta exempel och [utdata-HTML](50528261.zip) som genererats som referens.

## **Exempelkod**

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
