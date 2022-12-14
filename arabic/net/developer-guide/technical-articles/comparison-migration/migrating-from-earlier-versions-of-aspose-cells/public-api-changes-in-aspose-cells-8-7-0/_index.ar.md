---
title: API العام التغييرات في Aspose.Cells 8.7.0
type: docs
weight: 230
url: /ar/net/public-api-changes-in-aspose-cells-8-7-0/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.6.3 إلى 8.7.0 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة والمحذوفة وما إلى ذلك ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **دعم التوقيع الرقمي والكشف والاستخراج لمشروع VBA**
كشف هذا الإصدار من Aspose.Cells for .NET عن بعض الخصائص والطرق الجديدة لمساعدة المستخدمين في مهام مثل التوقيع رقميًا على مشروع VBA ، واكتشاف ما إذا كان مشروع VBA موقّعًا وصالحًا. علاوة على ذلك ، يسمح API الجديد باستخراج الشهادة كبيانات أولية من مشروع VBA الموقع رقميًا في Workbook.
###### **توقيع مشروع VBA رقميًا**
 كشف Aspose.Cells for .NET 8.7.0 عن طريقة VbaProject.Sign التي يمكن استخدامها[التوقيع رقميًا على مشروع VBA في مصنف](/cells/ar/net/digitally-sign-a-vba-code-project-with-certificate/). تقبل الطريقة المذكورة مثيلًا لفئة التوقيع الرقمي الموجود في مساحة الاسم Aspose.Cells.DigitalSignatures.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Sign the VbaProject using the X509Certificate

vbaProject.Sign(new DigitalSignature(new System.Security.Cryptography.X509Certificates.X509Certificate2(cert), "Comments", DateTime.Now));

{{< /highlight >}}


###### **الكشف عن مشروع VBA الموقع رقميًا**
 يمكن استخدام الخاصية VbaProject.IsSigned المكشوفة حديثًا في ملفات[اكتشاف ما إذا كان مشروع VBA في مصنف تم توقيعه رقميًا](/cells/ar/net/check-if-vba-code-is-signed/). الخاصية VbaProject.IsSigned هي من النوع Boolean ، والتي ترجع صحيحًا إذا تم توقيع مشروع VBA رقميًا والعكس صحيح.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Check if VbaProject is digitally signed

if (vbaProject.IsSigned)

{

    Console.WriteLine("VbaProject is digitally signed");

}

else

{

    Console.WriteLine("VbaProject is not digitally signed");

}

{{< /highlight >}}


###### **استخراج التوقيع الرقمي من مشروع VBA**
كشفت هذه المراجعة لـ API أيضًا عن خاصية VbaProject.CertRawData التي تسمح[استخراج البيانات الأولية للشهادة الرقمية من مشروع VBA](/cells/ar/net/export-vba-certificate-to-file-or-stream/). الخاصية VbaProject.CertRawData هي من نوع صفيف بايت ، والتي ستحتوي على بيانات الشهادة الأولية إذا كان مشروع VBA موقعًا رقميًا ، وإلا ستكون الخاصية المذكورة فارغة.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Extract digital signature in an array of bytes

var cert = vbaProject.CertRawData;

{{< /highlight >}}


###### **تحقق من صحة التوقيع الرقمي لمشروع VBA**
 إضافة أخرى إلى API العام هي خاصية VbaProject.IsValidSigned التي يمكن أن تكون مفيدة في[التحقق من صحة التوقيع الرقمي لمشروع VBA](/cells/ar/net/check-if-digital-signature-of-vba-code-is-valid/). تعود الخاصية المذكورة صحيحة إذا كان التوقيع الرقمي صحيحًا وخطأ إذا كان التوقيع غير صالح.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Check if VbaProject is digitally signed

if (vbaProject.IsSigned)

{

    //Check if signature is valid

    if (vbaProject.IsValidSigned)

    {

        Console.WriteLine("VbaProject is digitally signed & signature is valid");

    }

}

{{< /highlight >}}


### **حماية الطريقة**
 كشف Aspose.Cells for .NET 8.7.0 عن طريقة الحماية. VerifyPassword التي يمكن استخدامها[تحقق من كلمة المرور المستخدمة لحماية ورقة العمل](/cells/ar/net/verify-password-used-to-protect-the-worksheet/)يقبل هذا الأسلوب مثيلاً من السلسلة كمعامل ويعيد صحيحًا إذا تطابق كلمة المرور المحددة مع كلمة المرور المستخدمة لحماية ورقة العمل.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the desired Worksheet via its index or name

var sheet = book.Worksheets[0];

//Access Protection module of desired Worksheet

var protection = sheet.Protection;

//Verify the password for Worksheet

if (protection.VerifyPassword(password))

{

    Console.WriteLine("Password has matched");

}

else

{

    Console.WriteLine("Password did not match");

}

{{< /highlight >}}


### **حماية الملكية. حماية مع كلمة المرور المضافة**
 كشف هذا الإصدار من Aspose.Cells for .NET API أيضًا عن خاصية Protection.IsProtectedWithPassword التي يمكن أن تكون مفيدة في[الكشف عما إذا كانت ورقة العمل محمية بكلمة مرور أم لا](/cells/ar/net/detect-if-worksheet-is-password-protected/).

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the desired Worksheet via its index or name

var sheet = book.Worksheets[0];

//Access Protection module of desired Worksheet

var protection = sheet.Protection;

//Check if Worksheet is password protected

if (protection.IsProtectedWithPassword)

{

    Console.WriteLine("Worksheet is password protected");

}

else

{

    Console.WriteLine("Worksheet is not password protected");

}

{{< /highlight >}}


### **تمت إضافة خاصية ColorScale.Is3ColorScale**
 كشف Aspose.Cells for .NET 8.7.0 الخاصية ColorScale.Is3ColorScale التي يمكن استخدامها لإنشاء نسق شرطي لمقياس اللون 2. الخاصية المذكورة هي من النوع Boolean مع القيمة الافتراضية لـ true مما يعني أن التنسيق الشرطي سيكون من 3-Color Scale افتراضيًا. ومع ذلك ، تبديل الخاصية ColorScale.Is3ColorScale إلى false will[إنشاء تنسيق شرطي 2-Color Scale](/cells/ar/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/).

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access the Worksheet to which conditional formatting rule has to be added

var sheet = book.Worksheets[0];

//Add FormatConditions to the collection

int index = sheet.ConditionalFormattings.Add();

//Access newly added formatConditionCollection via its index

var formatConditionCollection = sheet.ConditionalFormattings[index];

//Create a CellArea on which conditional formatting rule will be applied

var cellArea = CellArea.CreateCellArea("A1", "A5");

//Add conditional formatted cell range

formatConditionCollection.AddArea(cellArea);

//Add format condition of type ColorScale

index = formatConditionCollection.AddCondition(FormatConditionType.ColorScale);

//Access newly added format condition via its index

var formatCondition = formatConditionCollection[index];

//Set Is3ColorScale to false in order to generate a 2-Color Scale format

formatCondition.ColorScale.Is3ColorScale = false;

//Set other necessary properties

{{< /highlight >}}


### **تمت إضافة الخاصية TxtLoadOptions.HasFormula**
 Aspose.Cells for .NET 8.7.0 قدم دعمًا لـ[تحديد الصيغ وتحليلها أثناء تحميل ملفات CSV / TXT التي تحتوي على بيانات عادية محددة](/cells/ar/net/load-or-import-csv-file-with-formulas/). تعرض خاصية TxtLoadOptions.HasFormula المكشوفة حديثًا عند ضبطها على true توجه API لتحليل الصيغ من ملف الإدخال المحدد وتعيينها على الخلايا ذات الصلة دون الحاجة إلى أي معالجة إضافية.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of TxtLoadOptions

var options = new TxtLoadOptions();

//Set HasFormula property to true

options.HasFormula = true;

//Set the Separator property as desired

options.Separator = ',';

//Load the CSV/TXT file using the instance of TxtLoadOptions

var book = new Workbook(inFilePath, options);

//Calculate formulas in order to get the calculated values of formula in CSV

book.CalculateFormula();

//Write result in any of the supported formats

book.Save(outFilePath);

{{< /highlight >}}


### **تمت إضافة خاصية DataLabels.IsResizeShapeToFitText**
 ميزة مفيدة أخرى كشفها Aspose.Cells for .NET 8.7.0 هي خاصية DataLabels.IsResizeShapeToFitText التي يمكنها تمكين[تغيير حجم الشكل لاحتواء النص](/cells/ar/net/resize-chart-s-data-label-shape-to-fit-text/) ميزة تطبيق Excel لتسميات بيانات الرسم البياني.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook containing the Chart

var book = new Workbook(inFilePath);

//Access the Worksheet that contains the Chart

var sheet = book.Worksheets[0];

//Access the desired Chart via its index or name

var chart = sheet.Charts[0];

//Access the DataLabels of desired NSeries

var labels = chart.NSeries[0].DataLabels;

//Set ResizeShapeToFitText property to true

labels.IsResizeShapeToFitText = true;

//Calculate Chart

chart.Calculate();

{{< /highlight >}}


### **تمت إضافة خاصية PdfSaveOptions.OptimizationType**
كشف Aspose.Cells for .NET 8.7.0 خاصية PdfSaveOptions.OptimizationType جنبًا إلى جنب مع تعداد PdfOptimizationType من أجل تسهيل قيام المستخدمين[اختر خوارزمية التحسين المطلوبة أثناء تصدير جداول البيانات إلى تنسيق PDF](/cells/ar/net/save-excel-into-pdf-with-standard-or-minimum-size/). هناك قيمتان محتملتان لخاصية PdfSaveOptions.OptimizationType كما هو مفصل أدناه.

1. PdfOptimizationType.MinimumSize: يتم اختراق الجودة لحجم الملف الناتج.
1. PdfOptimizationType.Standard: الجودة غير معرضة للخطر لذا سيكون حجم الملف الناتج كبيرًا.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of PdfSaveOptions

var pdfSaveOptions = new PdfSaveOptions();

//Set the OptimizationType property to desired value

pdfSaveOptions.OptimizationType = PdfOptimizationType.MinimumSize;

//Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook(inFilePath);

//Save the spreadsheet in PDF format while passing the instance of PdfSaveOptions

book.Save(outFilePath, pdfSaveOptions);

{{< /highlight >}}
## **إزالة واجهات برمجة التطبيقات**
### **مصنف الخاصية تمت إزالة خيارات الحفظ**
تم وضع علامة على الخاصية Workbook.SaveOptions قديمة بعض الوقت. مع هذا الإصدار ، تمت إزالته تمامًا من API العام ، لذلك يُنصح باستخدام Workbook.Save (Stream ، SaveOptions) أو Workbook.Save (string ، SaveOptions) كبديل.
