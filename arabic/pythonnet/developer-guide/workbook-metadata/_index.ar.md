---
title: باستخدام Metadata دفتر العمل مع Python.NET
linktitle: بيانات السجل الحصري
type: docs
weight: 320
url: /ar/python-net/using-workbookmetadata/
description: تعلم كيفية إدارة بيانات وصف دفتر العمل بكفاءة باستخدام Aspose.Cells لبايثون via .NET API.
---

{{% alert color="primary" %}}

تسمح Aspose.Cells لك بتحميل نسخة خفيفة من سجل العمل إلى الذاكرة لتحرير معلومات السجل الوصفية. يرجى استخدام الفئة [**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata) لتحميل السجل.

{{% /alert %}}

يستخدم الكود العيني التالي فئة [**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata) لتحرير خصائص الوثيقة المخصصة للسجل. بمجرد فتح السجل باستخدام فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)، ستتمكن من قراءة خصائص الوثيقة. إليك كود العينة باستخدام الفئة [**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata).

```python
import os
from aspose.cells import Workbook
from aspose.cells.metadata import MetadataOptions, MetadataType, WorkbookMetadata

# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Open Workbook metadata
options = MetadataOptions(MetadataType.DOCUMENT_PROPERTIES)
meta = WorkbookMetadata(os.path.join(data_dir, "Sample1.xlsx"), options)

# Set some properties
meta.custom_document_properties.add("test", "test")

# Save the metadata info
meta.save(os.path.join(data_dir, "Sample2.out.xlsx"))

# Open the workbook
w = Workbook(os.path.join(data_dir, "Sample2.out.xlsx"))

# Read document property
print(w.custom_document_properties.get("test"))

print("Press any key to continue...")
```

