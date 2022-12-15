---
title: ورقة عمل ملزمة لكائن مجموعة مخصص باستخدام GridWeb
type: docs
weight: 130
url: /ar/net/binding-worksheet-to-a-customized-collection-object-using-gridweb/
---
{{% alert color="primary" %}} 

 يوفر إطار Microsoft .NET العديد من فئات التجميع ولكنها في بعض الأحيان لا تفي بمتطلبات التطوير لذلك يقوم المطورون بإنشاء**مجموعات مخصصة**، وقد يتطلب ربط هذه المجموعات المخصصة بـ Aspose.Cells.GridWeb.

{{% /alert %}} 
## **ربط ورقة عمل بمجموعة مخصصة**
لتوضيح هذه الميزة ، تتناول هذه المقالة كيفية إنشاء تطبيق نموذج خطوة بخطوة. أولاً ، قم بإنشاء مجموعة مخصصة ثم استخدم تلك المجموعة للربط بورقة عمل.
### **الخطوة 1: إنشاء سجل مخصص**
قبل إنشاء مجموعة مخصصة ، قم بإنشاء فئة للاحتفاظ بالسجلات المخصصة التي سيتم تخزينها في المجموعة. الغرض من هذه المقالة هو إعطاء فكرة عن كيفية إنشاء مجموعاتك المخصصة وربطها بـ Aspose.Cells.GridWeb ، لذا فإن كيفية إنشاء السجل المخصص متروك لك.

يستخدم المثال أدناه فئة MyCustomRecord التي تحتوي على خمسة حقول خاصة وخمس خصائص عامة تتحكم في الوصول إلى الحقول الخاصة. هنا هيكل الخصائص:

-  خاصية StringField1 للقراءة والكتابة**سلسلة** (سلسلة).
-  خاصية ReadonlyField2 للقراءة فقط**سترينغفيلد 2** (سلسلة).
-  خاصية DateField1 للقراءة والكتابة**datefield1** (التاريخ والوقت).
-  خاصية IntField1 للقراءة والكتابة**intfield1** (عدد صحيح).
-  خاصية DoubleField1 للقراءة والكتابة**مزدوج الحقل 1** (مزدوج).

**C#**

{{< highlight "csharp" >}}

 //Creating a class that will act as record for the custom collection

public class MyCustomRecord

{

    //Private data members

    private string stringfield1;

    private string stringfield2 = "ABC";

    private DateTime datefield1;

    private int intfield1;

    private double doublefield1;

    //Creating a string property

    public string StringField1

    {

        get { return stringfield1; }

        set { stringfield1 = value; }

    }

    //Creating a readonly string property

    public string ReadonlyField2

    {

        get { return stringfield2; }

    }

    //Creating a DateTime property

    public DateTime DateField1

    {

        get { return datefield1; }

        set { datefield1 = value; }

    }

    //Creating an int property

    public int IntField1

    {

        get { return intfield1; }

        set { intfield1 = value; }

    }

    //Creating a double property

    public double DoubleField1

    {

        get { return doublefield1; }

        set { doublefield1 = value; }

    }

}

{{< /highlight >}}
### **الخطوة 2: إنشاء مجموعة مخصصة**
الآن ، قم بإنشاء مجموعة مخصصة لإضافة سجلات العملاء إليها والوصول إليها من. لتسهيل الأمر ، يستخدم هذا المثال فئة MyCollection التي تحتوي على مفهرس للقراءة فقط. باستخدام هذا المفهرس ، يمكننا الحصول على أي سجل مخصص مخزّن في المجموعة.

**C#**

{{< highlight "csharp" >}}

 //Creating a custom collection

public class MyCollection : CollectionBase

{

    //Leaving the collection constructor empty

    public MyCollection()

    {

    }

    //Creating a readonly property for custom collection. This Item property is used by GridWeb control to

    //determine the collection's type

    public MyCustomRecord this[int index]

    {

        get { return (MyCustomRecord)this.List[index]; }

    }

}

{{< /highlight >}}
### **الخطوة 3: ربط ورقة عمل بمجموعة مخصصة**
اكتملت عملية إنشاء مجموعة مخصصة. الآن استخدم المجموعة المخصصة للربط بورقة عمل في Aspose.Cells.GridWeb. قم أولاً بإنشاء نموذج ويب ، وأضف عنصر تحكم GridWeb إليه وأضف بعض التعليمات البرمجية.

لاستخدام المجموعة المخصصة للربط ، قم أولاً بإنشاء كائن من فئة MyCollection (تم إنشاؤه في الخطوة أعلاه).
ثم قم بإنشاء وإضافة كائنات MyCustomRecord إلى كائن MyCollection.

{{% alert color="primary" %}} 

هل تتساءل عن سبب عدم وجود طريقة في فئة MyCollection لإضافة كائن MyCustomRecord إلى المجموعة. ألق نظرة أخرى على الكود أعلاه وستلاحظ أن فئة MyCollection موروثة من فئة CollectionBase (التي طبقت واجهة IList التي توفر طريقة Add لإضافة كائن إلى المجموعة). استخدم طريقة Add من فئة IList عن طريق تنشيط كائن MyCollection إلى IList.

{{% /alert %}} 

أخيرًا ، قم بتعيين كائن MyCollection كمصدر بيانات ورقة العمل وربط ورقة العمل بالمجموعة. في هذه المرحلة ، يمكنك أيضًا إنشاء قواعد التحقق من صحة الأعمدة المرتبطة بورقة العمل.

**C#**

{{< highlight "csharp" >}}

 //Implementing Page_Load event handler

protected void Page_Load(object sender, EventArgs e)

{

    if (Page.IsPostBack == false && this.GridWeb1.IsPostBack == false)

    {

        //Creating an object of custom collection

        MyCollection list = new MyCollection();

        //Creating an instance of Random class

        System.Random rand = new System.Random();

        //Creating a loop that will run 5 times

        for (int i = 0; i < 5; i++)

        {

            //Creating an object of Custom Record

            MyCustomRecord rec = new MyCustomRecord();

            //Initializing all properties of Custom Record

            rec.DateField1 = DateTime.Now;

            rec.DoubleField1 = rand.NextDouble() * 10;

            rec.IntField1 = rand.Next(20);

            rec.StringField1 = "ABC_" + i;

            //Adding Custom Record to Collection

            ((IList)list).Add(rec);

        }

        //Accessing a desired worksheet

        GridWorksheet sheet = GridWeb1.WorkSheets[0];

        //Setting the Data Source of worksheet

        sheet.DataSource = list;

        //Creating columns automatically

        sheet.CreateAutoGenratedColumns();

        //Setting the validation type of value to DateTime

        sheet.BindColumns[2].Validation.ValidationType = ValidationType.DateTime;

        //Binding worksheet

        sheet.DataBind();

        //Assigning an event handler to InitializeNewBindRow event of the worksheet

        //sheet.InitializeNewBindRow += new InitializeNewBindRowHandler(GridWeb1_InitializeNewBindRow);

    }

}

{{< /highlight >}}
### **الخطوة 4: معالجة حدث InitializeNewBindRow الخاص بورقة العمل**
في الكود أعلاه ، ربما لاحظت سطرًا إضافيًا من التعليمات البرمجية المستخدمة لتعيين معالج الأحداث GridWeb1_InitializeNewBindRow إلى InitializeNewBindRow الخاص بورقة العمل. يتم تشغيل هذا الحدث عند إضافة صف منضم جديد إلى ورقة العمل. لقد أنشأنا معالج حدث لهذا الحدث بسبب خاصية DateField1 للكائن MyCustomRecord.

 Aspose.Cells. يتم تهيئة موقعGridWeb تلقائيًا**int** و**مزدوج** القيم مع**صفر (0)**كلما تمت إضافة صف منضم جديد إلى عنصر التحكم GridWeb. بالنسبة للتواريخ ، نود أن يقوم عنصر التحكم GridWeb بإضافة التاريخ الحالي تلقائيًا من النظام. للقيام بذلك ، قمنا بإنشاء معالج الأحداث GridWeb1_InitializeNewBindRow لحدث InitializeNewBindRow.

قم بالوصول إلى مثيل معين لفئة MyCustomRecord من GridWeb باستخدام وسيطة bindObject ثم قم بتعيين تاريخ النظام الحالي إلى خاصية DateField1 الخاصة به.

**C#**

{{< highlight "csharp" >}}

 //Creating GridWeb1_InitializeNewBindRow event handler

private void GridWeb1_InitializeNewBindRow(GridWorksheet sender, object bindObject)

{

    //Accessing that custom record object that is newly bound

    MyCustomRecord rec = (MyCustomRecord)bindObject;

    //Initializing the DateTime of a property when a new row gets bound to the database

    rec.DateField1 = DateTime.Now;

}

{{< /highlight >}}
### **الخطوة الخامسة: تشغيل التطبيق**
 قم بتشغيل التطبيق إما بالضغط على**السيطرة + F5** أو النقر فوق**بداية** زر في VS.NET. يتم فتح نموذج الويب في نافذة متصفح جديدة.

**ورقة عمل مرتبطة بمجموعة مخصصة** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-customized-collection-object-using-gridweb_1.png)



 انقر بزر الماوس الأيمن فوق عنصر التحكم GridWeb لإضافة سجل أو حذفه. على سبيل المثال ، أضف سجلاً جديدًا إلى ورقة العمل عن طريق تحديد**اضف سطر** اختيار.

**تحديد خيار إضافة صف من القائمة** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-customized-collection-object-using-gridweb_2.png)



 عند إضافة صف جديد إلى ورقة العمل ، تحتوي الخلايا على بيانات افتراضية بما في ذلك تاريخ النظام الحالي.

**تمت إضافة صف جديد إلى ورقة العمل بالبيانات الافتراضية** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-customized-collection-object-using-gridweb_3.png)



بعد إجراء التغييرات على البيانات ، انقر فوق**يحفظ** أو**يُقدِّم** لحفظ التغييرات الخاصة بك.

**حفظ التغييرات بالضغط على زر حفظ** 

![ما يجب القيام به: image_بديل_نص](binding-worksheet-to-a-customized-collection-object-using-gridweb_4.png)
## **استنتاج**
{{% alert color="primary" %}} 

توضح هذه المقالة كيفية ربط ورقة عمل بمجموعة مخصصة تم إنشاؤها. باستخدام Aspose.Cells.GridWeb ، يمكن للمطورين ربط أوراق العمل إما بقاعدة بيانات أو مجموعات مخصصة عبر مصمم أوراق العمل في وضع واجهة المستخدم الرسومية أو من خلال الترميز. يوفر هذا مجموعة واسعة من الخيارات للمطورين لإنشاء التطبيقات.

{{% /alert %}}
