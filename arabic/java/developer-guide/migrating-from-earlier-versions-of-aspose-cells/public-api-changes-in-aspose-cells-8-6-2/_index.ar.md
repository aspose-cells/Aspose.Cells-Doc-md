---
title: تغييرات في واجهة برمجة التطبيقات العامة في Aspose.Cells 8.6.2
type: docs
weight: 220
url: /ar/java/public-api-changes-in-aspose-cells-8-6-2/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات ل Aspose.Cells من الإصدار 8.6.1 إلى 8.6.2 التي قد تكون مثيرة للاهتمام لمطوري الوحدات/التطبيقات. فهو يتضمن ليس فقط الطرق العامة الجديدة والمحدثة والفصول المضافة، ولكن أيضًا وصفًا لأي تغييرات في السلوك الذي يكمن وراء الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **دعم معاودة الاتصال مع علامات Smart Markers**
قد فتح هذا الإصدار من واجهة برمجة التطبيقات Aspose.Cells for Java حقل WorkbookDesigner.CallBack وواجهة ISmartMarkerCallBack التي تسمح معًا بالحصول على [الإشعارات حول مرجع الخلية و/أو علامة Smart Marker التي يتم معالجتها](/cells/ar/java/getting-notifications-while-merging-data-with-smart-markers/). يوضح الكود التالي استخدام واجهة ISmartMarkerCallBack لتعريف صنف جديد يتعامل مع المعاودة لطريقة WorkbookDesigner.process. 

**Java**

{{< highlight csharp >}}

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

ويتضمن بقية العملية تحميل جدول البيانات المصمم يحتوي على علامات Smart Markers مع WorkbookDesigner أو إنشاء واحدة من البداية ومعالجتها عن طريق تعيين مصدر البيانات. ومع ذلك، من أجل تمكين الإشعارات، من الضروري تعيين خاصية WorkbookDesigner.CallBack قبل استدعاء طريقة WorkbookDesigner.process كما هو موضح أدناه.

**Java**

{{< highlight csharp >}}

 //Instantiate a new Workbook designer

WorkbookDesigner report = new WorkbookDesigner();

//Get the first worksheet of the workbook

Worksheet sheet = report.getWorkbook().getWorksheets().get(0);

//Set the Variable Array marker to a cell

//You may also place this Smart Marker into a template file manually using Excel and then open this file via WorkbookDesigner 

sheet.getCells().get("A1").putValue("&=$VariableArray");

//Set the data source for the marker(s)

report.setDataSource("VariableArray", new String[] { "English", "Arabic", "Hindi", "Urdu", "French" });

//Set the CallBack property

report.setCallBack(new SmartMarkerCallBack(report.getWorkbook()));

//Process the markers

report.process(false);

{{< /highlight >}}
### **تمت إضافة طريقة Chart.toPdf**
Aspose.Cells for Java 8.6.2 قامت بتعريض طريقة Chart.toPdf التي يمكن استخدامها لعرض شكل الرسم البياني مباشرة إلى تنسيق PDF. تقبل الطريقة المذكورة حاليًا معلمًا من نوع String كموقع لمسار الملف الناتج لتخزين الملف الناتج على القرص.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

 //Load spreadsheet containing charts

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first chart inside the worksheet

Chart chart = worksheet.getCharts().get(0);

//Save the chart in PDF format

chart.toPdf(outputFilePath);

{{< /highlight >}}
### **تمت إضافة طريقة Workbook.removeUnusedStyles**
Aspose.Cells for Java 8.6.2 قامت بتعريض طريقة Workbook.removeUnusedStyles التي يمكن استخدامها لإزالة جميع كائنات النمط غير المستخدمة من مجموعة أنماط. 

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.removeUnusedStyles();

{{< /highlight >}}
### **تمت إضافة خاصية Cells.Style**
يمكن استخدام خاصية Cells.Style للوصول إلى النمط لورقة العمل التي تمثل النمط الافتراضي.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.getWorksheets().get(0).getCells().getStyle();

{{< /highlight >}}
### **تمت إضافة الأحداث لـ GridWeb**
قام Aspose.Cells.GridWeb لجافا 8.6.2 بتعريض الأحداث الجديدة التالية.

1. AjaxCallFinished: يتم إطلاق الحدث عند انتهاء التحديث الآجاك للتحكم. (يجب تعيين EnableAJAX على true).
1. CellModifiedOnAjax: يتم إطلاق الحدث عند تعديل الخلية في استدعاء AJAX.
