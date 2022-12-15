---
title: إنشاء ورقة عرض هرمية
type: docs
weight: 30
url: /ar/net/creating-hierarchical-view-sheet/
---
{{% alert color="primary" %}} 

 يعد ربط البيانات ميزة GridWeb قوية وسهلة الاستخدام. يتم جلب البيانات المخزنة في جداول قاعدة البيانات إلى DataSet وتعبئتها بالبيانات

 تمثل جداول البيانات. باستخدام ميزة ربط البيانات ، يمكنك إنشاء عرض هرمي (عرض رئيسي-فرعي) للبيانات المترابطة و

 اعرضه في عنصر التحكم لجعله أكثر أناقة.

 يناقش هذا الموضوع إنشاء ورقة عرض هرمية. تحتوي بعض الصفوف في الورقة على طرق عرض فرعية. عندما ينقر المستخدم على الصفوف**وسعت**

 زر{{< emoticons/cross >}} ، يتم توسيع جدول العرض الفرعي لهذا الصف لأسفل. هذه الميزة مفيدة جدًا لإنشاء تقرير عرض هرمي.

**جدول مع عرض هرمي** 

![ما يجب القيام به: image_بديل_نص](creating-hierarchical-view-sheet_1.png)

{{% /alert %}} 
## **قم بإنشاء علاقات لـ DataTables**
على سبيل المثال ، يمكنك استخدام ADO.Net API واستخراج البيانات من جداول قاعدة البيانات. لإنشاء ورقة عرض هرمية ، يجب عليك تصميم DataSet

 بناء على بعض الجداول وإنشاء علاقة بينها أولاً. استخدم VS.NET's**مصمم مجموعة البيانات** لخلق العلاقة. في

 في هذا المثال ، هناك ثلاثة جداول بيانات: العملاء ، الطلبات ، تفاصيل الطلب. تعرض الورقة جميع معلومات العميل بشكل افتراضي. متي

 يقوم المستخدم بتوسيع العميل ، تعرض الشبكة جميع الطلبات التي وضعها العميل. عندما يقوم المستخدم بتوسيع طلب ، تعرض الشبكة التفاصيل

من هذا الترتيب. البيانات هرمية: تفاصيل الطلب مدرجة ضمن الطلبات ، والأوامر مدرجة ضمن العملاء.

لكي يعمل هذا ، يجب إنشاء العلاقات التالية بين جداول البيانات:

1.  قم بإنشاء مفتاح خارجي في طلبات DataTable ، حقل المفتاح هو CustomerID

![ما يجب القيام به: image_بديل_نص](creating-hierarchical-view-sheet_2.png)




1. إنشاء مفتاح خارجي في DataTable Order Details ، حقل المفتاح هو OrderID.

![ما يجب القيام به: image_بديل_نص](creating-hierarchical-view-sheet_3.png)



 يبدو مصمم DataSet الآن كما يلي:

![ما يجب القيام به: image_بديل_نص](creating-hierarchical-view-sheet_4.png)
### **ربط ورقة العمل**
 الآن استخدم ملف**مصمم أوراق العمل** لتعيين مصدر البيانات وعضو البيانات لورقة العمل ، وتكوين أعمدة ربط حقل البيانات.

 يضيف عنصر التحكم تلقائيًا رمز + لكل صف يتوافق مع سجل يحتوي كائن ربطه (بشكل عام كائن DataRowView)

 آراء الأطفال. عند النقر فوق الرمز + ، يتم توسيع السجل لإظهار طريقة العرض الفرعية. يستخدم المثال أدناه ملف**مصمم أوراق العمل** لربط

 ورقة عمل لجذر عملاء DataTable.

![ما يجب القيام به: image_بديل_نص](creating-hierarchical-view-sheet_5.png)
### **تخصيص الجداول الفرعية ربط الأعمدة**
 يوفر عنصر التحكم حدثًا يسمى GridWeb.BindingChildView يستخدمه المطورون لتخصيص أعمدة ربط الجداول التابعة. هذا المثال

 يحتاج إلى عرض تفاصيل الطلب "**سعر الوحدة** في شكل عملة. أضف معالج حدث لتغيير تنسيق رقم عمود الربط.

**C#**

{{< highlight "csharp" >}}

 // Handles the BindingChildView event to set the UnitPrice column.

private void GridWeb1_BindingChildView(Aspose.Cells.GridWeb.GridWeb childGrid, Aspose.Cells.GridWeb.Data.WebWorksheet childSheet)

{

    DataView view = (DataView)childSheet.DataSource;

    if (view.Table.TableName == "Order Details")

    {

        childSheet.BindColumns["UnitPrice"].NumberType = NumberType.Currency3;

    }

}



{{< /highlight >}}

**VB.NET**

{{< highlight "csharp" >}}

 'Handles the BindingChildView event to set the UnitPrice column.

Private Sub GridWeb1_BindingChildView(ByVal childGrid As Aspose.Cells.GridWeb.GridWeb, ByVal childSheet As 

Aspose.Cells.GridWeb.Data.WebWorksheet) Handles GridWeb1.BindingChildView

    Dim view As DataView = CType(childSheet.DataSource, DataView)

    If view.Table.TableName = "Order Details" Then

        childSheet.BindColumns("UnitPrice").NumberType = NumberType.Currency3

    End If

End Sub



{{< /highlight >}}
### **تحميل البيانات من قاعدة البيانات والربط**
كما هو موضح في[ورقة عمل ملزمة لمجموعة بيانات باستخدام مصمم أوراق عمل GridWeb](/cells/ar/net/binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer/),
 تحتاج إلى إضافة رمز إلى كتلة Page_Load لتحميل البيانات إلى DataSet من قاعدة بيانات ، وربط DataSet بالورقة في

 الخطوة التالية.

تحتوي فئة Asppose.Grid.Web.Data.WebWorksheet على بعض الخصائص المفيدة.

- على سبيل المثال ، يتم استخدام الخاصية EnableCreateBindColumnHeader لإنشاء عناوين العمود المرتبط داخل الورقة أو العمود

 الرؤوس يعرض أسماء الأعمدة المرتبطة. يأخذ القيم**حقيقي** أو**خاطئة**. 

- تحدد الخصائص BindStartRow و BindStartColumn الموضع في ورقة تحكم GridWeb التي يجب أن يرتبط المصدر بها.
- يتم استخدام الخاصية EnableExpandChildView لتعطيل العرض الفرعي الموسع لورقة العمل. بشكل افتراضي يتم تعيينه على صحيح.

 الفصل لديه بعض الأساليب المفيدة أيضًا.

- تقوم طريقة DataBind () بربط الورقة بالمصدر.
- يضيف CreateNewBindRow () صفًا جديدًا ويربطه بمصدر البيانات.
- يقوم DeleteBindRow () بحذف صف منضم.
- يعين الأسلوب SetRowExpand () الصف الموسع ويظهر محتوى العرض الفرعي في وضع ربط البيانات.
- يحصل أسلوب GetRowExpand () على قيمة منطقية تشير إلى ما إذا كان الصف قد تم توسيعه أم لا.

 في التعليمات البرمجية أدناه ، يتم تعبئة كائن DataSet "dataSet21" ببيانات تستند إلى ثلاثة جداول. يتم تصفية جدول العملاء لجعله

 الجدول الأول في العرض الهرمي. يتم إنشاء كائن WebWorksheet المسمى "الورقة" ، والذي يمسح الورقة أولاً ثم يعينها

 مرتبطة بمصدر البيانات.

**C#**

{{< highlight "csharp" >}}

 private void Page_Load(object sender, System.EventArgs e)

{

    // Put user code to initialize the page here

    if (!IsPostBack)

    {

        BindWithoutInSheetHeaders();

    }

}

private void BindWithoutInSheetHeaders()

{

    DemoDatabase2 db = new DemoDatabase2();

    string path = MapPath(".");

    path = path.Substring(0, path.LastIndexOf("\\"));

    path = path.Substring(0, path.LastIndexOf("\\"));

    db.oleDbConnection1.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + path + "\\Database\\Northwind.mdb";

    try

    {

        // Connects to database and fetches data.

        // Customers Table.

        db.oleDbDataAdapter1.Fill(dataSet21);

        // Orders Table.

        db.oleDbDataAdapter2.Fill(dataSet21);

        // OrderDetailTable.

        db.oleDbDataAdapter3.Fill(dataSet21);

        // Filter data

        dataSet21.Customers.DefaultView.RowFilter = "CustomerID<'BSAAA'";

        WebWorksheet sheet = GridWeb1.WebWorksheets[0];

        // Clears the sheet.

        sheet.Cells.Clear();

        // Disables creating in-sheet headers.

        sheet.EnableCreateBindColumnHeader = false;

        // Data cells begin from row 0.

        sheet.BindStartRow = 0;

        // Bind the sheet to the dataset.

        sheet.DataBind();

    }

    finally

    {

        db.oleDbConnection1.Close();

    }

}



{{< /highlight >}}

**VB.NET**

{{< highlight "csharp" >}}

 تحميل الصفحة الفرعية الخاصة (المرسل ByVal كـ System.Object ، ByVal e As System.EventArgs) يعالج MyBase.Load

 ضع رمز المستخدم لتهيئة الصفحة هنا

 إذا لم يكن الأمر كذلك ، فقم بإعادة الإرسال

 BindWithoutInSheetHeaders ()

 إنهاء إذا

End Sub

BindWithoutInSheetHeaders الخاص ()

 Dim db As DemoDatabase2 = New DemoDatabase2 ()

مسار خافت كسلسلة = MapPath (".")

 المسار = path.Substring (0، path.LastIndexOf ("\"))

 المسار = path.Substring (0، path.LastIndexOf ("\"))

 db.OleDbConnection1.ConnectionString = "الموفر = Microsoft.Jet.OLEDB.4.0 ؛ مصدر البيانات =" + المسار + "\ Database \ Northwind.mdb"

 محاولة

 يتصل بقاعدة البيانات ويجلب البيانات.

 جدول العملاء.

 db.OleDbDataAdapter1.Fill (DataSet21)

 جدول الطلبات.

 db.OleDbDataAdapter2.Fill (DataSet21)

 OrderDetailTable.

 db.OleDbDataAdapter3.Fill (DataSet21)

 تصفية البيانات

 DataSet21.Customers.DefaultView.RowFilter = "معرف العميل<'BSAAA'"

        Dim sheet As WebWorksheet = GridWeb1.WebWorksheets(0)

        ' Clears the sheet.

        sheet.Cells.Clear()

        ' Disables creating in-sheet headers.

        sheet.EnableCreateBindColumnHeader = False

        ' Data cells begin from row 0.

        sheet.BindStartRow = 0

        ' Bind the sheet to the dataset.

        sheet.DataBind()

    Finally

        db.OleDbConnection1.Close()

    End Try

End Sub



{{< /highlight >}}
