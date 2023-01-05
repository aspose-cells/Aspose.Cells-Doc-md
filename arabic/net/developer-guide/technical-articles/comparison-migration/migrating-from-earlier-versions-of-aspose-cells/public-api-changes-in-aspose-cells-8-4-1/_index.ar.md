---
title: عام API التغييرات في Aspose.Cells 8.4.1
type: docs
weight: 140
url: /ar/net/public-api-changes-in-aspose-cells-8-4-1/
---
{{% alert color="primary" %}} 

 يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.4.0 إلى 8.4.1 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ،[الفئات المضافة وما إلى ذلك.](/cells/ar/net/public-api-changes-in-aspose-cells-8-4-1/) و[الفئات المحذوفة وما إلى ذلك.](/cells/ar/net/public-api-changes-in-aspose-cells-8-4-1/)ولكن أيضًا وصف لأية تغييرات في السلوك خلف الكواليس عام Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **آلية تعديل اتصال قاعدة البيانات**
احتوت الفئة Aspose.Cells.ExternalConnections.ExternalConnection بالفعل على الطريقة والخصائص التي يمكن استخدامها لفحص تفاصيل اتصال قاعدة البيانات المخزنة في جدول بيانات. تمت قراءة معظم الخصائص المرتبطة بفئة Aspose.Cells.ExternalConnections.ExternalConnection حتى إصدار Aspose.Cells for .NET 8.4.1. مع هذا الإصدار ، قدم API الدعم لمعالجة إعدادات اتصال قاعدة البيانات أيضًا.

يوضح مقتطف التعليمات البرمجية التالي كيفية تعديل إعدادات اتصال قاعدة البيانات ديناميكيًا.

**C#**

{{< highlight "csharp" >}}

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



فيما يلي بعض الخصائص الأكثر أهمية التي تم عرضها بواسطة الفئة {Aspose.Cells.ExternalConnections.ExternalConnection}}.

|**اسم الخاصية**|**وصف**|
|:- |:- |
|الخلفية|يشير إلى ما إذا كان يمكن تحديث الاتصال في الخلفية (بشكل غير متزامن).<br> صحيح إذا كان الاستخدام المفضل للاتصال هو التحديث غير المتزامن في الخلفية ؛<br>خطأ إذا كان الاستخدام المفضل للاتصال هو التحديث المتزامن في المقدمة.|
|وصف الاتصال|يحدد وصف المستخدم لهذا الاتصال|
|معرف الاتصال|يحدد المعرف الفريد لهذا الاتصال.|
|أوراق اعتماد|تحدد طريقة المصادقة التي سيتم استخدامها عند إنشاء الاتصال (أو إعادة تأسيسه).|
|يتم حذف|يشير إلى ما إذا كان قد تم حذف اتصال المصنف المرتبط. صحيح إذا كان<br>تم حذف الاتصال ؛ خلاف ذلك ، خطأ.|
|جديد| صحيح إذا لم يتم تحديث الاتصال لأول مرة ؛ خلاف ذلك ، خطأ. هذه<br>يمكن أن تحدث الحالة عندما يحفظ المستخدم الملف قبل أن ينتهي الاستعلام من العودة.|
|حافظ على حياتك|صحيح عندما يجب أن يبذل تطبيق جدول البيانات جهودًا للحفاظ على الاتصال<br> افتح. عندما يكون خطأ ، يجب أن يغلق التطبيق الاتصال بعد استرجاع ملف<br>معلومة.|
|اسم|يحدد اسم الاتصال. يجب أن يكون لكل اتصال اسم فريد.|
|OdcFile| يحدد المسار الكامل لملف الاتصال الخارجي الذي كان هذا الاتصال منه<br> خلقت. إذا فشل الاتصال أثناء محاولة تحديث البيانات ، وطريقة إعادة الاتصال = 1 ،<br> ثم سيحاول تطبيق جدول البيانات مرة أخرى باستخدام معلومات من ملف الاتصال الخارجي<br>بدلاً من كائن الاتصال المضمّن في المصنف.|
|OnlyUseConnectionFile| يشير إلى ما إذا كان يجب أن يستخدم تطبيق جدول البيانات امتداد<br> يشار إلى معلومات الاتصال في ملف الاتصال الخارجي بواسطة السمة odcFile<br> عندما يتم تحديث الاتصال. إذا كان خطأ ، ثم تطبيق جدول البيانات<br>يجب اتباع الإجراء المشار إليه بواسطة سمة إعادة الاتصال|
|حدود|الحصول على مجموعة ConnectionParameterCollection لـ ODBC أو استعلام ويب.|
|طريقة إعادة الاتصال|حدد نوع طريقة إعادة الاتصال|
|تحديث داخلي|يحدد عدد الدقائق بين عمليات التحديث التلقائية للاتصال.|
|RefreshOnLoad|صحيح إذا كان يجب تحديث هذا الاتصال عند فتح الملف ؛ خلاف ذلك ، خطأ.|
|حفظ البيانات|صواب إذا كان سيتم حفظ البيانات الخارجية التي تم جلبها عبر الاتصال لملء جدول<br>مع المصنف خلاف ذلك ، خطأ.|
|حفظ كلمة المرور|صحيح إذا كان سيتم حفظ كلمة المرور كجزء من سلسلة الاتصال ؛ خلاف ذلك ، خطأ.|
|مصدر الملف| يُستخدم عندما يكون مصدر البيانات الخارجية مستندًا إلى الملف. عند الاتصال بمثل هذه البيانات<br> فشل المصدر ، يحاول تطبيق جدول البيانات الاتصال مباشرة بهذا الملف. ربما<br>معبرًا عنه في URI أو تدوين مسار الملف الخاص بالنظام.|
|SSOId|معرّف للدخول الأحادي (SSO) يُستخدم للمصادقة بين وسيط<br>خادم spreadsheetML ومصدر البيانات الخارجي.|
|يكتب|يحدد نوع مصدر البيانات.|

### **القدرة على تنسيق سلسلة فرعية من نص DataLabels**
كشف Aspose.Cells for .NET 8.4.1 طريقة DataLabels.Characters لاسترداد نسخة من فئة FontSetting التي تتوافق مع السلسلة الفرعية لـ ChartPoints.DataLabels. في المقابل ، يمكن استخدام مثيل فئة FontSetting لتنسيق السلسلة الفرعية من DataLabels بإعدادات وألوان مختلفة للخط.

يوضح مقتطف الشفرة التالي كيفية استخدام طريقة DataLabels.Characters.

**C#**

{{< highlight "csharp" >}}

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


### **القدرة على تعيين أبعاد الصورة المرغوبة لتصدير جدول البيانات والمخطط**
كشف Aspose.Cells for .NET 8.4.1 عن طريقة ImageOrPrintOptions.SetDesiredSize لتعيين أبعاد الصورة الناتجة أثناء تصدير جداول البيانات والمخططات إلى الصور. تقبل طريقة ImageOrPrintOptions.SetDesiredSize معلمتين من نوع العدد الصحيح ، حيث يكون الأول هو العرض المطلوب والثاني هو الارتفاع المطلوب.

يوضح مقتطف الكود التالي كيفية تعيين الأبعاد المطلوبة أثناء تصدير ورقة العمل إلى PNG.

**C#**

{{< highlight "csharp" >}}

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

يمكن أيضًا استخدام نفس الخاصية لتحويل المخططات إلى صور.

{{% /alert %}} 


### **تقديم التعليقات إلى PDF**
مع إصدار v8.4.1 ، قدم Aspose.Cells API خاصية PageSetup.PrintComments و PrintCommentsType لتسهيل عرض التعليقات أثناء تحويل جداول البيانات إلى تنسيق PDF. تعداد PrintCommentsType له الثوابت التالية.

- PrintCommentsType.PrintNoComments: لا يتم عرض التعليقات.
- PrintCommentsType.PrintInPlace: يتم عرض التعليقات حيث يتم وضعها.
- PrintCommentsType.PrintSheetEnd: يتم عرض التعليقات في نهاية ورقة العمل.

يوضح نموذج التعليمات البرمجية التالي استخدام خاصية PageSetup.PrintComments لعرض التعليقات باستخدام كافة قيم تعداد PrintCommentsType الممكنة.

**C#**

{{< highlight "csharp" >}}

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


### **انقل أوراق العمل في Aspose.Cells.GridDesktop**
Aspose.Cells.GridDesktop يوفر طريقة WorksheetCollection.MoveTo ، التي يمكن استخدامها لنقل ورقة العمل إلى الفهرس المحدد. تأخذ الطريقة المذكورة الفهارس (المستندة إلى الصفر) من ورقة العمل المصدر وورقة العمل الوجهة كمعلمات.

يوضح نموذج التعليمات البرمجية التالي استخدام الخاصية WorksheetCollection.MoveTo.

**C#**

{{< highlight "csharp" >}}

 //Move the second worksheet to 4th position.

GridDesktop1.Worksheets.MoveTo(1, 3);

{{< /highlight >}}


### **تمت إضافة المصنف. خاصية مرخصة**
لقد كشف Aspose.Cells for .NET 8.4.1 عن المصنف. تم ترخيصه والذي يمكن أن يساعد بشكل كبير في تحديد ما إذا تم تحميل الترخيص بنجاح أم لا. إذا قمت بالوصول إلى هذه الخاصية قبل تعيين الترخيص ، فسوف تُرجع القيمة false والعكس صحيح ، ومع ذلك ، يجب أن يكون الترخيص صالحًا.

يوضح نموذج التعليمات البرمجية التالي استخدام الخاصية Workbook.IsLicensed.

**C#**

{{< highlight "csharp" >}}

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
كشف Aspose.Cells for .NET 8.4.1 خاصية SVGFitToViewPort لفئة ImageOrPrintOptions التي يمكن استخدامها لتشغيل سمة viewBox لتنسيق ملف SVG أثناء تصدير جداول البيانات أو المخططات إلى تنسيق SVG. القيمة الافتراضية لهذه الخاصية خاطئة ، وبالتالي فإن XML الأساسي لملف SVG الذي تم إنشاؤه بدون تعيين الخاصية المذكورة أعلاه لن يتضمن سمة viewBox.

يوضح نموذج التعليمات البرمجية التالي استخدام خاصية ImageOrPrintOptions.SVGFitToViewPort.

**C#**

{{< highlight "csharp" >}}

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
## **واجهات برمجة التطبيقات المهجورة**
### **أسلوب Workbook.ValidateFormula قديم**
استخدم طريقة الصيغة Cell. للتحقق من صحة الصيغة.
