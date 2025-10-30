---
title: Desactivar CSS al Guardar en HTML con Python.NET
linktitle: Desactivar CSS al Guardar en HTML
type: docs
weight: 320
url: /es/python-net/disable-css-while-saving-to-html/
description: Aprende cómo desactivar los estilos CSS al guardar archivos Excel en formato HTML usando Aspose.Cells para Python via .NET API.
---

## **Escenarios de uso posibles**

Cuando guardas tu archivo Excel en HTML de una sola página, generalmente los elementos CSS se integran dentro del archivo HTML y se encuentran en la sección HEAD. Si adjuntas este archivo como contenido/cuerpo de un correo electrónico, la mayoría de los clientes de correo eliminarán los elementos CSS, lo que resulta en una representación incorrecta. La API Aspose.Cells para Python via .NET introduce una opción que permite desactivar opcionalmente el CSS, permitiendo aplicar estilos directamente en los elementos HTML. Si deseas establecer el HTML como contenido/cuerpo del correo, usa la propiedad [**HtmlSaveOptions.disable_css**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_css/) y configúralo en **True**.

## **Desactivar CSS al Guardar en HTML**

El siguiente código de ejemplo muestra el uso de la propiedad [**HtmlSaveOptions.disable_css**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_css/).

## **Código de muestra**

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
