---
title: إنشاء وتنسيق الجدول
type: docs
weight: 10
url: /ar/go-cpp/create-and-format-table/
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

| **تحديد نطاق البيانات لإنشاء كائن القائمة** |
| :- |
|![todo:image_alt_text](jHcNq4o.png)|
يعرض ذلك مربع حوار إنشاء القائمة.

| **مربع حوار إنشاء القائمة** |
| :- |
|![todo:image_alt_text](kJmukRF.png)|
تنفيذ كائن القائمة للبيانات وتحديد الصف الإجمالي (حدد **البيانات**, ثم **القائمة**, تتبعها **الصف الإجمالي**).

| **إنشاء كائن قائمة** |
| :- |
|![todo:image_alt_text](ECSGVdR.png)|

### **استخدام واجهة برمجة تطبيقات Aspose.Cells**

توفر Aspose.Cells فئة [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) التي تمثل ملف Microsoft Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) على مجموعة [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) تتيح الوصول إلى كل ورقة عمل في ملف Excel.

تمثل ورقة العمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). توفر فئة [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) مجموعة واسعة من الطرق لإدارة ورقة العمل. لإنشاء [ListObject](https://reference.aspose.com/cells/go-cpp/listobject/) في ورقة العمل، استخدم طريقة مجموعة [GetListObjects](https://reference.aspose.com/cells/go-cpp/worksheet/getlistobjects/). كل `[ListObject]` هو في الواقع كائن من فئة [ListObjectCollection](https://reference.aspose.com/cells/go-cpp/listobjectcollection/)، التي توفر طريقة [Add](https://reference.aspose.com/cells/go-cpp/listobjectcollection/add_int_int_int_int_bool/) لإضافة كائن `[ListObject]` وتحديد نطاق من الخلايا للقائمة.

وفقًا لنطاق الخلايا المحدد، يتم إنشاء كائن `[ListObject]` بواسطة Aspose.Cells. استخدم سمات (على سبيل المثال [SetShowTotals](https://reference.aspose.com/cells/go-cpp/listobject/setshowtotals/) و [GetListColumns](https://reference.aspose.com/cells/go-cpp/listobject/getlistcolumns/)، وغير ذلك) من فئة `[ListObject]` للتحكم في القائمة.

في المثال الوارد أدناه ، لقد قمنا بإنشاء نفس `[ListObject]` باستخدام واجهة برمجة التطبيقات Aspose.Cells كما قمنا بذلك باستخدام Microsoft Excel في الجزء السابق.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatingListObjects.go" >}}

## **تنسيق الجدول**

لإدارة وتحليل مجموعة من البيانات ذات الصلة ، من الممكن تحويل نطاق الخلايا إلى كائن قائمة (المعروف أيضًا باسم جدول Excel). الجدول هو سلسلة من الصفوف والأعمدة التي تحتوي على بيانات ذات صلة يتم إدارتها بشكل مستقل عن البيانات في الصفوف والأعمدة الأخرى. بشكل افتراضي ، يتم تمكين عمود كلي في الجدول في الصف الرأسي بحيث يمكنك تصفية أو فرز بيانات كائن القائمة بسرعة. يمكنك إضافة صف إجمالي (صف خاص في القائمة يوفر تحديد وظائف الفحص المجمعة المفيدة للعمل مع البيانات الرقمية) إلى كائن القائمة الذي يوفر قائمة منسدلة من وظائف الفحص المجمعة لكل خلية صفات الإجمالي. توفر Aspose.Cells خيارات لإنشاء وإدارة القوائم (أو الجداول).

### **تنسيق كائن قائمة**

توفر Aspose.Cells فئة [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) التي تمثل ملف Microsoft Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) على مجموعة [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) تتيح الوصول إلى كل ورقة عمل في ملف Excel.

تمثل ورقة العمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). توفر فئة [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) مجموعة واسعة من الطرق لإدارة أوراق العمل. لإنشاء *ListObject* في ورقة العمل، استخدم `ListObjectCollection`. كل `[ListObject]` هو في الواقع كائن من فئة `ListObjectCollection`، التي توفر طريقة [Add](https://reference.aspose.com/cells/go-cpp/listobjectcollection/add/) لإضافة كائن `[ListObject]` وتحديد نطاق الخلايا الذي يجب أن يشمله. وفقًا لنطاق الخلايا المحدد، يتم إنشاء *ListObject* في ورقة العمل بواسطة Aspose.Cells. استخدم سمات (على سبيل المثال [SetTableStyleType](https://reference.aspose.com/cells/go-cpp/listobject/settablestyletype/)) من فئة `[ListObject]` لتنسيق الجدول حسب متطلباتك.

يضيف المثال أدناه بيانات عينية إلى ورقة عمل ، ويضيف `[ListObject]` ويطبق الأنماط الافتراضية عليه. تتمتع أنماط `[ListObject]` بدعم من قبل Microsoft Excel 2007/2010.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormatTable.go" >}}
