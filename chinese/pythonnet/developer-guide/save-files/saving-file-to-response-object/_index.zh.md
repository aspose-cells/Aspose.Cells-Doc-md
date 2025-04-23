---
title: 将文件保存到响应对象中（Python.NET）
linktitle: 将文件保存到响应对象
type: docs
weight: 50
url: /zh/python-net/saving-file-to-response-object/
description: 学习如何使用Aspose.Cells for Python via .NET将Excel文件直接保存到HTTP响应流中。
---

{{% alert color="primary" %}}
Aspose.Cells for Python via .NET支持动态文件生成并直接传递给客户端浏览器。本文介绍了不同的方法将文件保存到响应流中。
{{% /alert %}}

## **保存文件到响应流**

### **XLS文件**
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

**Python.NET 等价：**


### **XLSX文件**
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

**Python.NET 等价：**
```python
# Using same approach as XLS example with different format
workbook.save(stream, SaveFormat.XLSX, ContentDisposition.INLINE, "report.xlsx")
```

### **PDF文件**
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

**Python.NET 等价：**
```python
from Aspose.Cells import PdfSaveOptions

options = PdfSaveOptions()
workbook.save(stream, options, ContentDisposition.ATTACHMENT, "output.pdf")
```

## **Python.NET中的流处理**
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

**Python.NET 实现：**
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

**注意事项：**
1. 使用`MemoryStream`进行内存中文件生成
2. 读取前请用`seek(0)`重置流位置
3. 在响应头设置合适的MIME类型
4. 对于Django/Flask等Web框架，使用特定的响应处理器
