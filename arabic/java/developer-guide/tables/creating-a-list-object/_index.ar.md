---
title: إنشاء جدول
type: docs
weight: 40
url: /ar/java/creating-a-list-object/
---

{{% alert color="primary" %}}

أحد ميزات الجداول الإلكترونية هو أنها تتيح لك إنشاء أنواع مختلفة من القوائم، على سبيل المثال: قوائم الهواتف، قوائم المهام، قوائم المعاملات، الأصول أو المطلوبات. يمكن لعدة مستخدمين العمل معًا لاستخدام وإنشاء وصيانة قوائم مختلفة.

يدعم Aspose.Cells إنشاء وإدارة القوائم.

{{% /alert %}}

## **مزايا الجدول**

هناك العديد من المزايا عند تحويل قائمة البيانات إلى كائن قائمة فعلي:

- يتم تضمين صفوف وأعمدة جديدة تلقائيًا.
- يمكن بسهولة إضافة صف إجمالي في أسفل القائمة لعرض الجمع والمتوسط والعد، إلخ.
- يتم دمج الأعمدة المضافة إلى اليمين تلقائيًا في كائن القائمة.
- ستتم توسيع الرسوم البيانية استنادًا إلى الصفوف والأعمدة تلقائيًا.
- ستتم توسيع النطاقات المسماة المخصصة للصفوف والأعمدة تلقائيًا.
- تكون القائمة محمية من حذف الصف والعمود بطريق الخطأ.

## **إنشاء جدول باستخدام Microsoft Excel**

**تحديد نطاق البيانات لإنشاء كائن القائمة** 

![todo:image_alt_text](creating-a-list-object_1.png)

يعرض ذلك مربع حوار إنشاء القائمة.

**مربع حوار إنشاء القائمة** 

![todo:image_alt_text](creating-a-list-object_2.png)

تنفيذ كائن القائمة وتحديد الصف الإجمالي (حدد **البيانات**، ثم **القائمة**، تليها **الصف الإجمالي**).

**إنشاء كائن القائمة** 

![todo:image_alt_text](creating-a-list-object_3.png)

## **إنشاء جدول باستخدام واجهة برمجة التطبيقات Aspose.Cells**

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)، التي تمثل ملف Excel من Microsoft. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) التي تسمح بالوصول إلى كل ورقة في ملف Excel.

تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). يوفر الفئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة ورقة العمل. لإنشاء [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) في ورقة العمل، استخدم مجموعة الخاصية [**ListObjects**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects) من فئة ورقة العمل. كل [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) هو في الواقع كائن من فئة [**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection)، التي توفر أيضًا طريقة الإضافة لإضافة كائن قائمة وتحديد نطاق الخلايا للقائمة.

وفقًا لنطاق الخلايا المحدد، يتم إنشاء كائن القائمة في ورقة العمل بواسطة Aspose.Cells. استخدم السمات (على سبيل المثال، ShowTotals، ListColumns الخ) لفئة [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) للتحكم في القائمة.

في المثال المعطى أدناه، قمنا بإنشاء نفس [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) باستخدام واجهة برمجة التطبيقات Aspose.Cells وكما قمنا بإنشائه باستخدام Microsoft Excel في القسم السابق.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-CreatingListObject-CreatingListObject.java" >}}
{{< app/cells/assistant language="java" >}}
