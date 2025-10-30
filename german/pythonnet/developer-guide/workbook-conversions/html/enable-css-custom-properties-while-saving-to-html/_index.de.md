---
title: CSS benutzerdefinierte Eigenschaften beim Speichern in HTML mit Python.NET aktivieren
linktitle: CSS Benutzerdefinierte Eigenschaften beim Speichern in HTML aktivieren
type: docs
weight: 320
url: /de/python-net/enable-css-custom-properties-while-saving-to-html/
description: Erfahren Sie, wie Sie CSS benutzerdefinierte Eigenschaften beim Speichern von Excel Dateien in HTML mit Aspose.Cells für Python via .NET API aktivieren.
---

## **Mögliche Verwendungsszenarien**

Wenn Sie Ihre Excel-Datei in HTML speichern, kann die Verwendung der [**HtmlSaveOptions.enable_css_custom_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/enable_css_custom_properties/)-Eigenschaft dazu führen, dass bei mehreren Vorkommen eines Base64-basierten Bildes das Bild nur einmal gespeichert wird. Dies verbessert die Leistung des resultierenden HTML-Dokuments. Verwenden Sie das Attribut [**HtmlSaveOptions.enable_css_custom_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/enable_css_custom_properties/) und setzen Sie es auf **True**, wenn Sie in HTML speichern.

![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg)

## **Aktivieren Sie CSS Standard-Eigenschaften beim Speichern in HTML**

Das folgende Beispiel zeigt die Verwendung des [**HtmlSaveOptions.enable_css_custom_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/enable_css_custom_properties/)-Attributs. Das Bildschirmfoto zeigt den Effekt, wenn diese Eigenschaft nicht auf True gesetzt ist. Laden Sie die [Beispiel-Excel-Datei](50528260.xlsx), die in diesem Code verwendet wird, sowie die generierte [HTML-Ausgabe](50528261.zip) zur Referenz herunter.

## **Beispielcode**

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
