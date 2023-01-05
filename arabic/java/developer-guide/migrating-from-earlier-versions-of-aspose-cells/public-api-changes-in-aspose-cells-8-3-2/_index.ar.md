---
title: API العام التغييرات في Aspose.Cells 8.3.2
type: docs
weight: 130
url: /ar/java/public-api-changes-in-aspose-cells-8-3-2/
---
{{% alert color="primary" %}} 

 يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.3.1 إلى 8.3.2 والتي قد تهم مطوري الوحدة النمطية / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ،[الفئات المضافة وما إلى ذلك.](/cells/ar/java/public-api-changes-in-aspose-cells-8-3-2/) و[الفئات المحذوفة وما إلى ذلك.](/cells/ar/java/public-api-changes-in-aspose-cells-8-3-2/)ولكن أيضًا وصف لأية تغييرات في السلوك خلف الكواليس عام Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **آلية لتعيين الوضع المطلق لـ PivotItem**
 من أجل توفير الميزة[وضع PivotItem المطلق](/cells/ar/java/specifying-the-absolute-position-of-the-pivot-item/)، أظهر Aspose.Cells for Java 8.3.2 سلسلة من الخصائص وطريقة كما هو موضح أدناه.

- يمكن استخدام PivotItem.setPosition لتعيين فهرس الموضع في جميع عناصر PivotItems بغض النظر عن العقدة الأصلية.
- يمكن استخدام PivotItem.setPositionInSameParentNode لتعيين فهرس الموضع في PivotItems ضمن نفس العقدة الأصلية.
- يمكن استخدام طريقة PivotItem.move (عدد صحيح ، منطقي isSameParent) لتحريك العنصر لأعلى أو لأسفل استنادًا إلى قيمة العد ، حيث يكون العدد هو رقم الموضع لتحريك PivotItem لأعلى أو لأسفل. إذا كانت قيمة العد أقل من الصفر ، فسيتم نقل العنصر لأعلى حيث كما لو كانت قيمة العد أكبر من الصفر ، سينتقل PivotItem إلى أسفل ، والنوع المنطقي هو نفس المعلمة الأصلية تحدد ما إذا كان يجب تنفيذ عملية النقل في نفس العقدة الأصلية أم لا.

{{% alert color="primary" %}} 

يرجى ملاحظة أنه من الضروري استدعاء أساليب PivotTable.refreshData و PivotTable.calculateData قبل استخدام PivotItem.setPosition و PivotItem.setPositionInSameParentNode و PivotItem.move (عدد int ، bool isSameParent).

{{% /alert %}} 
### **تمت إضافة سطر توقيع الفصل**
Aspose.Cells 8.3.2 يوفر الدعم لخط التوقيع لتقليد الميزة المكافئة لبرنامج MS Excel. كشف هذا الإصدار عن فئة SignatureLine وخاصية Picture.SignatureLine لهذا الغرض.

يضيف نموذج التعليمات البرمجية التالي خط التوقيع باستخدام الخاصية Picture.SignatureLine إلى المصنف.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Insert picture of your choice

int index = workbook.getWorksheets().get(0).getPictures().add(0, 0, "signature.jpg");

//Access picture and add signature line inside it

Picture pic = workbook.getWorksheets().get(0).getPictures().get(index);

//Create signature line object

SignatureLine s = new SignatureLine();

s.setSigner("John Doe");

s.setTitle("Development Lead");

s.setEmail("john.doe@aspose.com");

//Assign the signature line object to Picture.SignatureLine property

pic.setSignatureLine(s);

{{< /highlight >}}
### **طريقة Chart.hasAxis المضافة**
مع إصدار v8.3.2 ، قدم Aspose.Cells API طريقة Chart.hasAxis (نوع محور نوع المحور ، منطقي هو أساسي) لتحديد ما إذا كان المخطط يحتوي على محور معين أم لا.

يوضح نموذج التعليمات البرمجية التالي استخدام أسلوب Chart.hasAxis لتحديد ما إذا كان المخطط النموذجي يحتوي على محور أساسي وثانوي وقيمة.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the chart

Chart chart = worksheet.getCharts().get(0);

//Determine which axis exists in chart

boolean ret = chart.hasAxis(AxisType.CATEGORY, true);

System.out.println("Has Primary Category Axis: " + ret);

ret = chart.hasAxis(AxisType.CATEGORY, false);

System.out.println("Has Secondary Category Axis: " + ret);

ret = chart.hasAxis(AxisType.VALUE, true);

System.out.println("Has Primary Value Axis: " + ret);

ret = chart.hasAxis(AxisType.VALUE, false);

System.out.println("Has Seconary Value Axis: " + ret);

{{< /highlight >}}
### **الأسلوب WorkbookSettings.checkWriteProtectedPassword مضاف**
طريقة WorkbookSettings.checkWriteProtectedPassword تمكن المطورين من التحقق مما إذا كانت كلمة مرور معينة لتعديل جدول البيانات صحيحة أم لا.

**Java**

{{< highlight "csharp" >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.setPassword("1234");

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

boolean ret = workbook.checkWriteProtectedPassword("567");

System.out.println("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}
### **طرق التحميل الزائد WorkbookRender.toPrinter و SheetRender.toPrinter المضافة**
قدم Aspose.Cells 8.3.2 أساليب WorkbookRender.toPrinter (سلسلة printerName ، int printPageIndex ، int printPageCount) و SheetRender.toPrinter (string printerName، int printPageIndex، int printPageCount) لطباعة نطاق صفحات المصنف وورقة العمل على التوالي.

يوضح نموذج التعليمات البرمجية التالي استخدام الأساليب المذكورة أعلاه لطباعة الصفحات 2-5 من المصنف وورقة العمل.

**Java**

{{< highlight "csharp" >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Print the workbook specifying the range of pages

//Here we are printing pages 2-5

WorkbookRender wr = new WorkbookRender(workbook, new ImageOrPrintOptions());

wr.toPrinter(printerName, 1, 4);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Print the worksheet specifying the range of pages

//Here we are printing pages 2-5

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

sr.toPrinter(printerName, 1, 4);

{{< /highlight >}}
### **الطريقة Worksheet.refreshPivotTables المضافة**
تسمح الطريقة المضافة حديثًا Worksheet.refreshPivotTables بتحديث جميع الجداول المحورية في جدول بيانات معين في مكالمة واحدة.

**Java**

{{< highlight "csharp" >}}

 worksheet.refreshPivotTables();

{{< /highlight >}}
### **الأسلوب Workbook.getNamedStyle مضاف**
كشف Aspose.Cells 8.3.2 طريقة Workbook.getNamedStyle التي تقبل السلسلة كمعامل وتسترجع كائن النمط بناءً على المعامل الذي تم تمريره.
### **الطريقة Cells.importTwoDimensionArray مضافة**
لقد أتاح Aspose.Cells API استيراد مصفوفات ثنائية الأبعاد لخلايا جدول البيانات عن طريق تعريض طريقة Cells.importTwoDimensionArray (كائن [،] ، كائن [،] ، int ، int ، TxtLoadOptions). تستورد الطريقة المذكورة صفيفًا ثنائي الأبعاد من البيانات في ورقة عمل بخيارات أكثر مرونة محددة في TxtLoadOptions.
### **تمت إضافة خصائص OnePagePerSheet و PageIndex و PageCount**
كشف Aspose.Cells for Java 8.3.2 خصائص OnePagePerSheet و PageIndex و PageCount لفئة XpsSaveOptions. يمكن للمستخدم احتواء جميع محتويات جدول البيانات على صفحة واحدة من XPS باستخدام خاصية OnePagePerSheet و / أو استرداد عدد الصفحات المراد طباعتها باستخدام خاصية PageCount. تحصل خاصية PageIndex على / تعين الفهرس الذي يستند إلى 0 للصفحة الأولى المراد حفظها.
### **تمت إضافة خصائص NumberDecimalSeparator & NumberGroupSeparator**
قدم Aspose.Cells for Java 8.3.2 خصائص NumberDecimalSeparator & NumberGroupSeparator التي يمكنها الحصول على / تعيين الفواصل المخصصة المستخدمة لتنسيق وتحليل القيم الرقمية في جداول البيانات.

يوضح نموذج التعليمات البرمجية التالي كيفية تحديد الفواصل المخصصة باستخدام Aspose.Cells API. يحدد الكود التالي فواصل العشرية والمجموعة المخصصة كنقطة ومسافة على التوالي.

**Java**

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.getSettings().setNumberDecimalSeparator('.');

workbook.getSettings().setNumberGroupSeparator(' ');

{{< /highlight >}}
### **تمت إضافة الخاصية PdfSaveOptions.setFontSubstitutionCharGranularity**
كشف Aspose.Cells for Java 8.3.2 خاصية PdfSaveOptions.setFontSubstitutionCharGranularity للتغلب على المشكلة حيث لا يمكن عرض بعض أحرف Unicode باستخدام عائلة خطوط معينة. عندما يتم تعيين خاصية PdfSaveOptions.setFontSubstitutionCharGranularity إلى "صحيح" ، سيتم تغيير خط الحرف المحدد الذي لا يمكن عرضه إلى الخط القابل للعرض ويجب أن تظل بقية الكلمة أو الجملة بالخط الأصلي.

**Java**

{{< highlight "csharp" >}}

 //Save to PDF after setting PdfSaveOptions.setFontSubstitutionCharGranularity

PdfSaveOptions opts = new PdfSaveOptions();

opts.setFontSubstitutionCharGranularity(true);

{{< /highlight >}}
## **إزالة واجهات برمجة التطبيقات**
### **إزالة الطرق المتقادمة**
تمت إزالة الأساليب التالية من API العامة.

- طرق Workbook.open & Workbook.save.
- طريقة Workbook.setOleSize.
- طريقة Workbook.loadData.
- طرق WorkbookDesigner.open & WorkbookDesigner.save.
- طريقة WorksheetCollection.deleteName.
### **تمت إزالة الخصائص المتقادمة**
تمت إزالة الخصائص التالية من API العامة.

- مصنف. isProtected الملكية.
- المصنف خاصية اللغة.
- المصنف الملكية المنطقة.
- WorkbookSettings.ReCalcOnOpen الخاصية.
- إعدادات المصنف. خاصية اللغة.
- إعدادات المصنف. خاصية الترميز.
- خاصية WorkbookSettings.ConvertNumericData.
- الخاصية WorksheetCollection.HidePivotFieldList.
- خاصية WorksheetCollection.EnableHTTPCompression.
- خاصية WorksheetCollection.is المصغرة.
- WorksheetCollection.is الخاصية المخفية.
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
### **Workbook.saveOptions خاصية قديمة**
 يجب تمرير كائن من SaveOptions إلى أسلوب Workbook.Save بعد تعيين خصائص SaveOptions المناسبة.
### **مصنفات الملكية.الأنماط ونمط الصف**
يُنصح باستخدام طريقة Workbook.createStyle لإنشاء أسلوب ومعالجته لمثيل المصنف بدلاً من إنشاء أسلوب باستخدام أسلوب StyleCollection.add. علاوة على ذلك ، يمكن استخدام طريقة Workbook.getNamedStyle (سلسلة) للحصول على نمط مسمى بدلاً من StyleCollection.get (سلسلة).
### **الأسلوب PivotItem.move (عدد العمليات) قديم**
 مع إصدار Aspose.Cells 8.3.2 ، أدخل API حملًا زائدًا آخر لطريقة PivotItem.move التي تقبل معلمة العدد الصحيح للمعامل count والمعلمة المنطقية لنقل PivotItem داخل العقدة الأصلية.
