---
title: تغييرات واجهة برمجة التطبيقات العمومية في Aspose.Cells 8.8.3
type: docs
weight: 290
url: /ar/net/public-api-changes-in-aspose-cells-8-8-3/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات الخاصة ب Aspose.Cells من الإصدار 8.8.2 إلى 8.8.3 التي قد تكون ذات أهمية لمطوري الوحدات/التطبيقات. ويشمل هذا ليس فقط الطرق العامة الجديدة والمحدثة والصفوف المضافة والمحذوفة الخ، ولكن أيضاً وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **دعم الضوابط النشطة**
Aspose.Cells for .NET 8.8.3 قد قام بتعريض طريقة AddActiveXControl التي تسمح بإضافة تحكم نشط ActiveX إلى مجموعة الأشكال. الطريقة المذكورة تتطلب 7 معلمات لتحديد نوع التحكم، موقع وضع التحكم، وحجم التحكم. يمكن تحديد النوع باستخدام تعداد ControlType مع القيم الممكنة التالية.

1. ControlType.CheckBox
1. ControlType.ComboBox
1. ControlType.CommandButton
1. ControlType.Image
1. ControlType.Label
1. ControlType.ListBox
1. ControlType.RadioButton
1. ControlType.ScrollBar
1. ControlType.SpinButton
1. ControlType.TextBox
1. ControlType.ToggleButton
1. ControlType.Unknown

{{% alert color="primary" %}} 

يرجى الرجوع إلى المقالة المفصلة حول [إضافة أدوات تحكم ActiveX إلى ورق العمل](/cells/ar/net/add-activex-controls-using-aspose-cells/) لمزيد من التفاصيل حول هذه الميزة.

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

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
Aspose.Cells for .NET 8.8.3 يسمح بتعيين حجم ورقة الطباعة الافتراضي من إعدادات الطابعة الافتراضية أثناء استخدام طريقة LoadOptions.SetPaperSize المعرضة حديثًا كما هو موضح أدناه. يرجى ملاحظة أن المعلمة الداخلية للطريقة المذكورة هي القيمة من تعداد PaperSizeType التي تحتوي على الأحجام القياسية المحددة مسبقًا لأحجام الورق.

{{% alert color="primary" %}} 

يرجى الرجوع إلى المقالة المفصلة حول [تحميل جداول بيانات بحجم الورق المحدد](/cells/ar/net/load-workbook-with-specified-printer-paper-size/) لمزيد من التفاصيل حول هذه الميزة.

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions

var loadOptions = new LoadOptions();

// Set the PaperSize property to appropriate value

loadOptions.SetPaperSize(PaperSizeType.PaperA4);

// Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}


### **تمت إضافة الطريقة Cell.GetCharacters(flag)**
تسمح واجهات برمجة التطبيقات في Aspose.Cells بالحصول على كائنات الأحرف في شكل مجموعة من FontSetting عن طريق استخدام طريقة Cell.GetCharacters. مع هذا الإصدار، قد قامت واجهات برمجة التطبيقات Aspose.Cells for .NET بتعريض إصدارًا معتمدًا من طريقة Cell.GetCharacters الذي يمكن أن يقبل نوع بوليان كمعامل، مشيرًا إلى ما إذا كان يجب تطبيق نمط الجدول على الخلية إذا كانت الخلية جزءًا من ListObject.

**C#**

{{< highlight csharp >}}

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
قامت Aspose.Cells for .NET 8.8.3 بتعريض خاصية OleObject.AutoLoad التي تسمح بتحديث صورة OleObject إذا تم تغيير محتويات/بيانات الكائن الأساسي. بوضع الخاصية المذكورة على True، تجبر تطبيق Excel على تحديث صورة OleObject عند تحميل جدول بيانات الناتج.

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقال المفصل حول [تحديث أوتوماتيكي لكائنات Ole](/cells/ar/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

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
قامت Aspose.Cells for .NET 8.8.3 بتعريض خاصية HTMLLoadOptions.SupportDivTag التي تسمح بتحليل علامات DIV المضمنة في علامات TD أثناء تحميل ملفات HTML/قصاصات في نموذج الكائن Aspose.Cells. تحتوي الخاصية من نوع بوليان على القيمة الافتراضية False.

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقال المفصل حول [دعم علامات DIV الداخلية أثناء تحميل HTML](/cells/ar/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

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
قامت Aspose.Cells for .NET 8.8.3 بتعريض خاصية HtmlSaveOptions.ExportGridLines التي تسمح بتقديم خطوط الشبكة أثناء تصدير الجدول النشط إلى تنسيق HTML. الخاصية من نوع بوليان مع القيمة الافتراضية False، ومع ذلك، عندما يتم تعيينها على True، تقوم واجهة البرمجة بتقديم خطوط الشبكة لنطاق البيانات المتاح في تنسيق HTML.

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقال المفصل حول [تقديم خطوط الشبكة إلى HTML](/cells/ar/net/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

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
تُسمح واجهات برمجة التطبيقات الخاصة بـ Aspose.Cells الآن بالحصول على التعليقات لنموذج ListObject وتعيينها. ولتوفير هذه الميزة المذكورة، فإن واجهات برمجة التطبيقات الخاصة بـ Aspose.Cells قامت بتتاح خاصية ListObject.Comment.

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقال المفصل حول [إضافة تعليقات لـ ListObjects](/cells/ar/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

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


### **تمت إضافة الخاصية GridWeb.SessionStorePath**
أصبح Aspose.Cells.GridWeb for .NET 8.8.3 يعرض خاصية SessionStorePath التي تسمح بالحصول على المسار أو تعيينه لتخزين الجلسة عندما يكون وضع الجلسة هو ViewState. تحصل الخاصية المذكورة أعلاه أو تعين المسار النسبي إلى دليل تطبيق الويب الحالي.

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقال المفصل حول [تحديد مسار لملفات الجلسة المؤقتة](/cells/ar/net/specify-the-path-where-gridweb-stores-temporary-session-files/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.
## **تمت إزالة واجهات برمجة التطبيقات**
### **تمت إزالة أسلوب Workbook.Decrypt.**
تمت وضع علامة على الخاصية المذكورة كبالغة قبل فترة. تمت إزالتها تمامًا من واجهة برمجة التطبيقات العامة في هذا الإصدار. يُفضل تعيين خاصية WorkbookSettings.Password إلى قيمة null من أجل تحقيق نفس الهدف.
