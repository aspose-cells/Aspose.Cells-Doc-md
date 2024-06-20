---
title: العمل مع GridWeb
type: docs
weight: 20
url: /ar/java/working-with-gridweb/
---

## **فتح ملف Microsoft Excel**

يمكن لعنصر تحكم Aspose.Cells.GridWeb فتح وتحميل ملفات Microsoft Excel - مع البيانات والتنسيق والرسوم البيانية والصور وما إلى ذلك. تشرح هذا الموضوع الطريقة.

لفتح ملف Excel باستخدام عنصر تحكم GridWeb:

1. أضف تحكم Aspose.Cells.GridWeb إلى نموذج ويب أو صفحة.
1. استيراد ملف Excel عن طريق تحديد مسار الملف.
1. قم بتشغيل التطبيق أو فتح الصفحة.

لتحميل المحتوى من ملف Excel إلى عنصر تحكم Aspose.Cells.GridWeb ، يجب عليك استدعاء طريقة importExcelFile لتحديد مسار ملف Excel. بعد ذلك ، سيقوم عنصر تحكم GridWeb تلقائياً بالعثور على الملف من المسار المحدد وعرض محتوياته فيه. يتم توفير مقتطفات من الكود التي تحمل محتويات ملف Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-OpeningfromFile-OpeningfromFile.jsp" >}}

يمكن استخدام مقتطف الكود أعلاه بأي طريقة تريد. على سبيل المثال ، لتحميل ملف Excel تلقائياً عندما تحمل نموذج ويب ، أضف هذا الكود إلى حدث Page_Load للنموذج الذي حددته بنفسك.

**تم تحميل ملف Excel في GridWeb**

![todo:image_alt_text](working-with-gridweb_1.png)

## **حفظ ملف Microsoft Excel**

من الممكن إنشاء ملفات Microsoft Excel جديدة أو تلاعب بالملفات الموجودة ، على مواقع الويب في وضع GUI باستخدام عنصر تحكم Aspose.Cells.GridWeb. يمكن حفظ الملفات بعد ذلك باعتبارها ملفات Excel. يعمل عنصر تحكم Aspose.Cells.GridWeb بفعالية كمحرر جداول بيانات عبر الإنترنت. يوضح هذا الموضوع كيفية حفظ محتوى الجدول إلى ملفات Excel.

### **الحفظ كملف**

لحفظ محتوى عنصر تحكم Aspose.Cells.GridWeb كملف إكسل:

1. أضف تحكم Aspose.Cells.GridWeb إلى نموذج ويب أو صفحة.
1. احفظ عملك كملف إكسل في مسار محدد.
1. قم بتشغيل التطبيق أو فتح الصفحة.

يوضح المثال البرمجي أدناه كيفية حفظ محتوى الجدول في ملف إكسل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-SavingasFile-SavingasFile.jsp" >}}

يمكن استخدام مقطع الشفرة أعلاه بعدة طرق. وسيلة شائعة هي إضافة زر يقوم بحفظ محتوى الجدول في ملف Excel عند النقر عليه. تقدم Aspose.Cells.GridWeb نهجًا أسهل للمهمة. يحتوي Aspose.Cells.GridWeb على حدث يسمى SaveCommand. يمكن إضافة مقتطف الشفرة أعلاه إلى معالج الحدث الخاص بحدث SaveCommand الذي يسمح للمستخدمين بحفظ عملهم عن طريق النقر فوق زر **حفظ** المضمن في Aspose.Cells.GridWeb.

## **تغيير حجم Aspose.Cells.GridWeb وشريط الرأس الخاص به**

يشرح هذا المقال كيفية تغيير حجم GridWeb أثناء التشغيل باستخدام واجهة برمجة تطبيقات Aspose.Cells.GridWeb. كما يشرح كيفية تغيير أشرطة الرأس لتحسين قراءة البيانات عليها

### **تغيير عرض وارتفاع Aspose.Cells.GridWeb**

تغيير عرض وارتفاع عنصر التحكم Aspose.Cells.GridWeb هو ميزة بسيطة ولكنها مهمة. يتمثل عنصر التحكم Aspose.Cells.GridWeb بواسطة فئة GridWeb في واجهة برمجة التطبيقات. لتغيير عرض وارتفاع عنصر التحكم GridWeb، يُستخدم ببساطة خصائص العرض والارتفاع الخاصة به.

{{% alert color="primary" %}}

يمكن تحديد عرض وارتفاع العنصر التحكم بالبكسل أو النقاط.

{{% /alert %}}

يتم عرض إخراج مقطع الكود التالي أدناه.

**تغيير عرض وارتفاع عنصر التحكم GridWeb**

![todo:image_alt_text](working-with-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangedwidthheightofGridWebcontrol-ChangedwidthheightofGridWebcontrol.jsp" >}}

### **تغيير عرض وارتفاع شريط العنوان**

عنصر التحكم Aspose.Cells.GridWeb يحتوي على شريطي عنوان على النحو التالي:

- الشريط الرأسي العلوي، يمثل هذا الشريط الأعمدة كـ A، B، C، D، إلخ.
- الشريط الرأسي الأيسر، يمثل هذا الشريط الصفوف كـ 1، 2، 3، 4، إلخ.

يتم عرض كل من هذين الشريطين العنوانيين أدناه.

**شرائط العنوان**

![todo:image_alt_text](working-with-gridweb_3.png)

قم بتغيير ارتفاع شريط العنوان العلوي وعرض شريط العنوان الأيسر باستخدام خصائص ارتفاع شريط العنوان وعرض شريط العنوان الخاصتين بعنصر التحكم GridWeb على التوالي. يوضح الشكل أدناه إخراج مثال الكود الذي يليه.

تغيير عرض وارتفاع شريط العنوان

![todo:image_alt_text](working-with-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangingWidthandHeightofHeaderBar-ChangingWidthandHeightofHeaderBar.jsp" >}}

## **العمل مع أحداث Aspose.Cells.GridWeb**

يجب على جميع المطورين أن يكونوا على دراية بالأحداث وغرضها. يتم استخدام الأحداث لإرسال إشعارات بالتغييرات التي قد تحدث في عنصر تحكم أو فئة معينة. Aspose.Cells.GridWeb يحتوي على العديد من الأحداث التي يمكن استخدامها لأداء مهام محددة عند حدوث تغييرات معينة في العنصر التحكم.

يوفر هذا الموضوع مقدمة لجميع الأحداث المدعومة من قِبل تحكم Aspose.Cells.GridWeb مع بعض التفاصيل حول كيفية التعامل مع هذه الأحداث.

### **مقدمة لأحداث الشبكة**

يدعم تحكم Aspose.Cells.GridWeb عدة أحداث توفر مزيدًا من التحكم لأداء العمليات عند حدوث أحداث معينة في التحكم. يمكن العثور على قائمة كاملة من الأحداث المدعومة من تحكم Aspose.Cells.GridWeb أدناه.

|**الأحداث**|**الوصف**|
| :- | :- |
|CellCommand|يحدث عند النقر فوق ارتباط الأمر لخلية. عند حدوث هذا الحدث، يوفر المعامل e.Argument اسم الأمر.|
|CellDoubleClick|يحدث عند النقر المزدوج فوق الخلية.|
|ColumnDeleted|يحدث عندما يقوم المستخدم بحذف عمود من ورقة العمل باستخدام القائمة على الجانب العميل.|
|ColumnDeleting|يحدث عندما يحاول المستخدم حذف عمود من ورقة العمل باستخدام القائمة على الجانب العميل.|
|ColumnDoubleClick|يحدث عند نقر المستخدم مزدوجًا على رأس العمود.|
|ColumnInserted|يحدث عندما يقوم المستخدم بإدراج عمود في ورقة العمل باستخدام القائمة على الجانب العميل.|
|CustomCommand|يحدث عندما ينقر المستخدم على زر الأمر المخصص.|
|LoadCustomData|يحدث عندما يتم ضبط خاصية EnableSession للعنصر التحكم على قيمة false ويحتاج لتحميل بيانات ورقة العمل. يمكنك التعامل مع هذا الحدث في وضع بدون جلسة لتحميل بيانات ورقة العمل من ملف أو قاعدة بيانات.|
|PageIndexChanged|يحدث عند تغيير فهرس الصفحة لورقة المصنف.
|RowDeleted|يحدث عندما يقوم المستخدم بحذف صف من ورقة العمل باستخدام القائمة على الجانب العميل.|
|RowDeleting|يحدث عندما يحاول المستخدم حذف صفًا من ورقة العمل باستخدام القائمة على الجانب العميل.|
|RowDoubleClick|يحدث عند النقر المزدوج على رأس الصف.|
|RowInserted|يحدث عندما يقوم المستخدم بإدراج صف في ورقة العمل باستخدام القائمة على الجانب العميل.|
|SaveCommand|يحدث عند النقر على زر **حفظ**.|
|SheetTabClick|يحدث عند النقر على علامة تبويب الورقة.
|SubmitCommand|يحدث عند النقر على زر **إرسال**.
|UndoCommand|يحدث عند النقر على زر **تراجع**.
|AjaxCallFinished|يتم تنشيطه عند انتهاء التحديث AJAX لعنصر التحكم. (يجب تعيين EnableAJAX على true).
|CellModifiedOnAjax|يحدث عند تعديل الخلية في استدعاء AJAX.
|AfterColumnFilter|يحدث عند تطبيق التصفية على عمود.

### **معالجة أحداث الجدول**

لأداء عملية معينة عند تشغيل حدث معين، يجب علينا إنشاء معالج حدث. يقوم معالج الحدث بأداء المهمة المطلوبة عند تنشيط حدث معين. المثال التالي يوضح كيفية التعامل مع حدث بسيط للجدول.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HandlingGridEvents-HandlingGridEvents.jsp" >}}

## **العمل مع أحداث النقر المزدوج**

Aspose.Cells.GridWeb يحتوي على ثلاثة أنواع من أحداث النقر المزدوج:

- CellDoubleClick، تنشأ عندما يتم النقر المزدوج على خلية.
- ColumnDoubleClick، تنشأ عندما يتم النقر المزدوج على رأس العمود.
- RowDoubleClick، تنشأ عندما يتم النقر المزدوج على رأس الصف.

يناقش هذا الموضوع كيفية تمكين أحداث النقر المزدوج في Aspose.Cells.GridWeb. كما يناقش إنشاء معالجي الأحداث لهذه الأحداث.

### **تمكين أحداث النقر المزدوج**

يمكن تمكين جميع أنواع أحداث النقر المزدوج على الجانب العميلي عن طريق ضبط خاصية EnableDoubleClickEvent لعنصر تحكم GridWeb على true.

{{% alert color="primary" %}}

بشكل افتراضي، يتم ضبط خاصية EnableDoubleClickEvent على القيمة false. وهذا يعني أن أحداث النقر المزدوج غير ممكّنة بشكل افتراضي. لتنفيذ مثل هذه الأحداث، يجب تمكين الميزة أولاً.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-EnablingDoubleClickEvents-EnablingDoubleClickEvents.jsp" >}}

بمجرد تمكين أحداث النقر المزدوج، يمكن إنشاء معالجين للأحداث لأي من حوادث النقر المزدوج. يقوم هذان المعالجان بتنفيذ مهام محددة عند حدوث أي حدث نقر مزدوج معين.

### **معالجة أحداث النقر المزدوج**

#### **نقر مزدوج على الخلية**

يوفر معالج الحدث لحدث CellDoubleClick وسيطًا من نوع CellEventArgs، الذي يوفر المعلومات الكاملة عن الخلية التي تم النقر عليها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickCell-DoubleClickCell.jsp" >}}

#### **نقر مزدوج في رأس العمود**

يوفر معالج الحدث لحدث ColumnDoubleClick وسيطًا من نوع RowColumnEventArgs الذي يوفر رقم الفهرس للعمود الذي تم النقر عليه ومعلومات أخرى.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickColumnHeader-DoubleClickColumnHeader.jsp" >}}

#### **نقر مزدوج في رأس الصف**

يوفر معالج الحدث لحدث RowDoubleClick وسيطًا من نوع RowColumnEventArgs الذي يوفر رقم الفهرس للصف الذي تم النقر عليه ومعلومات أخرى ذات صلة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickRowHeader-DoubleClickRowHeader.jsp" >}}

## **ضبط النمط أو المظهر لعنصر Aspose.Cells.GridWeb**

Aspose.Cells.GridWeb لديها مظهرها وشعورها الافتراضي ولكن من الممكن تغيير مظهرها. Aspose.Cells.GridWeb توفر عدة خصائص لتمكين المطورين من السيطرة الكاملة على مظهرها. يناقش هذا الموضوع بعض تلك الخصائص.

### **ضبط النمط أو المظهر لعنصر Aspose.Cells.GridWeb**

#### **أنماط محددة مسبقاً**

لتوفير جهود المطورين، تقدم Aspose.Cells.GridWeb بعض الأنماط المحددة مسبقاً. ببساطة حدد نمطًا من القائمة لتطبيق النمط.

|**الأنماط**|**مخطط الألوان**|
| :- | :- |
|Standard|Silver|
|Colorful1|Rose|
|Colorful2|Blue|
|Professional1|Cyan|
|Professional2|Cyan again|
|Traditional1|Dark|
|Traditional2|Gray|
|Custom|Customized|
عند تحديد نمط معين، يغير الظهور الكامل لعنصر التحكم GridWeb. يمكن للمطورين تحديد نمط معين لتطبيقه في وقت التشغيل باستخدام واجهة برمجة التطبيقات المرنة لـ Aspose.Cells.GridWeb.

يوفر عنصر التحكم GridWeb خاصية PresetStyle التي يمكن للمطورين تعيين أي نمط محدد مسبقًا مرغوب فيه.

تُظهر الناتج من مقتطف الكود أدناه.

**عنصر تحكم GridWeb مع تطبيق نمط Colorful1 عليه**

![todo:image_alt_text](working-with-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **نمط شريط الرأس**

إذا نظرت إلى عنصر التحكم GridWeb، ستلاحظ وجود شريطي رأس. أحداهما للأعمدة (أي A و B و C و D وما إلى ذلك) والآخر للصفوف (أي 1 و 2 و 3 و 4 وما إلى ذلك). يسمح Aspose.Cells.GridWeb للمطورين بالتحكم في ظهور هذه الشرائط. يمكن للمطورين تعيين نمط الشرائط الرأسية في وقت التشغيل.

{{% alert color="primary" %}}

يوفر عنصر تحكم GridWeb خاصية HeaderBarStyle التي تطبق نمطًا على كلا الشريطين الرأسيين للعنصر التحكم.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **نمط شريط التبويب**

من الممكن أيضًا ضبط نمط شريط التبويب. يرجى رؤية الكود التالي

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HeaderBarStyle-HeaderBarStyle.jsp" >}}

#### **تحميل ملف النمط**

لتطبيق إعدادات النمط من ملف نمط موجود على عنصر تحكم GridWeb، يمكن للمطورين تعيين مسار ملف النمط إلى خاصية CustomStyleFileName للعنصر التحكم. ولكن قبل القيام بذلك، يجب تعيين خاصية PresetStyle الخاصة بالعنصر التحكم إلى Custom. لأن ملف النمط يحتوي على معلومات نمط مخصصة محددة بالفعل من قبل مطور.

يرجى الاطلاع على الصورة التالية التي تُظهر GridWeb بالنمط المخصص المطبق عليه.

![todo:image_alt_text](working-with-gridweb_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-CustomStyleSheet-CustomStyleSheet.jsp" >}}

{{% alert color="primary" %}}

مهم: تحميل ملف النمط إلى تحكم GridWeb لا يؤثر على إعدادات تنسيق الخلايا التابعة للتحكم.

{{% /alert %}}

#### **نموذج نمط مخصص عينة**

فيما يلي نموذج نمط مخصص عينة. يمكنك تعديله حسب متطلباتك.

{{< highlight java >}}

 <aspose.excel.web.viewerStyletemplate runat="server" HeaderBarWidth="30pt" ScrollBarBaseColor="#AFEEEE" SelectCellBgColor="#FFFAF0" ActiveHeaderBgColor="#DAA520" ActiveCellBgColor="#DDDDFF" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LeftBorderStyle-BorderWidth="" FrameTableStyle-LeftBorderStyle-BorderColor="" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-RightBorderStyle-BorderWidth="" FrameTableStyle-RightBorderStyle-BorderColor="" FrameTableStyle-BorderWidth="1px" FrameTableStyle-CellSpacing="0" FrameTableStyle-BorderColor="#C0FFC0" FrameTableStyle-CellPadding="0" FrameTableStyle-TopBorderStyle-BorderWidth="" FrameTableStyle-TopBorderStyle-BorderColor="" FrameTableStyle-BackColor="#FFFFCC" FrameTableStyle-BottomBorderStyle-BorderWidth="" FrameTableStyle-BottomBorderStyle-BorderColor="" HeaderBarStyle-LeftBorderStyle-BorderWidth="" HeaderBarStyle-LeftBorderStyle-BorderColor="" HeaderBarStyle-verticalalign="Middle" HeaderBarStyle-RightBorderStyle-BorderWidth="" HeaderBarStyle-RightBorderStyle-BorderColor="" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-font-size="10pt" HeaderBarStyle-BorderColor="#00C0C0" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-horizontalalign="Center" HeaderBarStyle-ForeColor="Red" HeaderBarStyle-TopBorderStyle-BorderWidth="" HeaderBarStyle-TopBorderStyle-BorderColor="" HeaderBarStyle-BackColor="#D8BFD8" HeaderBarStyle-BottomBorderStyle-BorderWidth="" HeaderBarStyle-BottomBorderStyle-BorderColor="" ViewTableStyle-LeftBorderStyle-BorderWidth="" ViewTableStyle-LeftBorderStyle-BorderColor="" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-RightBorderStyle-BorderWidth="" ViewTableStyle-RightBorderStyle-BorderColor="" ViewTableStyle-BorderWidth="0px" ViewTableStyle-CellSpacing="0" ViewTableStyle-CellPadding="0" ViewTableStyle-TopBorderStyle-BorderWidth="" ViewTableStyle-TopBorderStyle-BorderColor="" ViewTableStyle-BottomBorderStyle-BorderWidth="" ViewTableStyle-BottomBorderStyle-BorderColor="" BottomTableStyle-LeftBorderStyle-BorderWidth="" BottomTableStyle-LeftBorderStyle-BorderColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-RightBorderStyle-BorderWidth="" BottomTableStyle-RightBorderStyle-BorderColor="" BottomTableStyle-Height="32pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-CellSpacing="0" BottomTableStyle-BorderColor="#80FF80" BottomTableStyle-CellPadding="0" BottomTableStyle-ForeColor="#FFE0C0" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="#FF69B4" BottomTableStyle-BottomBorderStyle-BorderWidth="" BottomTableStyle-BottomBorderStyle-BorderColor="" HeaderBarHeight="15pt" ActiveTabStyle-LeftBorderStyle-BorderWidth="" ActiveTabStyle-LeftBorderStyle-BorderColor="" ActiveTabStyle-RightBorderStyle-BorderWidth="" ActiveTabStyle-RightBorderStyle-BorderColor="" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-font-size="10pt" ActiveTabStyle-BorderColor="#00C0C0" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="#FF00FF" ActiveTabStyle-TopBorderStyle-BorderWidth="" ActiveTabStyle-TopBorderStyle-BorderColor="" ActiveTabStyle-BackColor="#80FFFF" ActiveTabStyle-BottomBorderStyle-BorderWidth="" ActiveTabStyle-BottomBorderStyle-BorderColor="" HeaderBarTableStyle-LeftBorderStyle-BorderWidth="" HeaderBarTableStyle-LeftBorderStyle-BorderColor="" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-RightBorderStyle-BorderWidth="" HeaderBarTableStyle-RightBorderStyle-BorderColor="" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-CellSpacing="0" HeaderBarTableStyle-CellPadding="0" HeaderBarTableStyle-TopBorderStyle-BorderWidth="" HeaderBarTableStyle-TopBorderStyle-BorderColor="" HeaderBarTableStyle-BackColor="#C0FFC0" HeaderBarTableStyle-BottomBorderStyle-BorderWidth="" HeaderBarTableStyle-BottomBorderStyle-BorderColor="" DefaultGridLineColor="#228B22" TabStyle-LeftBorderStyle-BorderWidth="" TabStyle-LeftBorderStyle-BorderColor="" TabStyle-RightBorderStyle-BorderWidth="" TabStyle-RightBorderStyle-BorderColor="" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-font-size="8pt" TabStyle-BorderColor="#8080FF" TabStyle-BorderStyle="Groove" TabStyle-ForeColor="#FFFFCC" TabStyle-TopBorderStyle-BorderWidth="" TabStyle-TopBorderStyle-BorderColor="" TabStyle-BackColor="#C0C0FF" TabStyle-BottomBorderStyle-BorderWidth="" TabStyle-BottomBorderStyle-BorderColor="" scrollbararrowColor="#778899"/>

{{< /highlight >}}

## **إنشاء عنصر تحكم في صفحة ويب**

سيقوم هذا المقال بإرشادك حول كيفية إنشاء صفحة ويب JSP (Java Server Page) بسيطة تحتوي على عنصر تحكم GridWeb.

**الخطوة 1 - إنشاء هيكل الدليل**

عليك إنشاء الهيكل الدليل التالي في دليل **webapps** من خادم Tomcat

![todo:image_alt_text](working-with-gridweb_7.png)

هذه هي الدلائل والملفات التي يجب إنشاؤها. يرجى قراءة التعليقات واتباعها. يمكنك الحصول على أحدث أرشيفات إصدار Aspose.Cells.GridWeb for Java من [هذا الرابط](https://downloads.aspose.com/cells/java).

{{< highlight java >}}

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

**الخطوة 2 - إضافة الأكواد في الملفات المنشأة**

تُظهر هذه القسم الرمز لملفات مختلفة تم إنشاؤها في الهيكل الدليل أعلاه. يُرجى الحصول على هذه الأكواد وإضافتها في ملفاتك عن طريق فتحها في المفكرة ونسخ/لصقها.

**Web.xml**

{{< highlight java >}}

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

{{< highlight java >}}

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

**الخطوة 3 - تشغيل صفحة JSP العينية الخاصة بك**

الآن لقد قمت بكل شيء. حان وقت تشغيل الصفحة الويب. يُرجى بدء خادم Tomcat الخاص بك، ثم لصق العنوان (URL) التالي في متصفح الويب.

{{< highlight java >}}

 http://localhost:8080/SamplePageGridWebJava/SamplePage.jsp

{{< /highlight >}}

سترى شيئًا مشابهًا للصورة أدناه. مبروك، لقد استخدمت بنجاح عنصر تحكم GridWeb على صفحة JSP الخاصة بك.

![todo:image_alt_text](working-with-gridweb_8.png)

## **طباعة GridWeb**

هناك أوقات عندما يحتاج المطورون إلى طباعة محتوى GridWeb المضمن من صفحة ويب دون حفظ ملف Microsoft Excel. تدعم عنصر تحكم Aspose.Cells.GridWeb هذه الميزة.

### **طباعة GridWeb**

للطباعة دون حفظ ملف منفصل، اتصل بطريقة print() في فئة GridWeb على الجانب العميل لطباعة الجدول. يمكنك أيضًا اختيار بعض الأحداث المناسبة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-PrintingGridWeb-PrintingGridWeb.jsp" >}}

نظرًا لأنك تقوم بالاتصال به من الجانب العميل، فيجب عليك الحصول أولاً على معرف العميل لـ gridweb. يمكنك الحصول على معرف العميل باستخدام طريقة gridweb.getClientID().

### **كود عينة للجانب العميل**

يرجى الاطلاع على الرابط التالي الذي يستدعي طريقة gridweb.print() من الجانب العميل.

**HTML**

{{< highlight java >}}

 <a href="#" onclick='<%=gridweb.getClientID()%>.print(); '>Print Function of GridWeb</a>

{{< /highlight >}}

## **مقدمة إلى وضعيات الجدول المختلفة**

يصف هذا المقال وضعيات Aspose.Cells.GridWeb المختلفة. تتميز هذه الوضعيات بشكل منطقي بسبب ميزاتها وسلوكها المختلفة. لقد حددنا أنواع وضع مختلفة على النحو التالي:

- وضع التحرير
- وضع العرض

كل هذه الأوضاع لها خصائصها الخاصة. يمكن للمطورين العمل مع Aspose.Cells.GridWeb في أي وضع وفقًا لاحتياجاتهم. سنلقي نظرة على كل وضع أدناه.

### **وضع التحرير**

بشكل افتراضي، تكون عنصر التحكم Aspose.Cells.GridWeb في وضع التحرير. في وضع التحرير، يمكنك تحرير أو تعديل محتوى الجدول بالكامل باستخدام جميع الميزات التي يقدمها عنصر التحكم Aspose.Cells.GridWeb. تتضمن هذه الميزات:

- حفظ محتوى الجدول في ملفات Microsoft Excel.
- تقديم البيانات إلى خادم.
- حساب الصيغ.
- التراجع عن الإجراءات السابقة أو التخلص منها.
- إدارة الصفوف والأعمدة.
- قص ونسخ أو لصق البيانات.
- تنسيق الخلايا إلخ.

**عنصر التحكم GridWeb في وضع التحرير**

![todo:image_alt_text](working-with-gridweb_9.png)

يمكن للمطورين أيضًا التبديل إلى وضع التحرير بشكل برمجي عن طريق تعيين خاصية EditMode لعنصر التحكم GridWeb إلى true.

### **مثال الكود**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebEditMode-GridWebEditMode.jsp" >}}

### **وضع العرض**

عندما يكون تحكم GridWeb في وضع العرض، لا يمكن للمستخدمين تحرير أو تعديل محتوى الجدول، مما يعني أن المستخدمين يمكنهم فقط عرض محتوى الجدول. ولهذا السبب يُطلق على هذا الوضع اسم وضع العرض. في وضع العرض، يتم إخفاء بعض الأزرار (**Submit**, **Save** and **Undo**) والقائمة التي تظهر عند النقر بزر الماوس الأيمن تحتوي فقط على الخيارات **Copy** و **Find**.

عنصر تحكم GridWeb في وضع العرض 

![todo:image_alt_text](working-with-gridweb_10.png)

إذا كان المطورون يرغبون في أن يعرض مستخدموهم البيانات فقط فإنهم يمكنهم التبديل إلى وضع العرض برمجيًا عن طريق ضبط خاصية EditMode للتحكم GridWeb إلى **false**.

### **مثال الكود**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebViewMode-GridWebViewMode.jsp" >}}

{{% alert color="primary" %}}

حتى في وضع العرض، يمكن للمستخدمين تغيير ارتفاع وعرض الصفوف والأعمدة.

{{% /alert %}}
