---
title: تنسيق كائن قائمة  جدول
type: docs
weight: 50
url: /ar/java/format-a-list-object-table/
---

{{% alert color="primary" %}}

لإدارة وتحليل مجموعة من البيانات ذات الصلة، يمكن تحويل نطاق الخلايا إلى كائن قائمة (المعروف أيضًا باسم جدول Excel). الجدول هو سلسلة من الصفوف والأعمدة التي تحتوي على بيانات ذات صلة تدير بشكل مستقل عن البيانات في الصفوف والأعمدة الأخرى. بشكل افتراضي، كل عمود في الجدول له تمكين التصفية في الصف العلوي بحيث يمكنك تصفية أو فرز بيانات كائن القائمة بسرعة. يمكنك إضافة صف إجمالي (صف خاص في القائمة يوفر تشكيلة من الوظائف الإجمالية المفيدة للعمل مع البيانات العددية) إلى كائن القائمة الذي يوفر قائمة منسدلة من الوظائف الإجمالية لكل خلية في صف الإجمالي. توفر Aspose.Cells خيارات لإنشاء وإدارة القوائم (أو الجداول).

{{% /alert %}}

## **تنسيق كائن قائمة**

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)، التي تمثل ملف Excel من Microsoft. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) التي تسمح بالوصول إلى كل ورقة في ملف Excel.

تمثّل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) مجموعة واسعة من الخصائص والطرق لإدارة أوراق العمل. لإنشاء [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) في ورقة العمل، استخدم خاصية [**ListObjects**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects) من مجموعة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)، كل [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) هو في الواقع كائن من فئة [**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection)، والتي توفر أيضًا طريقة add لإضافة كائن قائمة وتحديد نطاق الخلايا الذي يجب أن يشمله. وفقًا لنطاق خلايا معين، يتم إنشاء [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) في ورقة العمل بواسطة Aspose.Cells. استخدم السمات (على سبيل المثال، [**TableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#TableStyleType-) من فئة [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)) لتنسيق الجدول حسب متطلباتك.

المثال أدناه يضيف بيانات عينية إلى ورقة العمل، ويضيف [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) ويطبق الأنماط الافتراضية عليه. تُدعم أنماط [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) بواسطة Microsoft Excel 2007/2010.

يتم إنشاء الناتج التالي عند تنفيذ الكود.

**تم إنشاء جدول مُنسّق في ورقة العمل** 

![todo:image_alt_text](format-a-list-object-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FormataListObject-FormataListObject.java" >}}
{{< app/cells/assistant language="java" >}}
