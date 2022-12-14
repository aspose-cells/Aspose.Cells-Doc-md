---
title: API العام التغييرات في Aspose.Cells 8.8.0
type: docs
weight: 260
url: /ar/net/public-api-changes-in-aspose-cells-8-8-0/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.7.2 إلى 8.8.0 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة والمحذوفة وما إلى ذلك ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **احصل على Cell مراجع للتوصيل الخارجي**
كشف Aspose.Cells for .NET 8.8.0 الخصائص الجديدة التالية التي تساعد في استرداد مراجع خلية الهدف والمخرجات للوصلات الخارجية المخزنة في جدول البيانات.

1. QueryTable.ConnectionId: الحصول على معرف الاتصال لجدول الاستعلام.
1. ExternalConnection.Id: يحصل على معرف الاتصال الخارجي.
1. ListObject.QueryTable: الحصول على QueryTable المرتبط.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[البحث عن جداول الاستعلام وكائنات القائمة ذات الصلة باتصالات البيانات الخارجية](/cells/ar/net/find-query-tables-and-list-objects-related-to-external-data-connections/)

{{% /alert %}} 
### **تمت إضافة خاصية HTMLLoadOptions.KeepPrecision المضافة**
أضاف Aspose.Cells for .NET 8.8.0 الخاصية HTMLLoadOptions.KeepPrecision للتحكم في تحويل القيم الرقمية الطويلة إلى تدوين أسي أثناء استيراد ملفات HTML. بشكل افتراضي ، يتم تحويل أي قيمة أطول من 15 رقمًا إلى تدوين أسي إذا كان يتم استيراد البيانات من سلسلة أو ملف HTML. ومع ذلك ، يمكن للمستخدمين الآن التحكم في هذا السلوك بمساعدة خاصية HTMLLoadOptions.KeepPrecision. إذا تم تعيين الخاصية المذكورة على true ، فسيتم استيراد القيم كما هي في المصدر.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[ تجنب تحويل القيم الرقمية الكبيرة إلى التدوين الأسي](/cells/ar/net/avoid-exponential-notation-of-large-numbers-while-importing-from/)

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

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

byte[]byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.KeepPrecision = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

Worksheet sheet = workbook.Worksheets[0];

sheet.AutoFitColumns();

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **تمت إضافة خاصية HTMLLoadOptions.DeleteRedundantSpaces**
كشف Aspose.Cells for .NET 8.8.0 الخاصية HTMLLoadOptions.DeleteRedundantSpaces من أجل الاحتفاظ بالمسافات الزائدة أو حذفها بعد علامة فاصل السطر (<br>علامة) أثناء استيراد البيانات من سلسلة أو ملف HTML. تحتوي الخاصية HTMLLoadOptions.DeleteRedundantSpaces على القيمة الافتراضية على أنها false مما يعني أنه سيتم الاحتفاظ بجميع المسافات الإضافية واستيرادها إلى كائن Workbook ، ومع ذلك ، عند التعيين على true ، فإن API سيحذف جميع المسافات الزائدة التي تأتي بعد علامة فاصل السطر.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[احذف المسافات الزائدة من HTML](/cells/ar/net/delete-redundant-spaces-after-line-break-while-importing/)

{{% /alert %}} 

يبدو سيناريو الاستخدام البسيط على النحو التالي.

**C#**

{{< highlight "csharp" >}}

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

byte[]byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.DeleteRedundantSpaces = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **تمت إضافة خاصية Style.QuotePrefix**
كشف Aspose.Cells for .NET 8.8.0 الخاصية Style.QuotePrefix لاكتشاف ما إذا كانت قيمة الخلية تبدأ برمز اقتباس واحد.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[كشف عرض أسعار مفرد في بداية قيمة Cell](/cells/ar/net/find-if-the-cell-value-starts-with-single-quote-mark/)

{{% /alert %}} 

يبدو سيناريو الاستخدام البسيط على النحو التالي.

**C#**

{{< highlight "csharp" >}}

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
## **واجهات برمجة التطبيقات التي عفا عليها الزمن**
### **خاصية LoadOptions.ConvertNumericData القديمة**
قام Aspose.Cells 8.8.0 بوضع علامة على الخاصية LoadOptions.ConvertNumericData على أنها قديمة. الرجاء استخدام الخاصية المقابلة من فئات HTMLLoadOptions أو TxtLoadOptions.
