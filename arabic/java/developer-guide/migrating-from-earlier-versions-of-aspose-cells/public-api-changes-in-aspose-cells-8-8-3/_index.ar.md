---
title: تغييرات واجهة برمجة التطبيقات العمومية في Aspose.Cells 8.8.3
type: docs
weight: 300
url: /ar/java/public-api-changes-in-aspose-cells-8-8-3/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات الخاصة ب Aspose.Cells من الإصدار 8.8.2 إلى 8.8.3 التي قد تكون ذات أهمية لمطوري الوحدات/التطبيقات. ويشمل هذا ليس فقط الطرق العامة الجديدة والمحدثة والصفوف المضافة والمحذوفة الخ، ولكن أيضاً وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **دعم الضوابط النشطة**
Aspose.Cells for Java 8.8.3 أظهرت أسلوب addActiveXControl الذي يسمح بإضافة ضوابط ActiveX إلى مجموعة Shapes. يتطلب الأسلوب المذكور 7 معاملات لتحديد نوع الضوابط ومكان وضع الضوابط وحجم الضوابط. يمكن تحديد النوع باستخدام تعداد ControlType باحتمالات قيم ممكنة التالية.

1. ControlType.CHECK_BOX
1. ControlType.COMBO_BOX
1. ControlType.COMMAND_BUTTON
1. ControlType.IMAGE
1. ControlType.LABEL
1. ControlType.LIST_BOX
1. ControlType.RADIO_BUTTON
1. ControlType.SCROLL_BAR
1. ControlType.SPIN_BUTTON
1. ControlType.TEXT_BOX
1. ControlType.TOGGLE_BUTTON
1. ControlType.UNKNOWN

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقال المفصل حول [إضافة عناصر تحكم ActiveX إلى ورق العمل](/cells/ar/java/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

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
إصدار Aspose.Cells for Java 8.8.3 يسمح بتعيين حجم ورق الطباعة الافتراضي من إعدادات الطابعة الافتراضية أثناء استخدام طريقة LoadOptions.setPaperSize المكشوفة حديثًا كالمظهر أدناه. يرجى ملاحظة أن المعلمة الداخلية للطريقة المذكورة أعلاه هي قيمة من التعداد PaperSizeType التي تحتوي على الأحجام القياسية المحددة مسبقاً.

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقال المفصل حول [تحميل جداول البيانات بحجم ورق محدد](/cells/ar/java/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions

LoadOptions loadOptions = new LoadOptions();

//Set the PaperSize property to appropriate value

loadOptions.setPaperSize(PaperSizeType.PAPER_A_4);

//Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}
### **تمت إضافة طريقة Cell.getCharacters(flag)**
تسمح واجهات برمجة التطبيقات Aspose.Cells بالحصول على كائنات الأحرف في شكل مصفوفة FontSetting عن طريق استخدام طريقة Cell.getCharacters. مع هذا الإصدار، فإن الـ API Aspose.Cells for Java قد قام بتعريض نسخة معظمة من الطريقة Cell.getCharacters التي يمكن أن تقبل بوليان كمعلمة، مشيرة إلى ما إذا كان يجب تطبيق نمط الجدول على الخلية إذا كانت الخلية جزءًا من ListObject.

**Java**

{{< highlight csharp >}}

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

FontSetting[] characters = cell.getCharacters(true);

{{< /highlight >}}
### **تمت إضافة خاصية OleObject.AutoLoad**
 Aspose.Cells for Java 8.8.3 قد قامت بتعريض الخاصية OleObject.AutoLoad التي تسمح بتحديث صورة OleObject إذا تم تغيير محتويات/بيانات الكائن الأساسي. عند ضبط الخاصية المذكورة أعلاه على القيمة true، تضطر تطبيق Excel إلى تحديث صورة OleObject عند تحميل جدول البيانات الناتج.

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقال المفصل حول [تحديث عناصر OleObjects تلقائيًا](/cells/ar/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

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
 Aspose.Cells for Java 8.8.3 قد قامت بتعريض الخاصية HTMLLoadOptions.SupportDivTag التي تسمح بتحليل الوسوم DIV المضمنة في وسوم TD أثناء تحميل ملفات/مقتطفات HTML في نموذج الكائن Aspose.Cells. تحتوي الخاصية من النوع البولياني على القيمة الافتراضية false.

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقال المفصل حول [دعم وسوم DIV الداخلية أثناء تحميل HTML](/cells/ar/java/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

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
قدمت Aspose.Cells for Java 8.8.3 خاصية HtmlSaveOptions.ExportGridLines التي تسمح بتقديم خطوط الشبكة أثناء تصدير جدول البيانات إلى تنسيق HTML. الخاصية من نوع Boolean لها القيمة الافتراضية false، ومع ذلك، عند ضبطها على true، تقوم الواجهة البرمجية بإظهار خطوط الشبكة لنطاق البيانات المتاحة في تنسيق HTML.

{{% alert color="primary" %}} 

للمزيد من التفاصيل حول هذه الميزة، يُرجى مراجعة المقال المفصل في [رسم خطوط الشبكة إلى الـ HTML](/cells/ar/java/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

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
تُسمح واجهات برمجة التطبيقات الخاصة بـ Aspose.Cells الآن بالحصول على التعليقات لنموذج ListObject وتعيينها. ولتوفير هذه الميزة المذكورة، فإن واجهات برمجة التطبيقات الخاصة بـ Aspose.Cells قامت بتتاح خاصية ListObject.Comment.

{{% alert color="primary" %}} 

للمزيد من التفاصيل حول هذه الميزة، يُرجى مراجعة المقال المفصل حول [إضافة تعليقات لـ ListObjects](/cells/ar/java/set-the-comment-of-table-or-list-object/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

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
## **تمت إزالة واجهات برمجة التطبيقات**
### **تمت إزالة طريقة Workbook.decrypt**
تمت وضع علامة على الخاصية المذكورة كبالغة قبل فترة. تمت إزالتها تمامًا من واجهة برمجة التطبيقات العامة في هذا الإصدار. يُفضل تعيين خاصية WorkbookSettings.Password إلى قيمة null من أجل تحقيق نفس الهدف.
