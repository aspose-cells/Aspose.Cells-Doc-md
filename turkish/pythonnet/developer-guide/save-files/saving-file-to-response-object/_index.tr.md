---
title: Python.NET ile Dosya Yanıt Nesnesine Kaydetme
linktitle: Yanıt Nesnesine Dosya Kaydet
type: docs
weight: 50
url: /tr/python-net/saving-file-to-response-object/
description: Aspose.Cells for Python via .NET kullanarak Excel dosyalarını doğrudan HTTP yanıt akışlarına nasıl kaydedeceğinizi öğrenin.
---

{{% alert color="primary" %}}
Aspose.Cells for Python via .NET, dinamik dosya üretimi ve doğrudan müşteri tarayıcılarına teslim edilmesini sağlar. Bu makale, dosyaları yanıt akışlarına kaydetmek için farklı yaklaşımları açıklar.
{{% /alert %}}

## **Yanıt Akışına Dosya Kaydetme**

### **XLS Dosyaları**
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

**Python.NET Eşdeğeri:**


### **XLSX Dosyaları**
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

**Python.NET Eşdeğeri:**
```python
# Using same approach as XLS example with different format
workbook.save(stream, SaveFormat.XLSX, ContentDisposition.INLINE, "report.xlsx")
```

### **PDF Dosyaları**
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

**Python.NET Eşdeğeri:**
```python
from Aspose.Cells import PdfSaveOptions

options = PdfSaveOptions()
workbook.save(stream, options, ContentDisposition.ATTACHMENT, "output.pdf")
```

## **Python.NET'te Akış Yönetimi**
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

**Python.NET Uygulaması:**
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

**Önemli Notlar:**
1. Bellek içi dosya oluşturma için `MemoryStream` kullanın
2. Okumadan önce her zaman akışın konumunu `seek(0)` ile sıfırlayın
3. Yanıt başlıklarında uygun MIME türlerini ayarlayın
4. Django/Flask gibi web çerçevesi kullanıyorsanız, çerçeveye özgü yanıt işleyicilerini kullanın
{{< app/cells/assistant language="python-net" >}}
