---
title: تحديث العارض
linktitle: تحديث العارض
type: docs
weight: 50
url: /ar/java/updating-slicer/
description: يوضح هذا المقال كيفية تحديث العارض لتصفية بيانات الجدول المحوري أو الجدول المرتبط باستخدام واجهة برمجة التطبيقات Aspose.Cells for Java.
keywords: Aspose.Cells Java تحديث العارض، Java كيفية تغيير العارض، كيفية تصفية الجدول المحوري بواسطة العارض في Java، Java Slicer selectItems، Java Slicer clearFilter، Java Slicer unselectItems.
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
يعني تحديث العارض تصفية بيانات الجدول المحوري أو الجدول المرتبط بالعارض. عندما تحدد عناصر العارض أو تلغي تحديدها في Microsoft Excel، يُعاد حساب الجدول المحوري أو الجدول المرتبط وفقًا لذلك. باستخدام Aspose.Cells for Java، لا تحتاج إلى المرور على عناصر ذاكرة التخزين المؤقت للعارض وتحديث العارض يدويًا — تقوم طريقة [Slicer.selectItems(String[], boolean)](https://reference.aspose.com/cells/java/com.aspose.cells/slicer/#selectItems-java.lang.String---boolean-) بتحديث العارض وإعادة حساب الجدول المحوري أو الجدول المرتبط مباشرةً من عناصر التصفية:
- `Slicer.selectItems(labels, append)` — تحدد التسميات المطلوبة وتعيد حساب الجدول المحوري أو الجدول المرتبط. عندما تكون قيمة `append` هي `true`، يتم الاحتفاظ بالتسميات المحددة في الأصل وتُضاف التسميات المطلوبة إلى التحديد؛ وعندما تكون قيمة `append` هي `false`، يتم مسح جميع التحديدات الأصلية وتبقى التسميات المطلوبة فقط محددة.
- `Slicer.unselectItems(labels)` — تلغي تحديد جزء من العناصر المحددة حاليًا.
- `Slicer.clearFilter()` — تزيل التصفية وتحدد جميع العناصر.

{{% alert color="primary" %}}
بدءًا من Aspose.Cells for Java 26.10، أصبحت خاصية `SlicerCacheItem.Selected` للقراءة فقط ولم يعد تعيين قيمتها مدعومًا. استخدم الطرق `Slicer.selectItems` و`Slicer.unselectItems` و`Slicer.clearFilter` بدلاً من تعيين `SlicerCacheItem.Selected` عنصرًا بعنصر.
{{% /alert %}}

## **تحديث العارض**
يقوم الكود النموذجي التالي بتحميل [ملف Excel النموذجي](67338506.xlsx) الذي يحتوي على عارض موجود مرتبط بجدول محوري. يحدد عناصر "Blue" و"Pink" فقط من العارض باستخدام `Slicer.selectItems(labels, false)` — يُعاد حساب الجدول المحوري مباشرةً من عناصر التصفية دون استدعاء `Slicer.refresh()` يدويًا. ثم يحفظ المصنف كـ [ملف Excel الناتج](67338505.xlsx). تُظهر لقطة الشاشة التالية تأثير الكود النموذجي على ملف Excel النموذجي. كما يمكنك أن ترى في لقطة الشاشة، يعرض الجدول المحوري العناصر المصفّاة فقط.
![todo:image_alt_text](updating-slicer_1.png)

## **الكود النموذجي**
استبدل التحديد الحالي (تبقى التسميات المطلوبة فقط محددة) وأعد حساب الجدول المحوري أو الجدول المرتبط:

```java
import com.aspose.cells.Workbook;
import com.aspose.cells.Worksheet;
import com.aspose.cells.Slicer;
// Load sample Excel file containing slicer.
Workbook workbook = new Workbook("sampleUpdatingSlicer.xlsx");
// Access first worksheet.
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
Slicer slicer = worksheet.getSlicers().get(0);
// Select only "Blue" and "Pink"; the linked pivot table or table
// is recalculated directly from the filter items.
slicer.selectItems(new String[] { "Blue", "Pink" }, false);
// Save the modified workbook.
workbook.save("out.xlsx");
```

احتفظ بالتسميات المحددة حاليًا وحدد عناصر إضافية:

```java
// Keep the current selection and add "Red" to it.
slicer.selectItems(new String[] { "Red" }, true);
```

ألغِ تحديد جزء من العناصر المحددة:

```java
// Remove "Pink" from the current selection.
slicer.unselectItems(new String[] { "Pink" });
```

أزل التصفية (حدد جميع العناصر):

```java
// Clear the filter; all slicer items become selected again.
slicer.clearFilter();
```

{{< app/cells/assistant language="java" >}}