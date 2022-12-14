---
title: إنشاء وتنسيق الجدول
type: docs
weight: 10
url: /ar/cpp/create-and-format-table/
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

|**تحديد نطاق البيانات لإنشاء كائن القائمة**|
|:- |
|![ما يجب القيام به: image_بديل_نص](jHcNq4o.png)|
يؤدي ذلك إلى عرض مربع الحوار "إنشاء قائمة".

|**إنشاء مربع حوار القائمة**|
|:- |
|![ما يجب القيام به: image_بديل_نص](kJmukRF.png)|
 تنفيذ كائن القائمة للبيانات وتحديد الصف الإجمالي (حدد**بيانات** ، ومن بعد**قائمة** ، تليها**إجمالي الصف**).

|**إنشاء كائن قائمة**|
|:- |
|![ما يجب القيام به: image_بديل_نص](ECSGVdR.png)|
### **باستخدام Aspose.Cells API**
 Aspose.Cells يوفر فئة[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) الذي يمثل ملف إكسل Microsoft. ال[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) فئة تحتوي على[أوراق العمل](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

 يتم تمثيل ورقة العمل بواسطة[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) صف دراسي. ال[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) يوفر class مجموعة واسعة من الأساليب لإدارة ورقة العمل. لإنشاء ملف[IListObject](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object) في ورقة العمل ، استخدم ملف[GetIListObjects](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a4356bc4b8cffee624891f10ea49a4705) طريقة جمع[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) صف دراسي. كل `[IListObject]` هو في الواقع كائن من[IListObjectCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object_collection) فئة ، والتي توفر كذلك[يضيف](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object_collection#ae4afda31b69b75a78558a65bef65ee42)طريقة لإضافة عنصر `[IListObject]` وتحديد نطاق من الخلايا للقائمة.

 وفقًا لنطاق الخلايا المحدد ، يتم إنشاء كائن `[IListObject]` بواسطة Aspose.Cells. استخدم السمات (على سبيل المثال[ShowTotals](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object#a9026460927f035f374f5e1ea74e639f2) و[ListColumns](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object#afeeb7bfabd0971e9fe34a09f0b83ae73)إلخ) من فئة `[IListObject]` للتحكم في القائمة.

في المثال الموضح أدناه ، أنشأنا نفس `[IListObject]` باستخدام Aspose.Cells API كما أنشأنا باستخدام Microsoft Excel في القسم أعلاه.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-CreatingListObjects.cpp" >}}
## **تنسيق جدول**
لإدارة وتحليل مجموعة من البيانات ذات الصلة ، من الممكن تحويل نطاق من الخلايا إلى كائن قائمة (يُعرف أيضًا باسم جدول Excel). الجدول عبارة عن سلسلة من الصفوف والأعمدة التي تحتوي على بيانات ذات صلة تتم إدارتها بشكل مستقل عن البيانات الموجودة في صفوف وأعمدة أخرى. بشكل افتراضي ، يتم تمكين التصفية في كل عمود في الجدول في صف الرأس بحيث يمكنك تصفية بيانات كائن القائمة أو فرزها بسرعة. يمكنك إضافة صف إجمالي (صف خاص في قائمة يوفر مجموعة مختارة من الوظائف المجمعة المفيدة للعمل مع البيانات الرقمية) إلى كائن القائمة الذي يوفر قائمة منسدلة بالوظائف المجمعة لكل خلية صف إجماليات. Aspose.Cells يوفر اختيارات لتكوين وادارة كشوف (أو جداول).
### **تنسيق كائن قائمة**
 Aspose.Cells يوفر فئة[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) الذي يمثل ملف إكسل Microsoft. ال[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) فئة تحتوي على[أوراق العمل](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

 يتم تمثيل ورقة العمل بواسطة[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) صف دراسي. ال[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) يوفر class مجموعة واسعة من الأساليب لإدارة أوراق العمل. لخلق*ListObject*في ورقة العمل ، استخدم `IListObjectCollection`. كل `[IListObject]` هو في الواقع ، كائن من الفئة `IListObjectCollection` ، والذي يوفر أيضًا[يضيف](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object_collection#ae4afda31b69b75a78558a65bef65ee42)طريقة لإضافة كائن `[IListObject]` وتحديد نطاق الخلايا التي يجب أن يشملها. وفقًا لنطاق الخلايا المحدد ، أ*ListObject* تم إنشاؤه في ورقة العمل بواسطة Aspose.Cells. استخدم السمات (على سبيل المثال ،[TableStyleType](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object#a5de8b5321b0ccb30dfb09cefe6536462)) من فئة `[IListObject]` لتنسيق الجدول وفقًا لمتطلباتك.

يضيف المثال أدناه بيانات نموذجية إلى ورقة عمل ، ويضيف `[IListObject]` ويطبق الأنماط الافتراضية عليها. يتم دعم أنماط `[IListObject]` بواسطة Microsoft Excel 2007/2010.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-FormatTable.cpp" >}}
