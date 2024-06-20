---
title: ربط الورقة العمل بكائن مجموعة مخصص باستخدام GridWeb
type: docs
weight: 130
url: /ar/net/aspose-cells-gridweb/bind-worksheet-to-a-customized-collection-object-using-gridweb/
keywords: GridWeb,bind
description: يقدم هذا المقال كيفية ربط الورقة العمل بمجموعة في GridWeb. 
---

{{% alert color="primary" %}} 

تقدم إطار العمل Microsoft .NET العديد من فئات المجموعات ولكن في بعض الأحيان لا تلبي متطلبات التطوير لذا يقوم المطورون بإنشاء **مجموعات مخصصة**، ويمكنك ربط ورقة عمل مع مثل تلك المجموعات المخصصة في GridWeb.

{{% /alert %}} 
## **ربط ورقة العمل بمجموعة مخصصة**
لتوضيح هذه الميزة، يقوم هذا المقال بشرح كيفية إنشاء تطبيق عيني خطوة بخطوة. أولاً، قم بإنشاء مجموعة مخصصة ثم استخدم تلك المجموعة للربط بورقة العمل.
### **الخطوة 1: إنشاء سجل مخصص**
قبل إنشاء مجموعة مخصصة، قم بإنشاء صنف لاحتواء السجلات المخصصة التي سيتم تخزينها في المجموعة. الغرض من هذا المقال هو إعطاء فكرة عن كيفية إنشاء مجموعاتك المخصصة الخاصة وربطها بـGridWeb، لذلك كيفية إنشاء السجل المخصص يعتمد عليك.

يستخدم المثال أدناه صنف MyCustomRecord الذي يحتوي على خمسة حقول خاصة وخمس خصائص عامة تسيطر على الوصول إلى الحقول الخاصة. إليك هيكل الخصائص:

- الخاصية StringField1 لقراءة وكتابة stringfield1 (string).
- الخاصية ReadonlyField2 لقراءة فقط stringfield2 (string).
- الخاصية DateField1 لقراءة وكتابة datefield1 (DateTime).
- الخاصية IntField1 لقراءة وكتابة intfield1 (integer).
- الخاصية DoubleField1 لقراءة وكتابة doublefield1 (double).

**C#**

{{< highlight csharp >}}

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
الآن، أنشئ مجموعة مخصصة لإضافة سجلات العملاء والوصول إليها. لتبسيط الأمور، يستخدم هذا المثال فئة MyCollection التي تحتوي على مؤشر ثابت. باستخدام هذا المؤشر، يمكننا الحصول على أي سجل مخصص مخزن في المجموعة.

**C#**

{{< highlight csharp >}}

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
انتهى عملية إنشاء مجموعة مخصصة الآن. الآن استخدم المجموعة المخصصة لربطها بورقة عمل في Aspose.Cells.GridWeb. أولاً، أنشئ نموذج ويب، أضف عنصر التحكم GridWeb إليه وأضف بعض الشفرة.

لاستخدام المجموعة المخصصة للربط، أنشئ أولاً كائنًا من فئة MyCollection (التي تم إنشاؤها في الخطوة السابقة).
ثم أنشئ وأضف كائنات MyCustomRecord إلى كائن MyCollection.

{{% alert color="primary" %}} 

هل تتساءل لماذا لم تكن هناك طريقة في فئة MyCollection لإضافة كائن MyCustomRecord إلى المجموعة. انظر مرة أخرى إلى الشيفرة أعلاه وستلاحظ أن فئة MyCollection مشتقة من فئة CollectionBase (التي نفذت واجهة IList التي توفر طريقة Add لإضافة كائن إلى المجموعة). استخدم طريقة Add في الفئة IList عن طريق رفع كائن MyCollection إلى IList.

{{% /alert %}} 

أخيراً، قم بتعيين كائن MyCollection كمصدر بيانات الورقة وقم بربط الورقة بالمجموعة. في هذه النقطة، يمكنك أيضًا إنشاء قواعد التحقق لأعمدة الورقة المُرتبطة.

**C#**

{{< highlight csharp >}}

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
### **الخطوة 4: التعامل مع حدث InitializeNewBindRow للورقة العمل**
في الشيفرة أعلاه، قد تلاحظ سطر إضافي من الشيفرة يستخدم لتعيين معالج حدث GridWeb1_InitializeNewBindRow لحدث InitializeNewBindRow للورقة العمل. يتم تشغيل هذا الحدث كلما تم إضافة صف مُربط جديد إلى ورقة العمل. قمنا بإنشاء معالج حدث لهذا الحدث بسبب خاصية DateField1 لكائن MyCustomRecord.

يقوم Aspose.Cells.GridWeb تلقائيًا بتهيئة القيم الصحيحة والعشرية بالصفر (0) كلما تمت إضافة صف مُربط جديد إلى عنصر التحكم GridWeb. بالنسبة للتواريخ، نود من عنصر التحكم GridWeb أن يُضيف تاريخ النظام الحالي تلقائيًا. للقيام بذلك، قمنا بإنشاء معالج حدث GridWeb1_InitializeNewBindRow للحدث InitializeNewBindRow.

الوصول إلى حالة معينة من فئة MyCustomRecord من GridWeb باستخدام argument bindObject ومن ثم قم بتعيين تاريخ النظام الحالي لخاصية DateField1.

**C#**

{{< highlight csharp >}}

 //Creating GridWeb1_InitializeNewBindRow event handler

private void GridWeb1_InitializeNewBindRow(GridWorksheet sender, object bindObject)

{

    //Accessing that custom record object that is newly bound

    MyCustomRecord rec = (MyCustomRecord)bindObject;

    //Initializing the DateTime of a property when a new row gets bound to the database

    rec.DateField1 = DateTime.Now;

}

{{< /highlight >}}
### **الخطوة 5: تشغيل التطبيق**
قم بتشغيل التطبيق عن طريق الضغط على **Ctrl+F5** أو النقر فوق زر **Start** في VS.NET. يتم فتح نموذج الويب في نافذة متصفح جديدة. 

**ورقة العمل مُربوطة بمجموعة مخصصة** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_1.png)



انقر بزر الماوس الأيمن على عنصر تحكم GridWeb لإضافة أو حذف سجل. على سبيل المثال، أضف سجلًا جديدًا إلى ورق العمل عن طريق تحديد خيار **إضافة صف**. 

**تحديد خيار إضافة صف من القائمة** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_2.png)



عند إضافة صف جديد إلى ورق العمل، تحتوي الخلايا على بيانات افتراضية بما في ذلك تاريخ النظام الحالي. 

**تمت إضافة صف جديد إلى ورق العمل ببيانات افتراضية** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_3.png)



بعد إجراء تغييرات على البيانات، انقر فوق **حفظ** أو **إرسال** لحفظ تغييراتك. 

**حفظ التغييرات بالنقر على زر الحفظ** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_4.png)
## **الاستنتاج**
{{% alert color="primary" %}} 

عرض هذا المقال كيفية ربط ورقة عمل بمجموعة مخصصة تم إنشاؤها. باستخدام Aspose.Cells.GridWeb، يمكن للمطورين ربط أوراق العمل إما بقاعدة بيانات أو مجموعات مخصصة عبر مصمم أوراق العمل بواجهة رسومية أو من خلال البرمجة. هذا يوفر مجموعة واسعة من الخيارات للمطورين في إنشاء التطبيقات.

{{% /alert %}}
