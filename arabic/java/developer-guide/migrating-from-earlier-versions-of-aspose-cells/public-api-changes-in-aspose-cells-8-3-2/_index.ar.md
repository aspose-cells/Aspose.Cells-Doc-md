---
title: معدلات واجهة برمجة التطبيقات العامة في Aspose.Cells 8.3.2
type: docs
weight: 130
url: /ar/java/public-api-changes-in-aspose-cells-8-3-2/
---

{{% alert color="primary" %}} 

وصف هذا المستند التغييرات في واجهة برمجة التطبيقات API من Aspose.Cells من الإصدار 8.3.1 إلى 8.3.2 التي قد تكون مثيرة لاهتمام مطوّري الوحدات / التطبيق. يتضمن الآشياء الجديدة والمُحدّثة للطرق العامة، [الفصول المضافة وما إضافة والمزيد](/cells/ar/java/public-api-changes-in-aspose-cells-8-3-2/) و[الفصول المزالة وما إزالة](/cells/ar/java/public-api-changes-in-aspose-cells-8-3-2/)، بالإضافة إلى وصف لأي تغييرات في السلوك الداخلي في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **آلية لوضع الموقع المطلق لـ PivotItem**
لتوفير ميزة [تحديد الموضع المطلق لعنصر الجدول المحوري](/cells/ar/java/specifying-the-absolute-position-of-the-pivot-item/)، فقد قامت Aspose.Cells for Java 8.3.2 بتعريض سلسلة من الخصائص والطريقة كما هو مدرج أدناه.

- يمكن استخدام PivotItem.setPosition لتعيين مؤشر الموقع في جميع PivotItems بصرف النظر عن العقد الأصل.
- يمكن استخدام PivotItem.setPositionInSameParentNode لتعيين مؤشر الموقع في PivotItems تحت نفس عقد الأصل.
- يمكن استخدام طريقة PivotItem.move(int count, bool isSameParent) لتحريك العنصر للأعلى أو للأسفل بناءً على قيمة العدد، حيث يُمثّل العدد عدد المواقع التي يتعين نقل PivotItem إلى الأعلى أو الأسفل. إذا كانت قيمة العدد أقل من الصفر، سيتم نقل العنصر إلى الأعلى، بينما إذا كانت قيمة العدد أكبر من الصفر، سيتم نقل PivotItem إلى الأسفل، يُحدد معامل نوع Boolean isSameParent ما إذا كان يجب أن تتم عملية النقل في نفس عقد الأصل أم لا.

{{% alert color="primary" %}} 

يرجى ملاحظة أنه من الضروري استدعاء طرق PivotTable.refreshData و PivotTable.calculateData قبل استخدام خصائص PivotItem.setPosition و PivotItem.setPositionInSameParentNode وطريقة PivotItem.move(int count, bool isSameParent).

{{% /alert %}} 
### **تم إضافة توقيع الفئة SignatureLine**
Aspose.Cells 8.3.2 يقدم الدعم لخطوط التوقيع لتقليد ميزة MS Excel المعادلة. لهذا الغرض، قد فتح هذا الإصدار الفئة SignatureLine وخاصية Picture.SignatureLine.

الكود العيني التالي يضيف خط توقيع باستخدام خاصية Picture.SignatureLine إلى دفتر العمل.

**Java**

{{< highlight csharp >}}

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
### **تمت إضافة طريقة Chart.hasAxis**
مع إصدار v8.3.2، قد قدمت واجهة برمجة التطبيقات Aspose.Cells طريقة Chart.hasAxis(AxisType axisType, bool isPrimary) لتحديد ما إكان لدى الرسم البياني محور معين أم لا.

يُظهر الكود العيني التالي استخدام طريقة Chart.hasAxis لتحديد ما إكان لدى الرسم البياني عيني، ثانوي وقيمة المحور.

**Java**

{{< highlight csharp >}}

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
### **تمت إضافة طريقة WorkbookSettings.checkWriteProtectedPassword**
تُمكّن طريقة WorkbookSettings.checkWriteProtectedPassword المطورين من التحقق مما إذا كانت كلمة المرور المعطاة لتعديل جدول البيانات صحيحة أم لا.

**Java**

{{< highlight csharp >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.setPassword("1234");

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

boolean ret = workbook.checkWriteProtectedPassword("567");

System.out.println("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}
### **تمت إضافة طرق تحميل توقيع الفئة WorkbookRender.toPrinter وSheetRender.toPrinter**
أوفرت Aspose.Cells 8.3.2 طريقة WorkbookRender.toPrinter(string printerName, int printPageIndex, int printPageCount) وطريقة SheetRender.toPrinter(string printerName, int printPageIndex, int printPageCount) لطباعة نطاق صفحات المصنف والصفحة على التوالي.

يوضح الكود العيني التالي استخدام الطرق المذكورة أعلاه لطباعة الصفحات 2-5 من المصنف والصفحة.

**Java**

{{< highlight csharp >}}

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
### **تمت إضافة طريقة Worksheet.refreshPivotTables**
تسمح الطريقة المضافة حديثًا Worksheet.refreshPivotTables باستعادة جميع الجداول المحورية في جدول بيانات معين في استدعاء واحد.

**Java**

{{< highlight csharp >}}

 worksheet.refreshPivotTables();

{{< /highlight >}}
### **تمت إضافة طريقة Workbook.getNamedStyle**
فتحت Aspose.Cells 8.3.2 الطريقة Workbook.getNamedStyle التي تقبل النص كمعلمة وتسترجع كائن النمط استنادًا إلى المعلمة المرسلة.
### **تمت إضافة طريقة Cells.importTwoDimensionArray**
أتاحت Aspose.Cells API استيراد مصفوفات ثنائية الأبعاد إلى خلايا الجداول عن طريق فتح الطريقة Cells.importTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions). تقوم الطريقة المذكورة بأهمية مصفوفة ثنائية الأبعاد من البيانات إلى ورقة عمل مع خيارات مرنة أكثر تعريفها في TxtLoadOptions.
### **تمت إضافة خصائص OnePagePerSheet وPageIndex & PageCount**
فتحت Aspose.Cells for Java 8.3.2 خصائص OnePagePerSheet وPageIndex & PageCount لفئة XpsSaveOptions. يمكن للمستخدم إعادة ترتيب جميع محتويات جدول البيانات على صفحة واحدة من XPS باستخدام خاصية OnePagePerSheet و/أو استرجاع عدد الصفحات المطبوعة باستخدام خاصية PageCount. تحصل خاصية PageIndex على/تعيين الفهرس المعتمد على 0 لأول صفحة يتم حفظها.
### **تمت إضافة خصائص NumberDecimalSeparator & NumberGroupSeparator**
قدمت Aspose.Cells for Java 8.3.2 خصائص NumberDecimalSeparator & NumberGroupSeparator التي يمكن الحصول/التعيين على فواصل مخصصة مستخدمة لتنسيق وتحليل القيم الرقمية في جداول البيانات.

يوضح الكود العيني التالي كيفية تحديد الفواصل المخصصة باستخدام واجهة برمجة التطبيقات Aspose.Cells. يحدد الكود التالي الفواصل المخصصة للعلامتين العشرية والمجموعة على التوالي.

**Java**

{{< highlight csharp >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.getSettings().setNumberDecimalSeparator('.');

workbook.getSettings().setNumberGroupSeparator(' ');

{{< /highlight >}}
### **تمت إضافة خاصية PdfSaveOptions.setFontSubstitutionCharGranularity**
فتحت Aspose.Cells for Java 8.3.2 خاصية PdfSaveOptions.setFontSubstitutionCharGranularity للتغلب على المشكلة التي قد لا يمكن فيها عرض بعض الحروف اليونيكود باستخدام عائلة الخط معينة. عند تعيين خاصية PdfSaveOptions.setFontSubstitutionCharGranularity على true، ستتم تغيير الخط الخاص بالحرف المعين الذي لا يمكن عرضه إلى خط قابل للعرض ويبقى بقية الكلمة أو الجملة في الخط الأصلي.

**Java**

{{< highlight csharp >}}

 //Save to PDF after setting PdfSaveOptions.setFontSubstitutionCharGranularity

PdfSaveOptions opts = new PdfSaveOptions();

opts.setFontSubstitutionCharGranularity(true);

{{< /highlight >}}
## **تمت إزالة واجهات برمجة التطبيقات**
### **تمت إزالة الأساليب القديمة**
الأساليب التالية تم إزالتها من واجهة برمجة التطبيقات العامة.

- أساليب Workbook.open و Workbook.save.
- أسلوب Workbook.setOleSize.
- أسلوب Workbook.loadData.
- أساليب WorkbookDesigner.open و WorkbookDesigner.save.
- أسلوب WorksheetCollection.deleteName.
### **تمت إزالة الخصائص القديمة**
الخصائص التالية تم إزالتها من واجهة برمجة التطبيقات العامة.

- خاصية Workbook.isProtected.
- خاصية Workbook.Language.
- خاصية Workbook.Region.
- خاصية WorkbookSettings.ReCalcOnOpen.
- خاصية WorkbookSettings.Language.
- خاصية WorkbookSettings.Encoding.
- خاصية WorkbookSettings.ConvertNumericData.
- خاصية WorksheetCollection.HidePivotFieldList.
- خاصية WorksheetCollection.EnableHTTPCompression.
- خاصية WorksheetCollection.isMinimized.
- خاصية WorksheetCollection.isHidden.
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
### **خاصية Workbook.saveOptions المهجورة**
يجب تمرير كائن SaveOptions إلى طريقة Workbook.Save بعد ضبط خصائص SaveOptions الصحيحة. 
### **واجهة برمجة التطبيقات Workbook.Styles & Class StyleCollection المهجورة**
يُنصح باستخدام طريقة Workbook.createStyle لإنشاء وتلاعب بالنمط لمثيل Workbook بدلاً من إنشاء نمط باستخدام طريقة StyleCollection.add. علاوة على ذلك، يمكن استخدام طريقة Workbook.getNamedStyle(string) للحصول على النمط المسمى بدلاً من StyleCollection.get(string).
### **طريقة PivotItem.move(int count) المهجورة**
مع إصدار Aspose.Cells 8.3.2، قدمت الواجهة البرمجة التطبيقات overload جديدة لطريقة PivotItem.move تقبل المعلمة الصحيحة للعدد والمعلمة البولية لنقل PivotItem داخل العقد الأصلي. 
