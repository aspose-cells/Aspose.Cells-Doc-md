---
title: Soporte para el diseño de etiquetas DIV al cargar HTML en el libro de Excel con Python via .NET
linktitle: Soporte para diseño de etiquetas DIV en importación de HTML
type: docs
weight: 50
url: /es/python-net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/
description: Aprende cómo mantener el diseño de etiquetas DIV al importar HTML en libros de Excel usando Aspose.Cells para Python via .NET. Mantén las conversiones de estructura HTML con control preciso.
---

{{% alert color="primary" %}} 

Normalmente, el diseño de las etiquetas div se ignora al cargar HTML en un objeto libro de Excel. Sin embargo, si deseas mantener el diseño de las etiquetas div, configura la propiedad [HtmlLoadOptions.support_div_tag](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/#support_div_tag) a **True**. El valor predeterminado de esta propiedad es **False**.

{{% /alert %}} 

 El siguiente código de ejemplo demuestra el uso de la propiedad [HtmlLoadOptions.support_div_tag](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/#support_div_tag). Descarga por favor el [Logotipo de Aspose](5115218.png) usado en el HTML de entrada y el [archivo Excel de salida](5115220.xlsx) generado por el código.

```python
import os
import io
from aspose.cells import Workbook, HtmlLoadOptions, LoadFormat, SaveFormat

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

export_html = f"""
<html>
<body>
    <table>
        <tr>
            <td>
                <div>This is some Text.</div>
                <div>
                    <div>
                        <span>This is some more Text</span>
                    </div>
                    <div>
                        <span>abc@abc.com</span>
                    </div>
                    <div>
                        <span>1234567890</span>
                    </div>
                    <div>
                        <span>ABC DEF</span>
                    </div>
                </div>
                <div>Generated On May 30, 2016 02:33 PM <br />Time Call Received from Jan 01, 2016 to May 30, 2016</div>
            </td>
            <td>
                <img src="{os.path.join(data_dir, 'ASpose_logo_100x100.png')}" />
            </td>
        </tr>
    </table>
</body>
</html>"""

with io.BytesIO(export_html.encode('utf-8')) as ms:
    # Specify HTML load options, support div tag layouts
    load_options = HtmlLoadOptions(LoadFormat.HTML)
    load_options.support_div_tag = True

    # Create workbook object from the html using load options
    wb = Workbook(ms, load_options)

    # Auto fit rows and columns of first worksheet
    ws = wb.worksheets[0]
    ws.auto_fit_rows()
    ws.auto_fit_columns()

    # Save the workbook in xlsx format
    output_path = os.path.join(data_dir, "DivTagsLayout_out.xlsx")
    wb.save(output_path, SaveFormat.XLSX)
```

```python
from aspose.cells import HtmlLoadOptions, Workbook, SaveFormat

# Create HTML load options and enable DIV tag support
load_options = HtmlLoadOptions()
load_options.support_div_tag = True

# Load HTML file with DIV tag layout preservation
workbook = Workbook("input.html", load_options)

# Save the workbook with preserved layout
workbook.save("output.xlsx", SaveFormat.XLSX)
```
