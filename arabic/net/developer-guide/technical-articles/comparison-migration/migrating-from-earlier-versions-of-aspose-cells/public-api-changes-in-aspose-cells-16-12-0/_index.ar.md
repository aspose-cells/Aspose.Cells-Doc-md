---
title: التغييرات العامة في واجهة برمجة التطبيقات العامة في Aspose.Cells 16.12.0
type: docs
weight: 360
url: /ar/net/public-api-changes-in-aspose-cells-16-12-0/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات لـ Aspose.Cells من الإصدار 16.11.0 إلى 16.12.0 التي قد تكون مهمة لمطوري الوحدات/التطبيقات. وتشمل ليس فقط الطرق العامة الجديدة والمحدثة، والفئات المضافة والمحذوفة وما إلى ذلك، ولكن أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **تصفية الكائنات أثناء وقت التحميل**
أصبح Aspose.Cells 16.12.0 يكشف فئة LoadFilter جنبًا إلى جنب مع خاصية LoadOptions.LoadFilter التي يمكنها معًا التحكم في نوع البيانات المراد تحميلها أثناء تهيئة نسخة من Workbook من ملف قالب.

إليك سيناريو استخدام بسيط لتحميل خصائص المستند فقط من ملف قالب.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class

// Select to load document properties by passing LoadDataFilterOptions.DocumentProperties to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.DocumentProperties);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



الكود التالي يقوم بتحميل كل شيء من جدول بيانات موجود باستثناء الرسوم البيانية.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to the constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.All & ~Aspose.Cells.LoadDataFilterOptions.Chart);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



الكود التالي يقوم بتحميل بيانات الخلية فقط (بالإضافة إلى الصيغ) والتنسيق من جدول بيانات موجود.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.CellData);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



تتيح فئة LoadFilter أيضاً تخصيص عملية التحميل وفقًا لخصائص ورقة العمل. لتخصيص عملية التحميل وفقًا لورقة العمل، يجب على الشخص تعيين طريقة LoadFilter.StartSheet كما هو موضح أدناه.

**C#**

{{< highlight csharp >}}

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



يستخدم كود التالي فئة CustomFilter المحددة أعلاه.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of CustomFilter class

options.LoadFilter = new CustomFilter();

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}


### **تمت إضافة عنصر FileFormatType.OTS إلى التعداد**
أصبح Aspose.Cells 16.12.0 يضيف مدخل OTS إلى تعداد FileFormatType من أجل كشف تنسيق ملفات OTS.

الكود التالي يستخدم FileFormatType.OTS.

**C#**

{{< highlight csharp >}}

 // Load a sample in an instance of FileStream

var stream = File.OpenRead(dir + "sample.ots");

// Detect the format of the stream

var fileFormatInfo = Aspose.Cells.FileFormatUtil.DetectFileFormat(stream);



// Check if stream is of type OTS

Debug.Assert(fileFormatInfo.FileFormatType == FileFormatType.OTS);

{{< /highlight >}}


### **تمت إضافة خاصية FontConfigs.PreferSystemFontSubstitutes.**
أضيف في Aspose.Cells 16.12.0 خاصية PreferSystemFontSubstitutes لفئة FontConfigs. تعتبر خاصية FontConfigs.PreferSystemFontSubstitutes من نوع Boolean، مشيرة إلى ما إذا كان يجب على واجهة برمجة التطبيقات استخدام آلية استبدال الخطوط النظامية أولاً في حالة عدم وجود الخط المطلوب وعدم تعريف استبدال للخط المعين. القيمة الافتراضية لخاصية FontConfigs.PreferSystemFontSubstitutes هي خاطئة (false).
### **تمت إضافة خاصية BuiltInDocumentPropertyCollection.ScaleCrop**
أصبح Aspose.Cells 16.12.0 يضيف خاصية ScaleCrop إلى فئة BuiltInDocumentPropertyCollection. تُشير ScaleCrop إلى وضع عرض مصغر المستند. يمكن ضبط هذا العنصر على true لتمكين تحجيم مصغر المستند وفقًا للعرض، بينما يمكن ضبطه على false لتمكين قص مصغر المستند لعرض الجزء الذي يناسب العرض.
### **تمت إضافة خاصية BuiltInDocumentPropertyCollection.LinksUpToDate**
أصبح Aspose.Cells 16.12.0 يكشف أيضًا خاصية LinksUpToDate لفئة BuiltInDocumentPropertyCollection. تُشير خاصية LinksUpToDate ما إذا كانت الروابط الفائقة في مستند محدّثة.
### **تمت إضافة أسلوب Workbook.ExportXml.**
قامت Aspose.Cells 16.12.0 بتعريض طريقة Workbook.ExportXml التي تسمح بتخزين بيانات خريطة XML إلى مسار محدد. تقبل طريقة Workbook.ExportXml 2 معامل حيث يجب أن يكون المعامل الأول من نوع string هو اسم خريطة XML ويجب أن يكون المعامل الثاني موقع مسار الملف لتخزين بيانات XML.
### **تمت إضافة أسلوب WorksheetCollection.CreateRange.**
قامت Aspose.Cells 16.12.0 بإضافة طريقة WorksheetCollection.CreateRange التي تسمح بإنشاء نطاق بناءً على عنوان (مرجع منطقة الخلية) وفهرس الورقة.

يستخدم المقتطف التالي أسلوب WorksheetCollection.CreateRange لإنشاء نطاق من الخلايا يمتد من A1 إلى A2 في الورقة الأولى (الافتراضية).

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Aspose.Cells.Workbook();

// Access WorksheetCollection from the Workbook

var sheets = book.Worksheets;



// Create a range in first worksheet

var range = sheets.CreateRange("A1:A2", 0);

{{< /highlight >}}
## **واجهات برمجة التطبيق القديمة**
### **خاصية Obsoleted LoadOptions.LoadDataOptions**
الرجاء استخدام خاصية LoadOptions.LoadFilter كبديل.
### **خاصية Obsoleted LoadOptions.LoadDataFilterOptions**
الرجاء استخدام خاصية LoadOptions.LoadFilter بدلاً منها.
### **خاصية Obsoleted LoadOptions.OnlyLoadDocumentProperties**
الرجاء استخدام خاصية LoadOptions.LoadFilter كبديل.
### **خاصية Obsoleted LoadOptions.LoadDataAndFormatting**
الرجاء استخدام خاصية LoadOptions.LoadFilter بدلاً منها.

{{% alert color="primary" %}} 

تم مشاركة مقاطع الشفرة لجميع واجهات برمجة التطبيقات المهجورة أعلاه.

{{% /alert %}}
## **حذف واجهات برمجة التطبيق**
### **خاصية محذوفة DataLabels.Rotation**
الرجاء استخدام خاصية DataLabels.RotationAngle بدلاً منها.
### **خاصية محذوفة Title.Rotation**
الرجاء استخدام خاصية Title.RotationAngle كبديل.
### **خاصية محذوفة DataLabels.Background**
من المستحسن استخدام خاصية DataLabels.BackgroundMode بدلاً منها.
### **خاصية محذوفة DisplayUnitLabel.Rotation**
يرجى النظر في استخدام خاصية DisplayUnitLabel.RotationAngle لتحقيق نفس الهدف.
