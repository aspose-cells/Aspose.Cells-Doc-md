---
title: تغييرات الواجهة البرمجية العامة في Aspose.Cells 8.7.0
type: docs
weight: 240
url: /ar/java/public-api-changes-in-aspose-cells-8-7-0/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات Aspose.Cells من الإصدار 8.6.3 إلى 8.7.0 التي قد تكون مثيرة لاهتمام لمطوري الوحدة/التطبيق. يتضمن ليس فقط الطرق الجديدة والمحدثة، الفئات المضافة والمحذوفة إلخ، ولكن أيضاً وصفاً لأي تغييرات في السلوك في الخلفية في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **دعم لتحسين ملفات PDF**
توفر واجهات برمجة التطبيقات Aspose.Cells بالفعل ميزة تحويل جداول البيانات إلى PDF. مع هذا الإصدار من الواجهة البرمجية، يمكن للمستخدمين الآن [تحسين حجم ملف PDF الناتج](/cells/ar/java/save-excel-into-pdf-with-standard-or-minimum-size/) أيضاً. قدمت Aspose.Cells for Java 8.7.0 خاصية PdfSaveOptions.OptimizationType جنبًا إلى جنب مع تعداد PdfOptimizationType من أجل تسهيل عملية اختيار خوارزمية التحسين المطلوبة أثناء تصدير جداول البيانات إلى تنسيق PDF. هناك قيمتان ممكنتان لخاصية PdfSaveOptions.OptimizationType كما هو مفصل أدناه. 

1. PdfOptimizationType.MINIMUM_SIZE: يتم التنازل عن الجودة من أجل حجم الملف الناتج.
1. PdfOptimizationType.STANDARD: لا يتم التنازل عن الجودة لذا سيكون حجم الملف الناتج كبيرًا.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

 //Create an instance of PdfSaveOptions

PdfSaveOptions pdfSaveOptions = new PdfSaveOptions();

//Set the OptimizationType property to desired value

pdfSaveOptions.setOptimizationType(PdfOptimizationType.MINIMUM_SIZE);

//Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook(inFilePath);

//Save the spreadsheet in PDF format while passing the instance of PdfSaveOptions

book.save(outFilePath, pdfSaveOptions);

{{< /highlight >}}
### **كشف توقيع مشروع VBA بواسطة الأرقام**
 تم فتح خاصية VbaProject.isSigned الجديدة للاستخدام في [الكشف عما إذا كان مشروع VBA في جدول بيانات موقعي يحمل توقيعًا رقميًا](/cells/ar/java/check-if-vba-code-is-signed/). تعتبر خاصية VbaProject.isSigned من نوع Boolean وتعيد قيمة صحيحة إذا كان مشروع VBA حاملًا لتوقيع رقمي والعكس صحيح.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

VbaProject vbaProject = book.getVbaProject();

//Check if VbaProject is digitally signed

if (vbaProject.isSigned())

{

	System.out.println("VbaProject is digitally signed");

}

else

{

	System.out.println("VbaProject is not digitally signed");

}

{{< /highlight >}}
### **إضافة طريقة Protection.verifyPassword**
 قامت واجهات برمجة التطبيقات Aspose.Cells بتعزيز فئة الحماية عن طريق إدخال طريقة verifyPassword التي تسمح بتحديد كلمة مرور كنوع String و[التحقق مما إذا كانت نفس كلمة المرور قد تم استخدامها لحماية ورقة البيانات](/cells/ar/java/verify-password-used-to-protect-the-worksheet/). تعيد طريقة Protection.verifyPassword قيمة صحيحة إذا كانت كلمة المرور المحددة مطابقة لكلمة المرور المستخدمة لحماية ورقة البيانات المعطاة وتعيد قيمة خاطئة إذا كانت كلمة المرور المحددة غير مطابقة. يستخدم الكود التالي طريقة Protection.verifyPassword بالاشتراك مع حقل Protection.isProtectedWithPassword للكشف عن حماية كلمة المرور والتحقق منها.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load a spreadsheet

Workbook book = new Workbook(inFilePath);

//Access the protected Worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Check if Worksheet is password protected

if (sheet.getProtection().isProtectedWithPassword())

{

  //Verify the password used to protect the Worksheet

  if (sheet.getProtection().verifyPassword("password"))

  {

	  System.out.println("Specified password has matched");

  }

  else

  {

	  System.out.println("Specified password has not matched");

  }

}

{{< /highlight >}}
### **إضافة خاصية Protection.isProtectedWithPassword**
كما فتح هذا الإصدار من Aspose.Cells for Java الحقل Protection.isProtectedWithPassword الذي يمكن أن يكون مفيدًا في [الكشف عما إذا كانت ورقة البيانات محمية بكلمة مرور أم لا](/cells/ar/java/detect-if-worksheet-is-password-protected/).

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(inFilePath);

//Access the desired Worksheet via its index or name

Worksheet sheet = book.getWorksheets().get(0);

//Access Protection module of desired Worksheet

Protection protection = sheet.getProtection();

//Check if Worksheet is password protected

if (protection.isProtectedWithPassword())

{

	System.out.println("Worksheet is password protected");

}

else

{

	System.out.println("Worksheet is not password protected");

}

{{< /highlight >}}
### **إضافة خاصية ColorScale.Is3ColorScale**
فتح إصدار 8.7.0 من Aspose.Cells for Java خاصية ColorScale.Is3ColorScale التي يمكن استخدامها لـ [إنشاء تنسيق مشروط بمقياس ألوان مزدوج](/cells/ar/java/adding-2-color-scale-and-3-color-scale-conditional-formattings/). تعتبر الخاصية المذكورة من نوع Boolean بقيمة افتراضية صحيحة مما يعني أن التنسيق المشروط سيكون بمقياس ألوان ثلاثي افتراضيًا. ومع ذلك، سينتج تبديل خاصية ColorScale.Is3ColorScale إلى خطأ تنسيق مشروط بمقياس ألوان ثنائي.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook();

//Access the Worksheet to which conditional formatting rule has to be added

Worksheet sheet = book.getWorksheets().get(0);

//Add FormatConditions to the collection

int index = sheet.getConditionalFormattings().add();

//Access newly added formatConditionCollection via its index

FormatConditionCollection formatConditionCollection = sheet.getConditionalFormattings().get(index);

//Create a CellArea on which conditional formatting rule will be applied

CellArea cellArea = CellArea.createCellArea("A1", "A5");

//Add conditional formatted cell range

formatConditionCollection.addArea(cellArea);

//Add format condition of type ColorScale

index = formatConditionCollection.addCondition(FormatConditionType.COLOR_SCALE);

//Access newly added format condition via its index

FormatCondition formatCondition = formatConditionCollection.get(index);

//Set Is3ColorScale to false in order to generate a 2-Color Scale format

formatCondition.getColorScale().setIs3ColorScale(false);

//Set other necessary properties

{{< /highlight >}}
### **تمت إضافة خاصية TxtLoadOptions.HasFormula.**
قدمت Aspose.Cells for Java 8.7.0 دعمًا لتحديد وتحليل الصيغ أثناء تحميل ملفات CSV/TXT التي تحتوي على بيانات نصية محددة. يوجّه الخيار الجديد TxtLoadOptions.HasFormula الواجهة إلى تحليل الصيغ من الملف المحدد الذي تم إدخاله وتعيينها للخلايا ذات الصلة دون الحاجة إلى أي معالجة إضافية.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

 //Create an instance of TxtLoadOptions

TxtLoadOptions options = new TxtLoadOptions();

//Set HasFormula property to true

options.setHasFormula(true);

//Set the Separator property as desired

options.setSeparator(',');

//Load the CSV/TXT file using the instance of TxtLoadOptions

Workbook book = new Workbook(inFilePath, options);

//Calculate formulas in order to get the calculated values of formula in CSV

book.calculateFormula();

//Write result in any of the supported formats

book.save(outFilePath);

{{< /highlight >}}
### **تمت إضافة خاصية DataLabels.ResizeShapeToFitText.**
ميزة مفيدة أخرى قد قدمتها Aspose.Cells for Java 8.7.0 هي خاصية DataLabels.ResizeShapeToFitText التي يمكنها تمكين ميزة تعديل حجم الشكل ليلائم النص في تطبيق Excel لتسميات بيانات الرسم البياني.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook containing the Chart

Workbook book = new Workbook(inFilePath);

//Access the Worksheet that contains the Chart

Worksheet sheet = book.getWorksheets().get(0);

//Access the desired Chart via its index or name

Chart chart = sheet.getCharts().get(0);

//Access the DataLabels of desired NSeries

DataLabels labels = chart.getNSeries().get(0).getDataLabels();

//Set ResizeShapeToFitText property to true

labels.setResizeShapeToFitText(true);

//Calculate Chart

chart.calculate();

{{< /highlight >}}
## **تمت إزالة واجهات برمجة التطبيقات**
### **تمت إزالة خاصية Workbook.SaveOptions.**
تم وضع خاصية Workbook.SaveOptions على لائحة التشويه منذ فترة. مع هذا الإصدار، تمت إزالتها بالكامل من واجهة برمجة التطبيقات العامة لذلك يُنصح باستخدام طريقة Workbook.save(Stream, SaveOptions) أو Workbook.save(string, SaveOptions) كبديل.
{{< app/cells/assistant language="java" >}}
