---
title: API عام تغييرات في Aspose.Cells 16.11.0
type: docs
weight: 350
url: /ar/net/public-api-changes-in-aspose-cells-16-11-0/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 16.10.0 إلى 16.11.0 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة والمحذوفة وما إلى ذلك ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **دعم إعدادات العولمة**
كشف Aspose.Cells 16.11.0 عن فئة GlobalizationSettings جنبًا إلى جنب مع خاصية WorkbookSettings.GlobalizationSettings من أجل فرض Aspose.Cells APIs لاستخدام تسميات مخصصة للمجموعات الفرعية. تحتوي فئة GlobalizationSettings على الطرق التالية التي يمكن تجاوزها في التنفيذ المخصص لإعطاء الأسماء المطلوبة للتسميات**مجموع** & **المبلغ الإجمالي**.

- GlobalizationSettings.GetTotalName: الحصول على الاسم الإجمالي للوظيفة.
- GlobalizationSettings.GetGrandTotalName: الحصول على الاسم الإجمالي الكلي للدالة.

فيما يلي فئة مخصصة بسيطة تعمل على توسيع فئة GlobalizationSettings وتتجاوز الأساليب المذكورة أعلاه لإرجاع تسميات مخصصة لوظيفة الدمج المتوسط.

**C#**

{{< highlight "csharp" >}}

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



المقتطف التالي يقوم بتحميل جدول بيانات موجود ويضيف الإجمالي الفرعي لنوع المتوسط على البيانات المتوفرة بالفعل في ورقة العمل. سيتم استدعاء فئة CustomSettings وأساليب GetTotalName & GetGrandTotalName الخاصة بها في وقت إضافة Subtotal إلى ورقة العمل.

**C#**

{{< highlight "csharp" >}}

 // Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

// Assigns the GlobalizationSettings property of the WorkbookSettings class

// to the class created in first step

book.Settings.GlobalizationSettings = new Cells.CustomSettings();

// Accesses the 1st worksheet from the collection which contains data

// Data resides in the cell range A2:B9

Worksheet sheet = book.Worksheets[0];

// Adds SubTotal of type Average to the worksheet

sheet.Cells.Subtotal(CellArea.CreateCellArea("A2", "B9"), 0, ConsolidationFunction.Average, new int[]{ 0,1 });

// Calculates Formulas

book.CalculateFormula();

// Auto fits all columns

sheet.AutoFitColumns();

// Saves the workbook on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}



تقدم فئة GlobalizationSettings أيضًا طريقة GetOtherName والتي تعد مفيدة للحصول على اسم تسميات "أخرى" للمخططات الدائرية. فيما يلي سيناريو استخدام بسيط لطريقة GlobalizationSettings.GetOtherName.

**C#**

{{< highlight "csharp" >}}

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



يقوم المقتطف التالي بتحميل جدول بيانات موجود يحتوي على مخطط دائري ، ويعرض المخطط للصورة أثناء استخدام فئة CustomSettings التي تم إنشاؤها أعلاه.

**C#**

{{< highlight "csharp" >}}

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
كشف Aspose.Cells 16.11.0 عن فئة CellsFactory التي لها حاليًا طريقة واحدة ، وهي ؛ خلق نمط. يمكن استخدام طريقة CellsFactory.CreateStyle لإنشاء مثيل لفئة Style دون إضافتها إلى مجموعة أنماط المصنف.

فيما يلي سيناريو الاستخدام البسيط لطريقة CellsFactory.CreateStyle.

**C#**

{{< highlight "csharp" >}}

 // Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

// Creates an instance of Style

Style style = factory.CreateStyle();

{{< /highlight >}}


### **تمت إضافة المصنف. خاصية AbsolutePath**
كشف Aspose.Cells 16.11.0 المصنف. تسمح الخاصية AbsolutePath بالحصول على المسار المطلق للمصنف المخزن في ملف workbook.xml أو تعيينه. هذه الخاصية مفيدة أثناء تحديث الروابط الخارجية فقط.
### **تمت إضافة أسلوب GridHyperlinkCollection.GetHyperlink**
كشف Aspose.Cells.GridWeb 16.11.0 طريقة GetHyperlink لفئة GridHyperlinkCollection التي تسمح بالحصول على مثيل GridHyperlink إما بتمرير مثيل GridCell أو زوج من الأعداد الصحيحة المقابلة لمؤشرات عمود الصف.

{{% alert color="primary" %}} 

في حالة عدم العثور على ارتباط تشعبي في الخلية المحددة ، فإن طريقة GetHyperlink سترجع فارغة.

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط لطريقة GetHyperlink.

**C#**

{{< highlight "csharp" >}}

 // Gets the active worksheet from the collection

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Accesses the GridHyperlinkCollection

GridHyperlinkCollection links = sheet.Hyperlinks;

// Gets hyperlink from cell A1

GridHyperlink link = links.GetHyperlink(sheet.Cells["A1"]);

// Gets hyperlink from cell D1

link = links.GetHyperlink(0, 3);

{{< /highlight >}}
## **واجهات برمجة التطبيقات التي عفا عليها الزمن**
### **منشئ أسلوب قديم**
يرجى استخدام طريقة cellFactory.CreateStyle كبديل.
## **واجهات برمجة التطبيقات المحذوفة**
### **تم حذف Cell.GetConditionalStyle Method**
الرجاء استخدام طريقة Cell.GetConditionalFormattingResult بدلاً من ذلك.
### **تم حذف طريقة Cells.MaxDataRowInColumn (عمود int)**
الرجاء استخدام طريقة Cells.GetLastDataRow (int) كبديل.
### **خاصية PageSetup.Draft المحذوفة**
يُنصح باستخدام خاصية PageSetup.PrintDraft بدلاً من ذلك.
### **تم حذف خاصية AutoFilter.FilterColumnCollection**
يرجى مراعاة استخدام خاصية AutoFilter.FilterColumns لتحقيق نفس الهدف.
### **TickLabels المحذوفة. خاصية الدوران**
الرجاء استخدام خاصية TickLabels.RotationAngle بدلاً من ذلك.
