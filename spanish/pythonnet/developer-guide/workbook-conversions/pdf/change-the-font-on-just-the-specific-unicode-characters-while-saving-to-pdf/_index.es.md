---
title: Cambiar la fuente en caracteres Unicode específicos al guardar en PDF con Python.NET
linktitle: Cambiar la fuente en caracteres Unicode específicos
type: docs
weight: 260
url: /es/python-net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Aprende cómo modificar las fuentes para caracteres Unicode específicos durante la conversión a PDF usando Aspose.Cells para Python via .NET. Asegura una renderización precisa del texto con sustitución de fuentes a nivel de carácter.
---

{{% alert color="primary" %}}

 Algunos caracteres Unicode no son visualizables con fuentes especificadas por el usuario. Uno de esos caracteres Unicode es el **Guion no separable** (U+2011) con número Unicode 8209. Este carácter no puede mostrarse con **Times New Roman** pero puede ser visible con fuentes como **Arial Unicode MS**.

 Cuando estos caracteres aparecen en un texto formateado con una fuente específica (por ejemplo, Times New Roman), Aspose.Cells cambia automáticamente la fuente de toda la palabra/frase a una compatible (por ejemplo, Arial Unicode MS). Para quienes desean cambiar solo la fuente del carácter no renderizable, ofrecemos control granular mediante la propiedad **PdfSaveOptions.is_font_substitution_char_granularity**.

{{% /alert %}}

## ** Comparación de ejemplos**

 Las capturas de pantalla a continuación demuestran resultados con diferentes configuraciones. El primer PDF muestra sustitución completa de fuente del texto, mientras que el segundo PDF solo cambia la fuente del carácter específico.

|**Sustitución total de texto**|**Sustitución a nivel de carácter**|
| :- | :- |
|![Cambio completo de fuente](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|![Cambio selectivo de fuente](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|

## ** Pasos para la implementación**

 Para habilitar la sustitución de fuente a nivel de carácter:

1. Crea un objeto [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/)
2. Accede a las celdas de la hoja de trabajo usando la propiedad [**Worksheet.cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/)
3. Establece los valores de celda que contienen caracteres Unicode especiales
4. Configura [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) con:
   - `is_font_substitution_char_granularity = True`
5. Guarda el libro en formato PDF

```python
import os
from aspose.cells import Workbook, PdfSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Create workbook object
workbook = Workbook()

# Access the first worksheet
worksheet = workbook.worksheets[0]

# Access cells
cell1 = worksheet.cells.get("A1")
cell2 = worksheet.cells.get("B1")

# Set the styles of both cells to Times New Roman
style = cell1.get_style()
style.font.name = "Times New Roman"
cell1.set_style(style)
cell2.set_style(style)

# Put the values inside the cell
cell1.put_value("Hello without Non-Breaking Hyphen")
cell2.put_value("Hello" + chr(8209) + " with Non-Breaking Hyphen")

# Autofit the columns
worksheet.auto_fit_columns()

# Save to Pdf without setting PdfSaveOptions.is_font_substitution_char_granularity
workbook.save(os.path.join(data_dir, "SampleOutput_out.pdf"))

# Save to Pdf after setting PdfSaveOptions.is_font_substitution_char_granularity to true
opts = PdfSaveOptions()
opts.is_font_substitution_char_granularity = True
workbook.save(os.path.join(data_dir, "SampleOutput2_out.pdf"), opts)
```

## ** Configuración clave**

Utiliza estos componentes esenciales de la API:

- La clase [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) para configuraciones de renderizado PDF
- La propiedad **is_font_substitution_char_granularity** para sustitución de fuente a nivel de carácter
- El método [**Workbook.save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/) para generación de salida

{{% alert color="note" %}} 
**Nota de diferencia API**: En Python.NET, las propiedades booleanas usan nomenclatura snake_case (`is_font_substitution_char_granularity`) en lugar de PascalCase, que se usa en .NET.
{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
