---
title: ربط ورقة عمل بقاعدة بيانات باستخدام مصمم أوراق العمل في VS.Net 2005
type: docs
weight: 40
url: /ar/net/binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005/
---
{{% alert color="primary" %}}

 تتناول هذه المقالة أسهل طريقة لربط أوراق العمل بجداول قاعدة البيانات بتنسيق**Visual Studio.Net 2005** باستخدام أداة خاصة مزودة برقم Aspose.Cells.GridWeb المسمى**مصمم أوراق العمل** . ستجعلك هذه المقالة بالتأكيد تشعر أنه من الأسهل استخدام ميزة ربط البيانات في Aspose.Cells.GridWeb بمساعدة**مصمم أوراق العمل** .

{{% /alert %}}

## **ربط ورقة عمل بقاعدة بيانات باستخدام مصمم أوراق العمل في VS.Net 2005**

 الغرض من هذه المقالة هو السماح لجميع المطورين بمعرفة كيفية إنشاء تطبيق لربط البيانات بتنسيق**VS.Net 2005** وفهم استخدام ودور**مصمم أوراق العمل** محرر. أفضل طريقة لتعلم وفهم أي شيء هي من خلال الأمثلة. لذلك ، في هذه المقالة ، سيكون من الأفضل لنا أيضًا إنشاء نموذج تطبيق لتوضيح استخدام**مصمم أوراق العمل**في أوراق العمل الملزمة مع قاعدة البيانات. لنقم بإنشاء تطبيق خطوة بخطوة.

### **الخطوة 1: إنشاء نموذج قاعدة بيانات**

 بادئ ذي بدء ، سنقوم بإنشاء نموذج قاعدة بيانات سيتم استخدامها في هذه المقالة. لقد استخدمنا MS Access لإنشاء نموذج قاعدة بيانات تحتوي على**منتجات** الجدول الذي يظهر مخططه أدناه:

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_1.png)

**شكل:** معلومات تصميم**منتجات** الطاولة

 يتم إضافة عدد قليل من السجلات الوهمية إلى ملف**منتجات** الجدول كما هو موضح أدناه في الشكل:

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_2.png)

**شكل:** السجلات في**منتجات** الطاولة

### **الخطوة الثانية: تصميم نموذج التطبيق**

 ان**تطبيق ويب ASP.NET** تم إنشاؤه وتصميمه في Visual Studio.NET 2005 كما هو موضح في الأشكال أدناه. تعتبر لقطات الشاشة هذه مفيدة للمطورين الذين ليسوا على دراية كبيرة باستخدام Aspose.Cells.GridWeb في Visual Studio.Net 2005.

أول تشغيل VS.Net 2005.

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_3.png)

**شكل:** بدء VS.Net 2005

قم بإنشاء موقع ويب جديد من القائمة File | New | Web Site ....

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_4.png)

**شكل:** إنشاء موقع ويب جديد

 بعد النقر فوق ملف | جديد | موقع ويب ... خيار القائمة ،**الموقع الجديد** يظهر الحوار. انقر على**تصفح** زر فيه.

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_5.png)

**شكل:**مربع حوار موقع ويب جديد

 بعد النقر فوق ملف**تصفح** الزر ، اختر مجلد الموقع في IIS المحلي. يمكنك إنشاء مجلد جديد وجعله مجلد افتراضي كما هو موضح في الشكل.

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_6.png)

**شكل:** إنشاء مجلد جديد


 بعد النقر فوق ملف**فتح** زر في**اختيار موقع** حوار**الموقع الجديد** سيبدو الحوار.

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_7.png)

**شكل:** تحديد موقع المشروع

الآن تم إنشاء المشروع

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_8.png)

**شكل:** مشروع تم إنشاؤه

### **وسائط XHTML و HTML**

**Aspose.Cells.GridWeb** يدعم وضع XHTML تمامًا والذي يتم تنفيذه افتراضيًا في VS.Net 2005 منذ**XhtmlMode** ممتلكات**شبكة** تم ضبط التحكم على**حقيقي** بشكل افتراضي عندما تضع عنصر التحكم على صفحة الويب. ولكن إذا كنت ترغب في تنفيذ وضع HTML للتحكم في VS.Net 2005 ، فيمكنك القيام بذلك بسهولة تامة. يجب عليك تعديل ملف**<! DOCTYPE>** ضع علامة قليلاً في التعليمات البرمجية المصدر لصفحة الويب وقم بتعيين ملف**XhtmlMode** ممتلكات**شبكة** السيطرة على**خطأ شنيع** .

#### **في هذا الموضوع سوف نستخدم وضع HTML للتحكم. لذا اتبع الخطوات أدناه**

##### **1. قم بالتبديل إلى عرض المصدر لصفحة الويب وابحث عن علامة <! DOCTYPE> التالية في شفرة المصدر.**

**XML**

{{< highlight "csharp" >}}

 <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

{{< /highlight >}}

بمجرد العثور على هذه العلامة ، حدد تلك العلامة الكاملة في شفرة المصدر كما هو موضح أدناه.

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_9.png)

**شكل:** التحديد**علامة <! DOCTYPE>**

 استبدل ملف**<! DOCTYPE>** علامة من شفرة المصدر الخاصة بك بالعلامة التالية.

**XML**

{{< highlight "csharp" >}}

  <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> 

{{< /highlight >}}

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_10.png)

**شكل:** التعديل**علامة <! DOCTYPE>**

##### **2. بعد أن تقوم بإضافة عنصر تحكم GridWeb إلى نموذج الويب. يجب عليك تحديد عنصر التحكم واختيار خاصية XhtmlMode من نافذة الخصائص لتعيينها على False.**

**إضافة GridWeb إلى WebForm** 

 انقر بزر الماوس الأيمن فوق**ToolBox** واختر**اختر العناصر ...** من القائمة.

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_11.png)

**شكل:** اختيار العناصر

 حدد الآن**شبكة** المكون وانقر**نعم**

{{% alert color="primary" %}}

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_12.png)

**شكل:** التحديد**شبكة** المكون في مربع حوار المكون

 الآن**شبكة** تمت إضافته كما هو موضح في الشكل أدناه.

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_13.png)

**شكل:** **شبكة** يضاف في صندوق الأدوات

 ضع ال**شبكة** في نموذج الويب كما هو موضح أدناه.

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_14.png)

**شكل:** وضع**شبكة** على صفحة الويب

{{% /alert %}} {{% alert color="primary" %}}

**إجراء** : حدد عنصر التحكم ، الآن ، اختر ملف**XhtmlMode** ممتلكات من**الخصائص** نافذة وضبطها على**خطأ شنيع** القيمة.

{{% /alert %}}

##### **الخطوة 3: الاتصال بقاعدة البيانات باستخدام Server Explorer و Setting Connection Object**

 أولاً نضيف قاعدة بيانات MS Access إلى المشروع الذي أنشأناه مسبقًا**الخطوة 1** . قد ترى ذلك**ديسيبل** يضاف الملف إلى المشروع.

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_15.png)

**شكل:** تمت إضافة قاعدة البيانات إلى مجلد المشروع

 الآن ، نذهب إلى**مصمم المكونات** نافذة نموذج الويب باستخدام خيار قائمة النقر بزر الماوس الأيمن على صفحة الويب.

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_16.png)

**شكل:** التحديد**عرض مصمم المكونات** اختيار

تظهر نافذة "مصمم المكونات" على النحو التالي.

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_17.png)

**شكل:** نافذة مصمم المكونات

 انقر نقرًا مزدوجًا فوق ملف**OleDbConnection** مكون من لوحة البيانات لوضع كائن oleDbConnection1 في النافذة.

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_18.png)

**شكل:** كائن oleDbConnection1

 حان الوقت الآن للاتصال بقاعدة البيانات. يمكننا القيام بذلك بسهولة عن طريق استخدام**مستكشف الخادم** في Visual Studio.NET 2005. اختر فقط**اتصال البيانات** في**مستكشف الخادم** وانقر بزر الماوس الأيمن. سترى قائمة سياق تظهر أمامك. يختار**إضافة اتصال ...**الخيار من القائمة كما هو موضح أدناه في الشكل:

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_19.png)

**شكل:** التحديد**إضافة اتصال ...** خيار من القائمة


 بعد الاختيار**إضافة اتصال ...** خيار من القائمة ،**إضافة اتصال** سيتم فتح الحوار و**تصفح** لتحديد ملف قاعدة البيانات كما هو موضح أدناه.

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_20.png)

**شكل:** اختيار ملف قاعدة البيانات

يمكنك اختبار الاتصال.

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_21.png)

**شكل:** اختبار الاتصال

يمكنك تصفح الاتصال للتحقق من الجدول وحقوله.

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_22.png)

**شكل:** فحص الجدول ومجالات الاتصال الخاصة به

 الآن إذا اخترت**oleDbConnection1** كائن في**مصمم المكونات** نافذة ، يمكنك تحديد سلسلة الاتصال المتعلقة بالاتصال الحالي الذي تم إنشاؤه للتو ، وهو موجود في خاصية "ConnectionString" الخاصة بـ**oleDbConnection1** الكائن في نافذة الخصائص.

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_23.png)

**شكل:** تحديد سلسلة الاتصال للكائن

 أخيرًا ، تم تغيير معدل الكائن إلى**محمي** لتحسين إمكانية الوصول.

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_24.png)

**شكل:** ضبط معدّل الكائن

##### **الخطوة 4: تكوين كائن محول البيانات**

 الآن ، أضف ملف**OleDbDataAdapter** مكون من لوحة البيانات في صندوق الأدوات لتكوينه. انقر نقرًا مزدوجًا فوق ملف**OleDbDataAdapter** في لوحة البيانات في صندوق الأدوات ، سيبدأ معالج التكوين الخاص به ويحدد الاتصال الحالي كما هو موضح في الشكل:

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_25.png)

**شكل:** معالج تكوين محول البيانات

 بعد النقر**التالي** ، انقر فوق**منشئ الاستعلام** لإضافة ال**منتجات** الجدول ، حدد كل الأعمدة وانقر**نعم** زر.

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_26.png)

**شكل:** إضافة جدول المنتج

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_27.png)

**شكل:** منشئ الاستعلام

 انقر الآن**إنهاء** زر لإنهاء المعالج.

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_28.png)

**شكل:** إنهاء المعالج

 بعد تكوين المعالج ، تتم إضافة oleDbDataAdapter1 تلقائيًا إلى النافذة كما هو موضح أدناه. أيضًا ، يمكنك ضبط معدّله على**محمي**.

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_29.png)

**شكل:** استرداد كائن OleDbDataAdapter في إطار المصمم

##### **الخطوة 5: إنشاء DataSet**

 نظرًا لأننا أنشأنا اتصال قاعدة البيانات وكائنات محول البيانات ، لكننا ما زلنا بحاجة إلى شيء حيث يمكننا تخزين البيانات بعد الاتصال بقاعدة البيانات. أ**مجموعة البيانات**يمكن للكائن تخزين البيانات بدقة ويمكننا أيضًا إنشاؤها بسهولة باستخدام VS.NET 2005 IDE. للقيام بذلك ، حدد**oleDbDataAdaper1** وانقر بزر الماوس الأيمن. ستظهر قائمة السياق مع بعض الخيارات. يختار**يولد** **مجموعة البيانات ...** الخيار من القائمة كما هو موضح أدناه في الشكل.

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_30.png)

**شكل:** التحديد**يولد** **مجموعة البيانات ...** خيار من القائمة

 بعد الاختيار**يولد** **مجموعة البيانات ...** خيار من القائمة ، أ**توليد مجموعة البيانات** سيتم فتح الحوار. باستخدام هذا الحوار ، يمكننا تحديد ما سيكون اسم الجديد**مجموعة البيانات** الكائن المراد إنشاؤه والجداول التي يجب إضافتها إليها**مجموعة البيانات** . يفحص**أضف مجموعة البيانات هذه إلى المصمم** الخيار وانقر**نعم** الزر كما هو موضح أدناه في الشكل.

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_31.png)

**شكل:** النقر**نعم** زر لتوليد**مجموعة البيانات**

 الآن ، يمكنك رؤية ملف**مجموعة البيانات 11** تمت إضافة الكائن إلى المصمم كما هو موضح أدناه في الشكل. اضبط معدّل الكائن على**محمي**.

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_32.png)

**شكل:** **مجموعة البيانات** تم إنشاؤه وإضافته إلى نافذة المصمم

يتم إنشاء رمز معين تلقائيًا في الاتصال المرتبط بملف .cs ، ومحول البيانات ، وكائن مجموعة البيانات.

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_33.png)

**شكل:** رمز تم إنشاؤه

##### **الخطوة 6: استخدام مصمم أوراق العمل**

 الآن ، حان الوقت لكشف السر. حدد عنصر التحكم وانقر بزر الماوس الأيمن. سيتم فتح قائمة السياق. حدد خيار مصمم أوراق العمل ... من القائمة كما هو موضح أدناه في الشكل.

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_34.png)

**شكل:** التحديد**مصمم أوراق العمل ...** خيار من القائمة

 بعد ذلك**محرر مجموعة أوراق العمل** الحوار (يسمى أيضًا**مصمم أوراق العمل** ) ، يمكنك رؤية العديد من الخصائص التي يمكن تهيئتها لربط ملف**الورقة 1** مع أي جدول في قاعدة البيانات. دعنا نختار**مصدر البيانات** منشأه. يكتب**مجموعة البيانات 11** فيه (الذي أنشأناه وأضفناه إلى نافذة المصمم في الخطوة السابقة). ثم انقر فوق**عضو البيانات** منشأه. يكتب**منتجات** كاسم جدول هنا كما هو موضح أدناه في الشكل:

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_35.png)

**شكل:** ضبط**مصدر البيانات** و**عضو البيانات** الخصائص

 الآن ، يمكنك تكوين ملفات**BindColumns** منشأه. بعد النقر فوقه ، يمكنك الآن إضافة أعمدة الربط وتعيين ملف**شرح** , **حقل البيانات** (يجب أن يكون هو نفسه**منتجات** حقول الجدول) وخصائص أخرى. يمكنك ضبط ملف**إنشاء تلقائي** إلى**حقيقي** وتطبيق**تصديق** وضبط**نوع_الرقم**مجالات مختلفة لمتطلباتك.

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_36.png)

**شكل:** النقر**BindColumns** منشأه

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_37.png)

**شكل:** **محرر مجموعة BindColumn** الحوار

##### **الخطوة 7: إضافة بعض سطور التعليمات البرمجية لصفحة الويب**

 وقد استخدمنا**مصمم أوراق العمل** بسهولة والآن علينا فقط إضافة بعض أسطر التعليمات البرمجية

 أولا سوف نضيف**OnInit** رمز متعلق بالحدث للتهيئة**InitializeComponent** طريقة لتهيئة وإنشاء كائنات الاتصال والأوامر ومحول البيانات ومجموعة البيانات. لا تتم إضافة سطور التعليمات البرمجية هذه مع الشفرة التي تم إنشاؤها تلقائيًا ، لذلك يتعين علينا إضافتها يدويًا.

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_38.png)

**شكل:** إضافة بعض code1

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_39.png)

**شكل:** إضافة بعض التعليمات البرمجية 2

 الآن نضيف بعض التعليمات البرمجية في ملف**Page_Load** معالج الحدث لملء**مجموعة البيانات 11** كائن ببيانات من قاعدة بيانات (باستخدام**oleDbDataAdapter1** ) وملزمة**شبكة** السيطرة مع**مجموعة البيانات 11** من خلال استدعاء ملف**ربط البيانات** طريقة.

{{% alert color="primary" %}}   {{% /alert %}}

##### **مثال:**

**C#**

{{< highlight "csharp" >}}

 //Implementing Page_Load event handler

protected void Page_Load(object sender, EventArgs e)

{

    //Checking if there is not any PostBack

    if (!IsPostBack)

    {

        try

        {

            //Filling DataSet with data 

            oleDbDataAdapter1.Fill(dataSet11);

            //Binding GridWeb with DataSet

            GridWeb1.DataBind();

        }

        finally

        {

            //Finally, closing database connection

            oleDbConnection1.Close();

        }

    }

}

{{< /highlight >}}

**VB.NET**

{{< highlight "csharp" >}}

 'Implementing Page_Load event handler

Protected Sub Page_Load(ByVal sender As Object, ByVal e As System.EventArgs) Handles Me.Load

    'Checking if there is not any PostBack

    If Not IsPostBack Then

        Try

            'Filling DataSet with data 

            oleDbDataAdapter1.Fill(dataSet11)

            'Binding GridWeb with DataSet

            GridWeb1.DataBind()

        Finally

            'Finally, closing database connection

            oleDbConnection1.Close()

        End Try

    End If

End Sub

{{< /highlight >}}

 يمكنك أيضًا التحقق من الرمز المضاف إلى**Page_Load** معالج الحدث كما هو موضح أدناه في الشكل:

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_40.png)

**شكل:** تمت إضافة الرمز إلى**Page_Load** معالج الحدث

إلى حد بعيد ، قمنا ببناء تطبيق قاعدة بيانات مفيد للغاية. لكن هذا التطبيق يمكّنك فقط من عرض بيانات الجدول. على الرغم من أنه يمكنك تحرير البيانات بتنسيق**شبكة** السيطرة ولكن عندما تغلق نافذة المتصفح الخاص بك وتفتح قاعدة البيانات الخاصة بك. ستجد أنه لم يتغير شيء. هذا يعني أن التغييرات التي أجريتها لم يتم حفظها في قاعدة البيانات. لذا ، هناك شيء ما عليك القيام به.

 سنقوم الآن بإضافة بعض التعليمات البرمجية إلى تطبيقنا بحيث**شبكة** قد يحفظ تغييراته على قاعدة البيانات الفعلية. دعونا فتح**الخصائص** جزء وحدد**SaveCommand** حدث**شبكة** السيطرة من قائمة أحداثها. إذا نقرت مرتين على**SaveCommand** الحدث ثم VS.NET 2005 سيتم إنشاء IDE**GridWeb1_SaveCommand** معالج الحدث لك. أضف بعض التعليمات البرمجية إلى معالج الأحداث هذا لتحديث قاعدة البيانات بالبيانات المعدلة المضمنة في**مجموعة البيانات** (ملزمة بورقة العمل) باستخدام**oleDbDataAdapter1**.

##### **مثال:**

**C#**

{{< highlight "csharp" >}}

 //Implementing the event handler for SaveCommand event

protected void GridWeb1_SaveCommand(object sender, EventArgs e)

{

    try

    {

        //Getting the modified data of worksheet as a DataSet

        DataSet dataset = (DataSet)GridWeb1.WebWorksheets[0].DataSource;

        //Updating database according to modified DataSet

        oleDbDataAdapter1.Update(dataset);

    }

    finally

    {

        //Closing database connection

        oleDbConnection1.Close();

    }

}

{{< /highlight >}}

**VB.NET**

{{< highlight "csharp" >}}

 'Implementing the event handler for SaveCommand event

Protected Sub GridWeb1_SaveCommand(ByVal sender As Object, ByVal e As System.EventArgs)

  Handles GridWeb1.SaveCommand

    Try

        'Getting the modified data of worksheet as a DataSet

        Dim dataset As DataSet = CType(GridWeb1.WebWorksheets(0).DataSource, DataSet)

        'Updating database according to modified DataSet

        oleDbDataAdapter1.Update(dataset)

    Finally

        'Closing database connection

        oleDbConnection1.Close()

    End Try

End Sub

{{< /highlight >}}

 يمكنك أيضًا التحقق من الرمز المضاف إلى**GridWeb1_SaveCommand** معالج الحدث كما هو موضح أدناه في الشكل:

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_41.png)

**شكل:** تمت إضافة الرمز إلى**GridWeb1_SaveCommand** معالج الحدث

 الآن ، إذا كنت ستحفظ التغييرات في قاعدة البيانات باستخدام**يحفظ** زر**شبكة** ، سيتم إنقاذهم بالتأكيد.

##### **الخطوة 8: تشغيل التطبيق الخاص بك**

 أخيرًا ، يمكننا ترجمة تطبيقنا وتشغيله إما بالضغط على**السيطرة + F5** أو النقر**بداية** زر. في مربع حوار التصحيح ، يمكنك تحديد خيار التصحيح المناسب والنقر فوق**نعم** الزر كما هو موضح أدناه في الشكل.

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_42.png)

**شكل:** تطبيق قيد التشغيل

 بعد التجميع ،**Default.aspx** سيتم فتح صفحة تطبيق الويب الخاص بنا في نافذة متصفح جديدة حيث يمكننا رؤية جميع البيانات المحملة من قاعدة البيانات كما هو موضح أدناه:

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_43.png)

**شكل:** تحميل البيانات في**شبكة** السيطرة من قاعدة البيانات

 عندما يتم تحميل البيانات في**شبكة** ثم ستشعر أن Aspose.Cells.GridWeb يوفر تحكمًا ضمنيًا في البيانات لمستخدميه. دعنا نتحقق من نوع ميزات معالجة البيانات التي يقدمها**شبكة** لمستخدميها.

##### **تأكيد صحة البيانات**

Aspose.Cells.GridWeb يقوم تلقائيًا بإنشاء قواعد تحقق مناسبة لكل الأعمدة المرتبطة وفقًا لأنواع البيانات الخاصة بها المعرفة في قاعدة البيانات. يمكنك رؤية نوع التحقق من صحة الخلية عن طريق تحريك مؤشر الماوس عليها كما هو موضح أدناه في الشكل:

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_44.png)

**شكل:**التحقق من نوع التحقق من صحة الخلية

 في الشكل أعلاه ، يمكننا أن نرى أن الخلية المحددة تحتوي على**\ <INT>** نوع التحقق ، مما يعني أنه يمكن للمستخدمين فقط إدخال قيمة عددية إليه وإلا سيحدث خطأ في التحقق من الصحة. علاوة على ذلك،**\ <مطلوب>** يوضح أن قيمة**معرف المنتج** مطلوب لتقديمه من قبل المستخدم.

##### **حذف الصفوف**

 لحذف صف ، يجب عليك أولاً تحديد صف (أو أي خلية في الصف) وتحديده**احذف صف** الخيار من قائمة النقر بزر الماوس الأيمن كما هو موضح أدناه:

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_45.png)

**شكل:** التحديد**احذف صف** خيار من القائمة

 بعد الاختيار**احذف صف** من القائمة ، يتم حذف الصف من ملف**شبكة** . انقر الآن**حفظ** زر**شبكة** لحذف هذا السجل في جدول قاعدة البيانات الأصلي.

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_46.png)

**شكل:** بيانات الشبكة (بعد حذف صف)

##### **تحرير الصفوف**

 يمكنك أيضًا تحرير البيانات في الخلايا أو الصفوف ثم النقر فوق**يحفظ** زر لحفظ التغييرات الخاصة بك.

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_47.png)

**شكل:** بيانات الشبكة (تحرير السجل 1)

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_48.png)

**شكل:** بيانات الشبكة (تحرير السجل 2)

##### **مضيفا الصفوف**

 لإضافة صف ، حدد**اضف سطر** الخيار من قائمة النقر بزر الماوس الأيمن كما هو موضح أدناه:

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_49.png)

**شكل:** التحديد**اضف سطر** خيار من القائمة

ستتم إضافة صف جديد إلى الورقة في نهاية الصفوف بعد التحديد**اضف سطر** خيار من القائمة. على يسار الصف المضاف حديثًا ، ستلاحظ وجود ملف**النجمة** تشير إلى أن الصف مضاف حديثًا.

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_50.png)

**شكل:** تمت إضافة صف جديد إلى الشبكة

 بعد إدخال القيم في الصف الجديد ، انقر فوق**يحفظ** لتأكيد التغييرات في جدول قاعدة البيانات الأصلي كما هو موضح أدناه

![ما يجب القيام به: image_بديل_نص](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_51.png)

**شكل:** حفظ التغييرات لجدول قاعدة البيانات عن طريق النقر**يحفظ** زر

{{% alert color="primary" %}}   {{% /alert %}}

##### **استنتاج**

{{% alert color="primary" %}}

**ربط البيانات** هي سمة مهمة من سمات Aspose.Cells.GridWeb. من السهل حقًا للمطورين ربط أوراق العمل الخاصة بهم باستخدام قاعدة البيانات**مصمم أوراق العمل** فائدة مقدمة من Aspose.Cells.GridWeb. Aspose.Cells.GridWeb مفيد جدًا للمطورين لتوفير وقتهم وجهودهم في إنشاء حلول شبكة قوية.

{{% /alert %}}
