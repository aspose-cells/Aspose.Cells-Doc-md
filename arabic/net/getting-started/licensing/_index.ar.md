---
title: Licensing
type: docs
weight: 120
url: /ar/net/licensing/
description: Aspose.Cells for .NET يوفر خططًا مختلفة للشراء أو يقدم نسخة تجريبية مجانية وترخيصًا مؤقتًا لمدة 30 يومًا للتقييم باستخدام Licensing وسياسات الاشتراك في C#.
keywords: Apply License from Disk or Stream. Set License from Disk or Stream. Apply License in Aspose.Cells.
---
{{% alert color="primary" %}}

 يمكنك بسهولة تنزيل نسخة تقييمية من Aspose.Cells من موقعه[صفحة التحميل](https://www.nuget.org/packages/Aspose.Cells) @ NuGet ريبو. يوفر الإصدار التقييمي نفس الإمكانيات تمامًا مثل الإصدار المرخص للمكون. علاوة على ذلك، يصبح الإصدار التقييمي مرخصًا ببساطة عند شراء ترخيص وإضافة سطرين من التعليمات البرمجية لتطبيق الترخيص.

{{% /alert %}}

##  **قيود إصدار التقييم**

يوفر الإصدار التقييمي للمنتج Aspose.Cells (بدون ترخيص محدد) وظائف المنتج الكاملة، ولكنه يقتصر على فتح 100 ملف في برنامج واحد وورقة عمل إضافية مع علامة مائية للتقييم.

القيود مبينة أدناه:

- **عدد الملفات المفتوحة** (Aspose.Cells)
 عند تشغيل البرنامج الخاص بك، يمكنك فقط فتح 100 ملف Excel باستخدام مكتبة Aspose.Cells. إذا تجاوز طلبك هذا الرقم، فسيتم طرح استثناء.
- **إعدادات ملف التكوين**(Aspose.Cells.GridWeb)
 لا يمكنك إعادة تحديد مسار البرنامج النصي عن طريق إضافة أسطر التعليمات البرمجية التالية إلى قسم التكوين (على سبيل المثال، في ملف web.config). acw_client هو مجلد يحتوي على ملفات وAspose.Cells.GridWeb يستخدم هذا المجلد لإدارة تكوينه الداخلي، ويحتوي على ملفات نصية وملفات صور وملفات أخرى لتحديد سلوك GridWeb وتعيين عمليات أخرى. يتم استخدام ملف التكوين لمنع عنصر التحكم من استخدام موارد العميل المضمنة (الصور والبرامج النصية وما إلى ذلك) وهو أمر مفيد في بعض الحالات/السيناريوهات. علاوة على ذلك، لن تصبح إعدادات التكوين هذه في ملف web.config سارية المفعول إلا مع الإصدار المرخص لعنصر التحكم.

**XML**

{{< highlight "csharp" >}}

 <appSettings>

<add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

<add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>

{{< /highlight >}}

{{% alert color="primary" %}}

قد تكون هذه الإعدادات إلزامية في بعض الحالات/السيناريوهات إذا كنت تستخدم Aspose.Cells.GridWeb للتحكم في مواقع نظام الملفات أو ملحقات MS Ajax وما إلى ذلك.

{{% /alert %}}

علاوة على ذلك، ستظهر دائمًا ورقة العمل ذات العلامة المائية للتقييم كورقة العمل النشطة في ملف Excel الذي تم إنشاؤه باستخدام مكتبة Aspose.Cells. فقط في الإصدار المرخص، يمكنك تعيين ورقة العمل النشطة إلى أوراق عمل أخرى. في الإخراج PDF أو ملف الصورة بحلول Aspose.Cells، سيتم لصق علامة مائية للتقييم في الجزء العلوي من المستند/الصورة. ولا يمكنك إخفاء تحذير حقوق الطبع والنشر للتقييم (ورقة العمل الإضافية) في عنصر تحكم GridWeb أيضًا، وستتم إضافته دائمًا (في النهاية في علامات تبويب ورقة العمل) في عنصر التحكم.

{{% alert color="primary" %}}

 إذا كنت ترغب في اختبار Aspose.Cells دون قيود الإصدار التقييمي، فيمكنك أيضًا طلب[ترخيص مؤقت لمدة 30 يومًا](https://purchase.aspose.com/temporary-license).

{{% /alert %}}

##  **كيفية تقديم طلب ترخيص في مكون Aspose.Cells**

الترخيص عبارة عن ملف XML نصي عادي يحتوي على تفاصيل مثل اسم المنتج وعدد المطورين المرخص لهم وتاريخ انتهاء صلاحية الاشتراك وما إلى ذلك. الملف موقع رقميًا، لذا لا تقم بتعديل الملف. حتى الإضافة غير المقصودة لفاصل أسطر إضافي في الملف ستؤدي إلى إبطاله. تحتاج إلى تعيين ترخيص قبل استخدام Aspose.Cells إذا كنت تريد تجنب قيود التقييم الخاصة به. مطلوب فقط تعيين ترخيص مرة واحدة لكل تطبيق (أو عملية). يمكن تحميل الترخيص من ملف أو دفق أو مورد مضمن.

Aspose.Cells يحاول العثور على الترخيص في المواقع التالية:

- المسار الصريح
- المجلد الذي يحتوي على Aspose.Cells.dll
- المجلد الذي يحتوي على التجميع الذي يسمى Aspose.Cells.dll
- المجلد الذي يحتوي على مجموعة الإدخال (ملف exe.)
- مورد مضمن في التجميع يسمى Aspose.Cells.dll

هناك طريقتان شائعتان لتطبيق الترخيص، من ملف أو دفق، أو كمورد مضمن.

###  **كيفية تطبيق ترخيص من القرص أو الدفق**

أسهل طريقة لتعيين ترخيص هي وضع ملف الترخيص في نفس المجلد مثل ملف Aspose.Cells.dll وتحديد اسم الملف فقط بدون مساره.

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license file through its path

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

عند استدعاء الأسلوب SetLicense، يجب أن يكون اسم الترخيص هو نفس اسم ملف الترخيص الخاص بك. على سبيل المثال، يمكنك تغيير اسم ملف الترخيص إلى *Aspose.Cells.lic.xml**. ثم في التعليمات البرمجية الخاصة بك، يجب عليك استخدام اسم الترخيص المعدل (**Aspose.Cells.lic.xml**) لأسلوب SetLicense.

{{% /alert %}}

من الممكن أيضًا تحميل ترخيص من الدفق.

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license through a stream

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense(myStream);

{{< /highlight >}}

###  **كيفية تطبيق الترخيص المقنن**

Aspose.Cells يسمح للمطورين بتطبيق المفتاح المقنن. إنها آلية ترخيص جديدة. وسيتم استخدام آلية الترخيص الجديدة إلى جانب طريقة الترخيص الحالية. يمكن لهؤلاء العملاء الذين يريدون أن تتم محاسبتهم على أساس استخدام ميزات API استخدام الترخيص المقنن. لمزيد من التفاصيل، يرجى الرجوع إلى[عداد Licensing الأسئلة الشائعة](https://purchase.aspose.com/faqs/licensing/metered)قسم.

فئة جديدة[مقننة](https://reference.aspose.com/cells/net/aspose.cells/metered)تم تقديمه لتطبيق المفتاح المقنن. فيما يلي نموذج التعليمات البرمجية الذي يوضح كيفية تعيين المفتاح العام والخاص.

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

###  **كيفية استخدام الموارد المضمنة**

هناك طريقة أخرى أنيقة لتعبئة الترخيص مع التطبيق الخاص بك والتأكد من عدم فقدانه، وهي تضمينه كمورد مضمن في إحدى التجميعات التي تستدعي Aspose.Cells. لتضمين ملف الترخيص كمورد مضمن، قم بتنفيذ الخطوات التالية :

1.  في Visual Studio .NET، قم بتضمين ملف الترخيص (.lic) في المشروع عن طريق التحديد**إضافة عنصر موجود** من**ملف** قائمة طعام.
1.  حدد الملف في Solution Explorer وقم بتعيينه**بناء العمل** ل**الموارد المضمنة** في نافذة الخصائص

للوصول إلى الترخيص المضمن في التجميع (كمورد مضمن)، ليس من الضروري استدعاء أساليب GetExecutingAssembly وGetManifestResourceStream لفئة System.Reflection.Assembly من Microsoft .NET Framework. كل ما عليك فعله هو إضافة ملف الترخيص كمورد مضمن إلى مشروعك وتمرير اسم ملف الترخيص إلى طريقة SetLicense. ال**Aspose.Cells.License** سيجد الفصل تلقائيًا ملف الترخيص في الموارد المضمنة. يرجى مراجعة المثال الموضح أدناه لفهم طريقة تعيين الترخيص (المضمن) في تطبيقاتك.

{{< highlight "csharp" >}}

 //Instantiate the License class

Aspose.Cells.License license = new Aspose.Cells.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

##  **كيفية تعيين الترخيص في Aspose.Cells ضوابط الشبكة**

في Aspose.Cells Grid Suite، يمكن تحميل الترخيص من ملف أو دفق أو مورد مضمن. Aspose.Cells.GridDesktop / Aspose.Cells.GridWeb يحاول العثور على الترخيص في المواقع التالية:

1. المسار الصريح
1. المجلد الذي يحتوي على ملف dll للمكون (المضمن في Aspose.Cells.GridDesktop أو Aspose.Cells.GridWeb)
1. المجلد الذي يحتوي على التجميع الذي يسمى ملف dll للمكون (المضمن في Aspose.Cells.GridDesktop أو Aspose.Cells.GridWeb)
1. المجلد الذي يحتوي على مجموعة الإدخال (ملف exe.)
1. مورد مضمن في التجميع يسمى ملف dll للمكون (مضمن في Aspose.Cells.GridDesktop أو Aspose.Cells.GridWeb)

{{% alert color="primary" %}}

إذا كنت تستخدم عنصر التحكم Aspose.Cells.GridDesktop، فسيتم استخدام فئة الترخيص كـ Aspose.Cells.GridDesktop.License ولكن إذا كنت تستخدم عنصر التحكم Aspose.Cells.GridWeb، فسيتم استخدام فئة الترخيص Aspose.Cells.GridWeb.License لتعيين الترخيص.

{{% /alert %}}

###  **كيفية تطبيق ترخيص من القرص أو الدفق**

أسهل طريقة لتعيين ترخيص هي وضع ملف الترخيص في نفس المجلد مثل ملف dll الخاص بالمكون (المضمن في Aspose.Cells.GridWeb) وتحديد اسم الملف فقط دون مساره.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense("MyLicense.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

عند استدعاء أسلوب SetLicense، يجب أن يكون اسم الترخيص هو نفس اسم ملف الترخيص الخاص بك. على سبيل المثال، يمكنك تغيير اسم ملف الترخيص إلى "MyLicense.lic.xml". بعد ذلك، في التعليمات البرمجية الخاصة بك، يجب عليك استخدام اسم الترخيص المعدل (أي MyLicense.lic.xml) لأسلوب SetLicense.

{{% /alert %}}

من الممكن أيضًا تحميل ترخيص من الدفق.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license through a stream

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense(myStream);

{{< /highlight >}}

###  **كيفية تطبيق الترخيص كمورد مضمن**

هناك طريقة أخرى أنيقة لتعبئة الترخيص مع تطبيقك والتأكد من عدم فقدانه، وهي تضمينه كمورد مضمن في إحدى التجميعات التي تستدعي ملف dll الخاص بالمكون (المضمن في Aspose.Cells.GridDesktop). لتضمين ملف الترخيص كمورد مضمن، قم بتنفيذ الخطوات التالية:

1.  في Visual Studio .NET، قم بتضمين ملف الترخيص (.lic) في المشروع باستخدام الملف**إضافة عنصر موجود** الخيار على**ملف** قائمة طعام.
1. حدد الملف في Solution Explorer وقم بتعيين Build Action على Embedded Resource في نافذة الخصائص.
1. للوصول إلى الترخيص المضمن في التجميع (كمورد مضمن)، ليس من الضروري استدعاء أساليب GetExecutingAssembly وGetManifestResourceStream للفئة System.Reflection.Assembly من Microsoft .NET Framework. بدلاً من ذلك، قم بإضافة ملف الترخيص كمورد مضمن في المشروع وتمرير اسم ملف الترخيص إلى أسلوب SetLicense. تقوم فئة الترخيص تلقائيًا بالعثور على ملف الترخيص في الموارد المضمنة.

يرجى مراجعة المثال الموضح أدناه لفهم هذه الطريقة لتطبيق الترخيص كمورد مضمن لتطبيقاتك.

{{< highlight "csharp" >}}

 //Instantiate the License class

Aspose.Cells.GridDesktop.License license = new Aspose.Cells.GridDesktop.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Total.lic");

{{< /highlight >}}

##  **كيفية تطبيق ترخيص في Aspose.Cells.GridDesktop لتطبيق WinForm**

يوصى بوضع رمز الترخيص الخاص بك قبل بدء تشغيل التطبيق الخاص بك وتطبيقه مرة واحدة فقط. على سبيل المثال، بالنسبة لتطبيق Windows C#، ضع رمز الترخيص في الطريقة الرئيسية.

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

##  **ملاحظات حول تطبيق الترخيص في Aspose.Cells.GridWeb**

من المستحسن وضع رمز الترخيص في Global.asax.cs لتطبيق الويب الخاص بك (من المفترض أن يتم وضع ملف الترخيص هذا على محرك الأقراص " d:\ "):

{{< highlight "csharp" >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(@"d:\Aspose.Cells.GridWeb.lic.xml");

}

{{< /highlight >}}

تحميل ترخيص من الدفق

{{< highlight "csharp" >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(myStream);

}

{{< /highlight >}}
