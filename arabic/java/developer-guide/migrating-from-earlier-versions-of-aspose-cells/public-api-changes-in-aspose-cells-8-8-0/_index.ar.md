---
title: التغييرات العامة في واجهة برمجة التطبيقات في Aspose.Cells 8.8.0
type: docs
weight: 270
url: /ar/java/public-api-changes-in-aspose-cells-8-8-0/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات لـ Aspose.Cells من الإصدار 8.7.2 إلى 8.8.0 التي قد تكون مثيرة للاهتمام للمطورين. يشمل ليس فقط الطرق الجديدة والمحدثة العامة والصفوف المضافة والمحذوفة وما إلى ذلك، ولكن أيضاً وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **الحصول على مراجع الخلية للاتصال الخارجي**
قامت Aspose.Cells for Java 8.8.0 بتعريض الخصائص الجديدة التالية التي تساعد في استرجاع مراجع الخلية المستهدفة والمخرجات للاتصالات الخارجية المخزنة في جدول البيانات. 

1. QueryTable.ConnectionId: يحصل على معرف الاتصال من جدول الاستعلام.
1. ExternalConnection.Id: يحصل على معرف الاتصال الخارجي.
1. ListObject.QueryTable: يحصل على الجدول المرتبط بجدول الاستعلام.

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقال المفصل حول [البحث في جداول الاستعلام وكائنات القائمة المتصلة باتصالات البيانات الخارجية](/cells/ar/java/find-query-tables-and-list-objects-related-to-external-data-connections/)

{{% /alert %}} 
### **تمت إضافة خاصية HTMLLoadOptions.KeepPrecision**
Aspose.Cells for Java 8.8.0 قامت بإضافة خاصية HTMLLoadOptions.KeepPrecision للتحكم في تحويل القيم الرقمية الطويلة إلى الدورية أثناء استيراد ملفات HTML. بشكل افتراضي، يتم تحويل أي قيمة تزيد عن 15 رقمًا للدورية إذا كان البيانات تمت استيرادها من سلسلة HTML أو ملف. ومع ذلك، يمكن للمستخدمين الآن التحكم في هذا السلوك بمساعدة خاصية HTMLLoadOptions.KeepPrecision. إذا تم تعيين الخاصية المذكورة على القيمة true، ستتم استيراد القيم كما هي في المصدر.

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقال المفصل حول [تجنب تحويل القيم الرقمية الكبيرة إلى الدورية](/cells/ar/java/avoid-exponential-notation-of-large-numbers-while-importing-from/)

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

 //Sample Html containing large number with digits greater than 15

String html = "<html>"

		+ "<body>"

		+ "<p>1234567890123456</p>"

		+ "</body>"

		+ "</html>";

//Convert Html to byte array

byte[] byteArray = html.getBytes();

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
Aspose.Cells for Java 8.8.0 has exposed the HTMLLoadOptions.DeleteRedundantSpaces property in order to keep or delete the extra spaces after the line break tag (<br> Tag) while importing the data from the HTML string or file. The HTMLLoadOptions.DeleteRedundantSpaces property has the default value as false that means, all extra spaces will be preserved and imported to the Workbook object, however, when set to true, the API will delete all the redundant spaces coming after the line break tag.

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقال المفصل حول [حذف المسافات الزائدة من HTML](/cells/ar/java/delete-redundant-spaces-after-line-break-while-importing/)

{{% /alert %}} 

سيناريو الاستخدام البسيط يبدو كما يلي. 

**Java**

{{< highlight csharp >}}

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

byte[] byteArray = html.getBytes();

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
Aspose.Cells for Java 8.8.0 قامت بتعريض خاصية Style.QuotePrefix للكشف عما إذا كانت قيمة الخلية تبدأ برمز اقتباس واحد. 

{{% alert color="primary" %}} 

للمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقال المفصل على [الكشف عن علامة اقتباس واحدة في بداية قيمة الخلية](/cells/ar/java/find-if-the-cell-value-starts-with-single-quote-mark/)

{{% /alert %}} 

سيناريو الاستخدام البسيط يبدو كما يلي. 

**Java**

{{< highlight csharp >}}

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
## **واجهات برمجة التطبيق القديمة**
### **خاصية LoadOptions.ConvertNumericData تم تجاهلها**
Aspose.Cells 8.8.0 قامت بتحديد خاصية LoadOptions.ConvertNumericData كمهجورة. يرجى استخدام الخاصية المقابلة في فئات HTMLLoadOptions أو TxtLoadOptions.
{{< app/cells/assistant language="java" >}}
