---
title: تغييرات في واجهة برمجة التطبيقات العامة في Aspose.Cells 8.6.2
type: docs
weight: 210
url: /ar/net/public-api-changes-in-aspose-cells-8-6-2/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات ل Aspose.Cells من الإصدار 8.6.1 إلى 8.6.2 التي قد تكون مثيرة للاهتمام لمطوري الوحدات/التطبيقات. فهو يتضمن ليس فقط الطرق العامة الجديدة والمحدثة والفصول المضافة، ولكن أيضًا وصفًا لأي تغييرات في السلوك الذي يكمن وراء الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **دعم معاودة الاتصال مع علامات Smart Markers**
قد قام هذا الإصدار من API Aspose.Cells for .NET بعرض خاصية WorkbookDesigner.CallBack وواجهة ISmartMarkerCallBack التي تسمح سويًا بالتنبيهات حول مرجع الخلية و / أو العلامة الذكية التي يتم معالجتها. يظهر الكود التالي استخدام واجهة ISmartMarkerCallBack لتحديد فئة جديدة تدير الاستدعاء لطريقة WorkbookDesigner.Process.

**C#**

{{< highlight csharp >}}

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



بقية العملية تتضمن تحميل جدول البيانات التصميمي الذي يحتوي على علامات ذكية باستخدام WorkbookDesigner ومعالجته عن طريق تعيين مصدر البيانات. ومع ذلك، من الضروري تعيين خاصية WorkbookDesigner.CallBack لتمكين الإشعارات قبل استدعاء طريقة WorkbookDesigner.Process كما يُوضح أدناه.

**C#**

{{< highlight csharp >}}

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


### **تمت إضافة طريقة Chart.ToPdf**
قد عرض الإصدار 8.6.2 لـ Aspose.Cells for .NET طريقة Chart.ToPdf التي يمكن استخدامها لعرض الشكل البياني مباشرة إلى تنسيق PDF. تقبل الطريقة المذكورة حاليًا معلمة من نوع سلسلة كموقع لملف لتخزين الملف الناتج على القرص.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

 //Load spreadsheet containing charts

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first chart inside the worksheet

Chart chart = worksheet.Charts[0];

//Save the chart in PDF format

chart.ToPdf(outputFilePath);

{{< /highlight >}}


### **أضيفت طريقة Workbook.RemoveUnusedStyles**
Aspose.Cells for .NET 8.6.2 قد عرضت طريقة Workbook.RemoveUnusedStyles التي يمكن استخدامها لـ [إزالة جميع كائنات النمط غير المستخدمة من مجموعة أنماط](/cells/ar/net/remove-unused-styles-inside-the-workbook/).

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.RemoveUnusedStyles();

{{< /highlight >}}


### **تمت إضافة خاصية Cells.Style**
يمكن استخدام خاصية Cells.Style للوصول إلى النمط لورقة العمل التي تمثل النمط الافتراضي.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.Worksheets[0].Cells.Style;

{{< /highlight >}}


### **تمت إضافة الأحداث لـ GridWeb**
أصبح في Aspose.Cells.GridWeb for .NET 8.6.2 تعريض الحدثين الجديدين التاليين.

1. AjaxCallFinished: يُطلق عند اكتمال التحديث بتقنية AJAX للتحكم. (يجب تعيين EnableAJAX إلى true).
1. CellModifiedOnAjax: يتم إطلاق الحدث عند تعديل الخلية في استدعاء AJAX.
