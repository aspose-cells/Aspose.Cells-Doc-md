---
title: تحديث تلقائي لكائن OLE
type: docs
weight: 270
url: /ar/python-net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
---

{{% alert color="primary" %}}

 توفر Aspose.Cells لـ Python via .NET الخاصية [**OleObject.auto_load**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/auto_load) لتحديث عنصر OLE عندما يتم فتح ملف Excel في Microsoft Excel. بفضل هذه الخاصية، ستعرض عنصر OLE الصورة الصحيحة التي أنتجها Microsoft Excel.

{{% /alert %}}

يقوم الكود العينة التالي بتحميل [ملف الإكسل العينة](5115231.xlsx) الذي يحتوي على صورة OLE غير حقيقية. الكائن OLE هو في الواقع مستند Microsoft Word ولكن ملف الإكسل العينة يعرض صورة الحيوان بدلاً من صورة Microsoft Word. ولكن إذا فتحت [ملف الإكسل الناتج](5115225.xlsx)، سترى Microsoft Excel عرض الصورة الصحيحة لـ OLE.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-OLE-RefreshOLEObjects-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
