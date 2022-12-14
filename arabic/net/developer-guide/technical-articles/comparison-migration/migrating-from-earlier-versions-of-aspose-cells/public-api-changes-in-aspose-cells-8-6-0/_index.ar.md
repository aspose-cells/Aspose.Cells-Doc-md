---
title: API العام التغييرات في Aspose.Cells 8.6.0
type: docs
weight: 190
url: /ar/net/public-api-changes-in-aspose-cells-8-6-0/
---
{{% alert color="primary" %}} 

 يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.5.2 إلى 8.6.0 والتي قد تهم مطوري الوحدة النمطية / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ،[الفئات المضافة وما إلى ذلك.](/cells/ar/net/public-api-changes-in-aspose-cells-8-6-0/)ولكن أيضًا وصف لأية تغييرات في السلوك خلف الكواليس عام Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **دعم معالجة البيانات الوصفية بدون إنشاء كائن من المصنف**
كشف هذا الإصدار من Aspose.Cells for .NET API عن فئتين جديدتين هما WorkbookMetadata & MetadataOptions جنبًا إلى جنب مع MetadataType للتعداد الجديد الذي يسمح الآن بمعالجة خصائص المستند (بيانات التعريف) دون إنشاء مثيل لـ Workbook. فئة WorkbookMetadata خفيفة الوزن وتوفر آلية سهلة الاستخدام وفعالة للغاية[قراءة وكتابة وتحديث خصائص المستند دون التأثير على الأداء العام](/cells/ar/net/using-workbookmetadata/).

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet with WorkbookMetadata while specifying appropriate MetadataType

MetadataOptions options = new MetadataOptions(MetadataType.DocumentProperties);

WorkbookMetadata metadata = new WorkbookMetadata(filePath, options);

//Set some properties

metadata.CustomDocumentProperties.Add("test", "test");

//Save the metadata info to spreadsheet

metadata.Save(filePath);

{{< /highlight >}}


### **تمت إضافة الخاصية HtmlSaveOptions.ExportFrameScriptsAndProperties**
كشف Aspose.Cells for .NET 8.6.0 خاصية HtmlSaveOptions.ExportFrameScriptsAndProperties التي يمكن استخدامها للتأثير على إنشاء نصوص إضافية أثناء تحويل جداول البيانات إلى تنسيق HTML. باستخدام الإعدادات الافتراضية ، تقوم واجهات برمجة تطبيقات Aspose.Cells بتصدير جدول البيانات بتنسيق HTML حيث يقوم تطبيق Excel بالتصدير ، أي ؛ يحتوي HTML الناتج على الإطارات والتعليقات الشرطية التي تكتشف نوع المتصفح وتضبط التخطيط وفقًا لذلك. القيمة الافتراضية لخاصية HtmlSaveOptions.ExportFrameScriptsAndProperties صحيحة ، وهذا يعني ؛ يتم التصدير وفقًا لمعايير Excel. ومع ذلك ، إذا تم تعيين الخاصية على خطأ ، فلن يتم تعيين API[إنشاء البرامج النصية المتعلقة بالإطارات والتعليقات الشرطية](/cells/ar/net/disable-exporting-frame-scripts-and-document-properties/). في هذه الحالة ، يمكن عرض HTML الناتج بشكل صحيح في أي متصفح ، ومع ذلك ، لا يمكن استيراده مرة أخرى باستخدام واجهات برمجة تطبيقات Aspose.Cells.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 //Load the spreadsheet

Workbook book = new Workbook(filePath);

//Disable exporting frame scripts and document properties

HtmlSaveOptions options = new HtmlSaveOptions();

options.ExportFrameScriptsAndProperties = false;

//Save spreadsheet as HTML

book.Save("output.html", options);

{{< /highlight >}}


### **شكل الخاصية تمت إضافة اسم ماركو**
 كشف Aspose.Cells for .NET 8.6.0 خاصية Shape.MarcoName التي يمكن استخدامها[قم بتعيين أي وحدة نمطية لـ VBA إلى عنصر تحكم النموذج](/cells/ar/net/assign-macro-to-form-control/) مثل هذا الزر من أجل توفير التفاعل. الخاصية هي من نوع سلسلة لذلك يمكنها قبول اسم الوحدة وتخصيصها لعنصر التحكم.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook workbook = new Workbook();

//Access first default worksheet

Worksheet sheet = workbook.Worksheets[0];

//Add a module to the worksheet

int moduleIdx = workbook.VbaProject.Modules.Add(sheet);

//Access newly added module from the collection

VbaModule module = workbook.VbaProject.Modules[moduleIdx];

//Add code to the module

module.Codes =

    "Sub ShowMessage()" + "\r\n" +

    "    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

    "End Sub";

//Add a Button on the worksheet and set its various properties

Aspose.Cells.Drawing.Button button = sheet.Shapes.AddButton(2, 0, 2, 0, 28, 80);

button.Placement = Aspose.Cells.Drawing.PlacementType.FreeFloating;

button.Font.Name = "Tahoma";

button.Font.IsBold = true;

button.Font.Color = System.Drawing.Color.Blue;

button.Text = "Aspose";

//Assign the VBA module to the button

button.MacroName = sheet.Name + ".ShowMessage";

//Save the result

workbook.Save("output.xlsm");

{{< /highlight >}}


### **تمت إضافة الخاصية OoxmlSaveOptions.UpdateZoom**
مع إصدار v8.6.0 ، كشف API Aspose.Cells for .NET API خاصية OoxmlSaveOptions.UpdateZoom التي يمكن استخدامها لتحديث PageSetup.Zoom إذا PageSetup.FitToPagesWide و / أو PageSetup.FitToPages تم استخدام خصائص ورقة العمل للتحكم.
