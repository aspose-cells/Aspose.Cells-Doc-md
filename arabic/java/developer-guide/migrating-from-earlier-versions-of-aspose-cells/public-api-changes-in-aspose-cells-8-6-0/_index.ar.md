---
title: API العام التغييرات في Aspose.Cells 8.6.0
type: docs
weight: 200
url: /ar/java/public-api-changes-in-aspose-cells-8-6-0/
---
{{% alert color="primary" %}} 

 يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.5.2 إلى 8.6.0 والتي قد تهم مطوري الوحدة النمطية / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ،[الفئات المضافة وما إلى ذلك.](/cells/ar/java/public-api-changes-in-aspose-cells-8-6-0/)ولكن أيضًا وصف لأية تغييرات في السلوك خلف الكواليس عام Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **دعم معالجة البيانات الوصفية بدون إنشاء كائن من المصنف**
كشف هذا الإصدار Aspose.Cells for Java API عن فئتين جديدتين هما WorkbookMetadata & MetadataOptions جنبًا إلى جنب مع MetadataType للتعداد الجديد الذي يسمح الآن بمعالجة خصائص المستند (بيانات التعريف) دون إنشاء مثيل لـ Workbook. فئة WorkbookMetadata خفيفة الوزن وتوفر آلية سهلة الاستخدام وفعالة للغاية[قراءة وكتابة وتحديث خصائص المستند دون التأثير على الأداء العام](/cells/ar/java/using-workbookmetadata/). 

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

 //Open Workbook metadata while specifying the appropriate MetadataType

MetadataOptions options = new MetadataOptions(MetadataType.DOCUMENT_PROPERTIES);

WorkbookMetadata metaWorkbook = new WorkbookMetadata("sample.xlsx", options);

//Set some properties

metaWorkbook.getCustomDocumentProperties().add("test", "test");

//Save the metadata information to the spreadsheet file

metaWorkbook.save(filePath);

{{< /highlight >}}
### **تمت إضافة الخاصية HtmlSaveOptions.ExportFrameScriptsAndProperties**
كشف Aspose.Cells for Java 8.6.0 خاصية HtmlSaveOptions.ExportFrameScriptsAndProperties التي يمكن استخدامها للتأثير على إنشاء نصوص إضافية أثناء تحويل جداول البيانات إلى تنسيق HTML. باستخدام الإعدادات الافتراضية ، تقوم واجهات برمجة تطبيقات Aspose.Cells بتصدير جدول البيانات بتنسيق HTML حيث يقوم تطبيق Excel بالتصدير ، أي ؛ يحتوي HTML الناتج على الإطارات والتعليقات الشرطية التي تكتشف نوع المتصفح وتضبط التخطيط وفقًا لذلك. القيمة الافتراضية لخاصية HtmlSaveOptions.ExportFrameScriptsAndProperties صحيحة ، وهذا يعني ؛ يتم التصدير وفقًا لمعايير Excel. إذا تم تعيين الخاصية على "خطأ" ، فلن يقوم API بذلك[إنشاء البرامج النصية المتعلقة بالإطارات والتعليقات الشرطية](/cells/ar/java/disable-exporting-frame-scripts-and-document-properties/). في هذه الحالة ، يمكن عرض HTML الناتج بشكل صحيح في أي متصفح ، ومع ذلك ، لا يمكن استيراده مرة أخرى باستخدام واجهات برمجة تطبيقات Aspose.Cells.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

 //Load the spreadsheet

Workbook book = new Workbook(filePath);

//Disable exporting frame scripts and document properties

HtmlSaveOptions options = new HtmlSaveOptions();

options.setExportFrameScriptsAndProperties(false);

//Save spreadsheet as HTML

book.save("output.html", options)

{{< /highlight >}}
### **شكل الخاصية تمت إضافة اسم ماركو**
 كشف Aspose.Cells for Java 8.6.0 خاصية Shape.MarcoName التي يمكن استخدامها[قم بتعيين وحدة نمطية لـ VBA إلى عنصر تحكم النموذج](/cells/ar/java/assign-macro-code-to-form-control/) مثل هذا الزر من أجل توفير التفاعل. الخاصية هي من نوع سلسلة لذلك يمكنها قبول اسم الوحدة وتخصيصها لعنصر التحكم.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

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
### **تمت إضافة الخاصية OoxmlSaveOptions.UpdateZoom**
مع إصدار v8.6.0 ، كشف API Aspose.Cells for Java API خاصية OoxmlSaveOptions.UpdateZoom التي يمكن استخدامها لتحديث PageSetup.Zoom إذا PageSetup.FitToPagesWide و / أو PageSetup.FitToPages تم استخدام خصائص ورقة العمل للتحكم.
