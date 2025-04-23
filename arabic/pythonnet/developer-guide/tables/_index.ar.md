---
title: إنشاء وإدارة جداول ملفات Microsoft Excel.
linktitle: الجداول
type: docs
weight: 150
url: /ar/python-net/create-and-format-table/
description: إدراج، تغيير الحجم، تحرير، حذف، تنسيق الجدول في ملفات Excel باستخدام مكتبة Aspose.Cells.
---

## **إنشاء جدول**

أحد ميزات الجداول الإلكترونية هو أنها تتيح لك إنشاء أنواع مختلفة من القوائم، على سبيل المثال: قوائم الهواتف، قوائم المهام، قوائم المعاملات، الأصول أو المطلوبات. يمكن لعدة مستخدمين العمل معًا لاستخدام وإنشاء وصيانة قوائم مختلفة.

يدعم Aspose.Cells لبايثون via .NET إنشاء وإدارة القوائم.

### **مزايا كائن القائمة**

هناك العديد من المزايا عند تحويل قائمة البيانات إلى كائن قائمة فعلي

- يتم تضمين صفوف وأعمدة جديدة تلقائيًا.
- يمكن بسهولة إضافة صف إجمالي في أسفل القائمة لعرض الجمع والمتوسط والعد، إلخ.
- يتم دمج الأعمدة المضافة إلى اليمين تلقائيًا في كائن القائمة.
- ستتم توسيع الرسوم البيانية استنادًا إلى الصفوف والأعمدة تلقائيًا.
- ستتم توسيع النطاقات المسماة المخصصة للصفوف والأعمدة تلقائيًا.
- تكون القائمة محمية من حذف الصف والعمود بطريق الخطأ.

### **إنشاء كائن قائمة باستخدام Microsoft Excel**

- تحديد نطاق البيانات لإنشاء كائن قائمة
- يعرض ذلك حوار إنشاء القائمة.
- نفذ كائن القائمة للبيانات وتحديد صف إجمالي (تحديد **Data**, ثم **List**, تليها **Total Row**).

### **باستخدام API Aspose.Cells لبايثون via .NET**

يوفر Aspose.Cells لبايثون via .NET فئة، [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)، التي تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

تُمثل ورقة العمل بواسطة الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة ورقة العمل. لإنشاء [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) في ورقة العمل، استخدم خاصية مجموعة [**list_objects**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/list_objects) للفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). كل [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) هو في الواقع كائن من فئة [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection/add/#int-int-int-int-bool)، التي توفر بدورها الأسلوب [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection/add/#int-int-int-int-bool) لإضافة كائن قائمة وتحديد مجموعة خلايا للقائمة.

وفقًا لنطاق الخلايا المحدد، يتم إنشاء كائن القائمة بواسطة Aspose.Cells لبايثون via .NET. استخدم سمات (على سبيل المثال، [**show_totals**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/show_totals)، [**ListColumns**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/list_columns)، وغيرها) من فئة [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) للتحكم في القائمة.

في المثال المقدم أدناه، قمنا بإنشاء نفس [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) باستخدام API Aspose.Cells لبايثون via .NET كما أنشأنا باستخدام Microsoft Excel في القسم أعلاه.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-CreatingListObject-1.py" >}}

## **تنسيق الجدول**

لإدارة وتحليل مجموعة من البيانات ذات الصلة، من الممكن تحويل نطاق من الخلايا إلى كائن قائمة (المعروف أيضًا باسم جدول Excel). الجدول هو سلسلة من الصفوف والأعمدة التي تحتوي على بيانات ذات صلة وتدار بشكل مستقل عن البيانات الموجودة في الصفوف والأعمدة الأخرى. بشكل افتراضي، يتم تمكين التصفية لكل عمود في الجدول في صف الرأس بحيث يمكنك تصفية أو تصنيف بيانات كائن القائمة بسرعة. يمكنك إضافة صف إجمالي (صف خاص في قائمة يوفر مجموعة من الوظائف التجميعية المفيدة للعمل مع البيانات الرقمية) إلى كائن القائمة الذي يوفر قائمة منسدلة من الوظائف التجميعية لكل خلية في الصف الإجمالي. يوفر Aspose.Cells لبايثون via .NET خيارات لإنشاء وإدارة القوائم (أو الجداول).

### **تنسيق كائن قائمة**

يوفر Aspose.Cells لبايثون via .NET فئة، [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)، التي تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)، التي تتيح الوصول إلى كل ورقة عمل في ملف Excel.

تُمثل ورقة العمل بواسطة الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة ورقة العمل. لإنشاء [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) في ورقة العمل، استخدم خاصية مجموعة [**list_objects**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/list_objects) للفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). كل [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) هو في الواقع كائن من فئة [**ListObjectCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection)، التي توفر بدورها الأسلوب [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection/add/#int-int-int-int-bool) لإضافة كائن قائمة وتحديد نطاق الخلايا التي يجب أن يحيط بها. وفقًا لنطاق الخلايا المحدد، يتم إنشاء [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) في ورقة العمل باستخدام Aspose.Cells. استخدم السمات (على سبيل المثال، [**table_style_type**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/table_style_type)) لفئة [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) لتنسيق الجدول وفقًا لاحتياجاتك.

يُضيف المثال أدناه بيانات عينية إلى ورقة عمل، يضيف [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) ويطبق الأنماط الافتراضية عليه. تدعم الأنماط [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) بواسطة Microsoft Excel 2007/2010.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-FormataListObject-1.py" >}}

## **مواضيع متقدمة**
- [تحويل الجدول إلى ODS](/cells/ar/python-net/convert-table-to-ods/)
- [العثور على جداول الاستعلام وكائنات القائمة المتعلقة باتصالات البيانات الخارجية](/cells/ar/python-net/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [قراءة وكتابة الجدول مع مصدر بيانات جدول الاستعلام](/cells/ar/python-net/read-and-write-table-with-query-table-data-source/)
- [ضبط التعليق للجدول أو كائن القائمة داخل ورقة العمل](/cells/ar/python-net/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [الجداول والمدى](/cells/ar/python-net/tables-and-ranges/)


