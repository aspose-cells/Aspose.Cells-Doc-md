---
title: معدلات واجهة برمجة التطبيقات العامة في Aspose.Cells 8.3.2
type: docs
weight: 120
url: /ar/net/public-api-changes-in-aspose-cells-8-3-2/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات ل Aspose.Cells من الإصدار 8.3.1 إلى 8.3.2 التي قد تكون ذات أهمية لمطوري الوحدات/التطبيقات. يشمل ليس فقط الطرق العامة الجديدة والمحدثة، [أصناف الفصل المضافة الخ](/cells/ar/net/public-api-changes-in-aspose-cells-8-3-2/)، و[أصناف التفصيل المزالة الخ](/cells/ar/net/public-api-changes-in-aspose-cells-8-3-2/)، ولكن أيضًا وصفًا لأي تغييرات في السلوك وراء الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **آلية لوضع الموقع المطلق لـ PivotItem**
لتوفير ميزة [تحديد الموضع المطلق للعنصر (PivotItem)](/cells/ar/net/specifying-the-absolute-position-of-the-pivot-item/), قام Aspose.Cells for .NET 8.3.2 بتعريض سلسلة من الخصائص والطرق المساعدة كما هو مدرج أدناه.

- يمكن استخدام خاصية PivotItem.Position لتحديد فهرس الموضع في جميع PivotItems بغض النظر عن العقدة الأم.
- يمكن استخدام خاصية PivotItem.PositionInSameParentNode لتحديد فهرس الموضع في PivotItems تحت نفس العقدة الأم.
- يمكن استخدام طريقة PivotItem.Move(int count, bool isSameParent) لنقل العنصر أعلى أو أسفل استنادًا إلى قيمة العدد، حيث يُمثل العدد عدد المواقع التي يتم نقل PivotItem إليها لأعلى أو لأسفل. إذا كانت قيمة العدد أقل من الصفر، سيتم نقل العنصر لأعلى، أما إذا كانت قيمة العدد أكبر من الصفر، سيتم نقل PivotItem لأسفل، يُحدد المعلم النوع Boolean isSameParent ما إذا كان يجب تنفيذ عملية النقل في نفس العقدة الأم أم لا.

{{% alert color="primary" %}} 

يرجى ملاحظة، من الضروري استدعاء طرق PivotTable.RefreshData وPivotTable.CalculateData قبل استخدام خصائص PivotItem.Position، PivotItem.PositionInSameParentNode، وطريقة PivotItem.Move(int count, bool isSameParent).

{{% /alert %}} 
### **تم إضافة توقيع الفئة SignatureLine**
قدم Aspose.Cells for .NET 8.3.2 الدعم لخط التوقيع لتقليد الميزة المعادة حول مايكروسوفت إكسيل. لهذا الغرض، قد عرض هذا الإصدار من Aspose.Cells for .NET الفئة SignatureLine وخاصية Picture.SignatureLine.

الكود العيني التالي يضيف خط توقيع باستخدام خاصية Picture.SignatureLine إلى دفتر العمل.

**C#**

{{< highlight csharp >}}

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


### **تمت إضافة طريقة Chart.HasAxis**
مع إصدار v8.3.2، قدمت واجهة برمجة التطبيقات Aspose.Cells طريقة Chart.HasAxis(AxisType axisType, bool isPrimary) لتحديد ما إذا كان الرسم البياني يحتوي على محور معين أم لا.

يوضح الكود النموذجي التالي استخدام طريقة Chart.HasAxis لتحديد ما إذا كان الرسم البياني النموذجي يحتوي على محور أساسي وثانوي، والقيمة.

**C#**

{{< highlight csharp >}}

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


### **تمت إضافة طريقة WorkbookSettings.CheckWriteProtectedPassword**
تمكن طريقة WorkbookSettings.CheckWriteProtectedPassword المطورين من التحقق مما إذا كانت كلمة المرور المعطاة لتعديل جدول البيانات صحيحة أم لا.

**C#**

{{< highlight csharp >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.Password = "1234";

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

bool ret = workbook.CheckWriteProtectedPassword("567");

Console.WriteLine("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}


### **تمت إضافة طرق السيرة المتوالية WorkbookRender.ToPrinter & SheetRender.ToPrinter**
قدم Aspose.Cells for .NET 8.3.2 طرق WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) وSheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) لطباعة نطاق الصفحات لدفتر العمل وجدول البيانات على التوالي.

يوضح الكود العيني التالي استخدام الطرق المذكورة أعلاه لطباعة الصفحات 2-5 من المصنف والصفحة.

**C#**

{{< highlight csharp >}}

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


### **أضيفت أسلوب تحديث الجداول المحورية في الورقة**
أسلوب تحديث الجداول المحورية المضاف حديثًا في الورقة يسمح بتحديث جميع الجداول المحورية في جدول بيانات معين بمكالمة واحدة.

**C#**

{{< highlight csharp >}}

 worksheet.RefreshPivotTables();

{{< /highlight >}}


### **تم إضافة أسلوب الحصول على الأسلوب المسمى في الدفتر**
قامت Aspose.Cells for .NET API بعرض أسلوب Workbook.GetNamedStyle الذي يقبل السلسلة كمعلمة ويسترجع كائن الأسلوب بناءً على المعلمة الممررة.
### **تمت إضافة أسلوب الاستيراد لمصفوفة ثنائية الأبعاد للخلايا**
قامت Aspose.Cells for .NET API بجعله ممكنًا استيراد المصفوفات ثنائية الأبعاد إلى خلايا جدول البيانات عن طريق عرض أسلوب Cells.ImportTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions). يقوم الأسلوب المذكور باستيراد مصفوفة ثنائية الأبعاد من البيانات في ورقة عمل مع خيارات أكثر مرونة تم تعريفها في TxtLoadOptions.
### **تمت إضافة خصائص OnePagePerSheet وPageIndex & PageCount**
قدمت Aspose.Cells for .NET 8.3.2 خصائص OnePagePerSheet, PageIndex و PageCount لفئة XpsSaveOptions. يمكن للمستخدم تناسب كل محتويات جدول بيانات على صفحة واحدة من XPS باستخدام خاصية OnePagePerSheet و/أو استرداد عدد الصفحات المراد طباعتها باستخدام خاصية PageCount. يتم الحصول على خاصية PageIndex للحصول على / تعيين الفهرس القائم على القيم التي ستتم حفظها.
### **تمت إضافة خصائص NumberDecimalSeparator & NumberGroupSeparator**
قدمت Aspose.Cells for .NET 8.3.2 خصائص NumberDecimalSeparator و NumberGroupSeparator التي يمكن الحصول عليها/تعيينها لفصل المحتوى المخصص المستخدم لتنسيق وتحليل القيم الرقمية في جداول بيانات.

الكود المقترح التالي يوضح كيفية تحديد الفواصل المخصصة باستخدام واجهة برمجة التطبيقات Aspose.Cells. يُحدد الكود التالي الفاصل المخصص العشري وفاصل المجموعة المخصصة كنقطة وفراغ على التوالي.

**C#**

{{< highlight csharp >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.Settings.NumberDecimalSeparator = '.';

workbook.Settings.NumberGroupSeparator = ' ';

{{< /highlight >}}


### **تمت إضافة خصائص PdfSaveOptions.IsFontSubstitutionCharGranularity**
قدمت Aspose.Cells for .NET 8.3.2 خاصية PdfSaveOptions.IsFontSubstitutionCharGranularity لتجاوز المشكلة حيث لا يمكن عرض بعض الأحرف اليونيكود باستخدام عائلة الخط الخاصة. عندما يتم تعيين خاصية PdfSaveOptions.IsFontSubstitutionCharGranularity على true سيتم تغيير الخط الخاص بالحرف المعين الذي لا يمكن عرضه إلى خط قابل للعرض ويجب أن يظل بقية الكلمة أو الجملة بنفس الخط الأصلي.

**C#**

{{< highlight csharp >}}

 //Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true

PdfSaveOptions opts = new PdfSaveOptions();

opts.IsFontSubstitutionCharGranularity = true;

{{< /highlight >}}


## **تمت إزالة واجهات برمجة التطبيقات**
### **تمت إزالة الأساليب القديمة**
الأساليب التالية تم إزالتها من واجهة برمجة التطبيقات العامة.

- أساليب فتح وحفظ الدفتر.
- أساليب مجموعة OleSize.
- أسلوب LoadData للدفتر.
- تشمل الأساليب WorkbookDesigner.Open و WorkbookDesigner.Save.
- تشمل الأساليب WorksheetCollection.DeleteName.
### **تمت إزالة الخصائص القديمة**
الخصائص التالية تم إزالتها من واجهة برمجة التطبيقات العامة.

- تشمل الخاصية Workbook.IsProtected.
- خاصية Workbook.Language.
- خاصية Workbook.Region.
- خاصية WorkbookSettings.ReCalcOnOpen.
- خاصية WorkbookSettings.Language.
- خاصية WorkbookSettings.Encoding.
- خاصية WorkbookSettings.ConvertNumericData.
- خاصية WorksheetCollection.HidePivotFieldList.
- خاصية WorksheetCollection.EnableHTTPCompression.
- تشمل الخاصية WorksheetCollection.IsMinimized.
- تشمل الخاصية WorksheetCollection.IsHidden.
- خاصية WorksheetCollection.SheetTabBarWidth.
- خاصية WorksheetCollection.WindowLeft.
- خاصية WorksheetCollection.WindowLeftInch.
- خاصية WorksheetCollection.WindowLeftCM.
- خاصية WorksheetCollection.WindowTop.
- خاصية WorksheetCollection.WindowTopInch.
- خاصية WorksheetCollection.WindowTopCM.
- خاصية WorksheetCollection.WindowWidth.
- خاصية WorksheetCollection.WindowWidthInch.
- خاصية WorksheetCollection.WindowWidthCM.
- خاصية WorksheetCollection.WindowHeight.
- خاصية WorksheetCollection.WindowHeightInch.
- خاصية WorksheetCollection.WindowHeightCM.
- خاصية Worksheet.HPageBreaks.
- خاصية Worksheet.VPageBreaks.
- خاصية HtmlSaveOptions.DisplayHTMLCrossString.
- خاصية HtmlSaveOptions.ExportChartImageFormat.
- خاصية SaveOptions.ExpCellNameToXLSX.
- خاصية SaveOptions.DefaultFont.
- خاصية SaveOptions.Compliance.
- خاصية SaveOptions.PdfBookmark.
- خاصية SaveOptions.PdfImageCompression.
- خاصية TxtSaveOptions.AlwaysQuoted.
## **واجهات برمجة التطبيقات المهملة**
### **واجهة برمجة تطبيقات قديمة لخاصية Workbook.SaveOptions**
يجب تمرير كائن SaveOptions إلى طريقة Workbook.Save بعد ضبط خصائص SaveOptions الصحيحة.
### **خاصية Workbook.Styles & فئة StyleCollection قديمة**
يُفضل استخدام طريقة Workbook.CreateStyle لإنشاء وتلاعب بالنمط لمثيل المصنف بدلاً من إنشاء نمط بطريقة StyleCollection.Add. علاوة على ذلك، يمكن استخدام الطريقة Workbook.GetNamedStyle(string) للحصول على نمط مسمى بدلاً من StyleCollection[string].
### **طريقة PivotItem.Move قديمة**
مع إصدار Aspose.Cells 8.3.2، قد قدمت واجهة API تحميل زائد آخر لطريقة PivotItem.Move تقبل المعلمة الصحيحة للعدد والمعلمة البولية لتحريك PivotItem داخل العقد الأصلي.
{{< app/cells/assistant language="csharp" >}}
