---
title: API العام التغييرات في Aspose.Cells 8.8.0
type: docs
weight: 270
url: /ar/java/public-api-changes-in-aspose-cells-8-8-0/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.7.2 إلى 8.8.0 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة والمحذوفة وما إلى ذلك ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **احصل على Cell مراجع للتوصيل الخارجي**
 كشف Aspose.Cells for Java 8.8.0 الخصائص الجديدة التالية التي تساعد في استرداد مراجع خلية الهدف والمخرجات للوصلات الخارجية المخزنة في جدول البيانات.

1. QueryTable.ConnectionId: الحصول على معرف الاتصال لجدول الاستعلام.
1. ExternalConnection.Id: يحصل على معرف الاتصال الخارجي.
1. ListObject.QueryTable: الحصول على QueryTable المرتبط.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[البحث عن جداول الاستعلام وكائنات القائمة ذات الصلة باتصالات البيانات الخارجية](/cells/ar/java/find-query-tables-and-list-objects-related-to-external-data-connections/)

{{% /alert %}} 
### **تمت إضافة خاصية HTMLLoadOptions.KeepPrecision المضافة**
أضاف Aspose.Cells for Java 8.8.0 الخاصية HTMLLoadOptions.KeepPrecision للتحكم في تحويل القيم الرقمية الطويلة إلى تدوين أسي أثناء استيراد ملفات HTML. بشكل افتراضي ، يتم تحويل أي قيمة أطول من 15 رقمًا إلى تدوين أسي إذا تم استيراد البيانات من HTML سلسلة أو ملف. ومع ذلك ، يمكن للمستخدمين الآن التحكم في هذا السلوك بمساعدة خاصية HTMLLoadOptions.KeepPrecision. إذا تم تعيين الخاصية المذكورة على true ، فسيتم استيراد القيم كما هي في المصدر.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[ تجنب تحويل القيم الرقمية الكبيرة إلى التدوين الأسي](/cells/ar/java/avoid-exponential-notation-of-large-numbers-while-importing-from/)

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

 //Sample Html containing large number with digits greater than 15

String html = "<html>"

		+ "<body>"

		+ "<p>1234567890123456</p>"

		+ "</body>"

		+ "</html>";

//Convert Html to byte array

byte[]byteArray = html.getBytes();

//Set Html load options and keep precision true

HTMLLoadOptions loadOptions = new HTMLLoadOptions(LoadFormat.HTML);

loadOptions.setKeepPrecision(true);

//Convert byte array into stream

java.io.ByteArrayInputStream stream = new java.io.ByteArrayInputStream(byteArray);

//Create workbook from stream with Html load options

Workbook workbook = new Workbook(stream, loadOptions);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Auto fit the sheet columns

worksheet.autoFitColumns();

//Save the workbook

workbook.save(dataDir + "output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **تمت إضافة خاصية HTMLLoadOptions.DeleteRedundantSpaces**
كشف Aspose.Cells for Java 8.8.0 الخاصية HTMLLoadOptions.DeleteRedundantSpaces من أجل الاحتفاظ بالمسافات الزائدة أو حذفها بعد علامة فاصل السطر (<br>علامة) أثناء استيراد البيانات من HTML سلسلة أو ملف. تحتوي الخاصية HTMLLoadOptions.DeleteRedundantSpaces على القيمة الافتراضية على أنها false مما يعني أنه سيتم الاحتفاظ بجميع المسافات الإضافية واستيرادها إلى كائن Workbook ، ومع ذلك ، عند التعيين على true ، فإن API سيحذف جميع المسافات الزائدة التي تأتي بعد علامة فاصل السطر.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[حذف المسافات الزائدة من HTML](/cells/ar/java/delete-redundant-spaces-after-line-break-while-importing/)

{{% /alert %}} 

 يبدو سيناريو الاستخدام البسيط على النحو التالي.

**Java**

{{< highlight "csharp" >}}

 //Sample Html containing redundant spaces after <br> tag

String html = "<html>"

		+ "<body>"

			+ "<table>"

				+ "<tr>"

					+ "<td>"

						+ "<br>    This is sample data"

						+ "<br>    This is sample data"

						+ "<br>    This is sample data"

					+ "</td>"

				+ "</tr>"

			+ "</table>"

		+ "</body>"

	+ "</html>";

//Convert Html to byte array

byte[]byteArray = html.getBytes();

//Set Html load options and keep precision true

HTMLLoadOptions loadOptions = new HTMLLoadOptions(LoadFormat.HTML);

loadOptions.setDeleteRedundantSpaces(true);

//Convert byte array into stream

java.io.ByteArrayInputStream stream = new java.io.ByteArrayInputStream(byteArray);

//Create workbook from stream with Html load options

Workbook workbook = new Workbook(stream, loadOptions);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Auto fit the sheet columns

worksheet.autoFitColumns();

//Save the workbook

workbook.save(dataDir + "output-" + loadOptions.getDeleteRedundantSpaces() + ".xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **تمت إضافة خاصية Style.QuotePrefix**
 كشف Aspose.Cells for Java 8.8.0 الخاصية Style.QuotePrefix لاكتشاف ما إذا كانت قيمة الخلية تبدأ برمز اقتباس واحد.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[كشف عرض أسعار مفرد في بداية قيمة Cell](/cells/ar/java/find-if-the-cell-value-starts-with-single-quote-mark/)

{{% /alert %}} 

 يبدو سيناريو الاستخدام البسيط على النحو التالي.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of workbook

Workbook workbook = new Workbook();

//Access first worksheet from the collection

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cells A1 and A2

Cell a1 = worksheet.getCells().get("A1");

Cell a2 = worksheet.getCells().get("A2");

//Add simple text to cell A1 and text with quote prefix to cell A2

a1.putValue("sample");

a2.putValue("'sample");

//Print their string values, A1 and A2 both are same

System.out.println("String value of A1: " + a1.getStringValue());

System.out.println("String value of A2: " + a2.getStringValue());

//Access styles of cells A1 and A2

Style s1 = a1.getStyle();

Style s2 = a2.getStyle();

System.out.println();

//Check if A1 and A2 has a quote prefix

System.out.println("A1 has a quote prefix: " + s1.getQuotePrefix());

System.out.println("A2 has a quote prefix: " + s2.getQuotePrefix());

{{< /highlight >}}
## **واجهات برمجة التطبيقات التي عفا عليها الزمن**
### **خاصية LoadOptions.ConvertNumericData القديمة**
قام Aspose.Cells 8.8.0 بوضع علامة على الخاصية LoadOptions.ConvertNumericData على أنها قديمة. الرجاء استخدام الخاصية المقابلة من فئات HTMLLoadOptions أو TxtLoadOptions.
