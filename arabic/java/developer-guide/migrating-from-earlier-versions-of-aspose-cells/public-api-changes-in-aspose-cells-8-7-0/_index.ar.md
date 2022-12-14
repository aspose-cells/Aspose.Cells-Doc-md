---
title: API العام التغييرات في Aspose.Cells 8.7.0
type: docs
weight: 240
url: /ar/java/public-api-changes-in-aspose-cells-8-7-0/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.6.3 إلى 8.7.0 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة والمحذوفة وما إلى ذلك ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **دعم لتحسين PDF**
 توفر واجهات برمجة التطبيقات Aspose.Cells بالفعل ميزة تحويل جداول البيانات إلى PDF. مع هذا الإصدار من API ، يمكن للمستخدمين الآن[تحسين حجم PDF الناتج](/cells/ar/java/save-excel-into-pdf-with-standard-or-minimum-size/)كذلك. كشف Aspose.Cells for Java 8.7.0 خاصية PdfSaveOptions.OptimizationType جنبًا إلى جنب مع تعداد PdfOptimizationType من أجل تسهيل اختيار خوارزمية التحسين المطلوبة للمستخدمين أثناء تصدير جداول البيانات إلى تنسيق PDF. هناك قيمتان محتملتان لخاصية PdfSaveOptions.OptimizationType كما هو مفصل أدناه.

1. PdfOptimizationType.MINIMUM_SIZE: يتم اختراق الجودة لحجم الملف الناتج.
1. PdfOptimizationType.STANDARD: لا يتم المساس بالجودة لذا سيكون حجم الملف الناتج كبيرًا.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

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
### **الكشف عن مشروع VBA الموقع رقميًا**
 يمكن استخدام خاصية VbaProject.isSigned المكشوفة حديثًا في ملفات[اكتشاف ما إذا كان مشروع VBA في مصنف تم توقيعه رقميًا](/cells/ar/java/check-if-vba-code-is-signed/). الخاصية VbaProject.isSigned هي من النوع Boolean ، والتي ترجع صحيحًا إذا تم توقيع مشروع VBA رقميًا والعكس صحيح.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

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
### **طريقة الحماية**
عززت واجهات برمجة التطبيقات Aspose.Cells فئة الحماية من خلال إدخال طريقة التحقق من كلمة المرور التي تسمح بتحديد كلمة مرور كمثيل من السلسلة و[يتحقق من استخدام نفس كلمة المرور لحماية ورقة العمل](/cells/ar/java/verify-password-used-to-protect-the-worksheet/). تعيد طريقة Protection.verifyPassword صحيحًا إذا كانت كلمة المرور المحددة تتطابق مع كلمة المرور المستخدمة لحماية ورقة العمل المحددة ، و false إذا كانت كلمة المرور المحددة غير متطابقة. يستخدم الجزء التالي من التعليمات البرمجية طريقة Protection.verifyPassword جنبًا إلى جنب مع حقل Protection.isProtectedWithPassword لاكتشاف حماية كلمة المرور والتحقق من كلمة المرور.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

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
### **حماية الملكية. isProtectedWith تمت إضافة كلمة المرور**
 كشف هذا الإصدار من Aspose.Cells for Java أيضًا عن حقل Protection.isProtectedWithPassword الذي يمكن أن يكون مفيدًا في[الكشف عما إذا كانت ورقة العمل محمية بكلمة مرور أم لا](/cells/ar/java/detect-if-worksheet-is-password-protected/).

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

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
### **تمت إضافة خاصية ColorScale.Is3ColorScale**
 كشف Aspose.Cells for Java 8.7.0 خاصية ColorScale.Is3ColorScale التي يمكن استخدامها[إنشاء تنسيق شرطي 2-Color Scale](/cells/ar/java/adding-2-color-scale-and-3-color-scale-conditional-formattings/). الخاصية المذكورة هي من النوع Boolean مع القيمة الافتراضية لـ true مما يعني أن التنسيق الشرطي سيكون من 3-Color Scale افتراضيًا. ومع ذلك ، سيؤدي تبديل الخاصية ColorScale.Is3ColorScale إلى false إلى إنشاء تنسيق شرطي لـ 2-Color Scale.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

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
### **تمت إضافة الخاصية TxtLoadOptions.HasFormula**
 Aspose.Cells for Java 8.7.0 قدم دعمًا لـ[تحديد الصيغ وتحليلها أثناء تحميل ملفات CSV / TXT التي تحتوي على بيانات عادية محددة](/cells/ar/java/load-or-import-csv-file-with-formulas/). تعرض خاصية TxtLoadOptions.HasFormula المكشوفة حديثًا عند ضبطها على true توجه API لتحليل الصيغ من ملف الإدخال المحدد وتعيينها على الخلايا ذات الصلة دون الحاجة إلى أي معالجة إضافية.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

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
### **تمت إضافة خاصية DataLabels.ResizeShapeToFitText**
 ميزة أخرى مفيدة كشفها Aspose.Cells for Java 8.7.0 هي خاصية DataLabels.ResizeShapeToFitText التي يمكنها تمكين[تغيير حجم الشكل لاحتواء النص](/cells/ar/java/resize-chart-s-data-label-shape-to-fit-text/) ميزة تطبيق Excel لتسميات بيانات الرسم البياني.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

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
## **إزالة واجهات برمجة التطبيقات**
### **مصنف الخاصية تمت إزالة خيارات الحفظ**
تم وضع علامة على الخاصية Workbook.SaveOptions قديمة بعض الوقت. مع هذا الإصدار ، تمت إزالته تمامًا من API العام ، لذلك يُنصح باستخدام Workbook.save (Stream ، SaveOptions) أو Workbook.save (سلسلة ، SaveOptions) كطريقة بديلة.
