---
title: ربط ورقة العمل بمجموعة بيانات باستخدام مصمم ورقة العمل في GridWeb
type: docs
weight: 20
url: /ar/net/aspose-cells-gridweb/bind-worksheet-to-a-dataset-use-designer/
keywords: GridWeb,bind,DataSet,Designer,designer
description: يقدم هذا المقال كيفية استخدام مصمم ورق العمل لربط ورق العمل بمجموعة بيانات في GridWeb.
---

{{% alert color="primary" %}} 

يناقش هذا المقال نهجًا سهلاً لربط أوراق العمل بجداول قاعدة البيانات في وضع واجهة المستخدم الرسومية باستخدام أداة خاصة تُتيحها Aspose.Cells.GridWeb، وهو مصمم ورق العمل. 

{{% /alert %}} 
## **ربط ورق العمل بقاعدة بيانات باستخدام مصمم ورق العمل**
	**الخطوة 1: إنشاء قاعدة بيانات نموذجية**
1. أولاً، نقوم بإنشاء قاعدة البيانات النموذج التي سيتم استخدامها في هذا المقال. نحن نستخدم Microsoft Access لإنشاء قاعدة بيانات تحتوي على جدول يسمى المنتجات. يُظهر هيكلها أدناه.
   **معلومات التصميم حول جدول المنتجات** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_1.png)




1. يتم إضافة بضع سجلات وهمية إلى جدول المنتجات.
   **السجلات في جدول المنتجات** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_2.png)
### **الخطوة 2: تصميم التطبيق النموذجي**
تم إنشاء تطبيق ويب ASP.NET وتصميمه في Visual Studio.NET كما هو موضح أدناه. 
**تصميم التطبيق النموذجي** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_3.png)
### **الخطوة 3: الاتصال بقاعدة بيانات باستخدام مستكشف الخادم**
حان الوقت للاتصال بقاعدة البيانات. يمكننا القيام بذلك بسهولة باستخدام مستكشف الخادم في Visual Studio.NET. 

1. حدد **اتصال البيانات** في **مستكشف الخادم** وانقر بزر الماوس الأيمن.
1. حدد **إضافة اتصال** من القائمة.
   **اختيار خيار إضافة اتصال** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_4.png)



يتم عرض مربع الحوار خصائص رابط البيانات. 
**مربع حوار خصائص رابط البيانات** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_5.png)



باستخدام هذا الحوار، يمكنك الاتصال بأي قاعدة بيانات. بشكل افتراضي، يتيح لك الاتصال بقاعدة بيانات SQL Server. لهذا المثال، نحتاج إلى الاتصال بقاعدة بيانات Microsoft Access. 

1. انقر على علامة التبويب **المزود**.
1. حدد **مزود بيانات Microsoft Jet 4.0 OLE DB** من قائمة **مزودات OLE DB(s)**.
1. انقر فوق **التالي**.
   **النقر على التالي بعد تحديد مزود بيانات OLE DB** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_6.png)


تم فتح صفحة التبويب **الاتصال**. 

1. حدد ملف قاعدة بيانات Microsoft Access (في حالتنا، db.mdb) وانقر على **موافق**.
   **النقر على زر موافق بعد تحديد ملف قاعدة البيانات** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_7.png)

{{% alert color="primary" %}} 

بعد النقر على **موافق**, سيتم إنشاء اتصال قاعدة بيانات بقاعدة بيانات Microsoft Access في **استكشاف الخادم**. انقر مرتين على الاتصال لرؤية كافة الجداول، والمشاهد، والإجراءات المخزنة في القاعدة بيانات.

{{% /alert %}} 
### **الخطوة 4: إنشاء أجسام اتصال قاعدة البيانات بشكل رسومي**
1. استعرض الجداول في قاعدة البيانات باستخدام **استكشاف الخادم**.
   هناك جدول واحد فقط، وهو الجدول المنتجات. 
1. اسحب وأسقط جدول المنتجات من **استكشاف الخادم** إلى **النموذج الويب**.
   **سحب جدول المنتجات من استكشاف الخادم وإسقاطه إلى النموذج الويب** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_8.png)



قد يظهر حوار.
**مربع الحوار لتأكيد تضمين كلمة مرور قاعدة البيانات في سلسلة الاتصال** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_9.png)



قرر ما إذا كنت ترغب في تضمين كلمة مرور قاعدة البيانات في سلسلة الاتصال أم لا. لهذا المثال، اخترنا **لا تضمن كلمة المرور**. 
تم إنشاء اثنين من أجسام اتصال قاعدة البيانات (oleDbConnection1 وoleDbDataAdapter1) وأُضيفا.
**تم إنشاء أجسام اتصال القاعدة de البيانات (oleDbConnection1 &oleDbDataAdapter1) وعرضها** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_10.png)



### **الخطوة 5: إنشاء مجموعة بيانات**
حتى الآن، قمنا بإنشاء أجسام اتصال قاعدة البيانات لكننا لا نزال بحاجة إلى مكان لتخزين البيانات بعد الاتصال بقاعدة البيانات. يمكن لكائن DataSet تخزين البيانات بدقة ويمكننا أيضًا إنشائه بسهولة باستخدام برنامج التطوير المُتكامل لـ VS.NET. 

1. حدد **oleDbDataAdaper1** وانقر بزر الماوس الأيمن.
1. حدد خيار **إنشاء مجموعة البيانات** من القائمة.
   **تحديد خيار إنشاء مجموعة البيانات** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_11.png)



يتم عرض حوار إنشاء مجموعة البيانات. 
هنا، يمكن اختيار اسم للكائن مجموعة البيانات الجديدة التي سيتم إنشاؤها، وأي جداول يجب إضافتها إليها. 

1. حدد خيار **أضف مجموعة البيانات هذه إلى المصمم**.
1. انقر على **موافق**.
   **النقر على زر موافق لإنشاء مجموعة البيانات** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_12.png)



تمت إضافة كائن dataSet11 إلى المصمم.
**تم إنشاء مجموعة البيانات وإضافتها إلى المصمم** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_13.png)
### **الخطوة 6: استخدام مصمم الأوراق العمل**
الآن، حان وقت فتح السر. 

1. حدد عنصر التحكم GridWeb وانقر بزر الماوس الأيمن.
1. حدد خيار **مصمم الأوراق العمل** من القائمة. 

   **تحديد خيار مصمم الأوراق العمل** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_14.png)



يتم عرض محرر مجموعة الأوراق العمل (المعروف أيضًا بمصمم الأوراق العمل). 
**حوار محرر مجموعة الأوراق العمل** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_15.png)



يحتوي الحوار على عدة خصائص يمكن تكوينها لربط Sheet1 بأي جدول في قاعدة البيانات.

1. حدد خاصية **مصدر البيانات**.
   يتم سرد كائن dataSet11 الذي تم إنشاؤه في الخطوة السابقة في القائمة. 
1. حدد dataSet11.
1. انقر فوق خاصية **DataMember**.
   تُظهر أداة تصميم أوراق العمل قائمة من الجداول في dataSet11. هناك جدول واحد فقط، وهو Products.
1. حدد جدول Products.
   **تعيين خصائص DataSource و DataMember** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_16.png)




1. تحقق من خاصية **BindColumns**.
   **فتح خاصية BindColumns** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_17.png)



يفتح النقر على خاصية **BindColumns** محرر مجموعة BindColumn.
**محرر مجموعة BindColumn** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_18.png)



في محرر مجموعة BindColumn، يتم إضافة جميع أعمدة جدول **Products** تلقائيًا إلى مجموعة BindColumns. 

1. حدد أي عمود وقم بتخصيص خصائصه.
   على سبيل المثال، يمكنك تعديل تسمية كل عمود.
   **تعديل تسمية عمود ProductID** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_19.png)




1. بعد إجراء التغييرات، انقر فوق **موافق**.
1. أغلق جميع الحوارات بالنقر على **موافق**.
   وأخيرًا، ستتم إعادتك إلى صفحة WebForm1.aspx. 
   **العودة إلى صفحة WebForm1.aspx بعد استخدام أداة تصميم أوراق العمل** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_20.png)


أعلاه، يُظهر اسم العمود في جدول Products. عرض الأعمدة صغير لذا فإن أسماء بعض الأعمدة لا تظهر بالكامل. 
### **الخطوة 7: إضافة كود إلى معالج حدث Page_Load**
لقد استخدمنا أداة تصميم أوراق العمل والآن يتوجب علينا فقط إضافة الكود إلى معالج حدث Page_Load لملء الكائن dataSet11 بالبيانات من قاعدة البيانات (باستخدام oleDbDataAdapter1) وربط عنصر التحكم GridWeb بـ dataSet11 باستدعاء طريقة DataBind الخاصة به. 

1. أضف الكود: 

**C#**

{{< highlight csharp >}}

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

{{< highlight csharp >}}

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

1. تحقق من اضافة الكود إلى معالج حدث "Page_Load".
   **الكود المضاف إلى معالج حدث "Page_Load"** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_21.png)
### **الخطوة 8: تشغيل التطبيق**
قم بتجميع وتشغيل التطبيق: إما اضغط **Ctrl+F5** أو انقر على **بدء**. 
**تشغيل التطبيق** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_22.png)



بعد التجميع، يتم فتح صفحة WebForm1.aspx في نافذة المتصفح مع جميع البيانات المحملة من قاعدة البيانات.
**البيانات المحملة في عنصر تحكم GridWeb من قاعدة البيانات** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_23.png)
## **العمل مع عنصر تحكم GridWeb**
عندما يتم تحميل البيانات في عنصر تحكم GridWeb، يوفر للمستخدمين السيطرة على البيانات. ويتم تقديم عدد من أنواع مختلفة من ميزات التلاعب بالبيانات من قبل GridWeb. 
### **التحقق من البيانات**
يقوم Aspose.Cells.GridWeb تلقائيًا بإنشاء قواعد التحقق المناسبة لجميع الأعمدة المرتبطة وفقًا لأنواع البيانات المحددة في قاعدة البيانات. انظر نوع التحقق لخلية عن طريق تحريك المؤشر فوقها.
**التحقق من نوع البيانات للخلية** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_24.png)

Here, the selected cell contains the **<INT>** validation, which means that users can only enter integer values into it. If they enter another value, a validation error occurs. Moreover, **<REQUIRED>** shows that the value Product ID must be submitted. 
### **حذف الصفوف**
لحذف صف، حدد صفًا (أو أي خلية في الصف)، انقر بزر الماوس الأيمن وحدد **حذف الصف**.
**اختيار خيار حذف الصف من القائمة** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_25.png)


ستتم حذف الصف على الفور.
**بيانات الشبكة (بعد حذف الصف)** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_26.png)
### **تحرير الصفوف**
تحرير البيانات في الخلايا أو الصفوف ثم انقر فوق ** حفظ ** أو ** تقديم ** لحفظ التغييرات. 
### **إضافة الصفوف**
1. لإضافة صف، انقر بزر الماوس الأيمن فوق خلية واختر ** إضافة صف **.
   **اختيار خيار إضافة صف من القائمة** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_27.png)



يتم إضافة صف جديد إلى الورقة في نهاية الصفوف الأخرى.
**تمت إضافة صف جديد إلى الشبكة** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_28.png)



At the left of the new row is an asterisk {{< emoticons/cross >}}, indicating that the row is new. 

1. إضافة قيم إلى الصف الجديد.
1. انقر فوق ** حفظ ** أو ** تقديم ** لتأكيد التغيير.
   **حفظ التغييرات على البيانات عن طريق النقر على زر الحفظ* 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_29.png)
### **ضبط تنسيق الأرقام**
في الوقت الحالي، تظهر الأسعار في عمود ** سعر المنتج ** كقيم رقمية. من الممكن أن يتم تغيير مظهرها لتبدو وكأنها عملة.

1. العودة إلى Visual Studio.NET.
1. فتح محرر مجموعة BindColumn.
   تم تعيين خاصية ** نوع الرقم ** لعمود ** سعر المنتج ** إلى ** عام **.
   **تم تعيين خاصية نوع الرقم إلى عام** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_30.png)




1. انقر فوق ** DropDownList ** واختر ** Currency4 ** من القائمة.
   **تغيير نوع الرقم إلى Currency4** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_31.png)




1. قم بتشغيل التطبيق مرة أخرى.
   القيم في عمود ** سعر المنتج ** الآن هي عملة.
   **أسعار المنتجات بتنسيق العملة** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_32.png)
### **تحرير البيانات**
حتى الآن، يسمح التطبيق بعرض بيانات الجدول فقط لمستخدميه. يمكن للمستخدمين تحرير البيانات في عنصر التحكم GridWeb ولكن عند إغلاق المتصفح وفتح قاعدة البيانات، لا يتم تغيير أي شيء. التغييرات التي تم إجراؤها لا تُحفظ في قاعدة البيانات. 

المثال التالي يضيف شيفرة إلى التطبيق حتى يتمكن GridWeb من حفظ التغييرات في قاعدة البيانات. 

1. افتح لوحة الخصائص واختر حدث SaveCommand لعنصر التحكم GridWeb من القائمة.
   اختيار حدث SaveCommand ل GridWeb 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_33.png)




1. انقر نقرًا مزدوجًا على حدث SaveCommand وينشئ VS.NET معالج حدث GridWeb1_SaveCommand.
1. أضف شيفرة إلى هذا المعالج لتحديث قاعدة البيانات باستخدام أي بيانات معدلة في مجموعة البيانات المقيدة بالجدول باستخدام oleDbDataAdapter1. 

**C#**

{{< highlight csharp >}}

 //Implementing the event handler for SaveCommand event

private void GridWeb1_SaveCommand(object sender, System.EventArgs e)

{

    try

    {

        //Getting the modified data of worksheet as a DataSet

        DataSet dataset = (DataSet)GridWeb1.WorkSheets[0].DataSource;

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

{{< highlight csharp >}}

 'Implementing the event handler for SaveCommand event

Private Sub GridWeb1_SaveCommand(ByVal sender As Object, ByVal e As System.EventArgs) Handles GridWeb1.SaveCommand

    Try

        'Getting the modified data of worksheet as a DataSet

        Dim dataset As DataSet = CType(GridWeb1.WorkSheets(0).DataSource, DataSet)

        'Updating database according to modified DataSet

        oleDbDataAdapter1.Update(dataset)

    Finally

        'Closing database connection

        oleDbConnection1.Close()

    End Try

End Sub



{{< /highlight >}}

يمكنك أيضًا التحقق من الشيفرة المُضافة إلى معالج الحدث GridWeb1_SaveCommand
الشيفرة المُضافة إلى معالج الحدث GridWeb1_SaveCommand 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_34.png)

يتم حفظ التغييرات في قاعدة البيانات باستخدام زر الحفظ الآن بالتأكيد
## **الاستنتاج**
{{% alert color="primary" %}} 

ربط البيانات هو ميزة هامة في Aspose.Cells.GridWeb. من السهل ربط أوراق العمل بقاعدة البيانات باستخدام أداة مصمم الأوراق العمل المُقدمة من Aspose.Cells.GridWeb. يوفر Aspose.Cells.GridWeb الوقت والجهد عند إنشاء حلول جدولية قوية. 

{{% /alert %}}
