---
title: تنسيق كائن قائمة - جدول
type: docs
weight: 50
url: /ar/java/format-a-list-object-table/
---
{{% alert color="primary" %}}

لإدارة وتحليل مجموعة من البيانات ذات الصلة ، من الممكن تحويل نطاق من الخلايا إلى كائن قائمة (يُعرف أيضًا باسم جدول Excel). الجدول عبارة عن سلسلة من الصفوف والأعمدة التي تحتوي على بيانات ذات صلة تتم إدارتها بشكل مستقل عن البيانات الموجودة في صفوف وأعمدة أخرى. بشكل افتراضي ، يتم تمكين التصفية في كل عمود في الجدول في صف الرأس بحيث يمكنك تصفية بيانات كائن القائمة أو فرزها بسرعة. يمكنك إضافة صف إجمالي (صف خاص في قائمة يوفر مجموعة مختارة من الوظائف المجمعة المفيدة للعمل مع البيانات الرقمية) إلى كائن القائمة الذي يوفر قائمة منسدلة بالوظائف المجمعة لكل خلية صف إجمالي. Aspose.Cells يوفر اختيارات لتكوين وادارة كشوف (أو جداول).

{{% /alert %}}

## **تنسيق كائن قائمة**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

 يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) توفر class مجموعة واسعة من الخصائص والأساليب لإدارة أوراق العمل. لخلق[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) في ورقة عمل ، استخدم[**ListObjects**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects) جمع ممتلكات[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي. كل[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) هو ، في الواقع ، كائن من[**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection)class ، والتي توفر أيضًا طريقة الإضافة لإضافة كائن قائمة وتحديد نطاق الخلايا التي يجب أن يشملها. وفقًا لنطاق الخلايا المحدد ، أ[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) تم إنشاؤه في ورقة العمل بواسطة Aspose.Cells. استخدم السمات (على سبيل المثال ،[**TableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#TableStyleType) ) التابع[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)فئة لتنسيق الجدول لمتطلباتك.

 يضيف المثال أدناه بيانات نموذجية إلى ورقة عمل ، ويضيف ملف[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) ويطبق الأنماط الافتراضية عليه.[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)الأنماط مدعومة بواسطة Microsoft Excel 2007/2010.

يتم إنشاء الإخراج التالي عند تنفيذ التعليمات البرمجية.

**يتم إنشاء جدول منسق في ورقة العمل** 

![ما يجب القيام به: image_بديل_نص](format-a-list-object-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FormataListObject-FormataListObject.java" >}}
