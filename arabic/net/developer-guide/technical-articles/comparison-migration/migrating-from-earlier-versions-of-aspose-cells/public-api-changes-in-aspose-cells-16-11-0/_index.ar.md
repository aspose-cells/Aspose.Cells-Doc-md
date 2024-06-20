---
title: تغييرات واجهة برمجة التطبيقات العامة في Aspose.Cells 16.11.0
type: docs
weight: 350
url: /ar/net/public-api-changes-in-aspose-cells-16-11-0/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات (API) لـ Aspose.Cells من الإصدار 16.10.0 إلى الإصدار 16.11.0 التي قد تكون مثيرة لاهتمام مطوري النماذج / التطبيقات. يتضمن ليس فقط الأساليب الجديدة والمحدثة العامة والفئات المضافة والمحذوفة إلخ، بل وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells أيضًا.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **دعم إعدادات العولمة**
أصدر Aspose.Cells 16.11.0 فئة GlobalizationSettings إلى جانب خاصية WorkbookSettings.GlobalizationSettings لفرض استخدام واجهات برمجة التطبيقات لـ Aspose.Cells لاستخدام تسميات مخصصة لإجمالي الأرقام الفرعية. تحتوي فئة GlobalizationSettings على الطرق التالية التي يمكن استبدالها في التنفيذ المخصص لإعطاء أسماء مرغوبة للتسميات **الإجمالي** و**الإجمالي الكلي**.

- GlobalizationSettings.GetTotalName: يحصل على اسم المجموع.
- GlobalizationSettings.GetGrandTotalName: يحصل على اسم الإجمالي الكبرى للوظيفة.

فيما يلي فئة مخصصة بسيطة توسع فئة GlobalizationSettings وتستبدل طرقها المذكورة أعلاه لإرجاع تسميات مخصصة لدالة التجميع المتوسطية.

**C#**

{{< highlight csharp >}}

 class CustomSettings : GlobalizationSettings

{

    public override string GetTotalName(ConsolidationFunction functionType)

    {

        switch (functionType)

        {

            case ConsolidationFunction.Average:

                return "AVG";

            default:

                return base.GetTotalName(functionType);

        }

    }

    public override string GetGrandTotalName(ConsolidationFunction functionType)

    {

        switch (functionType)

        {

            case ConsolidationFunction.Average:

                return "GRD AVG";

            default:

                return base.GetGrandTotalName(functionType);

        }

    }

}

{{< /highlight >}}



تحميل المقتطف التالي ورقة عمل موجودة بالفعل ويضيف Subtotal من النوع المتوسط على البيانات المتاحة بالفعل في ورقة العمل. سيتم استدعاء فئة CustomSettings وأساليب GetTotalName و GetGrandTotalName في وقت إضافة Subtotal إلى ورقة العمل.

**C#**

{{< highlight csharp >}}

 // Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

// Assigns the GlobalizationSettings property of the WorkbookSettings class

// to the class created in first step

book.Settings.GlobalizationSettings = new Cells.CustomSettings();

// Accesses the 1st worksheet from the collection which contains data

// Data resides in the cell range A2:B9

Worksheet sheet = book.Worksheets[0];

// Adds SubTotal of type Average to the worksheet

sheet.Cells.Subtotal(CellArea.CreateCellArea("A2", "B9"), 0, ConsolidationFunction.Average, new int[] { 0,1 });

// Calculates Formulas

book.CalculateFormula();

// Auto fits all columns

sheet.AutoFitColumns();

// Saves the workbook on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}



تقدم فئة GlobalizationSettings أيضًا أسلوب GetOtherName والذي يعد مفيدًا للحصول على اسم "آخر" للرسوم البيانية الدائرية. هنا سيناريو استخدام بسيط لأسلوب GlobalizationSettings.GetOtherName.

**C#**

{{< highlight csharp >}}

 class CustomSettings : GlobalizationSettings

{

    public override string GetOtherName()

    {

        int lcid = System.Globalization.CultureInfo.CurrentCulture.LCID;

        switch (lcid)

        {

            case 1033:

                return "Other";

            case 1036:

                return "Autre";

            case 1031:

                return "Andere";

            //Do other case

            default:

                return base.GetOtherName();

        }

    }

}

{{< /highlight >}}



المقتطف التالي يقوم بتحميل جدول بيانات موجود يحتوي على رسم بياني دائري، ويقوم بتقديم الرسم البياني إلى صورة أثناء استخدام فئة CustomSettings التي تم إنشاؤها أعلاه.

**C#**

{{< highlight csharp >}}

 // Loads an existing spreadsheet containing a pie chart

Workbook book = new Workbook(dir + "sample.xlsx");

// Assigns the GlobalizationSettings property of the WorkbookSettings class

// to the class created in first step

book.Settings.GlobalizationSettings = new Cells.CustomSettings();

// Accesses the 1st worksheet from the collection which contains pie chart

Worksheet sheet = book.Worksheets[0];

// Accesses the 1st chart from the collection

Chart chart = sheet.Charts[0];

// Refreshes the chart

chart.Calculate();

// Renders the chart to image

chart.ToImage(dir + "output.png", new ImageOrPrintOptions());

{{< /highlight >}}


### **تمت إضافة فئة CellsFactory**
Aspose.Cells 16.11.0 قد عرضت فئة CellsFactory التي تحتوي حاليًا على طريقة واحدة، وهي؛ CreateStyle. يمكن استخدام طريقة CellsFactory.CreateStyle لإنشاء مثيل لفئة Style دون إضافته إلى مجموعة أنماط دفتر العمل.

هنا سيناريو استخدام بسيط لطريقة CellsFactory.CreateStyle.

**C#**

{{< highlight csharp >}}

 // Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

// Creates an instance of Style

Style style = factory.CreateStyle();

{{< /highlight >}}


### **تمت إضافة خاصية Workbook.AbsolutePath**
أصدر Aspose.Cells 16.11.0 خاصية Workbook.AbsolutePath التي تسمح بالحصول على مسار العمل المؤقت المخزن في ملف workbook.xml أو تعيينه. تعتبر هذه الخاصية مفيدة أثناء تحديث الروابط الخارجية فقط.
### **تمت إضافة طريقة GridHyperlinkCollection.GetHyperlink**
قد عرض Aspose.Cells.GridWeb 16.11.0 طريقة GetHyperlink إلى فئة GridHyperlinkCollection التي تسمح بالحصول على مثيل من GridHyperlink سواء عن طريق تمرير مثيل GridCell أو زوج من الأعداد الصحيحة المقابلة لفهار الصف العمود.

{{% alert color="primary" %}} 

في حال عدم العثور على ارتباط تشعبي على الخلية المحددة ستقوم طريقة GetHyperlink بإرجاع قيمة فارغة.

{{% /alert %}} 

هنا سيناريو استخدام بسيط لطريقة GetHyperlink.

**C#**

{{< highlight csharp >}}

 // Gets the active worksheet from the collection

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Accesses the GridHyperlinkCollection

GridHyperlinkCollection links = sheet.Hyperlinks;

// Gets hyperlink from cell A1

GridHyperlink link = links.GetHyperlink(sheet.Cells["A1"]);

// Gets hyperlink from cell D1

link = links.GetHyperlink(0, 3);

{{< /highlight >}}
## **واجهات برمجة التطبيق القديمة**
### **مُنشئ نمط مهجور**
يرجى استخدام طريقة cellsFactory.CreateStyle كبديل.
## **حذف واجهات برمجة التطبيق**
### **الاكتشاف الشعبي للخلية.**
يرجى استخدام طريقة Cell.GetConditionalFormattingResult بدلاً من طريقة GetConditionalStyle.
### **طريقة حذف الخلايا.حدث الصف الأقصى في العمود(int column)**
يرجى استخدام طريقة Cells.GetLastDataRow(int) كبديل.
### **خاصية Draft في PageSetup تم حذفها**
من المستحسن استخدام خاصية PrintDraft في PageSetup بدلاً من ذلك.
### **خاصية FilterColumnCollection في AutoFilter تم حذفها**
يرجى النظر في استخدام خاصية FilterColumns في AutoFilter لتحقيق نفس الهدف.
### **خاصية Rotation في TickLabels تم حذفها**
الرجاء استخدام خاصية RotationAngle في TickLabels بدلاً من ذلك.
