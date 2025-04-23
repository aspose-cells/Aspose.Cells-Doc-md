---
title: تغييرات واجهة برمجة التطبيقات العامة في Aspose.Cells 8.6.3
type: docs
weight: 220
url: /ar/net/public-api-changes-in-aspose-cells-8-6-3/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات العامة لـ Aspose.Cells من الإصدار 8.6.2 إلى 8.6.3 التي قد تكون مهمة لمطوري الوحدات / التطبيقات. يشمل هذا ليس فقط الطرق العامة الجديدة والمحدثة ، والفئات المضافة ، ولكن أيضاً وصفًا لأي تغييرات في السلوك في خلفية Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **دعم تحليل HTML أثناء استيراد البيانات**
يُظهر هذا الإصدار من واجهة برمجة التطبيقات (API) التي تُعرضها Aspose.Cells for .NET خاصية ImportTableOptions.IsHtmlString التي توجه واجهة البرمجة (API) لتحليل علامات HTML أثناء استيراد البيانات على الورقة العمل وتعيين النتيجة المحللة كقيمة للخلية المقابلة. لاحظ، توفر واجهات برمجة التطبيقات (APIs) في Aspose.Cells بالفعل خاصية Cell.HtmlString لأداء هذه المهمة لخلية واحدة، ولكن أثناء استيراد البيانات بالجملة مثل من DataTable، فإن خاصية ImportTableOptions.IsHtmlString (عند تعيينها إلى true) تحاول تحليل جميع علامات HTML المدعومة وتعيين النتائج المحللة للخلايا المقابلة.

فيما يلي سيناريو الاستخدام الأبسط.

**C#**

{{< highlight csharp >}}

 //create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.IsHtmlString = true;

//Import data from DataTable while passing instance of ImportTableOptions

cells.ImportData(table, 0, 0, importOptions);

{{< /highlight >}}


### **أضيفت طريقة Workbook.CreateBuiltinStyle**
بواسطة الاصدار Aspose.Cells for .NET 8.6.3 فقد تم عرض طريقة Workbook.CreateBuiltinStyle التي يمكن استخدامها لإنشاء كائن من فئة Style الذي يتوافق مع أحد الـ [أنماط المضمنة المقدمة من تطبيق Excel](/cells/ar/net/using-built-in-styles/). طريقة Workbook.CreateBuiltinStyle تقبل ثابت من تصنيف BuiltinStyleType.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Create a built-in style of type Title

var style = book.CreateBuiltinStyle(BuiltinStyleType.Title);

{{< /highlight >}}


### **أضيفت طريقة Cells.ImportGridView**
بواسطة الاصدار Aspose.Cells for .NET 8.6.3 فقد تم عرض نسخة مكدسة من الطريقة Cells.ImportGridView التي يمكن الآن قبول مثيل لـ ImportTableOptions لتقديم مزيد من التحكم في عملية الاستيراد.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

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
في إشارة إلى التعزيزات المذكورة أعلاه، تم تعريض الإصدار الأخير من واجهة برمجة التطبيقات Aspose.Cells for .NET أيضًا خاصية ImportTableOptions.ConvertGridStyle. تسمح هذه الخاصية من النوع Boolean للمطورين بالتحكم في مظهر البيانات المستوردة، حيث تشير ضبط خاصية ImportTableOptions.ConvertGridStyle لتكون صحيحة إلى أن الواجهة البرمجية ستطبق نمط GridView على الخلايا حيث تم استيراد البيانات.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

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
تم تعريض الخاصية LoadDataOption.OnlyVisibleWorksheet في Aspose.Cells for .NET 8.6.3 والتي عند تعيينها على true ستؤثر على آلية التحميل لـ Aspose.Cells for .NET API، ونتيجة لذلك ستتم تحميل الورقات العمل المرئية فقط من جدول بيانات معطى. يُرجى مراجعة [المقالة التفصيلية](/cells/ar/net/different-ways-to-open-files/) حول هذا الموضوع.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

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
## **واجهات برمجة التطبيق القديمة**
### **طريقة Worksheet.CopyConditionalFormatting تم وضعها في حجب**
كبديل عن طريقة Worksheet.CopyConditionalFormatting، يُنصح باستخدام احدى طرق Cells.CopyRows أو Range.Copy.
### **تفضل استخدام خاصية Cells.LastCell كبديل عن الخاصية Cells.End.**
يرجى استخدام خاصية Cells.LastCell كبديل لخاصية Cells.End.
{{< app/cells/assistant language="csharp" >}}
