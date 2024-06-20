---
title: تغييرات الواجهة البرمجية العامة في Aspose.Cells 8.3.0
type: docs
weight: 100
url: /ar/net/public-api-changes-in-aspose-cells-8-3-0/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي طرأت على واجهة برمجة التطبيقات لـ Aspose.Cells من الإصدار 8.2.2 إلى 8.3.0 والتي قد تكون مهمة لمطوري الوحدات / التطبيقات.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **تمت إضافة خاصية WorkbookSettings.AutoRecover**
تمت إضافة الخاصية الجديدة AutoRecover إلى فئة WorkbookSettings للسماح للمطورين بتعيين خيار الاسترداد التلقائي لجداول البيانات في تطبيقاتهم.

{{% alert color="primary" %}} 

يرجى التحقق من المقال [ضبط استرداد تلقائي لجدول البيانات](http://aspose.com/docs/display/cellsnet/How+to+set+AutoRecover+property+of+Workbook) لمزيد من المعلومات.

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

settings.AutoRecover = true;

{{< /highlight >}}


### **تمت إضافة خاصية WorkbookSettings.CrashSave**
تمت إضافة خاصية CrashSave من النوع المنطقي إلى فئة WorkbookSettings التي تشير إلى ما إذا كانت التطبيق قد حفظ المصنف بعد حدوث تعطل.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.CrashSave);

{{< /highlight >}}


### **تمت إضافة خاصية WorkbookSettings.DataExtractLoad**
تمت إضافة خاصية DataExtractLoad إلى فئة WorkbookSettings للسماح للمطورين بالحصول على معلومات حول آخر عملية استرداد. إذا كانت الخاصية DataExtractLoad تقوم بإرجاع true فهذا يشير إلى أن عملية استرداد البيانات قد تمت على جدول البيانات.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.DataExtractLoad);

{{< /highlight >}}


### **تمت إضافة خاصية WorkbookSettings.RepairLoad**
تشير خاصية RepairLoad إذا كان قد تمت إصلاح ورقة الجدول في آخر تحميل بتطبيق Excel.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.RepairLoad);

{{< /highlight >}}


### **تمت إضافة خاصية TxtLoadOptions.KeepExactFormat**
تمت إضافة خاصية KeepExactFormat إلى فئة TxtLoadOptions التي تشير إلى ما إذا كان يجب الاحتفاظ بالتنسيق الدقيق لقيمة الخلية عند تحويل النص/النص إلى أرقام أو تاريخ. تمت إضافة هذه الخاصية لمطابقة سلوك تطبيق MS Excel لتحميل القيم الزمنية أو الرقمية من ملفات CSV. من أجل محاكاة سلوك MS Excel ، قم بتعيين الخاصية KeepExactFormat على false ، في حين أن القيمة الافتراضية هي true بحيث سيتم تنسيق قيمة الخلية كالنص في ملف CSV.

**C#**

{{< highlight csharp >}}

 var options = new TxtLoadOptions();

options.KeepExactFormat = false;

var book = new Workbook("sample.csv", options);

{{< /highlight >}}


### **تمت إضافة خاصية Shape.Id**
تمت إضافة خاصية Id إلى فئة Shape لتحديد كل كائن شكل بشكل فريد في ورقة الجدول المحددة. تساعد هذه الخاصية الجديدة أيضًا في تحديد كائنات الرسم البياني في جداول البيانات كما هو موضح أدناه.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

foreach(Chart chart in book.Worksheets[0].Charts)

{

    var shape = (Shape)chart.ChartObject;

    Console.WriteLine(shape.Id);

}

{{< /highlight >}}


### **تمت إضافة الطريقة SetPositionAuto إلى فئة PlotArea**
تمت إضافة الطريقة SetPositionAuto إلى فئة PlotArea التي تساعد في ضبط منطقة رسم الرسم البياني إلى الوضع التلقائي.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var chart = book.Worksheets[0].Charts[0];

chart.PlotArea.SetPositionAuto();

{{< /highlight >}}
