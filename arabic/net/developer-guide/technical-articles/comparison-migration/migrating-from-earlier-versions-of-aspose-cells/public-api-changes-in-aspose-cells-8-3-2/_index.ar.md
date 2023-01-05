---
title: API العام التغييرات في Aspose.Cells 8.3.2
type: docs
weight: 120
url: /ar/net/public-api-changes-in-aspose-cells-8-3-2/
---
{{% alert color="primary" %}} 

 يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.3.1 إلى 8.3.2 والتي قد تهم مطوري الوحدة النمطية / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ،[الفئات المضافة وما إلى ذلك.](/cells/ar/net/public-api-changes-in-aspose-cells-8-3-2/) و[الفئات المحذوفة وما إلى ذلك.](/cells/ar/net/public-api-changes-in-aspose-cells-8-3-2/)ولكن أيضًا وصف لأية تغييرات في السلوك خلف الكواليس عام Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **آلية لتعيين الوضع المطلق لـ PivotItem**
 من أجل توفير الميزة[وضع PivotItem المطلق](/cells/ar/net/specifying-the-absolute-position-of-the-pivot-item/)، أظهر Aspose.Cells for .NET 8.3.2 سلسلة من الخصائص وطرق المساعدة كما هو موضح أدناه.

- يمكن استخدام خاصية PivotItem.Position لتحديد فهرس الموضع في جميع عناصر PivotItems بغض النظر عن العقدة الأصلية.
- يمكن استخدام خاصية PivotItem.PositionInSameParentNode لتحديد فهرس الموضع في PivotItems ضمن نفس العقدة الأصلية.
- يمكن استخدام طريقة PivotItem.Move (عدد صحيح ، منطقي isSameParent) لتحريك العنصر لأعلى أو لأسفل بناءً على قيمة العد ، حيث يكون العدد هو رقم الموضع لتحريك PivotItem لأعلى أو لأسفل. إذا كانت قيمة العد أقل من الصفر ، فسيتم نقل العنصر لأعلى حيث كما لو كانت قيمة العد أكبر من الصفر ، سينتقل PivotItem إلى أسفل ، والنوع المنطقي هو نفس المعلمة الأصلية تحدد ما إذا كان يجب تنفيذ عملية النقل في نفس العقدة الأصلية أم لا.

{{% alert color="primary" %}} 

يرجى ملاحظة أنه من الضروري استدعاء أساليب PivotTable.RefreshData و PivotTable.CalculateData قبل استخدام طريقة PivotItem.Position و PivotItem.PositionInSameParentNode و PivotItem.Move (عدد int ، bool isSameParent).

{{% /alert %}} 
### **تمت إضافة سطر توقيع الفصل**
Aspose.Cells for .NET 8.3.2 يوفر الدعم لخط التوقيع لتقليد الميزة المكافئة لبرنامج MS Excel. كشف هذا الإصدار من Aspose.Cells for .NET فئة SignatureLine وخاصية Picture.SignatureLine لهذا الغرض.

يضيف نموذج التعليمات البرمجية التالي خط التوقيع باستخدام الخاصية Picture.SignatureLine إلى المصنف.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Insert picture of your choice

int index = workbook.Worksheets[0].Pictures.Add(0, 0, "signature.jpg");

//Access picture and add signature line inside it

Picture pic = workbook.Worksheets[0].Pictures[index];

//Create signature line object

SignatureLine s = new SignatureLine();

s.Signer = "John Doe";

s.Title = "Development Lead";

s.Email = "john.doe@aspose.com";

//Assign the signature line object to Picture.SignatureLine property

pic.SignatureLine = s;

{{< /highlight >}}


### **طريقة الرسم البياني**
مع إصدار v8.3.2 ، قدم Aspose.Cells API المخطط. طريقة HasAxis (AxisType axisType ، bool isPrimary) لتحديد ما إذا كان المخطط يحتوي على محور معين أم لا.

يوضح نموذج التعليمات البرمجية التالي استخدام أسلوب Chart.HasAxis لتحديد ما إذا كان المخطط النموذجي يحتوي على المحور الأساسي والثانوي والقيمة.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the chart

Chart chart = worksheet.Charts[0];

//Determine which axis exists in chart

bool ret = chart.HasAxis(AxisType.Category, true);

Console.WriteLine("Has Primary Category Axis: " + ret);

ret = chart.HasAxis(AxisType.Category, false);

Console.WriteLine("Has Secondary Category Axis: " + ret);

ret = chart.HasAxis(AxisType.Value, true);

Console.WriteLine("Has Primary Value Axis: " + ret);

ret = chart.HasAxis(AxisType.Value, false);

Console.WriteLine("Has Secondary Value Axis: " + ret);

{{< /highlight >}}


### **الأسلوب WorkbookSettings.CheckWriteProtectedPassword مضاف**
طريقة WorkbookSettings.CheckWriteProtectedPassword تمكن المطورين من التحقق مما إذا كانت كلمة مرور معينة لتعديل جدول البيانات صحيحة أم لا.

**C#**

{{< highlight "csharp" >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.Password = "1234";

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

bool ret = workbook.CheckWriteProtectedPassword("567");

Console.WriteLine("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}


### **طرق التحميل الزائد WorkbookRender.ToPrinter & SheetRender.ToPrinter المضافة**
قدم Aspose.Cells for .NET 8.3.2 أساليب WorkbookRender.ToPrinter (سلسلة PrinterName، int PrintPageIndex، int PrintPageCount) و SheetRender.ToPrinter (سلسلة PrinterName، int PrintPageIndex، int PrintPageCount) لطباعة نطاق صفحات المصنف وورقة العمل على التوالي.

يوضح نموذج التعليمات البرمجية التالي استخدام الأساليب المذكورة أعلاه لطباعة الصفحات 2-5 من المصنف وورقة العمل.

**C#**

{{< highlight "csharp" >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Print the workbook specifying the range of pages

//Here we are printing pages 2-5

WorkbookRender wr = new WorkbookRender(workbook, new ImageOrPrintOptions());

wr.ToPrinter(printerName, 1, 4);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Print the worksheet specifying the range of pages

//Here we are printing pages 2-5

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

sr.ToPrinter(printerName, 1, 4);

{{< /highlight >}}


### **الطريقة Worksheet.RefreshPivotTables المضافة**
الطريقة المضافة حديثًا Worksheet.RefreshPivotTables تسمح بتحديث جميع الجداول المحورية في جدول بيانات معين في مكالمة واحدة.

**C#**

{{< highlight "csharp" >}}

 worksheet.RefreshPivotTables();

{{< /highlight >}}


### **أسلوب Workbook.GetNamedStyle المضافة**
كشف Aspose.Cells for .NET API طريقة Workbook.GetNamedStyle التي تقبل السلسلة كمعامل وتسترجع كائن النمط بناءً على المعامل الذي تم تمريره.
### **الطريقة Cells. تمت إضافة PortTwoDimensionArray**
Aspose.Cells for .NET API أتاح استيراد مصفوفات ثنائية الأبعاد لخلايا جدول البيانات بتعريض طريقة Cells.ImportTwoDimensionArray (object [،]، object [،]، int، int، TxtLoadOptions). تستورد الطريقة المذكورة صفيفًا ثنائي الأبعاد من البيانات في ورقة عمل بخيارات أكثر مرونة محددة في TxtLoadOptions.
### **تمت إضافة خصائص OnePagePerSheet و PageIndex و PageCount**
كشف Aspose.Cells for .NET 8.3.2 خصائص OnePagePerSheet و PageIndex و PageCount لفئة XpsSaveOptions. يمكن للمستخدم احتواء جميع محتويات جدول البيانات على صفحة واحدة من XPS باستخدام خاصية OnePagePerSheet و / أو استرداد عدد الصفحات المراد طباعتها باستخدام خاصية PageCount. تحصل خاصية PageIndex على / تعين الفهرس الذي يستند إلى 0 للصفحة الأولى المراد حفظها.
### **تمت إضافة خصائص NumberDecimalSeparator & NumberGroupSeparator**
قدم Aspose.Cells for .NET 8.3.2 خصائص NumberDecimalSeparator & NumberGroupSeparator التي يمكنها الحصول على / تعيين الفواصل المخصصة المستخدمة لتنسيق وتحليل القيم الرقمية في جداول البيانات.

يوضح نموذج التعليمات البرمجية التالي كيفية تحديد الفواصل المخصصة باستخدام Aspose.Cells API. يحدد الكود التالي الفواصل العشرية والمجموعة المخصصة كنقطة ومسافة على التوالي.

**C#**

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.Settings.NumberDecimalSeparator = '.';

workbook.Settings.NumberGroupSeparator = ' ';

{{< /highlight >}}


### **تمت إضافة خاصية PdfSaveOptions.IsFontSubstitutionCharGranularity**
كشف Aspose.Cells for .NET 8.3.2 خاصية PdfSaveOptions.IsFontSubstitutionCharGranularity للتغلب على المشكلة حيث لا يمكن عرض بعض أحرف Unicode باستخدام عائلة خطوط معينة. عند تعيين خاصية PdfSaveOptions.IsFontSubstitutionCharGranularity إلى true ، سيتم تغيير خط الحرف المحدد الذي لا يمكن عرضه إلى الخط القابل للعرض ويجب أن تظل بقية الكلمة أو الجملة بالخط الأصلي.

**C#**

{{< highlight "csharp" >}}

 //Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true

PdfSaveOptions opts = new PdfSaveOptions();

opts.IsFontSubstitutionCharGranularity = true;

{{< /highlight >}}


## **إزالة واجهات برمجة التطبيقات**
### **إزالة الطرق المتقادمة**
تمت إزالة الأساليب التالية من API العامة.

- Workbook.Open & Workbook.Save الأساليب.
- طريقة Workbook.SetOleSize.
- طريقة Workbook.LoadData.
- WorkbookDesigner.Open & WorkbookDesigner.Save الطرق.
- طريقة WorksheetCollection.DeleteName.
### **تمت إزالة الخصائص المتقادمة**
تمت إزالة الخصائص التالية من API العامة.

- المصنف خاصية محمية.
- المصنف خاصية اللغة.
- المصنف الملكية المنطقة.
- WorkbookSettings.ReCalcOnOpen الخاصية.
- إعدادات المصنف. خاصية اللغة.
- إعدادات المصنف. خاصية الترميز.
- خاصية WorkbookSettings.ConvertNumericData.
- الخاصية WorksheetCollection.HidePivotFieldList.
- خاصية WorksheetCollection.EnableHTTPCompression.
- WorksheetCollection.Is الخاصية المصغرة.
- WorksheetCollection.Is الخاصية المخفية.
- الخاصية WorksheetCollection.SheetTabBarWidth.
- خاصية WorksheetCollection.WindowLeft.
- الخاصية WorksheetCollection.WindowLeftInch.
- الخاصية WorksheetCollection.WindowLeftCM.
- خاصية WorksheetCollection.WindowTop.
- الخاصية WorksheetCollection.WindowTopInch.
- الخاصية WorksheetCollection.WindowTopCM.
- الخاصية WorksheetCollection.WindowWidth.
- الخاصية WorksheetCollection.WindowWidthInch.
- الخاصية WorksheetCollection.WindowWidthCM.
- الخاصية WorksheetCollection.WindowHeight.
- الخاصية WorksheetCollection.WindowHeightInch.
- الخاصية WorksheetCollection.WindowHeightCM.
- Worksheet.HPageBreaks.
- Worksheet.VPageBreaks.
- الخاصية HtmlSaveOptions.DisplayHTMLCrossString.
- HtmlSaveOptions.ExportChartImageFormat الخاصية.
- SaveOptions.ExpCellNameToXLSX.
- SaveOptions.DefaultFont.
- SaveOptions.Compliance الخاصية.
- SaveOptions.Pdf خاصية الإشارة المرجعية.
- خاصية SaveOptions.PdfImageCompression.
- TxtSaveOptions.Always اقتباس الممتلكات.
## **واجهات برمجة التطبيقات المهجورة**
### **مصنف الخاصية. SaveOptions قديم**
يجب تمرير كائن من SaveOptions إلى أسلوب Workbook.Save بعد تعيين خصائص SaveOptions المناسبة.
### **مصنفات الملكية.الأنماط ونمط الصف**
يُنصح باستخدام طريقة Workbook.CreateStyle لإنشاء أسلوب ومعالجته لمثيل المصنف بدلاً من إنشاء أسلوب باستخدام أسلوب StyleCollection.Add. علاوة على ذلك ، يمكن استخدام طريقة Workbook.GetNamedStyle (سلسلة نصية) للحصول على نمط مسمى بدلاً من StyleCollection [سلسلة].
### **الأسلوب PivotItem.Move (عدد العمليات) قديم**
مع إصدار Aspose.Cells 8.3.2 ، قدم API حملًا زائدًا آخر لطريقة PivotItem.Move التي تقبل معلمة العدد الصحيح للمعامل count والمعلمة المنطقية لنقل PivotItem داخل العقدة الأصلية.
