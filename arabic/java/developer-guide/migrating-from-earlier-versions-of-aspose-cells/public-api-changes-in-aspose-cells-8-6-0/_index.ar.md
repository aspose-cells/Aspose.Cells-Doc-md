---
title: تغييرات الواجهة البرمجية العامة في Aspose.Cells 8.6.0
type: docs
weight: 200
url: /ar/java/public-api-changes-in-aspose-cells-8-6-0/
---

{{% alert color="primary" %}} 

يصف هذا الوثيقة التغييرات في واجهة برمجة Aspose.Cells من الإصدار 8.5.2 إلى 8.6.0 التي قد تهم مطوري الوحدات / التطبيقات. إنها تشمل ليس فقط الطرق العامة الجديدة والمحدثة، [الفئات المضافة إلخ](/cells/ar/java/public-api-changes-in-aspose-cells-8-6-0/)، ولكن أيضا وصف لأي تغييرات في السلوك في أسفل الستائر في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **دعم لعملية تعديل البيانات الوصفية بدون إنشاء كائن من المصنف**
قامت هذه الإصدارة من Aspose.Cells for Java بعرض فئتين جديدتين هما WorkbookMetadata و MetadataOptions جنبًا إلى جنب مع تعداد جديد MetadataType الذي يسمح الآن بتعديل خصائص المستند (البيانات الوصفية) بدون إنشاء مثيل للورقة العمل. فئة WorkbookMetadata خفيفة الوزن وتوفر آلية سهلة الاستخدام وفعالة لـ [قراءة وكتابة وتحديث خصائص المستند دون التأثير على الأداء العام](/cells/ar/java/using-workbookmetadata/). 

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

 //Open Workbook metadata while specifying the appropriate MetadataType

MetadataOptions options = new MetadataOptions(MetadataType.DOCUMENT_PROPERTIES);

WorkbookMetadata metaWorkbook = new WorkbookMetadata("sample.xlsx", options);

//Set some properties

metaWorkbook.getCustomDocumentProperties().add("test", "test");

//Save the metadata information to the spreadsheet file

metaWorkbook.save(filePath);

{{< /highlight >}}
### **تمت إضافة خاصية HtmlSaveOptions.ExportFrameScriptsAndProperties**
قامت الإصدارة 8.6.0 من Aspose.Cells for Java بعرض خاصية HtmlSaveOptions.ExportFrameScriptsAndProperties التي يمكن استخدامها للتأثير على إنشاء السكريبتات الإضافية أثناء تحويل الجداول الجدولية إلى تنسيق HTML. مع الإعدادات الافتراضية، تقوم واجهات برمجة Aspose.Cells بتصدير الجداول الجدولية بتنسيق HTML كما يفعل تطبيق Excel في التصدير، أي; يحتوي HTML الناتج على الإطارات والتعليقات الشرطية، التي تكتشف نوع المتصفح وتضبط التخطيط وفقًا لذلك. القيمة الافتراضية لخاصية HtmlSaveOptions.ExportFrameScriptsAndProperties هي true، وهذا يعني؛ يتم التصدير وفقًا لمعايير Excel. إذا تم ضبط الخاصية على false، فإن الواجهة البرمجية لن تقوم [بتوليد السكربتات المتعلقة بالإطارات وتعليقات المستند](/cells/ar/java/disable-exporting-frame-scripts-and-document-properties/). في هذه الحالة، يمكن عرض HTML الناتج بشكل صحيح في أي متصفح، ومع ذلك، لا يمكن استيراده مرة أخرى باستخدام واجهات برمجة Aspose.Cells.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

 //Load the spreadsheet

Workbook book = new Workbook(filePath);

//Disable exporting frame scripts and document properties

HtmlSaveOptions options = new HtmlSaveOptions();

options.setExportFrameScriptsAndProperties(false);

//Save spreadsheet as HTML

book.save("output.html", options)

{{< /highlight >}}
### **تمت إضافة خاصية Shape.MarcoName**
قامت الإصدارة 8.6.0 من Aspose.Cells for Java بعرض خاصية Shape.MarcoName التي يمكن استخدامها لـ [تعيين وحدة VBA لتحكم النموذج](/cells/ar/java/assign-macro-code-to-form-control/) مثل زر من أجل توفير التفاعل. الخاصية من نوع سلسلة لذلك يمكنها قبول اسم الوحدة وتعيينه للتحكم.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

 //Create a new Workbook object

Workbook workbook = new Workbook();

//Get the instance of first default worksheet

Worksheet sheet = workbook.getWorksheets().get(0);

//Add a new module to the first worksheet

int moduleIdx = workbook.getVbaProject().getModules().add(sheet);

//Get the instance of newly added module

VbaModule module = workbook.getVbaProject().getModules().get(moduleIdx);

//Add module code

module.setCodes("Sub ShowMessage()" + "\r\n" +

        "    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

        "End Sub");

//Create a new button to the worksheet and set its various properties

Button button = (Button) sheet.getShapes().addShape(MsoDrawingType.BUTTON, 2, 0, 2, 0, 28, 80);

button.setPlacement(PlacementType.FREE_FLOATING);

button.getFont().setName("Tahoma");

button.getFont().setBold(true);

button.getFont().setColor(Color.getBlue());

button.setText("Aspose");

//Assign the newly added module to the button

button.setMacroName(module.getName() + ".ShowMessage" );

//Save the spreadsheet in XLSM format

workbook.save("output.xlsm");

{{< /highlight >}}
### **تمت إضافة خاصية OoxmlSaveOptions.UpdateZoom**
مع الإصدار 8.6.0، قامت واجهات برمجة Aspose.Cells for Java بعرض خاصية OoxmlSaveOptions.UpdateZoom التي يمكن استخدامها لتحديث PageSetup.Zoom إذا كانت خصائص PageSetup.FitToPagesWide و / أو PageSetup.FitToPagesTall قد تم استخدامها للتحكم في تحجيم ورقة العمل.
