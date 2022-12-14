---
title: العمل مع GridWeb
type: docs
weight: 20
url: /ar/java/working-with-gridweb/
---
## **فتح ملف إكسل Microsoft**

Aspose.Cells. يمكن للتحكم في شبكة الويب فتح وتحميل ملفات Excel Microsoft - كاملة مع البيانات والتنسيق والرسوم البيانية والصور وما إلى ذلك. يوضح هذا الموضوع كيفية القيام بذلك.

لفتح ملف Excel باستخدام عنصر تحكم GridWeb:

1. قم بإضافة عنصر تحكم Aspose.Cells.GridWeb إلى نموذج أو صفحة ويب.
1. قم باستيراد ملف Excel عن طريق تحديد مسار الملف.
1. قم بتشغيل التطبيق أو افتح الصفحة.

لتحميل المحتوى من ملف Excel إلى عنصر تحكم Aspose.Cells.GridWeb ، يجب عليك استدعاء الأسلوب importExcelFile لتحديد مسار ملف Excel. بعد ذلك ، سيجد تحكم GridWeb تلقائيًا الملف من المسار المحدد ويعرض محتوياته فيه. يتم توفير مقتطف التعليمات البرمجية الذي يقوم بتحميل محتويات ملف Excel أدناه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-OpeningfromFile-OpeningfromFile.jsp" >}}

يمكن استخدام مقتطف الشفرة أعلاه بالطريقة التي تريدها. على سبيل المثال ، لتحميل ملف Excel تلقائيًا عند تحميل نموذج ويب ، أضف هذا الرمز إلى حدث Page_Load للنموذج الذي حددته بنفسك.

**يتم تحميل ملف Excel في GridWeb**

![ما يجب القيام به: image_بديل_نص](working-with-gridweb_1.png)

## **حفظ ملف Microsoft Excel**

من الممكن إنشاء ملفات Excel جديدة أو معالجة Microsoft موجودة ، على مواقع الويب في وضع واجهة المستخدم الرسومية باستخدام Aspose.Cells.GridWeb control. يمكن بعد ذلك حفظ الملفات في ملفات Excel. Aspose.Cells.GridWeb يعمل بشكل فعال كمحرر جداول بيانات على الإنترنت. يصف هذا الموضوع كيفية حفظ محتوى الشبكة في ملفات Excel.

### **الحفظ كملف**

لحفظ محتوى عنصر تحكم Aspose.Cells.GridWeb كملف Excel:

1. قم بإضافة عنصر تحكم Aspose.Cells.GridWeb إلى نموذج أو صفحة ويب.
1. احفظ عملك كملف Excel في مسار محدد.
1. قم بتشغيل التطبيق أو افتح الصفحة.

يوضح مثال الكود أدناه كيفية حفظ محتوى الشبكة في ملف Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-SavingasFile-SavingasFile.jsp" >}}

 يمكن استخدام مقتطف الشفرة أعلاه بعدة طرق. من الطرق الشائعة إضافة زر يحفظ محتوى الشبكة في ملف Excel عند النقر فوقه. Aspose.Cells.GridWeb يقدم طريقة أسهل للمهمة. Aspose.Cells.GridWeb له حدث يسمى SaveCommand. يمكن إضافة مقتطف الشفرة أعلاه إلى معالج الحدث SaveCommand والذي يسمح للمستخدمين بحفظ عملهم بالنقر فوق Aspose.Cells.GridWeb's المدمج**يحفظ** زر.

## **تغيير حجم Aspose.Cells.GridWeb وشريط رأسه**

يشرح هذا المقال كيفية القيام بتغيير حجم GridWeb في وقت التشغيل باستخدام Aspose.Cells.GridWeb API. كما يشرح كيفية تغيير حجم أشرطة الرأس لعنصر التحكم Aspose.Cells.GridWeb لتسهيل قراءة البيانات الخاصة بهم.

### **تغيير العرض والارتفاع Aspose.Cells.GridWeb**

تغيير عرض وارتفاع Aspose.Cells. يعد التحكم في شبكة الويب ميزة بسيطة ولكنها مهمة. يتم تمثيل عنصر تحكم Aspose.Cells.GridWeb بواسطة فئة GridWeb في API. لتغيير حجم عرض وارتفاع عنصر تحكم GridWeb ، ما عليك سوى استخدام خصائص العرض والارتفاع الخاصة به.

{{% alert color="primary" %}}

يمكن تحديد عرض وارتفاع عنصر التحكم بالبكسل أو بالنقاط.

{{% /alert %}}

يظهر أدناه إخراج مقتطف الشفرة التالي.

**عرض وارتفاع عنصر تحكم الشبكة المتغيرة**

![ما يجب القيام به: image_بديل_نص](working-with-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangedwidthheightofGridWebcontrol-ChangedwidthheightofGridWebcontrol.jsp" >}}

### **تغيير عرض وارتفاع شريط الرأس**

Aspose.Cells. يحتوي عنصر تحكم شبكة الويب على شريطين للرأس كما يلي:

- شريط الرأس العلوي ، يمثل شريط الرأس هذا أعمدة مثل A ، B ، C ، D ، إلخ.
- شريط الرأس الأيسر ، يمثل شريط الرأس هذا الصفوف مثل 1 ، 2 ، 3 ، 4 ، إلخ.

يتم عرض كل من أشرطة الرأس هذه أدناه.

**أشرطة الرأس**

![ما يجب القيام به: image_بديل_نص](working-with-gridweb_3.png)

قم بتغيير ارتفاع شريط الرأس العلوي وعرض شريط الرأس الأيسر باستخدام خصائص HeaderBarHeight و HeaderBarWidth لعنصر تحكم GridWeb على التوالي. يوضح الشكل أدناه إخراج مثال الكود التالي.

**تم تغيير عرض شريط الرأس وارتفاعه**

![ما يجب القيام به: image_بديل_نص](working-with-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangingWidthandHeightofHeaderBar-ChangingWidthandHeightofHeaderBar.jsp" >}}

## **العمل مع Aspose.Cells.GridWeb Events**

يجب أن يكون جميع المطورين على دراية بالأحداث والغرض منها. تُستخدم الأحداث لإرسال إخطارات بالتغييرات التي قد تحدث في عنصر تحكم أو فئة. Aspose.Cells.GridWeb له العديد من الأحداث التي يمكن استخدامها لأداء مهام محددة عند حدوث تغييرات معينة في عنصر التحكم.

يوفر هذا الموضوع مقدمة عن كافة الأحداث التي يدعمها عنصر تحكم Aspose.Cells.GridWeb بالإضافة إلى بعض التفاصيل حول كيفية التعامل مع هذه الأحداث.

### **مقدمة لأحداث الشبكة**

Aspose.Cells. يدعم التحكم في شبكة الويب العديد من الأحداث التي توفر مزيدًا من التحكم لتنفيذ العمليات عند تشغيل أحداث معينة في عنصر التحكم. قائمة كاملة بالأحداث التي يدعمها Aspose.Cells. يمكن العثور على عنصر تحكم شبكة الويب أدناه.

|**الأحداث**|**وصف**|
|:- |:- |
|سيلكوماند|يحدث عند النقر فوق الارتباط التشعبي لأمر خلية. عند إطلاق هذا الحدث ، توفر المعلمة e.Argument اسم الأمر.|
|CellDoubleClick|يحدث عندما يتم النقر نقرًا مزدوجًا على الخلية.|
|العمود محذوف|يحدث عندما يحذف المستخدم عمودًا من ورقة عمل باستخدام قائمة جانب العميل.|
|العمود حذف|يحدث عندما يحاول المستخدم حذف عمود من ورقة العمل باستخدام قائمة جانب العميل.|
|العمود DoubleClick|يحدث عندما يتم النقر نقرًا مزدوجًا فوق رأس العمود.|
|العمود مُدرج|يحدث عندما يُدرج المستخدم عمودًا في ورقة عمل باستخدام قائمة جانب العميل.|
|CustomCommand|يحدث عندما ينقر المستخدم فوق زر أمر مخصص.|
|LoadCustomData|يحدث عندما يتم تعيين خاصية EnableSession لعنصر التحكم على false وتحتاج إلى تحميل بيانات ورقة العمل. يمكنك معالجة هذا الحدث في الوضع بدون جلسات لتحميل بيانات ورقة العمل من ملف أو قاعدة بيانات.|
|PageIndexChanged|يحدث عندما يتم تغيير فهرس صفحة ورقة عنصر التحكم.|
|تم حذف الصف|يحدث عندما يقوم المستخدم بحذف صف من ورقة العمل باستخدام قائمة جانب العميل.|
|RowDeleting|يحدث عندما يحاول المستخدم حذف صف من ورقة العمل باستخدام قائمة جانب العميل.|
|RowDoubleClick|يحدث عند النقر المزدوج فوق رأس الصف.|
|تم إدراجها|يحدث عندما يُدرج المستخدم صفًا في ورقة العمل باستخدام قائمة جانب العميل.|
|SaveCommand| يحدث عندما يكون ملف**يحفظ** تم النقر فوق الزر.|
|SheetTabClick|يحدث عند النقر فوق علامة تبويب الورقة.|
|إرسال| يحدث عندما يكون ملف**يُقدِّم** تم النقر فوق الزر.|
|UndoCommand| يحدث عندما يكون ملف**الغاء التحميل** تم النقر فوق الزر.|
|أياكس كول|حرائق عند انتهاء تحديث AJAX لعنصر التحكم. (يجب تعيين EnableAJAX على صحيح).|
|CellModifiedOnAjax|تشغيل عند تعديل الخلية في مكالمة AJAX.|
|AfterColumnFilter|حرائق عند تطبيق عامل التصفية على عمود.|

### **معالجة أحداث الشبكة**

لإجراء عملية محددة عند تشغيل حدث معين ، يتعين علينا إنشاء معالج حدث. يقوم معالج الأحداث بتنفيذ المهمة المطلوبة عند تشغيل حدث معين. يوضح المثال التالي كيفية التعامل مع حدث شبكة بسيط.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HandlingGridEvents-HandlingGridEvents.jsp" >}}

## **العمل مع أحداث النقر المزدوج**

يحتوي Aspose.Cells.GridWeb على ثلاثة أنواع من أحداث النقر المزدوج:

- CellDoubleClick ، يتم تشغيله عند النقر نقرًا مزدوجًا على خلية.
- ColumnDoubleClick ، يتم تشغيله عند النقر نقرًا مزدوجًا فوق رأس العمود.
- RowDoubleClick ، يتم تشغيله عند النقر نقرًا مزدوجًا فوق رأس صف.

يناقش هذا الموضوع كيفية تمكين أحداث النقر المزدوج في Aspose.Cells.GridWeb. كما يناقش إنشاء معالجات الأحداث لهذه الأحداث.

### **تمكين أحداث النقر المزدوج**

يمكن تمكين جميع أنواع أحداث النقر المزدوج من جانب العميل عن طريق تعيين خاصية EnableDoubleClickEvent للتحكم في GridWeb إلى true.

{{% alert color="primary" %}}

بشكل افتراضي ، يتم تعيين الخاصية EnableDoubleClickEvent على false. هذا يعني أن أحداث النقر المزدوج لا يتم تمكينها افتراضيًا. لتنفيذ مثل هذه الأحداث ، قم أولاً بتمكين الميزة.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-EnablingDoubleClickEvents-EnablingDoubleClickEvents.jsp" >}}

بمجرد تمكين النقر المزدوج فوق الأحداث ، من الممكن إنشاء معالجات الأحداث لأي أحداث انقر نقرًا مزدوجًا عليها. تؤدي معالجات الأحداث هذه مهامًا محددة عند تشغيل حدث نقر مزدوج معين.

### **معالجة أحداث النقر المزدوج**

#### **انقر نقرًا مزدوجًا فوق Cell**

يوفر معالج الحدث للحدث CellDoubleClick وسيطة من النوع CellEventArgs ، والتي توفر المعلومات الكاملة للخلية التي تم النقر عليها نقرًا مزدوجًا.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickCell-DoubleClickCell.jsp" >}}

#### **انقر نقرًا مزدوجًا فوق رأس العمود**

يوفر معالج الحدث لحدث ColumnDoubleClick وسيطة من النوع RowColumnEventArgs الذي يوفر رقم الفهرس للعمود للرأس الذي تم النقر فوقه نقرًا مزدوجًا ومعلومات أخرى.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickColumnHeader-DoubleClickColumnHeader.jsp" >}}

#### **انقر نقرًا مزدوجًا فوق رأس الصف**

يوفر معالج الحدث للحدث RowDoubleClick وسيطة من النوع RowColumnEventArgs الذي يوفر رقم الفهرس للصف الخاص بالرأس الذي تم النقر فوقه نقرًا مزدوجًا والمعلومات الأخرى ذات الصلة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickRowHeader-DoubleClickRowHeader.jsp" >}}

## **ضبط نمط أو مظهر Aspose.Cells.GridWeb**

Aspose.Cells.GridWeb له شكله وإحساسه الافتراضي ولكن من الممكن تغيير مظهره. Aspose.Cells.GridWeb يوفر العديد من الخصائص للسماح للمطورين بالتحكم الكامل في مظهره. هذا الموضوع يناقش بعض تلك الخصائص.

### **ضبط نمط أو مظهر Aspose.Cells.GridWeb**

#### **الأنماط المحددة مسبقًا**

لتوفير جهود المطورين ، يقدم Aspose.Cells.GridWeb بعض الأنماط المحددة مسبقًا. ما عليك سوى تحديد نمط من القائمة لتطبيق النمط.

|**الأنماط**|**نظام الألوان**|
|:- |:- |
|اساسي|فضة|
|ملون 1|ارتفع|
|ملون 2|أزرق|
|المهنية 1|ازرق سماوي|
|المهنية 2|مرة أخرى سماوي|
|تقليدي 1|مظلم|
|تقليدي 2|رمادي|
|العادة|حسب الطلب|
عند تحديد نمط معين ، فإنه يغير المظهر الكامل لعنصر التحكم GridWeb. يمكن للمطورين تحديد نمط محدد مسبقًا ليتم تطبيقه في وقت التشغيل باستخدام API المرن من Aspose.Cells.GridWeb.

يوفر عنصر التحكم GridWeb خاصية PresetStyle التي يمكن للمطورين تعيين أي نمط محدد مسبقًا مرغوب فيه.

يتم عرض إخراج مقتطف الشفرة أدناه أدناه.

**يتم تطبيق التحكم في GridWeb بنمط Colorful1 عليه**

![ما يجب القيام به: image_بديل_نص](working-with-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **نمط شريط الرأس**

إذا ألقيت نظرة على عنصر تحكم GridWeb ، ستلاحظ شريطين للرأس. واحد للأعمدة (أي A ، B ، C ، D ، إلخ) والآخر للصفوف (أي 1 ، 2 ، 3 ، 4 ، إلخ). Aspose.Cells.GridWeb يسمح للمطورين بالتحكم في مظهر أشرطة الرأس هذه. يمكن للمطورين تعيين نمط أشرطة الرأس في وقت التشغيل.

{{% alert color="primary" %}}

يوفر عنصر التحكم GridWeb خاصية HeaderBarStyle التي تطبق نمطًا على كل من أشرطة الرأس لعنصر التحكم.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **نمط شريط الجدولة**

من الممكن ضبط نمط شريط علامات التبويب أيضًا. يرجى الاطلاع على الكود التالي

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HeaderBarStyle-HeaderBarStyle.jsp" >}}

#### **تحميل ملف النمط**

لتطبيق إعدادات النمط من ملف نمط موجود للتحكم في GridWeb ، يمكن للمطورين تعيين مسار ملف النمط إلى خاصية CustomStyleFileName لعنصر التحكم. ولكن ، قبل القيام بذلك ، يجب تعيين خاصية PresetStyle لعنصر التحكم إلى Custom. وذلك لأن ملف النمط هذا يحتوي على معلومات نمط مخصصة تم تعريفها بالفعل من قبل المطور.

يرجى الاطلاع على الصورة التالية التي تظهر GridWeb مع النمط المخصص المطبق عليها.

![ما يجب القيام به: image_بديل_نص](working-with-gridweb_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-CustomStyleSheet-CustomStyleSheet.jsp" >}}

{{% alert color="primary" %}}

هام: لا يؤثر تحميل ملف النمط في عنصر تحكم GridWeb على إعدادات التنسيق لخلايا عنصر التحكم.

{{% /alert %}}

#### **نموذج لقالب نمط مخصص**

ها هو نموذج لقالب النمط المخصص. يمكنك تعديله حسب متطلباتك.

{{< highlight "java" >}}

 <aspose.excel.web.viewerStyletemplate runat="server" HeaderBarWidth="30pt" ScrollBarBaseColor="#AFEEEE" SelectCellBgColor="#FFFAF0" ActiveHeaderBgColor="#DAA520" ActiveCellBgColor="#DDDDFF" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LeftBorderStyle-BorderWidth="" FrameTableStyle-LeftBorderStyle-BorderColor="" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-RightBorderStyle-BorderWidth="" FrameTableStyle-RightBorderStyle-BorderColor="" FrameTableStyle-BorderWidth="1px" FrameTableStyle-CellSpacing="0" FrameTableStyle-BorderColor="#C0FFC0" FrameTableStyle-CellPadding="0" FrameTableStyle-TopBorderStyle-BorderWidth="" FrameTableStyle-TopBorderStyle-BorderColor="" FrameTableStyle-BackColor="#FFFFCC" FrameTableStyle-BottomBorderStyle-BorderWidth="" FrameTableStyle-BottomBorderStyle-BorderColor="" HeaderBarStyle-LeftBorderStyle-BorderWidth="" HeaderBarStyle-LeftBorderStyle-BorderColor="" HeaderBarStyle-verticalalign="Middle" HeaderBarStyle-RightBorderStyle-BorderWidth="" HeaderBarStyle-RightBorderStyle-BorderColor="" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-font-size="10pt" HeaderBarStyle-BorderColor="#00C0C0" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-horizontalalign="Center" HeaderBarStyle-ForeColor="Red" HeaderBarStyle-TopBorderStyle-BorderWidth="" HeaderBarStyle-TopBorderStyle-BorderColor="" HeaderBarStyle-BackColor="#D8BFD8" HeaderBarStyle-BottomBorderStyle-BorderWidth="" HeaderBarStyle-BottomBorderStyle-BorderColor="" ViewTableStyle-LeftBorderStyle-BorderWidth="" ViewTableStyle-LeftBorderStyle-BorderColor="" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-RightBorderStyle-BorderWidth="" ViewTableStyle-RightBorderStyle-BorderColor="" ViewTableStyle-BorderWidth="0px" ViewTableStyle-CellSpacing="0" ViewTableStyle-CellPadding="0" ViewTableStyle-TopBorderStyle-BorderWidth="" ViewTableStyle-TopBorderStyle-BorderColor="" ViewTableStyle-BottomBorderStyle-BorderWidth="" ViewTableStyle-BottomBorderStyle-BorderColor="" BottomTableStyle-LeftBorderStyle-BorderWidth="" BottomTableStyle-LeftBorderStyle-BorderColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-RightBorderStyle-BorderWidth="" BottomTableStyle-RightBorderStyle-BorderColor="" BottomTableStyle-Height="32pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-CellSpacing="0" BottomTableStyle-BorderColor="#80FF80" BottomTableStyle-CellPadding="0" BottomTableStyle-ForeColor="#FFE0C0" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="#FF69B4" BottomTableStyle-BottomBorderStyle-BorderWidth="" BottomTableStyle-BottomBorderStyle-BorderColor="" HeaderBarHeight="15pt" ActiveTabStyle-LeftBorderStyle-BorderWidth="" ActiveTabStyle-LeftBorderStyle-BorderColor="" ActiveTabStyle-RightBorderStyle-BorderWidth="" ActiveTabStyle-RightBorderStyle-BorderColor="" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-font-size="10pt" ActiveTabStyle-BorderColor="#00C0C0" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="#FF00FF" ActiveTabStyle-TopBorderStyle-BorderWidth="" ActiveTabStyle-TopBorderStyle-BorderColor="" ActiveTabStyle-BackColor="#80FFFF" ActiveTabStyle-BottomBorderStyle-BorderWidth="" ActiveTabStyle-BottomBorderStyle-BorderColor="" HeaderBarTableStyle-LeftBorderStyle-BorderWidth="" HeaderBarTableStyle-LeftBorderStyle-BorderColor="" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-RightBorderStyle-BorderWidth="" HeaderBarTableStyle-RightBorderStyle-BorderColor="" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-CellSpacing="0" HeaderBarTableStyle-CellPadding="0" HeaderBarTableStyle-TopBorderStyle-BorderWidth="" HeaderBarTableStyle-TopBorderStyle-BorderColor="" HeaderBarTableStyle-BackColor="#C0FFC0" HeaderBarTableStyle-BottomBorderStyle-BorderWidth="" HeaderBarTableStyle-BottomBorderStyle-BorderColor="" DefaultGridLineColor="#228B22" TabStyle-LeftBorderStyle-BorderWidth="" TabStyle-LeftBorderStyle-BorderColor="" TabStyle-RightBorderStyle-BorderWidth="" TabStyle-RightBorderStyle-BorderColor="" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-font-size="8pt" TabStyle-BorderColor="#8080FF" TabStyle-BorderStyle="Groove" TabStyle-ForeColor="#FFFFCC" TabStyle-TopBorderStyle-BorderWidth="" TabStyle-TopBorderStyle-BorderColor="" TabStyle-BackColor="#C0C0FF" TabStyle-BottomBorderStyle-BorderWidth="" TabStyle-BottomBorderStyle-BorderColor="" scrollbararrowColor="#778899"/>

{{< /highlight >}}

## **إنشاء التحكم في نموذج ويب**

ستوجهك هذه المقالة حول كيفية إنشاء نموذج ويب بسيط JSP (صفحة خادم Java) مع وجود تحكم GridWeb فيه.

**الخطوة 1 - إنشاء هيكل الدليل**

 تحتاج إلى إنشاء بنية الدليل التالية في ملف**تطبيقات الويب**دليل Tomcat Server

![ما يجب القيام به: image_بديل_نص](working-with-gridweb_7.png)

 هذه هي الدلائل والملفات التي تحتاج إلى إنشائها. يرجى قراءة التعليقات ومتابعتها. يمكنك الحصول على أحدث أرشيفات إصدار Aspose.Cells.GridWeb for Java من[هذا الرابط](https://downloads.aspose.com/cells/java).

{{< highlight "java" >}}

 SamplePageGridWebJava

SamplePageGridWebJava\grid

//Get acwclient directory from GridWeb latest release archive from Downloads section

SamplePageGridWebJava\acwclient

SamplePageGridWebJava\WEB-INF

SamplePageGridWebJava\WEB-INF\lib

//Get aspose-gridweb-x.x.x.jar file from GridWeb latest release archive from Downloads section

SamplePageGridWebJava\WEB-INF\aspose-gridweb-x.x.x.jar

SamplePageGridWebJava\WEB-INF\web.xml

SamplePageGridWebJava\head.jsp

//Create this excel file using Microsoft Excel or you can use any excel file and rename it SampleExcel.xlsx

SamplePageGridWebJava\SampleExcel.xlsx

SamplePageGridWebJava\SamplePage.jsp

{{< /highlight >}}

**الخطوة 2 - إضافة الأكواد في الملفات التي تم إنشاؤها**

يعرض هذا القسم رمز الملفات المختلفة التي تم إنشاؤها في بنية الدليل أعلاه. يرجى الحصول على هذه الرموز وإضافتها في ملفاتك عن طريق فتحها في برنامج "المفكرة" ونسخها / لصقها.

**Web.xml**

{{< highlight "java" >}}

 <?xml version="1.0" encoding="UTF-8"?>

<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://java.sun.com/xml/ns/javaee" xmlns:web="http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd" xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd" id="WebApp_ID" version="2.5">

  <display-name>testGridWeb</display-name>

  <welcome-file-list>

    <welcome-file>SamplePage.jsp</welcome-file>

  </welcome-file-list>

  <servlet>

    <display-name>GridWebServlet</display-name>

    <servlet-name>GridWebServlet</servlet-name>

    <servlet-class>com.aspose.gridweb.GridWebServlet</servlet-class>

  </servlet>

  <servlet-mapping>

    <servlet-name>GridWebServlet</servlet-name>

    <url-pattern>/GridWebServlet</url-pattern>

  </servlet-mapping>

</web-app>

{{< /highlight >}}

**head.jsp**

{{< highlight "java" >}}

 <%

String path = request.getContextPath();

String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";

%>

<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE9"/>

<base href="<%=basePath%>">

<script type="text/javascript" language="javascript"

	src="grid/acw_client/acwmain.js"></script>

<script type="text/javascript" language="javascript"

	src="grid/acw_client/lang_en.js"></script>

<link href="grid/acw_client/menu.css" rel="stylesheet" type="text/css" />

<style>

span.acwxc {

	overflow: hidden;

	border: none;

	display: block;

	white-space: pre;

}

</style>

<style>

span.rotation90 {

	width: 100%;

	height: 100%;

	border: none;

	-webkit-transform: rotate(-90deg);

	-moz-transform: rotate(-90deg);

	filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=3 );

	display: block

}

</style>

<style>

span.rotation-90 {

	filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=1 );

	width: 100%;

	height: 100%;

	border: none;

	-webkit-transform: rotate(90deg);

	-moz-transform: rotate(90deg);

	display: block

}

</style>

<style>

span.wrap {

	white-space: pre-wrap;

	white-space: -moz-pre-wrap;

	white-space: -pre-wrap;

	white-space: -o-pre-wrap;

	word-wrap: break-word;

	-ms-word-break: break-all;

}

</style>

{{< /highlight >}}

**SamplePage.jsp**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-SamplePage-SamplePage.jsp" >}}

**الخطوة 3 - تشغيل نموذج صفحة ويب JSP**

الآن لقد فعلت كل شيء. حان الوقت لتشغيل صفحة الويب. يرجى بدء خادم Tomcat الخاص بك ثم لصق عنوان URL التالي في متصفح الويب.

{{< highlight "java" >}}

 http://localhost:8080/SamplePageGridWebJava/SamplePage.jsp

{{< /highlight >}}

سترى شيئًا مثل لقطة الشاشة التالية. تهانينا ، لقد نجحت في استخدام عنصر التحكم GridWeb في صفحة JSP الخاصة بك.

![ما يجب القيام به: image_بديل_نص](working-with-gridweb_8.png)

## **طباعة GridWeb**

هناك أوقات يحتاج فيها المطورون إلى طباعة محتوى GridWeb المتضمن من صفحة ويب دون حفظ ملف Excel Microsoft. يدعم عنصر تحكم Aspose.Cells.GridWeb هذه الميزة.

### **طباعة GridWeb**

للطباعة دون حفظ ملف منفصل ، قم باستدعاء أسلوب طباعة () فئة GridWeb من جانب العميل لطباعة الشبكة. يمكنك اختيار بعض الأحداث المناسبة أيضًا.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-PrintingGridWeb-PrintingGridWeb.jsp" >}}

نظرًا لأنك تتصل به من جانب العميل ، فسيتعين عليك أولاً الحصول على معرف عميل الشبكة. يمكنك الحصول على معرف العميل باستخدام طريقة gridweb.getClientID ().

### **نموذج التعليمات البرمجية من جانب العميل**

يرجى الاطلاع على الرابط التالي الذي يستدعي طريقة gridweb.print () من جانب العميل.

**لغة البرمجة**

{{< highlight "java" >}}

 <a href="#" onclick='<%=gridweb.getClientID()%>.print(); '>Print Function of GridWeb</a>

{{< /highlight >}}

## **مقدمة عن أوضاع الشبكة المختلفة**

توضح هذه المقالة أوضاع Aspose.Cells.GridWeb المختلفة. يتم تمييز هذه الأوضاع منطقيًا بسبب ميزاتها وسلوكياتها المختلفة. لقد حددنا أنواعًا مختلفة من الوضع على النحو التالي:

- وضع التحرير
- نمط العرض

كل هذه الأنماط لها خصائصها الخاصة. يمكن للمطورين العمل مع Aspose.Cells.GridWeb في أي وضع وفقًا لمتطلباتهم. سننظر في كل وضع أدناه.

### **وضع التحرير**

بشكل افتراضي ، يكون عنصر التحكم Aspose.Cells.GridWeb في وضع التحرير. في وضع التحرير ، يمكنك تحرير محتوى الشبكة أو تعديله بالكامل باستخدام جميع الميزات التي يوفرها عنصر التحكم Aspose.Cells.GridWeb. تشمل هذه الميزات:

- حفظ محتوى الشبكة في Microsoft ملفات Excel.
- إرسال البيانات إلى الخادم.
- حساب الصيغ.
- التراجع عن الإجراءات السابقة أو إهمالها.
- إدارة الصفوف والأعمدة.
- قص أو نسخ أو لصق البيانات.
- تنسيق الخلايا وما إلى ذلك.

**التحكم في GridWeb في وضع التحرير**

![ما يجب القيام به: image_بديل_نص](working-with-gridweb_9.png)

يمكن للمطورين أيضًا التبديل إلى وضع التحرير برمجيًا عن طريق تعيين الخاصية EditMode لعنصر التحكم GridWeb إلى true.

### **مثال رمز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebEditMode-GridWebEditMode.jsp" >}}

### **نمط العرض**

عندما يكون عنصر التحكم GridWeb في وضع العرض ، لا يمكن للمستخدمين تحرير محتوى الشبكة أو تعديله ، مما يعني أنه يمكن للمستخدمين عرض محتوى الشبكة فقط. لهذا السبب يسمى هذا الوضع وضع العرض. في وضع العرض ، هناك بعض الأزرار (**يُقدِّم**, **يحفظ** و**الغاء التحميل** ) مخفية والقائمة التي تظهر عند النقر بزر الماوس الأيمن تحتوي فقط على ملف**ينسخ** و**تجد** اختيار.

**التحكم في الشبكة في وضع العرض** 

![ما يجب القيام به: image_بديل_نص](working-with-gridweb_10.png)

 إذا كان المطورون يرغبون في أن يقوم مستخدموهم بعرض البيانات فقط ، فيمكنهم التبديل إلى وضع العرض برمجيًا عن طريق تعيين خاصية EditMode للتحكم في GridWeb إلى**خاطئة**.

### **مثال رمز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebViewMode-GridWebViewMode.jsp" >}}

{{% alert color="primary" %}}

حتى في وضع العرض ، يمكن للمستخدمين تغيير ارتفاع وعرض الصفوف والأعمدة.

{{% /alert %}}
