---
title: Guardar archivo en objeto de respuesta con Python.NET
linktitle: Guardando archivo en objeto de respuesta
type: docs
weight: 50
url: /es/python-net/saving-file-to-response-object/
description: Aprende cómo guardar archivos de Excel directamente en flujos de respuesta HTTP usando Aspose.Cells para Python via .NET.
---

{{% alert color="primary" %}}
Aspose.Cells para Python via .NET permite la generación dinámica de archivos y su entrega directa a los navegadores de clientes. Este artículo explica diferentes enfoques para guardar archivos en flujos de respuesta.
{{% /alert %}}

## **Guardar archivo en flujo de respuesta**

### **Archivos XLS**
```python
import os
from aspose.cells import Workbook, XlsSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Load your source workbook
workbook = Workbook()

Response = None  # This would typically come from a web framework in actual usage

if Response is not None:
    # Save in Excel2003 XLS format
    save_options = XlsSaveOptions()
    # Save workbook to response stream with appropriate headers
    workbook.save(Response, save_options)
    # Set content disposition and type for inline display
    Response.set_header("Content-Disposition", "inline; filename=\"output.xls\"")
    Response.set_content_type("application/vnd.ms-excel")
    Response.end()
```

**Equivalente en Python.NET:**


### **Archivos XLSX**
```python
import os
from aspose.cells import Workbook, OoxmlSaveOptions
import io

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")
Response = None

# Load your source workbook
workbook = Workbook()

if Response is not None:
    # Save in Xlsx format
    save_options = OoxmlSaveOptions()
    buffer = io.BytesIO()
    workbook.save(buffer, save_options)
    buffer.seek(0)
    Response.set_header('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    Response.set_header('Content-Disposition', 'attachment; filename="output.xlsx"')
    Response.write(buffer.getvalue())
    Response.end()
```

**Equivalente en Python.NET:**
```python
# Using same approach as XLS example with different format
workbook.save(stream, SaveFormat.XLSX, ContentDisposition.INLINE, "report.xlsx")
```

### **Archivos PDF**
```python
import os
from aspose.cells import Workbook, PdfSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")
Response = None

# Creating a Workbook object
workbook = Workbook()

if Response is not None:
    # Save in Pdf format
    save_options = PdfSaveOptions()
    workbook.save(Response, os.path.join(data_dir, "output.pdf"), content_disposition="attachment")
    Response.end()
```

**Equivalente en Python.NET:**
```python
from Aspose.Cells import PdfSaveOptions

options = PdfSaveOptions()
workbook.save(stream, options, ContentDisposition.ATTACHMENT, "output.pdf")
```

## **Manejo de flujo en Python.NET**
```python
import os
from io import BytesIO
from aspose.cells import Workbook, SaveFormat
from fastapi import Response

async def download_excel():
    # For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "data")
    file_path = os.path.join(data_dir, "Book1.xlsx")

    # Load your source workbook
    workbook = Workbook(file_path)

    # Save the workbook to a memory stream
    stream = BytesIO()
    workbook.save(stream, SaveFormat.XLSX)
    stream.seek(0)

    # Set the content type and file name
    content_type = "application/octet-stream"
    file_name = "output.xlsx"

    # Create response with headers
    headers = {"Content-Disposition": f"attachment; filename=\"{file_name}\""}
    return Response(
        content=stream.getvalue(),
        media_type=content_type,
        headers=headers
    )
```

**Implementación en Python.NET:**
```python
def save_to_response(workbook, filename, format):
    stream = MemoryStream()
    save_format = {
        "xls": SaveFormat.EXCEL_97_TO_2003,
        "xlsx": SaveFormat.XLSX,
        "pdf": SaveFormat.PDF
    }[format]

    workbook.save(stream, save_format)
    stream.seek(0)
    return stream.ToArray()

# Usage example:
# output = save_to_response(workbook, "report", "xlsx")
# HttpResponse(output, content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
```

**Notas importantes:**
1. Usa `MemoryStream` para generación de archivos en memoria
2. Siempre restablece la posición del flujo con `seek(0)` antes de leer
3. Establece tipos MIME adecuados en las cabeceras de la respuesta
4. Para frameworks web como Django/Flask, usa los manejadores de respuesta específicos del framework
