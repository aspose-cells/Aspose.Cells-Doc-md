---
title: API العام التغييرات في Aspose.Cells 8.3.0
type: docs
weight: 110
url: /ar/java/public-api-changes-in-aspose-cells-8-3-0/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.2.2 إلى 8.3.0 والتي قد تهم مطوري الوحدة / التطبيق.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **تمت إضافة خاصية WorkbookSettings.AutoRecover**
تمت إضافة أداة الإدخال / الضبط للخاصية الاسترداد التلقائي إلى فئة WorkbookSettings للسماح للمطورين بالحصول على / تعيين خيار الاسترداد التلقائي لجداول البيانات في تطبيقاتهم.

{{% alert color="primary" %}} 

 يرجى مراجعة المقال[إعداد الاسترداد التلقائي لجدول البيانات](http://aspose.com/docs/display/cellsjava/How+to+set+AutoRecover+property+of+Workbook) للمزيد من المعلومات.

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

settings.setAutoRecover(true);

{{< /highlight >}}

### **تمت إضافة خاصية WorkbookSettings.CrashSave**
تمت إضافة أداة جلب / أداة تعيين الخاصية CrashSave إلى فئة WorkbookSettings. تشير الخاصية Boolean type إلى ما إذا كان التطبيق قد حفظ ملف المصنف مؤخرًا بعد حدوث عطل أم لا.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getCrashSave());

{{< /highlight >}}

### **تمت إضافة خاصية WorkbookSettings.DataExtractLoad**
تمت إضافة أداة الإدخال / الضبط الخاصة بالخاصية DataExtractLoad إلى فئة WorkbookSettings للسماح للمطورين بالحصول على / تعيين المعلومات المتعلقة بعملية الاسترداد الأخيرة. إذا كانت الخاصية DataExtractLoad ترجع صحيحًا ، فهذا يشير إلى أن استعادة البيانات قد تم إجراؤها على ملف المصنف.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getDataExtractLoad());

{{< /highlight >}}

### **تمت إضافة إعدادات مصنف الملكية**
تمت إضافة getter / setter للخاصية RepairLoad إلى فئة WorkbookSettings. تشير خاصية Boolean type إلى ما إذا كان قد تم إصلاح جدول البيانات في جلسة التحميل الأخيرة باستخدام تطبيق Excel.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getRepairLoad());

{{< /highlight >}}

### **تمت إضافة الخاصية TxtLoadOptions.KeepExactFormat**
تمت إضافة الخاصية KeepExactFormat إلى فئة TxtLoadOptions التي تشير إلى ما إذا كان يجب الاحتفاظ بالتنسيق الدقيق لقيمة الخلية عند تحويل السلسلة / النص إلى أرقام أو DateTime. تمت إضافة هذه الخاصية لمطابقة سلوك تطبيق MS Excel لتحميل التاريخ والوقت أو القيم الرقمية من ملفات CSV. لمحاكاة سلوك MS Excel ، قم بتعيين الخاصية KeepExactFormat على false ، بينما القيمة الافتراضية هي true ، لذلك سيتم تنسيق قيمة الخلية كسلسلة في ملف CSV.

**Java**

{{< highlight "csharp" >}}

 TxtLoadOptions options = new TxtLoadOptions();

options.setKeepExactFormat(false);

Workbook book = new Workbook("sample.csv", options);

{{< /highlight >}}

### **شكل الملكية. أضيفت**
أضاف الإصدار v8.3.0 أداة الإدخال / الضبط للخاصية Shape.Id من أجل التعرف بشكل فريد على كل كائن شكل في جدول بيانات معين. تساعد هذه الخاصية الجديدة أيضًا في تحديد كائنات المخطط بشكل فريد في جدول بيانات كما هو موضح أدناه.

**Java**

{{< highlight "csharp" >}}

 كتاب المصنف = مصنف جديد ("sample.xlsx") ؛

ChartCollection Charts = book.getWorksheets (). get (0) .getCharts ()؛

 لـ (int index = 0 ؛ index<= charts.getCount(); index++)

{

    Chart chart = charts.get(index);

    Shape shape = (Shape)chart.getChartObject();

    System.out.println(shape.getId());

}

{{< /highlight >}}

### **الطريقة PlotArea.setPositionAuto المضافة**
تمت إضافة طريقة setPositionAuto إلى فئة PlotArea التي تساعد في تعيين منطقة رسم المخطط على الوضع التلقائي.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

Chart chart = book.getWorksheets().get(0).getCharts().get(0);

chart.getPlotArea().setPositionAuto();

{{< /highlight >}}
