---
title: التغييرات العامة في واجهة برمجة التطبيقات العامة في Aspose.Cells 8.6.1
type: docs
weight: 200
url: /ar/net/public-api-changes-in-aspose-cells-8-6-1/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات ل Aspose.Cells من الإصدار 8.6.0 إلى 8.6.1 التي قد تهم مطوري الوحدات / التطبيقات. يتضمن ليس فقط طرق عامة جديدة ومحدثة، وإضافة الفصول، ولكن أيضًا وصفًا لأي تغييرات في السلوك وراء الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **دعم نوع الوصلة HTML المستهدف**
تمت فتح تعداد Aspose.Cells for .NET API هذا تعداد بعنوان HtmlLinkTargetType جنباً إلى جنب مع خاصية جديدة HtmlSaveOptions.LinkTargetType التي تسمح معًا بتعيين نوع الهدف للروابط في ورقة البيانات أثناء التحويل إلى تنسيق HTML. القيم الممكنة لتعداد HtmlLinkTargetType هي كما يلي حيث القيمة الافتراضية هي Self.

1. HtmlLinkTargetType.Blank: يفتح المستند / الصفحة المرتبطة في نافذة أو علامة تبويب جديدة.
1. HtmlLinkTargetType.Parent: يفتح المستند / الصفحة المرتبطة في الإطار الأصلي.
1. HtmlLinkTargetType.Self: يفتح المستند / الصفحة المرتبطة في نفس الإطار الذي تم النقر على الرابط فيه.
1. HtmlLinkTargetType.Top: يفتح المستند / الصفحة المرتبطة في الجزء العلوي للنافذة.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the LinkTargetType property to appropriate value

options.LinkTargetType = HtmlLinkTargetType.Blank;

//Convert the spreadsheet to HTML with preset HtmlSaveOptions

workbook.Save(outputFilePath, options);

{{< /highlight >}}


### **تمت إضافة VbaModuleCollection.Remove Method**
قام Aspose.Cells for .NET 8.6.1 بفتح تحميل إضافي لطريقة VbaModuleCollection.Remove يمكنه الآن قبول مثيلًا من ورقة البيانات لإزالة جميع وحدات VBA المرتبطة بورقة البيانات المحددة.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.VbaProject.Modules;

//Remove the VBA modules from specific Worksheet

modules.Remove(workbook.Worksheets[0]);

{{< /highlight >}}


### **تمت إضافة RangeCollection.Add Method**
قام Aspose.Cells for .NET 8.6.1 بفتح طريقة RangeCollection.Add التي يمكن استخدامها لإضافة كائنات Range إلى مجموعة النطاقات لورقة بيانات معينة.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook

Cells cells = workbook.Worksheets[0].Cells;

//Retrieve the range collection from first worksheet of the Workbook

RangeCollection ranges = cells.Ranges;

//Add another range to the collection

ranges.Add(cells.CreateRange("A1:B4"));

{{< /highlight >}}


### **تمت إضافة طريقة Cell.SetCharacters**
يمكن استخدام الطريقة Cell.SetCharacters لتحديث جزء من النص الغني لكائن Cell معين. ويُستخدم الطريقة Cell.GetCharacters للوصول إلى أجزاء من النص ثم يمكن القيام بالتعديلات باستخدام الطريقة Cell.SetCharacters في حين أن الطريقة **Get** تُرجع مصفوفة من كائنات FontSetting التي يمكن التلاعب بها لتعيين خصائص مختلفة مثل اسم الخط، لون الخط، العرض إلخ ويمكن استخدام الطريقة **Set** لتطبيق التغييرات.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.Worksheets[0];

//Access the cells containing the Rich Text

Cell cell = worksheet.Cells["A1"];

//Retrieve the array of FontSetting from the cell

FontSetting[] settings = cell.GetCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].Font.Name = "Arial";

//Set the updated FontSetting

cell.SetCharacters(settings);

{{< /highlight >}}


### **تمت إضافة خاصية VbaProject.IsSigned**
Aspose.Cells for .NET 8.6.1 قد عرض خاصية VbaProject.IsSigned التي يمكن استخدامها لـ [اختبار ما إذا كان مشروع VbaProject في الورقة العمل موقعًا أم لا](/cells/ar/net/check-if-vba-project-in-a-workbook-is-signed/). تقوم الخاصية من نوع Boolean بإرجاع قيمة صحيحة إذا كان المشروع موقعًا.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

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
## **تم تعديل واجهات برمجة التطبيقات**
### **تم تعديل طريقة Cell.GetFormatConditions**
مع إصدار الإصدار 8.6.1، فإن API Aspose.Cells for .NET قد قام بتعديل نوع القيمة المُرجعة لطريقة Cell.GetFormatConditions التي تُرجع الآن مصفوفة من نوع FormatConditionCollection.
## **واجهات برمجة التطبيق القديمة**
### **تم تهجير طريقة Workbook.CheckWriteProtectedPassword**
مع إصدار الإصدار 8.6.1، فقد تم وضع علامة تهجير على طريقة Workbook.CheckWriteProtectedPassword. من المستحسن استخدام طريقة WorkbookSettings.WriteProtection.ValidatePassword التي يمكنها قبول قيمة سلسلة كقيمة معلمة وتُرجع قيمة Boolean إذا كانت كلمة المرور مطابقة لكلمة المرور المحددة لجدول البيانات.
{{< app/cells/assistant language="csharp" >}}
