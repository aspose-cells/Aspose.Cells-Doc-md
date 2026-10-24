---
title: تحديث العارض
linktitle: تحديث العارض
type: docs
weight: 60
url: /ar/python-java/updating-slicer/
description: يوضح هذا المقال كيفية تحديث العارض لتصفية بيانات الجدول المحوري أو الجدول المرتبط باستخدام واجهة برمجة التطبيقات Aspose.Cells for Python via Java.
keywords: Aspose.Cells for Python via Java تحديث العارض، تحديث العارض باستخدام Python وJava، كيفية تصفية الجدول المحوري بواسطة العارض في Python، Slicer selectItems، Slicer clearFilter، Slicer unselectItems.
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **تحديث العارض**
يعني تحديث العارض تصفية بيانات الجدول المحوري أو الجدول المرتبط بالعارض. يقوم Aspose.Cells for Python via Java بتحديث العارض وإعادة حساب الجدول المحوري أو الجدول المرتبط مباشرةً من عناصر التصفية:
- `Slicer.selectItems(labels, append)` — تحدد التسميات المطلوبة وتعيد حساب الجدول المحوري أو الجدول المرتبط. عندما تكون قيمة `append` هي `True`، يتم الاحتفاظ بالتسميات المحددة في الأصل وتُضاف التسميات المطلوبة إلى التحديد؛ وعندما تكون قيمة `append` هي `False`، يتم مسح جميع التحديدات الأصلية وتبقى التسميات المطلوبة فقط محددة.
- `Slicer.unselectItems(labels)` — تلغي تحديد جزء من العناصر المحددة حاليًا.
- `Slicer.clearFilter()` — تزيل التصفية وتحدد جميع العناصر.

{{% alert color="primary" %}}
بدءًا من Aspose.Cells for Python via Java 26.10، أصبحت خاصية `SlicerCacheItem.Selected` للقراءة فقط ولم يعد تعيين قيمتها مدعومًا. استخدم الطرق `Slicer.selectItems` و`Slicer.unselectItems` و`Slicer.clearFilter` بدلاً من تعيين `SlicerCacheItem.Selected` عنصرًا بعنصر.
يقوم الكود النموذجي التالي بتحميل [ملف Excel النموذجي](106365050.xlsx) يحتوي على عارض مرتبط بجدول محوري. تحدد عناصر "Blue" و"Pink" فقط من العارض باستخدام `Slicer.selectItems(labels, False)` — يُعاد حساب الجدول المحوري مباشرةً من عناصر التصفية دون استدعاء `Slicer.refresh()` يدويًا. ثم يحفظ المصنف كـ [ملف Excel الناتج](106365051.xlsx). تُظهر لقطة الشاشة التالية تأثير الكود النموذجي على ملف Excel النموذجي. كما يمكنك أن ترى في لقطة الشاشة، يعرض الجدول المحوري العناصر المصفّاة فقط.
![todo:image_alt_text](Updating-Slicer-using-Aspose.Cells.png)
{{% /alert %}}

## **الكود النموذجي**
استبدل التحديد الحالي (تبقى التسميات المطلوبة فقط محددة) وأعد حساب الجدول المحوري أو الجدول المرتبط:

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
# Load sample Excel file containing slicer.
workbook = Workbook("sampleUpdatingSlicer.xlsx")
# Access first worksheet.
worksheet = workbook.getWorksheets().get(0)
# Access the first slicer inside the slicer collection.
slicer = worksheet.getSlicers().get(0)
# Select only "Blue" and "Pink"; the linked pivot table or table
# is recalculated directly from the filter items.
slicer.selectItems(["Blue", "Pink"], False)
# Save the modified workbook.
workbook.save("out.xlsx")
jpype.shutdownJVM()
```

احتفظ بالتسميات المحددة حاليًا وحدد عناصر إضافية:

```python
# Keep the current selection and add "Red" to it.
slicer.selectItems(["Red"], True)
```

ألغِ تحديد جزء من العناصر المحددة:

```python
# Remove "Pink" from the current selection.
slicer.unselectItems(["Pink"])
```

أزل التصفية (حدد جميع العناصر):

```python
# Clear the filter; all slicer items become selected again.
slicer.clearFilter()
```

{{< app/cells/assistant language="python" >}}