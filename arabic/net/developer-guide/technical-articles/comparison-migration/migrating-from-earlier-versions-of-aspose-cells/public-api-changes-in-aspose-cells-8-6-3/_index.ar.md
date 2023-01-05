---
title: عام API التغييرات في Aspose.Cells 8.6.3
type: docs
weight: 220
url: /ar/net/public-api-changes-in-aspose-cells-8-6-3/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.6.2 إلى 8.6.3 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة ، ولكن أيضًا وصف أي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **دعم HTML التحليل أثناء استيراد البيانات**
كشف هذا الإصدار من Aspose.Cells for .NET API الخاصية ImportTableOptions.IsHtmlString التي توجه API لتحليل علامات HTML أثناء استيراد البيانات إلى ورقة العمل وتعيين النتيجة المحللة كقيمة خلية. يرجى ملاحظة أن واجهات برمجة التطبيقات Aspose.Cells توفر بالفعل Cell.HtmlString لأداء هذه المهمة لخلية واحدة ، ومع ذلك ، أثناء استيراد البيانات المجمعة مثل من DataTable ، تحاول خاصية ImportTableOptions.IsHtmlString (عند تعيينها إلى true) تحليل كل العناصر المدعومة HTML علامات تمييز وتحديد النتائج التي تم تحليلها للخانات المقابلة.

هنا هو أبسط سيناريو استخدام.

**C#**

{{< highlight "csharp" >}}

 //create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.IsHtmlString = true;

//Import data from DataTable while passing instance of ImportTableOptions

cells.ImportData(table, 0, 0, importOptions);

{{< /highlight >}}


### **أسلوب Workbook.CreateBuiltinStyle المضافة**
 كشف Aspose.Cells for .NET 8.6.3 عن طريقة Workbook.CreateBuiltinStyle التي يمكن استخدامها لإنشاء كائن من فئة Style يتوافق مع أحد[الأنماط المضمنة التي يوفرها تطبيق Excel](/cells/ar/net/using-built-in-styles/)يقبل أسلوب Workbook.CreateBuiltinStyle ثابتًا من التعداد BuiltinStyleType. يرجى ملاحظة أنه مع الإصدارات السابقة من واجهات برمجة التطبيقات Aspose.Cells ، يمكن إنجاز نفس المهمة عبر طريقة StyleCollection.CreateBuiltinStyle ولكن نظرًا لأن الإصدارات الأخيرة من واجهات برمجة التطبيقات Aspose.Cells أزالت فئة StyleCollection ، وبالتالي يمكن اعتبار طريقة Workbook التي تم عرضها مؤخرًا. تحقيق نفس الشيء.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Create a built-in style of type Title

var style = book.CreateBuiltinStyle(BuiltinStyleType.Title);

{{< /highlight >}}


### **الطريقة Cells. تمت إضافة ImportGridView**
كشف Aspose.Cells for .NET 8.6.3 عن نسخة محملة بشكل زائد من Cells.ImportGridView يمكنه الآن قبول نسخة من ImportTableOptions لمنح المزيد من التحكم في عملية الاستيراد.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Retrieve the Cells collection of first Worksheet in Workbook

var cells = book.Worksheets[0].Cells;

//create an instance of ImportTableOptions & set its various properties

var importOptions = new ImportTableOptions();

importOptions.IsHtmlString = true;

importOptions.IsFieldNameShown = true;

//Import data from GridView while passing instance of ImportTableOptions

cells.ImportGridView(gridView, 0, 0, importOptions);

{{< /highlight >}}


### **تمت إضافة خاصية ImportTableOptions.ConvertGridStyle**
بالإشارة إلى التحسينات المذكورة أعلاه ، فإن أحدث إصدار من Aspose.Cells for .NET API قد كشف أيضًا عن خاصية ImportTableOptions.ConvertGridStyle. تسمح خاصية النوع المنطقي هذه للمطورين بالتحكم في مظهر البيانات المستوردة ، حيث يشير تعيين خاصية ImportTableOptions.ConvertGridStyle إلى true أن API سيطبق نمط GridView على الخلايا التي تم استيراد البيانات إليها.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Retrieve the Cells collection of first Worksheet in Workbook

var cells = book.Worksheets[0].Cells;

//create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set ConvertGridStyle property to true

importOptions.ConvertGridStyle = true;



//Import data from GridView while passing instance of ImportTableOptions

cells.ImportGridView(gridView, 0, 0, importOptions);

{{< /highlight >}}


### **تمت إضافة خاصية LoadDataOption.OnlyVisibleWorksheet**
 كشف Aspose.Cells for .NET 8.6.3 خاصية LoadDataOption.OnlyVisibleWorksheet التي عند ضبطها على true ستؤثر على آلية التحميل Aspose.Cells for .NET API ، ونتيجة لذلك سيتم تحميل أوراق العمل المرئية فقط من جدول بيانات معين. رجاء تاكد من[مقالة مفصلة](/cells/ar/net/different-ways-to-open-files/) حول هذا الموضوع.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of LoadDataOption

var loadDataOptions = new LoadDataOption();

//Set OnlyVisibleWorksheet property to true

loadDataOptions.OnlyVisibleWorksheet = true;

//Create an instance of LoadOptions

var loadOptions = new LoadOptions();

//Set LoadDataOptions property to the instance of LoadDataOption created earlier

loadOptions.LoadDataOptions = loadDataOptions;



//Create an instance of Workbook & load an existing spreadsheet

//while passing the instance of LoadOptions created earlier

var book = new Workbook(inputFilePath, loadOptions);

{{< /highlight >}}
## **واجهات برمجة التطبيقات التي عفا عليها الزمن**
### **طريقة Worksheet.CopyConditionalFormatting مهملة**
كبديل لطريقة Worksheet.CopyConditionalFormatting ، يُنصح باستخدام أي من أساليب Cells.CopyRows أو Range.Copy.
### **الملكية Cells. انتهى متقادم**
من فضلك استخدم Cells.LastCell الملكية كبديل للملكية Cells.End.
