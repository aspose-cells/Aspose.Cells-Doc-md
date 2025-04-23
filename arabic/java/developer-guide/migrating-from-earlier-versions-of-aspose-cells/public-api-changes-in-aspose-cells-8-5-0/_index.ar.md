---
title: التغييرات العامة في الواجهة البرمجية لـ Aspose.Cells 8.5.0
type: docs
weight: 170
url: /ar/java/public-api-changes-in-aspose-cells-8-5-0/
---

{{% alert color="primary" %}} 

يصف هذا الوثيقة التغييرات في واجهة برمجة التطبيقات لـ Aspose.Cells من الإصدار 8.4.2 إلى 8.5.0 التي قد تكون مهمة لمطوري الوحدة / التطبيق. إنها تتضمن ليس فقط الطرق العامة الجديدة والمحدثة والفصول المضافة الخ وما إلى ذلك، ولكن أيضا وصف لأي تغييرات في السلوك وراء الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **تغيرت معلمات ICustomFunction.CalculateCustomFunction**
إذا كان أحد المعاملات للدالة المخصصة مرجعًا للخلية ، فقد كانت تستخدم واجهات برمجة التطبيقات القديمة Aspose.Cells APIs لتحويل مرجع الخلية إلى قيمة خلية واحدة أو مصفوفة كائنية من جميع قيم الخلية في المنطقة المشار إليها. ومع ذلك ، بالنسبة للعديد من الوظائف والمستخدمين ، ليس من الضروري مصفوفة قيم الخلية لجميع الخلايا في المنطقة المشار إليها ، فهم يحتاجون فقط إلى خلية واحدة مقابل موضع الصيغة ، أو فقط يحتاجون إلىالمرجع نفسه بدلاً من قيمة الخلية أو مصفوفة القيم. وبالنسبة لبعض الحالات ، قد زاد استخدام جميع قيم الخلية من مخاطر حدوث خطأ الإشارة المعكوسة.

لدعم هذا النوع من المتطلبات ، قامت إصدارة Aspose.Cells for Java 8.5.0 بتغيير قيمة المعلمة إلى "paramsList" للمنطقة المحولة. منذ الإصدار 8.5.0 ، يقوم واجهة برمجة التطبيقات بوضع كائن ReferredArea في "paramsList" عندما تكون المعلمة المقابلة هي مرجع أو ناتج الحساب هو مرجع. إذا كنت بحاجة إلى المرجع نفسه ، يمكنك استخدام ReferredArea مباشرة. إذا كنت بحاجة إلى الحصول على قيمة خلية واحدة من المرجع المقابل لموضع الصيغة ، يمكنك استخدام الطريقة ReferredArea.getValue(rowOffset, int colOffset). إذا كنت بحاجة إلى مصفوفة قيم الخلايا للمنطقة بأكملها ، فيمكنك استخدام الطريقة ReferredArea.getValues.

الآن ، حيث يقدم الإصدار Aspose.Cells for Java 8.5.0 ReferredArea في "paramsList" ، فإن ReferredAreaCollection في "contextObjects" لن يعد مطلوبًا بعد الآن (في الإصدارات القديمة قد لا تكون دائما لها إعداد واحد إلى واحد لمعلمات الدالة المخصصة) ، لذا قام هذا الإصدار أيضًا بإزالتها من "contextObjects" الآن.

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

            o = ra.getValues();

        }

        else

        {

            o = ra.getValue(0, 0);

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
اطلقت Aspose.Cells for Java 8.5.0 صفة خيارات الحساب لإضافة المزيد من المرونة والقابلية لمحرك الحساب الصيغي. وتحتوي الصفة الجديدة التي تمت إضافتها على الخصائص التالية. 

1. CalculationOptions.CalcStackSize: تحدد حجم الشريحة لحساب الخلايا بشكل متكرر. تحدد القيمة -1 أن الحساب سيستخدم WorkbookSettings.CalcStackSize من الدفتر المحاسبي المقابل.
1. CalculationOptions.CustomFunction: يوسع محرك حساب الصيغ بصيغة مخصصة.
1. CalculationOptions.IgnoreError: تشير قيمة النوع البوليانية إلى ما إذا كان يتعين إخفاء الأخطاء أثناء حساب الصيغ ، حيث يمكن أن تكون الأخطاء ناتجة عن وظيفة غير مدعومة ، أو رابط خارجي أو أكثر.
1. CalculationOptions.PrecisionStrategy: نوع استراتيجية حساب الدقة للقيمة التي تحدد الاستراتيجية لمعالجة الدقة في الحساب.
### **تمت إضافة استراتيجية حساب الدقة**
 قدمت Aspose.Cells for Java 8.5.0 تصنيف استراتيجية حساب الدقة لإضافة المزيد من المرونة لمحرك حساب الصيغ للحصول على النتائج المطلوبة. تحدد هذه الاستراتيجية معالجة الدقة في الحساب. وبسبب مشكلة الدقة في الحساب العددي IEEE 754 النقطي المحمول ، قد لا يتم حساب بعض الصيغ التي تبدو بسيطة لتعطي النتائج المتوقعة لذلك قد قدمت آخر اصدارات وواجهة برمجة التطبيقات الحقول التالية للحصول على النتائج المطلوبة وفقا للاختيار.

1. CalculationPrecisionStrategy.DECIMAL: يستخدم العدد العشري كعامل عند الإمكان ، وهو الأكثر غير كفئة من حيث الأداء.
1. CalculationPrecisionStrategy.ROUND: يقوم بتقريب نتائج الحساب وفقا للرقم الكبير.
1. CalculationPrecisionStrategy.NONE: لا يتم تطبيق استراتيجية بالتالي أثناء الحساب يستخدم المحرك القيمة العددية الأصلية كعامل ويعيد النتيجة مباشرة. هذا الخيار هو الأكثر كفاءة وينطبق على معظم الحالات.
### **الطرق المضافة لاستخدام خيارات الحساب**
مع إصدار v8.5.0 ، قامت واجهة برمجة التطبيقات Aspose.Cells بإضافة إصدارات فائضة من طريقة حساب الصيغ كما هو مدرج أدناه.

- Workbook.calculateFormula(CalculationOptions)
- Worksheet.calculateFormula(CalculationOptions options, bool recursive)
- Cell.calculate(CalculationOptions)
### **تمت إضافة حقل تعدادي PasteType.ROW_HEIGHTS**
قدمت Aspose.Cells APIs حقل تعدادي PasteType.ROW_HEIGHTS لغرض نسخ أطوال الصف أثناء نسخ المدى. عند تعيين خصائص PasteOptions.PasteType إلى (PasteType.ROW_HEIGHTS) سيتم نسخ أطوال جميع الصفوف داخل المدى المصدر إلى المدى الوجهة.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Source worksheet

Worksheet srcSheet = workbook.getWorksheets().get(0);

//Add destination worksheet

Worksheet dstSheet = workbook.getWorksheets().add("Destination Sheet");

//Set the row height of the 4th row

//This row height will be copied to destination range

srcSheet.getCells().setRowHeight(3, 50);

//Create source range to be copied

Range srcRange = srcSheet.getCells().createRange("A1:D10");

//Create destination range in destination worksheet

Range dstRange = dstSheet.getCells().createRange("A1:D10");

//PasteOptions, we want to copy row heights of source range to destination range

PasteOptions opts = new PasteOptions();

opts.setPasteType(PasteType.ROW_HEIGHTS);

//Copy source range to destination range with paste options

dstRange.copy(srcRange, opts);

//Write informative message in cell D4 of destination worksheet

dstSheet.getCells().get("D4").putValue("Row heights of source range copied to destination range");

//Save the workbook in xlsx format

workbook.save("output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **تمت إضافة خاصية SheetRender.PageScale**
عند تعيين تكوين الصفحة بتصغير باستخدام خيار **مناسب لعرض صفحة واحدة عرضيًا حسب عدد n صفحات عمودية m** ، يقوم Microsoft Excel بحساب معامل تكبير التكوين. يمكن تحقيق الأمر نفسه باستخدام خاصية SheetRender.PageScale المكشوفة بواسطة Aspose.Cells for Java 8.5.0. تعيد هذه الخاصية قيمة عشرية يمكن تحويلها إلى قيمة نسبية. على سبيل المثال ، إذا كانت تعيد 0.507968245 فهذا يعني أن معامل التكبير هو 51%.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Put some data in these cells

worksheet.getCells().get("A4").putValue("Test");

worksheet.getCells().get("S4").putValue("Test");

//Set paper size

worksheet.getPageSetup().setPaperSize(PaperSizeType.PAPER_A_4);

//Set fit to pages wide as 1

worksheet.getPageSetup().setFitToPagesWide(1);

//Calculate page scale via sheet render

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

//Write the page scale value

System.out.println(sr.getPageScale());

{{< /highlight >}}
### **تمت إضافة تعدادية CellValueFormatStrategy**
Aspose.Cells for Java 8.5.0 قد أضافت تعدادية جديدة CellValueFormatStrategy للتعامل مع الحالات التي يجب فيها استخراج قيم الخلية مع أو بدون تطبيق التنسيق. تحتوي تعدادية CellValueFormatStrategy على الحقول التالية. 

1. CellValueFormatStrategy.CELL_STYLE: مُنسَّقة فقط باستخدام تنسيق الخلية الأصلي.
1. CellValueFormatStrategy.DISPLAY_STYLE: مُنسَّقة باستخدام النمط المعروض للخلية.
1. CellValueFormatStrategy.NONE: غير مُنسَّقة.
### **تمت إضافة الدالة Cell.getStringValue**
من أجل استخدام تعدادية CellValueFormatStrategy ، قام v8.5.0 بتعريض الدالة Cell.getStringValue التي يمكن أن تقبل معلمة من نوع CellValueFormatStrategy وتُرجع القيمة تبعًا للخيار المحدد.

يُظهر مقتطف الكود التالي كيفية استخدام دالة Cells.getStringValue المعرضة حديثًا.

**Java**

{{< highlight csharp >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cell A1

Cell cell = worksheet.getCells().get("A1");

//Put value inside the cell

cell.putValue(0.012345);

//Format the cell that it should display 0.01 instead of 0.012345

Style style = cell.getStyle();

style.setNumber(2);

cell.setStyle(style);

//Get string value as Cell Style

String value = cell.getStringValue(CellValueFormatStrategy.CELL_STYLE);

System.out.println(value);

//Get string value without any formatting

value = cell.getStringValue(CellValueFormatStrategy.NONE);

System.out.println(value);

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
