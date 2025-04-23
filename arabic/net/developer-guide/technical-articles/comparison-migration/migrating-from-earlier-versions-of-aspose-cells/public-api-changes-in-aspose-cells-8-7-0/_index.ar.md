---
title: تغييرات الواجهة البرمجية العامة في Aspose.Cells 8.7.0
type: docs
weight: 230
url: /ar/net/public-api-changes-in-aspose-cells-8-7-0/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات Aspose.Cells من الإصدار 8.6.3 إلى 8.7.0 التي قد تكون مثيرة لاهتمام لمطوري الوحدة/التطبيق. يتضمن ليس فقط الطرق الجديدة والمحدثة، الفئات المضافة والمحذوفة إلخ، ولكن أيضاً وصفاً لأي تغييرات في السلوك في الخلفية في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **دعم التوقيع الرقمي لمشروع VBA، الكشف واستخراجه**
لقد قدم هذا الإصدار من Aspose.Cells for .NET بعض الخصائص والطرق الجديدة لمساعدة المستخدمين في المهام مثل توقيع مشروع VBA بشكل رقمي، والكشف عما إذا كان مشروع VBA موقعًا وصالحًا. علاوةً على ذلك، تسمح الواجهة البرمجية الجديدة باستخراج الشهادة كبيانات خام من مشروع VBA موقع رقميًا في مصنف البيانات.
###### **توقيع مشروع VBA رقميًا**
الإصدار 8.7.0 من Aspose.Cells for .NET قد عرض طريقة VbaProject.Sign التي يمكن استخدامها لتوقيع المشروع VBA في مصنف بيانات. تقبل هذه الطريقة نموذج DigitalSignature الذي يقع في أسماء النطاقات Aspose.Cells.DigitalSignatures.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Sign the VbaProject using the X509Certificate

vbaProject.Sign(new DigitalSignature(new System.Security.Cryptography.X509Certificates.X509Certificate2(cert), "Comments", DateTime.Now));

{{< /highlight >}}


###### **كشف توقيع مشروع VBA بواسطة الأرقام**
يمكن استخدام خاصية VbaProject.IsSigned المعرضة حديثًا ل [اكتشاف ما إذا كان مشروع VBA في دفتر العمل تم توقيعه رقميًا](/cells/ar/net/check-if-vba-code-is-signed/). تعتبر خاصية VbaProject.IsSigned من نوع Boolean، والتي تعيد القيمة true إذا كان مشروع VBA موقعاً رقميًا والعكس صحيح.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

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
لقد عرضت هذه المراجعة من الواجهة البرمجية أيضًا خاصية VbaProject.CertRawData التي تسمح ب [استخراج البيانات الخام للشهادة الرقمية من مشروع VBA](/cells/ar/net/export-vba-certificate-to-file-or-stream/). خاصية VbaProject.CertRawData من نوع مصفوفة بايت، والتي ستحتوي على البيانات الخام للشهادة إذا كان مشروع VBA موقعاً رقميًا، وغير ذلك ستكون الخاصية المذكورة خالية.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Extract digital signature in an array of bytes

var cert = vbaProject.CertRawData;

{{< /highlight >}}


###### **التحقق من التوقيع الرقمي لمشروع VBA**
إضافة أخرى إلى واجهة برمجة التطبيقات العمومية هي خاصية VbaProject.IsValidSigned التي يمكن أن تكون مفيدة في [التحقق من توقيع المشروع VBA الرقمي](/cells/ar/net/check-if-digital-signature-of-vba-code-is-valid/). تعيد الخاصية المذكورة القيمة true إذا كان التوقيع الرقمي صالحًا وfalse إذا كان التوقيع غير صالح.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

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


### **أضيفت الطريقة Protection.VerifyPassword**
Aspose.Cells for .NET 8.7.0 قد عرضت الطريقة Protection.VerifyPassword التي يمكن استخدامها ل [التحقق من كلمة المرور المستخدمة لحماية ورقة العمل](/cells/ar/net/verify-password-used-to-protect-the-worksheet/). تقبل هذه الطريقة مثيلًا لسلسلة كمعلمة وتعيد القيمة true إذا كانت كلمة المرور المحددة تتطابق مع كلمة المرور المستخدمة لحماية ورقة العمل.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

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


### **أضيفت الخاصية Protection.IsProtectedWithPassword**
لقد عرضت هذه الإصدار من Aspose.Cells for .NET API أيضًا خاصية Protection.IsProtectedWithPassword التي يمكن أن تكون مفيدة في [الكشف عما إذا كانت ورقة العمل محمية بكلمة مرور أم لا](/cells/ar/net/detect-if-worksheet-is-password-protected/).

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

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


### **إضافة خاصية ColorScale.Is3ColorScale**
Aspose.Cells for .NET 8.7.0 قد عرضت الخاصية ColorScale.Is3ColorScale التي يمكن استخدامها لإنشاء تنسيق مشروط بمقياس اللون المزدوج. تعتبر الخاصية المذكورة من نوع Boolean بقيمة افتراضية لها قيمة true مما يعني أن التنسيق المشروط سيكون بمقياس اللون الثلاثي بشكل افتراضي. ومع ذلك، فإن تحويل خاصية ColorScale.Is3ColorScale إلى false سيقوم [بتوليد تنسيق مشروط بمقياس اللون المزدوج](/cells/ar/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/).

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

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


### **تمت إضافة خاصية TxtLoadOptions.HasFormula.**
Aspose.Cells for .NET 8.7.0 قدم الدعم ل [تحديد وتحليل الصيغ أثناء تحميل ملفات CSV/TXT التي تحتوي على بيانات عادية محددة](/cells/ar/net/load-or-import-csv-file-with-formulas/) المكشوفة. يوجد الآن خاصية TxtLoadOptions.HasFormula حيث يقوم التطبيق بتحليل الصيغ من الملف المحدد وتعيينها في الخلايا ذات الصلة دون الحاجة إلى أي معالجة إضافية.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

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
ميزة مفيدة أخرى قام Aspose.Cells for .NET 8.7.0 بتكشيفها هي خاصية DataLabels.IsResizeShapeToFitText التي يمكن أن تمكن ميزة [تغيير حجم الشكل لتناسب النص](/cells/ar/net/resize-chart-s-data-label-shape-to-fit-text/) لتطبيق Excel على تسميات بيانات الرسم البياني.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

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
قدم Aspose.Cells for .NET 8.7.0 خاصية PdfSaveOptions.OptimizationType بالإضافة إلى تعداد PdfOptimizationType من أجل تيسير عملية [اختيار خوارزمية التحسين المطلوبة أثناء تصدير جداول البيانات إلى تنسيق PDF](/cells/ar/net/save-excel-into-pdf-with-standard-or-minimum-size/). هناك قيمتان ممكنتان لخاصية PdfSaveOptions.OptimizationType كما هو مفصل أدناه.

١. PdfOptimizationType.MinimumSize: يتم التضحية بالجودة من أجل حجم الملف الناتج.
١. PdfOptimizationType.Standard: الجودة لا تتضحى لذلك حجم الملف الناتج سيكون كبيرًا.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

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
## **تمت إزالة واجهات برمجة التطبيقات**
### **تمت إزالة خاصية Workbook.SaveOptions**
تم تحديد خاصية Workbook.SaveOptions بأنها قديمة منذ فترة. ومع هذا الإصدار، تمت إزالتها بشكل كامل من الـ API العامة لذلك يُنصح باستخدام الطريقة Workbook.Save(Stream, SaveOptions) أو Workbook.Save(string, SaveOptions) كبديل.
{{< app/cells/assistant language="csharp" >}}
