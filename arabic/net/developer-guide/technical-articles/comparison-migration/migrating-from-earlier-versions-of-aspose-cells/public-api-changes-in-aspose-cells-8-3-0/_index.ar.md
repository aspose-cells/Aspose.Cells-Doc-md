---
title: API العام التغييرات في Aspose.Cells 8.3.0
type: docs
weight: 100
url: /ar/net/public-api-changes-in-aspose-cells-8-3-0/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.2.2 إلى 8.3.0 والتي قد تهم مطوري الوحدة / التطبيق.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **تمت إضافة خاصية WorkbookSettings.AutoRecover**
تمت إضافة الخاصية الجديدة AutoRecover إلى فئة WorkbookSettings للسماح للمطورين بتعيين خيار الاسترداد التلقائي لجداول البيانات في تطبيقاتهم.

{{% alert color="primary" %}} 

 يرجى مراجعة المقال[إعداد الاسترداد التلقائي لجدول البيانات](http://aspose.com/docs/display/cellsnet/How+to+set+AutoRecover+property+of+Workbook) للمزيد من المعلومات.

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

settings.AutoRecover = true;

{{< /highlight >}}


### **تمت إضافة خاصية WorkbookSettings.CrashSave**
تمت إضافة خاصية النوع المنطقي CrashSave إلى فئة WorkbookSettings التي تشير إلى ما إذا كان التطبيق قد حفظ ملف المصنف آخر مرة بعد حدوث عطل أم لا.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.CrashSave);

{{< /highlight >}}


### **تمت إضافة خاصية WorkbookSettings.DataExtractLoad**
تمت إضافة الخاصية DataExtractLoad إلى فئة WorkbookSettings للسماح للمطورين بالحصول على المعلومات المتعلقة بعملية الاسترداد الأخيرة. إذا كانت الخاصية DataExtractLoad ترجع صحيحًا ، فهذا يشير إلى أن استعادة البيانات قد تم إجراؤها على جدول البيانات.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.DataExtractLoad);

{{< /highlight >}}


### **تمت إضافة إعدادات مصنف الملكية**
تشير الخاصية RepairLoad إلى ما إذا كان قد تم إصلاح جدول البيانات في آخر تحميل باستخدام تطبيق Excel.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.RepairLoad);

{{< /highlight >}}


### **تمت إضافة الخاصية TxtLoadOptions.KeepExactFormat**
تمت إضافة الخاصية KeepExactFormat إلى فئة TxtLoadOptions التي تشير إلى ما إذا كان يجب الاحتفاظ بالتنسيق الدقيق لقيمة الخلية عند تحويل السلسلة / النص إلى أرقام أو DateTime. تمت إضافة هذه الخاصية لمطابقة سلوك تطبيق MS Excel لتحميل DateTime أو القيم الرقمية من ملفات CSV. لمحاكاة سلوك MS Excel ، قم بتعيين الخاصية KeepExactFormat على false ، بينما القيمة الافتراضية هي true ، لذا سيتم تنسيق قيمة الخلية كسلسلة في ملف CSV.

**C#**

{{< highlight "csharp" >}}

 var options = new TxtLoadOptions();

options.KeepExactFormat = false;

var book = new Workbook("sample.csv", options);

{{< /highlight >}}


### **شكل الملكية. أضيفت**
تمت إضافة معرف الخاصية إلى فئة الشكل لتعريف كل كائن شكل بشكل فريد في ورقة spredsheet المحددة. تساعد هذه الخاصية الجديدة أيضًا في تحديد كائنات المخطط في جدول بيانات كما هو موضح أدناه.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

foreach(Chart chart in book.Worksheets[0].Charts)

{

    var shape = (Shape)chart.ChartObject;

    Console.WriteLine(shape.Id);

}

{{< /highlight >}}


### **الطريقة PlotArea.SetPositionAuto المضافة**
تمت إضافة طريقة SetPositionAuto إلى فئة PlotArea التي تساعد في تعيين منطقة رسم المخطط على الوضع التلقائي.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var chart = book.Worksheets[0].Charts[0];

chart.PlotArea.SetPositionAuto();

{{< /highlight >}}
