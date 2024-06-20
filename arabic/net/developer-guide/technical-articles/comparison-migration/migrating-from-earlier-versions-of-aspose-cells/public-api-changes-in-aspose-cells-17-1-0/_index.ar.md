---
title: تغييرات الواجهة البرمجية العامة في Aspose.Cells 17.1.0
type: docs
weight: 370
url: /ar/net/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

تصف هذه الوثيقة التغييرات في واجهة برمجة تطبيقات Aspose.Cells من الإصدار 16.12.0 إلى 17.1.0 التي قد تكون مثيرة لاهتمام مطوري الوحدات/التطبيقات. تتضمن ليس فقط الطرق العامة الجديدة والمحدثة والطرق العامة التي تمت إضافتها وإزالتها وتغيير الفصول الخلفية في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **الدعم لرسوم بيانية Excel 2016**
لقد أضافت واجهات برنامج التطبيقات Aspose.Cells دعم بضع رسوم بيانية لبرنامج Excel 2016 عن طريق تعزيز تعداد الرسم البياني. تمت إضافة الحقول الجديدة التالية مع إصدار Aspose.Cells 17.1.0.

- ChartType.BoxWhisker: يتم توزيع السلسلة كمربع وخطوط.
- ChartType.Funnel: يتم توزيع السلسلة كمهرجان.
- ChartType.ParetoLine: يتم توزيع السلسلة كخطوط باريتو.
- ChartType.Sunburst: يتم توزيع السلسلة كنجمة.
- نوع الرسم البياني.الخريطة الحرارية: تم تخطيط السلسلة كخريطة حرارية.
- نوع الرسم البياني.الشلال: تم تخطيط السلسلة كشلال.
- نوع الرسم البياني.التوزيع التكراري: تم تخطيط السلسلة كتوزيع تكراري.

{{% alert color="primary" %}} 

تحقق من المقال المفصل حول [قراءة أنواع رسومات Excel 2016](/cells/ar/net/read-and-manipulate-excel-2016-charts/)

{{% /alert %}} 
### **تمت إضافة Setter لخاصية LoadFilter.LoadDataFilterOptions.**
لقد أضاف Aspose.Cells 17.1.0 Setter لخاصية LoadFilter.LoadDataFilterOptions لاستبدال المتغير المثيل m_LoadDataFilterOptions. قد يقوم المستخدمون بتغيير خاصية LoadDataFilterOptions في تنفيذهم الخاص لفئة LoadFilter لتغيير سلوك تحميل ملفات القالب.

فيما يلي سيناريو استخدام بسيط.

{{% alert color="primary" %}} 

تحقق من المقال المفصل حول [تصفية القوالب المخصصة](/cells/ar/net/filter-objects-while-loading-workbook-or-worksheet/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 class CustomFilter : Aspose.Cells.LoadFilter

{

    public override void StartSheet(Worksheet sheet)

    {

        if (sheet.Name == "Sheet1")

        {

            // Load everything

            this.LoadDataFilterOptions = LoadDataFilterOptions.All;

        }

        else

        {

            // Load nothing

            this.LoadDataFilterOptions = LoadDataFilterOptions.None;

        }

    }

}

{{< /highlight >}}


### **تمت إضافة خاصية SignificantDigits في CellsHelper**
أضاف Aspose.Cells 17.1.0 خاصية SignificantDigits من فئة CellsHelper والتي تسمح بالحصول على عدد الأرقام الكبيرة أو تعيينها لقيم رقمية في ورقة البيانات. القيمة الافتراضية لخاصية CellsHelper.SignificantDigits هي 17 وذلك فقط إذا كان ينطبق تخزين النتيجة في تنسيق ملف XLSX.

إليك سيناريو بسيط لتوضيح استخدام خاصية CellsHelper.SignificantDigits

{{% alert color="primary" %}} 

تحقق من المقال المفصل حول [ضبط عدد الأرقام البارزة](/cells/ar/net/specifying-significant-digits-to-be-stored-in-excel-file/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Specify the number of significant digits

CellsHelper.SignificantDigits = 15;

{{< /highlight >}}


### **تمت إضافة خاصية Color في GlowEffect**
أضاف Aspose.Cells 17.1.0 خاصية Color في GlowEffect والتي يمكن استخدامها لاسترداد لون تأثير اللمعان.

تستخدم القصاصة التالية خاصية Color في GlowEffect

{{% alert color="primary" %}} 

تحقق من المقال المفصل حول [قراءة لون تأثير التوهج في الشكل](/cells/ar/net/read-color-of-shape-s-glow-effect/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Read the source excel file

var book = new Workbook(dir + "sample.xlsx");

// Access first worksheet

var sheet = book.Worksheets[0];

// Access the first shape

var shape = sheet.Shapes[0];

// Read the glow effect color

var glow = shape.Glow;

var color = glow.Color;

{{< /highlight >}}


### **تمت إضافة خصائص PaperWidth و PaperHeight في PageSetup**
أضاف Aspose.Cells 17.1.0 الخصائص PaperWidth و PaperHeight لفئة PageSetup. تُمثل خصائص PageSetup.PaperWidth و PageSetup.PaperHeight نوع double تمثل عرض وارتفاع الورق بوحدة البوصة مع مراعاة توجيه الصفحة.

{{% alert color="primary" %}} 

تحقق من المقال المفصل حول [استرداد حجم الورق لورقة العمل](/cells/ar/net/get-paper-width-and-height-of-page-setup-of-worksheet/)

{{% /alert %}} 
### **تمت إضافة خاصية CheckCustomNumberFormat في WorkbookSettings**
أضاف Aspose.Cells 17.1.0 خاصية CheckCustomNumberFormat لفئة WorkbookSettings. CheckCustomNumberFormat مفيدة في التحقق مما إذا تم تعيين خاصية Style.Custom بشكل صحيح أم لا. في حالة تم تعيين خاصية Style.Custom بشكل غير صحيح، أي بأن القيمة لا تتوافق مع النمط الصحيح ثم ستقوم واجهات برمجة التطبيقات لـ Aspose.Cells برمي CellsException مع رسالة مناسبة.

{{% alert color="primary" %}} 

يرجى التحقق من المقال المفصل حول [التحقق من التنسيق المخصص](/cells/ar/net/check-custom-number-format-when-setting-style-custom-property/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Workbook();

// Set CheckCustomNumberFormat property to true

book.Settings.CheckCustomNumberFormat = true;

// Access first worksheet

var sheet = book.Worksheets[0];

// Access a cell

var cell = sheet.Cells["B5"];

// Insert a value to the cell

cell.PutValue(2347);

// Access cell's style

Style style = cell.GetStyle();



// Set Custom property to an invalid pattern

style.Custom = "ggg @ fff";

// Set the modified style to the cell

cell.SetStyle(style);

{{< /highlight >}}


### **تمت إضافة حقل DisplayUnitType.Percentage**
حصلت Aspose.Cells 17.1.0 أيضًا على تعريض حقل النسبة الى تعداد DisplayUnitType. يشير حقل DisplayUnitType.Percentage إلى أن القيم على الرسم البياني ستتم قسمتها على 0.01.
## **تمت إزالة واجهات برمجة التطبيقات**
### **تمت إزالة المتغير المثيل m_LoadDataFilterOptions**
تمت إزالة المتغير المثيل m_LoadDataFilterOptions في هذا الإصدار. من المستحسن استخدام خاصية LoadFilter.LoadDataFilterOptions بدلاً من ذلك.
