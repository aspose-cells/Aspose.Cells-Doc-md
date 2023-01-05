---
title: API العام التغييرات في Aspose.Cells 8.6.1
type: docs
weight: 200
url: /ar/net/public-api-changes-in-aspose-cells-8-6-1/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.6.0 إلى 8.6.1 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة ، ولكن أيضًا وصف أي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **دعم لنوع هدف الارتباط HTML**
 كشف هذا الإصدار من Aspose.Cells for .NET API عن تعداد يسمى HtmlLinkTargetType مع خاصية جديدة HtmlSaveOptions.LinkTargetType التي تسمح معًا[اضبط النوع المستهدف للروابط في جدول البيانات أثناء التحويل إلى تنسيق HTML](/cells/ar/net/change-the-html-link-target-type/). القيم المحتملة لتعداد HtmlLinkTargetType كما يلي حيث تكون القيمة الافتراضية هي Self.

1. HtmlLinkTargetType.Blank: يفتح المستند / الصفحة المرتبطة في نافذة أو علامة تبويب جديدة.
1. HtmlLinkTargetType.Parent: يفتح المستند / الصفحة المرتبطة في الإطار الأصل.
1. HtmlLinkTargetType.Self: يفتح المستند / الصفحة المرتبطة في نفس الإطار حيث تم ربط الارتباط.
1. HtmlLinkTargetType.Top: يفتح المستند / الصفحة المرتبطة في نص النافذة بالكامل.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the LinkTargetType property to appropriate value

options.LinkTargetType = HtmlLinkTargetType.Blank;

//Convert the spreadsheet to HTML with preset HtmlSaveOptions

workbook.Save(outputFilePath, options);

{{< /highlight >}}


### **طريقة VbaModuleCollection.Remove مضافة**
كشف Aspose.Cells for .NET 8.6.1 حملًا زائدًا آخر لطريقة VbaModuleCollection.Remove التي يمكنها الآن قبول مثيل من ورقة العمل لإزالة جميع وحدات VBA النمطية المرتبطة بورقة العمل المحددة.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.VbaProject.Modules;

//Remove the VBA modules from specific Worksheet

modules.Remove(workbook.Worksheets[0]);

{{< /highlight >}}


### **الطريقة RangeCollection.Add added**
كشف Aspose.Cells for .NET 8.6.1 عن مجموعة RangeCollection. أضف طريقة يمكن استخدامها لإضافة كائنات النطاق إلى مجموعة النطاقات لورقة عمل معينة.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook

Cells cells = workbook.Worksheets[0].Cells;

//Retrieve the range collection from first worksheet of the Workbook

RangeCollection ranges = cells.Ranges;

//Add another range to the collection

ranges.Add(cells.CreateRange("A1:B4"));

{{< /highlight >}}


### **طريقة Cell: إضافة أحرف المجموعة**
 يمكن استخدام طريقة Cell.SetCharacters في[تحديث أجزاء النص المنسق](/cells/ar/net/access-and-update-the-portions-of-rich-text-of-cell/) لكائن Cell معطى. يتم استخدام طريقة Cell.GetCharacters للوصول إلى أجزاء النص ومن ثم يمكن إجراء التعديلات باستخدام طريقة Cell.SetCharacters بينما**يحصل** تقوم الطريقة بإرجاع مجموعة من كائنات FontSetting التي يمكن معالجتها لتعيين خصائص مختلفة ، اسم الخط ، ولون الخط ، والجرأة ، إلخ.**تعيين** يمكن استخدام الطريقة لتطبيق التغييرات.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.Worksheets[0];

//Access the cells containing the Rich Text

Cell cell = worksheet.Cells["A1"];

//Retrieve the array of FontSetting from the cell

FontSetting[]settings = cell.GetCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].Font.Name = "Arial";

//Set the updated FontSetting

cell.SetCharacters(settings);

{{< /highlight >}}


### **خاصية VbaProject.IsSigned**
 كشف Aspose.Cells for .NET 8.6.1 عن VbaProject.signed الخاصية التي يمكن استخدامها[اختبار ما إذا كان VbaProject في مصنف تم توقيعه أم لا](/cells/ar/net/check-if-vba-project-in-a-workbook-is-signed/)ترجع خاصية النوع المنطقي "صحيح" إذا تم توقيع المشروع.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VbaProject from the Workbook

VbaProject project = workbook.VbaProject;

//Test if VbaProject is signed

if (project.IsSigned)

{

    Console.WriteLine("VBA Project is Signed");

}

else

{

    Console.WriteLine("VBA Project is not Signed");

}

{{< /highlight >}}
## **واجهات برمجة التطبيقات المعدلة**
### **الطريقة Cell.GetFormatConditions Modified**
مع إصدار v8.6.1 ، قام Aspose.Cells for .NET API بتعديل نوع الإرجاع لطريقة Cell.GetFormatConditions التي تقوم الآن بإرجاع مصفوفة من النوع FormatConditionCollection.
## **واجهات برمجة التطبيقات التي عفا عليها الزمن**
### **مصنف الأسلوب .CheckWriteProtectedPassword قديم**
مع إصدار v8.6.1 ، تم وضع علامة على أسلوب Workbook.CheckWriteProtectedPassword بأنه مهمل. يُنصح باستخدام طريقة WorkbookSettings.WriteProtection.ValidatePassword التي يمكنها قبول قيمة سلسلة كمعامل وإرجاع قيمة منطقية إذا كانت كلمة المرور تتطابق مع كلمة المرور المحددة مسبقًا لجدول البيانات.
