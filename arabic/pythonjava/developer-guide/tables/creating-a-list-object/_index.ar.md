---
title: إنشاء كائن قائمة
type: docs
weight: 20
url: /ar/python-java/creating-a-list-object/
---

استخدام أوراق العمل يجعل من السهل العمل مع أنواع مختلفة من القوائم، على سبيل المثال. قوائم الهواتف، قوائم المهام، إلخ. تدعم Aspose.Cells إنشاء وإدارة القوائم.

## **مزايا كائن القائمة**

هناك العديد من المزايا عند تحويل قائمة البيانات إلى كائن قائمة فعلي:

- يتم تضمين صفوف وأعمدة جديدة تلقائيًا.
- يمكن بسهولة إضافة صف إجمالي في أسفل القائمة لعرض الجمع والمتوسط والعد، إلخ.
- يتم دمج الأعمدة المضافة إلى اليمين تلقائيًا في كائن القائمة.
- ستتم توسيع الرسوم البيانية استنادًا إلى الصفوف والأعمدة تلقائيًا.
- ستتم توسيع النطاقات المسماة المخصصة للصفوف والأعمدة تلقائيًا.
- تكون القائمة محمية من حذف الصف والعمود بطريق الخطأ.

## **إنشاء كائن قائمة باستخدام Microsoft Excel**

**تحديد نطاق البيانات لإنشاء كائن القائمة** 

![todo:image_alt_text](picture1.png)

يعرض ذلك مربع حوار إنشاء القائمة.

**مربع حوار إنشاء القائمة** 

![todo:image_alt_text](picture2.png)

تنفيذ كائن القائمة وتحديد الصف الإجمالي (حدد **البيانات** ثم **القائمة** تليها **الصف الإجمالي**).

**إنشاء كائن القائمة** 

![todo:image_alt_text](picture3.png)

## **إنشاء كائن قائمة باستخدام واجهة برمجة التطبيقات Aspose.Cells**

توفر Aspose.Cells فئة تُمثل ملف Excel للمايكروسوفت، الفئة [**Workbook**](https://reference.aspose.com/cells/python/asposecells.api/Workbook) تحتوي على مجموعة [**Worksheets**](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

يلوح برسالة الجدول الممثلة بالفئة [**Worksheet**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet). الفئة [**Worksheet**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet) توفر مجموعة واسعة من الخصائص والطرق لإدارة ورقة العمل. لإنشاء [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject) في ورقة العمل، استخدم خاصية مجموعة [**ListObjects**](https://reference.aspose.com/cells/python/asposecells.api/worksheet#ListObjects) من الفئة [**Worksheet**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet). يمثل كل [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)، في الواقع، كائنًا من الفئة [**ListObjectCollection**](https://reference.aspose.com/cells/python/asposecells.api/ListObjectCollection)، التي توفر بدورها الطريقة [**add**](https://reference.aspose.com/cells/python/asposecells.api/listobjectcollection#add(int,%20int,%20int,%20int,%20boolean)) لإضافة مجموعة البيانات وتحديد نطاق الخلايا للقائمة.

وفقًا لنطاق الخلايا المحدد، يتم إنشاء كائن القائمة في ورقة العمل بواسطة Aspose.Cells. استخدم السمات (على سبيل المثال، ShowTotals، ListColumns، الخ.) للفئة [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject) للتحكم في القائمة.

في المثال المُعطى أدناه، قمنا بإنشاء نفس [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject) باستخدام Aspose.Cells لواجهة برمجة التطبيقات لبيثون via Java كما قمنا بإنشائها باستخدام Microsoft Excel في القسم السابق.

## كود المصدر

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-CreatingListObject.py" >}}
