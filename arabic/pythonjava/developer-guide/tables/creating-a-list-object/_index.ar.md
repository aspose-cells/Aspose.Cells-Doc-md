---
title: إنشاء كائن قائمة
type: docs
weight: 20
url: /ar/python-java/creating-a-list-object/
---
يسهل استخدام أوراق العمل التعامل مع أنواع مختلفة من القوائم ، على سبيل المثال. قوائم الهاتف وقوائم المهام. الخ. Aspose.Cells يدعم إنشاء وإدارة القوائم.

## **مزايا كائن القائمة**

هناك عدد غير قليل من المزايا عند تحويل قائمة البيانات إلى كائن قائمة فعلي:

- يتم تضمين الصفوف والأعمدة الجديدة تلقائيًا.
- يمكن إضافة صف إجمالي أسفل قائمتك بسهولة لعرض SUM و AVERAGE و COUNT وما إلى ذلك.
- يتم دمج الأعمدة المضافة إلى اليمين تلقائيًا في كائن القائمة.
- سيتم توسيع المخططات المستندة إلى الصفوف والأعمدة تلقائيًا.
- سيتم توسيع النطاقات المسماة المعينة للصفوف والأعمدة تلقائيًا.
- القائمة محمية من الحذف العرضي للصف والعمود.

## **تكوين كائن قائمة باستخدام Microsoft Excel**

**تحديد نطاق البيانات لإنشاء كائن قائمة** 

![ما يجب القيام به: image_بديل_نص](picture1.png)

يؤدي ذلك إلى عرض مربع الحوار "إنشاء قائمة".

**إنشاء مربع حوار القائمة** 

![ما يجب القيام به: image_بديل_نص](picture2.png)

تنفيذ كائن القائمة وتحديد إجمالي الصف (حدد**بيانات**، ومن بعد**قائمة**، تليها**إجمالي الصف**).

**إنشاء كائن قائمة** 

![ما يجب القيام به: image_بديل_نص](picture3.png)

## **تكوين عنصر قائمة باستخدام Aspose.Cells API**

Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/python/asposecells.api/Workbook)، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/python/asposecells.api/Workbook)فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)توفر class مجموعة واسعة من الخصائص والأساليب لإدارة ورقة العمل. لخلق[**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)في ورقة عمل ، استخدم[**ListObjects**](https://reference.aspose.com/cells/python/asposecells.api/worksheet#ListObjects)جمع ممتلكات[**ورقة عمل**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)صف دراسي. كل[**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)هو ، في الواقع ، كائن من[**ListObjectCollection**](https://reference.aspose.com/cells/python/asposecells.api/ListObjectCollection)فئة ، والتي توفر كذلك[**يضيف**](https://reference.aspose.com/cells/python/asposecells.api/listobjectcollection#add(int,%20int,%20int,%20int,%20boolean)) لإضافة كائن قائمة وتحديد نطاق من الخلايا للقائمة.

وفقًا لنطاق الخلايا المحدد ، يتم إنشاء كائن القائمة في ورقة العمل بواسطة Aspose.Cells. استخدم السمات (على سبيل المثال ، ShowTotals و ListColumns وما إلى ذلك) من[**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)فئة للسيطرة على القائمة.

في المثال الموضح أدناه ، أنشأنا نفس الشيء[**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)باستخدام Aspose.Cells for Python via Java API كما أنشأنا باستخدام Microsoft Excel في القسم أعلاه.

## مصدر الرمز

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-CreatingListObject.py" >}}
