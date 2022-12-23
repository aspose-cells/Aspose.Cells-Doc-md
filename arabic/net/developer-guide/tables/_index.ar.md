---
title: انشاء وادارة جداول Microsoft ملفات Excel.
linktitle: الجداول
type: docs
weight: 150
url: /ar/net/create-and-format-table/
description: إدراج جدول ملفات Excel وتغيير حجمه وتحريره وحذفه وتنسيقه باستخدام مكتبة Aspose.Cells.
---
## **اصنع جدول**

تتمثل إحدى مزايا جداول البيانات في أنها تسمح لك بإنشاء أنواع مختلفة من القوائم ، على سبيل المثال ، قوائم الهاتف أو قوائم المهام أو قوائم المعاملات أو الأصول أو الخصوم. يمكن للعديد من المستخدمين العمل معًا لاستخدام قوائم متنوعة وإنشاؤها والاحتفاظ بها.

Aspose.Cells يدعم تكوين وإدارة القوائم.

### **مزايا كائن القائمة**

هناك عدد غير قليل من المزايا عند تحويل قائمة البيانات إلى كائن قائمة فعلي

- يتم تضمين الصفوف والأعمدة الجديدة تلقائيًا.
- يمكن إضافة صف إجمالي أسفل قائمتك بسهولة لعرض SUM و AVERAGE و COUNT وما إلى ذلك.
- يتم دمج الأعمدة المضافة إلى اليمين تلقائيًا في كائن القائمة.
- سيتم توسيع المخططات المستندة إلى الصفوف والأعمدة تلقائيًا.
- سيتم توسيع النطاقات المسماة المعينة للصفوف والأعمدة تلقائيًا.
- القائمة محمية من الحذف العرضي للصف والعمود.

### **تكوين كائن قائمة باستخدام Microsoft Excel**

- تحديد نطاق البيانات لإنشاء كائن قائمة
- يؤدي ذلك إلى عرض مربع الحوار "إنشاء قائمة".
-  قم بتنفيذ كائن القائمة للبيانات وتحديد صف الإجمالي (حدد**بيانات** ، ومن بعد**قائمة** ، تليها**إجمالي الصف**).

### **باستخدام Aspose.Cells API**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

 يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) توفر class مجموعة واسعة من الخصائص والأساليب لإدارة ورقة العمل. لخلق[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) في ورقة العمل ، استخدم ملف[**ListObjects**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects) جمع ممتلكات[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. كل[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) هو ، في الواقع ، كائن من[**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection) فئة ، والتي توفر كذلك[**يضيف**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index)طريقة لإضافة كائن قائمة وتحديد نطاق من الخلايا للقائمة.

وفقًا لنطاق الخلايا المحدد ، يتم إنشاء كائن القائمة بواسطة Aspose.Cells. استخدم السمات (على سبيل المثال ،[**ShowTotals**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/showtotals), [**ListColumns**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/listcolumns) ، وما إلى ذلك) من[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)فئة للسيطرة على القائمة.

 في المثال الموضح أدناه ، أنشأنا نفس الشيء[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)باستخدام Aspose.Cells API كما أنشأنا باستخدام Microsoft Excel في القسم أعلاه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-CreatingListObject-1.cs" >}}

## **تنسيق جدول**

لإدارة وتحليل مجموعة من البيانات ذات الصلة ، من الممكن تحويل نطاق من الخلايا إلى كائن قائمة (يُعرف أيضًا باسم جدول Excel). الجدول عبارة عن سلسلة من الصفوف والأعمدة التي تحتوي على بيانات ذات صلة تتم إدارتها بشكل مستقل عن البيانات الموجودة في صفوف وأعمدة أخرى. بشكل افتراضي ، يتم تمكين التصفية في كل عمود في الجدول في صف الرأس بحيث يمكنك تصفية بيانات كائن القائمة أو فرزها بسرعة. يمكنك إضافة صف إجمالي (صف خاص في قائمة يوفر مجموعة مختارة من الوظائف المجمعة المفيدة للعمل مع البيانات الرقمية) إلى كائن القائمة الذي يوفر قائمة منسدلة بالوظائف المجمعة لكل خلية صف إجمالي. Aspose.Cells يوفر اختيارات لتكوين وادارة كشوف (أو جداول).

### **تنسيق كائن قائمة**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

 يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) توفر class مجموعة واسعة من الخصائص والأساليب لإدارة أوراق العمل. لخلق[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) في ورقة عمل ، استخدم[**ListObjects**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects) جمع ممتلكات[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. كل[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) هو ، في الواقع ، كائن من[**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection) فئة ، والتي توفر كذلك[**يضيف**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index) طريقة لإضافة كائن قائمة وتحديد نطاق الخلايا التي يجب أن يشملها. وفقًا لنطاق الخلايا المحدد ، أ[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)تم إنشاؤه في ورقة العمل بواسطة Aspose.Cells. استخدم السمات (على سبيل المثال ،[**TableStyleType**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/tablestyletype) ) التابع[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)فئة لتنسيق الجدول لمتطلباتك.

 يضيف المثال أدناه بيانات نموذجية إلى ورقة عمل ، ويضيف ملف[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) وتطبيق الأنماط الافتراضية عليه.[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)الأنماط مدعومة بواسطة Microsoft Excel 2007/2010.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-FormataListObject-1.cs" >}}

## **موضوعات مسبقة**
- [حوّل الجدول إلى ODS](/cells/ar/net/convert-table-to-ods/)
- [البحث عن جداول الاستعلام وكائنات القائمة ذات الصلة باتصالات البيانات الخارجية](/cells/ar/net/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [قراءة وكتابة الجدول باستخدام مصدر بيانات جدول الاستعلام](/cells/ar/net/read-and-write-table-with-query-table-data-source/)
- [قم بتعيين تعليق جدول أو قائمة كائن داخل ورقة العمل](/cells/ar/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [الجداول والنطاقات](/cells/ar/net/tables-and-ranges/)

