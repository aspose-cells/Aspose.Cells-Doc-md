---
title: التغييرات العامة في الواجهة البرمجية لـ Aspose.Cells 8.5.0
type: docs
weight: 160
url: /ar/net/public-api-changes-in-aspose-cells-8-5-0/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات Aspose.Cells من الإصدار 8.4.2 إلى 8.5.0 التي قد تكون مهمة لمطوري الوحدات / التطبيقات. يتضمن ليس فقط الطرق العامة الجديدة والمحدثة والفئات المضافة [إلخ](/cells/ar/net/public-api-changes-in-aspose-cells-8-5-0/), ولكن أيضًا وصفًا لأي تغييرات في السلوك الذي يحدث خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **تغيرت معلمات ICustomFunction.CalculateCustomFunction**
إذا كان أحد المعاملات للدالة المخصصة مرجعًا للخلية ، فقد كانت تستخدم واجهات برمجة التطبيقات القديمة Aspose.Cells APIs لتحويل مرجع الخلية إلى قيمة خلية واحدة أو مصفوفة كائنية من جميع قيم الخلية في المنطقة المشار إليها. ومع ذلك ، بالنسبة للعديد من الوظائف والمستخدمين ، ليس من الضروري مصفوفة قيم الخلية لجميع الخلايا في المنطقة المشار إليها ، فهم يحتاجون فقط إلى خلية واحدة مقابل موضع الصيغة ، أو فقط يحتاجون إلىالمرجع نفسه بدلاً من قيمة الخلية أو مصفوفة القيم. وبالنسبة لبعض الحالات ، قد زاد استخدام جميع قيم الخلية من مخاطر حدوث خطأ الإشارة المعكوسة.

لدعم هذا النوع من المتطلبات، قامت Aspose.Cells for .NET 8.5.0 بتغيير قيمة المعلمة إلى "paramsList" للمنطقة المحددة. منذ الإصدار v8.5.0، يقوم واجهة برمجة التطبيقات بوضع كائن ReferredArea في "paramsList" عندما تكون المعلمة المقابلة مرجعًا أو نتيجة حسابها هي مرجع. إذا كنت بحاجة إلى المرجع نفسه، فيمكنك استخدام ReferredArea مباشرة. إذا كنت بحاجة إلى الحصول على قيمة خلية واحدة من المرجع المقابل مع وضع الصيغة، يمكنك استخدام طريقة ReferredArea.GetValue(rowOffset, int colOffset). إذا كنت بحاجة إلى مصفوفة قيم خلية للمنطقة بأكملها، يمكنك استخدام طريقة ReferredArea.GetValues.

الآن كما يُعطي Aspose.Cells for .NET 8.5.0 ReferredArea في "paramsList", لن يكون ReferredAreaCollection في "contextObjects" مطلوبًا بعد الآن (في الإصدارات القديمة كان لا يمكنه دائمًا إعطاء خريطة واحدة إلى واحدة لمعلمات الدالة المخصصة)، لذا تمت إزالته أيضًا من "contextObjects" الآن.

يتطلب هذا التغيير تغييرات في كود التنفيذ لـ ICustomFunction قليلاً عندما يكون هناك حاجة لقيمة/قيم للمعلمة المرجعية.

**التنفيذ القديم**

{{< highlight csharp >}}

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

**التنفيذ الجديد**

{{< highlight csharp >}}

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


### **وأضيفت صفة الخيارات الحسابية**
قام Aspose.Cells for .NET 8.5.0 بتعريض فئة CalculationOptions لإضافة المزيد من المرونة والقابلية للتمدد لمحرك حساب الصيغة. للفئة المضافة حديثًا الخصائص التالية.

1. CalculationOptions.CalcStackSize: تحدد حجم الشريحة لحساب الخلايا بشكل متكرر. تحدد القيمة -1 أن الحساب سيستخدم WorkbookSettings.CalcStackSize من الدفتر المحاسبي المقابل.
1. CalculationOptions.CustomFunction: يوسع محرك حساب الصيغ بصيغة مخصصة.
1. CalculationOptions.IgnoreError: تشير قيمة النوع البوليانية إلى ما إذا كان يتعين إخفاء الأخطاء أثناء حساب الصيغ ، حيث يمكن أن تكون الأخطاء ناتجة عن وظيفة غير مدعومة ، أو رابط خارجي أو أكثر.
1. CalculationOptions.PrecisionStrategy: نوع استراتيجية حساب الدقة للقيمة التي تحدد الاستراتيجية لمعالجة الدقة في الحساب.
### **تمت إضافة استراتيجية حساب الدقة**
قامت Aspose.Cells for .NET 8.5.0 بتعريض تعداد CalculationPrecisionStrategy لإضافة المزيد من المرونة إلى محرك حساب الصيغة للحصول على النتائج المرجوة. تعداد هذه الاستراتيجيات لمعالجة الدقة في الحساب. بسبب مشكلة الدقة في الحساب باستخدام IEEE 754 للنقاط العائمة، قد لا يتم حساب بعض الصيغ التي تبدو بسيطة لإعطاء النتائج المتوقعة، لذا قامت أحدث بنية للواجهة بتعريض الحقول التالية للحصول على النتائج المرجوة حسب الاختيار.

1. CalculationPrecisionStrategy.Decimal: يستخدم العدد العشري كعامل عند الإمكان، وهو الأقل كفاءة من حيث الأداء.
1. CalculationPrecisionStrategy.Round: يقوم بتقريب نتائج الحساب وفقًا للأرقام الكبيرة.
1. CalculationPrecisionStrategy.None: لا يتم تطبيق أي استراتيجية للحساب وبالتالي أثناء الحساب، يستخدم المحرك القيمة العشرية الأصلية كعامل ويُرجع النتيجة مباشرة. هذا الخيار هو الأكثر كفاءة وهو قابل للتطبيق في معظم الحالات.
### **الطرق المضافة لاستخدام خيارات الحساب**
مع إصدار v8.5.0، أضافت Aspose.Cells API نسخًا إضافية من طريقة CalculateFormula كما هو مدرج أدناه.

- Workbook.CalculateFormula(CalculationOptions)
- Worksheet.CalculateFormula(CalculationOptions options, bool recursive)
- Cell.Calculate(CalculationOptions)
### **تمت إضافة حقل تعداد PasteType.RowHeights**
قدمت Aspose.Cells APIs حقل تعداد PasteType.RowHeights لنسخ أطوال الصفوف أثناء نسخ النطاقات. عند ضبط خاصية PasteOptions.PasteType على PasteType.RowHeights، سيتم نسخ أطوال جميع الصفوف داخل النطاق المصدر إلى النطاق الوجهة.

**C#**

{{< highlight csharp >}}

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
عند ضبط تسوية الصفحة باستخدام الخيار **Fit to n page(s) wide by m tall**، يقوم Microsoft Excel بحساب عامل تسوية تسوية الصفحة. يمكن تحقيق النفس باستخدام خاصية SheetRender.PageScale التي يتم عرضها بواسطة Aspose.Cells for .NET 8.5.0. تُعيد هذه الخاصية قيمة مزدوجة يمكن تحويلها إلى قيمة النسبة المئوية. على سبيل المثال، إذا أعادت 0.507968245 فهذا يعني أن عامل التسوية هو 51٪.

**C#**

{{< highlight csharp >}}

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


### **تمت إضافة تعدادية CellValueFormatStrategy**
أضاف Aspose.Cells for .NET 8.5.0 تعدادًا جديدًا CellValueFormatStrategy للتعامل مع الحالات التي يجب استخراج قيم الخلية مع أو بدون تطبيق التنسيق. التعداد CellValueFormatStrategy يحتوي على الحقول التالية.

1. CellValueFormatStrategy.CellStyle: مهيأة فقط باستخدام التنسيق الأصلي للخلية.
1. CellValueFormatStrategy.DisplayStyle: مهيأة باستخدام النمط المعروض للخلية.
1. CellValueFormatStrategy.None: غير مهيأة.
### **تمت إضافة طريقة Cell.GetStingValue**
لاستخدام تعداد CellValueFormatStrategy، قامت v8.5.0 بتعريض طريقة Cell.GetStingValue التي يمكن أن تقبل معلمة من النوع CellValueFormatStrategy وتعيد القيمة تعتمد على الخيار المحدد.

يوضح مقطع الكود التالي كيفية استخدام طريقة Cells.GetStingValue المكشوفة حديثًا.

**C#**

{{< highlight csharp >}}

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
قامت Aspose.Cells for .NET 8.5.0 بتعريض خاصية ExportTableOptions.FormatStrategy للمستخدمين الذين يرغبون في تصدير البيانات إلى DataTable مع أو بدون تنسيق. تستخدم هذه الخاصية تعداد CellValueFormatStrategy وتصدر البيانات حسب الخيار المحدد.

يشرح الكود التالي استخدام خاصية ExportTableOptions.FormatStrategy.

**C#**

{{< highlight csharp >}}

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
{{< app/cells/assistant language="csharp" >}}
