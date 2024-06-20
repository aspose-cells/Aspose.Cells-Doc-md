---
title: التغييرات العامة في واجهة برمجة التطبيقات العامة في Aspose.Cells 8.6.1
type: docs
weight: 210
url: /ar/java/public-api-changes-in-aspose-cells-8-6-1/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات ل Aspose.Cells من الإصدار 8.6.0 إلى 8.6.1 التي قد تهم مطوري الوحدات / التطبيقات. يتضمن ليس فقط طرق عامة جديدة ومحدثة، وإضافة الفصول، ولكن أيضًا وصفًا لأي تغييرات في السلوك وراء الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **دعم نوع الوصلة HTML المستهدف**
قد عرضة هذا الإصدار من Aspose.Cells for Java API تعدادًا بإسم HtmlLinkTargetType جنبًا إلى جنب مع خاصية جديدة HtmlSaveOptions.LinkTargetType التي تتيح معًا [تعيين نوع الهدف للروابط في جدول البيانات أثناء التحويل إلى تنسيق HTML](/cells/ar/java/change-the-html-link-target-type/). قيم التعداد HtmlLinkTargetType المحتملة كما يلي حيث القيمة الافتراضية SELF.

1. HtmlLinkTargetType.BLANK: يفتح المستند/الصفحة المحددة في نافذة أو لسان جديد.
1. HtmlLinkTargetType.PARENT: يفتح المستند/الصفحة المحددة ضمن الإطار الرئيسي.
1. HtmlLinkTargetType.SELF: يفتح المستند/الصفحة المحددة في نفس الإطار الذي تم فيه النقر على الرابط.
1. HtmlLinkTargetType.TOP: يفتح المستند/الصفحة المحددة في الهيكل الكامل للنافذة.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the LinkTargetType property to appropriate value

options.setLinkTargetType(HtmlLinkTargetType.BLANK);


//Convert the spreadsheet to HTML with preset HtmlSaveOptions

workbook.save(outputFilePath, options);

{{< /highlight >}}
### **تمت إضافة طريقة VbaModuleCollection.remove**
قد عرض إصدار Aspose.Cells for Java 8.6.1 تعريضًا آخر للطريقة VbaModuleCollection.remove التي يمكن أن تقبل الآن مثيلًا من Worksheet لإزالة جميع الوحدات VBA المرتبطة بالورقة المحددة.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.getVbaProject().getModules();

//Remove the VBA modules from specific Worksheet

modules.remove(workbook.getWorksheets().get(0));

{{< /highlight >}}
### **تمت إضافة طريقة RangeCollection.add**
قد عرض إصدار Aspose.Cells for Java 8.6.1 طريقة RangeCollection.Add التي يمكن استخدامها لإضافة كائنات Range لمجموعة النطاقات لورقة العمل معينة.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook

Cells cells = workbook.getWorksheets().get(0).getCells();

//Retrieve the range collection from first worksheet of the Workbook

RangeCollection ranges = cells.getRanges();

//Add another range to the collection

ranges.add(cells.createRange("A1:B4"));

{{< /highlight >}}
### **تمت إضافة طريقة Cell.setCharacters**
يمكن استخدام طريقة Cell.setCharacters لتحديث أجزاء النص الغني لكائن الخلية المعطى. طريقة Cell.getCharacters يجب استخدامها للوصول إلى أجزاء النص ثم يمكن القيام بالتعديلات باستخدام طريقة Cell.setCharacters في حين أن طريقة الحصول **get** تعيد مجموعة من كائنات FontSetting التي يمكن التلاعب بها لتحديد مختلف الخصائص مثل اسم الخط، لون الخط، سمك الخط الخ. ويمكن استخدام طريقة **set** لتطبيق التغييرات.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the cells containing the Rich Text

Cell cell = worksheet.getCells().get("A1");

//Retrieve the array of FontSetting from the cell

FontSetting[] settings = cell.getCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].getFont().setName("Arial");

//Set the updated FontSetting

cell.setCharacters(settings);

{{< /highlight >}}
### **تمت إضافة خاصية VbaProject.isSigned**
Aspose.Cells for Java 8.6.1 قد فتح خاصية VbaProject.isSigned التي يمكن استخدامها لاختبار ما إذا كان VbaProject في الدفتر موقعة أم لا. تعيد الخاصية من نوع بوليان قيمة صحيحة إذا كان المشروع موقعا.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VbaProject from the Workbook

VbaProject project = workbook.getVbaProject();

//Test if VbaProject is signed

if (project.isSigned())

{

    System.out.println("VBA Project is Signed");

}

else

{

	System.out.println("VBA Project is not Signed");

}

{{< /highlight >}}
## **تم تعديل واجهات برمجة التطبيقات**
### **تم تعديل طريقة Cell.getFormatConditions**
مع إصدار v8.6.1، تم تعديل واجهة برمجة التطبيقات Aspose.Cells for Java التي تعيد النوع من طريقة Cell.getFormatConditions لتعيد الآن مجموعة من النوع FormatConditionCollection.
## **واجهات برمجة التطبيق القديمة**
### **تم تهجير طريقة Workbook.checkWriteProtectedPassword**
مع إصدار v8.6.1، تم وضع علامة تحذير على طريقة Workbook.checkWriteProtectedPassword. يوصى باستخدام طريقة WorkbookSettings.WriteProtection.validatePassword التي يمكنها قبول قيمة نصية كمعلمة وتعيد قيمة بوليانية إذا كانت كلمة المرور تطابقت مع كلمة المرور المحددة مسبقًا لجدول البيانات.
