---
title: التغييرات العامة في واجهة برمجة التطبيقات في Aspose.Cells 8.8.0
type: docs
weight: 260
url: /ar/net/public-api-changes-in-aspose-cells-8-8-0/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات لـ Aspose.Cells من الإصدار 8.7.2 إلى 8.8.0 التي قد تكون مثيرة للاهتمام للمطورين. يشمل ليس فقط الطرق الجديدة والمحدثة العامة والصفوف المضافة والمحذوفة وما إلى ذلك، ولكن أيضاً وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **الحصول على مراجع الخلية للاتصال الخارجي**
Aspose.Cells for .NET 8.8.0 تعرض الخصائص الجديدة التالية التي تساعد في استرجاع مراجع الخلية المستهدفة والناتجة للاتصالات الخارجية المخزنة في جدول البيانات.

1. QueryTable.ConnectionId: يحصل على معرف الاتصال من جدول الاستعلام.
1. ExternalConnection.Id: يحصل على معرف الاتصال الخارجي.
1. ListObject.QueryTable: يحصل على الجدول المرتبط بجدول الاستعلام.

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يُرجى مراجعة المقال المفصل حول [العثور على جداول الاستعلام وكائنات القائمة المتعلقة بالاتصالات الخارجية](/cells/ar/net/find-query-tables-and-list-objects-related-to-external-data-connections/)

{{% /alert %}} 
### **تمت إضافة خاصية HTMLLoadOptions.KeepPrecision**
Aspose.Cells for .NET 8.8.0 قد أضافت خاصية HTMLLoadOptions.KeepPrecision للتحكم في تحويل القيم الرقمية الطويلة إلى الدوران العلمي أثناء استيراد ملفات HTML. بشكل افتراضي، يتم تحويل أي قيمة تزيد عن 15 رقمًا إلى الدوران العلمي إذا كانت البيانات تستورد من سلسلة HTML أو ملف. ومع ذلك، يمكن للمستخدمين الآن التحكم في هذا السلوك بمساعدة خاصية HTMLLoadOptions.KeepPrecision. إذا تمت تعيين الخاصية المذكورة إلى true، ستتم استيراد القيم كما هي في المصدر.

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يُرجى مراجعة المقال المفصل حول [تجنب تحويل القيم الرقمية الكبيرة إلى الدوران العلمي](/cells/ar/net/avoid-exponential-notation-of-large-numbers-while-importing-from/)

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

 string html = @" 

<table data-cache=""not-cached"" class=""sortable""> 

   <tbody> 

    <tr> 

     <td class=""even"">9999999999999999</td> 

     <td class=""odd"">10.8%</td> 

    </tr> 

   </tbody> 

</table> 

";

byte[] byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.KeepPrecision = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

Worksheet sheet = workbook.Worksheets[0];

sheet.AutoFitColumns();

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **تمت إضافة خاصية HTMLLoadOptions.DeleteRedundantSpaces**
Aspose.Cells for .NET 8.8.0 has exposed the HTMLLoadOptions.DeleteRedundantSpaces property in order to keep or delete the extra spaces after the line break tag (<br> Tag) while importing the data from the HTML string or file. The HTMLLoadOptions.DeleteRedundantSpaces property has the default value as false that means, all extra spaces will be preserved and imported to the Workbook object, however, when set to true, the API will delete all the redundant spaces coming after the line break tag.

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يُرجى مراجعة المقال المفصل حول [حذف المسافات الزائدة من HTML](/cells/ar/net/delete-redundant-spaces-after-line-break-while-importing/)

{{% /alert %}} 

سيناريو الاستخدام البسيط يبدو كما يلي.

**C#**

{{< highlight csharp >}}

 string html = @" 

<html>

    <body>

        <table>

            <tr>

                <td>

                    <br>    This is sample data 

                    <br>    This is sample data

                    <br>    This is sample data

                </td>

            </tr>

        </table>

    </body>

</html>

";

byte[] byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.DeleteRedundantSpaces = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **تمت إضافة خاصية Style.QuotePrefix**
Aspose.Cells for .NET 8.8.0 تعرض الخاصية Style.QuotePrefix من أجل اكتشاف ما إذا كانت قيمة الخلية تبدأ برمز اقتباس واحد.

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقالة المفصلة حول [الكشف عن علامة اقتباس واحدة في بداية قيمة الخلية](/cells/ar/net/find-if-the-cell-value-starts-with-single-quote-mark/)

{{% /alert %}} 

سيناريو الاستخدام البسيط يبدو كما يلي.

**C#**

{{< highlight csharp >}}

 Workbook book = new Workbook();

Worksheet sheet = book.Worksheets[0];

Cell a1 = sheet.Cells["A1"];

Cell a2 = sheet.Cells["A2"];

a1.PutValue("sample");

a2.PutValue("'sample");

Console.WriteLine("String value of A1: " + a1.StringValue);

Console.WriteLine("String value of A2: " + a2.StringValue);

Style s1 = a1.GetStyle();

Style s2 = a2.GetStyle();

Console.WriteLine("A1 has a quote prefix: " + s1.QuotePrefix);

Console.WriteLine("A2 has a quote prefix: " + s2.QuotePrefix);

{{< /highlight >}}
## **واجهات برمجة التطبيق القديمة**
### **خاصية LoadOptions.ConvertNumericData تم تجاهلها**
Aspose.Cells 8.8.0 قامت بتحديد خاصية LoadOptions.ConvertNumericData كمهجورة. يرجى استخدام الخاصية المقابلة في فئات HTMLLoadOptions أو TxtLoadOptions.
