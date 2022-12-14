---
title: عام API التغييرات في Aspose.Cells 8.8.3
type: docs
weight: 290
url: /ar/net/public-api-changes-in-aspose-cells-8-8-3/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.8.2 إلى 8.8.3 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة والمحذوفة وما إلى ذلك ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **دعم عناصر تحكم ActiveX**
كشف Aspose.Cells for .NET 8.8.3 طريقة AddActiveXControl التي تسمح بإضافة عنصر تحكم ActiveX إلى ShapeCollection. تتطلب الطريقة المذكورة أعلاه 7 معلمات لتحديد نوع عنصر التحكم والموقع لوضع التحكم وحجم عنصر التحكم. يمكن تحديد النوع باستخدام تعداد ControlType مع القيم المحتملة التالية.

1. نوع التحكم
1. نوع التحكم
1. ControlType.CommandButton
1. نوع التحكم
1. نوع التحكم
1. نوع التحكم
1. نوع التحكم. زر راديو
1. نوع التحكم. شريط التمرير
1. نوع التحكم
1. ControlType.TextBox
1. نوع التحكم
1. نوع التحكم. غير معروف

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[إضافة عناصر تحكم ActiveX إلى ورقة العمل](/cells/ar/net/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook

var book = new Workbook();

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Add Toggle Button ActiveX Control to the ShapeCollection at specified location

var shape = sheet.Shapes.AddActiveXControl(ControlType.ToggleButton, 4, 0, 4, 0, 100, 30);

// Access the ActiveX Control object and set its linked cell property

ActiveXControl control = shape.ActiveXControl;

control.LinkedCell = "A1";

// Save the result on disc

book.Save(dir + "output.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}


### **تمت إضافة طريقة LoadOptions.SetPaperSize**
Aspose.Cells for .NET 8.8.3 يسمح بتعيين حجم ورق الطباعة الافتراضي من إعداد الطابعة الافتراضي أثناء استخدام طريقة LoadOptions.SetPaperSize المكشوفة حديثًا كما هو موضح أدناه. يرجى ملاحظة أن معلمة الإدخال للطريقة المذكورة أعلاه هي القيمة من تعداد PaperSizeType الذي يحتوي على أحجام الورق المحددة مسبقًا.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[قم بتحميل جداول بيانات بحجم ورق محدد](/cells/ar/net/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions

var loadOptions = new LoadOptions();

// Set the PaperSize property to appropriate value

loadOptions.SetPaperSize(PaperSizeType.PaperA4);

// Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}


### **تمت إضافة Cell. طريقة الحصول على أحرف (علم)**
تسمح واجهات برمجة التطبيقات Aspose.Cells بالحصول على كائنات الأحرف في شكل مصفوفة FontSetting باستخدام طريقة Cell.GetCharacters. مع هذا الإصدار ، كشف Aspose.Cells for .NET API إصدارًا زائد التحميل من Cell.GetCharacters الذي يمكنه قبول Boolean كمعامل ، مما يشير إلى ما إذا كان يجب تطبيق نمط الجدول على الخلية إذا كانت الخلية جزءًا من ListObject.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access cells collection of the first worksheet

var cells = sheet.Cells;

// Access particular cell from a ListObject

// Assuming A1 resides in a ListObject

var cell = cells["A1"];

// Get all Characters objects from the cell

var characters = cell.GetCharacters(true);

{{< /highlight >}}


### **تمت إضافة خاصية OleObject.AutoLoad**
كشف Aspose.Cells for .NET 8.8.3 خاصية OleObject.AutoLoad التي تسمح بتحديث صورة OleObject إذا تم تغيير محتويات / بيانات الكائن الأساسي. عند تعيين الخاصية المذكورة أعلاه على "true" ، تفرض على تطبيق Excel تحديث صورة OleObject عند تحميل جدول البيانات الناتج.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[تحديث OleObjects تلقائيًا](/cells/ar/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access OleObjectCollection from first worksheet

var oleObjects = sheet.OleObjects;

// Access a OleObject from the collection

var oleObject = oleObjects[0];

// Set AutoLoad to true

oleObject.AutoLoad = true;

{{< /highlight >}}


### **تمت إضافة خاصية HTMLLoadOptions.SupportDivTag**
كشف Aspose.Cells for .NET 8.8.3 خاصية HTMLLoadOptions.SupportDivTag التي تسمح بتحليل علامات DIV المضمنة في علامات TD أثناء تحميل ملفات / مقتطف HTML في نموذج كائن Aspose.Cells. خاصية النوع المنطقي لها القيمة الافتراضية false.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[دعم علامات DIV الداخلية أثناء تحميل HTML](/cells/ar/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 // Store the HTML snippet in a variable

var export_html = @"

<html>

<body>

    <table>

        <tr>

            <td>

                <div>This is some Text.</div>

                <div>

                    <div>

                        <span>This is some more Text</span>

                    </div>

                    <div>

                        <span>abc@abc.com</span>

                    </div>

                    <div>

                        <span>1234567890</span>

                    </div>

                    <div>

                        <span>ABC DEF</span>

                    </div>

                </div>

                <div>Generated On May 30, 2016 02:33 PM <br />Time Call Received from Jan 01, 2016 to May 30, 2016</div>

            </td>

            <td>

                <img src='ASpose_logo_100x100.png' />

            </td>

        </tr>

    </table>

</body>

</html>";

// Create an instance of MemoryStream and load the contents of the HTML

using (var stream = new MemoryStream(System.Text.Encoding.UTF8.GetBytes(export_html)))

{

    // Create an instance of HTMLLoadOptions

    var loadOptions = new HTMLLoadOptions(LoadFormat.Html);

    // Set SupportDivTag property to true

    loadOptions.SupportDivTag = true;

    // Create workbook object from the HTML using load options

    var book = new Workbook(stream, loadOptions);

    // Auto fit rows and columns of first worksheet

    var sheet = book.Worksheets[0];

    sheet.AutoFitRows();

    sheet.AutoFitColumns();

    // Save the spreadsheet on disc

    book.Save(dir + "output.xlsx", SaveFormat.Xlsx);

}

{{< /highlight >}}


### **تمت إضافة خاصية HtmlSaveOptions.ExportGridLines**
كشف Aspose.Cells for .NET 8.8.3 خاصية HtmlSaveOptions.ExportGridLines التي تسمح بعرض خطوط الشبكة أثناء تصدير جدول البيانات إلى تنسيق HTML. تحتوي خاصية Boolean type على القيمة الافتراضية false ، ومع ذلك ، عند التعيين على true ، فإن API يعرض خطوط الشبكة لنطاق البيانات المتاح بتنسيق HTML.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[عرض خطوط الشبكة إلى HTML](/cells/ar/net/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook and load existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Create an instance of HtmlSaveOptions

var options = new HtmlSaveOptions();

// Set ExportGridLines to true

options.ExportGridLines = true;

// Save the result in HTML format

book.Save(dir + "output.html", options);

{{< /highlight >}}


### **تمت إضافة خاصية ListObject.Comment**
تسمح واجهات برمجة التطبيقات Aspose.Cells الآن بالحصول على التعليقات وتعيينها لمثيل ListObject. من أجل توفير الميزة المذكورة أعلاه ، كشفت واجهات برمجة التطبيقات Aspose.Cells خاصية ListObject.Comment.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[إضافة تعليقات لـ ListObjects](/cells/ar/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook and load existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access first ListObject from the collection of ListObjects

var listObject = sheet.ListObjects[0];

// Set comments for the ListObject

listObject.Comment = "Comments";

// Save the result on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}


### **تمت إضافة خاصية GridWeb.SessionStorePath**
كشف Aspose.Cells.GridWeb for .NET 8.8.3 خاصية SessionStorePath التي تسمح بالحصول على مسار مخزن الجلسة أو تعيينه عندما يكون وضع الجلسة هو ViewState. تحصل الخاصية المذكورة أعلاه على المسار النسبي أو تعينه إلى الدليل الأساسي لتطبيق الويب الحالي.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[حدد مسار ملفات الجلسة المؤقتة](/cells/ar/net/specify-the-path-where-gridweb-stores-temporary-session-files/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.
## **إزالة واجهات برمجة التطبيقات**
### **تمت إزالة المصنف. طريقة فك التشفير**
تم وضع علامة على الممتلكات المذكورة قديمة بعض الوقت. قام هذا الإصدار بإزالته تمامًا من API. يُنصح بتعيين خاصية WorkbookSettings.Password على قيمة خالية من أجل تحقيق نفس الهدف.
