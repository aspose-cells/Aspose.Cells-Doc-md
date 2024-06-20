---
title: تغييرات الواجهة العامة في Aspose.Cells 8.4.1
type: docs
weight: 150
url: /ar/java/public-api-changes-in-aspose-cells-8-4-1/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات Aspose.Cells من الإصدار 8.4.0 إلى 8.4.1 التي قد تكون مثيرة للاهتمام لمطوري الوحدة/التطبيق. إنه يشمل ليس فقط الأساليب العامة الجديدة والمحدثة، ولكن أيضًا وصفًا لأي تغييرات في السلوك الكامن في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **آلية تعديل اتصال قاعدة البيانات**
كانت فئة com.aspose.cells.ExternalConnection تحتوي بالفعل على الطريقة والخصائص التي يمكن استخدامها لفحص تفاصيل اتصال قاعدة البيانات المخزنة في جدول بيانات. كانت معظم الخصائص المرتبطة مع فئة ExternalConnection للقراءة فقط حتى إصدار Aspose.Cells for Java 8.4.1. مع هذا الإصدار، قدمت واجهة برمجة التطبيقات الدعم لتلاعب إعدادات اتصال قاعدة البيانات أيضاً.

يوضح مقتطف الكود التالي كيفية تعديل إعدادات اتصال قاعدة البيانات ديناميكياً.

**Java**

{{< highlight csharp >}}

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

فيما يلي بعض الخصائص الأكثر أهمية المكشوفة بواسطة فئة {ExternalConnection}}.

|**اسم الخاصية** |**الوصف** |
| :- | :- |
|BackgroundRefresh |يرمز إلى ما إذا كان بإمكان التحديث في الخلفية (بشكل غير متزامن). <br>صحيح إذا كان استخدام الاتصال المفضل هو التحديث بشكل غير متزامن في الخلفية؛ <br>خطأ إذا كان استخدام الاتصال المفضل هو التحديث بشكل متزامن في الأمام. |
|ConnectionDescription |يحدد الوصف المستخدم لهذا الاتصال |
|ConnectionId |يحدد مُعرف فريد لهذا الاتصال. |
|Credentials |يحدد طريقة المصادقة المراد استخدامها عند إنشاء (أو إعادة إنشاء) الاتصال. |
|IsDeleted |يشير ما إذا كان اتصال جدول العمل المرتبط تم حذفه. صحيح إذا كان الاتصال<br>تم حذفه؛ خلاف ذلك، خطأ. |
|IsNew |صحيح إذا لم يتم تحديث الاتصال لأول مرة؛ خلاف ذلك، خطأ. يمكن حدوث هذه الحالة عندما يقوم المستخدم بحفظ الملف قبل اكتمال الاستعلام في العودة. |
|KeepAlive |صحيح عندما يجب على تطبيق جدول البيانات بذل جهود للإبقاء على الاتصال<br>مفتوح. عندما يكون خطأ، يجب للتطبيق إغلاق الاتصال بعد استرجاع<br>المعلومات. |
|Name |يُحدد اسم الاتصال. يجب أن يحمل كل اتصال اسمًا فريدًا. |
|OdcFile |يُحدد المسار الكامل إلى ملف الاتصال الخارجي الذي تم إنشاء هذا الاتصال منه. إذا فشل الاتصال أثناء محاولة تحديث البيانات، وكان reconnectionMethod=1،<br>فسوف يحاول تطبيق جدول البيانات مرة أخرى باستخدام المعلومات من ملف الاتصال الخارجي<br>بدلاً من كائن الاتصال المضمن داخل جدول البيانات. |
|OnlyUseConnectionFile |يدل على ما إذا كان يجب على تطبيق جدول البيانات استخدام دائمًا وفقط معلومات الاتصال<br>في ملف الاتصال الخارجي المشار إليه بواسطة سمة odcFile<br>عند تحديث الاتصال. إذا كان خطأ، فإن تطبيق جدول البيانات<br>يجب أن يتبع الإجراء المشار إليه بواسطة سمة reconnectionMethod |
|Parameters |يحصل على ConnectionParameterCollection لاستعلام ODBC or web. |
|ReConnectionMethod |تحديد نوع reconnectionMethod |
|RefreshInternal|يحدد عدد الدقائق بين التحديثات التلقائية للاتصال. |
|RefreshOnLoad |القيمة صحيحة إذا كان من المفترض تحديث هذا الاتصال عند فتح الملف. خلاف ذلك، فهي خاطئة. |
|SaveData |القيمة صحيحة إذا كان من المفترض حفظ البيانات الخارجية المحصولة عبر الاتصال لملء جدول بجانب الصفحة. خلاف ذلك، فهي خاطئة. |
|SavePassword |القيمة صحيحة إذا كان من المفترض حفظ كلمة المرور كجزء من سلسلة الاتصال. خلاف ذلك، فهي خاطئة. |
|SourceFile |تُستخدم عندما يكون مصدر البيانات الخارجي مستندًا إلى ملف. عند فشل الاتصال بمصدر بيانات مثل هذا، يحاول تطبيق جدول الجداول المغلقة التوصيل مباشرة بهذا الملف. قد يكون معربًا في رمز URI أو تعبير نظامي لمسار الملفات. |
|SSOId|معرف لتسجيل الدخول الموحّد (SSO) المستخدم للمصادقة بين خادم وسيط لجدول بيانات XML ومصدر البيانات الخارجي. |
|Type |يحدد نوع مصدر البيانات. |

### **قدرة تنسيق السلسلة الفرعية لنصوص DataLabels**
Aspose.Cells for Java 8.4.1 قد عرضت طريقة DataLabels.characters لاسترداد مثيل من فئة FontSetting التي تتوافق مع السلسلة الفرعية لـ ChartPoints.DataLabels. بدوره، يمكن استخدام مثيل من فئة FontSetting لتنسيق السلسلة الفرعية للـ DataLabels بإعدادات خط مختلفة ولون.

تُظهر مقطع الكود التالي كيفية استخدام الطريقة DataLabels.characters.

**Java**

{{< highlight csharp >}}

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

### **قدرة تعيين أبعاد الصور المرغوبة لتصدير جداول البيانات والرسوم البيانية**
Aspose.Cells for Java 8.4.1 قد عرضت الطريقة ImageOrPrintOptions.setDesiredSize لتعيين أبعاد الصورة الناتجة أثناء تصدير جداول البيانات والرسوم البيانية إلى صور. تقبل طريقة ImageOrPrintOptions.setDesiredSize معاملين من النوع الصحيح، حيث يكون الأول عرض المطلوب والثاني ارتفاع المطلوب.

يُظهر مقطع الكود التالي كيفية تعيين الأبعاد المرغوبة أثناء تصدير ورقة العمل إلى PNG.

**Java**

{{< highlight csharp >}}

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

يمكن أيضًا استخدام نفس الطريقة لتحويل الرسوم البيانية إلى صور. 

{{% /alert %}} 

### **عرض تعليقات إلى صيغة PDF**
مع إطلاق إصدار v8.4.1، قدمت واجهة API Aspose.Cells خاصية PageSetup.PrintComments وتصنيف PrintCommentsType من أجل تسهيل عرض التعليقات أثناء تحويل جداول البيانات إلى صيغة PDF. تصنيف PrintCommentsType يحتوي على الثوابت التالية. 

- PrintCommentsType.PRINT_NO_COMMENTS: لا يتم عرض التعليقات.
- PrintCommentsType.PRINT_IN_PLACE: يتم عرض التعليقات حيث يذكر مكانها.
- PrintCommentsType.PRINT_SHEET_END: يجب عرض التعليقات في نهاية ورقة العمل.

الشيفرة البرمجية النموذجية التالية توضح استخدام خاصية PageSetup.PrintComments لعرض التعليقات باستخدام جميع قيم تعداد PrintCommentsType الممكنة.

**Java**

{{< highlight csharp >}}

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

### **تمت إضافة خاصية Workbook.isLicensed**
Aspose.Cells for Java 8.4.1 قد كشف عن خاصية Workbook.isLicensed التي يمكن أن تكون مفيدة في تحديد ما إذا تم تحميل الترخيص بنجاح أم لا. إذا كنت تصل إلى هذه الخاصية قبل تعيين الترخيص، ستعيد قيمة كاذبة والعكس صحيح، ومع ذلك، يجب أن يكون الترخيص صالحًا.

الشيفرة البرمجية النموذجية التالية توضح استخدام خاصية Workbook.isLicensed.

**Java**

{{< highlight csharp >}}

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
Aspose.Cells for Java 8.4.1 قد كشف عن خاصية SVGFitToViewPort لفئة ImageOrPrintOptions التي يمكن استخدامها لتشغيل سمة viewBox لتنسيق ملف SVG أثناء تصدير الجداول الإرشادية أو المخططات إلى تنسيق SVG. القيمة الافتراضية لهذه الخاصية هي كاذبة لذلك فإن النص الأساسي لملف SVG الذي تم إنشاؤه دون ضبط الخاصية المذكورة لن يتضمن سمة viewBox.

الشيفرة البرمجية النموذجية التالية توضح استخدام خاصية ImageOrPrintOptions.SVGFitToViewPort.

**Java**

{{< highlight csharp >}}

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
## **واجهات برمجة التطبيق القديمة**
### **طريقة Workbook.validateFormula أصبحت غير مستخدمة**
استخدم خاصية Cell.Formula للتحقق من الصيغة.
