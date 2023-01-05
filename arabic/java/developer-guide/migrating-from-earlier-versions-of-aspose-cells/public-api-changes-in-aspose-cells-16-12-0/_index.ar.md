---
title: عام API تغييرات في Aspose.Cells 16.12.0
type: docs
weight: 370
url: /ar/java/public-api-changes-in-aspose-cells-16-12-0/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 16.11.0 إلى 16.12.0 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة والمحذوفة وما إلى ذلك ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **تصفية الكائنات في وقت التحميل**
كشف Aspose.Cells 16.12.0 عن فئة LoadFilter مع خاصية LoadOptions.LoadFilter التي يمكنها معًا التحكم في نوع البيانات التي سيتم تحميلها أثناء تهيئة مثيل مصنف من ملف قالب.

فيما يلي سيناريو استخدام بسيط لتحميل خصائص المستند فقط من ملف قالب.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing LoadDataFilterOptions.DocumentProperties to constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.DOCUMENT_PROPERTIES);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}

المقتطف التالي يقوم بتحميل كل شيء من جدول بيانات موجود باستثناء الرسوم البيانية.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing parameter to the constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.CHART);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}

يؤدي اتباع التعليمات البرمجية إلى تحميل بيانات الخلية فقط (جنبًا إلى جنب مع الصيغ) والتنسيق من جدول بيانات موجود.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing parameter to the constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.CELL_DATA);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}
### **تمت إضافة تعداد FileFormatType.OTS**
أضاف Aspose.Cells 16.12.0 إدخال OTS إلى تعداد FileFormatType لاكتشاف تنسيق ملفات OTS.

المقتطف التالي يستخدم FileFormatType.OTS.

**Java**

{{< highlight "csharp" >}}

 //Detect the format of the file

FileFormatInfo fileFormatInfo = FileFormatUtil.detectFileFormat(dir + "sample.ots");



//Check if stream is of type OTS

if(fileFormatInfo.getFileFormatType() == FileFormatType.OTS);

{

	System.out.println("It is an OTS file");

}

{{< /highlight >}}
### **تمت إضافة خاصية BuiltInDocumentPropertyCollection.ScaleCrop**
قام Aspose.Cells 16.12.0 بإضافة خاصية ScaleCrop إلى فئة BuiltInDocumentPropertyCollection. يشير ScaleCrop إلى وضع عرض مصغر المستند. يتيح ضبط هذا العنصر على "صواب" قياس الصورة المصغرة للمستند حسب العرض بينما يتيح تعيينه على "خطأ" إمكانية اقتصاص الصورة المصغرة للمستند لإظهار القسم الذي يناسب العرض.
### **تمت إضافة خاصية BuiltInDocumentPropertyCollection.LinksUpToDate**
 قام Aspose.Cells 16.12.0 أيضًا بعرض خاصية LinksUpToDate لفئة BuiltInDocumentPropertyCollection. تشير الخاصية LinksUpToDate إلى ما إذا كانت الارتباطات التشعبية في مستند محدثة.
### **تمت إضافة طريقة Workbook.exportXml**
كشف Aspose.Cells 16.12.0 عن طريقة Workbook.exportXml التي تسمح بتخزين بيانات مخطط XML إلى مسار الملف المحدد. يقبل الأسلوب Workbook.exportXml معلمتين حيث يجب أن تكون المعلمة الأولى من سلسلة النوع اسم مخطط XML والمعلمة الثانية يجب أن تكون موقع مسار الملف لتخزين بيانات XML.
### **تمت إضافة طريقة WorksheetCollection.createRange**
أضاف Aspose.Cells 16.12.0 طريقة WorksheetCollection.createRange التي تسمح بإنشاء نطاق بناءً على العنوان (مرجع منطقة الخلية) وفهرس ورقة العمل.

يستخدم المقتطف التالي طريقة WorksheetCollection.createRange لإنشاء نطاق من الخلايا يمتد عبر A1 إلى A2 في ورقة العمل الأولى (الافتراضية).

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access WorksheetCollection from the Workbook

WorksheetCollection sheets = book.getWorksheets();



//Create a range in first worksheet

Range range = sheets.createRange("A1:A2", 0);

{{< /highlight >}}
## **واجهات برمجة التطبيقات التي عفا عليها الزمن**
### **خاصية LoadOptions.LoadDataOptions التي عفا عليها الزمن**
الرجاء استخدام خاصية LoadOptions.LoadFilter كبديل.
### **خاصية LoadOptions.LoadDataFilterOptions التي عفا عليها الزمن**
الرجاء استخدام خاصية LoadOptions.LoadFilter بدلاً من ذلك.
### **خاصية LoadOptions.OnlyLoadDocumentProperties قديمة**
الرجاء استخدام خاصية LoadOptions.LoadFilter كبديل.
### **خاصية LoadOptions.LoadDataAndFormatting قديمة**
الرجاء استخدام خاصية LoadOptions.LoadFilter بدلاً من ذلك.

{{% alert color="primary" %}} 

تمت مشاركة مقتطفات التعليمات البرمجية لجميع واجهات برمجة التطبيقات القديمة أعلاه.

{{% /alert %}}
## **واجهات برمجة التطبيقات المحذوفة**
### **DataLabels المحذوفة. خاصية الدوران**
الرجاء استخدام خاصية DataLabels.RotationAngle بدلاً من ذلك.
### **عنوان محذوف. خاصية الدوران**
يرجى استخدام خاصية Title.RotationAngle كبديل.
### **تم حذف خاصية DataLabels.Background**
يُنصح باستخدام الخاصية DataLabels.BackgroundMode بدلاً من ذلك.
### **تم حذف خاصية DisplayUnitLabel.Rotation**
يرجى التفكير في استخدام خاصية DisplayUnitLabel.RotationAngle لتحقيق نفس الهدف.
### **طريقة Title.getCharacters المحذوفة**
الرجاء استخدام طريقة Title.characters بدلاً من ذلك.
