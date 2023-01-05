---
title: إنشاء جدول
type: docs
weight: 40
url: /ar/java/creating-a-list-object/
---
{{% alert color="primary" %}}

تتمثل إحدى مزايا جداول البيانات في أنها تسمح لك بإنشاء أنواع مختلفة من القوائم ، على سبيل المثال ، قوائم الهاتف أو قوائم المهام أو قوائم المعاملات أو الأصول أو الخصوم. يمكن للعديد من المستخدمين العمل معًا لاستخدام قوائم متنوعة وإنشاؤها والاحتفاظ بها.

Aspose.Cells يدعم تكوين وإدارة القوائم.

{{% /alert %}}

## **مزايا الجدول**

هناك عدد غير قليل من المزايا عند تحويل قائمة البيانات إلى كائن قائمة فعلي:

- يتم تضمين الصفوف والأعمدة الجديدة تلقائيًا.
- يمكن إضافة صف إجمالي أسفل قائمتك بسهولة لعرض SUM و AVERAGE و COUNT وما إلى ذلك.
- يتم دمج الأعمدة المضافة إلى اليمين تلقائيًا في كائن القائمة.
- سيتم توسيع المخططات المستندة إلى الصفوف والأعمدة تلقائيًا.
- سيتم توسيع النطاقات المسماة المعينة للصفوف والأعمدة تلقائيًا.
- القائمة محمية من الحذف العرضي للصف والعمود.

## **تكوين جدول باستخدام Microsoft Excel**

**تحديد نطاق البيانات لإنشاء كائن قائمة** 

![ما يجب القيام به: image_بديل_نص](creating-a-list-object_1.png)

يؤدي ذلك إلى عرض مربع الحوار "إنشاء قائمة".

**إنشاء مربع حوار القائمة** 

![ما يجب القيام به: image_بديل_نص](creating-a-list-object_2.png)

 تنفيذ كائن القائمة وتحديد إجمالي الصف (حدد**بيانات** ، ومن بعد**قائمة** ، تليها**إجمالي الصف**).

**إنشاء كائن قائمة** 

![ما يجب القيام به: image_بديل_نص](creating-a-list-object_3.png)

## **تكوين جدول باستخدام Aspose.Cells API**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

 يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) توفر class مجموعة واسعة من الخصائص والأساليب لإدارة ورقة العمل. لخلق[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) في ورقة عمل ، استخدم[**ListObjects**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects) مجموعة من فئة ورقة العمل. كل[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) هو ، في الواقع ، كائن من[**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection)class ، والتي توفر أيضًا طريقة الإضافة لإضافة كائن قائمة وتحديد نطاق من الخلايا للقائمة.

وفقًا لنطاق الخلايا المحدد ، يتم إنشاء كائن القائمة في ورقة العمل بواسطة Aspose.Cells. استخدم السمات (على سبيل المثال ، ShowTotals و ListColumns وما إلى ذلك) من[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)فئة للسيطرة على القائمة.

 في المثال الموضح أدناه ، أنشأنا نفس الشيء[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)باستخدام Aspose.Cells API كما أنشأنا باستخدام Microsoft Excel في القسم أعلاه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-CreatingListObject-CreatingListObject.java" >}}
