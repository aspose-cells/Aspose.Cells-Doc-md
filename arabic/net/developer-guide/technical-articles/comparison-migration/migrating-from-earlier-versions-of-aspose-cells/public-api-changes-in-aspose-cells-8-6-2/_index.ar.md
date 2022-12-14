---
title: API العام التغييرات في Aspose.Cells 8.6.2
type: docs
weight: 210
url: /ar/net/public-api-changes-in-aspose-cells-8-6-2/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.6.1 إلى 8.6.2 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة ، ولكن أيضًا وصف أي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **دعم معاودة الاتصال باستخدام العلامات الذكية**
 كشف هذا الإصدار من Aspose.Cells for .NET API عن خاصية WorkbookDesigner.CallBack وواجهة ISmartMarkerCallBack التي تسمح معًا[الحصول على إشعارات حول مرجع الخلية و / أو العلامة الذكية قيد المعالجة](/cells/ar/net/getting-notifications-while-merging-data-with-smart-markers/). يوضح الجزء التالي من التعليمات البرمجية استخدام واجهة ISmartMarkerCallBack لتحديد فئة جديدة تتعامل مع استدعاء أسلوب WorkbookDesigner.Process.

**C#**

{{< highlight "csharp" >}}

 class SmartMarkerCallBack : ISmartMarkerCallBack

{

    Workbook workbook;

    internal SmartMarkerCallBack(Workbook workbook)

    {

        this.workbook = workbook;

    }

    public void Process(int sheetIndex, int rowIndex, int colIndex, string tableName, string columnName)

    {

        Console.WriteLine("Processing Cell : " + workbook.Worksheets[sheetIndex].Name + "!" + CellsHelper.CellIndexToName(rowIndex, colIndex));

        Console.WriteLine("Processing Marker : " + tableName + "." + columnName);

    }

}

{{< /highlight >}}



تتضمن بقية العملية تحميل جدول بيانات المصمم الذي يحتوي على العلامات الذكية باستخدام WorkbookDesigner ومعالجته عن طريق تعيين مصدر البيانات. ومع ذلك ، لتمكين الإعلامات ، من الضروري تعيين خاصية WorkbookDesigner.CallBack قبل استدعاء طريقة WorkbookDesigner.Process كما هو موضح أدناه.

**C#**

{{< highlight "csharp" >}}

 //Loading the designer spreadsheet in an instance of Workbook

Workbook workbook = new Workbook(inputFilePath);

//Loading the instance of Workbook in an instance of WorkbookDesigner

WorkbookDesigner designer = new WorkbookDesigner(workbook);

//Set the WorkbookDesigner.CallBack property to an instance of newly created class

designer.CallBack = new SmartMarkerCallBack(workbook);

//Set the data source 

designer.SetDataSource(table);

//Process the Smart Markers in the designer spreadsheet

designer.Process(false);

{{< /highlight >}}


### **طريقة الرسم البياني. toPdf مضاف**
 كشف Aspose.Cells for .NET 8.6.2 الرسم البياني. طريقة toPdf التي يمكن استخدامها[تقديم شكل المخطط مباشرة إلى تنسيق PDF](/cells/ar/net/convert-an-excel-chart-to-image/). تقبل الطريقة المذكورة حاليًا معلمة من سلسلة النوع كموقع مسار الملف لتخزين الملف الناتج على القرص.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 //Load spreadsheet containing charts

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first chart inside the worksheet

Chart chart = worksheet.Charts[0];

//Save the chart in PDF format

chart.ToPdf(outputFilePath);

{{< /highlight >}}


### **أسلوب المصنف. تمت إضافة RemoveUnusedStyles**
 كشف Aspose.Cells for .NET 8.6.2 المصنف. طريقة RemoveUnusedStyles التي يمكن استخدامها[قم بإزالة كافة كائنات النمط غير المستخدمة من مجموعة الأنماط](/cells/ar/net/remove-unused-styles-inside-the-workbook/).

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.RemoveUnusedStyles();

{{< /highlight >}}


### **الخاصية Cells. تمت إضافة النمط**
يمكن استخدام الخاصية Cells.Style للوصول إلى النمط الخاص بورقة العمل الذي يمثل النمط الافتراضي.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.Worksheets[0].Cells.Style;

{{< /highlight >}}


### **تمت إضافة الأحداث لـ GridWeb**
Aspose.Cells.GridWeb for .NET 8.6.2 كشف الحدثين الجديدين التاليين.

1. AjaxCallFinished: يتم إطلاقه عند انتهاء تحديث AJAX لعنصر التحكم. (يجب تعيين EnableAJAX على صحيح).
1. CellModifiedOnAjax: الحرائق عندما يتم تعديل الخلية في استدعاء AJAX.
