---
title: العمل مع GridWeb
type: docs
weight: 20
url: /ar/java/working-with-gridweb/
---
##  **فتح ملف إكسل Microsoft**

Aspose.Cells. يمكن لعنصر تحكم GridWeb فتح وتحميل Microsoft من ملفات Excel - كاملة بالبيانات والتنسيقات والمخططات والصور وما إلى ذلك. يشرح هذا الموضوع كيفية القيام بذلك.

لفتح ملف Excel باستخدام عنصر تحكم GridWeb:

1. أضف عنصر التحكم Aspose.Cells.GridWeb إلى نموذج ويب أو صفحة.
1. قم باستيراد ملف Excel عن طريق تحديد مسار الملف.
1. قم بتشغيل التطبيق أو افتح الصفحة.

لتحميل المحتوى من ملف Excel إلى عنصر التحكم Aspose.Cells.GridWeb، يجب عليك استدعاء الأسلوب importExcelFile لتحديد مسار ملف Excel. بعد ذلك، سيبحث عنصر تحكم GridWeb تلقائيًا عن الملف من المسار المحدد ويعرض محتوياته فيه. يتم توفير مقتطف التعليمات البرمجية الذي يقوم بتحميل محتويات ملف Excel أدناه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-OpeningfromFile-OpeningfromFile.jsp" >}}

يمكن استخدام مقتطف الكود أعلاه بالطريقة التي تريدها. على سبيل المثال، لتحميل ملف Excel تلقائيًا عند تحميل نموذج ويب، أضف هذا الرمز إلى حدث Page_Load الخاص بالنموذج الذي حددته بنفسك.

**يتم تحميل ملف Excel إلى GridWeb**

![ما يجب القيام به:image_alt_text](working-with-gridweb_1.png)

##  **حفظ ملف إكسل Microsoft**

من الممكن إنشاء ملفات Excel Microsoft جديدة أو التعامل معها، على مواقع الويب في وضع واجهة المستخدم الرسومية باستخدام التحكم Aspose.Cells.GridWeb. يمكن بعد ذلك حفظ الملفات في ملفات Excel. Aspose.Cells.GridWeb يعمل بشكل فعال كمحرر جداول البيانات على الإنترنت. يصف هذا الموضوع كيفية حفظ محتوى الشبكة في ملفات Excel.

###  **الحفظ كملف**

لحفظ محتوى عنصر التحكم Aspose.Cells.GridWeb كملف Excel:

1. أضف عنصر التحكم Aspose.Cells.GridWeb إلى نموذج ويب أو صفحة.
1. احفظ عملك كملف Excel في المسار المحدد.
1. قم بتشغيل التطبيق أو افتح الصفحة.

يوضح مثال التعليمات البرمجية أدناه كيفية حفظ محتوى الشبكة في ملف Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-SavingasFile-SavingasFile.jsp" >}}

 يمكن استخدام مقتطف الكود أعلاه بعدة طرق. إحدى الطرق الشائعة هي إضافة زر يحفظ محتوى الشبكة في ملف Excel عند النقر عليه. Aspose.Cells.GridWeb يقدم طريقة أسهل للمهمة. Aspose.Cells.GridWeb لديه حدث يسمى SaveCommand. يمكن إضافة مقتطف الكود أعلاه إلى معالج الأحداث الخاص بحدث SaveCommand والذي يسمح للمستخدمين بحفظ عملهم بالنقر فوق Aspose.Cells.GridWeb المدمج**يحفظ** زر.

##  **تغيير حجم Aspose.Cells.GridWeb وشريط الرأس الخاص به**

تشرح هذه المقالة كيفية تغيير حجم GridWeb في وقت التشغيل باستخدام Aspose.Cells.GridWeb API. كما تشرح كيفية تغيير حجم أشرطة الرأس لعنصر التحكم Aspose.Cells.GridWeb لتسهيل قراءة بياناتها.

###  **تغيير العرض والارتفاع لـ Aspose.Cells.GridWeb**

يعد تغيير عرض وارتفاع Aspose.Cells.GridWeb ميزة بسيطة ولكنها مهمة. يتم تمثيل عنصر التحكم Aspose.Cells.GridWeb بواسطة فئة GridWeb في API. لتغيير حجم العرض والارتفاع لعنصر التحكم GridWeb، ما عليك سوى استخدام خصائص العرض والارتفاع الخاصة به.

{{% alert color="primary" %}}

يمكن تحديد العرض والارتفاع لعنصر التحكم بالبكسل أو النقاط.

{{% /alert %}}

يتم عرض إخراج مقتطف التعليمات البرمجية التالي أدناه.

**تم تغيير العرض والارتفاع لعنصر تحكم GridWeb**

![ما يجب القيام به:image_alt_text](working-with-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangedwidthheightofGridWebcontrol-ChangedwidthheightofGridWebcontrol.jsp" >}}

###  **تغيير العرض والارتفاع لشريط الرأس**

Aspose.Cells.يحتوي عنصر تحكم GridWeb على شريطي رأس كما يلي:

- شريط الرأس العلوي، يمثل شريط الرأس هذا الأعمدة مثل A وB وC وD وما إلى ذلك.
- شريط الرأس الأيسر، يمثل شريط الرأس هذا الصفوف مثل 1، 2، 3، 4، إلخ.

يتم عرض كلا شريطي الرأس أدناه.

**أشرطة الرأس**

![ما يجب القيام به:image_alt_text](working-with-gridweb_3.png)

قم بتغيير ارتفاع شريط الرأس العلوي وعرض شريط الرأس الأيسر باستخدام خصائص HeaderBarHeight وHeaderBarWidth لعنصر التحكم GridWeb على التوالي. يوضح الشكل أدناه مخرجات مثال التعليمات البرمجية التالي.

**تم تغيير عرض وارتفاع شريط الرأس**

![ما يجب القيام به:image_alt_text](working-with-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangingWidthandHeightofHeaderBar-ChangingWidthandHeightofHeaderBar.jsp" >}}

##  **العمل مع Aspose.Cells.GridWeb الأحداث**

يجب أن يكون جميع المطورين على دراية بالأحداث والغرض منها. يتم استخدام الأحداث لإرسال إعلامات بالتغييرات التي قد تحدث في عنصر التحكم أو الفئة. يحتوي Aspose.Cells.GridWeb على العديد من الأحداث التي يمكن استخدامها لتنفيذ مهام محددة عند حدوث تغييرات معينة في عنصر التحكم.

يوفر هذا الموضوع مقدمة لجميع الأحداث التي يدعمها عنصر التحكم Aspose.Cells.GridWeb بالإضافة إلى بعض التفاصيل حول كيفية التعامل مع هذه الأحداث.

###  **مقدمة لأحداث الشبكة**

Aspose.Cells. يدعم عنصر تحكم GridWeb العديد من الأحداث التي توفر المزيد من التحكم في تنفيذ العمليات عند تشغيل أحداث معينة في عنصر التحكم. يمكن العثور أدناه على قائمة كاملة بالأحداث التي يدعمها Aspose.Cells.GridWeb.

|**الأحداث**|**وصف**|
| :- | :- |
|أمر الخلية|يحدث عند النقر فوق الارتباط التشعبي للأمر الخاص بالخلية. عند إطلاق هذا الحدث، توفر المعلمة e.Argument اسم الأمر.|
|الخليةDoubleClick|يحدث عند النقر المزدوج على الخلية.|
|تم حذف العمود|يحدث عندما يقوم المستخدم بحذف عمود من ورقة العمل باستخدام القائمة من جانب العميل.|
|حذف العمود|يحدث عندما يحاول المستخدم حذف عمود من ورقة عمل باستخدام القائمة من جانب العميل.|
|عمود النقر المزدوج|يحدث عند النقر المزدوج على رأس العمود.|
|تم إدراج العمود|يحدث عندما يقوم المستخدم بإدراج عمود في ورقة عمل باستخدام القائمة من جانب العميل.|
|أمر مخصص|يحدث عندما يقوم المستخدم بالنقر فوق زر أمر مخصص.|
|تحميل البيانات المخصصة|يحدث عندما يتم تعيين خاصية EnableSession لعنصر التحكم إلى false وتحتاج إلى تحميل بيانات ورقة العمل. يمكنك التعامل مع هذا الحدث في وضع عدم الجلسة لتحميل بيانات ورقة العمل من ملف أو قاعدة بيانات.|
|PageIndexChanged|يحدث عند تغيير فهرس صفحة ورقة عنصر التحكم.|
|تم حذف الصف|يحدث عندما يقوم المستخدم بحذف صف من ورقة العمل باستخدام القائمة من جانب العميل.|
|حذف الصف|يحدث عندما يحاول المستخدم حذف صف من ورقة عمل باستخدام القائمة من جانب العميل.|
|صف النقر المزدوج|يحدث عند النقر المزدوج على رأس الصف.|
|تم إدراج الصف|يحدث عندما يقوم المستخدم بإدراج صف في ورقة العمل باستخدام القائمة من جانب العميل.|
|حفظ الأمر| يحدث عندما**يحفظ** تم النقر على الزر.|
|ورقةTabClick|يحدث عند النقر فوق علامة تبويب الورقة.|
|إرسال الأمر| يحدث عندما**يُقدِّم** تم النقر على الزر.|
|تراجع عن الأمر| يحدث عندما**الغاء التحميل** تم النقر على الزر.|
|تم الانتهاء من AjaxCall|يتم تشغيله عند انتهاء تحديث AJAX لعنصر التحكم. (يجب تعيين EnableAJAX على صحيح).|
|CellModifiedOnAjax|يتم تشغيله عند تعديل الخلية في استدعاء AJAX.|
|AfterColumnFilter|يتم تشغيله عند تطبيق المرشح على عمود.|

###  **التعامل مع أحداث الشبكة**

لإجراء عملية محددة لتشغيل حدث معين، يتعين علينا إنشاء معالج حدث. يقوم معالج الأحداث بتنفيذ المهمة المطلوبة عند تشغيل حدث معين. يوضح المثال التالي كيفية التعامل مع حدث شبكة بسيط.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HandlingGridEvents-HandlingGridEvents.jsp" >}}

##  **العمل مع أحداث النقر المزدوج**

Aspose.Cells.GridWeb يحتوي على ثلاثة أنواع من أحداث النقر المزدوج:

- CellDoubleClick، يتم تشغيله عند النقر المزدوج على الخلية.
- ColumnDoubleClick، يتم تشغيله عند النقر المزدوج على رأس العمود.
- RowDoubleClick، يتم تشغيله عند النقر المزدوج على رأس الصف.

يناقش هذا الموضوع كيفية تمكين أحداث النقر المزدوج في Aspose.Cells.GridWeb. ويناقش أيضًا إنشاء معالجات الأحداث لهذه الأحداث.

###  **تمكين أحداث النقر المزدوج**

يمكن تمكين كافة أنواع أحداث النقر المزدوج من جانب العميل عن طريق تعيين خاصية EnableDoubleClickEvent الخاصة بعنصر تحكم GridWeb على القيمة true.

{{% alert color="primary" %}}

بشكل افتراضي، يتم تعيين الخاصية EnableDoubleClickEvent إلى false. وهذا يعني أن أحداث النقر المزدوج غير ممكّنة افتراضيًا. لتنفيذ مثل هذه الأحداث، قم أولاً بتمكين الميزة.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-EnablingDoubleClickEvents-EnablingDoubleClickEvents.jsp" >}}

بمجرد تمكين أحداث النقر المزدوج، فمن الممكن إنشاء معالجات أحداث لأي أحداث يتم النقر عليها نقرًا مزدوجًا. تؤدي معالجات الأحداث هذه مهامًا محددة عند تشغيل حدث النقر المزدوج المحدد.

###  **التعامل مع أحداث النقر المزدوج**

####  **انقر مرتين على Cell**

يوفر معالج الحدث للحدث CellDoubleClick وسيطة من النوع CellEventArgs، والتي توفر المعلومات الكاملة للخلية التي تم النقر فوقها نقرًا مزدوجًا.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickCell-DoubleClickCell.jsp" >}}

####  **انقر نقرًا مزدوجًا فوق رأس العمود**

يوفر معالج الحدث لحدث ColumnDoubleClick وسيطة من النوع RowColumnEventArgs التي توفر رقم فهرس العمود الخاص بالرأس الذي تم النقر فوقه نقرًا مزدوجًا ومعلومات أخرى.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickColumnHeader-DoubleClickColumnHeader.jsp" >}}

####  **انقر نقراً مزدوجاً فوق رأس الصف**

يوفر معالج الحدث لحدث RowDoubleClick وسيطة من النوع RowColumnEventArgs التي توفر رقم فهرس الصف للرأس الذي تم النقر فوقه نقرًا مزدوجًا والمعلومات الأخرى ذات الصلة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickRowHeader-DoubleClickRowHeader.jsp" >}}

##  **تحديد النمط أو المظهر لـ Aspose.Cells.GridWeb**

Aspose.Cells.GridWeb له شكله ومظهره الافتراضي ولكن من الممكن تغيير مظهره. Aspose.Cells.GridWeb يوفر العديد من الخصائص للسماح للمطورين بالتحكم الكامل في مظهره. وهذا الموضوع يتحدث عن بعض تلك الخصائص.

###  **تحديد النمط أو المظهر لـ Aspose.Cells.GridWeb**

####  **أنماط محددة مسبقا**

لحفظ جهود المطورين، يقدم Aspose.Cells.GridWeb بعض الأنماط المعدة مسبقًا. ما عليك سوى تحديد نمط من القائمة لتطبيق النمط.

|**الأنماط**|**نظام الألوان**|
| :- | :- |
|معيار|فضة|
|ملون1|وَردَة|
|ملون2|أزرق|
|محترف1|ازرق سماوي|
|المهنية2|سماوي مرة أخرى|
|التقليدية1|مظلم|
|التقليدية2|رمادي|
|مخصص|حسب الطلب|
عند تحديد نمط معين، فإنه يغير المظهر الكامل لعنصر تحكم GridWeb. يمكن للمطورين تحديد نمط محدد مسبقًا ليتم تطبيقه في وقت التشغيل باستخدام API المرن لـ Aspose.Cells.GridWeb.

يوفر عنصر التحكم GridWeb خاصية PresetStyle التي يمكن للمطورين تعيين أي نمط محدد مسبقًا مطلوب لها.

يظهر أدناه إخراج مقتطف الكود أدناه.

**تحكم GridWeb مع نمط Colourful1 المطبق عليه**

![ما يجب القيام به:image_alt_text](working-with-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

####  **نمط شريط الرأس**

إذا ألقيت نظرة على عنصر تحكم GridWeb، ستلاحظ وجود شريطين رأسيين. واحد للأعمدة (أي A، B، C، D، وما إلى ذلك) والآخر للصفوف (أي 1، 2، 3، 4، وما إلى ذلك). Aspose.Cells.GridWeb يسمح للمطورين بالتحكم في مظهر أشرطة الرؤوس هذه. يمكن للمطورين تعيين نمط أشرطة الرأس في وقت التشغيل.

{{% alert color="primary" %}}

يوفر عنصر التحكم GridWeb خاصية HeaderBarStyle التي تطبق نمطًا على كلا شريطي رأس عنصر التحكم.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

####  **نمط شريط التبويب**

من الممكن ضبط نمط شريط علامات التبويب أيضًا. يرجى الاطلاع على الكود التالي

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HeaderBarStyle-HeaderBarStyle.jsp" >}}

####  **جارٍ تحميل ملف النمط**

لتطبيق إعدادات النمط من ملف نمط موجود على عنصر تحكم GridWeb، يمكن للمطورين تعيين مسار ملف النمط إلى خاصية CustomStyleFileName لعنصر التحكم. ولكن، قبل القيام بذلك، يجب تعيين خاصية PresetStyle لعنصر التحكم إلى Custom. وذلك لأن ملف النمط هذا يحتوي على معلومات النمط المخصصة التي تم تعريفها بالفعل بواسطة المطور.

يرجى الاطلاع على الصورة التالية التي توضح GridWeb مع النمط المخصص المطبق عليه.

![ما يجب القيام به:image_alt_text](working-with-gridweb_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-CustomStyleSheet-CustomStyleSheet.jsp" >}}

{{% alert color="primary" %}}

هام: تحميل ملف النمط إلى عنصر تحكم GridWeb لا يؤثر على إعدادات التنسيق لخلايا عنصر التحكم.

{{% /alert %}}

####  **نموذج لقالب النمط المخصص**

فيما يلي نموذج لقالب النمط المخصص. ويمكنك تعديله حسب متطلباتك.

{{< highlight "java" >}}

 <aspose.excel.web.viewerStyletemplate runat="server" HeaderBarWidth="30pt" ScrollBarBaseColor="#AFEEEE" SelectCellBgColor="#FFFAF0" ActiveHeaderBgColor="#DAA520" ActiveCellBgColor="#DDDDFF" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LeftBorderStyle-BorderWidth="" FrameTableStyle-LeftBorderStyle-BorderColor="" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-RightBorderStyle-BorderWidth="" FrameTableStyle-RightBorderStyle-BorderColor="" FrameTableStyle-BorderWidth="1px" FrameTableStyle-CellSpacing="0" FrameTableStyle-BorderColor="#C0FFC0" FrameTableStyle-CellPadding="0" FrameTableStyle-TopBorderStyle-BorderWidth="" FrameTableStyle-TopBorderStyle-BorderColor="" FrameTableStyle-BackColor="#FFFFCC" FrameTableStyle-BottomBorderStyle-BorderWidth="" FrameTableStyle-BottomBorderStyle-BorderColor="" HeaderBarStyle-LeftBorderStyle-BorderWidth="" HeaderBarStyle-LeftBorderStyle-BorderColor="" HeaderBarStyle-verticalalign="Middle" HeaderBarStyle-RightBorderStyle-BorderWidth="" HeaderBarStyle-RightBorderStyle-BorderColor="" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-font-size="10pt" HeaderBarStyle-BorderColor="#00C0C0" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-horizontalalign="Center" HeaderBarStyle-ForeColor="Red" HeaderBarStyle-TopBorderStyle-BorderWidth="" HeaderBarStyle-TopBorderStyle-BorderColor="" HeaderBarStyle-BackColor="#D8BFD8" HeaderBarStyle-BottomBorderStyle-BorderWidth="" HeaderBarStyle-BottomBorderStyle-BorderColor="" ViewTableStyle-LeftBorderStyle-BorderWidth="" ViewTableStyle-LeftBorderStyle-BorderColor="" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-RightBorderStyle-BorderWidth="" ViewTableStyle-RightBorderStyle-BorderColor="" ViewTableStyle-BorderWidth="0px" ViewTableStyle-CellSpacing="0" ViewTableStyle-CellPadding="0" ViewTableStyle-TopBorderStyle-BorderWidth="" ViewTableStyle-TopBorderStyle-BorderColor="" ViewTableStyle-BottomBorderStyle-BorderWidth="" ViewTableStyle-BottomBorderStyle-BorderColor="" BottomTableStyle-LeftBorderStyle-BorderWidth="" BottomTableStyle-LeftBorderStyle-BorderColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-RightBorderStyle-BorderWidth="" BottomTableStyle-RightBorderStyle-BorderColor="" BottomTableStyle-Height="32pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-CellSpacing="0" BottomTableStyle-BorderColor="#80FF80" BottomTableStyle-CellPadding="0" BottomTableStyle-ForeColor="#FFE0C0" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="#FF69B4" BottomTableStyle-BottomBorderStyle-BorderWidth="" BottomTableStyle-BottomBorderStyle-BorderColor="" HeaderBarHeight="15pt" ActiveTabStyle-LeftBorderStyle-BorderWidth="" ActiveTabStyle-LeftBorderStyle-BorderColor="" ActiveTabStyle-RightBorderStyle-BorderWidth="" ActiveTabStyle-RightBorderStyle-BorderColor="" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-font-size="10pt" ActiveTabStyle-BorderColor="#00C0C0" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="#FF00FF" ActiveTabStyle-TopBorderStyle-BorderWidth="" ActiveTabStyle-TopBorderStyle-BorderColor="" ActiveTabStyle-BackColor="#80FFFF" ActiveTabStyle-BottomBorderStyle-BorderWidth="" ActiveTabStyle-BottomBorderStyle-BorderColor="" HeaderBarTableStyle-LeftBorderStyle-BorderWidth="" HeaderBarTableStyle-LeftBorderStyle-BorderColor="" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-RightBorderStyle-BorderWidth="" HeaderBarTableStyle-RightBorderStyle-BorderColor="" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-CellSpacing="0" HeaderBarTableStyle-CellPadding="0" HeaderBarTableStyle-TopBorderStyle-BorderWidth="" HeaderBarTableStyle-TopBorderStyle-BorderColor="" HeaderBarTableStyle-BackColor="#C0FFC0" HeaderBarTableStyle-BottomBorderStyle-BorderWidth="" HeaderBarTableStyle-BottomBorderStyle-BorderColor="" DefaultGridLineColor="#228B22" TabStyle-LeftBorderStyle-BorderWidth="" TabStyle-LeftBorderStyle-BorderColor="" TabStyle-RightBorderStyle-BorderWidth="" TabStyle-RightBorderStyle-BorderColor="" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-font-size="8pt" TabStyle-BorderColor="#8080FF" TabStyle-BorderStyle="Groove" TabStyle-ForeColor="#FFFFCC" TabStyle-TopBorderStyle-BorderWidth="" TabStyle-TopBorderStyle-BorderColor="" TabStyle-BackColor="#C0C0FF" TabStyle-BottomBorderStyle-BorderWidth="" TabStyle-BottomBorderStyle-BorderColor="" scrollbararrowColor="#778899"/>

{{< /highlight >}}

##  **إنشاء عنصر تحكم في نموذج ويب**

سترشدك هذه المقالة حول كيفية إنشاء نموذج ويب بسيط JSP (Java صفحة الخادم) مع التحكم في GridWeb عليه.

**الخطوة 1 – إنشاء بنية الدليل**

 تحتاج إلى إنشاء بنية الدليل التالية في ملف**تطبيقات الويب**دليل خادم Tomcat

![ما يجب القيام به:image_alt_text](working-with-gridweb_7.png)

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

**الخطوة 2 - إضافة الرموز في الملفات التي تم إنشاؤها**

يعرض هذا القسم رمز الملفات المختلفة التي تم إنشاؤها في بنية الدليل أعلاه. يرجى الحصول على هذه الرموز وإضافتها إلى ملفاتك عن طريق فتحها في المفكرة ونسخها/لصقها.

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

**الخطوة 3 – تشغيل نموذج صفحة ويب JSP الخاصة بك**

الآن لقد فعلت كل شيء. لقد حان الوقت لتشغيل صفحة الويب. الرجاء بدء تشغيل خادم Tomcat ثم لصق عنوان URL التالي في متصفح الويب.

{{< highlight "java" >}}

 http://localhost:8080/SamplePageGridWebJava/SamplePage.jsp

{{< /highlight >}}

سترى شيئًا مثل لقطة الشاشة التالية. تهانينا، لقد نجحت في استخدام عنصر تحكم GridWeb على صفحة JSP الخاصة بك.

![ما يجب القيام به:image_alt_text](working-with-gridweb_8.png)

##  **طباعة شبكة الويب**

هناك أوقات يحتاج فيها المطورون إلى طباعة محتوى GridWeb المضمن من صفحة ويب دون حفظ ملف Excel Microsoft. يدعم عنصر التحكم Aspose.Cells.GridWeb هذه الميزة.

###  **طباعة شبكة الويب**

للطباعة دون حفظ ملف منفصل، قم باستدعاء جانب العميل أسلوب الطباعة () الخاص بفئة GridWeb لطباعة الشبكة. يمكنك اختيار بعض الأحداث المناسبة أيضًا.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-PrintingGridWeb-PrintingGridWeb.jsp" >}}

نظرًا لأنك تتصل به من جانب العميل، فسيتعين عليك أولاً الحصول على معرف عميل شبكة الويب. يمكنك الحصول على معرف العميل باستخدام طريقةgriweb.getClientID().

###  **نموذج التعليمات البرمجية من جانب العميل**

يرجى الاطلاع على الرابط التالي الذي يستدعي طريقةgridweb.print() من جانب العميل.

**HTML**

{{< highlight "java" >}}

 <a href="#" onclick='<%=gridweb.getClientID()%>.print(); '>Print Function of GridWeb</a>

{{< /highlight >}}

##  **مقدمة لأوضاع الشبكة المختلفة**

توضح هذه المقالة أوضاع Aspose.Cells.GridWeb المختلفة. يتم التمييز بين هذه الأوضاع منطقيًا بسبب ميزاتها وسلوكياتها المختلفة. لقد حددنا أنواعًا مختلفة من الأوضاع على النحو التالي:

- وضع التحرير
- اسلوب العرض

كل هذه الأوضاع لها خصائصها الخاصة. يمكن للمطورين العمل مع Aspose.Cells.GridWeb في أي وضع وفقًا لمتطلباتهم. سننظر في كل وضع أدناه.

###  **وضع التحرير**

بشكل افتراضي، يكون عنصر التحكم Aspose.Cells.GridWeb في وضع التحرير. في وضع التحرير، يمكنك تحرير محتوى الشبكة أو تعديله بالكامل باستخدام كافة الميزات التي يوفرها عنصر التحكم Aspose.Cells.GridWeb. تشمل هذه الميزات:

- حفظ محتوى الشبكة في ملفات Excel Microsoft.
- إرسال البيانات إلى الخادم.
- حساب الصيغ.
- التراجع عن الإجراءات السابقة أو التخلص منها.
- إدارة الصفوف والأعمدة.
- قص البيانات أو نسخها أو لصقها.
- تنسيق الخلايا الخ

**التحكم في GridWeb في وضع التحرير**

![ما يجب القيام به:image_alt_text](working-with-gridweb_9.png)

يمكن للمطورين أيضاً التبديل إلى وضع التحرير برمجياً عن طريق تعيين خاصية EditMode لعنصر التحكم GridWeb إلى true.

###  **مثال الكود**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebEditMode-GridWebEditMode.jsp" >}}

###  **اسلوب العرض**

عندما يكون عنصر التحكم GridWeb في وضع العرض، لا يمكن للمستخدمين تحرير محتوى الشبكة أو تعديله، مما يعني أنه يمكنهم عرض محتوى الشبكة فقط. ولهذا السبب يسمى هذا الوضع بوضع العرض. في وضع العرض، بضعة أزرار (**إرسال**،**يحفظ** و**تراجع**) مخفية والقائمة التي تظهر عند النقر بزر الماوس الأيمن تحتوي فقط على **نسخ** و**يجد** خيار.

**التحكم في GridWeb في وضع العرض** 

![ما يجب القيام به:image_alt_text](working-with-gridweb_10.png)

إذا أراد المطورون أن يقوم المستخدمون بعرض البيانات فقط، فيمكنهم التبديل إلى وضع العرض برمجيًا عن طريق تعيين خاصية EditMode الخاصة بعنصر تحكم GridWeb إلى *false**.

###  **مثال الكود**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebViewMode-GridWebViewMode.jsp" >}}

{{% alert color="primary" %}}

حتى في وضع العرض، يمكن للمستخدمين تغيير ارتفاع وعرض الصفوف والأعمدة.

{{% /alert %}}
