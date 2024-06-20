---
title: إنشاء وإدارة جداول ملفات Microsoft Excel.
linktitle: الجداول
type: docs
weight: 150
url: /ar/net/create-and-format-table/
description: إدراج، تغيير الحجم، تحرير، حذف، تنسيق الجدول في ملفات Excel باستخدام مكتبة Aspose.Cells.
---

## **إنشاء جدول**

أحد ميزات الجداول الإلكترونية هو أنها تتيح لك إنشاء أنواع مختلفة من القوائم، على سبيل المثال: قوائم الهواتف، قوائم المهام، قوائم المعاملات، الأصول أو المطلوبات. يمكن لعدة مستخدمين العمل معًا لاستخدام وإنشاء وصيانة قوائم مختلفة.

يدعم Aspose.Cells إنشاء وإدارة القوائم.

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

### **استخدام واجهة برمجة تطبيقات Aspose.Cells**

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)، التي تمثل ملف Excel من Microsoft. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) التي تسمح بالوصول إلى كل ورقة في ملف Excel.

تُمثل ورقة العمل بواسطة الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة ورقة العمل. لإنشاء [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) في ورقة العمل، استخدم خاصية مجموعة [**ListObjects**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects) للفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). كل [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) هو في الواقع كائن من فئة [**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection)، التي توفر بدورها الأسلوب [**Add**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index) لإضافة كائن قائمة وتحديد مجموعة خلايا للقائمة.

وفقًا لنطاق الخلايا المحدد، يتم إنشاء كائن القائمة بواسطة Aspose.Cells. استخدم السمات (على سبيل المثال، [**ShowTotals**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/showtotals)، [**ListColumns**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/listcolumns)، وما إلى ذلك) لفئة [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) للتحكم في القائمة.

في المثال المعطى أدناه، قمنا بإنشاء نفس [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) باستخدام واجهة برمجة التطبيقات Aspose.Cells وكما قمنا بإنشائه باستخدام Microsoft Excel في القسم السابق.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-CreatingListObject-1.cs" >}}

## **تنسيق الجدول**

لإدارة وتحليل مجموعة من البيانات ذات الصلة، يمكن تحويل نطاق الخلايا إلى كائن قائمة (المعروف أيضًا باسم جدول Excel). الجدول هو سلسلة من الصفوف والأعمدة التي تحتوي على بيانات ذات صلة تدير بشكل مستقل عن البيانات في الصفوف والأعمدة الأخرى. بشكل افتراضي، كل عمود في الجدول له تمكين التصفية في الصف العلوي بحيث يمكنك تصفية أو فرز بيانات كائن القائمة بسرعة. يمكنك إضافة صف إجمالي (صف خاص في القائمة يوفر تشكيلة من الوظائف الإجمالية المفيدة للعمل مع البيانات العددية) إلى كائن القائمة الذي يوفر قائمة منسدلة من الوظائف الإجمالية لكل خلية في صف الإجمالي. توفر Aspose.Cells خيارات لإنشاء وإدارة القوائم (أو الجداول).

### **تنسيق كائن قائمة**

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)، التي تمثل ملف Excel من Microsoft. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) التي تسمح بالوصول إلى كل ورقة في ملف Excel.

تُمثل ورقة العمل بواسطة الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة ورقة العمل. لإنشاء [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) في ورقة العمل، استخدم خاصية مجموعة [**ListObjects**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects) للفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). كل [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) هو في الواقع كائن من فئة [**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection)، التي توفر بدورها الأسلوب [**Add**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index) لإضافة كائن قائمة وتحديد نطاق الخلايا التي يجب أن يحيط بها. وفقًا لنطاق الخلايا المحدد، يتم إنشاء [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) في ورقة العمل باستخدام Aspose.Cells. استخدم السمات (على سبيل المثال، [**TableStyleType**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/tablestyletype)) لفئة [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) لتنسيق الجدول وفقًا لاحتياجاتك.

يُضيف المثال أدناه بيانات عينية إلى ورقة عمل، يضيف [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) ويطبق الأنماط الافتراضية عليه. تدعم الأنماط [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) بواسطة Microsoft Excel 2007/2010.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-FormataListObject-1.cs" >}}

## **مواضيع متقدمة**
- [تحويل الجدول إلى ODS](/cells/ar/net/convert-table-to-ods/)
- [العثور على جداول الاستعلام وكائنات القائمة المتعلقة باتصالات البيانات الخارجية](/cells/ar/net/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [قراءة وكتابة الجدول مع مصدر بيانات جدول الاستعلام](/cells/ar/net/read-and-write-table-with-query-table-data-source/)
- [ضبط التعليق للجدول أو كائن القائمة داخل ورقة العمل](/cells/ar/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [الجداول والمدى](/cells/ar/net/tables-and-ranges/)

