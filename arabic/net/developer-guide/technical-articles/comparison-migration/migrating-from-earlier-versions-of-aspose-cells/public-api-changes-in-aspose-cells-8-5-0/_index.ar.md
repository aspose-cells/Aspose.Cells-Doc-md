---
title: API العام التغييرات في Aspose.Cells 8.5.0
type: docs
weight: 160
url: /ar/net/public-api-changes-in-aspose-cells-8-5-0/
---
{{% alert color="primary" %}} 

 يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.4.2 إلى 8.5.0 والتي قد تهم مطوري الوحدة النمطية / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ،[الفئات المضافة وما إلى ذلك.](/cells/ar/net/public-api-changes-in-aspose-cells-8-5-0/)ولكن أيضًا وصف لأية تغييرات في السلوك خلف الكواليس عام Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **تم تغيير معلمات وظيفة ICustom.CalculateCustomFunction**
إذا كانت معلمة واحدة للوظيفة المخصصة هي مرجع الخلية ، في الإصدار القديم Aspose.Cells APIs المستخدمة لتحويل مرجع الخلية إلى قيمة خلية واحدة أو صفيف كائن لجميع قيم الخلية في المنطقة المشار إليها. ومع ذلك ، بالنسبة للعديد من الوظائف والمستخدمين ، لا يلزم وجود مصفوفة قيم الخلية لجميع الخلايا في المنطقة المشار إليها ، فهم يحتاجون فقط إلى خلية واحدة مطابقة لموضع الصيغة ، أو يحتاجون فقط إلى المرجع نفسه بدلاً من قيمة الخلية أو صفيف القيمة . في بعض الحالات ، يؤدي جلب جميع قيم الخلايا إلى زيادة خطر حدوث خطأ مرجعي دائري.

لدعم مثل هذا النوع من المتطلبات ، قام Aspose.Cells for .NET 8.5.0 بتغيير قيمة المعلمة إلى "paramsList" للمنطقة المشار إليها. منذ الإصدار 8.5.0 ، يضع API الكائن RefifiedArea في "paramsList" عندما تكون المعلمة المقابلة مرجعًا أو تكون النتيجة المحسوبة مرجعًا. إذا كنت بحاجة إلى المرجع نفسه ، فيمكنك استخدام RefifiedArea مباشرة. إذا كنت بحاجة إلى الحصول على قيمة خلية مفردة واحدة من المرجع المقابل لموضع الصيغة ، يمكنك استخدام أسلوب RefifiedArea.GetValue (rowOffset ، int colOffset). إذا كنت بحاجة إلى مصفوفة قيم الخلية للمنطقة بأكملها ، فيمكنك استخدام طريقة RefifiedArea.GetValues.

الآن نظرًا لأن 8.5.0 Aspose.Cells for .NET يعطي 8.5.0 RefifiedArea في "paramsList" ، فلن تكون هناك حاجة إلى مجموعة RefifiedAreaCollection في "ContextObjects" بعد الآن (في الإصدارات القديمة لم يكن بإمكانها إعطاء مخطط واحد لواحد لمعلمات الوظيفة المخصصة دائمًا) ، لذلك قام هذا الإصدار أيضًا بإزالته من "ContextObjects" الآن.

يتطلب هذا التغيير إجراء تغييرات على رمز تنفيذ وظيفة ICustomFunction قليلاً عندما تحتاج إلى قيمة / قيم المعلمة المرجعية.

**التنفيذ القديم**

{{< highlight "csharp" >}}

 public object CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    object o = paramsList[i];

    if (o is Array)

    {

        ...

    }

    else if...

    ...

}

{{< /highlight >}}

**تنفيذ جديد**

{{< highlight "csharp" >}}

 public object CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    object o = paramsList[i];

    if(o is ReferredArea) //fetch data from reference

    {

        ReferredArea ra = (ReferredArea)o;

        if(ra.IsArea)

        {

            o = ra.GetValues();

        }

        else

        {

            o = ra.GetValue(0, 0);

        }

    }

    if (o is Array)

    {

        ...

    }

    else if...

    ...

}

{{< /highlight >}}


### **تمت إضافة خيارات احتساب الفصل**
كشف Aspose.Cells for .NET 8.5.0 عن فئة CalculationOptions لإضافة المزيد من المرونة والقابلية للتوسعة لمحرك حساب الصيغة. الفئة المضافة حديثًا لها الخصائص التالية.

1. CalculationOptions.CalcStackSize: تحديد حجم المكدس لحساب الخلايا بشكل متكرر. -1 يحدد أن الحساب سيستخدم WorkbookSettings.CalcStackSize من المصنف المقابل.
1. CalculationOptions.CustomFunction: توسيع محرك حساب الصيغة باستخدام صيغة مخصصة.
1. CalculationOptions.IgnoreError: تشير قيمة النوع المنطقي إلى ما إذا كان سيتم إخفاء الأخطاء أثناء حساب الصيغ ، حيث قد تكون الأخطاء ناتجة عن وظيفة غير مدعومة أو ارتباط خارجي أو أكثر.
1. CalculationOptions.PrecisionStrategy: قيمة نوع CalculationPrecisionStrategy التي تحدد استراتيجية معالجة دقة الحساب.
### **تمت إضافة حساب العد الدقة الإستراتيجية**
كشف Aspose.Cells for .NET 8.5.0 إستراتيجية حساب التعداد لإضافة المزيد من المرونة لمحرك حساب الصيغة للحصول على النتائج المرجوة. هذا التعداد استراتيجيات معالجة الحساب بدقة. نظرًا لمسألة الدقة في IEEE 754 Floating-Point Arithmetic ، فقد لا يتم حساب بعض الصيغ التي تبدو بسيطة لإعطاء النتائج المتوقعة ، وبالتالي فإن أحدث إصدار API قد كشف الحقول التالية للحصول على النتائج المرجوة وفقًا للتحديد.

1. CalculationPrecisionStrategy.Decimal: يستخدم العلامة العشرية كمعامل حيثما أمكن ، وهو غير فعال من اعتبارات الأداء.
1. CalculationPrecisionStrategy.Round: تقريب نتائج الحساب وفقًا لأرقام ذات دلالة.
1. CalculationPrecisionStrategy.None: لم يتم تطبيق أي استراتيجية لذلك أثناء الحساب يستخدم المحرك القيمة المزدوجة الأصلية كمعامل ويعيد النتيجة مباشرة. هذا الخيار هو الأكثر فعالية ويمكن تطبيقه في معظم الحالات.
### **تمت إضافة طرق لاستخدام خيارات الحساب**
مع إصدار v8.5.0 ، أضاف Aspose.Cells API إصدارات التحميل الزائد لطريقة CalculateFormula كما هو موضح أدناه.

- المصنف .CalculateFormula (خيارات الحساب)
- Worksheet.CalculateFormula (CalculationOptions options ، bool recursive)
- Cell.حساب (خيارات الحساب)
### **تمت إضافة PasteType.RowHeights في حقل التعداد**
قدمت واجهات برمجة التطبيقات Aspose.Cells مجال التعداد PasteType.RowHeights لغرض نسخ ارتفاعات الصف أثناء نسخ النطاقات. عند ضبط خاصية PasteOptions.PasteType على ((PasteType.RowHeights}} سيتم نسخ ارتفاعات جميع الصفوف داخل نطاق المصدر إلى النطاق الوجهة.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Source worksheet

Worksheet srcSheet = workbook.Worksheets[0];

//Add destination worksheet

Worksheet dstSheet = workbook.Worksheets.Add("Destination Sheet");

//Set the row height of the 4th row

//This row height will be copied to destination range

srcSheet.Cells.SetRowHeight(3, 50);

//Create source range to be copied

Range srcRange = srcSheet.Cells.CreateRange("A1:D10");

//Create destination range in destination worksheet

Range dstRange = dstSheet.Cells.CreateRange("A1:D10");

//PasteOptions, we want to copy row heights of source range to destination range

PasteOptions opts = new PasteOptions();

opts.PasteType = PasteType.RowHeights;

//Copy source range to destination range with paste options

dstRange.Copy(srcRange, opts);

//Write informative message in cell D4 of destination worksheet

dstSheet.Cells["D4"].PutValue("Row heights of source range copied to destination range");

//Save the workbook in xlsx format

workbook.Save("output.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}


### **تمت إضافة خاصية SheetRender.PageScale**
عندما تقوم بتعيين مقياس إعداد الصفحة باستخدام**يصلح ل n صفحة (ق) عرض في متر طول** الخيار ، Microsoft يقوم Excel بحساب عامل تحجيم إعداد الصفحة. يمكن تحقيق نفس الشيء باستخدام خاصية SheetRender.PageScale المعروضة بواسطة Aspose.Cells for .NET 8.5.0. تقوم هذه الخاصية بإرجاع قيمة مزدوجة يمكن تحويلها إلى قيمة النسبة المئوية. على سبيل المثال ، إذا كانت تُرجع 0.507968245 ، فهذا يعني أن عامل القياس هو 51٪.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Put some data in these cells

worksheet.Cells["A4"].PutValue("Test");

worksheet.Cells["S4"].PutValue("Test");

//Set paper size

worksheet.PageSetup.PaperSize = PaperSizeType.PaperA4;

//Set fit to pages wide as 1

worksheet.PageSetup.FitToPagesWide = 1;

//Calculate page scale via sheet render

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

//Convert page scale double value to percentage

string strPageScale = sr.PageScale.ToString("0%");

//Write the page scale value

Console.WriteLine(strPageScale);

{{< /highlight >}}


### **تمت إضافة خلية التعداد CellValueFormatStrategy**
Aspose.Cells for .NET 8.5.0 أضاف إستراتيجية تعداد جديدة CellValueFormatStrategy للتعامل مع المواقف التي يجب فيها استخراج قيم الخلية مع تطبيق التنسيق أو بدونه. يحتوي Enumeration CellValueFormatStrategy على الحقول التالية.

1. CellValueFormatStrategy.CellStyle: منسق فقط بالتنسيق الأصلي للخلية.
1. CellValueFormatStrategy.DisplayStyle: منسق بنمط الخلية المعروض.
1. CellValueFormatStrategy.None: غير منسق.
### **الطريقة Cell.GetStingValue مضافة**
من أجل استخدام تعداد CellValueFormatStrategy ، كشف v8.5.0 عن طريقة Cell.GetStingValue التي يمكن أن تقبل معلمة من النوع CellValueFormatStrategy وإرجاع القيمة تعتمد على الخيار المحدد.

يوضح مقتطف التعليمات البرمجية التالي كيفية استخدام طريقة Cells.GetStingValue المكشوفة حديثًا.

**C#**

{{< highlight "csharp" >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cell A1

Cell cell = worksheet.Cells["A1"];

//Put value inside the cell

cell.PutValue(0.012345);

//Format the cell that it should display 0.01 instead of 0.012345

Style style = cell.GetStyle();

style.Number = 2;

cell.SetStyle(style);

//Get string value as Cell Style

string value = cell.GetStingValue(CellValueFormatStrategy.CellStyle);

Console.WriteLine(value);

//Get string value without any formatting

value = cell.GetStingValue(CellValueFormatStrategy.None);

Console.WriteLine(value);

{{< /highlight >}}


### **تمت إضافة خاصية ExportTableOptions.FormatStrategy**
كشف Aspose.Cells for .NET 8.5.0 خاصية ExportTableOptions.FormatStrategy للمستخدمين الذين يرغبون في تصدير البيانات إلى DataTable بالتنسيق أو بدونه. تستفيد هذه الخاصية من تعداد CellValueFormatStrategy وتقوم بتصدير البيانات وفقًا للخيار المحدد.

يشرح الكود التالي استخدام خاصية ExportTableOptions.FormatStrategy.

**C#**

{{< highlight "csharp" >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cell A1

Cell cell = worksheet.Cells["A1"];

//Put value inside the cell

cell.PutValue(0.012345);

//Format the cell that it should display 0.01 instead of 0.012345

Style style = cell.GetStyle();

style.Number = 2;

cell.SetStyle(style);

//Print the cell values as it displays in excel

Console.WriteLine("Cell String Value: " + cell.StringValue);

//Print the cell value without any format

Console.WriteLine("Cell String Value without Format: " + cell.StringValueWithoutFormat);

//Export Data Table Options with FormatStrategy as CellStyle

ExportTableOptions opts = new ExportTableOptions();

opts.ExportAsString = true;

opts.FormatStrategy = CellValueFormatStrategy.CellStyle;

//Export Data Table

DataTable dt = worksheet.Cells.ExportDataTable(0, 0, 1, 1, opts);

//Print the value of very first cell

Console.WriteLine("Export Data Table with Format Strategy as Cell Style: " + dt.Rows[0][0].ToString());

//Export Data Table Options with FormatStrategy as None

opts.FormatStrategy = CellValueFormatStrategy.None;

dt = worksheet.Cells.ExportDataTable(0, 0, 1, 1, opts);

//Print the value of very first cell

Console.WriteLine("Export Data Table with Format Strategy as None: " + dt.Rows[0][0].ToString());

{{< /highlight >}}
