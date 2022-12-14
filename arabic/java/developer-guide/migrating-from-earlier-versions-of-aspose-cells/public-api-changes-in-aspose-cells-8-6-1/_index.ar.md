---
title: API العام التغييرات في Aspose.Cells 8.6.1
type: docs
weight: 210
url: /ar/java/public-api-changes-in-aspose-cells-8-6-1/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.6.0 إلى 8.6.1 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة ، ولكن أيضًا وصف أي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **دعم نوع هدف ارتباط HTML**
كشف هذا الإصدار من Aspose.Cells for Java API عن تعداد يسمى HtmlLinkTargetType مع خاصية جديدة HtmlSaveOptions.LinkTargetType التي تسمح معًا[اضبط النوع المستهدف للروابط في جدول البيانات أثناء التحويل إلى تنسيق HTML](/cells/ar/java/change-the-html-link-target-type/). القيم المحتملة لتعداد HtmlLinkTargetType كما يلي حيث تكون القيمة الافتراضية هي SELF.

1. HtmlLinkTargetType.BLANK: يفتح المستند / الصفحة المرتبطة في نافذة أو علامة تبويب جديدة.
1. HtmlLinkTargetType.PARENT: يفتح المستند / الصفحة المرتبطة في الإطار الأصل.
1. HtmlLinkTargetType.SELF: يفتح المستند / الصفحة المرتبطة في نفس الإطار حيث تم ربط الارتباط.
1. HtmlLinkTargetType.TOP: يفتح المستند / الصفحة المرتبطة في النص الكامل للنافذة.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the LinkTargetType property to appropriate value

options.setLinkTargetType(HtmlLinkTargetType.BLANK);


//Convert the spreadsheet to HTML with preset HtmlSaveOptions

workbook.save(outputFilePath, options);

{{< /highlight >}}
### **الأسلوب VbaModuleCollection.remove مضاف**
كشف Aspose.Cells for Java 8.6.1 عن حمل زائد آخر لطريقة VbaModuleCollection.remove التي يمكنها الآن قبول مثيل من ورقة العمل لإزالة جميع وحدات VBA النمطية المرتبطة بورقة العمل المحددة.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.getVbaProject().getModules();

//Remove the VBA modules from specific Worksheet

modules.remove(workbook.getWorksheets().get(0));

{{< /highlight >}}
### **الأسلوب RangeCollection.add مضاف**
كشف Aspose.Cells for Java 8.6.1 عن مجموعة RangeCollection. أضف طريقة يمكن استخدامها لإضافة كائنات النطاق إلى مجموعة النطاقات لورقة عمل معينة.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook

Cells cells = workbook.getWorksheets().get(0).getCells();

//Retrieve the range collection from first worksheet of the Workbook

RangeCollection ranges = cells.getRanges();

//Add another range to the collection

ranges.add(cells.createRange("A1:B4"));

{{< /highlight >}}
### **الطريقة Cell.setCharacters added**
 يمكن استخدام طريقة Cell.setCharacters في[تحديث أجزاء النص المنسق](/cells/ar/java/access-and-update-the-portions-of-rich-text-of-cell/) لكائن Cell معطى. يتم استخدام طريقة Cell.getCharacters للوصول إلى أجزاء النص ومن ثم يمكن إجراء التعديلات باستخدام طريقة Cell.setCharacters بينما**احصل على** تقوم الطريقة بإرجاع مجموعة من كائنات FontSetting التي يمكن معالجتها لتعيين خصائص مختلفة ، اسم الخط ، ولون الخط ، والجرأة ، إلخ.**تعيين** يمكن استخدام الطريقة لتطبيق التغييرات.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the cells containing the Rich Text

Cell cell = worksheet.getCells().get("A1");

//Retrieve the array of FontSetting from the cell

FontSetting[]settings = cell.getCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].getFont().setName("Arial");

//Set the updated FontSetting

cell.setCharacters(settings);

{{< /highlight >}}
### **تمت إضافة الخاصية VbaProject.isSigned**
 كشف Aspose.Cells for Java 8.6.1 خاصية VbaProject.isSigned التي يمكن استخدامها[اختبار ما إذا كان VbaProject في مصنف تم توقيعه أم لا](/cells/ar/java/check-if-vba-project-in-a-workbook-is-signed/). ترجع خاصية النوع المنطقي "صحيح" إذا تم توقيع المشروع.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

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
## **واجهات برمجة التطبيقات المعدلة**
### **الطريقة Cell.getFormatConditions Modified**
مع إصدار v8.6.1 ، قام Aspose.Cells for Java API بتعديل نوع الإرجاع للطريقة Cell.getFormatConditions التي تقوم الآن بإرجاع مصفوفة من النوع FormatConditionCollection.
## **واجهات برمجة التطبيقات التي عفا عليها الزمن**
### **أسلوب Workbook.checkWriteProtectedPassword قديم**
مع إصدار v8.6.1 ، تم وضع علامة على أسلوب Workbook.checkWriteProtectedPassword بأنه مهمل. يُنصح باستخدام طريقة WorkbookSettings.WriteProtection.validatePassword التي يمكنها قبول قيمة سلسلة كمعامل وإرجاع قيمة منطقية إذا كانت كلمة المرور تتطابق مع كلمة المرور المحددة مسبقًا لجدول البيانات.
