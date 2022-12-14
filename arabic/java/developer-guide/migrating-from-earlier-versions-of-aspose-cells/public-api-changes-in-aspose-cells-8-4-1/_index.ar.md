---
title: عام API التغييرات في Aspose.Cells 8.4.1
type: docs
weight: 150
url: /ar/java/public-api-changes-in-aspose-cells-8-4-1/
---
{{% alert color="primary" %}} 

 يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.4.0 إلى 8.4.1 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ،[الفئات المضافة وما إلى ذلك.](/cells/ar/java/public-api-changes-in-aspose-cells-8-4-1/) و[الفئات المحذوفة وما إلى ذلك.](/cells/ar/java/public-api-changes-in-aspose-cells-8-4-1/)ولكن أيضًا وصف لأية تغييرات في السلوك خلف الكواليس عام Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **آلية تعديل اتصال قاعدة البيانات**
احتوت الفئة com.aspose.cells.ExternalConnection بالفعل على الطريقة والخصائص التي يمكن استخدامها لفحص تفاصيل اتصال قاعدة البيانات المخزنة في جدول بيانات. تمت قراءة معظم الخصائص المرتبطة بفئة ExternalConnection فقط حتى إصدار Aspose.Cells for Java 8.4.1. مع هذا الإصدار ، قدم API الدعم لمعالجة إعدادات اتصال قاعدة البيانات أيضًا.

يوضح مقتطف التعليمات البرمجية التالي كيفية تعديل إعدادات اتصال قاعدة البيانات ديناميكيًا.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first data connection

com.aspose.cells.ExternalConnection conn = workbook.getDataConnections().get(0);

//Change a few properties

conn.setName("MyConnectionName");

conn.setOdcFile("MyDefaulConnection.odc");

conn.setConnectionDescription("Test Connection");

conn.setCredentials(com.aspose.cells.CredentialsMethodType.PROMPT);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

فيما يلي بعض أهم الخصائص التي تم الكشف عنها بواسطة فئة {ExternalConnection}}.

|**اسم الخاصية** |**وصف** |
|:- |:- |
| الخلفية|يشير إلى ما إذا كان يمكن تحديث الاتصال في الخلفية (بشكل غير متزامن).<br> صحيح إذا كان الاستخدام المفضل للاتصال هو التحديث غير المتزامن في الخلفية ؛<br> خطأ إذا كان الاستخدام المفضل للاتصال هو التحديث المتزامن في المقدمة.|
| وصف الاتصال| يحدد وصف المستخدم لهذا الاتصال|
| معرف الاتصال| يحدد المعرف الفريد لهذا الاتصال.|
| أوراق اعتماد| تحدد طريقة المصادقة التي سيتم استخدامها عند إنشاء الاتصال (أو إعادة تأسيسه).|
| يتم حذف|يشير إلى ما إذا كان قد تم حذف اتصال المصنف المرتبط. صحيح إذا كان<br> تم حذف الاتصال ؛ خلاف ذلك ، خطأ.|
| جديد| صحيح إذا لم يتم تحديث الاتصال لأول مرة ؛ خلاف ذلك ، خطأ. هذه<br> يمكن أن تحدث الحالة عندما يحفظ المستخدم الملف قبل أن ينتهي الاستعلام من العودة.|
| حافظ على حياتك|صحيح عندما يجب أن يبذل تطبيق جدول البيانات جهودًا للحفاظ على الاتصال<br> افتح. عندما يكون خطأ ، يجب أن يغلق التطبيق الاتصال بعد استرجاع ملف<br> معلومة.|
| اسم| يحدد اسم الاتصال. يجب أن يكون لكل اتصال اسم فريد.|
| OdcFile| يحدد المسار الكامل لملف الاتصال الخارجي الذي كان هذا الاتصال منه<br> خلقت. إذا فشل الاتصال أثناء محاولة تحديث البيانات ، وطريقة إعادة الاتصال = 1 ،<br> ثم سيحاول تطبيق جدول البيانات مرة أخرى باستخدام معلومات من ملف الاتصال الخارجي<br> بدلاً من كائن الاتصال المضمّن في المصنف.|
| OnlyUseConnectionFile| يشير إلى ما إذا كان يجب أن يستخدم تطبيق جدول البيانات امتداد<br> يشار إلى معلومات الاتصال في ملف الاتصال الخارجي بواسطة السمة odcFile<br> عندما يتم تحديث الاتصال. إذا كان خطأ ، ثم تطبيق جدول البيانات<br>يجب اتباع الإجراء المشار إليه بواسطة سمة إعادة الاتصال|
| المعلمات| الحصول على مجموعة ConnectionParameterCollection لـ ODBC أو استعلام ويب.|
| طريقة إعادة الاتصال| حدد نوع طريقة إعادة الاتصال|
|تحديث داخلي| يحدد عدد الدقائق بين عمليات التحديث التلقائية للاتصال.|
| RefreshOnLoad| صحيح إذا كان يجب تحديث هذا الاتصال عند فتح الملف ؛ خلاف ذلك ، خطأ.|
| حفظ البيانات|صواب إذا كان سيتم حفظ البيانات الخارجية التي تم جلبها عبر الاتصال لملء جدول<br> مع المصنف خلاف ذلك ، خطأ.|
| حفظ كلمة المرور| صحيح إذا كان سيتم حفظ كلمة المرور كجزء من سلسلة الاتصال ؛ خلاف ذلك ، خطأ.|
| مصدر الملف| يُستخدم عندما يكون مصدر البيانات الخارجية مستندًا إلى الملف. عند الاتصال بمثل هذه البيانات<br> فشل المصدر ، يحاول تطبيق جدول البيانات الاتصال مباشرة بهذا الملف. ربما<br> معبرًا عنه في URI أو تدوين مسار الملف الخاص بالنظام.|
|SSOId|معرّف للدخول الأحادي (SSO) يُستخدم للمصادقة بين وسيط<br> خادم spreadsheetML ومصدر البيانات الخارجي.|
| يكتب| يحدد نوع مصدر البيانات.|

### **القدرة على تنسيق سلسلة فرعية من نص DataLabels**
كشف Aspose.Cells for Java 8.4.1 طريقة DataLabels.characters لاسترداد نسخة من فئة FontSetting التي تتوافق مع السلسلة الفرعية لـ ChartPoints.DataLabels. في المقابل ، يمكن استخدام مثيل فئة FontSetting لتنسيق السلسلة الفرعية من DataLabels بإعدادات وألوان مختلفة للخط.

يوضح مقتطف الشفرة التالي كيفية استخدام طريقة DataLabels.characters.

**Java**

{{< highlight "csharp" >}}

 //Create a workbook from source Excel file

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the first chart inside the sheet

com.aspose.cells.Chart chart = worksheet.getCharts().get(0);

//Access the data label of first series first point

com.aspose.cells.DataLabels labels = chart.getNSeries().get(0).getPoints().get(0).getDataLabels();

//Set data label text

labels.setText("Rich Text Label");

//Set the font setting of the first 10 characters

com.aspose.cells.FontSetting settings = labels.characters(0, 10);

settings.getFont().setColor(com.aspose.cells.Color.getRed());

settings.getFont().setBold(true);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

### **القدرة على تعيين أبعاد الصورة المرغوبة لتصدير جدول البيانات والمخطط**
كشف Aspose.Cells for Java 8.4.1 عن طريقة ImageOrPrintOptions.setDesiredSize لتعيين أبعاد الصورة الناتجة أثناء تصدير جداول البيانات والمخططات إلى الصور. تقبل طريقة ImageOrPrintOptions.setDesiredSize معلمتين من نوع العدد الصحيح ، حيث يكون الأول هو العرض المطلوب والثاني هو الارتفاع المطلوب.

يوضح مقتطف التعليمات البرمجية التالي كيفية تعيين الأبعاد المطلوبة أثناء تصدير ورقة العمل إلى PNG.

**Java**

{{< highlight "csharp" >}}

 com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Create an instance of ImageOrPrintOptions

com.aspose.cells.ImageOrPrintOptions options = new com.aspose.cells.ImageOrPrintOptions();

//Set resultant image format

options.setImageFormat(com.aspose.cells.ImageFormat.getPng());

//Set desired dimensions as 400x400

options.setDesiredSize(400, 400);

//Render sheet to image

com.aspose.cells.SheetRender renderer = new com.aspose.cells.SheetRender(worksheet, options);

renderer.toImage(0, "output.png");

{{< /highlight >}}

{{% alert color="primary" %}} 

 يمكن أيضًا استخدام نفس الطريقة لتحويل المخططات إلى صور.

{{% /alert %}} 

### **تقديم التعليقات إلى PDF**
 مع إصدار v8.4.1 ، قدم Aspose.Cells API خاصية PageSetup.PrintComments و PrintCommentsType لتسهيل عرض التعليقات أثناء تحويل جداول البيانات إلى تنسيق PDF. تعداد PrintCommentsType له الثوابت التالية.

- PrintCommentsType.PRINT_رقم_التعليقات: لا يجوز تقديم التعليقات.
- PrintCommentsType.PRINT_في_PLACE: يتم عرض التعليقات حيث يتم وضعها.
- PrintCommentsType.PRINT_ملزمة_النهاية: يتم عرض التعليقات في نهاية ورقة العمل.

يوضح نموذج التعليمات البرمجية التالي استخدام خاصية PageSetup.PrintComments لعرض التعليقات باستخدام كافة قيم تعداد PrintCommentsType الممكنة.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of workbook

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Print no comments

worksheet.getPageSetup().setPrintComments(com.aspose.cells.PrintCommentsType.PRINT_NO_COMMENTS);

//Save workbook in PDF format without comments

workbook.save("nocomments.pdf");

//Print the comments as displayed on sheet

worksheet.getPageSetup().setPrintComments(com.aspose.cells.PrintCommentsType.PRINT_IN_PLACE);

//Save workbook in PDF format while rendering comments in place

workbook.save("printinplace.pdf");

//Print the comments at the end of sheet

worksheet.getPageSetup().setPrintComments(com.aspose.cells.PrintCommentsType.PRINT_SHEET_END);

//Save workbook in PDF format while rendering comments at the end of worksheet

workbook.save("printsheetend.pdf");

{{< /highlight >}}

### **تمت إضافة خاصية Workbook.is المرخصة**
كشف Aspose.Cells for Java 8.4.1 Workbook.isLicensed والذي يمكن أن يساعد بشكل كبير في تحديد ما إذا تم تحميل الترخيص بنجاح أم لا. إذا قمت بالوصول إلى هذه الخاصية قبل تعيين الترخيص ، فسوف تُرجع القيمة false والعكس صحيح ، ومع ذلك ، يجب أن يكون الترخيص صالحًا.

يوضح نموذج التعليمات البرمجية التالي استخدام الخاصية Workbook.isLicensed.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object before setting a license

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook();

//Check if the license is loaded or not

if (!workbook.isLicensed())

{

	//Set license

	com.aspose.cells.License license = new com.aspose.cells.License();

	lic.SetLicense(licPath);

}

else

{

  //do process

}

{{< /highlight >}}

### **تمت إضافة خاصية ImageOrPrintOptions.SVGFitToViewPort**
كشف Aspose.Cells for Java 8.4.1 عن خاصية SVGFitToViewPort لفئة ImageOrPrintOptions التي يمكن استخدامها لتشغيل خاصية viewBox لتنسيق ملف SVG أثناء تصدير جداول البيانات أو الرسوم البيانية إلى تنسيق SVG. القيمة الافتراضية لهذه الخاصية هي false لذا فإن XML الأساسي لملف SVG الذي تم إنشاؤه بدون تعيين الخاصية المذكورة أعلاه لن تتضمن سمة viewBox.

يوضح نموذج التعليمات البرمجية التالي استخدام خاصية ImageOrPrintOptions.SVGFitToViewPort.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object from source file

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Create an instance of ImageOrPrintOptions

com.aspose.cells.ImageOrPrintOptions options = new com.aspose.cells.ImageOrPrintOptions();

//Set image format to SVG

options.setSaveFormat(com.aspose.cells.SaveFormat.SVG);

//Set the SVGFitToViewPort to true

options.setSVGFitToViewPort(true);

//Create an instance of SheetRender and initialize it with worksheet instance as well as object of ImageOrPrintOptions

com.aspose.cells.SheetRender renderer = new com.aspose.cells.SheetRender(worksheet, options);

renderer.toImage(0, "output.svg");

{{< /highlight >}}
## **واجهات برمجة التطبيقات التي عفا عليها الزمن**
### **أسلوب Workbook.validateFormula قديم**
استخدم خاصية Cell.Formula للتحقق من صحة الصيغة.
