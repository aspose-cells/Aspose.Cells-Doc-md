---
title: ترخيص
type: docs
weight: 120
url: /ar/net/licensing/
description: توفر Aspose.Cells for .NET خططًا مختلفة للشراء أو تقدم تجربة مجانية وترخيصًا مؤقتًا لمدة 30 يومًا للتقييم باستخدام سياسات الترخيص والاشتراك في C#.
keywords: C# تطبيق الترخيص من القرص أو التيار. C# ضبط الترخيص من القرص أو التيار. تطبيق الترخيص في Aspose.Cells for NET.
---

## **كيفية تطبيق ترخيص في مكون Aspose.Cells**

الترخيص هو ملف XML نصي عادي يحتوي على تفاصيل مثل اسم المنتج، عدد المطورين المرخص لهم، تاريخ انتهاء الاشتراك وما إلى ذلك. يتم توقيع الملف رقميًا، لذا لا تقم بتعديل الملف. حتى إضافة عرضية لسطر إضافي إلى الملف ستجعله غير صالح. يجب عليك تعيين ترخيص قبل استخدام Aspose.Cells إذا كنت ترغب في تجنب القيود التقييمية. لا يلزم سوى تعيين ترخيص مرة واحدة لكل تطبيق (أو عملية). يمكن تحميل الترخيص من ملف أو تيار، أو كمورد مضمن.

تحاول Aspose.Cells العثور على الترخيص في المواقع التالية:

- مسار واضح
- المجلد الذي يحتوي على Aspose.Cells.dll
- المجلد الذي يحتوي على التجميع الذي دعا إلى Aspose.Cells.dll
- المجلد الذي يحتوي على تجميع الدخول (ملف .exe) الخاص بك
- مورد مضمن في التجميع الذي دعا إلى Aspose.Cells.dll

هناك طريقتان شائعتين لتطبيق ترخيص، من ملف أو تيار، أو كمورد مضمن.

### **كيفية تطبيق ترخيص من القرص أو مصدر بيانات**

أسهل طريقة لتعيين ترخيص هو وضع ملف الترخيص في نفس المجلد الذي يحتوي على Aspose.Cells.dll وتحديد اسم الملف فقط دون مساره.

{{< highlight csharp >}}

 //Instantiate an instance of license and set the license file through its path

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

عندما تقوم بدعوة طريقة SetLicense، يجب أن يكون اسم الترخيص نفس اسم ملف الترخيص الخاص بك. على سبيل المثال، يمكنك تغيير اسم ملف الترخيص إلى Aspose.Cells.lic.xml. ثم في الكود الخاص بك، يجب أن تستخدم اسم الترخيص المعدل (Aspose.Cells.lic.xml) لطريقة SetLicense.

{{% /alert %}}

من الممكن أيضًا تحميل ترخيص من مصدر بيانات.

{{< highlight csharp >}}

 //Instantiate an instance of license and set the license through a stream

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **كيفية تطبيق ترخيص معتمد على الاستخدام**

تسمح Aspose.Cells للمطورين بتطبيق مفتاح معتمد. إنه آلية ترخيص جديدة. سيتم استخدام آلية الترخيص الجديدة إلى جانب الطريقة الترخيص الموجودة. يمكن لأولئك العملاء الذين يرغبون في الفوترة استنادًا إلى استخدام ميزات واجهة برمجة التطبيقات استخدام الترخيص المعتمد. لمزيد من التفاصيل، يرجى الرجوع إلى قسم [معتمد الاستخدام الترخيص الأكثر مبيعًا](https://purchase.aspose.com/faqs/licensing/metered).  

تم إدخال فئة جديدة [معتمد](https://reference.aspose.com/cells/net/aspose.cells/metered) لتطبيق مفتاح معتمد. يلي أدناه الرمز النموذجي الذي يوضح كيفية تعيين مفتاح عام وخاص للترخيص المعتمد.

{{< highlight csharp >}}

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

### **كيفية استخدام مورد مضمن**

طريقة آخرى رائعة لتعبئة الترخيص مع تطبيقك والتأكد من عدم فقدانه، هي تضمينه كمورد مضمن في أحد التجميعات التي تدعو إلى Aspose.Cells. لتضمين ملف الترخيص كمورد مضمن، قم بأداء الخطوات التالية:

1. في Visual Studio .NET، قم بتضمين ملف الترخيص (.lic) في المشروع من خلال تحديد [إضافة عنصر موجود] من القائمة [ملف].
1. حدد الملف في مستكشف الحلول وقم بتعيين [فعل البناء] إلى [مورد مضمن] في نافذة الخصائص

لا يلزم الوصول إلى الترخيص المضمن في التجميع (كمورد مضمن) أن يتم استدعاء GetExecutingAssembly و GetManifestResourceStream من فئة System.Reflection.Assembly في الإطار .NET من Microsoft. كل ما تحتاج إلى فعله هو إضافة ملف الترخيص كمورد مضمن في مشروعك وتمرير اسم ملف الترخيص إلى طريقة SetLicense. ستجد فئة Aspose.Cells.License تلقائيًا ملف الترخيص في الموارد المضمنة. يرجى مراجعة المثال المعطى أدناه لفهم هذه الطريقة لتعيين الترخيص (مضمن) في تطبيقاتك.

{{< highlight csharp >}}

 //Instantiate the License class

Aspose.Cells.License license = new Aspose.Cells.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **كيفية ضبط الترخيص في ضوابط Aspose.Cells Grid**

في مجموعة Aspose.Cells Grid Suite، يمكن تحميل الترخيص من ملف أو مصدر بيانات أو مورد مضمن. تحاول Aspose.Cells.GridDesktop / Aspose.Cells.GridWeb العثور على الترخيص في المواقع التالية:

1. مسار صريح
1. المجلد الذي يحتوي على ملف الـ DLL للمكون (المدرج في Aspose.Cells.GridDesktop أو Aspose.Cells.GridWeb)
1. المجلد الذي يحتوي على التجميع الذي استدعى ملف الـ DLL للمكون (المدرج في Aspose.Cells.GridDesktop أو Aspose.Cells.GridWeb)
1. المجلد الذي يحتوي على تجميع الدخول (الملف .exe الخاص بك)
2. مورد مضمن في التجميع الذي استدعى ملف الـ DLL للمكون (المدرج في Aspose.Cells.GridDesktop أو Aspose.Cells.GridWeb)

{{% alert color="primary" %}}

إذا كنت تستخدم تحكم Aspose.Cells.GridDesktop، سيتم استخدام فئة الترخيص Aspose.Cells.GridDesktop.License ولكن إذا كنت تستخدم تحكم Aspose.Cells.GridWeb، سيتم استخدام فئة الترخيص Aspose.Cells.GridWeb.License لضبط الترخيص.

{{% /alert %}}

### **كيفية تطبيق ترخيص من القرص أو مصدر بيانات**

أسهل طريقة لضبط ترخيص هي وضع ملف الترخيص في نفس المجلد الذي يحتوي على ملف الـ DLL للمكون (المدرج في Aspose.Cells.GridWeb) وتحديد اسم الملف فقط دون مساره.

{{< highlight csharp >}}

//Instantiate an instance of license and set the license file through its path

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense("MyLicense.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

عند استدعاء طريقة SetLicense، يجب أن يكون اسم الترخيص هو نفس اسم ملف الترخيص الخاص بك. على سبيل المثال، يمكنك تغيير اسم ملف الترخيص إلى "MyLicense.lic.xml". ثم في كودك، يجب أن تستخدم اسم الترخيص المعدل (أي MyLicense.lic.xml) لطريقة SetLicense.

{{% /alert %}}

من الممكن أيضًا تحميل ترخيص من مصدر بيانات.

{{< highlight csharp >}}

//Instantiate an instance of license and set the license through a stream

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **كيفية تطبيق ترخيص كمورد مضمن**

طريقة أخرى جميلة لتعبئة الترخيص مع تطبيقك والتأكد من عدم فقدانه هي تضمينه كمورد مضمن في أحد التجميعات التي تستدعي ملف الـ DLL للمكون (المدرج في Aspose.Cells.GridDesktop). لتضمين ملف الترخيص كمورد مضمن، قم بأداء الخطوات التالية:

1. في Visual Studio .NET، قم بتضمين ملف الترخيص (.lic) في المشروع باستخدام خيار **إضافة عنصر موجود** في قائمة **ملف**.
1. حدد الملف في مستكشف الحلول وقم بتعيين Build Action إلى مورد مضمن في نافذة الخصائص.
1. للوصول إلى الترخيص المضمن في التجميع (كمورد مضمن)، ليس من الضروري استدعاء GetExecutingAssembly و GetManifestResourceStream من فئة System.Reflection.Assembly في Microsoft .NET Framework. بدلاً من ذلك، أضف ملف الترخيص كمورد مضمن في مشروعك وقم بتمرير اسم ملف الترخيص إلى طريقة SetLicense. تجد الفئة الترخيص تلقائيًا ملف الترخيص في الموارد المضمنة.

برجاء مراجعة المثال المعطى أدناه لفهم هذه الطريقة لتطبيق ترخيص كمورد مضمن لتطبيقاتك.

{{< highlight csharp >}}

 //Instantiate the License class

Aspose.Cells.GridDesktop.License license = new Aspose.Cells.GridDesktop.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Total.lic");

{{< /highlight >}}

## **كيفية تطبيق ترخيص في Aspose.Cells.GridDesktop لتطبيق WinForm**

من المستحسن أن تضع كود الترخيص قبل بدء تطبيقك وتطبيقه مرة واحدة فقط. على سبيل المثال، لتطبيق كود الترخيص لتطبيق C# على نظام Windows، قم بوضع كود الترخيص في الطريقة الرئيسية.

{{< highlight csharp >}}

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

## **ملاحظات حول تطبيق الترخيص في Aspose.Cells.GridWeb**

من المُستحسن وضع رمز الترخيص في ملف Global.asax.cs لتطبيق الويب الخاص بك (يُفترض وضع ملف الترخيص هذا على محرك " d:\ "):

{{< highlight csharp >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(@"d:\Aspose.Cells.GridWeb.lic.xml");

}

{{< /highlight >}}

تحميل ترخيص من تيار

{{< highlight csharp >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(myStream);

}

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
