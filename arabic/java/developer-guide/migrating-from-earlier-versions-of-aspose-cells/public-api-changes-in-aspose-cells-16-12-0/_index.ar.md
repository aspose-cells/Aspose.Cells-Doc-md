---
title: التغييرات العامة في واجهة برمجة التطبيقات العامة في Aspose.Cells 16.12.0
type: docs
weight: 370
url: /ar/java/public-api-changes-in-aspose-cells-16-12-0/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات لـ Aspose.Cells من الإصدار 16.11.0 إلى 16.12.0 التي قد تكون مهمة لمطوري الوحدات/التطبيقات. وتشمل ليس فقط الطرق العامة الجديدة والمحدثة، والفئات المضافة والمحذوفة وما إلى ذلك، ولكن أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **تصفية الكائنات أثناء وقت التحميل**
أصبح Aspose.Cells 16.12.0 يكشف فئة LoadFilter جنبًا إلى جنب مع خاصية LoadOptions.LoadFilter التي يمكنها معًا التحكم في نوع البيانات المراد تحميلها أثناء تهيئة نسخة من Workbook من ملف قالب.

إليك سيناريو استخدام بسيط لتحميل خصائص المستند فقط من ملف قالب.

**Java**

{{< highlight csharp >}}

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

الكود التالي يقوم بتحميل كل شيء من جدول بيانات موجود باستثناء الرسوم البيانية.

**Java**

{{< highlight csharp >}}

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

الكود التالي يقوم بتحميل بيانات الخلية فقط (بالإضافة إلى الصيغ) والتنسيق من جدول بيانات موجود.

**Java**

{{< highlight csharp >}}

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
### **تمت إضافة عنصر FileFormatType.OTS إلى التعداد**
أصبح Aspose.Cells 16.12.0 يضيف مدخل OTS إلى تعداد FileFormatType من أجل كشف تنسيق ملفات OTS.

الكود التالي يستخدم FileFormatType.OTS.

**Java**

{{< highlight csharp >}}

 //Detect the format of the file

FileFormatInfo fileFormatInfo = FileFormatUtil.detectFileFormat(dir + "sample.ots");



//Check if stream is of type OTS

if(fileFormatInfo.getFileFormatType() == FileFormatType.OTS);

{

	System.out.println("It is an OTS file");

}

{{< /highlight >}}
### **تمت إضافة خاصية BuiltInDocumentPropertyCollection.ScaleCrop**
أصبح Aspose.Cells 16.12.0 يضيف خاصية ScaleCrop إلى فئة BuiltInDocumentPropertyCollection. تُشير ScaleCrop إلى وضع عرض مصغر المستند. يمكن ضبط هذا العنصر على true لتمكين تحجيم مصغر المستند وفقًا للعرض، بينما يمكن ضبطه على false لتمكين قص مصغر المستند لعرض الجزء الذي يناسب العرض.
### **تمت إضافة خاصية BuiltInDocumentPropertyCollection.LinksUpToDate**
أصبح Aspose.Cells 16.12.0 يكشف أيضًا خاصية LinksUpToDate لفئة BuiltInDocumentPropertyCollection. تُشير خاصية LinksUpToDate ما إذا كانت الروابط الفائقة في مستند محدّثة. 
### **تمت إضافة طريقة Workbook.exportXml**
أصبح Aspose.Cells 16.12.0 يكشف عن طريقة Workbook.exportXml التي تسمح بتخزين بيانات الخريطة XML في مسار ملف محدد. تقبل طريقة Workbook.exportXml معلمتين حيث يجب أن تكون المعلمة الأولى من النوع string اسم الخريطة XML ويجب أن يكون المعلمة الثانية مكان مسار الملف لتخزين بيانات XML.
### **تمت إضافة طريقة WorksheetCollection.createRange**
أصبح Aspose.Cells 16.12.0 يضيف طريقة WorksheetCollection.createRange التي تُسمح بإنشاء نطاق استنادًا إلى عنوان (مرجع المنطقة الخلية) وفهرس الورقة.

يستخدم الكود التالي طريقة WorksheetCollection.createRange لإنشاء مجموعة من الخلايا تمتد من A1 إلى A2 في الورقة العمل الأولى (الافتراضية).

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access WorksheetCollection from the Workbook

WorksheetCollection sheets = book.getWorksheets();



//Create a range in first worksheet

Range range = sheets.createRange("A1:A2", 0);

{{< /highlight >}}
## **واجهات برمجة التطبيق القديمة**
### **خاصية Obsoleted LoadOptions.LoadDataOptions**
الرجاء استخدام خاصية LoadOptions.LoadFilter كبديل.
### **خاصية Obsoleted LoadOptions.LoadDataFilterOptions**
الرجاء استخدام خاصية LoadOptions.LoadFilter بدلاً منها.
### **خاصية Obsoleted LoadOptions.OnlyLoadDocumentProperties**
الرجاء استخدام خاصية LoadOptions.LoadFilter كبديل.
### **خاصية Obsoleted LoadOptions.LoadDataAndFormatting**
الرجاء استخدام خاصية LoadOptions.LoadFilter بدلاً منها.

{{% alert color="primary" %}} 

تم مشاركة مقاطع الشفرة لجميع واجهات برمجة التطبيقات المهجورة أعلاه.

{{% /alert %}}
## **حذف واجهات برمجة التطبيق**
### **خاصية محذوفة DataLabels.Rotation**
الرجاء استخدام خاصية DataLabels.RotationAngle بدلاً منها.
### **خاصية محذوفة Title.Rotation**
الرجاء استخدام خاصية Title.RotationAngle كبديل.
### **خاصية محذوفة DataLabels.Background**
من المستحسن استخدام خاصية DataLabels.BackgroundMode بدلاً منها.
### **خاصية محذوفة DisplayUnitLabel.Rotation**
يرجى النظر في استخدام خاصية DisplayUnitLabel.RotationAngle لتحقيق نفس الهدف.
### **تم حذف الطريقة Title.getCharacters.**
يرجى استخدام طريقة Title.characters بدلاً من ذلك.
