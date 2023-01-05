---
title: عام API التغييرات في Aspose.Cells 8.8.3
type: docs
weight: 300
url: /ar/java/public-api-changes-in-aspose-cells-8-8-3/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.8.2 إلى 8.8.3 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة والمحذوفة وما إلى ذلك ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **دعم عناصر تحكم ActiveX**
كشف Aspose.Cells for Java 8.8.3 طريقة addActiveXControl التي تسمح بإضافة عنصر تحكم ActiveX إلى ShapeCollection. تتطلب الطريقة المذكورة أعلاه 7 معلمات لتحديد نوع عنصر التحكم والموقع لوضع التحكم وحجم عنصر التحكم. يمكن تحديد النوع باستخدام تعداد ControlType مع القيم المحتملة التالية.

1. نوع التحكم. CHECK_BOX
1. نوع التحكم
1. ControlType.COMMAND_BUTTON
1. نوع التحكم
1. نوع التحكم
1. نوع التحكم. LIST_BOX
1. نوع التحكم. RADIO_BUTTON
1. نوع التحكم
1. نوع التحكم
1. نوع التحكم. TEXT_BOX
1. نوع التحكم
1. نوع التحكم

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[إضافة عناصر تحكم ActiveX إلى ورقة العمل](/cells/ar/java/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Add Toggle Button ActiveX Control to the ShapeCollection at specified location

Shape shape = sheet.getShapes().addActiveXControl(ControlType.TOGGLE_BUTTON, 4, 0, 4, 0, 100, 30);

//Access the ActiveX Control object and set its linked cell property

ActiveXControl control = shape.getActiveXControl();

control.setLinkedCell("A1");

//Save the result on disc

book.save(dir + "output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **تمت إضافة طريقة LoadOptions.setPaperSize**
Aspose.Cells for Java 8.8.3 يسمح بتعيين حجم ورق الطباعة الافتراضي من إعداد الطابعة الافتراضي أثناء استخدام طريقة LoadOptions.setPaperSize المكشوفة حديثًا كما هو موضح أدناه. يرجى ملاحظة أن معلمة الإدخال للطريقة المذكورة أعلاه هي القيمة من تعداد PaperSizeType الذي يحتوي على أحجام الورق المحددة مسبقًا.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[قم بتحميل جداول بيانات بحجم ورق محدد](/cells/ar/java/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions

LoadOptions loadOptions = new LoadOptions();

//Set the PaperSize property to appropriate value

loadOptions.setPaperSize(PaperSizeType.PAPER_A_4);

//Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}
### **تمت إضافة طريقة Cell.getCharacters (flag)**
تسمح واجهات برمجة التطبيقات Aspose.Cells بالحصول على كائنات الأحرف في شكل مصفوفة FontSetting باستخدام طريقة Cell.getCharacters. مع هذا الإصدار ، كشف API for Java API Aspose.Cells عن نسخة محملة بشكل زائد من Cell.getCharacters التي يمكن أن تقبل Boolean كمعامل ، مما يشير إلى ما إذا كان يجب تطبيق نمط الجدول على الخلية إذا كانت الخلية جزءًا من ListObject.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access cells collection of the first worksheet

Cells cells = sheet.getCells();

//Access particular cell from a ListObject

//Assuming A1 resides in a ListObject

Cell cell = cells.get("A1");

//Get all Characters objects from the cell

FontSetting[]characters = cell.getCharacters(true);

{{< /highlight >}}
### **تمت إضافة خاصية OleObject.AutoLoad**
كشف Aspose.Cells for Java 8.8.3 خاصية OleObject.AutoLoad التي تسمح بتحديث صورة OleObject إذا تم تغيير محتويات / بيانات الكائن الأساسي. عند تعيين الخاصية المذكورة أعلاه على "true" ، تفرض على تطبيق Excel تحديث صورة OleObject عند تحميل جدول البيانات الناتج.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[تحديث OleObjects تلقائيًا](/cells/ar/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access OleObjectCollection from first worksheet

OleObjectCollection oleObjects = sheet.getOleObjects();

//Access a OleObject from the collection

OleObject oleObject = oleObjects.get(0);

//Set AutoLoad to true

oleObject.setAutoLoad(true);

{{< /highlight >}}
### **تمت إضافة خاصية HTMLLoadOptions.SupportDivTag**
كشف Aspose.Cells for Java 8.8.3 خاصية HTMLLoadOptions.SupportDivTag التي تسمح بتحليل علامات DIV المضمنة في علامات TD أثناء تحميل ملفات / مقتطف HTML في نموذج كائن Aspose.Cells. خاصية النوع المنطقي لها القيمة الافتراضية false.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[دعم علامات DIV الداخلية أثناء تحميل HTML](/cells/ar/java/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

 //Store the HTML snippet in a variable

String export_html = "<html>"

\+ "<body>"

\+ " <table>"

\+ "     <tr>"

\+ "         <td>"

\+ "             <div>This is some Text.</div>"

\+ "             <div>"

\+ "                 <div>"

\+ "                     <span>This is some more Text</span>"

\+ "                 </div>"

\+ "                 <div>"

\+ "                     <span>abc@abc.com</span>"

\+ "                 </div>"

\+ "                 <div>"

\+ "                     <span>1234567890</span>"

\+ "                 </div>"

\+ "                 <div>"

\+ "                     <span>ABC DEF</span>"

\+ "                 </div>"

\+ "             </div>"

\+ "             <div>Generated On May 30, 2016 02:33 PM <br />Time Call Received from Jan 01, 2016 to May 30, 2016</div>"

\+ "         </td>"

\+ "         <td>"

\+ "             <img src='ASpose_logo_100x100.png' />"

\+ "         </td>"

\+ "     </tr>"

\+ " </table>"

\+ "</body>"

\+ "</html>";

//Convert HTML string to InputStream

InputStream stream = new ByteArrayInputStream(export_html.getBytes(StandardCharsets.UTF_8));

//Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions(LoadFormat.HTML);

// Set SupportDivTag property to true

loadOptions.setSupportDivTag(true);

//Create workbook object from the HTML using load options

Workbook book = new Workbook(stream, loadOptions);

//Save the spreadsheet on disc

book.save(dir + "output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **تمت إضافة خاصية HtmlSaveOptions.ExportGridLines**
كشف Aspose.Cells for Java 8.8.3 خاصية HtmlSaveOptions.ExportGridLines التي تسمح بعرض خطوط الشبكة أثناء تصدير جدول البيانات إلى تنسيق HTML. تحتوي خاصية النوع المنطقي على القيمة الافتراضية false ، ومع ذلك ، عند التعيين إلى true ، فإن API يعرض خطوط الشبكة لنطاق البيانات المتاح بتنسيق HTML.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[تقديم خطوط الشبكة إلى HTML](/cells/ar/java/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set ExportGridLines to true

options.setExportGridLines(true);

//Save the result in HTML format

book.save(dir + "output.html", options);

{{< /highlight >}}
### **تمت إضافة خاصية ListObject.Comment**
تسمح واجهات برمجة التطبيقات Aspose.Cells الآن بالحصول على التعليقات وتعيينها لمثيل ListObject. من أجل توفير الميزة المذكورة أعلاه ، كشفت واجهات برمجة التطبيقات Aspose.Cells خاصية ListObject.Comment.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[إضافة تعليقات لـ ListObjects](/cells/ar/java/set-the-comment-of-table-or-list-object/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access first ListObject from the collection of ListObjects

ListObject listObject = sheet.getListObjects().get(0);

//Set comments for the ListObject

listObject.setComment("Comments");

//Save the result on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}
## **إزالة واجهات برمجة التطبيقات**
### **إزالة طريقة Workbook.decrypt**
تم وضع علامة على الممتلكات المذكورة قديمة بعض الوقت. قام هذا الإصدار بإزالته تمامًا من API. يُنصح بتعيين خاصية WorkbookSettings.Password على قيمة خالية من أجل تحقيق نفس الهدف.
