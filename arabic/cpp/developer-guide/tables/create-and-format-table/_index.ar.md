---
title: إنشاء وتنسيق الجدول
type: docs
weight: 10
url: /ar/cpp/create-and-format-table/
---
##  **اصنع جدول**
إحدى مزايا جداول البيانات هي أنها تسمح لك بإنشاء أنواع مختلفة من القوائم، على سبيل المثال، قوائم الهاتف، أو قوائم المهام، أو قوائم المعاملات، أو الأصول أو الخصوم. يمكن للعديد من المستخدمين العمل معًا لاستخدام قوائم متنوعة وإنشائها والاحتفاظ بها.

Aspose.Cells يدعم إنشاء وإدارة القوائم.
###  **مزايا كائن القائمة**
هناك عدد لا بأس به من المزايا عند تحويل قائمة البيانات إلى كائن قائمة فعلي

- يتم تضمين الصفوف والأعمدة الجديدة تلقائيًا.
- يمكن بسهولة إضافة صف إجمالي في أسفل قائمتك لعرض SUM، وAVERAGE، وCOUNT، وما إلى ذلك.
- يتم دمج الأعمدة المضافة إلى اليمين تلقائيًا في كائن القائمة.
- سيتم توسيع المخططات المستندة إلى الصفوف والأعمدة تلقائيًا.
- سيتم توسيع النطاقات المسماة المخصصة للصفوف والأعمدة تلقائيًا.
- القائمة محمية من الحذف غير المقصود للصفوف والأعمدة.
###  **إنشاء كائن قائمة باستخدام Microsoft Excel**

|**تحديد نطاق البيانات لإنشاء كائن القائمة**|
| :- |
|![ما يجب القيام به:image_alt_text](jHcNq4o.png)|
يؤدي هذا إلى عرض مربع الحوار "إنشاء قائمة".

|**إنشاء مربع حوار القائمة**|
| :- |
|![ما يجب القيام به:image_alt_text](kJmukRF.png)|
تنفيذ كائن القائمة للبيانات وتحديد الصف الإجمالي (اختر *البيانات**، ثم *القائمة**، متبوعة بـ *الصف الإجمالي**).

|**إنشاء كائن القائمة**|
| :- |
|![ما يجب القيام به:image_alt_text](ECSGVdR.png)|
###  **باستخدام Aspose.Cells API**
 Aspose.Cells يوفر فئة[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) الذي يمثل ملف Excel Microsoft. ال[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) يحتوي الفصل على[أوراق عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) فصل. ال[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) يوفر الفصل مجموعة واسعة من الأساليب لإدارة ورقة العمل. لإنشاء[ListObject](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/) في ورقة العمل، استخدم[GetListObjects](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getlistobjects/) طريقة جمع ال[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) فصل. كل `[ListObject]` هو في الواقع كائن من[ListObjectCollection](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/) الطبقة، والتي توفر كذلك[يضيف](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/)طريقة لإضافة كائن `[ListObject]` وتحديد نطاق من الخلايا للقائمة.

 وفقًا لنطاق الخلايا المحدد، يتم إنشاء الكائن `[ListObject]` بواسطة Aspose.Cells. استخدم السمات (على سبيل المثال[SetShowTotals](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/setshowtotals/) و[GetListColumns](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/getlistcolumns/)إلخ) للفئة `[ListObject]` للتحكم في القائمة.

في المثال الموضح أدناه، قمنا بإنشاء نفس `[ListObject]` باستخدام Aspose.Cells API كما أنشأنا باستخدام Microsoft Excel في القسم أعلاه.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-CreatingListObjects-new.cpp" >}}
##  **تنسيق جدول**
لإدارة مجموعة من البيانات المرتبطة وتحليلها، من الممكن تحويل نطاق من الخلايا إلى كائن قائمة (يُعرف أيضًا باسم جدول Excel). الجدول عبارة عن سلسلة من الصفوف والأعمدة التي تحتوي على بيانات مرتبطة تتم إدارتها بشكل مستقل عن البيانات الموجودة في الصفوف والأعمدة الأخرى. بشكل افتراضي، يتم تمكين التصفية في صف الرأس لكل عمود في الجدول بحيث يمكنك تصفية بيانات كائن القائمة أو فرزها بسرعة. يمكنك إضافة صف إجمالي (صف خاص في قائمة يوفر مجموعة مختارة من الوظائف التجميعية المفيدة للعمل مع البيانات الرقمية) إلى كائن القائمة الذي يوفر قائمة منسدلة للوظائف التجميعية لكل خلية صف الإجماليات. Aspose.Cells يوفر خيارات لإنشاء وإدارة القوائم (أو الجداول).
###  **تنسيق كائن القائمة**
 Aspose.Cells يوفر فئة[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) الذي يمثل ملف Excel Microsoft. ال[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) يحتوي الفصل على[أوراق عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) فصل. ال[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) يوفر الفصل مجموعة واسعة من الأساليب لإدارة أوراق العمل. لخلق*ListObject*في ورقة العمل، استخدم `ListObjectCollection`. كل `[ListObject]` هو في الواقع كائن من فئة `ListObjectCollection`، مما يوفر المزيد[يضيف](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/)طريقة لإضافة كائن `[ListObject]` وتحديد نطاق الخلايا التي يجب أن يشملها. وفقا لمجموعة محددة من الخلايا، أ*ListObject* تم إنشاؤه في ورقة العمل بواسطة Aspose.Cells. استخدم السمات (على سبيل المثال،[SetTableStyleType](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/settablestyletype/)) للفئة `[ListObject]` لتنسيق الجدول حسب متطلباتك.

يضيف المثال أدناه بيانات نموذجية إلى ورقة عمل، ويضيف `[ListObject]` ويطبق الأنماط الافتراضية عليها. أنماط `[ListObject]` مدعومة بـ Microsoft Excel 2007/2010.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-FormatTable-new.cpp" >}}
