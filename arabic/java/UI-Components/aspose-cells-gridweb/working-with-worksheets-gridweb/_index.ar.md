---
title: العمل مع صفحات العمل الخاصة بـ GridWeb
type: docs
weight: 30
url: /ar/java/working-with-worksheets-gridweb/
---

## **الوصول إلى صفحات العمل**

يتناول هذا الموضوع الوصول إلى صفحات العمل لتحكم GridWeb. يمكننا أيضًا تسمية هذه الصفحات بصفحات ويب لأنها تنتمي إلى GridWeb وتُستخدم في تطبيقات الويب.

جميع صفحات العمل الواردة في تحكم GridWeb مخزنة في مجموعة GridWorksheetCollection لتحكم GridWeb. من السهل الوصول إلى صفحة العمل معينة عن طريق فهرس الصفحة الخاص بها.

يمكن للمطورين الوصول إلى صفحة العمل المحددة عن طريق تحديد فهرس الصفحة كما هو موضح أدناه في مقتطف الكود المثالي.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingWorksheet-AccessingWorksheet.jsp" >}}

## **إزالة ورقة العمل**

يقدم هذا الموضوع معلومات موجزة حول إزالة أوراق العمل من ملفات Microsoft Excel باستخدام واجهة برمجة تطبيقات GridWeb. احذف ورقة عمل عن طريق تحديد فهرسها.

يمكن للمطورين إزالة ورقة عمل معينة عن طريق تحديد فهرسها باستخدام طريقة removeAt في مجموعة GridWorksheetCollection على النحو الموضح في رمز المثال أدناه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingWorksheet-RemovingWorksheet.jsp" >}}

## **إضافة أوراق عمل**

الأوراق العمل هي جزء أساسي من GridWeb. يتم إدارة جميع البيانات وتخزينها في شكل أوراق عمل. يسمح GridWeb للمطورين بإضافة ورقة عمل أو أكثر إلى عنصر تحكم Aspose.Cells.GridWeb. يظهر هذا الموضوع النهج البسيط لإضافة أوراق عمل إلى GridWeb.

### **دون تحديد اسم الورقة**

أبسط طريقة لإضافة ورقة عمل إلى Aspose.Cells.GridWeb هو استدعاء طريقة add في فئة GridWorksheetCollection في عنصر التحكم GridWeb. ينشئ هذا الطرق أوراق عمل تستخدم أسماء افتراضية (مثل Sheet1، Sheet2، Sheet3 وهلم جرا) ويضيفها إلى عنصر التحكم GridWeb.

**النتيجة: تمت إضافة ورقة عمل بالاسم الافتراضي إلى GridWeb** 

![todo:image_alt_text](working-with-worksheets-gridweb_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithoutSpecificName-AddingWorksheetWithoutSpecificName.jsp" >}}

### **بتحديد اسم الورقة**

لإضافة ورقة عمل باسم معين إلى عنصر التحكم GridWeb بدلاً من استخدام نظام التسمية الافتراضي، قم باستدعاء الإصدار المكدس من الطريقة add التي تأخذ سلسلة الاسم المحددة SheetName. على سبيل المثال، يقوم المثال أدناه بإضافة ورقة عمل بالاسم Invoice.

**النتيجة: تمت إضافة ورقة عمل بالاسم المحدد إلى GridWeb** 

![todo:image_alt_text](working-with-worksheets-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithSpecificName-AddingWorksheetWithSpecificName.jsp" >}}

{{% alert color="primary" %}}

تعيد الطريقة add() فهرس الورقة الجديدة الذي يمكن استخدامه للوصول إلى مثيل هذه الورقة. لمزيد من التفاصيل حول كيفية الوصول إلى الأوراق العمل، اقرأ [الوصول إلى الأوراق العمل](/cells/ar/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

## **إعادة تسمية ورقة العمل**

إعادة تسمية ورقة العمل يمكن أن تكون مفيدة جدًا عند العمل مع العديد من الأوراق العمل في GridWeb وتقرر تغيير أسمائها لجعلها أكثر معنى. على سبيل المثال، يمكن إعادة تسمية ورقة عمل تحتوي على فاتورة إلى Invoice بدلاً من Sheet1. يصف هذا الموضوع هذه الميزة البسيطة ولكن المفيدة.

### **إعادة تسمية ورقة العمل**

تحتوي جميع الأوراق العمل على خاصية Name التي تسمح للمطورين بالوصول إلى أسماء الأوراق العمل أو تعديلها. لإعادة تسمية ورقة العمل:

1. الوصول إلى ورقة العمل من GridWorksheetCollection.
2. إعادة تسمية الورقة المحددة.

{{% alert color="primary" %}}

لمزيد من التفاصيل حول الوصول إلى الأوراق العمل في Aspose.Cells.GridWeb، يرجى الرجوع إلى [الوصول إلى الأوراق العمل](/cells/ar/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

قبل تنفيذ الكود، تحتوي ورقة العمل على اسم افتراضي، مثل Sheet1.

**ملف الإدخال: ورقة عمل باسم افتراضي Sheet1** 

![todo:image_alt_text](working-with-worksheets-gridweb_3.png)

بعد تشغيل الكود، يتم إعادة تسمية ورقة العمل باسم الفاتورة.

الناتج: تم إعادة تسمية ورقة العمل باسم الفاتورة 

![todo:image_alt_text](working-with-worksheets-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RenamingWorksheet-RenamingWorksheet.jsp" >}}

## **نسخ صفحة العمل**

[إضافة الأوراق العمل](/cells/ar/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-addingworksheets) تصف كيفية إضافة أوراق عمل جديدة إلى GridWeb. من الممكن أيضًا إضافة نسخة (أو نسخة طبق الأصل) من ورقة عمل أخرى إلى تحكم Aspose.Cells.GridWeb. يمكن أن يكون هذا الميزة مفيدًا عندما يكون للبيانات المتطابقة أو المماثلة في ورقة عمل واحدة أيضًا مطلوبة في ورقة عمل أخرى. عندئذٍ، من الأسهل نسخ ورقة العمل الحالية وإضافتها إلى Aspose.Cells.GridWeb كورقة عمل جديدة بدلاً من إنشائها من الصفر.

### **باستخدام فهرس الصفحة**

يوضح الشيفرة المثالية أدناه كيفية إضافة نسخة من ورقة العمل إلى تحكم GridWeb عن طريق تحديد فهرس الورقة في طريقة addCopy لمجموعة GridWorksheetCollection.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetIndex-CopyWorksheetUsingSheetIndex.jsp" >}}
### **باستخدام اسم الصفحة**
يوضح الشيفرة المثالية أدناه كيفية إضافة نسخة من ورقة العمل إلى تحكم GridWeb عن طريق تحديد اسم الورقة في طريقة addCopy لمجموعة GridWorksheetCollection.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetName-CopyWorksheetUsingSheetName.jsp" >}}

{{% alert color="primary" %}}

تُرجع طريقة addCopy فهرس الورقة المضافة حديثًا الذي يمكن استخدامه للوصول إلى مثيل ورق العمل. لمزيد من التفاصيل حول كيفية الوصول إلى الأوراق العمل، اقرأ [الوصول إلى الأوراق العمل](/cells/ar/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

## **العمل مع النطاقات المسماة**

عادةً ما تُستخدم التسميات الخاصة بالأعمدة والصفوف للإشارة إلى الخلايا بشكل فريد، ولكن يمكنك إنشاء أسماء وصفية لتمثيل الخلايا أو مجموعات الخلايا أو الصيغ أو القيم الثابتة.

قد تشير كلمة الـ **اسم** إلى سلسلة من الأحرف التي تمثل خليةً أو مجموعة من الخلايا أو صيغةً أو قيمةً ثابتة. على سبيل المثال، يُمكن استخدام أسماء سهلة الفهم، مثل المنتجات، للإشارة إلى نطاقات صعبة الفهم، مثل Sales!C20:C30.

يمكن استخدام العلامات في الصيغ التي تشير إلى البيانات على نفس ورقة العمل. إذا كنت ترغب في تمثيل نطاق على ورقة عمل أخرى، قد تستخدم اسم. **نطاقات المسميات** هي واحدة من أكثر الميزات قوة في Microsoft Excel.

يمكن للمستخدمين تعيين اسم لنطاق واستخدام ذلك الاسم في الصيغ. تدعم Aspose.Cells.GridWeb هذه الميزة.

### **إضافة/الإشارة إلى النطاقات المسماة في الصيغ**

يوفر تحكم GridWeb صنفين (GridName وGridNameCollection) للعمل مع النطاقات المسماة.

ستساعدك مقطعة الشيفرة التالية على فهم كيفية استخدامها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingNamedRangesinFormulas-AddingNamedRangesinFormulas.jsp" >}}

## **إدارة التعليقات في ورقة العمل**

يناقش هذا الموضوع إضافة التعليقات، والوصول إليها، وإزالتها من الأوراق العمل. التعليقات مفيدة لإضافة ملاحظات أو معلومات مفيدة للمستخدمين الذين سيعملون مع الورقة. لدى المطورين مرونة في إضافة التعليقات إلى أي خلية من ورقة العمل.

### **العمل مع التعليقات**

#### **إضافة التعليقات**

لإضافة تعليق إلى ورقة العمل، يرجى اتباع الخطوات التالية:

1. أضف عنصر تحكم Aspose.Cells.GridWeb إلى نموذج الويب.
1. الوصول إلى ورقة العمل التي ترغب في إضافة تعليقات إليها.
1. أضف تعليقًا لخلية.
1. تحديد ملاحظة للتعليق الجديد.

**تمت إضافة تعليق إلى ورقة العمل** 

![todo:image_alt_text](working-with-worksheets-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingComments-AddingComments.jsp" >}}

#### **الوصول إلى التعليقات**

للوصول إلى تعليق:

1. الوصول إلى الخلية التي تحتوي على التعليق.
1. الحصول على إشارة الخلية.
1. تمرير الإشارة إلى مجموعة التعليقات للوصول إلى التعليق.
1. الآن يمكن تعديل خصائص التعليق.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingComments-AccessingComments.jsp" >}}

#### **إزالة التعليقات**

لإزالة تعليق:

1. الوصول إلى الخلية كما هو موضح أعلاه.
1. استخدام طريقة removeAt في مجموعة التعليقات لإزالة التعليق.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingComments-RemovingComments.jsp" >}}

## **إدارة الروابط الفعلية في ورقة العمل**

يناقش هذا الموضوع أنواع الروابط الفعلية المعتمدة في Aspose.Cells.GridWeb وكيفية إدارتها برمجياً. يمكن استخدام الروابط الفعلية إما لإنشاء روابط إلى عناوين الويب أو لإجراء استدعاء مرتجع إلى خادم.

### **أنواع الروابط الفعلية**

تدعم الروابط الفرعية التالية التي يتم دعمها بواسطة Aspose.Cells.GridWeb:

- الروابط النصية URL، الروابط التي تطبق على النص.
- الروابط URL للصور، الروابط التطبق على الصور.

#### **روابط URL نصية**

المثال أدناه يضيف رابطين فرعيين إلى ورقة العمل. أحدهما له هدف _blank بينما الآخر مضبوط على _parent.

![todo:image_alt_text](working-with-worksheets-gridweb_6.png)

**الناتج: روابط نصية مضافة إلى ورقة العمل**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-TextURLHyperlinks-TextURLHyperlinks.jsp" >}}

#### **روابط URL للصور**

المثال أدناه يضيف رابط URL للصورة إلى ورقة العمل.

![todo:image_alt_text](working-with-worksheets-gridweb_7.png)

**الناتج: رابط الصورة مضاف إلى ورقة العمل**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-ImageURLHyperlinks-ImageURLHyperlinks.jsp" >}}

## **فرز البيانات**

الفرز ميزة قيمة للغاية عندما يتعلق الأمر بمعالجة البيانات. البيانات غير المرتبة تسبب صعوبة للمستخدمين عند البحث عن معلومات محددة. تدعم Aspose.Cells.GridWeb ميزات فرز قوية. يناقش هذا الموضوع فرز البيانات باستخدام واجهة برمجة التطبيقات Aspose.Cells.GridWeb.

تسمح Aspose.Cells.GridWeb للمطورين بفرز البيانات بشكل أفقي وعمودي بحيث يمكن للمطورين فرز البيانات من الأعلى إلى الأسفل أو من اليسار إلى اليمين.

### **من الأعلى إلى الأسفل**

لفرز البيانات من أعلى إلى أسفل: 

1. أضف عنصر تحكم Aspose.Cells.GridWeb إلى نموذج الويب الخاص بك.
1. قم بالوصول إلى ورقة العمل التي ترغب في فرزها.
3. قم بفرز نطاق البيانات بأي ترتيب (تصاعدي أو تنازلي). تأكد من تحديد التوجيه من الأعلى إلى الأسفل.

المثال أدناه يقوم بفرز البيانات في عمودين (معرف الطالب واسم الطالب) من ورقة العمل بترتيب تصاعدي. يتم فرز اثني عشر صفًا فقط من عمودين باتجاه الأعلى إلى الأسفل.

قبل تطبيق الكود، تحتوي ورقة العمل على بيانات غير مرتبة.

**المدخلات: البيانات غير المرتبة** 

![todo:image_alt_text](working-with-worksheets-gridweb_8.png)

بعد تنفيذ الكود، يتم فرز البيانات بترتيب تصاعدي.

**الناتج: تم فرز البيانات من الأعلى إلى الأسفل بترتيب تصاعدي** 

![todo:image_alt_text](working-with-worksheets-gridweb_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromtoptobottomascendingorder-datasortedfromtoptobottomascendingorder.jsp" >}}

### **من اليسار إلى اليمين**

لفرز البيانات من اليسار إلى اليمين:

1. أضف عنصر تحكم Aspose.Cells.GridWeb إلى نموذج الويب الخاص بك.
1. قم بالوصول إلى ورقة العمل التي ترغب في فرزها.
1. قم بفرز مجموعة البيانات بأي ترتيب (تصاعدي أو تنازلي). تأكد من تحديد اليسار إلى اليمين.

المثال أدناه يقوم بفرز البيانات في صفين (معرف الطالب واسم الطالب) بترتيب تصاعدي. يتم فرز صفين فقط من أصل أربعة أعمدة من اليسار إلى اليمين.

قبل تطبيق الكود، تحتوي ورقة العمل على بيانات غير مرتبة.

**الإدخال: البيانات الغير مرتبة قبل تنفيذ مقتطف الكود** 

![todo:image_alt_text](working-with-worksheets-gridweb_10.png)

بعد تنفيذ الكود، تم فرز البيانات بترتيب تصاعدي.

**الناتج: تم فرز البيانات من اليسار إلى اليمين بترتيب تصاعدي** 

![todo:image_alt_text](working-with-worksheets-gridweb_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromleftrightascendingorder-datasortedfromleftrightascendingorder.jsp" >}}

## **البحث والاستبدال**

أحد أسرع الطرق لإجراء تغييرات متكررة في جدول بيانات كبير هو استخدام ميزة البحث والاستبدال. يساعدك البحث في تحديد سلسلة نصية أو بيانات ويقوم الاستبدال بتعويضها بقيمة جديدة. توفر Aspose.Cells.GridWeb هذه الميزة. فهو يتيح لك البحث والاستبدال بسلسلة نصية محددة أو قيمة في جانب العميل لورقة العمل من خلال حوار بسيط. حتى يسمح لك بالبحث عن بيانات جزئية.

### **حوار البحث/الاستبدال**

هناك طريقتان لفتح حوار البحث/الاستبدال:

1. عندما يكون العنصر التحكم نشطًا، اضغط على **CTRL+F** لفتح الحوار، أو اضغط على مفتاح **CTRL+R** لفتح الحوار مع تمكين زر **Replace**.
1. حرك المؤشر إلى منطقة الخلية في ورقة العمل، ثم انقر بالزر الأيمن. حدد **بحث** أو **استبدال** من القائمة.

**تحديد البحث**

![todo:image_alt_text](working-with-worksheets-gridweb_12.png)

يتم عرض حوار البحث والاستبدال.

حوار البحث/الاستبدال

![todo:image_alt_text](working-with-worksheets-gridweb_13.png)

استخدام البحث

للبحث:

1. افتح حوار البحث/الاستبدال.
1. اكتب السلسلة التي ترغب في البحث عنها في حقل البحث.
1. انقر فوق "البحث عن الأتي" للبحث.

يتم تحديد الخلية التالية التي تطابق شرط البحث الخاص بك.

{{% alert color="primary" %}}

إذا لم يتم العثور على المعيار الخاص بالبحث الخاص بك، يتم عرض صندوق حوار يخبرك.

{{% /alert %}}

### **خيارات البحث**

هناك بعض خيارات البحث التي يمكنك تخصيصها في الحوار. الجدول أدناه يقوم بتسجيلها.

|**لا.**|**اسم الخيار**|**الوصف**|
| :- | :- | :- |
|1|مطابقة الحالة|تشير ما إذا كان سيرتك الذاتية تستخدم بحثاً حساسًا لحالة الأحرف أم لا.|
|2|مطابقة الكلمة الكاملة|تشير ما إذا كان يتوجب مطابقة الكلمة بأكملها في البحث أم لا.|
|3|البحث لأعلى|تشير ما إذا كان البحث سيتم من الأسفل إلى الأعلى أم لا.|
|4|التعبير العادي|عند التحقق، سيعامل الضابط السلسلة في مربع نص البحث على أنها تعبير عادي في عملية البحث.|
|5|البحث في الصيغ/القيم|عند تحديد الصيغ، سيطابق الضابط الصيغة أو القيمة غير المنسقة للخلايا إذا كانت الصيغة أو القيمة غير المنسقة موجودة. عند تحديد القيم، سيقوم الضابط بمطابقة القيمة المعروضة للخلايا فقط.|

### **استخدام الاستبدال**

لاستبدال النص أو القيم:

1. افتح حوار مربع البحث/الاستبدال عن طريق الضغط على **CTRL+F**, أو حدد النقر بزر الماوس الأيمن على خلية ما ثم حدد **البحث** قبل النقر على **استبدال**.
1. اكتب السلسلة البديلة في حقل **استبدال ب**.
1. انقر **استبدال**.

لاستبدال النص:

1. افتح صندوق الحوار.
1. أدخل النص الذي تريد العثور عليه في مجال **البحث عن**، والنص الذي تريد استبداله في مجال **الاستبدال بـ**.
1. استبدال حدوث واحد في كل مرة بالنقر على **العثور على التالي** تليه **استبدال**.
1. إذا كنت متأكدًا جدًا مما تحتويه ورقة العمل، انقر على **استبدال الكل**.

{{% alert color="primary" %}}

إذا كان ورقة العمل ليست في وضع التحرير، لن يتم عرض زر **استبدال**.

{{% /alert %}}

## إضافة/إزالة الروابط التشعبية من الجانب العميل

Aspose.Cells GridWeb الآن يدعم إضافة وإزالة الروابط التشعبية من الجانب العميل. لهذا الغرض، يوفر الواجهة البرمجية للمستخدم الوظائف "addCelllink" و "delCelllink". يظهر مقتطفات الكود التالية إضافة وإزالة الروابط التشعبية من الجانب العميل في GridWeb.

### مثال على الكود

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-1.jsp" >}}

يمكنك أيضًا الارتباط بورقة باستخدام مقتطف الكود التالي.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-2.jsp" >}}

## تحديث إعدادات الخط من الجانب العميل

يدعم الآن Aspose.Cells GridWeb تغيير إعدادات الخط من الجانب العميل. لذلك، توفر الواجهة البرمجية التالية الوظائف

- **updateCellFontStyle**: Params - r/i/b/ib للعادي/مائل/عريض/مائل && عريض
- **updateCellFontSize**: Params - fontname، الخ.
- **updateCellFontName**: Params - fontsize، الخ. '12pt'
- **updateCellFontColor**: المعلمات - لا شيء/تسطير/يتميز/تسطير&&يتميز
- **updateCellFontLine**: المعلمات - لون html مثل #aa22ee أو اسم لون معروف مثل أخضر، أحمر، ...
- **updateCellBackGroundColor**: المعلمات - لون html مثل #aa22ee أو اسم لون معروف مثل أخضر، أحمر، ...

الكود البرمجي التالي يوضح تغيير إعدادات الخط من الجانب العميل في GridWeb.

### مثال على الكود

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-update_font_from_client_side-1.jsp" >}}

## إضافة/إزالة التعليقات من الجانب العميل

Aspose.Cells GridWeb الآن يدعم إضافة وإزالة التعليقات من الجانب العميل. لهذا الغرض، يوفر الواجهة البرمجية للمستخدم الوظائف "addcomments" و "delcomments". يظهر مقتطف الكود التالي إضافة وإزالة التعليقات من الجانب العميل في GridWeb.

### مثال على الكود

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add_remove_comments_from_client_side.jsp" >}}

## إظهار الأزرار لإضافة/إزالة أوراق العمل

يدعم Aspose.Cells GridWeb الآن إضافة وإزالة الأوراق عن طريق استخدام الأزرار في شريط الأدوات. ليكونت الأزرار مرئية على الواجهة الأمامية، يجب عليك ضبط **GridWeb1.ShowAddButton** إلى **true**. توضح مقتطفات الكود التالية إضافة أزرار الإضافة/الإزالة إلى شريط أدوات GridWeb.

### مثال على الكود

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "GridWeb-show_add_remove_worksheet_buttons.java" >}}
