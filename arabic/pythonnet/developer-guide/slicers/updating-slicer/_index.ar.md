---
title: تحديث العارض
linktitle: تحديث العارض
type: docs
weight: 50
url: /ar/python-net/updating-slicer/
description: تعلّم كيفية تحديث العارض لتصفية بيانات الجدول المحوري أو الجدول المرتبط باستخدام Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python إكسيل، مكتبة Python لإكسيل، تحديث العارض في Python بدون إكسيل، تصفية الجدول المحوري بواسطة العارض في Python، Slicer select_items، Slicer clear_filter.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
يعني تحديث العارض تصفية بيانات الجدول المحوري أو الجدول المرتبط بالعارض. عندما تقوم بتحديد عناصر العارض أو إلغاء تحديدها في Microsoft Excel، يُعاد حساب الجدول المحوري أو الجدول المرتبط وفقًا لذلك. باستخدام Aspose.Cells for Python via .NET، لا تحتاج إلى المرور على عناصر ذاكرة التخزين المؤقت للعارض وتحديث العارض يدويًا — تقوم طريقة [**Slicer.select_items(labels, append)**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicer/selectitems/) بتحديث العارض وإعادة حساب الجدول المحوري أو الجدول المرتبط مباشرةً من عناصر التصفية:
- `Slicer.select_items(labels, append)` — تحدد التسميات المطلوبة وتعيد حساب الجدول المحوري أو الجدول المرتبط. عندما تكون قيمة `append` هي `True`، يتم الاحتفاظ بالتسميات المحددة في الأصل وتُضاف التسميات المطلوبة إلى التحديد؛ وعندما تكون قيمة `append` هي `False`، يتم مسح جميع التحديدات الأصلية وتبقى التسميات المطلوبة فقط محددة.
- `Slicer.unselect_items(labels)` — تلغي تحديد جزء من العناصر المحددة حاليًا.
- `Slicer.clear_filter()` — تزيل التصفية وتحدد جميع العناصر.

{{% alert color="primary" %}}
بدءًا من Aspose.Cells for Python via .NET 26.10، أصبحت خاصية `SlicerCacheItem.selected` للقراءة فقط ولم يعد تعيين قيمتها مدعومًا. استخدم الطرق `Slicer.select_items` و`Slicer.unselect_items` و`Slicer.clear_filter` بدلاً من تعيين `SlicerCacheItem.selected` عنصرًا بعنصر.
{{% /alert %}}

## **كيفية تحديث العارض باستخدام مكتبة Aspose.Cells لبايثون إكسيل**
يقوم الكود النموذجي التالي بتحميل [ملف Excel النموذجي](67338475.xlsx) الذي يحتوي على عارض موجود مرتبط بجدول محوري. يحدد عناصر "Blue" و"Pink" فقط من العارض باستخدام `Slicer.select_items(labels, False)` — يُعاد حساب الجدول المحوري مباشرةً من عناصر التصفية دون استدعاء `Slicer.refresh()` يدويًا. ثم يحفظ المصنف كـ [ملف Excel الناتج](67338476.xlsx). تُظهر لقطة الشاشة التالية تأثير الكود النموذجي على ملف Excel النموذجي. كما يمكنك أن ترى في لقطة الشاشة، يعرض الجدول المحوري العناصر المصفّاة فقط.
![todo:image_alt_text](updating-slicer_1.png)

## **الكود النموذجي**
استبدل التحديد الحالي (تبقى التسميات المطلوبة فقط محددة) وأعد حساب الجدول المحوري أو الجدول المرتبط:

```python
import aspose.cells as ac
# Load sample Excel file containing slicer.
workbook = ac.Workbook("sampleUpdatingSlicer.xlsx")
# Access first worksheet.
worksheet = workbook.worksheets[0]
# Access the first slicer inside the slicer collection.
slicer = worksheet.slicers[0]
# Select only "Blue" and "Pink"; the linked pivot table or table
# is recalculated directly from the filter items.
slicer.select_items(["Blue", "Pink"], False)
# Save the modified workbook.
workbook.save("out.xlsx")
```

احتفظ بالتسميات المحددة حاليًا وحدد عناصر إضافية:

```python
# Keep the current selection and add "Red" to it.
slicer.select_items(["Red"], True)
```

ألغِ تحديد جزء من العناصر المحددة:

```python
# Remove "Pink" from the current selection.
slicer.unselect_items(["Pink"])
```

أزل التصفية (حدد جميع العناصر):

```python
# Clear the filter; all slicer items become selected again.
slicer.clear_filter()
```

{{< app/cells/assistant language="python-net" >}}