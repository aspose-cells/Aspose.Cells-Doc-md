---
title: Habilitar Propiedades Personalizadas de CSS al guardar en HTML con Python.NET
linktitle: Habilitar Propiedades Personalizadas de CSS al guardar en HTML
type: docs
weight: 320
url: /es/python-net/enable-css-custom-properties-while-saving-to-html/
description: Aprende cómo habilitar propiedades personalizadas de CSS al guardar archivos Excel en HTML usando Aspose.Cells para Python via .NET API.
---

## **Escenarios de uso posibles**

Cuando guardas tu archivo Excel en HTML, en escenarios donde hay múltiples ocasiones de una misma imagen en base64, usar propiedades personalizadas de CSS permite que los datos de la imagen se guarden solo una vez. Esto mejora el rendimiento del HTML resultante. Usa el atributo [**HtmlSaveOptions.enable_css_custom_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/enable_css_custom_properties/) y configúralo en **True** al guardar en HTML.

![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg)

## **Habilitar Propiedades Personalizadas de CSS al guardar en HTML**

El siguiente código de ejemplo demuestra el uso del atributo [**HtmlSaveOptions.enable_css_custom_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/enable_css_custom_properties/). La captura de pantalla muestra el efecto cuando esta propiedad no está configurada en True. Descarga el [archivo Excel de ejemplo](50528260.xlsx) utilizado en este código y el [HTML de salida](50528261.zip) generado para referencia.

## **Código de muestra**

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
