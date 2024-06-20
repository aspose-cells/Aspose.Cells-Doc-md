---
title: تغييرات الواجهة البرمجية العامة في Aspose.Cells 8.6.0
type: docs
weight: 190
url: /ar/net/public-api-changes-in-aspose-cells-8-6-0/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها في واجهة برمجة التطبيقات العامة لـ Aspose.Cells من الإصدار 8.5.2 إلى 8.6.0 والتي قد تكون مثيرة للاهتمام لمطوري الوحدات/التطبيقات. يشمل ليس فقط الطرق العامة الجديدة والمُحدّثة و[الصفوف المضافة الخلافية الخلافية الخلافة الخلافية الخلافة الخلافة الخلافية الجديدة إلخ](/خلايا/ar/net/التغييرات-في-واجهة-البرمجة-العامة-في-اصوز-خلايا-8-6-0/) ، ولكن أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **دعم لعملية تعديل البيانات الوصفية بدون إنشاء كائن من المصنف**
تم تعريض هذا الإصدار من واجهة برمجة التطبيقات الخارجية Aspose.Cells for .NET فئتين جديدتين هما WorkbookMetadata و MetadataOptions جنبًا إلى جنب مع تعداد جديد MetadataType الذي يسمح الآن بالتلاعب في خصائص المستندات (البيانات الوصفية) دون إنشاء مثيل للجدول. صفيفة WorkbookMetadata خفيفة الوزن وتوفر آلية سهلة الاستخدام جدًا وفعالة لـ [قراءة وكتابة وتحديث خصائص المستندات دون التأثير على الأداء الشامل](/الخلايا/ar/net/استخدام-workbookmetadata/).

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet with WorkbookMetadata while specifying appropriate MetadataType

MetadataOptions options = new MetadataOptions(MetadataType.DocumentProperties);

WorkbookMetadata metadata = new WorkbookMetadata(filePath, options);

//Set some properties

metadata.CustomDocumentProperties.Add("test", "test");

//Save the metadata info to spreadsheet

metadata.Save(filePath);

{{< /highlight >}}


### **تمت إضافة خاصية HtmlSaveOptions.ExportFrameScriptsAndProperties**
تم تعريض إصدار Aspose.Cells for .NET 8.6.0 خاصية HtmlSaveOptions.ExportFrameScriptsAndProperties التي يمكن استخدامها للتأثير على إنشاء البرمجيات النصية الإضافية أثناء تحويل جداول البيانات إلى تنسيق HTML. باستخدام الإعدادات الافتراضية، تقوم واجهات برمجة التطبيقات من Aspose.Cells بتصدير جدول البيانات إلى تنسيق HTML بنفس الطريقة التي يفعلها تطبيق Excel، أي أن الناتج HTML يحتوي على الإطارات والتعليقات الشرطية التي تكتشف نوع المتصفح وتعدل التصميم وفقًا لذلك. القيمة الافتراضية لخاصية HtmlSaveOptions.ExportFrameScriptsAndProperties هي صحيح، وهذا يعني أن التصدير يتم وفقًا لمعايير Excel. ومع ذلك، إذا كانت الخاصية مُعيَّنة إلى قيمة خاطئة، فلن تقوم واجهات برمجة التطبيقات ب[توليد البرمجيات النصية المتعلقة بالإطارات والتعليقات الشرطية](/الخلايا/ar/net/تعطيل-تصدير-البرامج-النصية-النسيجية-والخصائص-الوثيقة/). في هذه الحالة، يمكن عرض الـ HTML الناتج بشكل صحيح في أي متصفح، ومع ذلك، لا يمكن استيراده مرة أخرى باستخدام واجهات برمجة التطبيقات من Aspose.Cells.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

 //Load the spreadsheet

Workbook book = new Workbook(filePath);

//Disable exporting frame scripts and document properties

HtmlSaveOptions options = new HtmlSaveOptions();

options.ExportFrameScriptsAndProperties = false;

//Save spreadsheet as HTML

book.Save("output.html", options);

{{< /highlight >}}


### **تمت إضافة خاصية Shape.MarcoName**
تم تعريض إصدار Aspose.Cells for .NET 8.6.0 لخاصية Shape.MarcoName التي يمكن استخدامها لـ [تعيين أي وحدة VBA لعنصر تحكم في النموذج](/الخلايا/ar/net/تعيين-الوحدة-لعنصر-التحكم/) مثل زر من أجل توفير التفاعل. الخاصية من نوع سلسلة لذلك يمكنها قبول اسم الوحدة وتعيينه إلى العنصر التحكم.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

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


### **تمت إضافة خاصية OoxmlSaveOptions.UpdateZoom**
مع إصدار الإصدار v8.6.0، فقد قامت واجهة برمجة التطبيقات Aspose.Cells for .NET بفتح خاصية OoxmlSaveOptions.UpdateZoom والتي يمكن استخدامها لتحديث خاصية PageSetup.Zoom إذا تم استخدام PageSetup.FitToPagesWide و / أو PageSetup.FitToPagesTall properties للتحكم في تحجيم ورقة البيانات.
