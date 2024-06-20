---
title: إنشاء عرض ورقة هرمية
type: docs
weight: 30
url: /ar/net/aspose-cells-gridweb/create-hierarchical-view-sheet/
keywords: GridWeb، هرمي
description: يقدم هذا المقال كيفية إنشاء العرض الهرمي في GridWeb.
---

{{% alert color="primary" %}} 

ربط البيانات هو ميزة قوية وسهلة الاستخدام في GridWeb. يتم جلب البيانات المخزنة في جداول قاعدة البيانات في مجموعة بيانات وملؤها بالبيانات 

ممثلة الجداول البيانية. باستخدام ميزة ربط البيانات، يمكنك إنشاء عرض هرمي (عرض أب-ابن) للبيانات المترابطة و 

عرضها في التحكم لجعلها أكثر أناقة. 

تناقش هذه الموضوع إنشاء ورقة عرض هرمية. بعض الصفوف في الورقة لديها عروض فرعية. عندما ينقر المستخدم على الصف الموسع

button {{< emoticons/cross >}}, the child view table of that row is expanded down. This feature is very helpful for building a hierarchical view report. 

**جدول بعرض تسلسلي** 

![todo:image_alt_text](creating-hierarchical-view-sheet_1.png)

{{% /alert %}} 
## **إنشاء علاقات للجداول البيانية**
على سبيل المثال، تستخدم واجهة برمجة التطبيقات ADO.Net وتستخرج البيانات من جداول قاعدة البيانات. لإنشاء جدول بعرض تسلسلي، يجب عليك تصميم مجموعة بيانات

يستند إلى بعض الجداول وإنشاء علاقة بينها أولاً. استخدم مصمم الجداول التلقائية لإنشاء العلاقة. في هذا المثال، هناك ثلاثة جداول بيانات: العملاء، الطلبات، تفاصيل الطلب. يظهر الجدول جميع معلومات العملاء افتراضيًا. عندما 

يقوم المستخدم بتوسيع عميل، يظهر الشبكة جميع الطلبات التي قام بها هذا العميل. عندما يوسع المستخدم طلبًا، تظهر الشبكة التفاصيل 

لهذا الطلب. البيانات تسلسلية: يتم سرد تفاصيل الطلب تحت الطلبات، وتوجد الطلبات تحت العملاء. 

لكي يعمل هذا، يجب إنشاء العلاقات التالية بين جداول البيانات:

لكي يعمل هذا، يجب إنشاء العلاقات التالية بين جداول البيانات:

1. إنشاء مفتاح خارجي على جدول البيانات الخاص بالطلبات، حقل المفتاح هو معرف العميل 

![todo:image_alt_text](creating-hierarchical-view-sheet_2.png)




2. إنشاء مفتاح خارجي على جدول تفاصيل الطلب، حقل المفتاح هو معرف الطلب. 

![todo:image_alt_text](creating-hierarchical-view-sheet_3.png)



يبدو مصمم مجموعة البيانات الآن على النحو التالي: 

![todo:image_alt_text](creating-hierarchical-view-sheet_4.png)
### **ربط ورقة العمل**
استخدم الآن **مصمم ورق العمل** لتعيين مصدر البيانات والمشترك لورقة العمل، وضبط أعمدة ربط حقول البيانات. 

يضيف الضبط تلقائيًا أيقونة + لكل صف يتوافق مع سجل تعيينه (عمومًا كائن DataRowView) لديه 

عروض فرعية. عند النقر على الرمز +، يتم توسيع السجل لعرض العرض الفرعي. يستخدم المثال أدناه **مصمم ورق العمل** لربط 

ورقة العمل إلى جدول البيانات الرئيسي للعملاء. 

![todo:image_alt_text](creating-hierarchical-view-sheet_5.png)
### **تخصيص أعمدة ربط الجداول الفرعية**
يوفر الضبط حدثًا يسمى GridWeb.BindingChildView يستخدمه المطورون لتخصيص أعمدة ربط الجداول الفرعية. يحتاج هذا المثال 

إلى عرض حقل تفاصيل الطلبات **UnitPrice** بتنسيق العملة. أضف معالج حدث لتغيير تنسيق الرقم لعمود الربط. 

**C#**

{{< highlight csharp >}}

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

{{< highlight csharp >}}

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
كما هو موضح في [ربط ورقة البيانات بمجموعة البيانات باستخدام مصمم ورق الأعمال في GridWeb](/cells/ar/net/binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer/)
يجب عليك إضافة كود إلى كتلة Page_Load لتحميل البيانات إلى مجموعة البيانات من قاعدة بيانات، وربط مجموعة البيانات بالورقة في الخطوة التالية. 

الخطوة التالية. 

تمتلك فئة Asppose.Grid.Web.Data.WebWorksheet بعض الخصائص المفيدة.

- على سبيل المثال، يُستخدم خاصية EnableCreateBindColumnHeader لإنشاء عناوين العمود المرتبط ضمن الورقة، أو العمود الذي يعرض العناوين

يأخذ القيم **true** أو **false**. 

- تحدد الخصائص BindStartRow وBindStartColumn الموقع في الورقة لعنصر تحكم GridWeb التي يجب أن يتم ربط المصدر بها.
- تُستخدم خاصية EnableExpandChildView لتعطيل عرض الطفل الموسع للورقة. بشكل افتراضي، يتم تعيينها على true.

تمتلك الفئة أيضًا بعض الأساليب المفيدة. 

- تقوم الأسلوب DataBind() بربط ورقة بالمصدر.
- يضيف CreateNewBindRow() صفًا جديدًا ويربطه بمصدر البيانات.
- يقوم DeleteBindRow() بحذف صف مرتبط.
- يقوم الأسلوب SetRowExpand() بتعيين الصف الموسع وعرض محتوى العرض الفرعي في وضع ربط البيانات.
- يقوم الأسلوب GetRowExpand() بالحصول على قيمة بولية تشير إلى ما إذا كان الصف قد تم توسيعه أم لا.

في الكود أدناه، يتم ملء كائن مجموعة البيانات "dataSet21" بالبيانات بناءً على ثلاث جداول. يتم تصفية جدول العملاء لتكون 

أول جدول في العرض التسلسلي. يتم إنشاء كائن WebWorksheet يسمى "sheet"، والذي يُطهر الورقة أولاً ثم يعينها 

مرتبة إلى مصدر البيانات. 

**C#**

{{< highlight csharp >}}

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

        WebWorksheet sheet = GridWeb1.WorkSheets[0];

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

{{< highlight csharp >}}

 Private Sub Page_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

    'Put user code to initialize the page here

    If Not IsPostBack Then

        BindWithoutInSheetHeaders()

    End If

End Sub

Private Sub BindWithoutInSheetHeaders()

    Dim db As DemoDatabase2 = New DemoDatabase2()

    Dim path As String = MapPath(".")

    path = path.Substring(0, path.LastIndexOf("\"))

    path = path.Substring(0, path.LastIndexOf("\"))

    db.OleDbConnection1.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + path + "\Database\Northwind.mdb"

    Try

        ' Connects to database and fetches data.

        ' Customers Table.

        db.OleDbDataAdapter1.Fill(DataSet21)

        ' Orders Table.

        db.OleDbDataAdapter2.Fill(DataSet21)

        ' OrderDetailTable.

        db.OleDbDataAdapter3.Fill(DataSet21)

        ' Filter data

        DataSet21.Customers.DefaultView.RowFilter = "CustomerID<'BSAAA'"

        Dim sheet As WebWorksheet = GridWeb1.WorkSheets(0)

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
