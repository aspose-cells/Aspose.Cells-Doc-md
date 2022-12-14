---
title: عام API تغييرات في Aspose.Cells 16.12.0
type: docs
weight: 360
url: /ar/net/public-api-changes-in-aspose-cells-16-12-0/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 16.11.0 إلى 16.12.0 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة والمحذوفة وما إلى ذلك ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **تصفية الكائنات في وقت التحميل**
كشف Aspose.Cells 16.12.0 عن فئة LoadFilter مع خاصية LoadOptions.LoadFilter التي يمكنها معًا التحكم في نوع البيانات التي سيتم تحميلها أثناء تهيئة مثيل مصنف من ملف قالب.

فيما يلي سيناريو استخدام بسيط لتحميل خصائص المستند فقط من ملف قالب.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class

// Select to load document properties by passing LoadDataFilterOptions.DocumentProperties to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.DocumentProperties);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



المقتطف التالي يقوم بتحميل كل شيء من جدول بيانات موجود باستثناء الرسوم البيانية.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to the constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.All & ~Aspose.Cells.LoadDataFilterOptions.Chart);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



يؤدي اتباع التعليمات البرمجية إلى تحميل بيانات الخلية فقط (جنبًا إلى جنب مع الصيغ) والتنسيق من جدول بيانات موجود.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.CellData);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



تسمح فئة LoadFilter أيضًا بتخصيص عملية التحميل وفقًا لخصائص ورقة العمل. من أجل تخصيص عملية التحميل وفقًا لورقة العمل ، يتعين على المرء تجاوز طريقة LoadFilter.StartSheet كما هو موضح أدناه.

**C#**

{{< highlight "csharp" >}}

 class CustomFilter : Aspose.Cells.LoadFilter

{

    public override void StartSheet(Worksheet sheet)

    {

        if (sheet.Name == "Sheet1")

        {

            // Load everything

            m_LoadDataFilterOptions = Aspose.Cells.LoadDataFilterOptions.All;

        }

        else

        {

            // Load nothing

            m_LoadDataFilterOptions = Aspose.Cells.LoadDataFilterOptions.None;

        }

    }

}

{{< /highlight >}}



يستخدم المقتطف التالي فئة CustomFilter المحددة أعلاه.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of CustomFilter class

options.LoadFilter = new CustomFilter();

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}


### **تمت إضافة تعداد FileFormatType.OTS**
أضاف Aspose.Cells 16.12.0 إدخال OTS إلى تعداد FileFormatType لاكتشاف تنسيق ملفات OTS.

المقتطف التالي يستخدم FileFormatType.OTS.

**C#**

{{< highlight "csharp" >}}

 // Load a sample in an instance of FileStream

var stream = File.OpenRead(dir + "sample.ots");

// Detect the format of the stream

var fileFormatInfo = Aspose.Cells.FileFormatUtil.DetectFileFormat(stream);



// Check if stream is of type OTS

Debug.Assert(fileFormatInfo.FileFormatType == FileFormatType.OTS);

{{< /highlight >}}


### **تمت إضافة خاصية FontConfigs.PreferSystemFontSubstitutes**
كشف Aspose.Cells 16.12.0 الخاصية PreferSystemFontSubstitutes لفئة FontConfigs. تعتبر الخاصية FontConfigs.PreferSystemFontSubstitutes من النوع Boolean ، مما يشير إلى ما إذا كان يجب أن يستخدم API آلية استبدال خط النظام أولاً ، في حالة عدم وجود الخط المطلوب ولم يتم تحديد أي بديل للخط المعين. القيمة الافتراضية لخاصية FontConfigs.PreferSystemFontSubstitutes هي false.
### **تمت إضافة خاصية BuiltInDocumentPropertyCollection.ScaleCrop**
قام Aspose.Cells 16.12.0 بإضافة خاصية ScaleCrop إلى فئة BuiltInDocumentPropertyCollection. يشير ScaleCrop إلى وضع عرض مصغر المستند. يتيح ضبط هذا العنصر على "صواب" قياس الصورة المصغرة للمستند حسب العرض بينما يتيح تعيينه على "خطأ" إمكانية اقتصاص الصورة المصغرة للمستند لإظهار القسم الذي يناسب العرض.
### **تمت إضافة خاصية BuiltInDocumentPropertyCollection.LinksUpToDate**
قام Aspose.Cells 16.12.0 أيضًا بعرض خاصية LinksUpToDate لفئة BuiltInDocumentPropertyCollection. تشير الخاصية LinksUpToDate إلى ما إذا كانت الارتباطات التشعبية في مستند محدثة.
### **تمت إضافة طريقة Workbook.ExportXml**
كشف Aspose.Cells 16.12.0 عن طريقة Workbook.ExportXml التي تسمح بتخزين بيانات مخطط XML إلى مسار الملف المحدد. يقبل الأسلوب Workbook.ExportXml معلمتين حيث يجب أن تكون المعلمة الأولى من سلسلة النوع اسم مخطط XML والمعلمة الثانية يجب أن تكون موقع مسار الملف لتخزين بيانات XML.
### **تمت إضافة WorksheetCollection.CreateRange**
أضاف Aspose.Cells 16.12.0 طريقة WorksheetCollection.CreateRange التي تسمح بإنشاء نطاق بناءً على العنوان (مرجع منطقة الخلية) وفهرس ورقة العمل.

يستخدم المقتطف التالي طريقة WorksheetCollection.CreateRange لإنشاء نطاق من الخلايا يمتد عبر A1 إلى A2 في ورقة العمل الأولى (الافتراضية).

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook

var book = new Aspose.Cells.Workbook();

// Access WorksheetCollection from the Workbook

var sheets = book.Worksheets;



// Create a range in first worksheet

var range = sheets.CreateRange("A1:A2", 0);

{{< /highlight >}}
## **واجهات برمجة التطبيقات التي عفا عليها الزمن**
### **خاصية LoadOptions.LoadDataOptions التي عفا عليها الزمن**
الرجاء استخدام خاصية LoadOptions.LoadFilter كبديل.
### **خاصية LoadOptions.LoadDataFilterOptions التي عفا عليها الزمن**
الرجاء استخدام خاصية LoadOptions.LoadFilter بدلاً من ذلك.
### **خاصية LoadOptions.OnlyLoadDocumentProperties قديمة**
الرجاء استخدام خاصية LoadOptions.LoadFilter كبديل.
### **خاصية LoadOptions.LoadDataAndFormatting قديمة**
الرجاء استخدام خاصية LoadOptions.LoadFilter بدلاً من ذلك.

{{% alert color="primary" %}} 

تمت مشاركة مقتطفات التعليمات البرمجية لجميع واجهات برمجة التطبيقات القديمة أعلاه.

{{% /alert %}}
## **واجهات برمجة التطبيقات المحذوفة**
### **DataLabels المحذوفة. خاصية الدوران**
الرجاء استخدام خاصية DataLabels.RotationAngle بدلاً من ذلك.
### **عنوان محذوف. خاصية الدوران**
يرجى استخدام خاصية Title.RotationAngle كبديل.
### **تم حذف خاصية DataLabels.Background**
يُنصح باستخدام الخاصية DataLabels.BackgroundMode بدلاً من ذلك.
### **تم حذف خاصية DisplayUnitLabel.Rotation**
يرجى التفكير في استخدام خاصية DisplayUnitLabel.RotationAngle لتحقيق نفس الهدف.
