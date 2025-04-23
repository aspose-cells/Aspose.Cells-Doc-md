---
title: تغييرات الواجهة البرمجية العامة في Aspose.Cells 8.3.0
type: docs
weight: 110
url: /ar/java/public-api-changes-in-aspose-cells-8-3-0/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي طرأت على واجهة برمجة التطبيقات لـ Aspose.Cells من الإصدار 8.2.2 إلى 8.3.0 والتي قد تكون مهمة لمطوري الوحدات / التطبيقات.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **تمت إضافة خاصية WorkbookSettings.AutoRecover**
تمت إضافة متسلسلة الحصول / التعيين لخاصية AutoRecover إلى صف الورقة الإعدادات بهدف السماح للمطورين بالحصول / التعيين من خيار الاستعادة التلقائية لجداول البيانات في تطبيقاتهم. 

{{% alert color="primary" %}} 

يرجى التحقق من المقال [ضبط الاستعادة التلقائية لأوراق البيانات](http://aspose.com/docs/display/cellsjava/How+to+set+AutoRecover+property+of+Workbook) لمزيد من المعلومات.

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

settings.setAutoRecover(true);

{{< /highlight >}}

### **تمت إضافة خاصية WorkbookSettings.CrashSave**
تمت إضافة متسلسلة الحصول / التعيين لخاصية CrashSave إلى صف الإعدادات بحيث تشير الخاصية من نوع البوليان إذا كان التطبيق قد قام بحفظ ملف العمل بعد وقوع حادث.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getCrashSave());

{{< /highlight >}}

### **تمت إضافة خاصية WorkbookSettings.DataExtractLoad**
تمت إضافة متسلسلة الحصول / التعيين لخاصية DataExtractLoad إلى صف الإعدادات بهدف السماح للمطورين بالحصول / التعيين لمعلومات حول الاسترداد الأخير. إذا كانت خاصية DataExtractLoad تُرجع true فهذا يدل على أن عملية الاسترداد قد تمت على ملف العمل.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getDataExtractLoad());

{{< /highlight >}}

### **تمت إضافة خاصية WorkbookSettings.RepairLoad**
تمت إضافة متسلسلة الحصول / التعيين لخاصية RepairLoad إلى صف الإعدادات بحيث تشير الخاصية من نوع البوليان إذا تم إصلاح جدول البيانات خلال جلسة التحميل الأخيرة مع تطبيق Excel.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getRepairLoad());

{{< /highlight >}}

### **تمت إضافة خاصية TxtLoadOptions.KeepExactFormat**
تمت إضافة خاصية KeepExactFormat إلى فئة TxtLoadOptions التي تشير إلى ما إذا كان يجب الاحتفاظ بالتنسيق الدقيق لقيمة الخلية عند تحويل النص/النص إلى أرقام أو تاريخ. تمت إضافة هذه الخاصية لمطابقة سلوك تطبيق MS Excel لتحميل القيم الزمنية أو الرقمية من ملفات CSV. من أجل محاكاة سلوك MS Excel ، قم بتعيين الخاصية KeepExactFormat على false ، في حين أن القيمة الافتراضية هي true بحيث سيتم تنسيق قيمة الخلية كالنص في ملف CSV.

**Java**

{{< highlight csharp >}}

 TxtLoadOptions options = new TxtLoadOptions();

options.setKeepExactFormat(false);

Workbook book = new Workbook("sample.csv", options);

{{< /highlight >}}

### **تمت إضافة خاصية Shape.Id**
تمت إضافة getter/setter للخاصية Shape.Id في الإصدار 8.3.0 من أجل تحديد هوية كل عنصر شكل بشكل فريد في جدول بيانات معين. تساعد هذه الخاصية الجديدة أيضا في تحديد كائنات الرسم البياني بشكل فريد في جدول بيانات كما هو مبين أدناه.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

ChartCollection charts = book.getWorksheets().get(0).getCharts();

for(int index = 0; index <= charts.getCount(); index++)

{

    Chart chart = charts.get(index);

    Shape shape = (Shape)chart.getChartObject();

    System.out.println(shape.getId());

}

{{< /highlight >}}

### **تمت إضافة طريقة setPositionAuto إلى فئة PlotArea**
تمت إضافة الطريقة setPositionAuto إلى فئة PlotArea التي تساعد في ضبط منطقة الرسم البياني إلى وضع تلقائي.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

Chart chart = book.getWorksheets().get(0).getCharts().get(0);

chart.getPlotArea().setPositionAuto();

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
