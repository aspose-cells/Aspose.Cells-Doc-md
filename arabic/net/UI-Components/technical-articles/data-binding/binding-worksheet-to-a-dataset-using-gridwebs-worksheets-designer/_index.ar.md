---
title: ربط ورقة العمل بمجموعة بيانات باستخدام مصمم أوراق عمل GridWebs
type: docs
weight: 20
url: /ar/net/binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer/
---
{{% alert color="primary" %}} 

 تتناول هذه المقالة طريقة سهلة لربط أوراق العمل بجداول قاعدة البيانات في وضع واجهة المستخدم الرسومية باستخدام أداة خاصة متوفرة مع Aspose.Cells.GridWeb ، مصمم أوراق العمل.

{{% /alert %}} 
## **ربط ورقة عمل بقاعدة البيانات باستخدام مصمم أوراق العمل**
	**الخطوة 1: إنشاء نموذج قاعدة بيانات**
1. أولاً ، نقوم بإنشاء نموذج قاعدة البيانات التي سيتم استخدامها في هذه المقالة. نحن نستخدم Microsoft Access لإنشاء قاعدة بيانات تحتوي على جدول يسمى المنتجات. يتم عرض المخطط أدناه.
   **معلومات تصميم جدول المنتجات** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_1.png)




1. يتم إضافة عدد قليل من السجلات الوهمية إلى جدول المنتجات.
   **السجلات في جدول المنتجات** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_2.png)
### **الخطوة الثانية: تصميم نموذج التطبيق**
 تم إنشاء وتصميم تطبيق ويب ASP.NET في Visual Studio.NET كما هو موضح أدناه.
**تطبيق نموذج مصمم** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_3.png)
### **الخطوة 3: الاتصال بقاعدة البيانات باستخدام Server Explorer**
 حان الوقت للاتصال بقاعدة البيانات. يمكننا القيام بذلك بسهولة باستخدام Server Explorer في Visual Studio.NET.

1.  يختار**اتصال البيانات** في**مستكشف الخادم** وانقر بزر الماوس الأيمن.
1.  يختار**إضافة اتصال** من القائمة.
   **تحديد خيار إضافة اتصال** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_4.png)



 يتم عرض مربع حوار خصائص ارتباط البيانات.
**مربع حوار خصائص ارتباط البيانات** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_5.png)



 باستخدام هذا الحوار ، يمكنك الاتصال بأي قاعدة بيانات. بشكل افتراضي ، يسمح لك بالاتصال بقاعدة بيانات SQL Server. في هذا المثال ، نحتاج إلى الاتصال بقاعدة بيانات Microsoft Access.

1.  انقر على**مزود** التبويب.
1.  يختار**Microsoft Jet 4.0 OLE DB Provider** من**موفر (موفرو) OLE DB** قائمة.
1.  انقر**التالي**.
   **النقر فوق التالي بعد تحديد موفر OLE DB** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_6.png)


 ال**اتصال** تم فتح صفحة علامة التبويب.

1.  حدد ملف قاعدة بيانات Access Microsoft (في حالتنا ، db.mdb) وانقر**نعم**.
   **النقر فوق الزر "موافق" بعد اختيار ملف قاعدة البيانات** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_7.png)

{{% alert color="primary" %}} 

 بعد النقر**نعم** ، سيتم إنشاء اتصال قاعدة البيانات بقاعدة بيانات Access Microsoft في**مستكشف الخادم**انقر نقرًا مزدوجًا فوق الاتصال لمشاهدة جميع الجداول وطرق العرض والإجراءات المخزنة في قاعدة البيانات.

{{% /alert %}} 
### **الخطوة 4: إنشاء كائنات اتصال قاعدة البيانات بيانياً**
1.  تصفح الجداول في قاعدة البيانات باستخدام ملف**مستكشف الخادم**.
 يوجد جدول واحد فقط ، المنتجات.
1.  قم بسحب وإسقاط جدول المنتجات من ملف**مستكشف الخادم** الى**نموذج ويب**.
   **سحب جدول المنتجات من Server Explorer وإسقاطه إلى نموذج الويب** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_8.png)



قد يظهر مربع حوار.
**مربع حوار لتأكيد تضمين كلمة مرور قاعدة البيانات في سلسلة الاتصال** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_9.png)



 حدد ما إذا كنت تريد تضمين كلمة مرور قاعدة البيانات في سلسلة الاتصال أم لا. في هذا المثال ، اخترنا**لا تقم بتضمين كلمة المرور**. 
تم إنشاء كائنين لاتصال قاعدة البيانات (oleDbConnection1 و oleDbDataAdapter1) وإضافتهما.
**تم إنشاء كائنات اتصال قاعدة البيانات (oleDbConnection1 & oleDbDataAdapter1) وعرضها** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_10.png)



### **الخطوة 5: إنشاء DataSet**
حتى الآن ، أنشأنا كائنات اتصال قاعدة البيانات ولكننا ما زلنا بحاجة إلى مكان لتخزين البيانات بعد الاتصال بقاعدة البيانات. يمكن لعنصر DataSet تخزين البيانات بدقة ويمكننا أيضًا إنشاؤها بسهولة باستخدام VS.NET IDE.

1.  يختار**oleDbDataAdaper1** وانقر بزر الماوس الأيمن.
1.  يختار**توليد مجموعة البيانات** خيار من القائمة.
   **تحديد خيار إنشاء مجموعة البيانات** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_11.png)



 يتم عرض مربع الحوار "إنشاء مجموعة البيانات".
 هنا ، من الممكن تحديد اسم لكائن DataSet الجديد الذي سيتم إنشاؤه والجداول التي يجب إضافتها إليه.

1.  حدد ملف**أضف مجموعة البيانات هذه إلى المصمم** اختيار.
1.  انقر**نعم**.
   **النقر فوق الزر "موافق" لإنشاء DataSet** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_12.png)



يتم إضافة كائن dataSet11 إلى المصمم.
**تم إنشاء مجموعة البيانات وإضافتها إلى المصمم** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_13.png)
### **الخطوة 6: استخدام مصمم أوراق العمل**
 الآن ، حان الوقت لكشف السر.

1. حدد عنصر التحكم GridWeb وانقر بزر الماوس الأيمن.
1.  يختار**مصمم أوراق العمل** خيار من القائمة.

   **تحديد خيار مصمم أوراق العمل** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_14.png)



 يتم عرض محرر مجموعة أوراق العمل (يسمى أيضًا مصمم أوراق العمل).
**مربع حوار محرر مجموعة أوراق العمل** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_15.png)



يحتوي مربع الحوار على العديد من الخصائص التي يمكن تكوينها لربط الورقة 1 بأي جدول في قاعدة البيانات.

1.  حدد ملف**مصدر البيانات** خاصية.
 يتم سرد الكائن dataSet11 الذي تم إنشاؤه في الخطوة السابقة في القائمة.
1. حدد البيانات
1.  انقر على**عضو البيانات** خاصية.
 يعرض "مصمم أوراق العمل" تلقائيًا قائمة بالجداول في dataSet11. يوجد جدول واحد فقط ، المنتجات.
1. حدد جدول المنتجات.
   **تعيين خصائص DataSource و DataMember** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_16.png)




1.  افحص ال**BindColumns** خاصية.
   **النقر فوق خاصية BindColumns** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_17.png)



 النقر فوق ملف**BindColumns** الخاصية تفتح محرر مجموعة BindColumn.
**محرر مجموعة BindColumn** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_18.png)



 في محرر مجموعة BindColumn ، تكون جميع أعمدة ملحق**منتجات** يتم إضافة الجدول تلقائيًا إلى مجموعة BindColumns.

1. حدد أي عمود وخصص خصائصه.
 على سبيل المثال ، يمكنك تعديل تسمية كل عمود.
   **تعديل التسمية التوضيحية لعمود ProductID** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_19.png)




1.  بعد إجراء التغييرات ، انقر فوق**نعم**.
1.  أغلق جميع مربعات الحوار عن طريق النقر**نعم**.
 أخيرًا ، يتم إرجاعك إلى صفحة WebForm1.aspx.
   **العودة إلى صفحة WebForm1.aspx بعد استخدام "مصمم أوراق العمل"** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_20.png)


 أعلاه ، يظهر اسم عمود جدول المنتجات. عرض الأعمدة صغير لذا فإن الأسماء الكاملة لبعض الأعمدة غير مرئية بالكامل.
### **الخطوة 7: إضافة رمز إلى Page_Load Event Handler**
 لقد استخدمنا مصمم أوراق العمل والآن علينا فقط إضافة رمز إلى معالج الأحداث Page_Load لملء كائن dataSet11 ببيانات من قاعدة البيانات (باستخدام oleDbDataAdapter1) وربط عنصر تحكم GridWeb بـ dataSet11 عن طريق استدعاء أسلوب DataBind الخاص به.

1.  أضف الكود:

**C#**

{{< highlight "csharp" >}}

 //Implementing Page_Load event handler

private void Page_Load(object sender, System.EventArgs e)

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

Private Sub Page_Load(ByVal sender As Object, ByVal e As System.EventArgs) Handles MyBase.Load

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

1. تحقق من الشفرة المضافة إلى معالج الأحداث Page_Load.
   **تمت إضافة الرمز إلى معالج الأحداث Page_Load** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_21.png)
### **الخطوة 8: تشغيل التطبيق**
 ترجمة التطبيق وتشغيله: اضغط إما**السيطرة + F5** أو انقر**بداية**. 
**تشغيل التطبيق** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_22.png)



بعد التحويل البرمجي ، يتم فتح صفحة WebForm1.aspx في نافذة مستعرض مع تحميل كافة البيانات من قاعدة البيانات.
**البيانات التي تم تحميلها في عنصر التحكم GridWeb من قاعدة البيانات** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_23.png)
## **العمل مع GridWeb Control**
 عندما يتم تحميل البيانات في عنصر التحكم GridWeb فإنه يوفر للمستخدمين التحكم في البيانات. يقدم GridWeb عددًا من الأنواع المختلفة من ميزات معالجة البيانات.
### **تأكيد صحة البيانات**
Aspose.Cells.GridWeb يقوم تلقائيًا بإنشاء قواعد تحقق مناسبة لكل الأعمدة المرتبطة وفقًا لأنواع البيانات المعرفة في قاعدة البيانات. اطلع على نوع التحقق من صحة الخلية عن طريق تمرير المؤشر فوقها.
**التحقق من نوع التحقق من صحة الخلية** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_24.png)

 هنا ، تحتوي الخلية المحددة على ملف**<INT>** التحقق من الصحة ، مما يعني أنه يمكن للمستخدمين إدخال قيم صحيحة فقط فيه. إذا أدخلوا قيمة أخرى ، يحدث خطأ في التحقق من الصحة. علاوة على ذلك،**<مطلوب>** يوضح أنه يجب تقديم معرّف المنتج للقيمة.
### **حذف الصفوف**
 لحذف صف ، حدد صفًا (أو أي خلية في الصف) ، وانقر بزر الماوس الأيمن وحدد**احذف صف**.
**تحديد خيار حذف الصف من القائمة** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_25.png)


سيتم حذف الصف على الفور.
**بيانات الشبكة (بعد حذف صف)** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_26.png)
### **تحرير الصفوف**
قم بتحرير البيانات في الخلايا أو الصفوف ثم انقر فوق**يحفظ** أو**يُقدِّم** لحفظ التغييرات.
### **مضيفا الصفوف**
1.  لإضافة صف ، انقر بزر الماوس الأيمن فوق خلية وحددها**اضف سطر**.
   **تحديد خيار إضافة صف من القائمة** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_27.png)



يتم إضافة صف جديد إلى الورقة في نهاية الصفوف الأخرى.
**تمت إضافة صف جديد إلى الشبكة** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_28.png)



 توجد علامة النجمة على يسار الصف الجديد{{< emoticons/cross >}} ، مما يشير إلى أن الصف جديد.

1. أضف القيم إلى الصف الجديد.
1.  انقر**يحفظ** أو**يُقدِّم** لتأكيد التغيير.
   **حفظ التغييرات على البيانات بالنقر فوق * حفظ** زر*

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_29.png)
### **ضبط تنسيق الرقم**
 في الوقت الحالي ، فإن الأسعار في**سعر المنتج** يتم عرض العمود كقيم عددية. من الممكن جعلها تبدو وكأنها عملة.

1. العودة إلى Visual Studio.NET.
1. افتح محرر مجموعة BindColumn.
 ال**نوع_الرقم** ممتلكات**سعر المنتج** تم تعيين العمود إلى**عام**.
   **تم تعيين الخاصية NumberType على عام** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_30.png)




1.  انقر**قائمة منسدلة** واختر**العملة 4** من القائمة.
   **تم تغيير الخاصية NumberType إلى Currency4** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_31.png)




1. قم بتشغيل التطبيق مرة أخرى.
 القيم الموجودة في**سعر المنتج** العمود هو العملة الآن.
   **أسعار المنتجات بتنسيق رقم العملة** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_32.png)
### **تعديل بيانات**
 يسمح التطبيق حتى الآن لمستخدميه فقط بعرض بيانات الجدول. يمكن للمستخدمين تحرير البيانات في عنصر التحكم GridWeb ولكن عند إغلاق المتصفح وفتح قاعدة البيانات ، لم يتغير شيء. لا يتم حفظ التغييرات التي تم إجراؤها في قاعدة البيانات.

 يضيف المثال التالي التعليمات البرمجية إلى التطبيق بحيث يمكن لـ GridWeb حفظ التغييرات في قاعدة البيانات.

1. افتح ال**ملكيات** جزء وحدد الحدث SaveCommand لعنصر تحكم GridWeb من القائمة.
   **تحديد حدث SaveCommand من GridWeb** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_33.png)




1.  انقر نقرًا مزدوجًا فوق ملف**SaveCommand** يقوم الحدث و VS.NET بإنشاء معالج الأحداث GridWeb1_SaveCommand.
1.  أضف التعليمات البرمجية إلى معالج الأحداث هذا الذي سيقوم بتحديث قاعدة البيانات بأي بيانات معدلة في DataSet المرتبطة بورقة العمل باستخدام oleDbDataAdapter1.

**C#**

{{< highlight "csharp" >}}

 //Implementing the event handler for SaveCommand event

private void GridWeb1_SaveCommand(object sender, System.EventArgs e)

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

Private Sub GridWeb1_SaveCommand(ByVal sender As Object, ByVal e As System.EventArgs) Handles GridWeb1.SaveCommand

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

يمكنك أيضًا التحقق من الكود المضاف إلى معالج الأحداث GridWeb1_SaveCommand
**تمت إضافة التعليمات البرمجية إلى معالج الأحداث GridWeb1_SaveCommand** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_34.png)

 احفظ التغييرات في قاعدة البيانات باستخدام ملف**يحفظ** زر الآن يحفظها بالتأكيد.
## **استنتاج**
{{% alert color="primary" %}} 

يعد ربط البيانات ميزة مهمة في Aspose.Cells.GridWeb. من السهل ربط أوراق العمل بقاعدة بيانات باستخدام الأداة المساعدة Worksheets Designer المقدمة من Aspose.Cells.GridWeb. Aspose.Cells.GridWeb يوفر الوقت والجهد عند إنشاء حلول شبكة قوية.

{{% /alert %}}
