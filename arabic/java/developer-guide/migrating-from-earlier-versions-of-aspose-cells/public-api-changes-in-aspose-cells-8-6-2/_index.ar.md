---
title: API العام التغييرات في Aspose.Cells 8.6.2
type: docs
weight: 220
url: /ar/java/public-api-changes-in-aspose-cells-8-6-2/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.6.1 إلى 8.6.2 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة ، ولكن أيضًا وصف أي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **دعم معاودة الاتصال باستخدام العلامات الذكية**
كشف هذا الإصدار من Aspose.Cells for Java API عن حقل WorkbookDesigner.CallBack وواجهة ISmartMarkerCallBack التي تسمح معًا[الحصول على إشعارات حول مرجع الخلية و / أو العلامة الذكية قيد المعالجة](/cells/ar/java/getting-notifications-while-merging-data-with-smart-markers/) . يوضح الجزء التالي من التعليمات البرمجية استخدام واجهة ISmartMarkerCallBack لتحديد فئة جديدة تتعامل مع استدعاء طريقة WorkbookDesigner.process.

**Java**

{{< highlight "csharp" >}}

 public class SmartMarkerCallBack implements ISmartMarkerCallBack 

{

	Workbook workbook;

	SmartMarkerCallBack(Workbook workbook)

	{

	    this.workbook = workbook;

	}



	@Override

	public void process(int sheetIndex, int rowIndex, int colIndex, String tableName, String columnName)

	{

	    System.out.println("Processing Cell : " + workbook.getWorksheets().get(sheetIndex).getName() + "!" + CellsHelper.cellIndexToName(rowIndex, colIndex));

	    System.out.println("Processing Marker : " + tableName + "." + columnName);

	}

}

{{< /highlight >}}

تتضمن بقية العملية تحميل جدول بيانات المصمم الذي يحتوي على العلامات الذكية باستخدام WorkbookDesigner أو إنشاء واحد من البداية ومعالجته عن طريق تعيين مصدر البيانات. ومع ذلك ، لتمكين الإعلامات ، من الضروري تعيين خاصية WorkbookDesigner.CallBack قبل استدعاء طريقة WorkbookDesigner.process كما هو موضح أدناه.

**Java**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook designer

WorkbookDesigner report = new WorkbookDesigner();

//Get the first worksheet of the workbook

Worksheet sheet = report.getWorkbook().getWorksheets().get(0);

//Set the Variable Array marker to a cell

//You may also place this Smart Marker into a template file manually using Excel and then open this file via WorkbookDesigner 

sheet.getCells().get("A1").putValue("&=$VariableArray");

//Set the data source for the marker(s)

report.setDataSource("VariableArray", new String[]{ "English", "Arabic", "Hindi", "Urdu", "French" });

//Set the CallBack property

report.setCallBack(new SmartMarkerCallBack(report.getWorkbook()));

//Process the markers

report.process(false);

{{< /highlight >}}
### **تمت إضافة طريقة Chart.toPdf**
كشف Aspose.Cells for Java 8.6.2 طريقة Chart.toPdf التي يمكن استخدامها لعرض شكل المخطط مباشرة إلى تنسيق PDF. تقبل الطريقة المذكورة حاليًا معلمة من النوع String كموقع مسار الملف لتخزين الملف الناتج على القرص.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

 //Load spreadsheet containing charts

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first chart inside the worksheet

Chart chart = worksheet.getCharts().get(0);

//Save the chart in PDF format

chart.toPdf(outputFilePath);

{{< /highlight >}}
### **أسلوب Workbook.removeUnusedStyles مضاف**
 كشف Aspose.Cells for Java 8.6.2 طريقة Workbook.removeUnusedStyles التي يمكن استخدامها[قم بإزالة كافة كائنات النمط غير المستخدمة من مجموعة الأنماط](/cells/ar/java/remove-unused-styles-inside-the-workbook/). 

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.removeUnusedStyles();

{{< /highlight >}}
### **الخاصية Cells. تمت إضافة النمط**
يمكن استخدام الخاصية Cells.Style للوصول إلى النمط الخاص بورقة العمل الذي يمثل النمط الافتراضي.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.getWorksheets().get(0).getCells().getStyle();

{{< /highlight >}}
### **تمت إضافة الأحداث لـ GridWeb**
Aspose.Cells.GridWeb for Java 8.6.2 كشف الحدثين الجديدين التاليين.

1. AjaxCallFinished: يتم إطلاقه عند انتهاء تحديث AJAX لعنصر التحكم. (يجب تعيين EnableAJAX على true).
1. CellModifiedOnAjax: الحرائق عندما يتم تعديل الخلية في استدعاء AJAX.
