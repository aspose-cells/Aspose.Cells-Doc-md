---
title: الترخيص
type: docs
weight: 120
url: /ar/net/licensing/
---
{{% alert color="primary" %}}

 يمكنك بسهولة تنزيل إصدار تقييم Aspose.Cells من موقعه[صفحة التحميل](https://www.nuget.org/packages/Aspose.Cells) @ NuGet الريبو. يوفر الإصدار التقييمي نفس الإمكانات تمامًا مثل الإصدار المرخص من المكون. علاوة على ذلك ، يصبح الإصدار التقييمي مرخصًا ببساطة عند شراء ترخيص وإضافة سطرين من التعليمات البرمجية لتطبيق الترخيص.

{{% /alert %}}

## **قيود إصدار التقييم**

يوفر الإصدار التقييمي لمنتج Aspose.Cells (بدون ترخيص محدد) وظائف المنتج الكاملة ، ولكنه يقتصر على فتح 100 ملف في برنامج واحد وورقة عمل إضافية مع علامة مائية للتقييم.

القيود موضحة أدناه:

- **عدد الملفات المفتوحة** (Aspose.Cells)
عند تشغيل برنامجك ، يمكنك فقط فتح 100 ملف Excel باستخدام مكتبة Aspose.Cells. إذا تجاوز التطبيق الخاص بك هذا الرقم ، فسيتم طرح استثناء.
- **إعدادات ملف التكوين** (Aspose.Cells.GridWeb)
 لا يمكنك إعادة تحديد مسار البرنامج النصي عن طريق إضافة سطور التعليمات البرمجية التالية في قسم التكوين (على سبيل المثال في ملف web.config). acw_client هو مجلد يحتوي على ملفات و Aspose.Cells.GridWeb يستخدم هذا المجلد لإدارة تكوينه الداخلي ، ويحتوي على ملفات نصية وملفات صور وملفات أخرى لتحديد سلوك GridWeb وتعيين عمليات أخرى. يتم استخدام ملف التكوين لمنع عنصر التحكم من استخدام موارد العميل المضمنة (الصور والبرامج النصية وما إلى ذلك) والتي تكون مفيدة في بعض الحالات / السيناريوهات. علاوة على ذلك ، فإن إعدادات التكوين هذه في ملف web.config ستصبح سارية فقط مع الإصدار المرخص من عنصر التحكم.

**XML**

{{< highlight "csharp" >}}

 <appSettings>

<add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

<add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>

{{< /highlight >}}

{{% alert color="primary" %}}

قد تكون هذه الإعدادات إلزامية في بعض الحالات / السيناريوهات إذا كنت تستخدم Aspose.Cells.GridWeb control في مواقع نظام الملفات أو ملحقات MS Ajax وما إلى ذلك.

{{% /alert %}}

علاوة على ذلك ، ستظهر ورقة العمل التي تحتوي على علامة مائية للتقييم دائمًا على أنها ورقة العمل النشطة في ملف Excel الذي تم إنشاؤه باستخدام مكتبة Aspose.Cells. فقط في الإصدار المرخص ، يمكنك تعيين ورقة العمل النشطة على أوراق عمل أخرى. في الإخراج PDF أو ملف الصورة بواسطة Aspose.Cells ، سيتم لصق علامة مائية للتقييم في أعلى المستند / الصورة. لا يمكنك إخفاء تحذير حقوق النشر للتقييم (ورقة العمل الإضافية) في عنصر تحكم GridWeb أيضًا ، ستتم إضافته دائمًا (في نهاية علامات تبويب ورقة العمل) في عنصر التحكم.

{{% alert color="primary" %}}

 إذا كنت ترغب في اختبار Aspose.Cells بدون قيود إصدار التقييم ، يمكنك أيضًا طلب ملف[ترخيص مؤقت لمدة 30 يومًا](https://purchase.aspose.com/temporary-license).

{{% /alert %}}

## **تطبيق ترخيص مكون Aspose.Cells**

الترخيص عبارة عن ملف XML نص عادي يحتوي على تفاصيل مثل اسم المنتج وعدد المطورين المرخص لهم وتاريخ انتهاء الاشتراك وما إلى ذلك. الملف موقّع رقميًا ، لذا لا تعدّل الملف. حتى الإضافة غير المقصودة لفاصل سطر إضافي في الملف سوف يبطل ذلك. تحتاج إلى تعيين ترخيص قبل استخدام Aspose.Cells إذا كنت تريد تجنب قيود التقييم الخاصة به. مطلوب فقط تعيين ترخيص مرة واحدة لكل تطبيق (أو عملية). يمكن تحميل الترخيص من ملف أو دفق أو مورد مضمن.

Aspose.Cells يحاول العثور على الترخيص في المواقع التالية:

- مسار صريح
- المجلد الذي يحتوي على Aspose.Cells.dll
- المجلد الذي يحتوي على التجميع الذي يسمى Aspose.Cells.dll
- المجلد الذي يحتوي على تجميع الإدخال (الخاص بك. exe)
- مورد مضمن في التجميع يسمى Aspose.Cells.dll

هناك طريقتان شائعتان لتطبيق ترخيص ، من ملف أو دفق ، أو كمورد مضمن.

### **تطبيق ترخيص من القرص أو الدفق**

أسهل طريقة لتعيين ترخيص ، هي وضع ملف الترخيص في نفس المجلد مثل Aspose.Cells.dll وتحديد اسم الملف فقط بدون مساره.

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license file through its path

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

 عند استدعاء طريقة SetLicense ، يجب أن يكون اسم الترخيص هو نفسه اسم ملف الترخيص الخاص بك. على سبيل المثال ، يمكنك تغيير اسم ملف الترخيص إلى**Aspose.Cells.lic.xml**. ثم في التعليمات البرمجية الخاصة بك ، يجب عليك استخدام اسم الترخيص المعدل (**Aspose.Cells.lic.xml**) لطريقة SetLicense.

{{% /alert %}}

من الممكن أيضًا تحميل ترخيص من دفق.

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license through a stream

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **طلب ترخيص مقنن**

Aspose.Cells يسمح للمطورين بتطبيق المفتاح المقنن. إنها آلية ترخيص جديدة. سيتم استخدام آلية الترخيص الجديدة جنبًا إلى جنب مع طريقة الترخيص الحالية. يمكن للعملاء الذين يريدون أن تتم محاسبتهم بناءً على استخدام ميزات API استخدام الترخيص المقنن. لمزيد من التفاصيل ، يرجى الرجوع إلى[الأسئلة الشائعة حول الترخيص المقنن](https://purchase.aspose.com/faqs/licensing/metered)الجزء.

فئة جديدة[مقننة](https://reference.aspose.com/cells/net/aspose.cells/metered)تم تقديمه لتطبيق المفتاح المقنن. فيما يلي نموذج التعليمات البرمجية الذي يوضح كيفية تعيين المفتاح العام والخاص الذي تم قياسه.

{{< highlight "csharp" >}}

 //Set metered public and private keys

Metered metered = new Metered();

//Access the setMeteredKey property and pass public and private keys as parameters

metered.SetMeteredKey("*************", "*************");

//Instantiate a new Workbook

Workbook workbook = new Workbook();

//Check if the license is set

Console.WriteLine(workbook.IsLicensed);

//Get the Consumption quantity

decimal amountBefore = Metered.GetConsumptionQuantity();

Console.WriteLine(amountBefore);

Workbook workbook2 = new Workbook("e:\\test2\\Book1.xlsx");

workbook2.Save("e:\\test2\\out1.xlsx");

//Since uploading data is already running on another thread, so you might need to wait for some time (optional)

System.Threading.Thread.Sleep(10000);

//Get the Consumption quantity again which should be greater a bit

decimal amountAfter = Metered.GetConsumptionQuantity();

Console.WriteLine(amountAfter);

{{< /highlight >}}

### **استخدام مورد مضمن**

هناك طريقة أخرى رائعة لتعبئة الترخيص مع التطبيق الخاص بك والتأكد من عدم فقده ، وهي تضمينه كمورد مضمن في أحد التجميعات التي تستدعي Aspose.Cells. لتضمين ملف الترخيص كمورد مضمن ، قم بتنفيذ الخطوات التالية :

1.  في Visual Studio .NET ، قم بتضمين ملف الترخيص (.lic) في المشروع عن طريق التحديد**إضافة عنصر موجود** من**ملف** قائمة.
1. حدد الملف في مستكشف الحلول واضبط**بناء العمل** إلى**الموارد المضمنة** في نافذة الخصائص

 للوصول إلى الترخيص المضمن في التجميع (كمورد مضمن) ، لا يلزم استدعاء أساليب GetExecutingAssembly و GetManifestResourceStream لفئة System.Reflection.Assembly لـ Microsoft .NET Framework. كل ما عليك فعله هو إضافة ملف الترخيص كمورد مضمن إلى مشروعك وتمرير اسم ملف الترخيص إلى طريقة SetLicense. ال**Aspose.Cells.License** سيجد الفصل تلقائيًا ملف الترخيص في الموارد المضمنة. يرجى مراجعة المثال الوارد أدناه لفهم طريقة تعيين الترخيص (المضمنة) في تطبيقاتك.

{{< highlight "csharp" >}}

 //Instantiate the License class

Aspose.Cells.License license = new Aspose.Cells.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **تحديد الترخيص في Aspose.Cells Grid Controls**

في Aspose.Cells Grid Suite ، يمكن تحميل الترخيص من ملف أو دفق أو مصدر مضمن. Aspose.Cells.GridDesktop / Aspose.Cells. يحاول GridWeb البحث عن الترخيص في المواقع التالية:

1. مسار صريح
1. المجلد الذي يحتوي على ملف dll الخاص بالمكون (مضمن في Aspose.Cells.GridDesktop أو Aspose.Cells.GridWeb)
1. المجلد الذي يحتوي على التجميع الذي يسمى dll للمكون (مضمن في Aspose.Cells.GridDesktop أو Aspose.Cells.GridWeb)
1. المجلد الذي يحتوي على تجميع الإدخال (الخاص بك. exe)
1. مورد مضمن في التجميع يسمى dll للمكون (مضمن في Aspose.Cells.GridDesktop أو Aspose.Cells.GridWeb)

{{% alert color="primary" %}}

إذا كنت تستخدم Aspose.Cells.GridDesktop control ، فسيتم استخدام فئة الترخيص كـ Aspose.Cells.GridDesktop.License ولكن إذا كنت تستخدم Aspose.Cells.GridWeb control فسيتم استخدام Aspose.Cells.GridWeb.License لتعيين الترخيص.

{{% /alert %}}

### **تطبيق ترخيص من القرص أو الدفق**

أسهل طريقة لتعيين ترخيص ، هي وضع ملف الترخيص في نفس المجلد مثل ملف dll الخاص بالمكون (مضمن في Aspose.Cells.GridWeb) وتحديد اسم الملف فقط بدون مساره.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense("MyLicense.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

عند استدعاء طريقة SetLicense ، يجب أن يكون اسم الترخيص هو نفسه اسم ملف الترخيص الخاص بك. على سبيل المثال ، يمكنك تغيير اسم ملف الترخيص إلى "MyLicense.lic.xml". ثم في التعليمات البرمجية الخاصة بك ، يجب عليك استخدام اسم الترخيص المعدل (أي MyLicense.lic.xml) لطريقة SetLicense.

{{% /alert %}}

من الممكن أيضًا تحميل ترخيص من دفق.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license through a stream

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **تطبيق ترخيص كمورد مضمن**

هناك طريقة أخرى رائعة لتعبئة الترخيص مع التطبيق الخاص بك والتأكد من عدم فقده ، وهي تضمينه كمورد مضمن في إحدى التجميعات التي تستدعي dll للمكون (مضمن في Aspose.Cells.GridDesktop). لتضمين ملف الترخيص كمورد مضمن ، قم بتنفيذ الخطوات التالية:

1.  في Visual Studio .NET ، قم بتضمين ملف الترخيص (.lic) في المشروع باستخدام امتداد**إضافة عنصر موجود** الخيار على**ملف** قائمة.
1. حدد الملف في مستكشف الحلول واضبط إنشاء إجراء على الموارد المضمنة في نافذة الخصائص.
1. للوصول إلى الترخيص المضمن في التجميع (كمورد مضمن) ، لا يلزم استدعاء أساليب GetExecutingAssembly و GetManifestResourceStream لفئة System.Reflection.Assembly لـ Microsoft .NET Framework. بدلاً من ذلك ، أضف ملف الترخيص كمورد مضمن في الخاص بك المشروع وتمرير اسم ملف الترخيص إلى طريقة SetLicense. تبحث فئة الترخيص تلقائيًا عن ملف الترخيص في الموارد المضمنة.

يرجى مراجعة المثال الوارد أدناه لفهم هذه الطريقة لتطبيق الترخيص كمورد مضمن لتطبيقاتك.

{{< highlight "csharp" >}}

 //Instantiate the License class

Aspose.Cells.GridDesktop.License license = new Aspose.Cells.GridDesktop.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Total.lic");

{{< /highlight >}}

## **جاري تطبيق ترخيص في Aspose.Cells.GridDesktop لتطبيق WinForm**

يوصى بوضع رمز الترخيص الخاص بك قبل أن يبدأ تطبيقك وتطبيقه مرة واحدة فقط. على سبيل المثال ، بالنسبة لتطبيق windows C# ، ضع كود الترخيص في الطريقة الرئيسية.

{{< highlight "csharp" >}}

public class Form1 : System.Windows.Forms.Form

{

private Aspose.Cells.GridDesktop.GridDesktop gridDesktop1;

/// <summary>

/// Required designer variable.

/// </summary>

private System.ComponentModel.Container components = null;

public Form1()

{

//

// Required for Windows Form Designer support

//

InitializeComponent();

//

// TODO: Add any constructor code after InitializeComponent call

//

}

/// The main entry point for the application.

/// </summary>

.

.

.

.

[STAThread]

static void Main()

{

Aspose.Cells.GridDesktop.License lic = new Aspose.Cells.GridDesktop.License();

//Use this line if you are using an explicit path for the license file.

lic.SetLicense(@"C:\MyLicense.lic");

//Or use the line below if you are using the license file as an embedded resource.

//lic.SetLicense("MyLicense.lic");

Application.Run(new Form1());

}

private void Form1_Load(object sender, System.EventArgs e)

{

Aspose.Cells.GridDesktop.Worksheet sheet = this.gridDesktop1.Worksheets.Add("MySheet");

sheet.Cells["A1"].SetCellValue("Hello");

gridDesktop1.ActiveSheetIndex = 1;

}

}

{{< /highlight >}}

## **ملاحظات حول تطبيق ترخيص في Aspose.Cells.GridWeb**

يوصى بوضع رمز الترخيص في Global.asax.cs لتطبيق الويب الخاص بك (يُفترض أن يتم وضع ملف الترخيص هذا على محرك الأقراص "d: \"):

{{< highlight "csharp" >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(@"d:\Aspose.Cells.GridWeb.lic.xml");

}

{{< /highlight >}}

تحميل ترخيص من دفق

{{< highlight "csharp" >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(myStream);

}

{{< /highlight >}}
