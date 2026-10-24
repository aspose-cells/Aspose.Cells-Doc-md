---
title: تحديث العارض
linktitle: تحديث العارض
type: docs
weight: 50
url: /ar/net/updating-slicer/
description: يوضح هذا المقال كيفية تحديث العارض لتصفية بيانات الجدول المحوري أو الجدول المرتبط باستخدام واجهة برمجة التطبيقات Aspose.Cells for .NET.
keywords: Aspose.Cells C# تحديث العارض، C# كيفية تغيير العارض، كيفية تصفية الجدول المحوري بواسطة العارض في C#، C# Slicer SelectItems، C# Slicer ClearFilter، C# Slicer UnselectItems.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
يعني تحديث العارض تصفية بيانات الجدول المحوري أو الجدول المرتبط بالعارض. عندما تحدد عناصر العارض أو تلغي تحديدها في Microsoft Excel، يُعاد حساب الجدول المحوري أو الجدول المرتبط وفقًا لذلك. باستخدام Aspose.Cells for .NET، لا تحتاج إلى المرور على عناصر ذاكرة التخزين المؤقت للعارض وتحديث العارض يدويًا — تقوم طريقة [**Slicer.SelectItems(string[], bool)**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/selectitems/) بتحديث العارض وإعادة حساب الجدول المحوري أو الجدول المرتبط مباشرةً من عناصر التصفية:
- `Slicer.SelectItems(labels, append)` — تحدد التسميات المطلوبة وتعيد حساب الجدول المحوري أو الجدول المرتبط. عندما تكون قيمة `append` هي `true`، يتم الاحتفاظ بالتسميات المحددة في الأصل وتُضاف التسميات المطلوبة إلى التحديد؛ وعندما تكون قيمة `append` هي `false`، يتم مسح جميع التحديدات الأصلية وتبقى التسميات المطلوبة فقط محددة.
- `Slicer.UnselectItems(labels)` — تلغي تحديد جزء من العناصر المحددة حاليًا.
- `Slicer.ClearFilter()` — تزيل التصفية وتحدد جميع العناصر.

{{% alert color="primary" %}}
بدءًا من Aspose.Cells for .NET 26.10، أصبحت خاصية `SlicerCacheItem.Selected` للقراءة فقط ولم يعد تعيين قيمتها مدعومًا. استخدم الطرق `Slicer.SelectItems` و`Slicer.UnselectItems` و`Slicer.ClearFilter` بدلاً من تعيين `SlicerCacheItem.Selected` عنصرًا بعنصر.
{{% /alert %}}

## **كيفية تحديث العارض**
يقوم الكود النموذجي التالي بتحميل [ملف Excel النموذجي](67338475.xlsx) الذي يحتوي على عارض موجود مرتبط بجدول محوري. يحدد عناصر "Blue" و"Pink" فقط من العارض باستخدام `Slicer.SelectItems(labels, false)` — يُعاد حساب الجدول المحوري مباشرةً من عناصر التصفية دون استدعاء `Slicer.Refresh()` يدويًا. ثم يحفظ المصنف كـ [ملف Excel الناتج](67338476.xlsx). تُظهر لقطة الشاشة التالية تأثير الكود النموذجي على ملف Excel النموذجي. كما يمكنك أن ترى في لقطة الشاشة، يعرض الجدول المحوري العناصر المصفّاة فقط.
![todo:image_alt_text](updating-slicer_1.png)

## **الكود النموذجي**
استبدل التحديد الحالي (تبقى التسميات المطلوبة فقط محددة) وأعد حساب الجدول المحوري أو الجدول المرتبط:

```csharp
using Aspose.Cells;
using Aspose.Cells.Slicers;
// Load sample Excel file containing slicer.
Workbook workbook = new Workbook("sampleUpdatingSlicer.xlsx");
// Access first worksheet.
Worksheet worksheet = workbook.Worksheets[0];
// Access the first slicer inside the slicer collection.
Slicer slicer = worksheet.Slicers[0];
// Select only "Blue" and "Pink"; the linked pivot table or table
// is recalculated directly from the filter items.
slicer.SelectItems(new string[] { "Blue", "Pink" }, false);
// Save the modified workbook.
workbook.Save("out.xlsx");
```

احتفظ بالتسميات المحددة حاليًا وحدد عناصر إضافية:

```csharp
// Keep the current selection and add "Red" to it.
slicer.SelectItems(new string[] { "Red" }, true);
```

ألغِ تحديد جزء من العناصر المحددة:

```csharp
// Remove "Pink" from the current selection.
slicer.UnselectItems(new string[] { "Pink" });
```

أزل التصفية (حدد جميع العناصر):

```csharp
// Clear the filter; all slicer items become selected again.
slicer.ClearFilter();
```

{{< app/cells/assistant language="csharp" >}}