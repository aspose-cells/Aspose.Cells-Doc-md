---
title: Renderizar líneas de cuadrícula sólidas al convertir Excel a PDF con Python.NET
linktitle: Renderizar líneas de cuadrícula sólidas
type: docs
weight: 390
url: /es/python-net/render-solid-gridline-while-converting-excel-to-pdf/
description: Aprende cómo mostrar líneas de cuadrícula sólidas durante la conversión de Excel a PDF usando Aspose.Cells para Python via .NET.

---

Para compatibilidad con versiones anteriores, Aspose.Cells renderiza las líneas de cuadrícula como líneas punteadas por defecto al convertir Excel a PDF. Sin embargo, los Excel modernos renderizan las líneas de cuadrícula como líneas sólidas hoy en día.

Con la opción [PdfSaveOptions.gridline_type](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/gridline_type/), Aspose.Cells también puede renderizar las líneas de cuadrícula como líneas sólidas.

```python
import os
from aspose.cells import Workbook, PdfSaveOptions, GridlineType

# Create an empty Workbook
wb = Workbook()

# Prepare data
worksheet = wb.worksheets[0]
worksheet.cells.get("D9").put_value("gridline")

# Enable to print gridline
worksheet.page_setup.print_gridlines = True

# Set to render gridline as solid line
pdf_save_options = PdfSaveOptions()
pdf_save_options.gridline_type = GridlineType.HAIR

# Save the pdf file with PdfSaveOptions
current_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(current_dir, "output")

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

wb.save(os.path.join(output_dir, "test_Cs.pdf"), pdf_save_options)
```

![solid-gridline.png](solid-gridline.png)
{{< app/cells/assistant language="python-net" >}}
