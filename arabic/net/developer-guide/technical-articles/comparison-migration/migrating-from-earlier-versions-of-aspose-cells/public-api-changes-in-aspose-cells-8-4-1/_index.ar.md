---
title: تغييرات الواجهة العامة في Aspose.Cells 8.4.1
type: docs
weight: 140
url: /ar/net/public-api-changes-in-aspose-cells-8-4-1/
---

{{% alert color="primary" %}} 

توضح هذه الوثيقة التغييرات في واجهة برمجة Aspose.Cells من الإصدار 8.4.0 إلى 8.4.1 التي قد تكون مثيرة لاهتمام مطوري الوحدات/التطبيقات. وتشمل ليس فقط الأساليب العامة الجديدة والمحدثة و[الفئات المضافة الخ وما إلى ذلك](/cells/ar/net/public-api-changes-in-aspose-cells-8-4-1/) و[الفئات المحذوفة الخ وما إلى ذلك](/cells/ar/net/public-api-changes-in-aspose-cells-8-4-1/), ولكن أيضًا وصف لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **آلية تعديل اتصال قاعدة البيانات**
احتوت فئة Aspose.Cells.ExternalConnections.ExternalConnection بالفعل على الطريقة والخصائص التي يمكن استخدامها لفحص تفاصيل اتصال قاعدة البيانات المخزنة في جدول بيانات. كانت معظم الخصائص المرتبطة بفئة Aspose.Cells.ExternalConnections.ExternalConnection قراءة فقط حتى الإصدار Aspose.Cells for .NET 8.4.1. مع هذا الإصدار، قدمت الواجهة برمجة التطبيقات الدعم لتلاعب إعدادات اتصال قاعدة البيانات أيضًا.

يوضح مقتطف الكود التالي كيفية تعديل إعدادات اتصال قاعدة البيانات ديناميكياً.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first data connection

Aspose.Cells.ExternalConnections.ExternalConnection conn = workbook.DataConnections[0];

//Change a few properties

conn.Name = "MyConnectionName";

conn.OdcFile = "MyDefaulConnection.odc";

conn.ConnectionDescription = "Test Connection";

conn.Credentials = Aspose.Cells.ExternalConnections.CredentialsMethodType.Prompt;

//Save the workbook

workbook.Save(output);

{{< /highlight >}}



إليك بعض الخصائص الأهم التي تكشف عنها فئة {Aspose.Cells.ExternalConnections.ExternalConnection}}.

|**اسم الخاصية**|**الوصف**|
| :- | :- |
|BackgroundRefresh|يشير ما إذا كان بإمكان تحديث الاتصال في الخلفية (بشكل غير متزامن). <br>صحيح إذا كان الاستخدام المفضل للاتصال هو تحديثه بشكل غير متزامن في الخلفية؛ <br>خطأ إذا كان الاستخدام المفضل للاتصال هو تحديثه بشكل متزامن في الأمام.|
|ConnectionDescription|يحدد وصف المستخدم لهذا الاتصال|
|ConnectionId|يحدد المعرف الفريد لهذا الاتصال.|
|Credentials|تحدد طريقة المصادقة التي سيتم استخدامها عند إنشاء (أو إعادة إنشاء) الاتصال.
|IsDeleted|يشير ما إذا كان تم حذف اتصال جدول البيانات المرتبط. TRUE إذا تم حذف الاتصال. في حال عدم الحذف، يكون القيمة FALSE.
|IsNew|TRUE إذا لم يتم تحديث الاتصال للمرة الأولى، وإلا فإن القيمة FALSE. يمكن حدوث هذه الحالة عندما يقوم المستخدم بحفظ الملف قبل انتهاء الاستعلام من إعادة الرجوع.
|KeepAlive|TRUE عندما يجب على تطبيق جدول البيانات الجدولية بذل جهود للحفاظ على الاتصال مفتوحًا. عندما تكون القيمة FALSE، يجب على التطبيق إغلاق الاتصال بعد استرداد المعلومات.
|Name|تحدد اسم الاتصال. يجب أن يكون لكل اتصال اسم فريد.
|OdcFile|تحدد المسار الكامل إلى ملف اتصال خارجي من تم إنشاء هذا الاتصال. إذا فشل الاتصال خلال محاولة تحديث البيانات، وكان reconnectionMethod=1، سيحاول تطبيق جدول البيانات الجدولية مرة أخرى باستخدام المعلومات من ملف الاتصال الخارجي بدلاً من كائن الاتصال المضمن داخل مصنف العمل.
|OnlyUseConnectionFile|تشير ما إذا كان يجب على تطبيق جدول البيانات الجدولية دائمًا وفقط استخدام معلومات الاتصال في ملف الاتصال الخارجي المشير إليه بسمة odcFile عند تحديث الاتصال. إذا كانت القيمة FALSE، فيجب على تطبيق جدول البيانات الجدولية اتباع الإجراء المشار إليه بسمة reconnectionMethod.
|Parameters|يحصل على مجموعة ConnectionParameterCollection لاستعلام ODBC أو الويب.
|ReConnectionMethod|تحديد نوع reconnectionMethod.
|RefreshInternal|: يُحدد عدد الدقائق بين تحديثات الاتصال التلقائية.|
|RefreshOnLoad|TRUE إذا كان يجب تحديث هذا الاتصال عند فتح الملف، وإلا فإن القيمة FALSE.
|SaveData|TRUE إذا كانت البيانات الخارجية التي تم استردادها عبر الاتصال لملء الجدول يجب حفظها مع مصنف العمل، وإلا فإن القيمة FALSE.
|SavePassword|TRUE إذا كان يجب حفظ كلمة المرور كجزء من سلسلة الاتصال، وإلا فإن القيمة FALSE.
|SourceFile|يستخدم عندما تكون مصدر البيانات الخارجية مستندة إلى ملف. عند فشل الاتصال بمثل هذا المصدر، يحاول تطبيق جدول البيانات الجدولية الاتصال مباشرة بملف البيانات هذا. قد يتم التعبير عنها في URI أو علامة مرجعية مسار الملف النظام.
|SSOId|معرف لتسجيل الدخول الفردي (SSO) المستخدم للمصادقة بين خادم صفحة بيانات جدول البيانات الوسيط ومصدر البيانات الخارجي.
|Type|تحدد نوع مصدر البيانات.

### **قدرة تنسيق السلسلة الفرعية لنصوص DataLabels**
Aspose.Cells for .NET 8.4.1 لقد عرضت القدرة على تنسيق الطرق Charagters لاسترداد مثيل من فئة FontSetting التي تتوافق مع السلسلة الفرعية لـ ChartPoints. يمكن استخدام مثيل فئة FontSetting لتنسيق السلسلة الفرعية للـ DataLabels بإعدادات خطوط ولون مختلفة.

يعرض مقتطف الكود التالي كيفية استخدام طريقة Charagters الخاصة بـ DataLabels.

**C#**

{{< highlight csharp >}}

 //Create a workbook from source Excel file

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Access the first chart inside the sheet

Aspose.Cells.Charts.Chart chart = worksheet.Charts[0];

//Access the data label of first series first point

Aspose.Cells.Charts.DataLabels labels = chart.NSeries[0].Points[0].DataLabels;

//Set data label text

labels.Text = "Rich Text Label";

//Set the font setting of the first 10 characters

Aspose.Cells.FontSetting settings = labels.Characters(0, 10);

settings.Font.Color = System.Drawing.Color.Red;

settings.Font.IsBold = true;

//Save the workbook

workbook.Save(output);

{{< /highlight >}}


### **قدرة تعيين أبعاد الصور المرغوبة لتصدير جداول البيانات والرسوم البيانية**
Aspose.Cells for .NET 8.4.1 قد عرضت طريقة SetDesiredSize للفئة ImageOrPrintOptions لتعيين أبعاد الصورة الناتجة أثناء تصدير جداول البيانات والرسوم البيانية إلى صور. تقبل طريقة SetDesiredSize للفئة ImageOrPrintOptions معاملي نوع العدد الصحيح، حيث يكون الأول عرض المطلوب والثاني ارتفاع المطلوب.

يُظهر مقطع الكود التالي كيفية تعيين الأبعاد المرغوبة أثناء تصدير ورقة العمل إلى PNG.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source file

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Create an instance of ImageOrPrintOptions

Aspose.Cells.Rendering.ImageOrPrintOptions options = new Aspose.Cells.Rendering.ImageOrPrintOptions();

//Set resultant image format

options.ImageFormat = System.Drawing.Imaging.ImageFormat.Png;

//Set desired dimensions as 400x400

options.SetDesiredSize(400, 400);

//Render sheet to image

Aspose.Cells.Rendering.SheetRender renderer = new Aspose.Cells.Rendering.SheetRender(worksheet, options);

renderer.ToImage(0, "output.png"); 

{{< /highlight >}}

{{% alert color="primary" %}} 

يمكن أيضًا استخدام خاصية نفسها لتحويل الرسوم البيانية إلى صور.

{{% /alert %}} 


### **عرض تعليقات إلى صيغة PDF**
مع إطلاق إصدار v8.4.1، قدمت واجهة API Aspose.Cells خاصية PageSetup.PrintComments وتصنيف PrintCommentsType من أجل تسهيل عرض التعليقات أثناء تحويل جداول البيانات إلى صيغة PDF. تصنيف PrintCommentsType يحتوي على الثوابت التالية.

- PrintCommentsType.PrintNoComments: لن يتم عرض التعليقات.
- PrintCommentsType.PrintInPlace: ستتم عرض التعليقات حيث تم وضعها.
- PrintCommentsType.PrintSheetEnd: ستتم عرض التعليقات في نهاية ورقة البيانات.

الشيفرة البرمجية النموذجية التالية توضح استخدام خاصية PageSetup.PrintComments لعرض التعليقات باستخدام جميع قيم تعداد PrintCommentsType الممكنة.

**C#**

{{< highlight csharp >}}

 //Create an instance of workbook

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Print no comments

worksheet.PageSetup.PrintComments = Aspose.Cells.PrintCommentsType.PrintNoComments;

//Save workbook in PDF format without comments

workbook.Save("nocomments.pdf");

//Print the comments as displayed on sheet

worksheet.PageSetup.PrintComments = Aspose.Cells.PrintCommentsType.PrintInPlace;

//Save workbook in PDF format while rendering comments in place

workbook.Save("printinplace.pdf");

//Print the comments at the end of sheet

worksheet.PageSetup.PrintComments = Aspose.Cells.PrintCommentsType.PrintSheetEnd;

//Save workbook in PDF format while rendering comments at the end of worksheet

workbook.Save("printsheetend.pdf");

{{< /highlight >}}


### **نقل ورقات العمل في Aspose.Cells.GridDesktop**
يوفر Aspose.Cells.GridDesktop طريقة WorksheetCollection.MoveTo يمكن استخدامها لنقل ورقة عمل إلى الفهرس المحدد. تأخذ الطريقة المذكورة مؤشرات (بداية من الصفر) لورقة العمل المصدر وورقة العمل الوجهة كمعلمات.

الكود البرنامجي التالي يوضح استخدام خاصية WorksheetCollection.MoveTo.

**C#**

{{< highlight csharp >}}

 //Move the second worksheet to 4th position.

GridDesktop1.Worksheets.MoveTo(1, 3);

{{< /highlight >}}


### **تمت إضافة خاصية Workbook.IsLicensed**
Aspose.Cells for .NET 8.4.1 قد عرضت الفئة Workbook خاصية IsLicensed التي يمكن أن تكون مفيدة لتحديد ما إذا تم تحميل الترخيص بنجاح أو لا. إذا قمت بالوصول إلى هذه الخاصية قبل تعيين الترخيص، فستعيد قيمة خاطئة والعكس صحيح، ومع ذلك، يجب أن يكون الترخيص صالحًا.

الكود البرنامجي التالي يوضح استخدام خاصية Workbook.IsLicensed.

**C#**

{{< highlight csharp >}}

 //Create workbook object before setting a license

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook();

//Check if the license is loaded or not

if (!workbook.IsLicensed)

{

    //Set license

    Aspose.Cells.License license = new Aspose.Cells.License();

    lic.SetLicense(licPath);

}

else

{

    //do process

}

{{< /highlight >}}


### **تمت إضافة خاصية ImageOrPrintOptions.SVGFitToViewPort**
Aspose.Cells for .NET 8.4.1 قد عرضت الفئة ImageOrPrintOptions خاصية SVGFitToViewPort التي يمكن استخدامها لتشغيل سمة viewBox لتنسيق ملف SVG أثناء تصدير جداول البيانات أو الرسوم البيانية إلى تنسيق SVG. القيمة الافتراضية لهذه الخاصية هي false لذلك سيتم إنشاء XML الأساسي لملف SVG الذي تم إنشاؤه بدون ضبط الخاصية المذكورة أعلاه دون تضمين سمة viewBox.

الشيفرة البرمجية النموذجية التالية توضح استخدام خاصية ImageOrPrintOptions.SVGFitToViewPort.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source file

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Create an instance of ImageOrPrintOptions

Aspose.Cells.Rendering.ImageOrPrintOptions options = new Aspose.Cells.Rendering.ImageOrPrintOptions();

//Set image format to SVG

options.SaveFormat = Aspose.Cells.SaveFormat.SVG;

//Set the SVGFitToViewPort to true

options.SVGFitToViewPort = true;

//Create an instance of SheetRender and initialize it with worksheet instance as well as object of ImageOrPrintOptions

Aspose.Cells.Rendering.SheetRender renderer = new Aspose.Cells.Rendering.SheetRender(worksheet, options);

renderer.ToImage(0, "output.svg");

{{< /highlight >}}
## **واجهات برمجة التطبيقات المهملة**
### **تم إهمال واجهة برمجة التطبيقات Workbook.ValidateFormula**
استخدم طريقة Cell.Formula للتحقق من الصيغة.
